from __main__ import app
from flask import jsonify, request
import os
from dotenv import load_dotenv
load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
metadata = [('authorization', f'Bearer {bearer_token}')]

from sqlalchemy import create_engine, select, MetaData, Table, and_
username = os.getenv('CSSI_DATABASE_USERNAME')
password = os.getenv('CSSI_DATABASE_PASSWORD')

engine = create_engine("postgresql+psycopg2://" + username + ":" + password + "@tts.rd.unr.edu/postgres")
metadata = MetaData()
table = Table(
    'sensor_data', 
    metadata,
    autoload_with=engine
)

# data route
@app.route('/data', methods=['GET'])
def data():
    try:
        response_object = {'status': 'success'}
        if request.method == 'GET':
            stmt = select(
                table.columns.time,
                table.columns.payload,
                table.columns.metadata
            ).limit(40)

            connection = engine.connect()
            results = connection.execute(stmt).fetchall()
            response_object['data'] = []
            for row in results:
                response_object['data'].append({
                      'timestamp': row.time,
                      'payload': row.payload,
                      'metadata': row.metadata
                })
            
            return jsonify(response_object)
    except:
        response_object = {'status': 'failure'}
        return jsonify(response_object)