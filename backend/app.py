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

import user
import application
import applications
import data

app.register_blueprint(user.user_endpoint)
app.register_blueprint(data.data_endpoint)
app.register_blueprint(application.application_endpoint)
app.register_blueprint(applications.applications_endpoint)

# health route
@app.route('/health', methods=['GET'])
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify(False)
    except:
        return jsonify(True)


if __name__ == '__main__':
    app.run()