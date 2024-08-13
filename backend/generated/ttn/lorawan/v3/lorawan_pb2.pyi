from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOIN_REQUEST: _ClassVar[MType]
    JOIN_ACCEPT: _ClassVar[MType]
    UNCONFIRMED_UP: _ClassVar[MType]
    UNCONFIRMED_DOWN: _ClassVar[MType]
    CONFIRMED_UP: _ClassVar[MType]
    CONFIRMED_DOWN: _ClassVar[MType]
    REJOIN_REQUEST: _ClassVar[MType]
    PROPRIETARY: _ClassVar[MType]

class Major(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LORAWAN_R1: _ClassVar[Major]

class MACVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAC_UNKNOWN: _ClassVar[MACVersion]
    MAC_V1_0: _ClassVar[MACVersion]
    MAC_V1_0_1: _ClassVar[MACVersion]
    MAC_V1_0_2: _ClassVar[MACVersion]
    MAC_V1_1: _ClassVar[MACVersion]
    MAC_V1_0_3: _ClassVar[MACVersion]
    MAC_V1_0_4: _ClassVar[MACVersion]

class PHYVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHY_UNKNOWN: _ClassVar[PHYVersion]
    PHY_V1_0: _ClassVar[PHYVersion]
    TS001_V1_0: _ClassVar[PHYVersion]
    PHY_V1_0_1: _ClassVar[PHYVersion]
    TS001_V1_0_1: _ClassVar[PHYVersion]
    PHY_V1_0_2_REV_A: _ClassVar[PHYVersion]
    RP001_V1_0_2: _ClassVar[PHYVersion]
    PHY_V1_0_2_REV_B: _ClassVar[PHYVersion]
    RP001_V1_0_2_REV_B: _ClassVar[PHYVersion]
    PHY_V1_1_REV_A: _ClassVar[PHYVersion]
    RP001_V1_1_REV_A: _ClassVar[PHYVersion]
    PHY_V1_1_REV_B: _ClassVar[PHYVersion]
    RP001_V1_1_REV_B: _ClassVar[PHYVersion]
    PHY_V1_0_3_REV_A: _ClassVar[PHYVersion]
    RP001_V1_0_3_REV_A: _ClassVar[PHYVersion]
    RP002_V1_0_0: _ClassVar[PHYVersion]
    RP002_V1_0_1: _ClassVar[PHYVersion]
    RP002_V1_0_2: _ClassVar[PHYVersion]
    RP002_V1_0_3: _ClassVar[PHYVersion]
    RP002_V1_0_4: _ClassVar[PHYVersion]

class DataRateIndex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_RATE_0: _ClassVar[DataRateIndex]
    DATA_RATE_1: _ClassVar[DataRateIndex]
    DATA_RATE_2: _ClassVar[DataRateIndex]
    DATA_RATE_3: _ClassVar[DataRateIndex]
    DATA_RATE_4: _ClassVar[DataRateIndex]
    DATA_RATE_5: _ClassVar[DataRateIndex]
    DATA_RATE_6: _ClassVar[DataRateIndex]
    DATA_RATE_7: _ClassVar[DataRateIndex]
    DATA_RATE_8: _ClassVar[DataRateIndex]
    DATA_RATE_9: _ClassVar[DataRateIndex]
    DATA_RATE_10: _ClassVar[DataRateIndex]
    DATA_RATE_11: _ClassVar[DataRateIndex]
    DATA_RATE_12: _ClassVar[DataRateIndex]
    DATA_RATE_13: _ClassVar[DataRateIndex]
    DATA_RATE_14: _ClassVar[DataRateIndex]
    DATA_RATE_15: _ClassVar[DataRateIndex]

class DataRateOffset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_RATE_OFFSET_0: _ClassVar[DataRateOffset]
    DATA_RATE_OFFSET_1: _ClassVar[DataRateOffset]
    DATA_RATE_OFFSET_2: _ClassVar[DataRateOffset]
    DATA_RATE_OFFSET_3: _ClassVar[DataRateOffset]
    DATA_RATE_OFFSET_4: _ClassVar[DataRateOffset]
    DATA_RATE_OFFSET_5: _ClassVar[DataRateOffset]
    DATA_RATE_OFFSET_6: _ClassVar[DataRateOffset]
    DATA_RATE_OFFSET_7: _ClassVar[DataRateOffset]

class JoinRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REJOIN_CONTEXT: _ClassVar[JoinRequestType]
    REJOIN_SESSION: _ClassVar[JoinRequestType]
    REJOIN_KEYS: _ClassVar[JoinRequestType]
    JOIN: _ClassVar[JoinRequestType]

class RejoinRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTEXT: _ClassVar[RejoinRequestType]
    SESSION: _ClassVar[RejoinRequestType]
    KEYS: _ClassVar[RejoinRequestType]

class CFListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREQUENCIES: _ClassVar[CFListType]
    CHANNEL_MASKS: _ClassVar[CFListType]

class Class(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLASS_A: _ClassVar[Class]
    CLASS_B: _ClassVar[Class]
    CLASS_C: _ClassVar[Class]

class TxSchedulePriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOWEST: _ClassVar[TxSchedulePriority]
    LOW: _ClassVar[TxSchedulePriority]
    BELOW_NORMAL: _ClassVar[TxSchedulePriority]
    NORMAL: _ClassVar[TxSchedulePriority]
    ABOVE_NORMAL: _ClassVar[TxSchedulePriority]
    HIGH: _ClassVar[TxSchedulePriority]
    HIGHEST: _ClassVar[TxSchedulePriority]

class MACCommandIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CID_RFU_0: _ClassVar[MACCommandIdentifier]
    CID_RESET: _ClassVar[MACCommandIdentifier]
    CID_LINK_CHECK: _ClassVar[MACCommandIdentifier]
    CID_LINK_ADR: _ClassVar[MACCommandIdentifier]
    CID_DUTY_CYCLE: _ClassVar[MACCommandIdentifier]
    CID_RX_PARAM_SETUP: _ClassVar[MACCommandIdentifier]
    CID_DEV_STATUS: _ClassVar[MACCommandIdentifier]
    CID_NEW_CHANNEL: _ClassVar[MACCommandIdentifier]
    CID_RX_TIMING_SETUP: _ClassVar[MACCommandIdentifier]
    CID_TX_PARAM_SETUP: _ClassVar[MACCommandIdentifier]
    CID_DL_CHANNEL: _ClassVar[MACCommandIdentifier]
    CID_REKEY: _ClassVar[MACCommandIdentifier]
    CID_ADR_PARAM_SETUP: _ClassVar[MACCommandIdentifier]
    CID_DEVICE_TIME: _ClassVar[MACCommandIdentifier]
    CID_FORCE_REJOIN: _ClassVar[MACCommandIdentifier]
    CID_REJOIN_PARAM_SETUP: _ClassVar[MACCommandIdentifier]
    CID_PING_SLOT_INFO: _ClassVar[MACCommandIdentifier]
    CID_PING_SLOT_CHANNEL: _ClassVar[MACCommandIdentifier]
    CID_BEACON_TIMING: _ClassVar[MACCommandIdentifier]
    CID_BEACON_FREQ: _ClassVar[MACCommandIdentifier]
    CID_DEVICE_MODE: _ClassVar[MACCommandIdentifier]
    CID_RELAY_CONF: _ClassVar[MACCommandIdentifier]
    CID_RELAY_END_DEVICE_CONF: _ClassVar[MACCommandIdentifier]
    CID_RELAY_FILTER_LIST: _ClassVar[MACCommandIdentifier]
    CID_RELAY_UPDATE_UPLINK_LIST: _ClassVar[MACCommandIdentifier]
    CID_RELAY_CTRL_UPLINK_LIST: _ClassVar[MACCommandIdentifier]
    CID_RELAY_CONFIGURE_FWD_LIMIT: _ClassVar[MACCommandIdentifier]
    CID_RELAY_NOTIFY_NEW_END_DEVICE: _ClassVar[MACCommandIdentifier]

class RelayCADPeriodicity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELAY_CAD_PERIODICITY_1_SECOND: _ClassVar[RelayCADPeriodicity]
    RELAY_CAD_PERIODICITY_500_MILLISECONDS: _ClassVar[RelayCADPeriodicity]
    RELAY_CAD_PERIODICITY_250_MILLISECONDS: _ClassVar[RelayCADPeriodicity]
    RELAY_CAD_PERIODICITY_100_MILLISECONDS: _ClassVar[RelayCADPeriodicity]
    RELAY_CAD_PERIODICITY_50_MILLISECONDS: _ClassVar[RelayCADPeriodicity]
    RELAY_CAD_PERIODICITY_20_MILLISECONDS: _ClassVar[RelayCADPeriodicity]

class RelaySecondChAckOffset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELAY_SECOND_CH_ACK_OFFSET_0: _ClassVar[RelaySecondChAckOffset]
    RELAY_SECOND_CH_ACK_OFFSET_200: _ClassVar[RelaySecondChAckOffset]
    RELAY_SECOND_CH_ACK_OFFSET_400: _ClassVar[RelaySecondChAckOffset]
    RELAY_SECOND_CH_ACK_OFFSET_800: _ClassVar[RelaySecondChAckOffset]
    RELAY_SECOND_CH_ACK_OFFSET_1600: _ClassVar[RelaySecondChAckOffset]
    RELAY_SECOND_CH_ACK_OFFSET_3200: _ClassVar[RelaySecondChAckOffset]

class RelayLimitBucketSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELAY_LIMIT_BUCKET_SIZE_1: _ClassVar[RelayLimitBucketSize]
    RELAY_LIMIT_BUCKET_SIZE_2: _ClassVar[RelayLimitBucketSize]
    RELAY_LIMIT_BUCKET_SIZE_4: _ClassVar[RelayLimitBucketSize]
    RELAY_LIMIT_BUCKET_SIZE_12: _ClassVar[RelayLimitBucketSize]

class RelaySmartEnableLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELAY_SMART_ENABLE_LEVEL_8: _ClassVar[RelaySmartEnableLevel]
    RELAY_SMART_ENABLE_LEVEL_16: _ClassVar[RelaySmartEnableLevel]
    RELAY_SMART_ENABLE_LEVEL_32: _ClassVar[RelaySmartEnableLevel]
    RELAY_SMART_ENABLE_LEVEL_64: _ClassVar[RelaySmartEnableLevel]

class RelayWORChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELAY_WOR_CHANNEL_DEFAULT: _ClassVar[RelayWORChannel]
    RELAY_WOR_CHANNEL_SECONDARY: _ClassVar[RelayWORChannel]

class RelayResetLimitCounter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELAY_RESET_LIMIT_COUNTER_ZERO: _ClassVar[RelayResetLimitCounter]
    RELAY_RESET_LIMIT_COUNTER_RELOAD_RATE: _ClassVar[RelayResetLimitCounter]
    RELAY_RESET_LIMIT_COUNTER_MAX_VALUE: _ClassVar[RelayResetLimitCounter]
    RELAY_RESET_LIMIT_COUNTER_NO_RESET: _ClassVar[RelayResetLimitCounter]

class RelayCtrlUplinkListAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELAY_CTRL_UPLINK_LIST_ACTION_READ_W_F_CNT: _ClassVar[RelayCtrlUplinkListAction]
    RELAY_CTRL_UPLINK_LIST_ACTION_REMOVE_TRUSTED_END_DEVICE: _ClassVar[RelayCtrlUplinkListAction]

class AggregatedDutyCycle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DUTY_CYCLE_1: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_2: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_4: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_8: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_16: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_32: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_64: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_128: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_256: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_512: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_1024: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_2048: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_4096: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_8192: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_16384: _ClassVar[AggregatedDutyCycle]
    DUTY_CYCLE_32768: _ClassVar[AggregatedDutyCycle]

class PingSlotPeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PING_EVERY_1S: _ClassVar[PingSlotPeriod]
    PING_EVERY_2S: _ClassVar[PingSlotPeriod]
    PING_EVERY_4S: _ClassVar[PingSlotPeriod]
    PING_EVERY_8S: _ClassVar[PingSlotPeriod]
    PING_EVERY_16S: _ClassVar[PingSlotPeriod]
    PING_EVERY_32S: _ClassVar[PingSlotPeriod]
    PING_EVERY_64S: _ClassVar[PingSlotPeriod]
    PING_EVERY_128S: _ClassVar[PingSlotPeriod]

class RejoinCountExponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REJOIN_COUNT_16: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_32: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_64: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_128: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_256: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_512: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_1024: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_2048: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_4096: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_8192: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_16384: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_32768: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_65536: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_131072: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_262144: _ClassVar[RejoinCountExponent]
    REJOIN_COUNT_524288: _ClassVar[RejoinCountExponent]

class RejoinTimeExponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REJOIN_TIME_0: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_1: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_2: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_3: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_4: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_5: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_6: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_7: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_8: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_9: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_10: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_11: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_12: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_13: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_14: _ClassVar[RejoinTimeExponent]
    REJOIN_TIME_15: _ClassVar[RejoinTimeExponent]

class RejoinPeriodExponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REJOIN_PERIOD_0: _ClassVar[RejoinPeriodExponent]
    REJOIN_PERIOD_1: _ClassVar[RejoinPeriodExponent]
    REJOIN_PERIOD_2: _ClassVar[RejoinPeriodExponent]
    REJOIN_PERIOD_3: _ClassVar[RejoinPeriodExponent]
    REJOIN_PERIOD_4: _ClassVar[RejoinPeriodExponent]
    REJOIN_PERIOD_5: _ClassVar[RejoinPeriodExponent]
    REJOIN_PERIOD_6: _ClassVar[RejoinPeriodExponent]
    REJOIN_PERIOD_7: _ClassVar[RejoinPeriodExponent]

class DeviceEIRP(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_EIRP_8: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_10: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_12: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_13: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_14: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_16: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_18: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_20: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_21: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_24: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_26: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_27: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_29: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_30: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_33: _ClassVar[DeviceEIRP]
    DEVICE_EIRP_36: _ClassVar[DeviceEIRP]

class ADRAckLimitExponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADR_ACK_LIMIT_1: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_2: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_4: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_8: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_16: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_32: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_64: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_128: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_256: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_512: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_1024: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_2048: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_4096: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_8192: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_16384: _ClassVar[ADRAckLimitExponent]
    ADR_ACK_LIMIT_32768: _ClassVar[ADRAckLimitExponent]

class ADRAckDelayExponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ADR_ACK_DELAY_1: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_2: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_4: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_8: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_16: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_32: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_64: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_128: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_256: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_512: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_1024: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_2048: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_4096: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_8192: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_16384: _ClassVar[ADRAckDelayExponent]
    ADR_ACK_DELAY_32768: _ClassVar[ADRAckDelayExponent]

class RxDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RX_DELAY_0: _ClassVar[RxDelay]
    RX_DELAY_1: _ClassVar[RxDelay]
    RX_DELAY_2: _ClassVar[RxDelay]
    RX_DELAY_3: _ClassVar[RxDelay]
    RX_DELAY_4: _ClassVar[RxDelay]
    RX_DELAY_5: _ClassVar[RxDelay]
    RX_DELAY_6: _ClassVar[RxDelay]
    RX_DELAY_7: _ClassVar[RxDelay]
    RX_DELAY_8: _ClassVar[RxDelay]
    RX_DELAY_9: _ClassVar[RxDelay]
    RX_DELAY_10: _ClassVar[RxDelay]
    RX_DELAY_11: _ClassVar[RxDelay]
    RX_DELAY_12: _ClassVar[RxDelay]
    RX_DELAY_13: _ClassVar[RxDelay]
    RX_DELAY_14: _ClassVar[RxDelay]
    RX_DELAY_15: _ClassVar[RxDelay]

class Minor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MINOR_RFU_0: _ClassVar[Minor]
    MINOR_1: _ClassVar[Minor]
    MINOR_RFU_2: _ClassVar[Minor]
    MINOR_RFU_3: _ClassVar[Minor]
    MINOR_RFU_4: _ClassVar[Minor]
    MINOR_RFU_5: _ClassVar[Minor]
    MINOR_RFU_6: _ClassVar[Minor]
    MINOR_RFU_7: _ClassVar[Minor]
    MINOR_RFU_8: _ClassVar[Minor]
    MINOR_RFU_9: _ClassVar[Minor]
    MINOR_RFU_10: _ClassVar[Minor]
    MINOR_RFU_11: _ClassVar[Minor]
    MINOR_RFU_12: _ClassVar[Minor]
    MINOR_RFU_13: _ClassVar[Minor]
    MINOR_RFU_14: _ClassVar[Minor]
    MINOR_RFU_15: _ClassVar[Minor]
JOIN_REQUEST: MType
JOIN_ACCEPT: MType
UNCONFIRMED_UP: MType
UNCONFIRMED_DOWN: MType
CONFIRMED_UP: MType
CONFIRMED_DOWN: MType
REJOIN_REQUEST: MType
PROPRIETARY: MType
LORAWAN_R1: Major
MAC_UNKNOWN: MACVersion
MAC_V1_0: MACVersion
MAC_V1_0_1: MACVersion
MAC_V1_0_2: MACVersion
MAC_V1_1: MACVersion
MAC_V1_0_3: MACVersion
MAC_V1_0_4: MACVersion
PHY_UNKNOWN: PHYVersion
PHY_V1_0: PHYVersion
TS001_V1_0: PHYVersion
PHY_V1_0_1: PHYVersion
TS001_V1_0_1: PHYVersion
PHY_V1_0_2_REV_A: PHYVersion
RP001_V1_0_2: PHYVersion
PHY_V1_0_2_REV_B: PHYVersion
RP001_V1_0_2_REV_B: PHYVersion
PHY_V1_1_REV_A: PHYVersion
RP001_V1_1_REV_A: PHYVersion
PHY_V1_1_REV_B: PHYVersion
RP001_V1_1_REV_B: PHYVersion
PHY_V1_0_3_REV_A: PHYVersion
RP001_V1_0_3_REV_A: PHYVersion
RP002_V1_0_0: PHYVersion
RP002_V1_0_1: PHYVersion
RP002_V1_0_2: PHYVersion
RP002_V1_0_3: PHYVersion
RP002_V1_0_4: PHYVersion
DATA_RATE_0: DataRateIndex
DATA_RATE_1: DataRateIndex
DATA_RATE_2: DataRateIndex
DATA_RATE_3: DataRateIndex
DATA_RATE_4: DataRateIndex
DATA_RATE_5: DataRateIndex
DATA_RATE_6: DataRateIndex
DATA_RATE_7: DataRateIndex
DATA_RATE_8: DataRateIndex
DATA_RATE_9: DataRateIndex
DATA_RATE_10: DataRateIndex
DATA_RATE_11: DataRateIndex
DATA_RATE_12: DataRateIndex
DATA_RATE_13: DataRateIndex
DATA_RATE_14: DataRateIndex
DATA_RATE_15: DataRateIndex
DATA_RATE_OFFSET_0: DataRateOffset
DATA_RATE_OFFSET_1: DataRateOffset
DATA_RATE_OFFSET_2: DataRateOffset
DATA_RATE_OFFSET_3: DataRateOffset
DATA_RATE_OFFSET_4: DataRateOffset
DATA_RATE_OFFSET_5: DataRateOffset
DATA_RATE_OFFSET_6: DataRateOffset
DATA_RATE_OFFSET_7: DataRateOffset
REJOIN_CONTEXT: JoinRequestType
REJOIN_SESSION: JoinRequestType
REJOIN_KEYS: JoinRequestType
JOIN: JoinRequestType
CONTEXT: RejoinRequestType
SESSION: RejoinRequestType
KEYS: RejoinRequestType
FREQUENCIES: CFListType
CHANNEL_MASKS: CFListType
CLASS_A: Class
CLASS_B: Class
CLASS_C: Class
LOWEST: TxSchedulePriority
LOW: TxSchedulePriority
BELOW_NORMAL: TxSchedulePriority
NORMAL: TxSchedulePriority
ABOVE_NORMAL: TxSchedulePriority
HIGH: TxSchedulePriority
HIGHEST: TxSchedulePriority
CID_RFU_0: MACCommandIdentifier
CID_RESET: MACCommandIdentifier
CID_LINK_CHECK: MACCommandIdentifier
CID_LINK_ADR: MACCommandIdentifier
CID_DUTY_CYCLE: MACCommandIdentifier
CID_RX_PARAM_SETUP: MACCommandIdentifier
CID_DEV_STATUS: MACCommandIdentifier
CID_NEW_CHANNEL: MACCommandIdentifier
CID_RX_TIMING_SETUP: MACCommandIdentifier
CID_TX_PARAM_SETUP: MACCommandIdentifier
CID_DL_CHANNEL: MACCommandIdentifier
CID_REKEY: MACCommandIdentifier
CID_ADR_PARAM_SETUP: MACCommandIdentifier
CID_DEVICE_TIME: MACCommandIdentifier
CID_FORCE_REJOIN: MACCommandIdentifier
CID_REJOIN_PARAM_SETUP: MACCommandIdentifier
CID_PING_SLOT_INFO: MACCommandIdentifier
CID_PING_SLOT_CHANNEL: MACCommandIdentifier
CID_BEACON_TIMING: MACCommandIdentifier
CID_BEACON_FREQ: MACCommandIdentifier
CID_DEVICE_MODE: MACCommandIdentifier
CID_RELAY_CONF: MACCommandIdentifier
CID_RELAY_END_DEVICE_CONF: MACCommandIdentifier
CID_RELAY_FILTER_LIST: MACCommandIdentifier
CID_RELAY_UPDATE_UPLINK_LIST: MACCommandIdentifier
CID_RELAY_CTRL_UPLINK_LIST: MACCommandIdentifier
CID_RELAY_CONFIGURE_FWD_LIMIT: MACCommandIdentifier
CID_RELAY_NOTIFY_NEW_END_DEVICE: MACCommandIdentifier
RELAY_CAD_PERIODICITY_1_SECOND: RelayCADPeriodicity
RELAY_CAD_PERIODICITY_500_MILLISECONDS: RelayCADPeriodicity
RELAY_CAD_PERIODICITY_250_MILLISECONDS: RelayCADPeriodicity
RELAY_CAD_PERIODICITY_100_MILLISECONDS: RelayCADPeriodicity
RELAY_CAD_PERIODICITY_50_MILLISECONDS: RelayCADPeriodicity
RELAY_CAD_PERIODICITY_20_MILLISECONDS: RelayCADPeriodicity
RELAY_SECOND_CH_ACK_OFFSET_0: RelaySecondChAckOffset
RELAY_SECOND_CH_ACK_OFFSET_200: RelaySecondChAckOffset
RELAY_SECOND_CH_ACK_OFFSET_400: RelaySecondChAckOffset
RELAY_SECOND_CH_ACK_OFFSET_800: RelaySecondChAckOffset
RELAY_SECOND_CH_ACK_OFFSET_1600: RelaySecondChAckOffset
RELAY_SECOND_CH_ACK_OFFSET_3200: RelaySecondChAckOffset
RELAY_LIMIT_BUCKET_SIZE_1: RelayLimitBucketSize
RELAY_LIMIT_BUCKET_SIZE_2: RelayLimitBucketSize
RELAY_LIMIT_BUCKET_SIZE_4: RelayLimitBucketSize
RELAY_LIMIT_BUCKET_SIZE_12: RelayLimitBucketSize
RELAY_SMART_ENABLE_LEVEL_8: RelaySmartEnableLevel
RELAY_SMART_ENABLE_LEVEL_16: RelaySmartEnableLevel
RELAY_SMART_ENABLE_LEVEL_32: RelaySmartEnableLevel
RELAY_SMART_ENABLE_LEVEL_64: RelaySmartEnableLevel
RELAY_WOR_CHANNEL_DEFAULT: RelayWORChannel
RELAY_WOR_CHANNEL_SECONDARY: RelayWORChannel
RELAY_RESET_LIMIT_COUNTER_ZERO: RelayResetLimitCounter
RELAY_RESET_LIMIT_COUNTER_RELOAD_RATE: RelayResetLimitCounter
RELAY_RESET_LIMIT_COUNTER_MAX_VALUE: RelayResetLimitCounter
RELAY_RESET_LIMIT_COUNTER_NO_RESET: RelayResetLimitCounter
RELAY_CTRL_UPLINK_LIST_ACTION_READ_W_F_CNT: RelayCtrlUplinkListAction
RELAY_CTRL_UPLINK_LIST_ACTION_REMOVE_TRUSTED_END_DEVICE: RelayCtrlUplinkListAction
DUTY_CYCLE_1: AggregatedDutyCycle
DUTY_CYCLE_2: AggregatedDutyCycle
DUTY_CYCLE_4: AggregatedDutyCycle
DUTY_CYCLE_8: AggregatedDutyCycle
DUTY_CYCLE_16: AggregatedDutyCycle
DUTY_CYCLE_32: AggregatedDutyCycle
DUTY_CYCLE_64: AggregatedDutyCycle
DUTY_CYCLE_128: AggregatedDutyCycle
DUTY_CYCLE_256: AggregatedDutyCycle
DUTY_CYCLE_512: AggregatedDutyCycle
DUTY_CYCLE_1024: AggregatedDutyCycle
DUTY_CYCLE_2048: AggregatedDutyCycle
DUTY_CYCLE_4096: AggregatedDutyCycle
DUTY_CYCLE_8192: AggregatedDutyCycle
DUTY_CYCLE_16384: AggregatedDutyCycle
DUTY_CYCLE_32768: AggregatedDutyCycle
PING_EVERY_1S: PingSlotPeriod
PING_EVERY_2S: PingSlotPeriod
PING_EVERY_4S: PingSlotPeriod
PING_EVERY_8S: PingSlotPeriod
PING_EVERY_16S: PingSlotPeriod
PING_EVERY_32S: PingSlotPeriod
PING_EVERY_64S: PingSlotPeriod
PING_EVERY_128S: PingSlotPeriod
REJOIN_COUNT_16: RejoinCountExponent
REJOIN_COUNT_32: RejoinCountExponent
REJOIN_COUNT_64: RejoinCountExponent
REJOIN_COUNT_128: RejoinCountExponent
REJOIN_COUNT_256: RejoinCountExponent
REJOIN_COUNT_512: RejoinCountExponent
REJOIN_COUNT_1024: RejoinCountExponent
REJOIN_COUNT_2048: RejoinCountExponent
REJOIN_COUNT_4096: RejoinCountExponent
REJOIN_COUNT_8192: RejoinCountExponent
REJOIN_COUNT_16384: RejoinCountExponent
REJOIN_COUNT_32768: RejoinCountExponent
REJOIN_COUNT_65536: RejoinCountExponent
REJOIN_COUNT_131072: RejoinCountExponent
REJOIN_COUNT_262144: RejoinCountExponent
REJOIN_COUNT_524288: RejoinCountExponent
REJOIN_TIME_0: RejoinTimeExponent
REJOIN_TIME_1: RejoinTimeExponent
REJOIN_TIME_2: RejoinTimeExponent
REJOIN_TIME_3: RejoinTimeExponent
REJOIN_TIME_4: RejoinTimeExponent
REJOIN_TIME_5: RejoinTimeExponent
REJOIN_TIME_6: RejoinTimeExponent
REJOIN_TIME_7: RejoinTimeExponent
REJOIN_TIME_8: RejoinTimeExponent
REJOIN_TIME_9: RejoinTimeExponent
REJOIN_TIME_10: RejoinTimeExponent
REJOIN_TIME_11: RejoinTimeExponent
REJOIN_TIME_12: RejoinTimeExponent
REJOIN_TIME_13: RejoinTimeExponent
REJOIN_TIME_14: RejoinTimeExponent
REJOIN_TIME_15: RejoinTimeExponent
REJOIN_PERIOD_0: RejoinPeriodExponent
REJOIN_PERIOD_1: RejoinPeriodExponent
REJOIN_PERIOD_2: RejoinPeriodExponent
REJOIN_PERIOD_3: RejoinPeriodExponent
REJOIN_PERIOD_4: RejoinPeriodExponent
REJOIN_PERIOD_5: RejoinPeriodExponent
REJOIN_PERIOD_6: RejoinPeriodExponent
REJOIN_PERIOD_7: RejoinPeriodExponent
DEVICE_EIRP_8: DeviceEIRP
DEVICE_EIRP_10: DeviceEIRP
DEVICE_EIRP_12: DeviceEIRP
DEVICE_EIRP_13: DeviceEIRP
DEVICE_EIRP_14: DeviceEIRP
DEVICE_EIRP_16: DeviceEIRP
DEVICE_EIRP_18: DeviceEIRP
DEVICE_EIRP_20: DeviceEIRP
DEVICE_EIRP_21: DeviceEIRP
DEVICE_EIRP_24: DeviceEIRP
DEVICE_EIRP_26: DeviceEIRP
DEVICE_EIRP_27: DeviceEIRP
DEVICE_EIRP_29: DeviceEIRP
DEVICE_EIRP_30: DeviceEIRP
DEVICE_EIRP_33: DeviceEIRP
DEVICE_EIRP_36: DeviceEIRP
ADR_ACK_LIMIT_1: ADRAckLimitExponent
ADR_ACK_LIMIT_2: ADRAckLimitExponent
ADR_ACK_LIMIT_4: ADRAckLimitExponent
ADR_ACK_LIMIT_8: ADRAckLimitExponent
ADR_ACK_LIMIT_16: ADRAckLimitExponent
ADR_ACK_LIMIT_32: ADRAckLimitExponent
ADR_ACK_LIMIT_64: ADRAckLimitExponent
ADR_ACK_LIMIT_128: ADRAckLimitExponent
ADR_ACK_LIMIT_256: ADRAckLimitExponent
ADR_ACK_LIMIT_512: ADRAckLimitExponent
ADR_ACK_LIMIT_1024: ADRAckLimitExponent
ADR_ACK_LIMIT_2048: ADRAckLimitExponent
ADR_ACK_LIMIT_4096: ADRAckLimitExponent
ADR_ACK_LIMIT_8192: ADRAckLimitExponent
ADR_ACK_LIMIT_16384: ADRAckLimitExponent
ADR_ACK_LIMIT_32768: ADRAckLimitExponent
ADR_ACK_DELAY_1: ADRAckDelayExponent
ADR_ACK_DELAY_2: ADRAckDelayExponent
ADR_ACK_DELAY_4: ADRAckDelayExponent
ADR_ACK_DELAY_8: ADRAckDelayExponent
ADR_ACK_DELAY_16: ADRAckDelayExponent
ADR_ACK_DELAY_32: ADRAckDelayExponent
ADR_ACK_DELAY_64: ADRAckDelayExponent
ADR_ACK_DELAY_128: ADRAckDelayExponent
ADR_ACK_DELAY_256: ADRAckDelayExponent
ADR_ACK_DELAY_512: ADRAckDelayExponent
ADR_ACK_DELAY_1024: ADRAckDelayExponent
ADR_ACK_DELAY_2048: ADRAckDelayExponent
ADR_ACK_DELAY_4096: ADRAckDelayExponent
ADR_ACK_DELAY_8192: ADRAckDelayExponent
ADR_ACK_DELAY_16384: ADRAckDelayExponent
ADR_ACK_DELAY_32768: ADRAckDelayExponent
RX_DELAY_0: RxDelay
RX_DELAY_1: RxDelay
RX_DELAY_2: RxDelay
RX_DELAY_3: RxDelay
RX_DELAY_4: RxDelay
RX_DELAY_5: RxDelay
RX_DELAY_6: RxDelay
RX_DELAY_7: RxDelay
RX_DELAY_8: RxDelay
RX_DELAY_9: RxDelay
RX_DELAY_10: RxDelay
RX_DELAY_11: RxDelay
RX_DELAY_12: RxDelay
RX_DELAY_13: RxDelay
RX_DELAY_14: RxDelay
RX_DELAY_15: RxDelay
MINOR_RFU_0: Minor
MINOR_1: Minor
MINOR_RFU_2: Minor
MINOR_RFU_3: Minor
MINOR_RFU_4: Minor
MINOR_RFU_5: Minor
MINOR_RFU_6: Minor
MINOR_RFU_7: Minor
MINOR_RFU_8: Minor
MINOR_RFU_9: Minor
MINOR_RFU_10: Minor
MINOR_RFU_11: Minor
MINOR_RFU_12: Minor
MINOR_RFU_13: Minor
MINOR_RFU_14: Minor
MINOR_RFU_15: Minor

class Message(_message.Message):
    __slots__ = ("m_hdr", "mic", "mac_payload", "join_request_payload", "join_accept_payload", "rejoin_request_payload")
    M_HDR_FIELD_NUMBER: _ClassVar[int]
    MIC_FIELD_NUMBER: _ClassVar[int]
    MAC_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    JOIN_REQUEST_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REJOIN_REQUEST_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    m_hdr: MHDR
    mic: bytes
    mac_payload: MACPayload
    join_request_payload: JoinRequestPayload
    join_accept_payload: JoinAcceptPayload
    rejoin_request_payload: RejoinRequestPayload
    def __init__(self, m_hdr: _Optional[_Union[MHDR, _Mapping]] = ..., mic: _Optional[bytes] = ..., mac_payload: _Optional[_Union[MACPayload, _Mapping]] = ..., join_request_payload: _Optional[_Union[JoinRequestPayload, _Mapping]] = ..., join_accept_payload: _Optional[_Union[JoinAcceptPayload, _Mapping]] = ..., rejoin_request_payload: _Optional[_Union[RejoinRequestPayload, _Mapping]] = ...) -> None: ...

class MHDR(_message.Message):
    __slots__ = ("m_type", "major")
    M_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    m_type: MType
    major: Major
    def __init__(self, m_type: _Optional[_Union[MType, str]] = ..., major: _Optional[_Union[Major, str]] = ...) -> None: ...

class MACPayload(_message.Message):
    __slots__ = ("f_hdr", "f_port", "frm_payload", "decoded_payload", "full_f_cnt")
    F_HDR_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    DECODED_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    FULL_F_CNT_FIELD_NUMBER: _ClassVar[int]
    f_hdr: FHDR
    f_port: int
    frm_payload: bytes
    decoded_payload: _struct_pb2.Struct
    full_f_cnt: int
    def __init__(self, f_hdr: _Optional[_Union[FHDR, _Mapping]] = ..., f_port: _Optional[int] = ..., frm_payload: _Optional[bytes] = ..., decoded_payload: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., full_f_cnt: _Optional[int] = ...) -> None: ...

class FHDR(_message.Message):
    __slots__ = ("dev_addr", "f_ctrl", "f_cnt", "f_opts")
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    F_CTRL_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_OPTS_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    f_ctrl: FCtrl
    f_cnt: int
    f_opts: bytes
    def __init__(self, dev_addr: _Optional[bytes] = ..., f_ctrl: _Optional[_Union[FCtrl, _Mapping]] = ..., f_cnt: _Optional[int] = ..., f_opts: _Optional[bytes] = ...) -> None: ...

class FCtrl(_message.Message):
    __slots__ = ("adr", "adr_ack_req", "ack", "f_pending", "class_b")
    ADR_FIELD_NUMBER: _ClassVar[int]
    ADR_ACK_REQ_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    F_PENDING_FIELD_NUMBER: _ClassVar[int]
    CLASS_B_FIELD_NUMBER: _ClassVar[int]
    adr: bool
    adr_ack_req: bool
    ack: bool
    f_pending: bool
    class_b: bool
    def __init__(self, adr: bool = ..., adr_ack_req: bool = ..., ack: bool = ..., f_pending: bool = ..., class_b: bool = ...) -> None: ...

class JoinRequestPayload(_message.Message):
    __slots__ = ("join_eui", "dev_eui", "dev_nonce")
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_NONCE_FIELD_NUMBER: _ClassVar[int]
    join_eui: bytes
    dev_eui: bytes
    dev_nonce: bytes
    def __init__(self, join_eui: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ..., dev_nonce: _Optional[bytes] = ...) -> None: ...

class RejoinRequestPayload(_message.Message):
    __slots__ = ("rejoin_type", "net_id", "join_eui", "dev_eui", "rejoin_cnt")
    REJOIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    REJOIN_CNT_FIELD_NUMBER: _ClassVar[int]
    rejoin_type: RejoinRequestType
    net_id: bytes
    join_eui: bytes
    dev_eui: bytes
    rejoin_cnt: int
    def __init__(self, rejoin_type: _Optional[_Union[RejoinRequestType, str]] = ..., net_id: _Optional[bytes] = ..., join_eui: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ..., rejoin_cnt: _Optional[int] = ...) -> None: ...

class JoinAcceptPayload(_message.Message):
    __slots__ = ("encrypted", "join_nonce", "net_id", "dev_addr", "dl_settings", "rx_delay", "cf_list")
    ENCRYPTED_FIELD_NUMBER: _ClassVar[int]
    JOIN_NONCE_FIELD_NUMBER: _ClassVar[int]
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    DL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RX_DELAY_FIELD_NUMBER: _ClassVar[int]
    CF_LIST_FIELD_NUMBER: _ClassVar[int]
    encrypted: bytes
    join_nonce: bytes
    net_id: bytes
    dev_addr: bytes
    dl_settings: DLSettings
    rx_delay: RxDelay
    cf_list: CFList
    def __init__(self, encrypted: _Optional[bytes] = ..., join_nonce: _Optional[bytes] = ..., net_id: _Optional[bytes] = ..., dev_addr: _Optional[bytes] = ..., dl_settings: _Optional[_Union[DLSettings, _Mapping]] = ..., rx_delay: _Optional[_Union[RxDelay, str]] = ..., cf_list: _Optional[_Union[CFList, _Mapping]] = ...) -> None: ...

class DLSettings(_message.Message):
    __slots__ = ("rx1_dr_offset", "rx2_dr", "opt_neg")
    RX1_DR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RX2_DR_FIELD_NUMBER: _ClassVar[int]
    OPT_NEG_FIELD_NUMBER: _ClassVar[int]
    rx1_dr_offset: DataRateOffset
    rx2_dr: DataRateIndex
    opt_neg: bool
    def __init__(self, rx1_dr_offset: _Optional[_Union[DataRateOffset, str]] = ..., rx2_dr: _Optional[_Union[DataRateIndex, str]] = ..., opt_neg: bool = ...) -> None: ...

class CFList(_message.Message):
    __slots__ = ("type", "freq", "ch_masks")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FREQ_FIELD_NUMBER: _ClassVar[int]
    CH_MASKS_FIELD_NUMBER: _ClassVar[int]
    type: CFListType
    freq: _containers.RepeatedScalarFieldContainer[int]
    ch_masks: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, type: _Optional[_Union[CFListType, str]] = ..., freq: _Optional[_Iterable[int]] = ..., ch_masks: _Optional[_Iterable[bool]] = ...) -> None: ...

class LoRaDataRate(_message.Message):
    __slots__ = ("bandwidth", "spreading_factor", "coding_rate")
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    SPREADING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    CODING_RATE_FIELD_NUMBER: _ClassVar[int]
    bandwidth: int
    spreading_factor: int
    coding_rate: str
    def __init__(self, bandwidth: _Optional[int] = ..., spreading_factor: _Optional[int] = ..., coding_rate: _Optional[str] = ...) -> None: ...

class FSKDataRate(_message.Message):
    __slots__ = ("bit_rate",)
    BIT_RATE_FIELD_NUMBER: _ClassVar[int]
    bit_rate: int
    def __init__(self, bit_rate: _Optional[int] = ...) -> None: ...

class LRFHSSDataRate(_message.Message):
    __slots__ = ("modulation_type", "operating_channel_width", "coding_rate")
    MODULATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_CHANNEL_WIDTH_FIELD_NUMBER: _ClassVar[int]
    CODING_RATE_FIELD_NUMBER: _ClassVar[int]
    modulation_type: int
    operating_channel_width: int
    coding_rate: str
    def __init__(self, modulation_type: _Optional[int] = ..., operating_channel_width: _Optional[int] = ..., coding_rate: _Optional[str] = ...) -> None: ...

class DataRate(_message.Message):
    __slots__ = ("lora", "fsk", "lrfhss")
    LORA_FIELD_NUMBER: _ClassVar[int]
    FSK_FIELD_NUMBER: _ClassVar[int]
    LRFHSS_FIELD_NUMBER: _ClassVar[int]
    lora: LoRaDataRate
    fsk: FSKDataRate
    lrfhss: LRFHSSDataRate
    def __init__(self, lora: _Optional[_Union[LoRaDataRate, _Mapping]] = ..., fsk: _Optional[_Union[FSKDataRate, _Mapping]] = ..., lrfhss: _Optional[_Union[LRFHSSDataRate, _Mapping]] = ...) -> None: ...

class TxSettings(_message.Message):
    __slots__ = ("data_rate", "frequency", "enable_crc", "timestamp", "time", "downlink", "concentrator_timestamp")
    class Downlink(_message.Message):
        __slots__ = ("antenna_index", "tx_power", "invert_polarization")
        ANTENNA_INDEX_FIELD_NUMBER: _ClassVar[int]
        TX_POWER_FIELD_NUMBER: _ClassVar[int]
        INVERT_POLARIZATION_FIELD_NUMBER: _ClassVar[int]
        antenna_index: int
        tx_power: float
        invert_polarization: bool
        def __init__(self, antenna_index: _Optional[int] = ..., tx_power: _Optional[float] = ..., invert_polarization: bool = ...) -> None: ...
    DATA_RATE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CRC_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATOR_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    data_rate: DataRate
    frequency: int
    enable_crc: bool
    timestamp: int
    time: _timestamp_pb2.Timestamp
    downlink: TxSettings.Downlink
    concentrator_timestamp: int
    def __init__(self, data_rate: _Optional[_Union[DataRate, _Mapping]] = ..., frequency: _Optional[int] = ..., enable_crc: bool = ..., timestamp: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., downlink: _Optional[_Union[TxSettings.Downlink, _Mapping]] = ..., concentrator_timestamp: _Optional[int] = ...) -> None: ...

class GatewayAntennaIdentifiers(_message.Message):
    __slots__ = ("gateway_ids", "antenna_index")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_INDEX_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    antenna_index: int
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., antenna_index: _Optional[int] = ...) -> None: ...

class ClassBCGatewayIdentifiers(_message.Message):
    __slots__ = ("gateway_ids", "antenna_index", "group_index")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_INDEX_FIELD_NUMBER: _ClassVar[int]
    GROUP_INDEX_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    antenna_index: int
    group_index: int
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., antenna_index: _Optional[int] = ..., group_index: _Optional[int] = ...) -> None: ...

class UplinkToken(_message.Message):
    __slots__ = ("ids", "timestamp", "server_time", "concentrator_time", "gateway_time")
    IDS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
    CONCENTRATOR_TIME_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_TIME_FIELD_NUMBER: _ClassVar[int]
    ids: GatewayAntennaIdentifiers
    timestamp: int
    server_time: _timestamp_pb2.Timestamp
    concentrator_time: int
    gateway_time: _timestamp_pb2.Timestamp
    def __init__(self, ids: _Optional[_Union[GatewayAntennaIdentifiers, _Mapping]] = ..., timestamp: _Optional[int] = ..., server_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., concentrator_time: _Optional[int] = ..., gateway_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DownlinkPath(_message.Message):
    __slots__ = ("uplink_token", "fixed")
    UPLINK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    uplink_token: bytes
    fixed: GatewayAntennaIdentifiers
    def __init__(self, uplink_token: _Optional[bytes] = ..., fixed: _Optional[_Union[GatewayAntennaIdentifiers, _Mapping]] = ...) -> None: ...

class TxRequest(_message.Message):
    __slots__ = ("downlink_paths", "rx1_delay", "rx1_data_rate", "rx1_frequency", "rx2_data_rate", "rx2_frequency", "priority", "absolute_time", "frequency_plan_id", "advanced")
    CLASS_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_PATHS_FIELD_NUMBER: _ClassVar[int]
    RX1_DELAY_FIELD_NUMBER: _ClassVar[int]
    RX1_DATA_RATE_FIELD_NUMBER: _ClassVar[int]
    RX1_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RX2_DATA_RATE_FIELD_NUMBER: _ClassVar[int]
    RX2_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_TIME_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    downlink_paths: _containers.RepeatedCompositeFieldContainer[DownlinkPath]
    rx1_delay: RxDelay
    rx1_data_rate: DataRate
    rx1_frequency: int
    rx2_data_rate: DataRate
    rx2_frequency: int
    priority: TxSchedulePriority
    absolute_time: _timestamp_pb2.Timestamp
    frequency_plan_id: str
    advanced: _struct_pb2.Struct
    def __init__(self, downlink_paths: _Optional[_Iterable[_Union[DownlinkPath, _Mapping]]] = ..., rx1_delay: _Optional[_Union[RxDelay, str]] = ..., rx1_data_rate: _Optional[_Union[DataRate, _Mapping]] = ..., rx1_frequency: _Optional[int] = ..., rx2_data_rate: _Optional[_Union[DataRate, _Mapping]] = ..., rx2_frequency: _Optional[int] = ..., priority: _Optional[_Union[TxSchedulePriority, str]] = ..., absolute_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., frequency_plan_id: _Optional[str] = ..., advanced: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., **kwargs) -> None: ...

class RelaySecondChannel(_message.Message):
    __slots__ = ("ack_offset", "data_rate_index", "frequency")
    ACK_OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    ack_offset: RelaySecondChAckOffset
    data_rate_index: DataRateIndex
    frequency: int
    def __init__(self, ack_offset: _Optional[_Union[RelaySecondChAckOffset, str]] = ..., data_rate_index: _Optional[_Union[DataRateIndex, str]] = ..., frequency: _Optional[int] = ...) -> None: ...

class RelayUplinkForwardLimits(_message.Message):
    __slots__ = ("bucket_size", "reload_rate")
    BUCKET_SIZE_FIELD_NUMBER: _ClassVar[int]
    RELOAD_RATE_FIELD_NUMBER: _ClassVar[int]
    bucket_size: RelayLimitBucketSize
    reload_rate: int
    def __init__(self, bucket_size: _Optional[_Union[RelayLimitBucketSize, str]] = ..., reload_rate: _Optional[int] = ...) -> None: ...

class RelayForwardLimits(_message.Message):
    __slots__ = ("bucket_size", "reload_rate")
    BUCKET_SIZE_FIELD_NUMBER: _ClassVar[int]
    RELOAD_RATE_FIELD_NUMBER: _ClassVar[int]
    bucket_size: RelayLimitBucketSize
    reload_rate: int
    def __init__(self, bucket_size: _Optional[_Union[RelayLimitBucketSize, str]] = ..., reload_rate: _Optional[int] = ...) -> None: ...

class RelayEndDeviceAlwaysMode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RelayEndDeviceDynamicMode(_message.Message):
    __slots__ = ("smart_enable_level",)
    SMART_ENABLE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    smart_enable_level: RelaySmartEnableLevel
    def __init__(self, smart_enable_level: _Optional[_Union[RelaySmartEnableLevel, str]] = ...) -> None: ...

class RelayEndDeviceControlledMode(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MACCommand(_message.Message):
    __slots__ = ("cid", "raw_payload", "reset_ind", "reset_conf", "link_check_ans", "link_adr_req", "link_adr_ans", "duty_cycle_req", "rx_param_setup_req", "rx_param_setup_ans", "dev_status_ans", "new_channel_req", "new_channel_ans", "dl_channel_req", "dl_channel_ans", "rx_timing_setup_req", "tx_param_setup_req", "rekey_ind", "rekey_conf", "adr_param_setup_req", "device_time_ans", "force_rejoin_req", "rejoin_param_setup_req", "rejoin_param_setup_ans", "ping_slot_info_req", "ping_slot_channel_req", "ping_slot_channel_ans", "beacon_timing_ans", "beacon_freq_req", "beacon_freq_ans", "device_mode_ind", "device_mode_conf", "relay_conf_req", "relay_conf_ans", "relay_end_device_conf_req", "relay_end_device_conf_ans", "relay_update_uplink_list_req", "relay_update_uplink_list_ans", "relay_ctrl_uplink_list_req", "relay_ctrl_uplink_list_ans", "relay_configure_fwd_limit_req", "relay_configure_fwd_limit_ans", "relay_notify_new_end_device_req")
    class ResetInd(_message.Message):
        __slots__ = ("minor_version",)
        MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        minor_version: Minor
        def __init__(self, minor_version: _Optional[_Union[Minor, str]] = ...) -> None: ...
    class ResetConf(_message.Message):
        __slots__ = ("minor_version",)
        MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        minor_version: Minor
        def __init__(self, minor_version: _Optional[_Union[Minor, str]] = ...) -> None: ...
    class LinkCheckAns(_message.Message):
        __slots__ = ("margin", "gateway_count")
        MARGIN_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_COUNT_FIELD_NUMBER: _ClassVar[int]
        margin: int
        gateway_count: int
        def __init__(self, margin: _Optional[int] = ..., gateway_count: _Optional[int] = ...) -> None: ...
    class LinkADRReq(_message.Message):
        __slots__ = ("data_rate_index", "tx_power_index", "channel_mask", "channel_mask_control", "nb_trans")
        DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        TX_POWER_INDEX_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_MASK_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_MASK_CONTROL_FIELD_NUMBER: _ClassVar[int]
        NB_TRANS_FIELD_NUMBER: _ClassVar[int]
        data_rate_index: DataRateIndex
        tx_power_index: int
        channel_mask: _containers.RepeatedScalarFieldContainer[bool]
        channel_mask_control: int
        nb_trans: int
        def __init__(self, data_rate_index: _Optional[_Union[DataRateIndex, str]] = ..., tx_power_index: _Optional[int] = ..., channel_mask: _Optional[_Iterable[bool]] = ..., channel_mask_control: _Optional[int] = ..., nb_trans: _Optional[int] = ...) -> None: ...
    class LinkADRAns(_message.Message):
        __slots__ = ("channel_mask_ack", "data_rate_index_ack", "tx_power_index_ack")
        CHANNEL_MASK_ACK_FIELD_NUMBER: _ClassVar[int]
        DATA_RATE_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        TX_POWER_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        channel_mask_ack: bool
        data_rate_index_ack: bool
        tx_power_index_ack: bool
        def __init__(self, channel_mask_ack: bool = ..., data_rate_index_ack: bool = ..., tx_power_index_ack: bool = ...) -> None: ...
    class DutyCycleReq(_message.Message):
        __slots__ = ("max_duty_cycle",)
        MAX_DUTY_CYCLE_FIELD_NUMBER: _ClassVar[int]
        max_duty_cycle: AggregatedDutyCycle
        def __init__(self, max_duty_cycle: _Optional[_Union[AggregatedDutyCycle, str]] = ...) -> None: ...
    class RxParamSetupReq(_message.Message):
        __slots__ = ("rx2_data_rate_index", "rx1_data_rate_offset", "rx2_frequency")
        RX2_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        RX1_DATA_RATE_OFFSET_FIELD_NUMBER: _ClassVar[int]
        RX2_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        rx2_data_rate_index: DataRateIndex
        rx1_data_rate_offset: DataRateOffset
        rx2_frequency: int
        def __init__(self, rx2_data_rate_index: _Optional[_Union[DataRateIndex, str]] = ..., rx1_data_rate_offset: _Optional[_Union[DataRateOffset, str]] = ..., rx2_frequency: _Optional[int] = ...) -> None: ...
    class RxParamSetupAns(_message.Message):
        __slots__ = ("rx2_data_rate_index_ack", "rx1_data_rate_offset_ack", "rx2_frequency_ack")
        RX2_DATA_RATE_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        RX1_DATA_RATE_OFFSET_ACK_FIELD_NUMBER: _ClassVar[int]
        RX2_FREQUENCY_ACK_FIELD_NUMBER: _ClassVar[int]
        rx2_data_rate_index_ack: bool
        rx1_data_rate_offset_ack: bool
        rx2_frequency_ack: bool
        def __init__(self, rx2_data_rate_index_ack: bool = ..., rx1_data_rate_offset_ack: bool = ..., rx2_frequency_ack: bool = ...) -> None: ...
    class DevStatusAns(_message.Message):
        __slots__ = ("battery", "margin")
        BATTERY_FIELD_NUMBER: _ClassVar[int]
        MARGIN_FIELD_NUMBER: _ClassVar[int]
        battery: int
        margin: int
        def __init__(self, battery: _Optional[int] = ..., margin: _Optional[int] = ...) -> None: ...
    class NewChannelReq(_message.Message):
        __slots__ = ("channel_index", "frequency", "min_data_rate_index", "max_data_rate_index")
        CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        MIN_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        channel_index: int
        frequency: int
        min_data_rate_index: DataRateIndex
        max_data_rate_index: DataRateIndex
        def __init__(self, channel_index: _Optional[int] = ..., frequency: _Optional[int] = ..., min_data_rate_index: _Optional[_Union[DataRateIndex, str]] = ..., max_data_rate_index: _Optional[_Union[DataRateIndex, str]] = ...) -> None: ...
    class NewChannelAns(_message.Message):
        __slots__ = ("frequency_ack", "data_rate_ack")
        FREQUENCY_ACK_FIELD_NUMBER: _ClassVar[int]
        DATA_RATE_ACK_FIELD_NUMBER: _ClassVar[int]
        frequency_ack: bool
        data_rate_ack: bool
        def __init__(self, frequency_ack: bool = ..., data_rate_ack: bool = ...) -> None: ...
    class DLChannelReq(_message.Message):
        __slots__ = ("channel_index", "frequency")
        CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        channel_index: int
        frequency: int
        def __init__(self, channel_index: _Optional[int] = ..., frequency: _Optional[int] = ...) -> None: ...
    class DLChannelAns(_message.Message):
        __slots__ = ("channel_index_ack", "frequency_ack")
        CHANNEL_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_ACK_FIELD_NUMBER: _ClassVar[int]
        channel_index_ack: bool
        frequency_ack: bool
        def __init__(self, channel_index_ack: bool = ..., frequency_ack: bool = ...) -> None: ...
    class RxTimingSetupReq(_message.Message):
        __slots__ = ("delay",)
        DELAY_FIELD_NUMBER: _ClassVar[int]
        delay: RxDelay
        def __init__(self, delay: _Optional[_Union[RxDelay, str]] = ...) -> None: ...
    class TxParamSetupReq(_message.Message):
        __slots__ = ("max_eirp_index", "uplink_dwell_time", "downlink_dwell_time")
        MAX_EIRP_INDEX_FIELD_NUMBER: _ClassVar[int]
        UPLINK_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
        DOWNLINK_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
        max_eirp_index: DeviceEIRP
        uplink_dwell_time: bool
        downlink_dwell_time: bool
        def __init__(self, max_eirp_index: _Optional[_Union[DeviceEIRP, str]] = ..., uplink_dwell_time: bool = ..., downlink_dwell_time: bool = ...) -> None: ...
    class RekeyInd(_message.Message):
        __slots__ = ("minor_version",)
        MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        minor_version: Minor
        def __init__(self, minor_version: _Optional[_Union[Minor, str]] = ...) -> None: ...
    class RekeyConf(_message.Message):
        __slots__ = ("minor_version",)
        MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
        minor_version: Minor
        def __init__(self, minor_version: _Optional[_Union[Minor, str]] = ...) -> None: ...
    class ADRParamSetupReq(_message.Message):
        __slots__ = ("adr_ack_limit_exponent", "adr_ack_delay_exponent")
        ADR_ACK_LIMIT_EXPONENT_FIELD_NUMBER: _ClassVar[int]
        ADR_ACK_DELAY_EXPONENT_FIELD_NUMBER: _ClassVar[int]
        adr_ack_limit_exponent: ADRAckLimitExponent
        adr_ack_delay_exponent: ADRAckDelayExponent
        def __init__(self, adr_ack_limit_exponent: _Optional[_Union[ADRAckLimitExponent, str]] = ..., adr_ack_delay_exponent: _Optional[_Union[ADRAckDelayExponent, str]] = ...) -> None: ...
    class DeviceTimeAns(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: _timestamp_pb2.Timestamp
        def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class ForceRejoinReq(_message.Message):
        __slots__ = ("rejoin_type", "data_rate_index", "max_retries", "period_exponent")
        REJOIN_TYPE_FIELD_NUMBER: _ClassVar[int]
        DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_RETRIES_FIELD_NUMBER: _ClassVar[int]
        PERIOD_EXPONENT_FIELD_NUMBER: _ClassVar[int]
        rejoin_type: RejoinRequestType
        data_rate_index: DataRateIndex
        max_retries: int
        period_exponent: RejoinPeriodExponent
        def __init__(self, rejoin_type: _Optional[_Union[RejoinRequestType, str]] = ..., data_rate_index: _Optional[_Union[DataRateIndex, str]] = ..., max_retries: _Optional[int] = ..., period_exponent: _Optional[_Union[RejoinPeriodExponent, str]] = ...) -> None: ...
    class RejoinParamSetupReq(_message.Message):
        __slots__ = ("max_count_exponent", "max_time_exponent")
        MAX_COUNT_EXPONENT_FIELD_NUMBER: _ClassVar[int]
        MAX_TIME_EXPONENT_FIELD_NUMBER: _ClassVar[int]
        max_count_exponent: RejoinCountExponent
        max_time_exponent: RejoinTimeExponent
        def __init__(self, max_count_exponent: _Optional[_Union[RejoinCountExponent, str]] = ..., max_time_exponent: _Optional[_Union[RejoinTimeExponent, str]] = ...) -> None: ...
    class RejoinParamSetupAns(_message.Message):
        __slots__ = ("max_time_exponent_ack",)
        MAX_TIME_EXPONENT_ACK_FIELD_NUMBER: _ClassVar[int]
        max_time_exponent_ack: bool
        def __init__(self, max_time_exponent_ack: bool = ...) -> None: ...
    class PingSlotInfoReq(_message.Message):
        __slots__ = ("period",)
        PERIOD_FIELD_NUMBER: _ClassVar[int]
        period: PingSlotPeriod
        def __init__(self, period: _Optional[_Union[PingSlotPeriod, str]] = ...) -> None: ...
    class PingSlotChannelReq(_message.Message):
        __slots__ = ("frequency", "data_rate_index")
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
        frequency: int
        data_rate_index: DataRateIndex
        def __init__(self, frequency: _Optional[int] = ..., data_rate_index: _Optional[_Union[DataRateIndex, str]] = ...) -> None: ...
    class PingSlotChannelAns(_message.Message):
        __slots__ = ("frequency_ack", "data_rate_index_ack")
        FREQUENCY_ACK_FIELD_NUMBER: _ClassVar[int]
        DATA_RATE_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        frequency_ack: bool
        data_rate_index_ack: bool
        def __init__(self, frequency_ack: bool = ..., data_rate_index_ack: bool = ...) -> None: ...
    class BeaconTimingAns(_message.Message):
        __slots__ = ("delay", "channel_index")
        DELAY_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
        delay: int
        channel_index: int
        def __init__(self, delay: _Optional[int] = ..., channel_index: _Optional[int] = ...) -> None: ...
    class BeaconFreqReq(_message.Message):
        __slots__ = ("frequency",)
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        frequency: int
        def __init__(self, frequency: _Optional[int] = ...) -> None: ...
    class BeaconFreqAns(_message.Message):
        __slots__ = ("frequency_ack",)
        FREQUENCY_ACK_FIELD_NUMBER: _ClassVar[int]
        frequency_ack: bool
        def __init__(self, frequency_ack: bool = ...) -> None: ...
    class DeviceModeInd(_message.Message):
        __slots__ = ()
        CLASS_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class DeviceModeConf(_message.Message):
        __slots__ = ()
        CLASS_FIELD_NUMBER: _ClassVar[int]
        def __init__(self, **kwargs) -> None: ...
    class RelayConfReq(_message.Message):
        __slots__ = ("configuration",)
        class Configuration(_message.Message):
            __slots__ = ("second_channel", "default_channel_index", "cad_periodicity")
            SECOND_CHANNEL_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
            CAD_PERIODICITY_FIELD_NUMBER: _ClassVar[int]
            second_channel: RelaySecondChannel
            default_channel_index: int
            cad_periodicity: RelayCADPeriodicity
            def __init__(self, second_channel: _Optional[_Union[RelaySecondChannel, _Mapping]] = ..., default_channel_index: _Optional[int] = ..., cad_periodicity: _Optional[_Union[RelayCADPeriodicity, str]] = ...) -> None: ...
        CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        configuration: MACCommand.RelayConfReq.Configuration
        def __init__(self, configuration: _Optional[_Union[MACCommand.RelayConfReq.Configuration, _Mapping]] = ...) -> None: ...
    class RelayConfAns(_message.Message):
        __slots__ = ("second_channel_frequency_ack", "second_channel_ack_offset_ack", "second_channel_data_rate_index_ack", "second_channel_index_ack", "default_channel_index_ack", "cad_periodicity_ack")
        SECOND_CHANNEL_FREQUENCY_ACK_FIELD_NUMBER: _ClassVar[int]
        SECOND_CHANNEL_ACK_OFFSET_ACK_FIELD_NUMBER: _ClassVar[int]
        SECOND_CHANNEL_DATA_RATE_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        SECOND_CHANNEL_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_CHANNEL_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        CAD_PERIODICITY_ACK_FIELD_NUMBER: _ClassVar[int]
        second_channel_frequency_ack: bool
        second_channel_ack_offset_ack: bool
        second_channel_data_rate_index_ack: bool
        second_channel_index_ack: bool
        default_channel_index_ack: bool
        cad_periodicity_ack: bool
        def __init__(self, second_channel_frequency_ack: bool = ..., second_channel_ack_offset_ack: bool = ..., second_channel_data_rate_index_ack: bool = ..., second_channel_index_ack: bool = ..., default_channel_index_ack: bool = ..., cad_periodicity_ack: bool = ...) -> None: ...
    class RelayEndDeviceConfReq(_message.Message):
        __slots__ = ("configuration",)
        class Configuration(_message.Message):
            __slots__ = ("always", "dynamic", "end_device_controlled", "backoff", "second_channel", "serving_device_id")
            ALWAYS_FIELD_NUMBER: _ClassVar[int]
            DYNAMIC_FIELD_NUMBER: _ClassVar[int]
            END_DEVICE_CONTROLLED_FIELD_NUMBER: _ClassVar[int]
            BACKOFF_FIELD_NUMBER: _ClassVar[int]
            SECOND_CHANNEL_FIELD_NUMBER: _ClassVar[int]
            SERVING_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
            always: RelayEndDeviceAlwaysMode
            dynamic: RelayEndDeviceDynamicMode
            end_device_controlled: RelayEndDeviceControlledMode
            backoff: int
            second_channel: RelaySecondChannel
            serving_device_id: str
            def __init__(self, always: _Optional[_Union[RelayEndDeviceAlwaysMode, _Mapping]] = ..., dynamic: _Optional[_Union[RelayEndDeviceDynamicMode, _Mapping]] = ..., end_device_controlled: _Optional[_Union[RelayEndDeviceControlledMode, _Mapping]] = ..., backoff: _Optional[int] = ..., second_channel: _Optional[_Union[RelaySecondChannel, _Mapping]] = ..., serving_device_id: _Optional[str] = ...) -> None: ...
        CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
        configuration: MACCommand.RelayEndDeviceConfReq.Configuration
        def __init__(self, configuration: _Optional[_Union[MACCommand.RelayEndDeviceConfReq.Configuration, _Mapping]] = ...) -> None: ...
    class RelayEndDeviceConfAns(_message.Message):
        __slots__ = ("second_channel_frequency_ack", "second_channel_data_rate_index_ack", "second_channel_index_ack", "backoff_ack")
        SECOND_CHANNEL_FREQUENCY_ACK_FIELD_NUMBER: _ClassVar[int]
        SECOND_CHANNEL_DATA_RATE_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        SECOND_CHANNEL_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        BACKOFF_ACK_FIELD_NUMBER: _ClassVar[int]
        second_channel_frequency_ack: bool
        second_channel_data_rate_index_ack: bool
        second_channel_index_ack: bool
        backoff_ack: bool
        def __init__(self, second_channel_frequency_ack: bool = ..., second_channel_data_rate_index_ack: bool = ..., second_channel_index_ack: bool = ..., backoff_ack: bool = ...) -> None: ...
    class RelayUpdateUplinkListReq(_message.Message):
        __slots__ = ("rule_index", "forward_limits", "dev_addr", "w_f_cnt", "root_wor_s_key", "device_id", "session_key_id")
        RULE_INDEX_FIELD_NUMBER: _ClassVar[int]
        FORWARD_LIMITS_FIELD_NUMBER: _ClassVar[int]
        DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
        W_F_CNT_FIELD_NUMBER: _ClassVar[int]
        ROOT_WOR_S_KEY_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
        rule_index: int
        forward_limits: RelayUplinkForwardLimits
        dev_addr: bytes
        w_f_cnt: int
        root_wor_s_key: bytes
        device_id: str
        session_key_id: bytes
        def __init__(self, rule_index: _Optional[int] = ..., forward_limits: _Optional[_Union[RelayUplinkForwardLimits, _Mapping]] = ..., dev_addr: _Optional[bytes] = ..., w_f_cnt: _Optional[int] = ..., root_wor_s_key: _Optional[bytes] = ..., device_id: _Optional[str] = ..., session_key_id: _Optional[bytes] = ...) -> None: ...
    class RelayUpdateUplinkListAns(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RelayCtrlUplinkListReq(_message.Message):
        __slots__ = ("rule_index", "action")
        RULE_INDEX_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        rule_index: int
        action: RelayCtrlUplinkListAction
        def __init__(self, rule_index: _Optional[int] = ..., action: _Optional[_Union[RelayCtrlUplinkListAction, str]] = ...) -> None: ...
    class RelayCtrlUplinkListAns(_message.Message):
        __slots__ = ("rule_index_ack", "w_f_cnt")
        RULE_INDEX_ACK_FIELD_NUMBER: _ClassVar[int]
        W_F_CNT_FIELD_NUMBER: _ClassVar[int]
        rule_index_ack: bool
        w_f_cnt: int
        def __init__(self, rule_index_ack: bool = ..., w_f_cnt: _Optional[int] = ...) -> None: ...
    class RelayConfigureFwdLimitReq(_message.Message):
        __slots__ = ("reset_limit_counter", "join_request_limits", "notify_limits", "global_uplink_limits", "overall_limits")
        RESET_LIMIT_COUNTER_FIELD_NUMBER: _ClassVar[int]
        JOIN_REQUEST_LIMITS_FIELD_NUMBER: _ClassVar[int]
        NOTIFY_LIMITS_FIELD_NUMBER: _ClassVar[int]
        GLOBAL_UPLINK_LIMITS_FIELD_NUMBER: _ClassVar[int]
        OVERALL_LIMITS_FIELD_NUMBER: _ClassVar[int]
        reset_limit_counter: RelayResetLimitCounter
        join_request_limits: RelayForwardLimits
        notify_limits: RelayForwardLimits
        global_uplink_limits: RelayForwardLimits
        overall_limits: RelayForwardLimits
        def __init__(self, reset_limit_counter: _Optional[_Union[RelayResetLimitCounter, str]] = ..., join_request_limits: _Optional[_Union[RelayForwardLimits, _Mapping]] = ..., notify_limits: _Optional[_Union[RelayForwardLimits, _Mapping]] = ..., global_uplink_limits: _Optional[_Union[RelayForwardLimits, _Mapping]] = ..., overall_limits: _Optional[_Union[RelayForwardLimits, _Mapping]] = ...) -> None: ...
    class RelayConfigureFwdLimitAns(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RelayNotifyNewEndDeviceReq(_message.Message):
        __slots__ = ("dev_addr", "snr", "rssi")
        DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
        SNR_FIELD_NUMBER: _ClassVar[int]
        RSSI_FIELD_NUMBER: _ClassVar[int]
        dev_addr: bytes
        snr: int
        rssi: int
        def __init__(self, dev_addr: _Optional[bytes] = ..., snr: _Optional[int] = ..., rssi: _Optional[int] = ...) -> None: ...
    CID_FIELD_NUMBER: _ClassVar[int]
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    RESET_IND_FIELD_NUMBER: _ClassVar[int]
    RESET_CONF_FIELD_NUMBER: _ClassVar[int]
    LINK_CHECK_ANS_FIELD_NUMBER: _ClassVar[int]
    LINK_ADR_REQ_FIELD_NUMBER: _ClassVar[int]
    LINK_ADR_ANS_FIELD_NUMBER: _ClassVar[int]
    DUTY_CYCLE_REQ_FIELD_NUMBER: _ClassVar[int]
    RX_PARAM_SETUP_REQ_FIELD_NUMBER: _ClassVar[int]
    RX_PARAM_SETUP_ANS_FIELD_NUMBER: _ClassVar[int]
    DEV_STATUS_ANS_FIELD_NUMBER: _ClassVar[int]
    NEW_CHANNEL_REQ_FIELD_NUMBER: _ClassVar[int]
    NEW_CHANNEL_ANS_FIELD_NUMBER: _ClassVar[int]
    DL_CHANNEL_REQ_FIELD_NUMBER: _ClassVar[int]
    DL_CHANNEL_ANS_FIELD_NUMBER: _ClassVar[int]
    RX_TIMING_SETUP_REQ_FIELD_NUMBER: _ClassVar[int]
    TX_PARAM_SETUP_REQ_FIELD_NUMBER: _ClassVar[int]
    REKEY_IND_FIELD_NUMBER: _ClassVar[int]
    REKEY_CONF_FIELD_NUMBER: _ClassVar[int]
    ADR_PARAM_SETUP_REQ_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TIME_ANS_FIELD_NUMBER: _ClassVar[int]
    FORCE_REJOIN_REQ_FIELD_NUMBER: _ClassVar[int]
    REJOIN_PARAM_SETUP_REQ_FIELD_NUMBER: _ClassVar[int]
    REJOIN_PARAM_SETUP_ANS_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_INFO_REQ_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_CHANNEL_REQ_FIELD_NUMBER: _ClassVar[int]
    PING_SLOT_CHANNEL_ANS_FIELD_NUMBER: _ClassVar[int]
    BEACON_TIMING_ANS_FIELD_NUMBER: _ClassVar[int]
    BEACON_FREQ_REQ_FIELD_NUMBER: _ClassVar[int]
    BEACON_FREQ_ANS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODE_IND_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODE_CONF_FIELD_NUMBER: _ClassVar[int]
    RELAY_CONF_REQ_FIELD_NUMBER: _ClassVar[int]
    RELAY_CONF_ANS_FIELD_NUMBER: _ClassVar[int]
    RELAY_END_DEVICE_CONF_REQ_FIELD_NUMBER: _ClassVar[int]
    RELAY_END_DEVICE_CONF_ANS_FIELD_NUMBER: _ClassVar[int]
    RELAY_UPDATE_UPLINK_LIST_REQ_FIELD_NUMBER: _ClassVar[int]
    RELAY_UPDATE_UPLINK_LIST_ANS_FIELD_NUMBER: _ClassVar[int]
    RELAY_CTRL_UPLINK_LIST_REQ_FIELD_NUMBER: _ClassVar[int]
    RELAY_CTRL_UPLINK_LIST_ANS_FIELD_NUMBER: _ClassVar[int]
    RELAY_CONFIGURE_FWD_LIMIT_REQ_FIELD_NUMBER: _ClassVar[int]
    RELAY_CONFIGURE_FWD_LIMIT_ANS_FIELD_NUMBER: _ClassVar[int]
    RELAY_NOTIFY_NEW_END_DEVICE_REQ_FIELD_NUMBER: _ClassVar[int]
    cid: MACCommandIdentifier
    raw_payload: bytes
    reset_ind: MACCommand.ResetInd
    reset_conf: MACCommand.ResetConf
    link_check_ans: MACCommand.LinkCheckAns
    link_adr_req: MACCommand.LinkADRReq
    link_adr_ans: MACCommand.LinkADRAns
    duty_cycle_req: MACCommand.DutyCycleReq
    rx_param_setup_req: MACCommand.RxParamSetupReq
    rx_param_setup_ans: MACCommand.RxParamSetupAns
    dev_status_ans: MACCommand.DevStatusAns
    new_channel_req: MACCommand.NewChannelReq
    new_channel_ans: MACCommand.NewChannelAns
    dl_channel_req: MACCommand.DLChannelReq
    dl_channel_ans: MACCommand.DLChannelAns
    rx_timing_setup_req: MACCommand.RxTimingSetupReq
    tx_param_setup_req: MACCommand.TxParamSetupReq
    rekey_ind: MACCommand.RekeyInd
    rekey_conf: MACCommand.RekeyConf
    adr_param_setup_req: MACCommand.ADRParamSetupReq
    device_time_ans: MACCommand.DeviceTimeAns
    force_rejoin_req: MACCommand.ForceRejoinReq
    rejoin_param_setup_req: MACCommand.RejoinParamSetupReq
    rejoin_param_setup_ans: MACCommand.RejoinParamSetupAns
    ping_slot_info_req: MACCommand.PingSlotInfoReq
    ping_slot_channel_req: MACCommand.PingSlotChannelReq
    ping_slot_channel_ans: MACCommand.PingSlotChannelAns
    beacon_timing_ans: MACCommand.BeaconTimingAns
    beacon_freq_req: MACCommand.BeaconFreqReq
    beacon_freq_ans: MACCommand.BeaconFreqAns
    device_mode_ind: MACCommand.DeviceModeInd
    device_mode_conf: MACCommand.DeviceModeConf
    relay_conf_req: MACCommand.RelayConfReq
    relay_conf_ans: MACCommand.RelayConfAns
    relay_end_device_conf_req: MACCommand.RelayEndDeviceConfReq
    relay_end_device_conf_ans: MACCommand.RelayEndDeviceConfAns
    relay_update_uplink_list_req: MACCommand.RelayUpdateUplinkListReq
    relay_update_uplink_list_ans: MACCommand.RelayUpdateUplinkListAns
    relay_ctrl_uplink_list_req: MACCommand.RelayCtrlUplinkListReq
    relay_ctrl_uplink_list_ans: MACCommand.RelayCtrlUplinkListAns
    relay_configure_fwd_limit_req: MACCommand.RelayConfigureFwdLimitReq
    relay_configure_fwd_limit_ans: MACCommand.RelayConfigureFwdLimitAns
    relay_notify_new_end_device_req: MACCommand.RelayNotifyNewEndDeviceReq
    def __init__(self, cid: _Optional[_Union[MACCommandIdentifier, str]] = ..., raw_payload: _Optional[bytes] = ..., reset_ind: _Optional[_Union[MACCommand.ResetInd, _Mapping]] = ..., reset_conf: _Optional[_Union[MACCommand.ResetConf, _Mapping]] = ..., link_check_ans: _Optional[_Union[MACCommand.LinkCheckAns, _Mapping]] = ..., link_adr_req: _Optional[_Union[MACCommand.LinkADRReq, _Mapping]] = ..., link_adr_ans: _Optional[_Union[MACCommand.LinkADRAns, _Mapping]] = ..., duty_cycle_req: _Optional[_Union[MACCommand.DutyCycleReq, _Mapping]] = ..., rx_param_setup_req: _Optional[_Union[MACCommand.RxParamSetupReq, _Mapping]] = ..., rx_param_setup_ans: _Optional[_Union[MACCommand.RxParamSetupAns, _Mapping]] = ..., dev_status_ans: _Optional[_Union[MACCommand.DevStatusAns, _Mapping]] = ..., new_channel_req: _Optional[_Union[MACCommand.NewChannelReq, _Mapping]] = ..., new_channel_ans: _Optional[_Union[MACCommand.NewChannelAns, _Mapping]] = ..., dl_channel_req: _Optional[_Union[MACCommand.DLChannelReq, _Mapping]] = ..., dl_channel_ans: _Optional[_Union[MACCommand.DLChannelAns, _Mapping]] = ..., rx_timing_setup_req: _Optional[_Union[MACCommand.RxTimingSetupReq, _Mapping]] = ..., tx_param_setup_req: _Optional[_Union[MACCommand.TxParamSetupReq, _Mapping]] = ..., rekey_ind: _Optional[_Union[MACCommand.RekeyInd, _Mapping]] = ..., rekey_conf: _Optional[_Union[MACCommand.RekeyConf, _Mapping]] = ..., adr_param_setup_req: _Optional[_Union[MACCommand.ADRParamSetupReq, _Mapping]] = ..., device_time_ans: _Optional[_Union[MACCommand.DeviceTimeAns, _Mapping]] = ..., force_rejoin_req: _Optional[_Union[MACCommand.ForceRejoinReq, _Mapping]] = ..., rejoin_param_setup_req: _Optional[_Union[MACCommand.RejoinParamSetupReq, _Mapping]] = ..., rejoin_param_setup_ans: _Optional[_Union[MACCommand.RejoinParamSetupAns, _Mapping]] = ..., ping_slot_info_req: _Optional[_Union[MACCommand.PingSlotInfoReq, _Mapping]] = ..., ping_slot_channel_req: _Optional[_Union[MACCommand.PingSlotChannelReq, _Mapping]] = ..., ping_slot_channel_ans: _Optional[_Union[MACCommand.PingSlotChannelAns, _Mapping]] = ..., beacon_timing_ans: _Optional[_Union[MACCommand.BeaconTimingAns, _Mapping]] = ..., beacon_freq_req: _Optional[_Union[MACCommand.BeaconFreqReq, _Mapping]] = ..., beacon_freq_ans: _Optional[_Union[MACCommand.BeaconFreqAns, _Mapping]] = ..., device_mode_ind: _Optional[_Union[MACCommand.DeviceModeInd, _Mapping]] = ..., device_mode_conf: _Optional[_Union[MACCommand.DeviceModeConf, _Mapping]] = ..., relay_conf_req: _Optional[_Union[MACCommand.RelayConfReq, _Mapping]] = ..., relay_conf_ans: _Optional[_Union[MACCommand.RelayConfAns, _Mapping]] = ..., relay_end_device_conf_req: _Optional[_Union[MACCommand.RelayEndDeviceConfReq, _Mapping]] = ..., relay_end_device_conf_ans: _Optional[_Union[MACCommand.RelayEndDeviceConfAns, _Mapping]] = ..., relay_update_uplink_list_req: _Optional[_Union[MACCommand.RelayUpdateUplinkListReq, _Mapping]] = ..., relay_update_uplink_list_ans: _Optional[_Union[MACCommand.RelayUpdateUplinkListAns, _Mapping]] = ..., relay_ctrl_uplink_list_req: _Optional[_Union[MACCommand.RelayCtrlUplinkListReq, _Mapping]] = ..., relay_ctrl_uplink_list_ans: _Optional[_Union[MACCommand.RelayCtrlUplinkListAns, _Mapping]] = ..., relay_configure_fwd_limit_req: _Optional[_Union[MACCommand.RelayConfigureFwdLimitReq, _Mapping]] = ..., relay_configure_fwd_limit_ans: _Optional[_Union[MACCommand.RelayConfigureFwdLimitAns, _Mapping]] = ..., relay_notify_new_end_device_req: _Optional[_Union[MACCommand.RelayNotifyNewEndDeviceReq, _Mapping]] = ...) -> None: ...

class MACCommands(_message.Message):
    __slots__ = ("commands",)
    COMMANDS_FIELD_NUMBER: _ClassVar[int]
    commands: _containers.RepeatedCompositeFieldContainer[MACCommand]
    def __init__(self, commands: _Optional[_Iterable[_Union[MACCommand, _Mapping]]] = ...) -> None: ...

class FrequencyValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class ZeroableFrequencyValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class DataRateOffsetValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: DataRateOffset
    def __init__(self, value: _Optional[_Union[DataRateOffset, str]] = ...) -> None: ...

class DataRateIndexValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: DataRateIndex
    def __init__(self, value: _Optional[_Union[DataRateIndex, str]] = ...) -> None: ...

class PingSlotPeriodValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: PingSlotPeriod
    def __init__(self, value: _Optional[_Union[PingSlotPeriod, str]] = ...) -> None: ...

class AggregatedDutyCycleValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: AggregatedDutyCycle
    def __init__(self, value: _Optional[_Union[AggregatedDutyCycle, str]] = ...) -> None: ...

class RxDelayValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: RxDelay
    def __init__(self, value: _Optional[_Union[RxDelay, str]] = ...) -> None: ...

class ADRAckLimitExponentValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ADRAckLimitExponent
    def __init__(self, value: _Optional[_Union[ADRAckLimitExponent, str]] = ...) -> None: ...

class ADRAckDelayExponentValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: ADRAckDelayExponent
    def __init__(self, value: _Optional[_Union[ADRAckDelayExponent, str]] = ...) -> None: ...

class DeviceEIRPValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: DeviceEIRP
    def __init__(self, value: _Optional[_Union[DeviceEIRP, str]] = ...) -> None: ...

class RelayForwardUplinkReq(_message.Message):
    __slots__ = ("data_rate", "snr", "rssi", "wor_channel", "frequency", "raw_payload")
    DATA_RATE_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    WOR_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    data_rate: DataRate
    snr: int
    rssi: int
    wor_channel: RelayWORChannel
    frequency: int
    raw_payload: bytes
    def __init__(self, data_rate: _Optional[_Union[DataRate, _Mapping]] = ..., snr: _Optional[int] = ..., rssi: _Optional[int] = ..., wor_channel: _Optional[_Union[RelayWORChannel, str]] = ..., frequency: _Optional[int] = ..., raw_payload: _Optional[bytes] = ...) -> None: ...

class RelayForwardDownlinkReq(_message.Message):
    __slots__ = ("raw_payload",)
    RAW_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    raw_payload: bytes
    def __init__(self, raw_payload: _Optional[bytes] = ...) -> None: ...

class RelayUplinkToken(_message.Message):
    __slots__ = ("ids", "session_key_id", "full_f_cnt")
    IDS_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    FULL_F_CNT_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.EndDeviceIdentifiers
    session_key_id: bytes
    full_f_cnt: int
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., session_key_id: _Optional[bytes] = ..., full_f_cnt: _Optional[int] = ...) -> None: ...
