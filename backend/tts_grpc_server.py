from concurrent import futures
import logging

import grpc
import generated.ttn.lorawan.v3.application_services_pb2 as application_services_pb2
import generated.ttn.lorawan.v3.application_services_pb2_grpc as application_services_pb2_grpc
import generated.ttn.lorawan.v3.application_pb2 as application_pb2
import generated.ttn.lorawan.v3.application_pb2_grpc as application_pb2_grpc


class ApplicationRegistry(application_services_pb2_grpc.ApplicationRegistryServicer):
    def List(self, request, context):
        return application_pb2.ListApplicationsRequest()


def serve():
    port = "1884"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    application_services_pb2_grpc.add_ApplicationRegistryServicer_to_server(ApplicationRegistry(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()