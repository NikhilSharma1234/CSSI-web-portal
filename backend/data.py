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
    
@app.route('/export', methods=['POST'])
def export_data():
    try:
        response_object = {'status': 'success'}
        data = request.get_json()

        selected_devices = data.get('devices', [])
        start_time = data.get('startTime')
        end_time = data.get('endTime')

        stmt = select(
            table.columns.dev_eui,
            table.columns.time,
            table.columns.payload,
            table.columns.metadata
        ).where(
            and_(
                table.columns.dev_eui.in_(selected_devices),
                table.columns.time >= start_time,
                table.columns.time <= end_time
            )
        )

        connection = engine.connect()
        results = connection.execute(stmt).fetchall()
        response_object['data'] = []
        for counter, row in enumerate(results):
            if 'temperature' in row.payload:
                response_object['data'].append({
                    'dev_eui': row.dev_eui,
                    'batteryCapacity': row.payload['batteryCapacity'],
                    'timestamp': row.time,
                    'temperature': row.payload['temperature'],
                    'temp_SOIL': None,
                    'water_SOIL': None,
                    'item_number': counter,
                })
            elif 'temp_SOIL' in row.payload:
                response_object['data'].append({
                    'dev_eui': row.dev_eui,
                    'timestamp': row.time,
                    'batteryCapacity': row.payload['Bat'] * 20,
                    'temperature': None,
                    'temp_SOIL': row.payload['temp_SOIL'],
                    'water_SOIL': row.payload['water_SOIL'],
                    'item_number': counter
                })

        return jsonify(response_object)
    except Exception as e:
        print(e)
        response_object = {'status': 'failure'}
        return jsonify(response_object), 500