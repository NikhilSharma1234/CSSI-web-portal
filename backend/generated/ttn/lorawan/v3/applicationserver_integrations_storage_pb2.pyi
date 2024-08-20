from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import messages_pb2 as _messages_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContinuationTokenPayload(_message.Message):
    __slots__ = ("limit", "after", "before", "f_port", "order", "field_mask", "last", "last_received_id")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    LAST_RECEIVED_ID_FIELD_NUMBER: _ClassVar[int]
    limit: _wrappers_pb2.UInt32Value
    after: _timestamp_pb2.Timestamp
    before: _timestamp_pb2.Timestamp
    f_port: _wrappers_pb2.UInt32Value
    order: str
    field_mask: _field_mask_pb2.FieldMask
    last: _duration_pb2.Duration
    last_received_id: int
    def __init__(self, limit: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., f_port: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., order: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., last: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., last_received_id: _Optional[int] = ...) -> None: ...

class GetStoredApplicationUpRequest(_message.Message):
    __slots__ = ("application_ids", "end_device_ids", "type", "limit", "after", "before", "f_port", "order", "field_mask", "last", "continuation_token")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    CONTINUATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    type: str
    limit: _wrappers_pb2.UInt32Value
    after: _timestamp_pb2.Timestamp
    before: _timestamp_pb2.Timestamp
    f_port: _wrappers_pb2.UInt32Value
    order: str
    field_mask: _field_mask_pb2.FieldMask
    last: _duration_pb2.Duration
    continuation_token: str
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., type: _Optional[str] = ..., limit: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., f_port: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., order: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., last: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., continuation_token: _Optional[str] = ...) -> None: ...

class GetStoredApplicationUpCountRequest(_message.Message):
    __slots__ = ("application_ids", "end_device_ids", "type", "after", "before", "f_port", "last")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    type: str
    after: _timestamp_pb2.Timestamp
    before: _timestamp_pb2.Timestamp
    f_port: _wrappers_pb2.UInt32Value
    last: _duration_pb2.Duration
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., type: _Optional[str] = ..., after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., f_port: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., last: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class GetStoredApplicationUpCountResponse(_message.Message):
    __slots__ = ("count",)
    class CountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: _containers.ScalarMap[str, int]
    def __init__(self, count: _Optional[_Mapping[str, int]] = ...) -> None: ...
