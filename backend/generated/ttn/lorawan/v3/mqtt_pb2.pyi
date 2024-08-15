from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MQTTConnectionInfo(_message.Message):
    __slots__ = ("public_address", "public_tls_address", "username")
    PUBLIC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_TLS_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    public_address: str
    public_tls_address: str
    username: str
    def __init__(self, public_address: _Optional[str] = ..., public_tls_address: _Optional[str] = ..., username: _Optional[str] = ...) -> None: ...
