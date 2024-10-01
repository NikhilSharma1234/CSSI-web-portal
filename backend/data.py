from __main__ import app
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from sqlalchemy import func, select
import os
from dotenv import load_dotenv
import grpc
import generated.ttn.lorawan.v3.application_services_pb2_grpc as application_services_pb2_grpc
import generated.ttn.lorawan.v3.application_pb2 as application_pb2
import generated.ttn.lorawan.v3.identifiers_pb2 as identifiers_pb2

import generated.ttn.lorawan.v3.user_services_pb2_grpc as user_services_pb2_grpc
import generated.ttn.lorawan.v3.user_pb2 as user_pb2
import google.protobuf.field_mask_pb2 as field_mask_pb2

from flask import Blueprint

load_dotenv()

data_endpoint = Blueprint('data', __name__)

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

@data_endpoint.route('/data', methods=['POST'])
def data():
    try:
        data = request.get_json()
        
        sensor_ids = data.get('sensor_ids', [])
        payload_type = data.get('payload_type')
        predefined_period = data.get('period')
        
        if not sensor_ids or not payload_type or not predefined_period:
            return jsonify({'status': 'fail', 'message': 'Sensor IDs, payload type, and period are required'}), 400
        
        now = datetime.now(timezone.utc)
        
        period_mapping = {
            '1H': timedelta(hours=1),
            '24H': timedelta(hours=24),
            '7D': timedelta(days=7),
            '14D': timedelta(days=14),
            '30D': timedelta(days=30),
            '6M': timedelta(days=180),
            '1Y': timedelta(days=365),
            'ALL': 'None'
        }
        
        if predefined_period not in period_mapping:
            return jsonify({'status': 'fail', 'message': 'Invalid period selected'}), 400
        
        if predefined_period == 'ALL':
            start_time = datetime.min.replace(tzinfo=timezone.utc)
        else:
            start_time = now - period_mapping[predefined_period]
        
        stmt = select(
            table.columns.dev_eui,
            table.columns.time,
            table.columns.payload
        ).where(
            and_(
                table.columns.dev_eui.in_(sensor_ids),
                table.columns.time >= start_time,
                table.columns.time <= now
            )
        )
        
        with engine.connect() as connection:
            results = connection.execute(stmt).fetchall()
        
        response_data = [
            {
                'dev_eui': row.dev_eui,
                'timestamp': row.time.isoformat(),
                payload_type: row.payload.get(payload_type),
                'item_number': counter
            }
            for counter, row in enumerate(results)
            if payload_type in row.payload
        ]
        
        return jsonify({'status': 'success', 'data': response_data})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'status': 'failure', 'message': str(e)}), 500
    
@data_endpoint.route('/export', methods=['POST'])
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
                    'conduct_SOIL': None,
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
                    'conduct_SOIL': row.payload['conduct_SOIL'],
                    'item_number': counter
                })

        return jsonify(response_object)
    except Exception as e:
        print(e)
        response_object = {'status': 'failure'}
        return jsonify(response_object), 500