from google.protobuf import duration_pb2 as _duration_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1
from ttn.lorawan.v3 import keys_pb2 as _keys_pb2
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JoinRequest(_message.Message):
    __slots__ = ("raw_payload", "payload", "dev_addr", "selected_mac_version", "net_id", "downlink_settings", "rx_delay", "cf_list", "correlation_ids", "consumed_airtime")
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    SELECTED_MAC_VERSION_FIELD_NUMBER: _ClassVar[int]
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RX_DELAY_FIELD_NUMBER: _ClassVar[int]
    CF_LIST_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_AIRTIME_FIELD_NUMBER: _ClassVar[int]
    raw_payload: bytes
    payload: _lorawan_pb2.Message
    dev_addr: bytes
    selected_mac_version: _lorawan_pb2.MACVersion
    net_id: bytes
    downlink_settings: _lorawan_pb2.DLSettings
    rx_delay: _lorawan_pb2.RxDelay
    cf_list: _lorawan_pb2.CFList
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    consumed_airtime: _duration_pb2.Duration
    def __init__(self, raw_payload: _Optional[bytes] = ..., payload: _Optional[_Union[_lorawan_pb2.Message, _Mapping]] = ..., dev_addr: _Optional[bytes] = ..., selected_mac_version: _Optional[_Union[_lorawan_pb2.MACVersion, str]] = ..., net_id: _Optional[bytes] = ..., downlink_settings: _Optional[_Union[_lorawan_pb2.DLSettings, _Mapping]] = ..., rx_delay: _Optional[_Union[_lorawan_pb2.RxDelay, str]] = ..., cf_list: _Optional[_Union[_lorawan_pb2.CFList, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., consumed_airtime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class JoinResponse(_message.Message):
    __slots__ = ("raw_payload", "session_keys", "lifetime", "correlation_ids")
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEYS_FIELD_NUMBER: _ClassVar[int]
    LIFETIME_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    raw_payload: bytes
    session_keys: _keys_pb2.SessionKeys
    lifetime: _duration_pb2.Duration
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, raw_payload: _Optional[bytes] = ..., session_keys: _Optional[_Union[_keys_pb2.SessionKeys, _Mapping]] = ..., lifetime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ...) -> None: ...
