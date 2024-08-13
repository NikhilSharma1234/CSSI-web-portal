from ttn.lorawan.v3 import client_pb2 as _client_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateClientEmailMessage(_message.Message):
    __slots__ = ("create_client_request", "api_key")
    CREATE_CLIENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    create_client_request: _client_pb2.CreateClientRequest
    api_key: _rights_pb2.APIKey
    def __init__(self, create_client_request: _Optional[_Union[_client_pb2.CreateClientRequest, _Mapping]] = ..., api_key: _Optional[_Union[_rights_pb2.APIKey, _Mapping]] = ...) -> None: ...
