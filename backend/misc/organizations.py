#from __main__ import app
from flask import jsonify, request
import os
from dotenv import load_dotenv
import grpc
import generated.ttn.lorawan.v3.organization_services_pb2_grpc as organization_services_pb2_grpc
import generated.ttn.lorawan.v3.organization_pb2 as organization_pb2
import generated.ttn.lorawan.v3.identifiers_pb2 as identifiers_pb2
import google.protobuf.field_mask_pb2 as field_mask_pb2

load_dotenv()

bearer_token = os.getenv('BEARER_TOKEN')
metadata = [('authorization', f'Bearer {bearer_token}')]

# applciations route
@app.route('/organizations', methods=['GET'])
def organizations():
    try:
        response_object = {'status': 'success'}
        if request.method == 'GET':
            user_id = request.args.get('user_id')
            collaborator = identifiers_pb2.OrganizationOrUserIdentifiers(user_ids = identifiers_pb2.UserIdentifiers(user_id=user_id))
            with grpc.insecure_channel("tts.rd.unr.edu:1884") as channel:
                stub = organization_services_pb2_grpc.OrganizationRegistryStub(channel)
                response = stub.List(organization_pb2.ListOrganizationsRequest(collaborator = collaborator, field_mask=field_mask_pb2.FieldMask(paths=['name', 'description'])), metadata=metadata)
            response_object['organizations'] = []
            for organization in response.organizations:
                response_object['organizations'].append({
                    'id': organization.ids.organization_id,
                    'name': organization.name,
                    'description': organization.description
                })
                
            return jsonify(response_object)
    except:
        response_object = {'status': 'failure'}
        return jsonify(response_object)
