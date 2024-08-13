from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from ttn.lorawan.v3 import error_pb2 as _error_pb2
from ttn.lorawan.v3 import gateway_pb2 as _gateway_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from ttn.lorawan.v3 import messages_pb2 as _messages_pb2
from ttn.lorawan.v3 import mqtt_pb2 as _mqtt_pb2
from ttn.lorawan.v3 import regional_pb2 as _regional_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GatewayUp(_message.Message):
    __slots__ = ("uplink_messages", "gateway_status", "tx_acknowledgment")
    UPLINK_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_STATUS_FIELD_NUMBER: _ClassVar[int]
    TX_ACKNOWLEDGMENT_FIELD_NUMBER: _ClassVar[int]
    uplink_messages: _containers.RepeatedCompositeFieldContainer[_messages_pb2.UplinkMessage]
    gateway_status: _gateway_pb2.GatewayStatus
    tx_acknowledgment: _messages_pb2.TxAcknowledgment
    def __init__(self, uplink_messages: _Optional[_Iterable[_Union[_messages_pb2.UplinkMessage, _Mapping]]] = ..., gateway_status: _Optional[_Union[_gateway_pb2.GatewayStatus, _Mapping]] = ..., tx_acknowledgment: _Optional[_Union[_messages_pb2.TxAcknowledgment, _Mapping]] = ...) -> None: ...

class GatewayDown(_message.Message):
    __slots__ = ("downlink_message",)
    DOWNLINK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    downlink_message: _messages_pb2.DownlinkMessage
    def __init__(self, downlink_message: _Optional[_Union[_messages_pb2.DownlinkMessage, _Mapping]] = ...) -> None: ...

class ScheduleDownlinkResponse(_message.Message):
    __slots__ = ("delay", "downlink_path", "rx1", "rx2")
    DELAY_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_PATH_FIELD_NUMBER: _ClassVar[int]
    RX1_FIELD_NUMBER: _ClassVar[int]
    RX2_FIELD_NUMBER: _ClassVar[int]
    delay: _duration_pb2.Duration
    downlink_path: _lorawan_pb2.DownlinkPath
    rx1: bool
    rx2: bool
    def __init__(self, delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., downlink_path: _Optional[_Union[_lorawan_pb2.DownlinkPath, _Mapping]] = ..., rx1: bool = ..., rx2: bool = ...) -> None: ...

class ScheduleDownlinkErrorDetails(_message.Message):
    __slots__ = ("path_errors",)
    PATH_ERRORS_FIELD_NUMBER: _ClassVar[int]
    path_errors: _containers.RepeatedCompositeFieldContainer[_error_pb2.ErrorDetails]
    def __init__(self, path_errors: _Optional[_Iterable[_Union[_error_pb2.ErrorDetails, _Mapping]]] = ...) -> None: ...

class BatchGetGatewayConnectionStatsRequest(_message.Message):
    __slots__ = ("gateway_ids", "field_mask")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.GatewayIdentifiers]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway_ids: _Optional[_Iterable[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class BatchGetGatewayConnectionStatsResponse(_message.Message):
    __slots__ = ("entries",)
    class EntriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _gateway_pb2.GatewayConnectionStats
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_gateway_pb2.GatewayConnectionStats, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.MessageMap[str, _gateway_pb2.GatewayConnectionStats]
    def __init__(self, entries: _Optional[_Mapping[str, _gateway_pb2.GatewayConnectionStats]] = ...) -> None: ...
