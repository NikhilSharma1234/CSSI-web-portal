from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
FILE_FIELD_NUMBER: _ClassVar[int]
file: _descriptor.FieldDescriptor
MESSAGE_FIELD_NUMBER: _ClassVar[int]
message: _descriptor.FieldDescriptor
FIELD_FIELD_NUMBER: _ClassVar[int]
field: _descriptor.FieldDescriptor
ONEOF_FIELD_NUMBER: _ClassVar[int]
oneof: _descriptor.FieldDescriptor
ENUM_FIELD_NUMBER: _ClassVar[int]
enum: _descriptor.FieldDescriptor
ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
enum_value: _descriptor.FieldDescriptor
SERVICE_FIELD_NUMBER: _ClassVar[int]
service: _descriptor.FieldDescriptor
METHOD_FIELD_NUMBER: _ClassVar[int]
method: _descriptor.FieldDescriptor

class FileOptions(_message.Message):
    __slots__ = ("marshaler_all", "unmarshaler_all")
    MARSHALER_ALL_FIELD_NUMBER: _ClassVar[int]
    UNMARSHALER_ALL_FIELD_NUMBER: _ClassVar[int]
    marshaler_all: bool
    unmarshaler_all: bool
    def __init__(self, marshaler_all: bool = ..., unmarshaler_all: bool = ...) -> None: ...

class MessageOptions(_message.Message):
    __slots__ = ("marshaler", "unmarshaler", "wrapper")
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    UNMARSHALER_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_FIELD_NUMBER: _ClassVar[int]
    marshaler: bool
    unmarshaler: bool
    wrapper: bool
    def __init__(self, marshaler: bool = ..., unmarshaler: bool = ..., wrapper: bool = ...) -> None: ...

class FieldOptions(_message.Message):
    __slots__ = ("marshaler_func", "unmarshaler_func")
    MARSHALER_FUNC_FIELD_NUMBER: _ClassVar[int]
    UNMARSHALER_FUNC_FIELD_NUMBER: _ClassVar[int]
    marshaler_func: str
    unmarshaler_func: str
    def __init__(self, marshaler_func: _Optional[str] = ..., unmarshaler_func: _Optional[str] = ...) -> None: ...

class OneofOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnumOptions(_message.Message):
    __slots__ = ("marshaler", "marshal_as_number", "marshal_as_string", "unmarshaler", "prefix")
    MARSHALER_FIELD_NUMBER: _ClassVar[int]
    MARSHAL_AS_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MARSHAL_AS_STRING_FIELD_NUMBER: _ClassVar[int]
    UNMARSHALER_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    marshaler: bool
    marshal_as_number: bool
    marshal_as_string: bool
    unmarshaler: bool
    prefix: str
    def __init__(self, marshaler: bool = ..., marshal_as_number: bool = ..., marshal_as_string: bool = ..., unmarshaler: bool = ..., prefix: _Optional[str] = ...) -> None: ...

class EnumValueOptions(_message.Message):
    __slots__ = ("value", "aliases")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ALIASES_FIELD_NUMBER: _ClassVar[int]
    value: str
    aliases: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, value: _Optional[str] = ..., aliases: _Optional[_Iterable[str]] = ...) -> None: ...

class ServiceOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MethodOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
