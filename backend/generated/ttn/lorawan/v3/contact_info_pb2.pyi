from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContactType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTACT_TYPE_OTHER: _ClassVar[ContactType]
    CONTACT_TYPE_ABUSE: _ClassVar[ContactType]
    CONTACT_TYPE_BILLING: _ClassVar[ContactType]
    CONTACT_TYPE_TECHNICAL: _ClassVar[ContactType]

class ContactMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTACT_METHOD_OTHER: _ClassVar[ContactMethod]
    CONTACT_METHOD_EMAIL: _ClassVar[ContactMethod]
    CONTACT_METHOD_PHONE: _ClassVar[ContactMethod]
CONTACT_TYPE_OTHER: ContactType
CONTACT_TYPE_ABUSE: ContactType
CONTACT_TYPE_BILLING: ContactType
CONTACT_TYPE_TECHNICAL: ContactType
CONTACT_METHOD_OTHER: ContactMethod
CONTACT_METHOD_EMAIL: ContactMethod
CONTACT_METHOD_PHONE: ContactMethod

class ContactInfo(_message.Message):
    __slots__ = ("contact_type", "contact_method", "value", "public", "validated_at")
    CONTACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_METHOD_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_FIELD_NUMBER: _ClassVar[int]
    VALIDATED_AT_FIELD_NUMBER: _ClassVar[int]
    contact_type: ContactType
    contact_method: ContactMethod
    value: str
    public: bool
    validated_at: _timestamp_pb2.Timestamp
    def __init__(self, contact_type: _Optional[_Union[ContactType, str]] = ..., contact_method: _Optional[_Union[ContactMethod, str]] = ..., value: _Optional[str] = ..., public: bool = ..., validated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ContactInfoValidation(_message.Message):
    __slots__ = ("id", "token", "entity", "contact_info", "created_at", "expires_at", "updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    token: str
    entity: _identifiers_pb2.EntityIdentifiers
    contact_info: _containers.RepeatedCompositeFieldContainer[ContactInfo]
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., token: _Optional[str] = ..., entity: _Optional[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]] = ..., contact_info: _Optional[_Iterable[_Union[ContactInfo, _Mapping]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
