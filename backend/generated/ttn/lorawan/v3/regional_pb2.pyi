from google.protobuf import duration_pb2 as _duration_pb2
from ttn.lorawan.v3 import gateway_pb2 as _gateway_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConcentratorConfig(_message.Message):
    __slots__ = ("channels", "lora_standard_channel", "fsk_channel", "lbt", "ping_slot", "radios", "clock_source")
    class Channel(_message.Message):
        __slots__ = ("frequency", "radio")
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        RADIO_FIELD_NUMBER: _ClassVar[int]
        frequency: int
        radio: int
        def __init__(self, frequency: _Optional[int] = ..., radio: _Optional[int] = ...) -> None: ...
    class LoRaStandardChannel(_message.Message):
        __slots__ = ("frequency", "radio", "bandwidth", "spreading_factor")
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        RADIO_FIELD_NUMBER: _ClassVar[int]
        BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
        SPREADING_FACTOR_FIELD_NUMBER: _ClassVar[int]
        frequency: int
        radio: int
        bandwidth: int
        spreading_factor: int
        def __init__(self, frequency: _Optional[int] = ..., radio: _Optional[int] = ..., bandwidth: _Optional[int] = ..., spreading_factor: _Optional[int] = ...) -> None: ...
    class FSKChannel(_message.Message):
        __slots__ = ("frequency", "radio")
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        RADIO_FIELD_NUMBER: _ClassVar[int]
        frequency: int
        radio: int
        def __init__(self, frequency: _Optional[int] = ..., radio: _Optional[int] = ...) -> None: ...
    class LBTConfiguration(_message.Message):
        __slots__ = ("rssi_target", "rssi_offset", "scan_time")
        RSSI_TARGET_FIELD_NUMBER: _ClassVar[int]
        RSSI_OFFSET_FIELD_NUMBER: _ClassVar[int]
        SCAN_TIME_FIELD_NUMBER: _ClassVar[int]
        rssi_target: float
        rssi_offset: float
        scan_time: _duration_pb2.Duration
        def __init__(self, rssi_target: _Optional[float] = ..., rssi_offset: _Optional[float] = ..., scan_time: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    LORA_STANDARD_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FSK_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    LBT_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_FIELD_NUMBER: _ClassVar[int]
    RADIOS_FIELD_NUMBER: _ClassVar[int]
    CLOCK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[ConcentratorConfig.Channel]
    lora_standard_channel: ConcentratorConfig.LoRaStandardChannel
    fsk_channel: ConcentratorConfig.FSKChannel
    lbt: ConcentratorConfig.LBTConfiguration
    ping_slot: ConcentratorConfig.Channel
    radios: _containers.RepeatedCompositeFieldContainer[_gateway_pb2.GatewayRadio]
    clock_source: int
    def __init__(self, channels: _Optional[_Iterable[_Union[ConcentratorConfig.Channel, _Mapping]]] = ..., lora_standard_channel: _Optional[_Union[ConcentratorConfig.LoRaStandardChannel, _Mapping]] = ..., fsk_channel: _Optional[_Union[ConcentratorConfig.FSKChannel, _Mapping]] = ..., lbt: _Optional[_Union[ConcentratorConfig.LBTConfiguration, _Mapping]] = ..., ping_slot: _Optional[_Union[ConcentratorConfig.Channel, _Mapping]] = ..., radios: _Optional[_Iterable[_Union[_gateway_pb2.GatewayRadio, _Mapping]]] = ..., clock_source: _Optional[int] = ...) -> None: ...
