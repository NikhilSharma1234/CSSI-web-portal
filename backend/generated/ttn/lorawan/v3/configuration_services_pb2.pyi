from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListFrequencyPlansRequest(_message.Message):
    __slots__ = ("base_frequency", "band_id")
    BASE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    BAND_ID_FIELD_NUMBER: _ClassVar[int]
    base_frequency: int
    band_id: str
    def __init__(self, base_frequency: _Optional[int] = ..., band_id: _Optional[str] = ...) -> None: ...

class FrequencyPlanDescription(_message.Message):
    __slots__ = ("id", "base_id", "name", "base_frequency", "band_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    BASE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    BAND_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    base_id: str
    name: str
    base_frequency: int
    band_id: str
    def __init__(self, id: _Optional[str] = ..., base_id: _Optional[str] = ..., name: _Optional[str] = ..., base_frequency: _Optional[int] = ..., band_id: _Optional[str] = ...) -> None: ...

class ListFrequencyPlansResponse(_message.Message):
    __slots__ = ("frequency_plans",)
    FREQUENCY_PLANS_FIELD_NUMBER: _ClassVar[int]
    frequency_plans: _containers.RepeatedCompositeFieldContainer[FrequencyPlanDescription]
    def __init__(self, frequency_plans: _Optional[_Iterable[_Union[FrequencyPlanDescription, _Mapping]]] = ...) -> None: ...

class GetPhyVersionsRequest(_message.Message):
    __slots__ = ("band_id",)
    BAND_ID_FIELD_NUMBER: _ClassVar[int]
    band_id: str
    def __init__(self, band_id: _Optional[str] = ...) -> None: ...

class GetPhyVersionsResponse(_message.Message):
    __slots__ = ("version_info",)
    class VersionInfo(_message.Message):
        __slots__ = ("band_id", "phy_versions")
        BAND_ID_FIELD_NUMBER: _ClassVar[int]
        PHY_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        band_id: str
        phy_versions: _containers.RepeatedScalarFieldContainer[_lorawan_pb2.PHYVersion]
        def __init__(self, band_id: _Optional[str] = ..., phy_versions: _Optional[_Iterable[_Union[_lorawan_pb2.PHYVersion, str]]] = ...) -> None: ...
    VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    version_info: _containers.RepeatedCompositeFieldContainer[GetPhyVersionsResponse.VersionInfo]
    def __init__(self, version_info: _Optional[_Iterable[_Union[GetPhyVersionsResponse.VersionInfo, _Mapping]]] = ...) -> None: ...

class ListBandsRequest(_message.Message):
    __slots__ = ("band_id", "phy_version")
    BAND_ID_FIELD_NUMBER: _ClassVar[int]
    PHY_VERSION_FIELD_NUMBER: _ClassVar[int]
    band_id: str
    phy_version: _lorawan_pb2.PHYVersion
    def __init__(self, band_id: _Optional[str] = ..., phy_version: _Optional[_Union[_lorawan_pb2.PHYVersion, str]] = ...) -> None: ...

class BandDescription(_message.Message):
    __slots__ = ("id", "beacon", "ping_slot_frequencies", "max_uplink_channels", "uplink_channels", "max_downlink_channels", "downlink_channels", "sub_bands", "data_rates", "freq_multiplier", "implements_cf_list", "cf_list_type", "receive_delay_1", "receive_delay_2", "join_accept_delay_1", "join_accept_delay_2", "max_fcnt_gap", "supports_dynamic_adr", "adr_ack_limit", "min_retransmit_timeout", "max_retransmit_timeout", "tx_offset", "max_adr_data_rate_index", "relay_forward_delay", "relay_receive_delay", "tx_param_setup_req_support", "default_max_eirp", "default_rx2_parameters", "boot_dwell_time", "relay")
    class Beacon(_message.Message):
        __slots__ = ("data_rate_index", "coding_rate", "frequencies")
        DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        CODING_RATE_FIELD_NUMBER: _ClassVar[int]
        FREQUENCIES_FIELD_NUMBER: _ClassVar[int]
        data_rate_index: _lorawan_pb2.DataRateIndex
        coding_rate: str
        frequencies: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., coding_rate: _Optional[str] = ..., frequencies: _Optional[_Iterable[int]] = ...) -> None: ...
    class Channel(_message.Message):
        __slots__ = ("frequency", "min_data_rate", "max_data_rate")
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        MIN_DATA_RATE_FIELD_NUMBER: _ClassVar[int]
        MAX_DATA_RATE_FIELD_NUMBER: _ClassVar[int]
        frequency: int
        min_data_rate: _lorawan_pb2.DataRateIndex
        max_data_rate: _lorawan_pb2.DataRateIndex
        def __init__(self, frequency: _Optional[int] = ..., min_data_rate: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., max_data_rate: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ...) -> None: ...
    class SubBandParameters(_message.Message):
        __slots__ = ("min_frequency", "max_frequency", "duty_cycle", "max_eirp")
        MIN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        MAX_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        DUTY_CYCLE_FIELD_NUMBER: _ClassVar[int]
        MAX_EIRP_FIELD_NUMBER: _ClassVar[int]
        min_frequency: int
        max_frequency: int
        duty_cycle: float
        max_eirp: float
        def __init__(self, min_frequency: _Optional[int] = ..., max_frequency: _Optional[int] = ..., duty_cycle: _Optional[float] = ..., max_eirp: _Optional[float] = ...) -> None: ...
    class BandDataRate(_message.Message):
        __slots__ = ("rate",)
        RATE_FIELD_NUMBER: _ClassVar[int]
        rate: _lorawan_pb2.DataRate
        def __init__(self, rate: _Optional[_Union[_lorawan_pb2.DataRate, _Mapping]] = ...) -> None: ...
    class DataRatesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BandDescription.BandDataRate
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BandDescription.BandDataRate, _Mapping]] = ...) -> None: ...
    class Rx2Parameters(_message.Message):
        __slots__ = ("data_rate_index", "frequency")
        DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        data_rate_index: _lorawan_pb2.DataRateIndex
        frequency: int
        def __init__(self, data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., frequency: _Optional[int] = ...) -> None: ...
    class DwellTime(_message.Message):
        __slots__ = ("uplinks", "downlinks")
        UPLINKS_FIELD_NUMBER: _ClassVar[int]
        DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
        uplinks: _wrappers_pb2.BoolValue
        downlinks: _wrappers_pb2.BoolValue
        def __init__(self, uplinks: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., downlinks: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class RelayParameters(_message.Message):
        __slots__ = ("wor_channels",)
        class RelayWORChannel(_message.Message):
            __slots__ = ("frequency", "ack_frequency", "data_rate_index")
            FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            ACK_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
            frequency: int
            ack_frequency: int
            data_rate_index: _lorawan_pb2.DataRateIndex
            def __init__(self, frequency: _Optional[int] = ..., ack_frequency: _Optional[int] = ..., data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ...) -> None: ...
        WOR_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        wor_channels: _containers.RepeatedCompositeFieldContainer[BandDescription.RelayParameters.RelayWORChannel]
        def __init__(self, wor_channels: _Optional[_Iterable[_Union[BandDescription.RelayParameters.RelayWORChannel, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    BEACON_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_FREQUENCIES_FIELD_NUMBER: _ClassVar[int]
    MAX_UPLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    UPLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    MAX_DOWNLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SUB_BANDS_FIELD_NUMBER: _ClassVar[int]
    DATA_RATES_FIELD_NUMBER: _ClassVar[int]
    FREQ_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    IMPLEMENTS_CF_LIST_FIELD_NUMBER: _ClassVar[int]
    CF_LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_DELAY_1_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_DELAY_2_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_DELAY_1_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_DELAY_2_FIELD_NUMBER: _ClassVar[int]
    MAX_FCNT_GAP_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_DYNAMIC_ADR_FIELD_NUMBER: _ClassVar[int]
    ADR_ACK_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MIN_RETRANSMIT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_RETRANSMIT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MAX_ADR_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    RELAY_FORWARD_DELAY_FIELD_NUMBER: _ClassVar[int]
    RELAY_RECEIVE_DELAY_FIELD_NUMBER: _ClassVar[int]
    TX_PARAM_SETUP_REQ_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MAX_EIRP_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_RX2_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    BOOT_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    id: str
    beacon: BandDescription.Beacon
    ping_slot_frequencies: _containers.RepeatedScalarFieldContainer[int]
    max_uplink_channels: int
    uplink_channels: _containers.RepeatedCompositeFieldContainer[BandDescription.Channel]
    max_downlink_channels: int
    downlink_channels: _containers.RepeatedCompositeFieldContainer[BandDescription.Channel]
    sub_bands: _containers.RepeatedCompositeFieldContainer[BandDescription.SubBandParameters]
    data_rates: _containers.MessageMap[int, BandDescription.BandDataRate]
    freq_multiplier: int
    implements_cf_list: bool
    cf_list_type: _lorawan_pb2.CFListType
    receive_delay_1: _duration_pb2.Duration
    receive_delay_2: _duration_pb2.Duration
    join_accept_delay_1: _duration_pb2.Duration
    join_accept_delay_2: _duration_pb2.Duration
    max_fcnt_gap: int
    supports_dynamic_adr: bool
    adr_ack_limit: _lorawan_pb2.ADRAckLimitExponent
    min_retransmit_timeout: _duration_pb2.Duration
    max_retransmit_timeout: _duration_pb2.Duration
    tx_offset: _containers.RepeatedScalarFieldContainer[float]
    max_adr_data_rate_index: _lorawan_pb2.DataRateIndex
    relay_forward_delay: _duration_pb2.Duration
    relay_receive_delay: _duration_pb2.Duration
    tx_param_setup_req_support: bool
    default_max_eirp: float
    default_rx2_parameters: BandDescription.Rx2Parameters
    boot_dwell_time: BandDescription.DwellTime
    relay: BandDescription.RelayParameters
    def __init__(self, id: _Optional[str] = ..., beacon: _Optional[_Union[BandDescription.Beacon, _Mapping]] = ..., ping_slot_frequencies: _Optional[_Iterable[int]] = ..., max_uplink_channels: _Optional[int] = ..., uplink_channels: _Optional[_Iterable[_Union[BandDescription.Channel, _Mapping]]] = ..., max_downlink_channels: _Optional[int] = ..., downlink_channels: _Optional[_Iterable[_Union[BandDescription.Channel, _Mapping]]] = ..., sub_bands: _Optional[_Iterable[_Union[BandDescription.SubBandParameters, _Mapping]]] = ..., data_rates: _Optional[_Mapping[int, BandDescription.BandDataRate]] = ..., freq_multiplier: _Optional[int] = ..., implements_cf_list: bool = ..., cf_list_type: _Optional[_Union[_lorawan_pb2.CFListType, str]] = ..., receive_delay_1: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., receive_delay_2: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., join_accept_delay_1: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., join_accept_delay_2: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_fcnt_gap: _Optional[int] = ..., supports_dynamic_adr: bool = ..., adr_ack_limit: _Optional[_Union[_lorawan_pb2.ADRAckLimitExponent, str]] = ..., min_retransmit_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max_retransmit_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., tx_offset: _Optional[_Iterable[float]] = ..., max_adr_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., relay_forward_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., relay_receive_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., tx_param_setup_req_support: bool = ..., default_max_eirp: _Optional[float] = ..., default_rx2_parameters: _Optional[_Union[BandDescription.Rx2Parameters, _Mapping]] = ..., boot_dwell_time: _Optional[_Union[BandDescription.DwellTime, _Mapping]] = ..., relay: _Optional[_Union[BandDescription.RelayParameters, _Mapping]] = ...) -> None: ...

class ListBandsResponse(_message.Message):
    __slots__ = ("descriptions",)
    class VersionedBandDescription(_message.Message):
        __slots__ = ("band",)
        class BandEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: BandDescription
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BandDescription, _Mapping]] = ...) -> None: ...
        BAND_FIELD_NUMBER: _ClassVar[int]
        band: _containers.MessageMap[str, BandDescription]
        def __init__(self, band: _Optional[_Mapping[str, BandDescription]] = ...) -> None: ...
    class DescriptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListBandsResponse.VersionedBandDescription
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListBandsResponse.VersionedBandDescription, _Mapping]] = ...) -> None: ...
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    descriptions: _containers.MessageMap[str, ListBandsResponse.VersionedBandDescription]
    def __init__(self, descriptions: _Optional[_Mapping[str, ListBandsResponse.VersionedBandDescription]] = ...) -> None: ...
