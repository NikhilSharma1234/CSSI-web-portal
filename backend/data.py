#from __main__ import app
from collections import defaultdict
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from sqlalchemy import func, select, desc
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

# Used for data visualization - Button Periods
@data_endpoint.route('/dataButton', methods=['POST'])
def dataButton():
    try:
        data = request.get_json()
        
        selected_sensor_data = data.get('data', [])
        sensor_ids = list(selected_sensor_data.keys())
        predefined_period = data.get('period')
        selected_aggregation = data.get('aggregation')
        payload_types = set()

        for payload_list in selected_sensor_data.values():
            if not isinstance(payload_list, list) or not all(isinstance(payload, str) for payload in payload_list):
                return jsonify({'status': 'fail', 'message': 'Payload types must be strings in a list'}), 400
            payload_types.update(payload_list)

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
            'ALL': None
        }

        if predefined_period not in period_mapping:
            return jsonify({'status': 'fail', 'message': 'Invalid period selected'}), 400

        start_time = datetime.min.replace(tzinfo=timezone.utc) if predefined_period == 'ALL' else now - period_mapping[predefined_period]
        mapping = get_sensor_mapping()

        derivation_map = {item['payload_value']: item for item in mapping}
        
        stmt = select(
            table.columns.dev_eui,
            table.columns.time,
            table.columns.payload,
            table.columns.metadata
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
        for row in results:
            dev_eui = row.dev_eui
            timestamp = row.time
            payload = row.payload
            metadata = row.metadata

            for payload_type in payload_types:
                if payload_type in payload or payload_type in metadata:
                    if payload_type in payload:
                        data_point = payload[payload_type]
                    else:
                        data_point = metadata[payload_type]
                    
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
                        'timestamp': timestamp,
                        'payload_type': payload_type,
                        'value': data_point,
                    })

        if selected_aggregation != 'None':
            interval_mapping = {
                '1 Hour': timedelta(hours=1),
                '1 Day': timedelta(days=1),
                '7 Days': timedelta(days=7),
                '1 Month': timedelta(days=30),
                '6 Months': timedelta(days=180)
            }

            if selected_aggregation not in interval_mapping:
                return jsonify({'status': 'fail', 'message': 'Invalid aggregation option'}), 400

            aggregation_interval = interval_mapping[selected_aggregation]
            
            # Update: Nested defaultdict to store lists for each payload_type within each (dev_eui, interval_start) key
            aggregated_data = defaultdict(lambda: defaultdict(list))

            for item in response_data:
                dev_eui = item['dev_eui']
                timestamp = item['timestamp']
                if item['value'] == 'NULL': 
                    continue
                data_point = float(item['value'])
                payload_type = item['payload_type']  # Get the payload type

                if aggregation_interval == timedelta(days=1): 
                    interval_start = timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
                elif aggregation_interval == timedelta(weeks=1): 
                    interval_start = timestamp - timedelta(days=timestamp.weekday())
                    interval_start = interval_start.replace(hour=0, minute=0, second=0, microsecond=0)
                elif aggregation_interval.days >= 30: 
                    interval_start = timestamp.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                else:
                    seconds = int(aggregation_interval.total_seconds())
                    rounded_seconds = (timestamp.minute * 60 + timestamp.second) % seconds
                    interval_start = timestamp - timedelta(seconds=rounded_seconds, microseconds=timestamp.microsecond)

                aggregated_data[(dev_eui, interval_start)][payload_type].append(data_point)

            response_data = [
                {
                    'dev_eui': dev_eui,
                    'timestamp': interval_start.isoformat(),
                    'payload_type': payload_type,
                    'value': sum(values) / len(values) 
                }
                for (dev_eui, interval_start), payload_dict in aggregated_data.items()
                for payload_type, values in payload_dict.items()
            ]

        return jsonify({'status': 'success', 'data': response_data})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'status': 'failure', 'message': str(e)}), 500

# Used for data visualization - Date Time Picker
@data_endpoint.route('/data', methods=['POST'])
def data():
    try:
        data = request.get_json()
        # Extract sensor data, sensor ids, payload types, and time range from request
        selected_sensor_data = data.get('data', {})
        sensor_ids = list(selected_sensor_data.keys())
        payload_types = set()

        # Ensure payload types are valid
        for payload_list in selected_sensor_data.values():
            if not isinstance(payload_list, list) or not all(isinstance(payload, str) for payload in payload_list):
                return jsonify({'status': 'fail', 'message': 'Payload types must be strings in a list'}), 400
            payload_types.update(payload_list)

        # Ensure both sensor IDs and payload types are provided
        if not sensor_ids or not payload_types:
            return jsonify({'status': 'fail', 'message': 'Sensor IDs and payload types are required'}), 400

        # Handle time range
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if not start_time or not end_time:
            return jsonify({'status': 'fail', 'message': 'Start time and end time are required'}), 400

        # Convert start_time and end_time to datetime objects
        try:
            start_time = datetime.fromisoformat(start_time).astimezone(timezone.utc)
            end_time = datetime.fromisoformat(end_time).astimezone(timezone.utc)
        except ValueError:
            return jsonify({'status': 'fail', 'message': 'Invalid time format. Please use ISO 8601 format.'}), 400

        mapping = get_sensor_mapping()
        derivation_map = {item['payload_value']: item for item in mapping}

        # Build the SQL query to fetch data within the time range
        stmt = select(
            table.columns.dev_eui,
            table.columns.time,
            table.columns.payload
        ).where(
            and_(
                table.columns.dev_eui.in_(sensor_ids),
                table.columns.time >= start_time,
                table.columns.time <= end_time
            )
        )

        with engine.connect() as connection:
            results = connection.execute(stmt).fetchall()

        response_data = []

        # Process each row of data
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
                            try:
                                locals_dict = {'value': data_point}
                                data_point = eval(derivation, {}, locals_dict)
                            except Exception as e:
                                print(f"Error in derivation for {dev_eui} on {timestamp}: {e}")

                    # Store the processed data
                    response_data.append({
                        'dev_eui': dev_eui,
                        'timestamp': timestamp.isoformat(),
                        'payload_type': payload_type,
                        'value': data_point,
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
            stmt = select(table.columns.dev_eui, table.columns.payload, table.columns.metadata, table.columns.time).where(
                and_(
                    table.columns.dev_eui == device_id,
                    ~table.columns.payload.has_key('error')  # Exclude rows with an 'error' key in payload
                )
            ).order_by(
                desc(table.columns.time)
            ).limit(1)

            with engine.connect() as connection:
                result = connection.execute(stmt).first()
            if result:
                payload = result.payload
                metadata = result.metadata
                dev_eui = result.dev_eui
                capabilities[dev_eui] = {
                    "lastReading": {
                        "time": result.time
                    }
                }
                for key in payload.keys():
                    if key in payload_to_type.keys():
                        capabilities[dev_eui]["type"] = payload_to_type[key]
                    if key in payload_to_display_name.keys():
                        capabilities[dev_eui]["lastReading"][payload_to_display_name[key]] = payload[key]
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
                # For any information needed from the metadata
                for key in metadata.keys():
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
        print(capabilities)
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
                
                if payload_value in row.payload or payload_value in row.metadata:
                    # Apply derivation if it exists, else use the value directly in either payload or metadata
                    if payload_value in row.payload:
                        value = row.payload[payload_value]
                    else:
                        value = row.metadata[payload_value]

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
