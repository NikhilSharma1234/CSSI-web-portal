from __future__ import print_function

import logging

import grpc
import generated.ttn.lorawan.v3.application_services_pb2 as application_services_pb2
import generated.ttn.lorawan.v3.application_services_pb2_grpc as application_services_pb2_grpc
import generated.ttn.lorawan.v3.application_pb2 as application_pb2
import generated.ttn.lorawan.v3.application_pb2_grpc as application_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.secure_channel("tts.rd.unr.edu:1884", tok) as channel:
        stub = application_services_pb2_grpc.ApplicationRegistryStub(channel)
        response = stub.List(application_pb2.ListApplicationsRequest())
    print(response)


if __name__ == "__main__":
    logging.basicConfig()
    run()