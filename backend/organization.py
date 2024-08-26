from __main__ import app
from flask import jsonify, request
import os
from dotenv import load_dotenv
import grpc
import generated.ttn.lorawan.v3.organization_services_pb2_grpc as organization_services_pb2_grpc
import generated.ttn.lorawan.v3.organization_pb2 as organization_pb2
import generated.ttn.lorawan.v3.identifiers_pb2 as identifiers_pb2

import generated.ttn.lorawan.v3.user_services_pb2_grpc as user_services_pb2_grpc
import generated.ttn.lorawan.v3.user_pb2 as user_pb2
import google.protobuf.field_mask_pb2 as field_mask_pb2

load_dotenv()
bearer_token = os.getenv('BEARER_TOKEN')
metadata = [('authorization', f'Bearer {bearer_token}')]

# applciations route
@app.route('/organization', methods=['GET', 'POST', 'PUT'])
def organization():
    try:
        response_object = {'status': 'success'}
        if request.method == 'POST':
            post_data = request.get_json()
            user_id = post_data.get('user_id')
            app_id = post_data.get('app_id')
            name = post_data.get('name')
            description = post_data.get('description')

            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = organization_services_pb2_grpc.OrganizationRegistryStub(channel)
                organization = organization_pb2.Organization(ids=identifiers_pb2.OrganizationIdentifiers(organization_id=app_id), name=name, description=description)
                response = stub.Create(organization_pb2.CreateOrganizationRequest(organization=organization, collaborator=identifiers_pb2.OrganizationOrUserIdentifiers(user_ids=identifiers_pb2.UserIdentifiers(user_id=user_id))), metadata=metadata)
            response_object['organization'] = response.ids.organization_id
            return jsonify(response_object)
        elif request.method == 'GET':
            app_id = request.args.get('app_id')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = organization_services_pb2_grpc.OrganizationRegistryStub(channel)
                response = stub.Get(
                    organization_pb2.GetOrganizationRequest(
                        organization_ids=identifiers_pb2.OrganizationIdentifiers(organization_id=app_id),
                        field_mask=field_mask_pb2.FieldMask(paths=['name', 'description'])
                    ),
                    metadata=metadata
                )
            response_object['organization'] = {
                'name': response.name,
                'description': response.description
            }
            return jsonify(response_object)
        elif request.method == 'PUT':
            put_data = request.get_json()
            app_id = put_data.get('app_id')
            name = put_data.get('name')
            description = put_data.get('description')
            user_id = put_data.get('user_id')
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = organization_services_pb2_grpc.OrganizationRegistryStub(channel)
                organization = organization_pb2.Organization(ids=identifiers_pb2.OrganizationIdentifiers(organization_id=app_id), name=name, description=description)
                response = stub.Update(organization_pb2.UpdateOrganizationRequest(organization=organization, field_mask=field_mask_pb2.FieldMask(paths=['name', 'description'])), metadata=metadata)            
            response_object['organization'] = {
                'name': response.name,
                'description': response.description
            }
            return jsonify(response_object)
    except:
        response_object = {'status': 'failure'}
        return jsonify(response_object)