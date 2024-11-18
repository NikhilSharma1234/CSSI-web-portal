from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

import data

app.register_blueprint(data.data_endpoint)

# health route
@app.route('/health', methods=['GET'])
def health():
    try:
        return jsonify(False)
    except:
        return jsonify(True)


if __name__ == '__main__':
    app.run(port=5001)