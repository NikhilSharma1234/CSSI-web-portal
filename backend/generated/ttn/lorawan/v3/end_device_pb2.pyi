from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import keys_pb2 as _keys_pb2
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from ttn.lorawan.v3 import messages_pb2 as _messages_pb2
from ttn.lorawan.v3 import metadata_pb2 as _metadata_pb2
from ttn.lorawan.v3 import picture_pb2 as _picture_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POWER_UNKNOWN: _ClassVar[PowerState]
    POWER_BATTERY: _ClassVar[PowerState]
    POWER_EXTERNAL: _ClassVar[PowerState]
POWER_UNKNOWN: PowerState
POWER_BATTERY: PowerState
POWER_EXTERNAL: PowerState

class Session(_message.Message):
    __slots__ = ("dev_addr", "keys", "last_f_cnt_up", "last_n_f_cnt_down", "last_a_f_cnt_down", "last_conf_f_cnt_down", "started_at", "queued_application_downlinks")
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    LAST_F_CNT_UP_FIELD_NUMBER: _ClassVar[int]
    LAST_N_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    LAST_A_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    LAST_CONF_F_CNT_DOWN_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    QUEUED_APPLICATION_DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    keys: _keys_pb2.SessionKeys
    last_f_cnt_up: int
    last_n_f_cnt_down: int
    last_a_f_cnt_down: int
    last_conf_f_cnt_down: int
    started_at: _timestamp_pb2.Timestamp
    queued_application_downlinks: _containers.RepeatedCompositeFieldContainer[_messages_pb2.ApplicationDownlink]
    def __init__(self, dev_addr: _Optional[bytes] = ..., keys: _Optional[_Union[_keys_pb2.SessionKeys, _Mapping]] = ..., last_f_cnt_up: _Optional[int] = ..., last_n_f_cnt_down: _Optional[int] = ..., last_a_f_cnt_down: _Optional[int] = ..., last_conf_f_cnt_down: _Optional[int] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., queued_application_downlinks: _Optional[_Iterable[_Union[_messages_pb2.ApplicationDownlink, _Mapping]]] = ...) -> None: ...

class BoolValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class ServingRelayForwardingLimits(_message.Message):
    __slots__ = ("reset_behavior", "join_requests", "notifications", "uplink_messages", "overall")
    RESET_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    JOIN_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    UPLINK_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    OVERALL_FIELD_NUMBER: _ClassVar[int]
    reset_behavior: _lorawan_pb2.RelayResetLimitCounter
    join_requests: _lorawan_pb2.RelayForwardLimits
    notifications: _lorawan_pb2.RelayForwardLimits
    uplink_messages: _lorawan_pb2.RelayForwardLimits
    overall: _lorawan_pb2.RelayForwardLimits
    def __init__(self, reset_behavior: _Optional[_Union[_lorawan_pb2.RelayResetLimitCounter, str]] = ..., join_requests: _Optional[_Union[_lorawan_pb2.RelayForwardLimits, _Mapping]] = ..., notifications: _Optional[_Union[_lorawan_pb2.RelayForwardLimits, _Mapping]] = ..., uplink_messages: _Optional[_Union[_lorawan_pb2.RelayForwardLimits, _Mapping]] = ..., overall: _Optional[_Union[_lorawan_pb2.RelayForwardLimits, _Mapping]] = ...) -> None: ...

class RelayUplinkForwardingRule(_message.Message):
    __slots__ = ("limits", "last_w_f_cnt", "device_id", "session_key_id")
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    LAST_W_F_CNT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    limits: _lorawan_pb2.RelayUplinkForwardLimits
    last_w_f_cnt: int
    device_id: str
    session_key_id: bytes
    def __init__(self, limits: _Optional[_Union[_lorawan_pb2.RelayUplinkForwardLimits, _Mapping]] = ..., last_w_f_cnt: _Optional[int] = ..., device_id: _Optional[str] = ..., session_key_id: _Optional[bytes] = ...) -> None: ...

class ServingRelayParameters(_message.Message):
    __slots__ = ("second_channel", "default_channel_index", "cad_periodicity", "uplink_forwarding_rules", "limits")
    SECOND_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    CAD_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    UPLINK_FORWARDING_RULES_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    second_channel: _lorawan_pb2.RelaySecondChannel
    default_channel_index: int
    cad_periodicity: _lorawan_pb2.RelayCADPeriodicity
    uplink_forwarding_rules: _containers.RepeatedCompositeFieldContainer[RelayUplinkForwardingRule]
    limits: ServingRelayForwardingLimits
    def __init__(self, second_channel: _Optional[_Union[_lorawan_pb2.RelaySecondChannel, _Mapping]] = ..., default_channel_index: _Optional[int] = ..., cad_periodicity: _Optional[_Union[_lorawan_pb2.RelayCADPeriodicity, str]] = ..., uplink_forwarding_rules: _Optional[_Iterable[_Union[RelayUplinkForwardingRule, _Mapping]]] = ..., limits: _Optional[_Union[ServingRelayForwardingLimits, _Mapping]] = ...) -> None: ...

class ServedRelayParameters(_message.Message):
    __slots__ = ("always", "dynamic", "end_device_controlled", "backoff", "second_channel", "serving_device_id")
    ALWAYS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_CONTROLLED_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_FIELD_NUMBER: _ClassVar[int]
    SECOND_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SERVING_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    always: _lorawan_pb2.RelayEndDeviceAlwaysMode
    dynamic: _lorawan_pb2.RelayEndDeviceDynamicMode
    end_device_controlled: _lorawan_pb2.RelayEndDeviceControlledMode
    backoff: int
    second_channel: _lorawan_pb2.RelaySecondChannel
    serving_device_id: str
    def __init__(self, always: _Optional[_Union[_lorawan_pb2.RelayEndDeviceAlwaysMode, _Mapping]] = ..., dynamic: _Optional[_Union[_lorawan_pb2.RelayEndDeviceDynamicMode, _Mapping]] = ..., end_device_controlled: _Optional[_Union[_lorawan_pb2.RelayEndDeviceControlledMode, _Mapping]] = ..., backoff: _Optional[int] = ..., second_channel: _Optional[_Union[_lorawan_pb2.RelaySecondChannel, _Mapping]] = ..., serving_device_id: _Optional[str] = ...) -> None: ...

class RelayParameters(_message.Message):
    __slots__ = ("serving", "served")
    SERVING_FIELD_NUMBER: _ClassVar[int]
    SERVED_FIELD_NUMBER: _ClassVar[int]
    serving: ServingRelayParameters
    served: ServedRelayParameters
    def __init__(self, serving: _Optional[_Union[ServingRelayParameters, _Mapping]] = ..., served: _Optional[_Union[ServedRelayParameters, _Mapping]] = ...) -> None: ...

class ServingRelaySettings(_message.Message):
    __slots__ = ("second_channel", "default_channel_index", "cad_periodicity", "uplink_forwarding_rules", "limits")
    SECOND_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    CAD_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    UPLINK_FORWARDING_RULES_FIELD_NUMBER: _ClassVar[int]
    LIMITS_FIELD_NUMBER: _ClassVar[int]
    second_channel: _lorawan_pb2.RelaySecondChannel
    default_channel_index: _wrappers_pb2.UInt32Value
    cad_periodicity: _lorawan_pb2.RelayCADPeriodicity
    uplink_forwarding_rules: _containers.RepeatedCompositeFieldContainer[RelayUplinkForwardingRule]
    limits: ServingRelayForwardingLimits
    def __init__(self, second_channel: _Optional[_Union[_lorawan_pb2.RelaySecondChannel, _Mapping]] = ..., default_channel_index: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., cad_periodicity: _Optional[_Union[_lorawan_pb2.RelayCADPeriodicity, str]] = ..., uplink_forwarding_rules: _Optional[_Iterable[_Union[RelayUplinkForwardingRule, _Mapping]]] = ..., limits: _Optional[_Union[ServingRelayForwardingLimits, _Mapping]] = ...) -> None: ...

class ServedRelaySettings(_message.Message):
    __slots__ = ("always", "dynamic", "end_device_controlled", "backoff", "second_channel", "serving_device_id")
    ALWAYS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_CONTROLLED_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_FIELD_NUMBER: _ClassVar[int]
    SECOND_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    SERVING_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    always: _lorawan_pb2.RelayEndDeviceAlwaysMode
    dynamic: _lorawan_pb2.RelayEndDeviceDynamicMode
    end_device_controlled: _lorawan_pb2.RelayEndDeviceControlledMode
    backoff: _wrappers_pb2.UInt32Value
    second_channel: _lorawan_pb2.RelaySecondChannel
    serving_device_id: str
    def __init__(self, always: _Optional[_Union[_lorawan_pb2.RelayEndDeviceAlwaysMode, _Mapping]] = ..., dynamic: _Optional[_Union[_lorawan_pb2.RelayEndDeviceDynamicMode, _Mapping]] = ..., end_device_controlled: _Optional[_Union[_lorawan_pb2.RelayEndDeviceControlledMode, _Mapping]] = ..., backoff: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., second_channel: _Optional[_Union[_lorawan_pb2.RelaySecondChannel, _Mapping]] = ..., serving_device_id: _Optional[str] = ...) -> None: ...

class RelaySettings(_message.Message):
    __slots__ = ("serving", "served")
    SERVING_FIELD_NUMBER: _ClassVar[int]
    SERVED_FIELD_NUMBER: _ClassVar[int]
    serving: ServingRelaySettings
    served: ServedRelaySettings
    def __init__(self, serving: _Optional[_Union[ServingRelaySettings, _Mapping]] = ..., served: _Optional[_Union[ServedRelaySettings, _Mapping]] = ...) -> None: ...

class MACParameters(_message.Message):
    __slots__ = ("max_eirp", "adr_data_rate_index", "adr_tx_power_index", "adr_nb_trans", "adr_ack_limit", "adr_ack_delay", "rx1_delay", "rx1_data_rate_offset", "rx2_data_rate_index", "rx2_frequency", "max_duty_cycle", "rejoin_time_periodicity", "rejoin_count_periodicity", "ping_slot_frequency", "ping_slot_data_rate_index", "beacon_frequency", "channels", "uplink_dwell_time", "downlink_dwell_time", "adr_ack_limit_exponent", "adr_ack_delay_exponent", "ping_slot_data_rate_index_value", "relay")
    class Channel(_message.Message):
        __slots__ = ("uplink_frequency", "downlink_frequency", "min_data_rate_index", "max_data_rate_index", "enable_uplink")
        UPLINK_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        DOWNLINK_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        MIN_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        ENABLE_UPLINK_FIELD_NUMBER: _ClassVar[int]
        uplink_frequency: int
        downlink_frequency: int
        min_data_rate_index: _lorawan_pb2.DataRateIndex
        max_data_rate_index: _lorawan_pb2.DataRateIndex
        enable_uplink: bool
        def __init__(self, uplink_frequency: _Optional[int] = ..., downlink_frequency: _Optional[int] = ..., min_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., max_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., enable_uplink: bool = ...) -> None: ...
    MAX_EIRP_FIELD_NUMBER: _ClassVar[int]
    ADR_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ADR_TX_POWER_INDEX_FIELD_NUMBER: _ClassVar[int]
    ADR_NB_TRANS_FIELD_NUMBER: _ClassVar[int]
    ADR_ACK_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ADR_ACK_DELAY_FIELD_NUMBER: _ClassVar[int]
    RX1_DELAY_FIELD_NUMBER: _ClassVar[int]
    RX1_DATA_RATE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RX2_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    RX2_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MAX_DUTY_CYCLE_FIELD_NUMBER: _ClassVar[int]
    REJOIN_TIME_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    REJOIN_COUNT_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BEACON_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    UPLINK_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
    ADR_ACK_LIMIT_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    ADR_ACK_DELAY_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_DATA_RATE_INDEX_VALUE_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    max_eirp: float
    adr_data_rate_index: _lorawan_pb2.DataRateIndex
    adr_tx_power_index: int
    adr_nb_trans: int
    adr_ack_limit: int
    adr_ack_delay: int
    rx1_delay: _lorawan_pb2.RxDelay
    rx1_data_rate_offset: _lorawan_pb2.DataRateOffset
    rx2_data_rate_index: _lorawan_pb2.DataRateIndex
    rx2_frequency: int
    max_duty_cycle: _lorawan_pb2.AggregatedDutyCycle
    rejoin_time_periodicity: _lorawan_pb2.RejoinTimeExponent
    rejoin_count_periodicity: _lorawan_pb2.RejoinCountExponent
    ping_slot_frequency: int
    ping_slot_data_rate_index: _lorawan_pb2.DataRateIndex
    beacon_frequency: int
    channels: _containers.RepeatedCompositeFieldContainer[MACParameters.Channel]
    uplink_dwell_time: BoolValue
    downlink_dwell_time: BoolValue
    adr_ack_limit_exponent: _lorawan_pb2.ADRAckLimitExponentValue
    adr_ack_delay_exponent: _lorawan_pb2.ADRAckDelayExponentValue
    ping_slot_data_rate_index_value: _lorawan_pb2.DataRateIndexValue
    relay: RelayParameters
    def __init__(self, max_eirp: _Optional[float] = ..., adr_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., adr_tx_power_index: _Optional[int] = ..., adr_nb_trans: _Optional[int] = ..., adr_ack_limit: _Optional[int] = ..., adr_ack_delay: _Optional[int] = ..., rx1_delay: _Optional[_Union[_lorawan_pb2.RxDelay, str]] = ..., rx1_data_rate_offset: _Optional[_Union[_lorawan_pb2.DataRateOffset, str]] = ..., rx2_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., rx2_frequency: _Optional[int] = ..., max_duty_cycle: _Optional[_Union[_lorawan_pb2.AggregatedDutyCycle, str]] = ..., rejoin_time_periodicity: _Optional[_Union[_lorawan_pb2.RejoinTimeExponent, str]] = ..., rejoin_count_periodicity: _Optional[_Union[_lorawan_pb2.RejoinCountExponent, str]] = ..., ping_slot_frequency: _Optional[int] = ..., ping_slot_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., beacon_frequency: _Optional[int] = ..., channels: _Optional[_Iterable[_Union[MACParameters.Channel, _Mapping]]] = ..., uplink_dwell_time: _Optional[_Union[BoolValue, _Mapping]] = ..., downlink_dwell_time: _Optional[_Union[BoolValue, _Mapping]] = ..., adr_ack_limit_exponent: _Optional[_Union[_lorawan_pb2.ADRAckLimitExponentValue, _Mapping]] = ..., adr_ack_delay_exponent: _Optional[_Union[_lorawan_pb2.ADRAckDelayExponentValue, _Mapping]] = ..., ping_slot_data_rate_index_value: _Optional[_Union[_lorawan_pb2.DataRateIndexValue, _Mapping]] = ..., relay: _Optional[_Union[RelayParameters, _Mapping]] = ...) -> None: ...

class EndDeviceVersion(_message.Message):
    __slots__ = ("ids", "lorawan_version", "lorawan_phy_version", "frequency_plan_id", "photos", "supports_class_b", "supports_class_c", "default_mac_settings", "min_frequency", "max_frequency", "supports_join", "resets_join_nonces", "default_formatters")
    IDS_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_VERSION_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_PHY_VERSION_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_B_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_C_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MAC_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MIN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MAX_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_JOIN_FIELD_NUMBER: _ClassVar[int]
    RESETS_JOIN_NONCES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FORMATTERS_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    lorawan_version: _lorawan_pb2.MACVersion
    lorawan_phy_version: _lorawan_pb2.PHYVersion
    frequency_plan_id: str
    photos: _containers.RepeatedScalarFieldContainer[str]
    supports_class_b: bool
    supports_class_c: bool
    default_mac_settings: MACSettings
    min_frequency: int
    max_frequency: int
    supports_join: bool
    resets_join_nonces: bool
    default_formatters: _messages_pb2.MessagePayloadFormatters
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., lorawan_version: _Optional[_Union[_lorawan_pb2.MACVersion, str]] = ..., lorawan_phy_version: _Optional[_Union[_lorawan_pb2.PHYVersion, str]] = ..., frequency_plan_id: _Optional[str] = ..., photos: _Optional[_Iterable[str]] = ..., supports_class_b: bool = ..., supports_class_c: bool = ..., default_mac_settings: _Optional[_Union[MACSettings, _Mapping]] = ..., min_frequency: _Optional[int] = ..., max_frequency: _Optional[int] = ..., supports_join: bool = ..., resets_join_nonces: bool = ..., default_formatters: _Optional[_Union[_messages_pb2.MessagePayloadFormatters, _Mapping]] = ...) -> None: ...

class ADRSettings(_message.Message):
    __slots__ = ("static", "dynamic", "disabled")
    class StaticMode(_message.Message):
        __slots__ = ("data_rate_index", "tx_power_index", "nb_trans")
        DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        TX_POWER_INDEX_FIELD_NUMBER: _ClassVar[int]
        NB_TRANS_FIELD_NUMBER: _ClassVar[int]
        data_rate_index: _lorawan_pb2.DataRateIndex
        tx_power_index: int
        nb_trans: int
        def __init__(self, data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., tx_power_index: _Optional[int] = ..., nb_trans: _Optional[int] = ...) -> None: ...
    class DynamicMode(_message.Message):
        __slots__ = ("margin", "min_data_rate_index", "max_data_rate_index", "min_tx_power_index", "max_tx_power_index", "min_nb_trans", "max_nb_trans", "channel_steering", "overrides")
        class ChannelSteeringSettings(_message.Message):
            __slots__ = ("lora_narrow", "disabled")
            class LoRaNarrowMode(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class DisabledMode(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            LORA_NARROW_FIELD_NUMBER: _ClassVar[int]
            DISABLED_FIELD_NUMBER: _ClassVar[int]
            lora_narrow: ADRSettings.DynamicMode.ChannelSteeringSettings.LoRaNarrowMode
            disabled: ADRSettings.DynamicMode.ChannelSteeringSettings.DisabledMode
            def __init__(self, lora_narrow: _Optional[_Union[ADRSettings.DynamicMode.ChannelSteeringSettings.LoRaNarrowMode, _Mapping]] = ..., disabled: _Optional[_Union[ADRSettings.DynamicMode.ChannelSteeringSettings.DisabledMode, _Mapping]] = ...) -> None: ...
        class PerDataRateIndexOverride(_message.Message):
            __slots__ = ("min_nb_trans", "max_nb_trans")
            MIN_NB_TRANS_FIELD_NUMBER: _ClassVar[int]
            MAX_NB_TRANS_FIELD_NUMBER: _ClassVar[int]
            min_nb_trans: _wrappers_pb2.UInt32Value
            max_nb_trans: _wrappers_pb2.UInt32Value
            def __init__(self, min_nb_trans: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., max_nb_trans: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
        class Overrides(_message.Message):
            __slots__ = ("data_rate_0", "data_rate_1", "data_rate_2", "data_rate_3", "data_rate_4", "data_rate_5", "data_rate_6", "data_rate_7", "data_rate_8", "data_rate_9", "data_rate_10", "data_rate_11", "data_rate_12", "data_rate_13", "data_rate_14", "data_rate_15")
            DATA_RATE_0_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_1_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_2_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_3_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_4_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_5_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_6_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_7_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_8_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_9_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_10_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_11_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_12_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_13_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_14_FIELD_NUMBER: _ClassVar[int]
            DATA_RATE_15_FIELD_NUMBER: _ClassVar[int]
            data_rate_0: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_1: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_2: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_3: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_4: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_5: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_6: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_7: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_8: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_9: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_10: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_11: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_12: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_13: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_14: ADRSettings.DynamicMode.PerDataRateIndexOverride
            data_rate_15: ADRSettings.DynamicMode.PerDataRateIndexOverride
            def __init__(self, data_rate_0: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_1: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_2: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_3: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_4: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_5: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_6: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_7: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_8: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_9: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_10: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_11: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_12: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_13: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_14: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ..., data_rate_15: _Optional[_Union[ADRSettings.DynamicMode.PerDataRateIndexOverride, _Mapping]] = ...) -> None: ...
        MARGIN_FIELD_NUMBER: _ClassVar[int]
        MIN_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        MIN_TX_POWER_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_TX_POWER_INDEX_FIELD_NUMBER: _ClassVar[int]
        MIN_NB_TRANS_FIELD_NUMBER: _ClassVar[int]
        MAX_NB_TRANS_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_STEERING_FIELD_NUMBER: _ClassVar[int]
        OVERRIDES_FIELD_NUMBER: _ClassVar[int]
        margin: _wrappers_pb2.FloatValue
        min_data_rate_index: _lorawan_pb2.DataRateIndexValue
        max_data_rate_index: _lorawan_pb2.DataRateIndexValue
        min_tx_power_index: _wrappers_pb2.UInt32Value
        max_tx_power_index: _wrappers_pb2.UInt32Value
        min_nb_trans: _wrappers_pb2.UInt32Value
        max_nb_trans: _wrappers_pb2.UInt32Value
        channel_steering: ADRSettings.DynamicMode.ChannelSteeringSettings
        overrides: ADRSettings.DynamicMode.Overrides
        def __init__(self, margin: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., min_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndexValue, _Mapping]] = ..., max_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndexValue, _Mapping]] = ..., min_tx_power_index: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., max_tx_power_index: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., min_nb_trans: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., max_nb_trans: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., channel_steering: _Optional[_Union[ADRSettings.DynamicMode.ChannelSteeringSettings, _Mapping]] = ..., overrides: _Optional[_Union[ADRSettings.DynamicMode.Overrides, _Mapping]] = ...) -> None: ...
    class DisabledMode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    STATIC_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    static: ADRSettings.StaticMode
    dynamic: ADRSettings.DynamicMode
    disabled: ADRSettings.DisabledMode
    def __init__(self, static: _Optional[_Union[ADRSettings.StaticMode, _Mapping]] = ..., dynamic: _Optional[_Union[ADRSettings.DynamicMode, _Mapping]] = ..., disabled: _Optional[_Union[ADRSettings.DisabledMode, _Mapping]] = ...) -> None: ...

class MACSettings(_message.Message):
    __slots__ = ("class_b_timeout", "ping_slot_periodicity", "ping_slot_data_rate_index", "ping_slot_frequency", "beacon_frequency", "class_c_timeout", "rx1_delay", "rx1_data_rate_offset", "rx2_data_rate_index", "rx2_frequency", "factory_preset_frequencies", "max_duty_cycle", "supports_32_bit_f_cnt", "use_adr", "adr_margin", "resets_f_cnt", "status_time_periodicity", "status_count_periodicity", "desired_rx1_delay", "desired_rx1_data_rate_offset", "desired_rx2_data_rate_index", "desired_rx2_frequency", "desired_max_duty_cycle", "desired_adr_ack_limit_exponent", "desired_adr_ack_delay_exponent", "desired_ping_slot_data_rate_index", "desired_ping_slot_frequency", "desired_beacon_frequency", "desired_max_eirp", "class_b_c_downlink_interval", "uplink_dwell_time", "downlink_dwell_time", "adr", "schedule_downlinks", "relay", "desired_relay")
    CLASS_B_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    BEACON_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CLASS_C_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RX1_DELAY_FIELD_NUMBER: _ClassVar[int]
    RX1_DATA_RATE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RX2_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    RX2_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    FACTORY_PRESET_FREQUENCIES_FIELD_NUMBER: _ClassVar[int]
    MAX_DUTY_CYCLE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_32_BIT_F_CNT_FIELD_NUMBER: _ClassVar[int]
    USE_ADR_FIELD_NUMBER: _ClassVar[int]
    ADR_MARGIN_FIELD_NUMBER: _ClassVar[int]
    RESETS_F_CNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_TIME_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_COUNT_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RX1_DELAY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RX1_DATA_RATE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RX2_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RX2_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MAX_DUTY_CYCLE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ADR_ACK_LIMIT_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_ADR_ACK_DELAY_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_PING_SLOT_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DESIRED_PING_SLOT_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_BEACON_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MAX_EIRP_FIELD_NUMBER: _ClassVar[int]
    CLASS_B_C_DOWNLINK_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    UPLINK_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
    ADR_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    DESIRED_RELAY_FIELD_NUMBER: _ClassVar[int]
    class_b_timeout: _duration_pb2.Duration
    ping_slot_periodicity: _lorawan_pb2.PingSlotPeriodValue
    ping_slot_data_rate_index: _lorawan_pb2.DataRateIndexValue
    ping_slot_frequency: _lorawan_pb2.ZeroableFrequencyValue
    beacon_frequency: _lorawan_pb2.ZeroableFrequencyValue
    class_c_timeout: _duration_pb2.Duration
    rx1_delay: _lorawan_pb2.RxDelayValue
    rx1_data_rate_offset: _lorawan_pb2.DataRateOffsetValue
    rx2_data_rate_index: _lorawan_pb2.DataRateIndexValue
    rx2_frequency: _lorawan_pb2.FrequencyValue
    factory_preset_frequencies: _containers.RepeatedScalarFieldContainer[int]
    max_duty_cycle: _lorawan_pb2.AggregatedDutyCycleValue
    supports_32_bit_f_cnt: BoolValue
    use_adr: BoolValue
    adr_margin: _wrappers_pb2.FloatValue
    resets_f_cnt: BoolValue
    status_time_periodicity: _duration_pb2.Duration
    status_count_periodicity: _wrappers_pb2.UInt32Value
    desired_rx1_delay: _lorawan_pb2.RxDelayValue
    desired_rx1_data_rate_offset: _lorawan_pb2.DataRateOffsetValue
    desired_rx2_data_rate_index: _lorawan_pb2.DataRateIndexValue
    desired_rx2_frequency: _lorawan_pb2.FrequencyValue
    desired_max_duty_cycle: _lorawan_pb2.AggregatedDutyCycleValue
    desired_adr_ack_limit_exponent: _lorawan_pb2.ADRAckLimitExponentValue
    desired_adr_ack_delay_exponent: _lorawan_pb2.ADRAckDelayExponentValue
    desired_ping_slot_data_rate_index: _lorawan_pb2.DataRateIndexValue
    desired_ping_slot_frequency: _lorawan_pb2.ZeroableFrequencyValue
    desired_beacon_frequency: _lorawan_pb2.ZeroableFrequencyValue
    desired_max_eirp: _lorawan_pb2.DeviceEIRPValue
    class_b_c_downlink_interval: _duration_pb2.Duration
    uplink_dwell_time: BoolValue
    downlink_dwell_time: BoolValue
    adr: ADRSettings
    schedule_downlinks: BoolValue
    relay: RelaySettings
    desired_relay: RelaySettings
    def __init__(self, class_b_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ping_slot_periodicity: _Optional[_Union[_lorawan_pb2.PingSlotPeriodValue, _Mapping]] = ..., ping_slot_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndexValue, _Mapping]] = ..., ping_slot_frequency: _Optional[_Union[_lorawan_pb2.ZeroableFrequencyValue, _Mapping]] = ..., beacon_frequency: _Optional[_Union[_lorawan_pb2.ZeroableFrequencyValue, _Mapping]] = ..., class_c_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., rx1_delay: _Optional[_Union[_lorawan_pb2.RxDelayValue, _Mapping]] = ..., rx1_data_rate_offset: _Optional[_Union[_lorawan_pb2.DataRateOffsetValue, _Mapping]] = ..., rx2_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndexValue, _Mapping]] = ..., rx2_frequency: _Optional[_Union[_lorawan_pb2.FrequencyValue, _Mapping]] = ..., factory_preset_frequencies: _Optional[_Iterable[int]] = ..., max_duty_cycle: _Optional[_Union[_lorawan_pb2.AggregatedDutyCycleValue, _Mapping]] = ..., supports_32_bit_f_cnt: _Optional[_Union[BoolValue, _Mapping]] = ..., use_adr: _Optional[_Union[BoolValue, _Mapping]] = ..., adr_margin: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., resets_f_cnt: _Optional[_Union[BoolValue, _Mapping]] = ..., status_time_periodicity: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., status_count_periodicity: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., desired_rx1_delay: _Optional[_Union[_lorawan_pb2.RxDelayValue, _Mapping]] = ..., desired_rx1_data_rate_offset: _Optional[_Union[_lorawan_pb2.DataRateOffsetValue, _Mapping]] = ..., desired_rx2_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndexValue, _Mapping]] = ..., desired_rx2_frequency: _Optional[_Union[_lorawan_pb2.FrequencyValue, _Mapping]] = ..., desired_max_duty_cycle: _Optional[_Union[_lorawan_pb2.AggregatedDutyCycleValue, _Mapping]] = ..., desired_adr_ack_limit_exponent: _Optional[_Union[_lorawan_pb2.ADRAckLimitExponentValue, _Mapping]] = ..., desired_adr_ack_delay_exponent: _Optional[_Union[_lorawan_pb2.ADRAckDelayExponentValue, _Mapping]] = ..., desired_ping_slot_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndexValue, _Mapping]] = ..., desired_ping_slot_frequency: _Optional[_Union[_lorawan_pb2.ZeroableFrequencyValue, _Mapping]] = ..., desired_beacon_frequency: _Optional[_Union[_lorawan_pb2.ZeroableFrequencyValue, _Mapping]] = ..., desired_max_eirp: _Optional[_Union[_lorawan_pb2.DeviceEIRPValue, _Mapping]] = ..., class_b_c_downlink_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., uplink_dwell_time: _Optional[_Union[BoolValue, _Mapping]] = ..., downlink_dwell_time: _Optional[_Union[BoolValue, _Mapping]] = ..., adr: _Optional[_Union[ADRSettings, _Mapping]] = ..., schedule_downlinks: _Optional[_Union[BoolValue, _Mapping]] = ..., relay: _Optional[_Union[RelaySettings, _Mapping]] = ..., desired_relay: _Optional[_Union[RelaySettings, _Mapping]] = ...) -> None: ...

class MACState(_message.Message):
    __slots__ = ("current_parameters", "desired_parameters", "device_class", "lorawan_version", "last_confirmed_downlink_at", "last_dev_status_f_cnt_up", "ping_slot_periodicity", "pending_application_downlink", "queued_responses", "pending_requests", "queued_join_accept", "pending_join_request", "rx_windows_available", "recent_uplinks", "recent_downlinks", "last_network_initiated_downlink_at", "rejected_adr_data_rate_indexes", "rejected_adr_tx_power_indexes", "rejected_frequencies", "last_downlink_at", "rejected_data_rate_ranges", "last_adr_change_f_cnt_up", "recent_mac_command_identifiers", "pending_relay_downlink")
    class JoinRequest(_message.Message):
        __slots__ = ("downlink_settings", "rx_delay", "cf_list")
        DOWNLINK_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        RX_DELAY_FIELD_NUMBER: _ClassVar[int]
        CF_LIST_FIELD_NUMBER: _ClassVar[int]
        downlink_settings: _lorawan_pb2.DLSettings
        rx_delay: _lorawan_pb2.RxDelay
        cf_list: _lorawan_pb2.CFList
        def __init__(self, downlink_settings: _Optional[_Union[_lorawan_pb2.DLSettings, _Mapping]] = ..., rx_delay: _Optional[_Union[_lorawan_pb2.RxDelay, str]] = ..., cf_list: _Optional[_Union[_lorawan_pb2.CFList, _Mapping]] = ...) -> None: ...
    class JoinAccept(_message.Message):
        __slots__ = ("payload", "request", "keys", "correlation_ids", "dev_addr", "net_id")
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        KEYS_FIELD_NUMBER: _ClassVar[int]
        CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
        DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
        NET_ID_FIELD_NUMBER: _ClassVar[int]
        payload: bytes
        request: MACState.JoinRequest
        keys: _keys_pb2.SessionKeys
        correlation_ids: _containers.RepeatedScalarFieldContainer[str]
        dev_addr: bytes
        net_id: bytes
        def __init__(self, payload: _Optional[bytes] = ..., request: _Optional[_Union[MACState.JoinRequest, _Mapping]] = ..., keys: _Optional[_Union[_keys_pb2.SessionKeys, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., dev_addr: _Optional[bytes] = ..., net_id: _Optional[bytes] = ...) -> None: ...
    class UplinkMessage(_message.Message):
        __slots__ = ("payload", "settings", "rx_metadata", "received_at", "correlation_ids", "device_channel_index")
        class TxSettings(_message.Message):
            __slots__ = ("data_rate",)
            DATA_RATE_FIELD_NUMBER: _ClassVar[int]
            data_rate: _lorawan_pb2.DataRate
            def __init__(self, data_rate: _Optional[_Union[_lorawan_pb2.DataRate, _Mapping]] = ...) -> None: ...
        class RxMetadata(_message.Message):
            __slots__ = ("gateway_ids", "channel_rssi", "snr", "downlink_path_constraint", "uplink_token", "packet_broker", "relay")
            class PacketBrokerMetadata(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class RelayMetadata(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_RSSI_FIELD_NUMBER: _ClassVar[int]
            SNR_FIELD_NUMBER: _ClassVar[int]
            DOWNLINK_PATH_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
            UPLINK_TOKEN_FIELD_NUMBER: _ClassVar[int]
            PACKET_BROKER_FIELD_NUMBER: _ClassVar[int]
            RELAY_FIELD_NUMBER: _ClassVar[int]
            gateway_ids: _identifiers_pb2.GatewayIdentifiers
            channel_rssi: float
            snr: float
            downlink_path_constraint: _enums_pb2.DownlinkPathConstraint
            uplink_token: bytes
            packet_broker: MACState.UplinkMessage.RxMetadata.PacketBrokerMetadata
            relay: MACState.UplinkMessage.RxMetadata.RelayMetadata
            def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., channel_rssi: _Optional[float] = ..., snr: _Optional[float] = ..., downlink_path_constraint: _Optional[_Union[_enums_pb2.DownlinkPathConstraint, str]] = ..., uplink_token: _Optional[bytes] = ..., packet_broker: _Optional[_Union[MACState.UplinkMessage.RxMetadata.PacketBrokerMetadata, _Mapping]] = ..., relay: _Optional[_Union[MACState.UplinkMessage.RxMetadata.RelayMetadata, _Mapping]] = ...) -> None: ...
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        RX_METADATA_FIELD_NUMBER: _ClassVar[int]
        RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
        CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
        payload: _lorawan_pb2.Message
        settings: MACState.UplinkMessage.TxSettings
        rx_metadata: _containers.RepeatedCompositeFieldContainer[MACState.UplinkMessage.RxMetadata]
        received_at: _timestamp_pb2.Timestamp
        correlation_ids: _containers.RepeatedScalarFieldContainer[str]
        device_channel_index: int
        def __init__(self, payload: _Optional[_Union[_lorawan_pb2.Message, _Mapping]] = ..., settings: _Optional[_Union[MACState.UplinkMessage.TxSettings, _Mapping]] = ..., rx_metadata: _Optional[_Iterable[_Union[MACState.UplinkMessage.RxMetadata, _Mapping]]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ..., device_channel_index: _Optional[int] = ...) -> None: ...
    class DownlinkMessage(_message.Message):
        __slots__ = ("payload", "correlation_ids")
        class Message(_message.Message):
            __slots__ = ("m_hdr", "mac_payload")
            class MHDR(_message.Message):
                __slots__ = ("m_type",)
                M_TYPE_FIELD_NUMBER: _ClassVar[int]
                m_type: _lorawan_pb2.MType
                def __init__(self, m_type: _Optional[_Union[_lorawan_pb2.MType, str]] = ...) -> None: ...
            class MACPayload(_message.Message):
                __slots__ = ("f_port", "full_f_cnt")
                F_PORT_FIELD_NUMBER: _ClassVar[int]
                FULL_F_CNT_FIELD_NUMBER: _ClassVar[int]
                f_port: int
                full_f_cnt: int
                def __init__(self, f_port: _Optional[int] = ..., full_f_cnt: _Optional[int] = ...) -> None: ...
            M_HDR_FIELD_NUMBER: _ClassVar[int]
            MAC_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
            m_hdr: MACState.DownlinkMessage.Message.MHDR
            mac_payload: MACState.DownlinkMessage.Message.MACPayload
            def __init__(self, m_hdr: _Optional[_Union[MACState.DownlinkMessage.Message.MHDR, _Mapping]] = ..., mac_payload: _Optional[_Union[MACState.DownlinkMessage.Message.MACPayload, _Mapping]] = ...) -> None: ...
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        CORRELATION_IDS_FIELD_NUMBER: _ClassVar[int]
        payload: MACState.DownlinkMessage.Message
        correlation_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, payload: _Optional[_Union[MACState.DownlinkMessage.Message, _Mapping]] = ..., correlation_ids: _Optional[_Iterable[str]] = ...) -> None: ...
    class DataRateRange(_message.Message):
        __slots__ = ("min_data_rate_index", "max_data_rate_index")
        MIN_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        min_data_rate_index: _lorawan_pb2.DataRateIndex
        max_data_rate_index: _lorawan_pb2.DataRateIndex
        def __init__(self, min_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ..., max_data_rate_index: _Optional[_Union[_lorawan_pb2.DataRateIndex, str]] = ...) -> None: ...
    class DataRateRanges(_message.Message):
        __slots__ = ("ranges",)
        RANGES_FIELD_NUMBER: _ClassVar[int]
        ranges: _containers.RepeatedCompositeFieldContainer[MACState.DataRateRange]
        def __init__(self, ranges: _Optional[_Iterable[_Union[MACState.DataRateRange, _Mapping]]] = ...) -> None: ...
    class RejectedDataRateRangesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: MACState.DataRateRanges
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[MACState.DataRateRanges, _Mapping]] = ...) -> None: ...
    CURRENT_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_VERSION_FIELD_NUMBER: _ClassVar[int]
    LAST_CONFIRMED_DOWNLINK_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_DEV_STATUS_F_CNT_UP_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
    PENDING_APPLICATION_DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    QUEUED_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    PENDING_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    QUEUED_JOIN_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    PENDING_JOIN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    RX_WINDOWS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    RECENT_UPLINKS_FIELD_NUMBER: _ClassVar[int]
    RECENT_DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    LAST_NETWORK_INITIATED_DOWNLINK_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_ADR_DATA_RATE_INDEXES_FIELD_NUMBER: _ClassVar[int]
    REJECTED_ADR_TX_POWER_INDEXES_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FREQUENCIES_FIELD_NUMBER: _ClassVar[int]
    LAST_DOWNLINK_AT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_DATA_RATE_RANGES_FIELD_NUMBER: _ClassVar[int]
    LAST_ADR_CHANGE_F_CNT_UP_FIELD_NUMBER: _ClassVar[int]
    RECENT_MAC_COMMAND_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    PENDING_RELAY_DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    current_parameters: MACParameters
    desired_parameters: MACParameters
    device_class: _lorawan_pb2.Class
    lorawan_version: _lorawan_pb2.MACVersion
    last_confirmed_downlink_at: _timestamp_pb2.Timestamp
    last_dev_status_f_cnt_up: int
    ping_slot_periodicity: _lorawan_pb2.PingSlotPeriodValue
    pending_application_downlink: _messages_pb2.ApplicationDownlink
    queued_responses: _containers.RepeatedCompositeFieldContainer[_lorawan_pb2.MACCommand]
    pending_requests: _containers.RepeatedCompositeFieldContainer[_lorawan_pb2.MACCommand]
    queued_join_accept: MACState.JoinAccept
    pending_join_request: MACState.JoinRequest
    rx_windows_available: bool
    recent_uplinks: _containers.RepeatedCompositeFieldContainer[MACState.UplinkMessage]
    recent_downlinks: _containers.RepeatedCompositeFieldContainer[MACState.DownlinkMessage]
    last_network_initiated_downlink_at: _timestamp_pb2.Timestamp
    rejected_adr_data_rate_indexes: _containers.RepeatedScalarFieldContainer[_lorawan_pb2.DataRateIndex]
    rejected_adr_tx_power_indexes: _containers.RepeatedScalarFieldContainer[int]
    rejected_frequencies: _containers.RepeatedScalarFieldContainer[int]
    last_downlink_at: _timestamp_pb2.Timestamp
    rejected_data_rate_ranges: _containers.MessageMap[int, MACState.DataRateRanges]
    last_adr_change_f_cnt_up: int
    recent_mac_command_identifiers: _containers.RepeatedScalarFieldContainer[_lorawan_pb2.MACCommandIdentifier]
    pending_relay_downlink: _lorawan_pb2.RelayForwardDownlinkReq
    def __init__(self, current_parameters: _Optional[_Union[MACParameters, _Mapping]] = ..., desired_parameters: _Optional[_Union[MACParameters, _Mapping]] = ..., device_class: _Optional[_Union[_lorawan_pb2.Class, str]] = ..., lorawan_version: _Optional[_Union[_lorawan_pb2.MACVersion, str]] = ..., last_confirmed_downlink_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_dev_status_f_cnt_up: _Optional[int] = ..., ping_slot_periodicity: _Optional[_Union[_lorawan_pb2.PingSlotPeriodValue, _Mapping]] = ..., pending_application_downlink: _Optional[_Union[_messages_pb2.ApplicationDownlink, _Mapping]] = ..., queued_responses: _Optional[_Iterable[_Union[_lorawan_pb2.MACCommand, _Mapping]]] = ..., pending_requests: _Optional[_Iterable[_Union[_lorawan_pb2.MACCommand, _Mapping]]] = ..., queued_join_accept: _Optional[_Union[MACState.JoinAccept, _Mapping]] = ..., pending_join_request: _Optional[_Union[MACState.JoinRequest, _Mapping]] = ..., rx_windows_available: bool = ..., recent_uplinks: _Optional[_Iterable[_Union[MACState.UplinkMessage, _Mapping]]] = ..., recent_downlinks: _Optional[_Iterable[_Union[MACState.DownlinkMessage, _Mapping]]] = ..., last_network_initiated_downlink_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_adr_data_rate_indexes: _Optional[_Iterable[_Union[_lorawan_pb2.DataRateIndex, str]]] = ..., rejected_adr_tx_power_indexes: _Optional[_Iterable[int]] = ..., rejected_frequencies: _Optional[_Iterable[int]] = ..., last_downlink_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., rejected_data_rate_ranges: _Optional[_Mapping[int, MACState.DataRateRanges]] = ..., last_adr_change_f_cnt_up: _Optional[int] = ..., recent_mac_command_identifiers: _Optional[_Iterable[_Union[_lorawan_pb2.MACCommandIdentifier, str]]] = ..., pending_relay_downlink: _Optional[_Union[_lorawan_pb2.RelayForwardDownlinkReq, _Mapping]] = ...) -> None: ...

class EndDeviceAuthenticationCode(_message.Message):
    __slots__ = ("value", "valid_from", "valid_to")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_TO_FIELD_NUMBER: _ClassVar[int]
    value: str
    valid_from: _timestamp_pb2.Timestamp
    valid_to: _timestamp_pb2.Timestamp
    def __init__(self, value: _Optional[str] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class EndDevice(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "name", "description", "attributes", "version_ids", "service_profile_id", "network_server_address", "network_server_kek_label", "application_server_address", "application_server_kek_label", "application_server_id", "join_server_address", "locations", "picture", "supports_class_b", "supports_class_c", "lorawan_version", "lorawan_phy_version", "frequency_plan_id", "min_frequency", "max_frequency", "supports_join", "resets_join_nonces", "root_keys", "net_id", "mac_settings", "mac_state", "pending_mac_state", "session", "pending_session", "last_dev_nonce", "used_dev_nonces", "last_join_nonce", "last_rj_count_0", "last_rj_count_1", "last_dev_status_received_at", "power_state", "battery_percentage", "downlink_margin", "queued_application_downlinks", "formatters", "provisioner_id", "provisioning_data", "multicast", "claim_authentication_code", "skip_payload_crypto", "skip_payload_crypto_override", "activated_at", "last_seen_at", "serial_number", "lora_alliance_profile_ids")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LocationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _metadata_pb2.Location
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_metadata_pb2.Location, _Mapping]] = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_KEK_LABEL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_SERVER_KEK_LABEL_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    JOIN_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_B_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLASS_C_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_VERSION_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_PHY_VERSION_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    MIN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MAX_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_JOIN_FIELD_NUMBER: _ClassVar[int]
    RESETS_JOIN_NONCES_FIELD_NUMBER: _ClassVar[int]
    ROOT_KEYS_FIELD_NUMBER: _ClassVar[int]
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    MAC_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MAC_STATE_FIELD_NUMBER: _ClassVar[int]
    PENDING_MAC_STATE_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    PENDING_SESSION_FIELD_NUMBER: _ClassVar[int]
    LAST_DEV_NONCE_FIELD_NUMBER: _ClassVar[int]
    USED_DEV_NONCES_FIELD_NUMBER: _ClassVar[int]
    LAST_JOIN_NONCE_FIELD_NUMBER: _ClassVar[int]
    LAST_RJ_COUNT_0_FIELD_NUMBER: _ClassVar[int]
    LAST_RJ_COUNT_1_FIELD_NUMBER: _ClassVar[int]
    LAST_DEV_STATUS_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_MARGIN_FIELD_NUMBER: _ClassVar[int]
    QUEUED_APPLICATION_DOWNLINKS_FIELD_NUMBER: _ClassVar[int]
    FORMATTERS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_DATA_FIELD_NUMBER: _ClassVar[int]
    MULTICAST_FIELD_NUMBER: _ClassVar[int]
    CLAIM_AUTHENTICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    SKIP_PAYLOAD_CRYPTO_FIELD_NUMBER: _ClassVar[int]
    SKIP_PAYLOAD_CRYPTO_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ACTIVATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LORA_ALLIANCE_PROFILE_IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.EndDeviceIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    name: str
    description: str
    attributes: _containers.ScalarMap[str, str]
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    service_profile_id: str
    network_server_address: str
    network_server_kek_label: str
    application_server_address: str
    application_server_kek_label: str
    application_server_id: str
    join_server_address: str
    locations: _containers.MessageMap[str, _metadata_pb2.Location]
    picture: _picture_pb2.Picture
    supports_class_b: bool
    supports_class_c: bool
    lorawan_version: _lorawan_pb2.MACVersion
    lorawan_phy_version: _lorawan_pb2.PHYVersion
    frequency_plan_id: str
    min_frequency: int
    max_frequency: int
    supports_join: bool
    resets_join_nonces: bool
    root_keys: _keys_pb2.RootKeys
    net_id: bytes
    mac_settings: MACSettings
    mac_state: MACState
    pending_mac_state: MACState
    session: Session
    pending_session: Session
    last_dev_nonce: int
    used_dev_nonces: _containers.RepeatedScalarFieldContainer[int]
    last_join_nonce: int
    last_rj_count_0: int
    last_rj_count_1: int
    last_dev_status_received_at: _timestamp_pb2.Timestamp
    power_state: PowerState
    battery_percentage: _wrappers_pb2.FloatValue
    downlink_margin: int
    queued_application_downlinks: _containers.RepeatedCompositeFieldContainer[_messages_pb2.ApplicationDownlink]
    formatters: _messages_pb2.MessagePayloadFormatters
    provisioner_id: str
    provisioning_data: _struct_pb2.Struct
    multicast: bool
    claim_authentication_code: EndDeviceAuthenticationCode
    skip_payload_crypto: bool
    skip_payload_crypto_override: _wrappers_pb2.BoolValue
    activated_at: _timestamp_pb2.Timestamp
    last_seen_at: _timestamp_pb2.Timestamp
    serial_number: str
    lora_alliance_profile_ids: _identifiers_pb2.LoRaAllianceProfileIdentifiers
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., service_profile_id: _Optional[str] = ..., network_server_address: _Optional[str] = ..., network_server_kek_label: _Optional[str] = ..., application_server_address: _Optional[str] = ..., application_server_kek_label: _Optional[str] = ..., application_server_id: _Optional[str] = ..., join_server_address: _Optional[str] = ..., locations: _Optional[_Mapping[str, _metadata_pb2.Location]] = ..., picture: _Optional[_Union[_picture_pb2.Picture, _Mapping]] = ..., supports_class_b: bool = ..., supports_class_c: bool = ..., lorawan_version: _Optional[_Union[_lorawan_pb2.MACVersion, str]] = ..., lorawan_phy_version: _Optional[_Union[_lorawan_pb2.PHYVersion, str]] = ..., frequency_plan_id: _Optional[str] = ..., min_frequency: _Optional[int] = ..., max_frequency: _Optional[int] = ..., supports_join: bool = ..., resets_join_nonces: bool = ..., root_keys: _Optional[_Union[_keys_pb2.RootKeys, _Mapping]] = ..., net_id: _Optional[bytes] = ..., mac_settings: _Optional[_Union[MACSettings, _Mapping]] = ..., mac_state: _Optional[_Union[MACState, _Mapping]] = ..., pending_mac_state: _Optional[_Union[MACState, _Mapping]] = ..., session: _Optional[_Union[Session, _Mapping]] = ..., pending_session: _Optional[_Union[Session, _Mapping]] = ..., last_dev_nonce: _Optional[int] = ..., used_dev_nonces: _Optional[_Iterable[int]] = ..., last_join_nonce: _Optional[int] = ..., last_rj_count_0: _Optional[int] = ..., last_rj_count_1: _Optional[int] = ..., last_dev_status_received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., power_state: _Optional[_Union[PowerState, str]] = ..., battery_percentage: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., downlink_margin: _Optional[int] = ..., queued_application_downlinks: _Optional[_Iterable[_Union[_messages_pb2.ApplicationDownlink, _Mapping]]] = ..., formatters: _Optional[_Union[_messages_pb2.MessagePayloadFormatters, _Mapping]] = ..., provisioner_id: _Optional[str] = ..., provisioning_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., multicast: bool = ..., claim_authentication_code: _Optional[_Union[EndDeviceAuthenticationCode, _Mapping]] = ..., skip_payload_crypto: bool = ..., skip_payload_crypto_override: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., activated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., serial_number: _Optional[str] = ..., lora_alliance_profile_ids: _Optional[_Union[_identifiers_pb2.LoRaAllianceProfileIdentifiers, _Mapping]] = ...) -> None: ...

class EndDevices(_message.Message):
    __slots__ = ("end_devices",)
    END_DEVICES_FIELD_NUMBER: _ClassVar[int]
    end_devices: _containers.RepeatedCompositeFieldContainer[EndDevice]
    def __init__(self, end_devices: _Optional[_Iterable[_Union[EndDevice, _Mapping]]] = ...) -> None: ...

class DevAddrPrefix(_message.Message):
    __slots__ = ("dev_addr", "length")
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    length: int
    def __init__(self, dev_addr: _Optional[bytes] = ..., length: _Optional[int] = ...) -> None: ...

class CreateEndDeviceRequest(_message.Message):
    __slots__ = ("end_device",)
    END_DEVICE_FIELD_NUMBER: _ClassVar[int]
    end_device: EndDevice
    def __init__(self, end_device: _Optional[_Union[EndDevice, _Mapping]] = ...) -> None: ...

class UpdateEndDeviceRequest(_message.Message):
    __slots__ = ("end_device", "field_mask")
    END_DEVICE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device: EndDevice
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device: _Optional[_Union[EndDevice, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class BatchUpdateEndDeviceLastSeenRequest(_message.Message):
    __slots__ = ("updates",)
    class EndDeviceLastSeenUpdate(_message.Message):
        __slots__ = ("ids", "last_seen_at")
        IDS_FIELD_NUMBER: _ClassVar[int]
        LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
        ids: _identifiers_pb2.EndDeviceIdentifiers
        last_seen_at: _timestamp_pb2.Timestamp
        def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., last_seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[BatchUpdateEndDeviceLastSeenRequest.EndDeviceLastSeenUpdate]
    def __init__(self, updates: _Optional[_Iterable[_Union[BatchUpdateEndDeviceLastSeenRequest.EndDeviceLastSeenUpdate, _Mapping]]] = ...) -> None: ...

class GetEndDeviceRequest(_message.Message):
    __slots__ = ("end_device_ids", "field_mask")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEndDeviceIdentifiersForEUIsRequest(_message.Message):
    __slots__ = ("join_eui", "dev_eui")
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    join_eui: bytes
    dev_eui: bytes
    def __init__(self, join_eui: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ...) -> None: ...

class ListEndDevicesRequest(_message.Message):
    __slots__ = ("application_ids", "field_mask", "order", "limit", "page", "filters")
    class Filter(_message.Message):
        __slots__ = ("updated_since",)
        UPDATED_SINCE_FIELD_NUMBER: _ClassVar[int]
        updated_since: _timestamp_pb2.Timestamp
        def __init__(self, updated_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    filters: _containers.RepeatedCompositeFieldContainer[ListEndDevicesRequest.Filter]
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., filters: _Optional[_Iterable[_Union[ListEndDevicesRequest.Filter, _Mapping]]] = ...) -> None: ...

class SetEndDeviceRequest(_message.Message):
    __slots__ = ("end_device", "field_mask")
    END_DEVICE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device: EndDevice
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device: _Optional[_Union[EndDevice, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ResetAndGetEndDeviceRequest(_message.Message):
    __slots__ = ("end_device_ids", "field_mask")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class EndDeviceTemplate(_message.Message):
    __slots__ = ("end_device", "field_mask", "mapping_key")
    END_DEVICE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    MAPPING_KEY_FIELD_NUMBER: _ClassVar[int]
    end_device: EndDevice
    field_mask: _field_mask_pb2.FieldMask
    mapping_key: str
    def __init__(self, end_device: _Optional[_Union[EndDevice, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., mapping_key: _Optional[str] = ...) -> None: ...

class EndDeviceTemplateFormat(_message.Message):
    __slots__ = ("name", "description", "file_extensions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    file_extensions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., file_extensions: _Optional[_Iterable[str]] = ...) -> None: ...

class EndDeviceTemplateFormats(_message.Message):
    __slots__ = ("formats",)
    class FormatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: EndDeviceTemplateFormat
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EndDeviceTemplateFormat, _Mapping]] = ...) -> None: ...
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    formats: _containers.MessageMap[str, EndDeviceTemplateFormat]
    def __init__(self, formats: _Optional[_Mapping[str, EndDeviceTemplateFormat]] = ...) -> None: ...

class ConvertEndDeviceTemplateRequest(_message.Message):
    __slots__ = ("format_id", "data", "end_device_version_ids")
    FORMAT_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    format_id: str
    data: bytes
    end_device_version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    def __init__(self, format_id: _Optional[str] = ..., data: _Optional[bytes] = ..., end_device_version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ...) -> None: ...

class BatchDeleteEndDevicesRequest(_message.Message):
    __slots__ = ("application_ids", "device_ids")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    device_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., device_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchGetEndDevicesRequest(_message.Message):
    __slots__ = ("application_ids", "device_ids", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    device_ids: _containers.RepeatedScalarFieldContainer[str]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., device_ids: _Optional[_Iterable[str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
