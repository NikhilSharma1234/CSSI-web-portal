from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv
import grpc
import generated.ttn.lorawan.v3.application_services_pb2_grpc as application_services_pb2_grpc
import generated.ttn.lorawan.v3.application_pb2 as application_pb2
import generated.ttn.lorawan.v3.identifiers_pb2 as identifiers_pb2

import generated.ttn.lorawan.v3.user_services_pb2_grpc as user_services_pb2_grpc
import generated.ttn.lorawan.v3.user_pb2 as user_pb2
import google.protobuf.field_mask_pb2 as field_mask_pb2

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
metadata = [('authorization', f'Bearer {bearer_token}')]

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
@app.route('/user', methods=['GET', 'POST', 'PUT'])
def user():
    try:
        response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json()
            name = post_data.get('name')
            email = post_data.get('email')
            user_id = post_data.get('user_id')
            password = post_data.get('password')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = user_services_pb2_grpc.UserRegistryStub(channel)
                user = user_pb2.User(
                    ids=identifiers_pb2.UserIdentifiers(user_id=user_id, email=email),
                    name=name,
                    primary_email_address=email,
                    password=password
                )
                response = stub.Create(user_pb2.CreateUserRequest(user=user) , metadata=metadata)
            response_object['user'] = response.ids.user_id
            response_object['message'] = 'User added!'
        elif request.method == 'GET':
            user_id = request.args.get('user_id')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = user_services_pb2_grpc.UserRegistryStub(channel)
                response = stub.Get(
                    user_pb2.GetUserRequest(
                        user_ids=identifiers_pb2.UserIdentifiers(user_id=user_id),
                        field_mask=field_mask_pb2.FieldMask(paths=['name', 'primary_email_address'])
                    ),
                    metadata=metadata
                )
            response_object['user'] = {
                'name': response.name,
                'email': response.primary_email_address
            }
        elif request.method == 'PUT':
            put_data = request.get_json()
            user_id = put_data.get('user_id')
            name = put_data.get('name')
            email = put_data.get('email')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = user_services_pb2_grpc.UserRegistryStub(channel)
                user = user_pb2.User(ids=identifiers_pb2.UserIdentifiers(user_id=user_id), name=name, primary_email_address=email)
                response = stub.Update(user_pb2.UpdateUserRequest(user=user, field_mask=field_mask_pb2.FieldMask(paths=['name', 'primary_email_address'])), metadata=metadata)
            response_object['user'] = {
                'name': response.name,
                'email': response.primary_email_address
            }
        return jsonify(response_object)
    except:
        response_object = {'status': 'failure'}
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
    try:
        response_object = {'status': 'success'}
        if request.method == 'GET':
            user_id = request.args.get('user_id')
            collaborator = identifiers_pb2.OrganizationOrUserIdentifiers(user_ids = identifiers_pb2.UserIdentifiers(user_id=user_id))
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = application_services_pb2_grpc.ApplicationRegistryStub(channel)
                response = stub.List(application_pb2.ListApplicationsRequest(collaborator = collaborator, field_mask=field_mask_pb2.FieldMask(paths=['name', 'description'])), metadata=metadata)
            response_object['applications'] = []
            for application in response.applications:
                response_object['applications'].append({
                    'id': application.ids.application_id,
                    'name': application.name,
                    'description': application.description
                })
                
            return jsonify(response_object)
    except:
        response_object = {'status': 'failure'}
        return jsonify(response_object)
        

# applciations route
@app.route('/application', methods=['GET', 'POST', 'PUT'])
def application():
    try:
        response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json()
            app_id = post_data.get('app_id')
            name = post_data.get('name')
            description = post_data.get('description')
            user_id = post_data.get('user_id')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = application_services_pb2_grpc.ApplicationRegistryStub(channel)
                application = application_pb2.Application(ids=identifiers_pb2.ApplicationIdentifiers(application_id=app_id), name=name, description=description)
                response = stub.Create(application_pb2.CreateApplicationRequest(application=application, collaborator=identifiers_pb2.OrganizationOrUserIdentifiers(user_ids=identifiers_pb2.UserIdentifiers(user_id=user_id))), metadata=metadata)
            response_object['application'] = response.ids.application_id
            return jsonify(response_object)
        elif request.method == 'GET':
            app_id = request.args.get('app_id')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = application_services_pb2_grpc.ApplicationRegistryStub(channel)
                response = stub.Get(
                    application_pb2.GetApplicationRequest(
                        application_ids=identifiers_pb2.ApplicationIdentifiers(application_id=app_id),
                        field_mask=field_mask_pb2.FieldMask(paths=['name', 'description'])
                    ),
                    metadata=metadata
                )
            response_object['application'] = {
                'name': response.name,
                'description': response.description
            }
            return jsonify(response_object)
        elif request.method == 'PUT':
            return "ECHO: PUT\n"
    except:
        response_object = {'status': 'failure'}
        return jsonify(response_object)


if __name__ == '__main__':
    app.run()