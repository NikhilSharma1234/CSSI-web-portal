from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import error_pb2 as _error_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import keys_pb2 as _keys_pb2
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from ttn.lorawan.v3 import metadata_pb2 as _metadata_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PayloadFormatter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FORMATTER_NONE: _ClassVar[PayloadFormatter]
    FORMATTER_REPOSITORY: _ClassVar[PayloadFormatter]
    FORMATTER_GRPC_SERVICE: _ClassVar[PayloadFormatter]
    FORMATTER_JAVASCRIPT: _ClassVar[PayloadFormatter]
    FORMATTER_CAYENNELPP: _ClassVar[PayloadFormatter]
FORMATTER_NONE: PayloadFormatter
FORMATTER_REPOSITORY: PayloadFormatter
FORMATTER_GRPC_SERVICE: PayloadFormatter
FORMATTER_JAVASCRIPT: PayloadFormatter
FORMATTER_CAYENNELPP: PayloadFormatter

class UplinkMessage(_message.Message):
    __slots__ = ("raw_payload", "payload", "settings", "rx_metadata", "received_at", "correlation_ids", "device_channel_index", "consumed_airtime", "crc_status")
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RX_METADATA_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_AIRTIME_FIELD_NUMBER: _ClassVar[int]
    CRC_STATUS_FIELD_NUMBER: _ClassVar[int]
    raw_payload: bytes
    payload: _lorawan_pb2.Message
    settings: _lorawan_pb2.TxSettings
    rx_metadata: _containers.RepeatedCompositeFieldContainer[_metadata_pb2.RxMetadata]
    received_at: _timestamp_pb2.Timestamp
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    device_channel_index: int
    consumed_airtime: _duration_pb2.Duration
    crc_status: _wrappers_pb2.BoolValue
    def __init__(self, raw_payload: _Optional[bytes] = ..., payload: _Optional[_Union[_lorawan_pb2.Message, _Mapping]] = ..., settings: _Optional[_Union[_lorawan_pb2.TxSettings, _Mapping]] = ..., rx_metadata: _Optional[_Iterable[_Union[_metadata_pb2.RxMetadata, _Mapping]]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., device_channel_index: _Optional[int] = ..., consumed_airtime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., crc_status: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class DownlinkMessage(_message.Message):
    __slots__ = ("raw_payload", "payload", "end_device_ids", "request", "scheduled", "correlation_ids", "session_key_id")
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    raw_payload: bytes
    payload: _lorawan_pb2.Message
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    request: _lorawan_pb2.TxRequest
    scheduled: _lorawan_pb2.TxSettings
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    session_key_id: bytes
    def __init__(self, raw_payload: _Optional[bytes] = ..., payload: _Optional[_Union[_lorawan_pb2.Message, _Mapping]] = ..., end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., request: _Optional[_Union[_lorawan_pb2.TxRequest, _Mapping]] = ..., scheduled: _Optional[_Union[_lorawan_pb2.TxSettings, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., session_key_id: _Optional[bytes] = ...) -> None: ...

class TxAcknowledgment(_message.Message):
    __slots__ = ("correlation_ids", "result", "downlink_message")
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[TxAcknowledgment.Result]
        UNKNOWN_ERROR: _ClassVar[TxAcknowledgment.Result]
        TOO_LATE: _ClassVar[TxAcknowledgment.Result]
        TOO_EARLY: _ClassVar[TxAcknowledgment.Result]
        COLLISION_PACKET: _ClassVar[TxAcknowledgment.Result]
        COLLISION_BEACON: _ClassVar[TxAcknowledgment.Result]
        TX_FREQ: _ClassVar[TxAcknowledgment.Result]
        TX_POWER: _ClassVar[TxAcknowledgment.Result]
        GPS_UNLOCKED: _ClassVar[TxAcknowledgment.Result]
    SUCCESS: TxAcknowledgment.Result
    UNKNOWN_ERROR: TxAcknowledgment.Result
    TOO_LATE: TxAcknowledgment.Result
    TOO_EARLY: TxAcknowledgment.Result
    COLLISION_PACKET: TxAcknowledgment.Result
    COLLISION_BEACON: TxAcknowledgment.Result
    TX_FREQ: TxAcknowledgment.Result
    TX_POWER: TxAcknowledgment.Result
    GPS_UNLOCKED: TxAcknowledgment.Result
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    result: TxAcknowledgment.Result
    downlink_message: DownlinkMessage
    def __init__(self, correlation_ids: _Optional[_Iterable[str]] = ..., result: _Optional[_Union[TxAcknowledgment.Result, str]] = ..., downlink_message: _Optional[_Union[DownlinkMessage, _Mapping]] = ...) -> None: ...

class GatewayTxAcknowledgment(_message.Message):
    __slots__ = ("gateway_ids", "tx_ack")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    TX_ACK_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    tx_ack: TxAcknowledgment
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., tx_ack: _Optional[_Union[TxAcknowledgment, _Mapping]] = ...) -> None: ...

class GatewayUplinkMessage(_message.Message):
    __slots__ = ("message", "band_id")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    BAND_ID_FIELD_NUMBER: _ClassVar[int]
    message: UplinkMessage
    band_id: str
    def __init__(self, message: _Optional[_Union[UplinkMessage, _Mapping]] = ..., band_id: _Optional[str] = ...) -> None: ...

class ApplicationUplink(_message.Message):
    __slots__ = ("session_key_id", "f_port", "f_cnt", "frm_payload", "decoded_payload", "decoded_payload_warnings", "normalized_payload", "normalized_payload_warnings", "rx_metadata", "settings", "received_at", "app_s_key", "last_a_f_cnt_down", "confirmed", "consumed_airtime", "packet_error_rate", "locations", "version_ids", "network_ids")
    class LocationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _metadata_pb2.Location
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_metadata_pb2.Location, _Mapping]] = ...) -> None: ...
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DECODED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DECODED_PAYLOAD_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_PAYLOAD_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    RX_METADATA_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    LAST_A_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_AIRTIME_FIELD_NUMBER: _ClassVar[int]
    PACKET_ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_IDS_FIELD_NUMBER: _ClassVar[int]
    session_key_id: bytes
    f_port: int
    f_cnt: int
    frm_payload: bytes
    decoded_payload: _struct_pb2.Struct
    decoded_payload_warnings: _containers.RepeatedScalarFieldContainer[str]
    normalized_payload: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    normalized_payload_warnings: _containers.RepeatedScalarFieldContainer[str]
    rx_metadata: _containers.RepeatedCompositeFieldContainer[_metadata_pb2.RxMetadata]
    settings: _lorawan_pb2.TxSettings
    received_at: _timestamp_pb2.Timestamp
    app_s_key: _keys_pb2.KeyEnvelope
    last_a_f_cnt_down: int
    confirmed: bool
    consumed_airtime: _duration_pb2.Duration
    packet_error_rate: float
    locations: _containers.MessageMap[str, _metadata_pb2.Location]
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    network_ids: _identifiers_pb2.NetworkIdentifiers
    def __init__(self, session_key_id: _Optional[bytes] = ..., f_port: _Optional[int] = ..., f_cnt: _Optional[int] = ..., frm_payload: _Optional[bytes] = ..., decoded_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., decoded_payload_warnings: _Optional[_Iterable[str]] = ..., normalized_payload: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ..., normalized_payload_warnings: _Optional[_Iterable[str]] = ..., rx_metadata: _Optional[_Iterable[_Union[_metadata_pb2.RxMetadata, _Mapping]]] = ..., settings: _Optional[_Union[_lorawan_pb2.TxSettings, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., app_s_key: _Optional[_Union[_keys_pb2.KeyEnvelope, _Mapping]] = ..., last_a_f_cnt_down: _Optional[int] = ..., confirmed: bool = ..., consumed_airtime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., packet_error_rate: _Optional[float] = ..., locations: _Optional[_Mapping[str, _metadata_pb2.Location]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., network_ids: _Optional[_Union[_identifiers_pb2.NetworkIdentifiers, _Mapping]] = ...) -> None: ...

class ApplicationUplinkNormalized(_message.Message):
    __slots__ = ("session_key_id", "f_port", "f_cnt", "frm_payload", "normalized_payload", "normalized_payload_warnings", "rx_metadata", "settings", "received_at", "confirmed", "consumed_airtime", "locations", "version_ids", "network_ids")
    class LocationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _metadata_pb2.Location
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_metadata_pb2.Location, _Mapping]] = ...) -> None: ...
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_PAYLOAD_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    RX_METADATA_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    CONSUMED_AIRTIME_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_IDS_FIELD_NUMBER: _ClassVar[int]
    session_key_id: bytes
    f_port: int
    f_cnt: int
    frm_payload: bytes
    normalized_payload: _struct_pb2.Struct
    normalized_payload_warnings: _containers.RepeatedScalarFieldContainer[str]
    rx_metadata: _containers.RepeatedCompositeFieldContainer[_metadata_pb2.RxMetadata]
    settings: _lorawan_pb2.TxSettings
    received_at: _timestamp_pb2.Timestamp
    confirmed: bool
    consumed_airtime: _duration_pb2.Duration
    locations: _containers.MessageMap[str, _metadata_pb2.Location]
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    network_ids: _identifiers_pb2.NetworkIdentifiers
    def __init__(self, session_key_id: _Optional[bytes] = ..., f_port: _Optional[int] = ..., f_cnt: _Optional[int] = ..., frm_payload: _Optional[bytes] = ..., normalized_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., normalized_payload_warnings: _Optional[_Iterable[str]] = ..., rx_metadata: _Optional[_Iterable[_Union[_metadata_pb2.RxMetadata, _Mapping]]] = ..., settings: _Optional[_Union[_lorawan_pb2.TxSettings, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., confirmed: bool = ..., consumed_airtime: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., locations: _Optional[_Mapping[str, _metadata_pb2.Location]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., network_ids: _Optional[_Union[_identifiers_pb2.NetworkIdentifiers, _Mapping]] = ...) -> None: ...

class ApplicationLocation(_message.Message):
    __slots__ = ("service", "location", "attributes")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    service: str
    location: _metadata_pb2.Location
    attributes: _containers.ScalarMap[str, str]
    def __init__(self, service: _Optional[str] = ..., location: _Optional[_Union[_metadata_pb2.Location, _Mapping]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ApplicationJoinAccept(_message.Message):
    __slots__ = ("session_key_id", "app_s_key", "invalidated_downlinks", "pending_session", "received_at")
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    INVALIDATED_DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    PENDING_SESSION_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    session_key_id: bytes
    app_s_key: _keys_pb2.KeyEnvelope
    invalidated_downlinks: _containers.RepeatedCompositeFieldContainer[ApplicationDownlink]
    pending_session: bool
    received_at: _timestamp_pb2.Timestamp
    def __init__(self, session_key_id: _Optional[bytes] = ..., app_s_key: _Optional[_Union[_keys_pb2.KeyEnvelope, _Mapping]] = ..., invalidated_downlinks: _Optional[_Iterable[_Union[ApplicationDownlink, _Mapping]]] = ..., pending_session: bool = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ApplicationDownlink(_message.Message):
    __slots__ = ("session_key_id", "f_port", "f_cnt", "frm_payload", "decoded_payload", "decoded_payload_warnings", "confirmed", "class_b_c", "priority", "correlation_ids", "confirmed_retry")
    class ClassBC(_message.Message):
        __slots__ = ("gateways", "absolute_time")
        GATEWAYS_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_TIME_FIELD_NUMBER: _ClassVar[int]
        gateways: _containers.RepeatedCompositeFieldContainer[_lorawan_pb2.ClassBCGatewayIdentifiers]
        absolute_time: _timestamp_pb2.Timestamp
        def __init__(self, gateways: _Optional[_Iterable[_Union[_lorawan_pb2.ClassBCGatewayIdentifiers, _Mapping]]] = ..., absolute_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class ConfirmedRetry(_message.Message):
        __slots__ = ("attempt", "max_attempts")
        ATTEMPT_FIELD_NUMBER: _ClassVar[int]
        MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        attempt: int
        max_attempts: _wrappers_pb2.UInt32Value
        def __init__(self, attempt: _Optional[int] = ..., max_attempts: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DECODED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DECODED_PAYLOAD_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    CLASS_B_C_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_RETRY_FIELD_NUMBER: _ClassVar[int]
    session_key_id: bytes
    f_port: int
    f_cnt: int
    frm_payload: bytes
    decoded_payload: _struct_pb2.Struct
    decoded_payload_warnings: _containers.RepeatedScalarFieldContainer[str]
    confirmed: bool
    class_b_c: ApplicationDownlink.ClassBC
    priority: _lorawan_pb2.TxSchedulePriority
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    confirmed_retry: ApplicationDownlink.ConfirmedRetry
    def __init__(self, session_key_id: _Optional[bytes] = ..., f_port: _Optional[int] = ..., f_cnt: _Optional[int] = ..., frm_payload: _Optional[bytes] = ..., decoded_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., decoded_payload_warnings: _Optional[_Iterable[str]] = ..., confirmed: bool = ..., class_b_c: _Optional[_Union[ApplicationDownlink.ClassBC, _Mapping]] = ..., priority: _Optional[_Union[_lorawan_pb2.TxSchedulePriority, str]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., confirmed_retry: _Optional[_Union[ApplicationDownlink.ConfirmedRetry, _Mapping]] = ...) -> None: ...

class ApplicationDownlinks(_message.Message):
    __slots__ = ("downlinks",)
    DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    downlinks: _containers.RepeatedCompositeFieldContainer[ApplicationDownlink]
    def __init__(self, downlinks: _Optional[_Iterable[_Union[ApplicationDownlink, _Mapping]]] = ...) -> None: ...

class ApplicationDownlinkFailed(_message.Message):
    __slots__ = ("downlink", "error")
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    downlink: ApplicationDownlink
    error: _error_pb2.ErrorDetails
    def __init__(self, downlink: _Optional[_Union[ApplicationDownlink, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.ErrorDetails, _Mapping]] = ...) -> None: ...

class ApplicationInvalidatedDownlinks(_message.Message):
    __slots__ = ("downlinks", "last_f_cnt_down", "session_key_id")
    DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    LAST_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    downlinks: _containers.RepeatedCompositeFieldContainer[ApplicationDownlink]
    last_f_cnt_down: int
    session_key_id: bytes
    def __init__(self, downlinks: _Optional[_Iterable[_Union[ApplicationDownlink, _Mapping]]] = ..., last_f_cnt_down: _Optional[int] = ..., session_key_id: _Optional[bytes] = ...) -> None: ...

class DownlinkQueueOperationErrorDetails(_message.Message):
    __slots__ = ("dev_addr", "session_key_id", "min_f_cnt_down", "pending_dev_addr", "pending_session_key_id", "pending_min_f_cnt_down")
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    PENDING_DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    PENDING_SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    PENDING_MIN_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    session_key_id: bytes
    min_f_cnt_down: int
    pending_dev_addr: bytes
    pending_session_key_id: bytes
    pending_min_f_cnt_down: int
    def __init__(self, dev_addr: _Optional[bytes] = ..., session_key_id: _Optional[bytes] = ..., min_f_cnt_down: _Optional[int] = ..., pending_dev_addr: _Optional[bytes] = ..., pending_session_key_id: _Optional[bytes] = ..., pending_min_f_cnt_down: _Optional[int] = ...) -> None: ...

class ApplicationServiceData(_message.Message):
    __slots__ = ("service", "data")
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    service: str
    data: _struct_pb2.Struct
    def __init__(self, service: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ApplicationUp(_message.Message):
    __slots__ = ("end_device_ids", "correlation_ids", "received_at", "uplink_message", "uplink_normalized", "join_accept", "downlink_ack", "downlink_nack", "downlink_sent", "downlink_failed", "downlink_queued", "downlink_queue_invalidated", "location_solved", "service_data", "simulated")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    UPLINK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPLINK_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ACK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_NACK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_SENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FAILED_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_QUEUED_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_QUEUE_INVALIDATED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SOLVED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    SIMULATED_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    correlation_ids: _containers.RepeatedScalarFieldContainer[str]
    received_at: _timestamp_pb2.Timestamp
    uplink_message: ApplicationUplink
    uplink_normalized: ApplicationUplinkNormalized
    join_accept: ApplicationJoinAccept
    downlink_ack: ApplicationDownlink
    downlink_nack: ApplicationDownlink
    downlink_sent: ApplicationDownlink
    downlink_failed: ApplicationDownlinkFailed
    downlink_queued: ApplicationDownlink
    downlink_queue_invalidated: ApplicationInvalidatedDownlinks
    location_solved: ApplicationLocation
    service_data: ApplicationServiceData
    simulated: bool
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., uplink_message: _Optional[_Union[ApplicationUplink, _Mapping]] = ..., uplink_normalized: _Optional[_Union[ApplicationUplinkNormalized, _Mapping]] = ..., join_accept: _Optional[_Union[ApplicationJoinAccept, _Mapping]] = ..., downlink_ack: _Optional[_Union[ApplicationDownlink, _Mapping]] = ..., downlink_nack: _Optional[_Union[ApplicationDownlink, _Mapping]] = ..., downlink_sent: _Optional[_Union[ApplicationDownlink, _Mapping]] = ..., downlink_failed: _Optional[_Union[ApplicationDownlinkFailed, _Mapping]] = ..., downlink_queued: _Optional[_Union[ApplicationDownlink, _Mapping]] = ..., downlink_queue_invalidated: _Optional[_Union[ApplicationInvalidatedDownlinks, _Mapping]] = ..., location_solved: _Optional[_Union[ApplicationLocation, _Mapping]] = ..., service_data: _Optional[_Union[ApplicationServiceData, _Mapping]] = ..., simulated: bool = ...) -> None: ...

class MessagePayloadFormatters(_message.Message):
    __slots__ = ("up_formatter", "up_formatter_parameter", "down_formatter", "down_formatter_parameter")
    UP_FORMATTER_FIELD_NUMBER: _ClassVar[int]
    UP_FORMATTER_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    DOWN_FORMATTER_FIELD_NUMBER: _ClassVar[int]
    DOWN_FORMATTER_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    up_formatter: PayloadFormatter
    up_formatter_parameter: str
    down_formatter: PayloadFormatter
    down_formatter_parameter: str
    def __init__(self, up_formatter: _Optional[_Union[PayloadFormatter, str]] = ..., up_formatter_parameter: _Optional[str] = ..., down_formatter: _Optional[_Union[PayloadFormatter, str]] = ..., down_formatter_parameter: _Optional[str] = ...) -> None: ...

class DownlinkQueueRequest(_message.Message):
    __slots__ = ("end_device_ids", "downlinks")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    downlinks: _containers.RepeatedCompositeFieldContainer[ApplicationDownlink]
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., downlinks: _Optional[_Iterable[_Union[ApplicationDownlink, _Mapping]]] = ...) -> None: ...
