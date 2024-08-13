from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PeerInfo(_message.Message):
    __slots__ = ("grpc_port", "tls", "roles", "tags")
    class TagsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GRPC_PORT_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    grpc_port: int
    tls: bool
    roles: _containers.RepeatedScalarFieldContainer[_enums_pb2.ClusterRole]
    tags: _containers.ScalarMap[str, str]
    def __init__(self, grpc_port: _Optional[int] = ..., tls: bool = ..., roles: _Optional[_Iterable[_Union[_enums_pb2.ClusterRole, str]]] = ..., tags: _Optional[_Mapping[str, str]] = ...) -> None: ...
