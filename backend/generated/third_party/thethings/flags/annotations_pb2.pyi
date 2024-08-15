from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

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
    __slots__ = ()
    def __init__(self) -> None: ...

class MessageOptions(_message.Message):
    __slots__ = ("select", "set", "wrapper", "semantical")
    SELECT_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_FIELD_NUMBER: _ClassVar[int]
    SEMANTICAL_FIELD_NUMBER: _ClassVar[int]
    select: bool
    set: bool
    wrapper: bool
    semantical: bool
    def __init__(self, select: bool = ..., set: bool = ..., wrapper: bool = ..., semantical: bool = ...) -> None: ...

class FieldOptions(_message.Message):
    __slots__ = ("select", "set", "set_flag_new_func", "set_flag_getter_func", "hidden", "semantical")
    SELECT_FIELD_NUMBER: _ClassVar[int]
    SET_FIELD_NUMBER: _ClassVar[int]
    SET_FLAG_NEW_FUNC_FIELD_NUMBER: _ClassVar[int]
    SET_FLAG_GETTER_FUNC_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    SEMANTICAL_FIELD_NUMBER: _ClassVar[int]
    select: bool
    set: bool
    set_flag_new_func: str
    set_flag_getter_func: str
    hidden: bool
    semantical: bool
    def __init__(self, select: bool = ..., set: bool = ..., set_flag_new_func: _Optional[str] = ..., set_flag_getter_func: _Optional[str] = ..., hidden: bool = ..., semantical: bool = ...) -> None: ...

class OneofOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EnumOptions(_message.Message):
    __slots__ = ("alias_map",)
    ALIAS_MAP_FIELD_NUMBER: _ClassVar[int]
    alias_map: str
    def __init__(self, alias_map: _Optional[str] = ...) -> None: ...

class EnumValueOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ServiceOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MethodOptions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
