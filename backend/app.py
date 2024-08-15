from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv
import grpc
import generated.ttn.lorawan.v3.application_services_pb2 as application_services_pb2
import generated.ttn.lorawan.v3.application_services_pb2_grpc as application_services_pb2_grpc
import generated.ttn.lorawan.v3.application_pb2 as application_pb2
import generated.ttn.lorawan.v3.application_pb2_grpc as application_pb2_grpc
import generated.ttn.lorawan.v3.identifiers_pb2 as identifiers_pb2

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'))
    return conn

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# user route
@app.route('/user', methods=['GET', 'POST'])
def user():
    conn = get_db_connection()
    cur = conn.cursor()
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        name = post_data.get('name')
        email = post_data.get('email')
        cur.execute('INSERT INTO users (name, email)'
                    'VALUES (%s, %s)',
                    (name, email))
        conn.commit()
        cur.close()
        conn.close()
        response_object['message'] = 'User added!'
    else:
        # GET request (currently returns all users)
        cur.execute('SELECT * FROM users;')
        users = cur.fetchall()
        cur.close()
        conn.close()
        response_object['users'] = users
        response_object['message'] = 'Users returned!'
    return jsonify(response_object)

# health route
@app.route('/health', methods=['GET'])
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify(False)
    except:
        return jsonify(True)
    
# applciations route
@app.route('/applications', methods=['GET'])
def applications():
        response_object = {'status': 'success'}

        # with open('cert.crt', 'rb') as c:
        #     cert = c.read()
        # with open('cert.key', 'rb') as k:
        #     key = k.read()

        # credentials = grpc.ssl_channel_credentials(
        #     certificate_chain = cert,
        #     private_key = key
        # )

        bearer_token = os.getenv('BEARER_TOKEN')
        metadata = [('authorization', f'Bearer {bearer_token}')]
        
        collaborator = identifiers_pb2.OrganizationOrUserIdentifiers(user_ids = identifiers_pb2.UserIdentifiers(user_id='nikhil'))
        with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
            stub = application_services_pb2_grpc.ApplicationRegistryStub(channel)
            response = stub.List(application_pb2.ListApplicationsRequest(collaborator = collaborator) , metadata=metadata)
        # print(response.applications[0].ids.application_id)
        response_object['applications'] = response.applications[0].ids.application_id
        return jsonify(response_object)


if __name__ == '__main__':
    app.run()