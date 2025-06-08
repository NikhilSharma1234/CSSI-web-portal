#from __main__ import app
from collections import defaultdict
from flask import jsonify, request
from datetime import datetime, timedelta, timezone
from sqlalchemy import func, select
import os
from dotenv import load_dotenv

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
    'sensor_mapping', 
    metadata,
    autoload_with=engine
)

UNIT_STANDARDIZATION = {
    
    'celsius': '°C',
    'fahrenheit': '°F',
    'kelvin': 'K',
    
    'decibels': 'dB',
    'decibel milliwatt': 'dBm',
    
    'percent': '%',
    'microsiemens per centimeter': 'µS/cm',
    'millisiemens per centimeter': 'mS/cm',
    
    'volt': 'V',
    
    'meter': 'm',
    'kilogram': 'kg',
    'second': 's',
    'centimeter': 'cm',
    'millimeter': 'mm'
}

PAYLOAD_TYPE_TO_UNIT = {
    'temperature': '°C',
    'temp_SOIL': '°C',
    'water_SOIL': '%',
    'conduct_SOIL': 'µS/cm',
    'Bat': '%',
    'bat': 'V',
    'batteryCapacity': '%',
    'BatV': '%',
    'snr': 'dB',
    'rssi': 'dBm'
}

def standardize_unit(payload_type: str, raw_unit: str) -> str:
    if payload_type in PAYLOAD_TYPE_TO_UNIT:
        return PAYLOAD_TYPE_TO_UNIT[payload_type]
    
    lower_unit = raw_unit.lower()
    if lower_unit in UNIT_STANDARDIZATION:
        return UNIT_STANDARDIZATION[lower_unit]
    
    if 'celsius' in lower_unit:
        return '°C'
    if 'fahrenheit' in lower_unit:
        return '°F'
    
    return raw_unit

def get_sensor_mapping():
    stmt = select(
            table.columns.type,
            table.columns.display_name,
            table.columns.payload_value,
            table.columns.brand,
            table.columns.model,
            table.columns.unit,
            table.columns.derivation,
            table.columns.description,
            table.columns.sortable,
            table.columns.width
        )
        
    with engine.connect() as connection:
        results = connection.execute(stmt).fetchall()

    mapping = [
        {
            "type": row.type,
            "display_name": row.display_name,
            "payload_value": row.payload_value,
            "brand": row.brand,
            "model": row.model,
            "unit": row.unit,
            "derivation": row.derivation,
            "description": row.description,
            "sortable": row.sortable,
            "width": row.width,
        }
        for row in results
    ]

    return mapping

if __name__ == '__main__':
    get_sensor_mapping()
