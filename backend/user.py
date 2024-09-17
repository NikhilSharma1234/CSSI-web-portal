#from __main__ import app
from flask import jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import grpc
import os
import generated.ttn.lorawan.v3.identifiers_pb2 as identifiers_pb2
import generated.ttn.lorawan.v3.user_services_pb2_grpc as user_services_pb2_grpc
import generated.ttn.lorawan.v3.user_pb2 as user_pb2
import google.protobuf.field_mask_pb2 as field_mask_pb2
from flask import Blueprint

user_endpoint = Blueprint('user', __name__)


load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')
metadata = [('authorization', f'Bearer {bearer_token}')]

# user route
@user_endpoint.route('/user', methods=['GET', 'POST', 'PUT'])
def user():
    try:
        response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json()
            name = post_data.get('name')
            email = post_data.get('email')
            user_id = post_data.get('user_id')
            password = post_data.get('password')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = user_services_pb2_grpc.UserRegistryStub(channel)
                user = user_pb2.User(
                    ids=identifiers_pb2.UserIdentifiers(user_id=user_id, email=email),
                    name=name,
                    primary_email_address=email,
                    password=password
                )
                response = stub.Create(user_pb2.CreateUserRequest(user=user) , metadata=metadata)
            response_object['user'] = response.ids.user_id
            response_object['message'] = 'User added!'
        elif request.method == 'GET':
            user_id = request.args.get('user_id')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = user_services_pb2_grpc.UserRegistryStub(channel)
                response = stub.Get(
                    user_pb2.GetUserRequest(
                        user_ids=identifiers_pb2.UserIdentifiers(user_id=user_id),
                        field_mask=field_mask_pb2.FieldMask(paths=['name', 'primary_email_address'])
                    ),
                    metadata=metadata
                )
            response_object['user'] = {
                'name': response.name,
                'email': response.primary_email_address
            }
        elif request.method == 'PUT':
            put_data = request.get_json()
            user_id = put_data.get('user_id')
            name = put_data.get('name')
            email = put_data.get('email')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = user_services_pb2_grpc.UserRegistryStub(channel)
                user = user_pb2.User(ids=identifiers_pb2.UserIdentifiers(user_id=user_id), name=name, primary_email_address=email)
                response = stub.Update(user_pb2.UpdateUserRequest(user=user, field_mask=field_mask_pb2.FieldMask(paths=['name', 'primary_email_address'])), metadata=metadata)
            response_object['user'] = {
                'name': response.name,
                'email': response.primary_email_address
            }
        return jsonify(response_object)
    except:
        response_object = {'status': 'failure'}
        return jsonify(response_object)
