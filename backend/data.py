#from __main__ import app
from collections import defaultdict
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from sqlalchemy import func, select
import os
from dotenv import load_dotenv
from helper import get_sensor_mapping
from flask import Blueprint

load_dotenv()

data_endpoint = Blueprint('data', __name__)

from sqlalchemy import create_engine, select, MetaData, Table, and_
username = os.getenv('CSSI_DATABASE_USERNAME')
password = os.getenv('CSSI_DATABASE_PASSWORD')
host = os.getenv('CSSI_DATABASE_HOST','tts.rd.unr.edu')
table = os.getenv('CSSI_DATABASE_TABLE','postgres')

engine = create_engine("postgresql+psycopg2://" + username + ":" + password + f"@{host}/{table}")
metadata = MetaData()
table = Table(
    'sensor_data', 
    metadata,
    autoload_with=engine
)

mapping = [
    {
        "type": "Temperature",
        "display_name": "Temperature",
        "payload_value": "temperature",
        "brand": "laird",
        "model": "rs1xx",
        "unit": "celsius",
        "derivation": None,
        "description": "Temperature from laird sensor",
        "sortable": True,
        "width": 90,
    },
    {
        "type": "Temperature",
        "display_name": "Temperature Red",
        "payload_value": "Temp_Red",
        "brand": "dragino",
        "model": "D20,22,23",
        "unit": "celsius",
        "derivation": None,
        "description": "Temperature from the red probe",
        "sortable": True,
        "width": 90,
    },
    {
        "type": "Temperature",
        "display_name": "Temperature Black",
        "payload_value": "Temp_Black",
        "brand": "dragino",
        "model": "D20,22,23",
        "unit": "celsius",
        "derivation": None,
        "description": "Temperature from the black probe",
        "sortable": True,
        "width": 90,
    },
    {
        "type": "Temperature",
        "display_name": "Temperature White",
        "payload_value": "Temp_White",
        "brand": "dragino",
        "model": "D20,22,23",
        "unit": "celsius",
        "derivation": None,
        "description": "Temperature from the white probe",
        "sortable": True,
        "width": 90,
    },
    {
        "type": "Soil Moisture",
        "display_name": "Soil Moisture",
        "payload_value": "water_SOIL",
        "brand": "dragino",
        "model": "LSE01",
        "unit": "percent",
        "derivation": None,
        "description": "Soil moisture from the sensor",
        "sortable": True,
        "width": 90,
    },
    {
        "type": "Soil Moisture",
        "display_name": "Soil Conductivity",
        "payload_value": "conduct_SOIL",
        "brand": "dragino",
        "model": "LSE01",
        "unit": "microsiemens per centimeter",
        "derivation": None,
        "description": "Soil conductivity from the sensor",
        "sortable": True,
        "width": 120,
    },
    {
        "type": "Soil Moisture",
        "display_name": "Soil Temperature",
        "payload_value": "temp_SOIL",
        "brand": "dragino",
        "model": "LSE01",
        "unit": "celsius",
        "derivation": None,
        "description": "Soil temperature from the sensor",
        "sortable": True,
        "width": 120,
    },
    {
        "type": "Soil Moisture",
        "display_name": "Battery Life",
        "payload_value": "Bat",
        "brand": "dragino",
        "model": "LSE01",
        "unit": "float",
        "derivation": "value*20",
        "description": "Battery life from the sensor",
        "sortable": True,
        "width": 90,
    },
    {
        "type": "Temperature",
        "display_name": "Battery Life",
        "payload_value": "BatV",
        "brand": "dragino",
        "model": "D20,22,23",
        "unit": "float",
        "derivation": "value*20",
        "description": "Battery life from the sensor",
        "sortable": True,
        "width": 90,
    },
    {
        "type": "Temperature",
        "display_name": "Battery Life",
        "payload_value": "batteryCapacity",
        "brand": "laird",
        "model": "rs1xx",
        "unit": "string",
        "derivation": "int(str(value).replace('%', '').split('-')[1])",
        "description": "Battery life from the sensor",
        "sortable": True,
        "width": 90,
    }    
]

payload_to_display_name = {
    'temperature': 'Temperature',
    'Temp_Red': 'Temperature Red',
    'Temp_Black': 'Temperature Black',
    'Temp_White': 'Temperature White',
    'water_SOIL': 'Soil Moisture',
    'conduct_SOIL': 'Soil Conductivity',
    'temp_SOIL': 'Soil Temperature',
    'Bat': 'Battery Life',
    'BatV': 'Battery Life',
    'batteryCapacity': 'Battery Life'
}

payload_to_type = {
    'temperature': 'Temperature',
    'Temp_Red': 'Temperature',
    'Temp_Black': 'Temperature',
    'Temp_White': 'Temperature',
    'water_SOIL': 'Soil Moisture',
    'conduct_SOIL': 'Soil Moisture',
    'temp_SOIL': 'Soil Moisture',
    'Bat': 'Soil Moisture',
    'BatV': 'Temperature',
    'batteryCapacity': 'Temperature'
}

derivation_map = {item['payload_value']: item for item in mapping}

# Used for data visualization
@data_endpoint.route('/data', methods=['POST'])
def data():
    try:
        data = request.get_json()
        
        selected_sensor_data = data.get('data', [])
        sensor_ids = list(selected_sensor_data.keys())
        predefined_period = data.get('period')
        payload_types = set()

        for payload_list in selected_sensor_data.values():
            if not isinstance(payload_list, list) or not all(isinstance(payload, str) for payload in payload_list):
                return jsonify({'status': 'fail', 'message': 'Payload types must be strings in a list'}), 400
            payload_types.update(payload_list)

        # Validate that we have at least one payload type
        if not payload_types:
            return jsonify({'status': 'fail', 'message': 'No valid payload types provided'}), 400
        
        if not sensor_ids or not payload_types or not predefined_period:
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

        mapping = get_sensor_mapping()

        derivation_map = {item['payload_value']: item for item in mapping}
        
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

        response_data = []

        # Process each result to apply derivations immediately
        for row in results:
            dev_eui = row.dev_eui
            timestamp = row.time
            payload = row.payload

            for payload_type in payload_types:
                if payload_type in payload:
                    data_point = payload[payload_type]
                    
                    # Apply derivation if it exists
                    if payload_type in derivation_map:
                        derivation = derivation_map[payload_type]['derivation']
                        if derivation:
                            # Safely evaluate the derivation expression
                            try:
                                locals_dict = {'value': data_point}
                                data_point = eval(derivation, {}, locals_dict)
                            except Exception as e:
                                print(f"Error in derivation for {dev_eui} on {timestamp}: {e}")

                    # Store the processed data immediately
                    response_data.append({
                        'dev_eui': dev_eui,
                        'timestamp': timestamp.isoformat(),
                        'payload_type': payload_type,
                        'value': data_point,
                        'item_number': len(response_data) + 1
                    })

        # Now handle aggregation for specific periods
        if predefined_period in ['1Y', '6M', 'ALL']:
            # Initialize a dictionary to hold readings for each dev_eui and 10-day period
            aggregated_data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

            # Populate aggregated data
            for item in response_data:
                dev_eui = item['dev_eui']
                timestamp = item['timestamp']
                if item['value'] == 'NULL': 
                    continue
                data_point = float(item['value'])
                payload_type = item['payload_type']  # Get the payload type

                # Calculate which 10-day interval the timestamp belongs to
                interval_start = (datetime.fromisoformat(timestamp) - timedelta(days=datetime.fromisoformat(timestamp).day % 1)).replace(hour=0, minute=0, second=0, microsecond=0)
                aggregated_data[dev_eui][payload_type][interval_start].append(data_point)

            # Calculate averages for each dev_eui, payload_type, and each interval
            response_data = []
            for dev_eui, payload_types in aggregated_data.items():
                for payload_type, intervals in payload_types.items():
                    for interval_start, data_points in intervals.items():
                        average_data = sum(data_points) / len(data_points)
                        response_data.append({
                            'dev_eui': dev_eui,
                            'timestamp': interval_start.isoformat(),
                            'payload_type': payload_type,  # Include payload_type in the response
                            'value': average_data,
                            'item_number': len(response_data) + 1
                        })

        return jsonify({'status': 'success', 'data': response_data})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'status': 'failure', 'message': str(e)}), 500
    

# Used to get the type of device
@data_endpoint.route('/devices', methods=['POST'])
def get_device_type():
    try:
        data = request.get_json()
        sensor_ids = data.get('sensor_ids', [])

        if not sensor_ids:
            return jsonify({'status': 'fail', 'message': 'Sensor IDs are required'}), 400

        capabilities = {}
        mapping = get_sensor_mapping()
        payload_to_display_name = {item["payload_value"]: item["display_name"] for item in mapping}
        payload_to_type = {item["payload_value"]: item["type"] for item in mapping}

        for device_id in sensor_ids:
            stmt = select(table.columns.dev_eui, table.columns.payload).where(
                and_(
                    table.columns.dev_eui == device_id,
                    ~table.columns.payload.has_key('error')  # Exclude rows with an 'error' key in payload
                )
            )

            with engine.connect() as connection:
                result = connection.execute(stmt).first()
            if result:
                payload = result.payload
                dev_eui = result.dev_eui
                capabilities[dev_eui] = {}
                for key in payload.keys():
                    if key in payload_to_type.keys():
                        capabilities[dev_eui]["type"] = payload_to_type[key]
                    if key in payload_to_display_name.keys():
                        if "readings" in capabilities[dev_eui].keys():
                            capabilities[dev_eui]["readings"].append({
                                "payload_value": key,
                                "display_name": payload_to_display_name[key]
                            })
                        else:
                            capabilities[dev_eui]["readings"] = [{
                                "payload_value": key,
                                "display_name": payload_to_display_name[key]
                            }]

        return jsonify({'status': 'success', 'capabilities': capabilities})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'status': 'failure', 'message': str(e)}), 500

# Used for data export feature
@data_endpoint.route('/export', methods=['POST'])
def export_data():
    try:
        response_object = {'status': 'success'}
        data = request.get_json()
        
        selected_devices = data.get('devices', [])
        start_time = data.get('startTime')
        end_time = data.get('endTime')

        mapping = get_sensor_mapping()
        
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
        
        # Prepare metadata mapping for response
        mapping_info = {
            entry['payload_value']: {
                'display_name': entry['display_name'],
                'unit': entry['unit'],
                'description': entry['description'],
                'sortable': entry['sortable'],
                'width': entry['width']
            }
            for entry in mapping
        }
        
        for counter, row in enumerate(results):
            data_entry = {
                'dev_eui': row.dev_eui,
                'timestamp': row.time,
                'item_number': counter
            }
            
            for entry in mapping:
                payload_value = entry['payload_value']
                
                if payload_value in row.payload:
                    # Apply derivation if it exists, else use the value directly
                    value = row.payload[payload_value]
                    if entry['derivation']:
                        # Safely evaluate the derivation with 'value' in local context
                        locals_dict = {'value': value}
                        value = eval(entry['derivation'], {}, locals_dict)
                        value = round(value, 2)
                    
                    # Add field to data entry using payload_value as the key
                    data_entry[payload_value] = value
            
            response_object['data'].append(data_entry)

        # Add the mapping info to the response
        response_object['mapping'] = mapping_info
        
        return jsonify(response_object)
    
    except Exception as e:
        print(e)
        response_object = {'status': 'failure'}
        return jsonify(response_object), 500