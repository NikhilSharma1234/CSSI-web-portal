from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorDetails(_message.Message):
    __slots__ = ("namespace", "name", "message_format", "attributes", "correlation_id", "cause", "code", "details")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    name: str
    message_format: str
    attributes: _struct_pb2.Struct
    correlation_id: str
    cause: ErrorDetails
    code: int
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, namespace: _Optional[str] = ..., name: _Optional[str] = ..., message_format: _Optional[str] = ..., attributes: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., correlation_id: _Optional[str] = ..., cause: _Optional[_Union[ErrorDetails, _Mapping]] = ..., code: _Optional[int] = ..., details: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
