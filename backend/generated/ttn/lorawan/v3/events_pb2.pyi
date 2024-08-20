from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ("name", "time", "identifiers", "data", "correlation_ids", "origin", "context", "visibility", "authentication", "remote_ip", "user_agent", "unique_id")
    class ContextEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class Authentication(_message.Message):
        __slots__ = ("type", "token_type", "token_id")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
        type: str
        token_type: str
        token_id: str
        def __init__(self, type: _Optional[str] = ..., token_type: _Optional[str] = ..., token_id: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_FIELD_NUMBER: _ClassVar[int]
    REMOTE_IP_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    time: _timestamp_pb2.Timestamp
    identifiers: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.EntityIdentifiers]
    data: _any_pb2.Any
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    origin: str
    context: _containers.ScalarMap[str, bytes]
    visibility: _rights_pb2.Rights
    authentication: Event.Authentication
    remote_ip: str
    user_agent: str
    unique_id: str
    def __init__(self, name: _Optional[str] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., identifiers: _Optional[_Iterable[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., origin: _Optional[str] = ..., context: _Optional[_Mapping[str, bytes]] = ..., visibility: _Optional[_Union[_rights_pb2.Rights, _Mapping]] = ..., authentication: _Optional[_Union[Event.Authentication, _Mapping]] = ..., remote_ip: _Optional[str] = ..., user_agent: _Optional[str] = ..., unique_id: _Optional[str] = ...) -> None: ...

class StreamEventsRequest(_message.Message):
    __slots__ = ("identifiers", "tail", "after", "names")
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    TAIL_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.EntityIdentifiers]
    tail: int
    after: _timestamp_pb2.Timestamp
    names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, identifiers: _Optional[_Iterable[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]]] = ..., tail: _Optional[int] = ..., after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., names: _Optional[_Iterable[str]] = ...) -> None: ...

class FindRelatedEventsRequest(_message.Message):
    __slots__ = ("correlation_id",)
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    correlation_id: str
    def __init__(self, correlation_id: _Optional[str] = ...) -> None: ...

class FindRelatedEventsResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[Event]
    def __init__(self, events: _Optional[_Iterable[_Union[Event, _Mapping]]] = ...) -> None: ...
