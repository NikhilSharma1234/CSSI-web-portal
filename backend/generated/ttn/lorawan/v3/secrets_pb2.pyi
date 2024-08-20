from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Secret(_message.Message):
    __slots__ = ("key_id", "value")
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    value: bytes
    def __init__(self, key_id: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
