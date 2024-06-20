from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv
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


# sanity check route
@app.route('/user', methods=['GET', 'POST'])
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        name = post_data.get('name')
        email = post_data.get('email')
        password = post_data.get('password')
        cur.execute('INSERT INTO users (name, email, password)'
                    'VALUES (%s, %s, %s)',
                    (name, email, password))
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


if __name__ == '__main__':
    app.run()