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
