#from __main__ import app
from collections import defaultdict
from io import StringIO
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from sqlalchemy import func, select, desc
import os
from dotenv import load_dotenv
from helper import get_sensor_mapping
from flask import Blueprint
import pandas as pd
import boto3
from botocore.client import Config
import asyncio
import httpx
import json
import re
from copy import deepcopy

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
        # Convert data to DataFrame
        df = pd.DataFrame(response_data)

        # Convert timestamp to string format
        df["timestamp"] = df["timestamp"].astype(str)

        # Save CSV to a buffer
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # S3 bucket details
        s3_bucket_name = "csv-bucket-nikhil"
        s3_file_name = f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        # Upload to S3
        s3_client = boto3.client("s3",
            config=Config(signature_version='s3v4'))
        
        s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=s3_file_name,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        presigned_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{s3_file_name}"

        return jsonify({'status': 'success', 'data': response_data, 'CSV_URL': presigned_url})

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
            table.columns.payload,
            table.columns.metadata
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
        return jsonify({'status': 'success', 'capabilities': capabilities})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'status': 'failure', 'message': str(e)}), 500
    
# Used to get the type of device
@data_endpoint.route('/devicesCSV', methods=['POST'])
def get_device_type_CSV():
    try:
        data = request.get_json()
        sensor_ids = data.get('sensor_ids', [])
        sensorWithLocation = data.get('sensorsWithLocation', [])

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
        print(sensorWithLocation)
        merged = {}

        for dev_eui, cap_data in capabilities.items():
            merged[dev_eui] = deepcopy(cap_data)  # Avoid modifying original

            # Add device_id and location if available
            sensor_info = sensorWithLocation.get(dev_eui, {})
            merged[dev_eui]["device_id"] = sensor_info.get("device_id", None)

            if "location" in sensor_info:
                merged[dev_eui]["location"] = sensor_info["location"]

    
        reading_keys = set()
        for sensor in merged.values():
            if 'lastReading' in sensor:
                reading_keys.update(sensor['lastReading'].keys())
        reading_keys.discard('time')
        sorted_reading_keys = sorted(reading_keys)

        # Step 2: Build rows for the DataFrame
        rows = []

        for dev_eui, data in merged.items():
            row = {
                'dev_eui': dev_eui,
                'device_id': data.get('device_id'),
                'type': data.get('type'),
                'time': data.get('lastReading', {}).get('time'),
                'latitude': data.get('location', {}).get('latitude', None),
                'longitude': data.get('location', {}).get('longitude', None),
            }

            for key in sorted_reading_keys:
                row[key] = data['lastReading'].get(key, None)

            rows.append(row)

        # Step 3: Create and return DataFrame
        df = pd.DataFrame(rows)

        # Save CSV to a buffer
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # S3 bucket details
        s3_bucket_name = "csv-bucket-nikhil"
        s3_file_name = f"devices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        # Upload to S3
        s3_client = boto3.client("s3",
            config=Config(signature_version='s3v4'))
        
        s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=s3_file_name,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        presigned_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{s3_file_name}"

        return jsonify({'status': 'success', 'capabilities': capabilities, 'CSV_URL': presigned_url})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'status': 'failure', 'message': str(e)}), 500

# Used for data export feature
@data_endpoint.route('/export', methods=['POST'])
async def export_data():
    try:
        response_object = {'status': 'success'}
        data = request.get_json()
        
        devices = data.get('devices', [])
        selected_devices = devices.keys()
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
                'sensor_name': devices[row.dev_eui],
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

                # Convert data to DataFrame
        df = pd.DataFrame(response_object["data"])

        # Convert timestamp to string format
        df["timestamp"] = df["timestamp"].astype(str)

        # Save CSV to a buffer
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # S3 bucket details
        s3_bucket_name = "csv-bucket-nikhil"
        s3_file_name = f"sensor_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        # Upload to S3
        s3_client = boto3.client("s3",
            config=Config(signature_version='s3v4'))
        
        s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=s3_file_name,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        presigned_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{s3_file_name}"
        response_object["CSV_URL"] = presigned_url
        
        return jsonify(response_object)
    
    except Exception as e:
        print(e)
        response_object = {'status': 'failure'}
        return jsonify(response_object), 500

@data_endpoint.route('/ai', methods=['POST'])
async def fetch_ai_response():
    try:
        response_object = {'status': 'success'}
        data = request.get_json()
        urlFile = data.get("url")
        messages = data.get("messages")
        print(messages)
        data = await fetch_ai_response(urlFile, messages)
        print(data)
        response_object["data"] = data
        return jsonify(response_object)
    except Exception as e:
        print(e)
        response_object = {'status': 'failure'}
        return jsonify(response_object), 500
    
async def fetch_ai_response(urlFile, messages):
    print("here")
    url = "https://www.chatcsv.co/api/v1/chat"
    token = "REDACTED"  # Replace with your actual token

    data = {
        "model": "gpt-4-0613",
        "messages":
        [
            {"role": "user", "content": "whats your name"},
            {"role": "assistant", "content": "bob"},
        ] + messages,
        "files": [urlFile],  # Replace with actual file link
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "Accept": "text/event-stream"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=data, timeout=30.0)
            data = ""
            if response.status_code != 200:
                raise Exception(f"HTTP error! Status: {response.status_code}, Response: {response.text}")

            # Read response as a stream
            async for chunk in response.aiter_text():
                data += chunk
                print(chunk, end="")  # Process SSE chunks
            return data

        except Exception as error:
            print("Error fetching chat response:", error)

# Run the async function

@data_endpoint.route('/event', methods=['POST'])
async def send_user_event():
    try:
        response_object = {'status': 'success'}
        data = request.get_json()
        user_id = data.get("user_id")
        event_type = data.get("event_type")
        event_description = data.get("event_description")
        project = data.get("project")
        page = data.get("page")
        extra = data.get("extra")
    
        dynamodb = boto3.resource('dynamodb')

        table=dynamodb.Table('nikhil-user-events')

        table.put_item(
            Item={
                'time': datetime.now().strftime('%Y%m%d_%H%M%S'),
                'user_id': user_id,
                'event_type': event_type,
                'event_description': event_description,
                'extra': extra,
                'page': page,
                'project': project,
            }
        )
        return jsonify(response_object)
    except Exception as e:
        print(e)
        response_object = {'status': 'failure'}
        return jsonify(response_object), 500
    
@data_endpoint.route('/suggest', methods=['POST'])
async def fetch_ai_suggestions():
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('nikhil-user-events')

        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq(user_id),
            ScanIndexForward=False,  # Sort descending = newest first
            Limit=100
        )

        # Convert data to DataFrame
        df = pd.DataFrame(response.get('Items', []))

        # Save CSV to a buffer
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # S3 bucket details
        s3_bucket_name = "csv-bucket-nikhil"
        s3_file_name = f"suggestions{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        # Upload to S3
        s3_client = boto3.client("s3",
            config=Config(signature_version='s3v4'))
        
        s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=s3_file_name,
            Body=csv_buffer.getvalue(),
            ContentType="text/csv"
        )
        presigned_url = f"https://{s3_bucket_name}.s3.amazonaws.com/{s3_file_name}"
        messages = [
            {"role": "user", "content": "This is the data from recent user events. Give me 4 suggestions of what the user might want to do next on the portal, 2 of FetchData type and 2 of Navigation type. FetchData will always have the extra attribute populated. Give me the page, project, event_type, extra and event_description matching with each suggestion in JSON format like: {\"suggestions\": [{\"event_type\": \"\",\"event_description\": \"\",\"extra\": \"...\",\"page\": \"\",\"project\": \"\", \"AI_explanation\": \"\"},...]}. Do not give me any made up pages or data. Make sure what you return is ONLY JSON and NO other text or content. Stringify the json content within extra and do not omit any data within the row."}
        ]
        data = await fetch_ai_response(presigned_url, messages)

        response_text = data.strip()
    
        if response_text.startswith('{'):
            json_str = response_text
        else:
            json_str = response_text.split("```json", 1)[1].split("```", 1)[0].strip()

        filteredData = json.loads(json_str)

        return jsonify({
            'status': 'success', 'suggestions': filteredData
        })
    except Exception as e:
        print(e)
        return jsonify({'status': 'failure'}), 500