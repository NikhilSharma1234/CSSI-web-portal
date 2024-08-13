from __future__ import print_function

import logging

import os
from dotenv import load_dotenv
load_dotenv()

import grpc
import generated.ttn.lorawan.v3.application_services_pb2 as application_services_pb2
import generated.ttn.lorawan.v3.application_services_pb2_grpc as application_services_pb2_grpc
import generated.ttn.lorawan.v3.application_pb2 as application_pb2
import generated.ttn.lorawan.v3.application_pb2_grpc as application_pb2_grpc
import generated.ttn.lorawan.v3.identifiers_pb2 as identifiers_pb2


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    with open('cert.crt', 'rb') as c:
        cert = c.read()
    with open('cert.key', 'rb') as k:
        key = k.read()

    credentials = grpc.ssl_channel_credentials(
        certificate_chain = cert,
        private_key = key
    )

    bearer_token = os.getenv('BEARER_TOKEN')
    metadata = [('authorization', f'Bearer {bearer_token}')]
    
    user_id = {{}}
    collaborator = identifiers_pb2.OrganizationOrUserIdentifiers(user_ids = user_id)

    print("Will try to greet world ...")
    with grpc.secure_channel("tts.rd.unr.edu:1884", credentials) as channel:
        stub = application_services_pb2_grpc.ApplicationRegistryStub(channel)
        response = stub.List(application_pb2.ListApplicationsRequest(collaborator = collaborator), metadata=metadata)
    print(response)


if __name__ == "__main__":
    logging.basicConfig()
    run()