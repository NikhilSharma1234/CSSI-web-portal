from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Picture(_message.Message):
    __slots__ = ("embedded", "sizes")
    class Embedded(_message.Message):
        __slots__ = ("mime_type", "data")
        MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        mime_type: str
        data: bytes
        def __init__(self, mime_type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...
    class SizesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    EMBEDDED_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    embedded: Picture.Embedded
    sizes: _containers.ScalarMap[int, str]
    def __init__(self, embedded: _Optional[_Union[Picture.Embedded, _Mapping]] = ..., sizes: _Optional[_Mapping[int, str]] = ...) -> None: ...
