from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimulateMetadataParams(_message.Message):
    __slots__ = ("rssi", "snr", "timestamp", "time", "lorawan_version", "lorawan_phy_version", "band_id", "frequency", "channel_index", "bandwidth", "spreading_factor", "data_rate_index")
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_VERSION_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_PHY_VERSION_FIELD_NUMBER: _ClassVar[int]
    BAND_ID_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    SPREADING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DATA_RATE_INDEX_FIELD_NUMBER: _ClassVar[int]
    rssi: float
    snr: float
    timestamp: int
    time: _timestamp_pb2.Timestamp
    lorawan_version: _lorawan_pb2.MACVersion
    lorawan_phy_version: _lorawan_pb2.PHYVersion
    band_id: str
    frequency: int
    channel_index: int
    bandwidth: int
    spreading_factor: int
    data_rate_index: int
    def __init__(self, rssi: _Optional[float] = ..., snr: _Optional[float] = ..., timestamp: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lorawan_version: _Optional[_Union[_lorawan_pb2.MACVersion, str]] = ..., lorawan_phy_version: _Optional[_Union[_lorawan_pb2.PHYVersion, str]] = ..., band_id: _Optional[str] = ..., frequency: _Optional[int] = ..., channel_index: _Optional[int] = ..., bandwidth: _Optional[int] = ..., spreading_factor: _Optional[int] = ..., data_rate_index: _Optional[int] = ...) -> None: ...

class SimulateJoinRequestParams(_message.Message):
    __slots__ = ("join_eui", "dev_eui", "dev_nonce", "app_key", "nwk_key")
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_NONCE_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    NWK_KEY_FIELD_NUMBER: _ClassVar[int]
    join_eui: bytes
    dev_eui: bytes
    dev_nonce: bytes
    app_key: bytes
    nwk_key: bytes
    def __init__(self, join_eui: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ..., dev_nonce: _Optional[bytes] = ..., app_key: _Optional[bytes] = ..., nwk_key: _Optional[bytes] = ...) -> None: ...

class SimulateDataUplinkParams(_message.Message):
    __slots__ = ("dev_addr", "f_nwk_s_int_key", "s_nwk_s_int_key", "nwk_s_enc_key", "app_s_key", "adr", "adr_ack_req", "confirmed", "ack", "f_cnt", "f_port", "frm_payload", "conf_f_cnt", "tx_dr_idx", "tx_ch_idx", "f_opts")
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    F_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    S_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    NWK_S_ENC_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    ADR_FIELD_NUMBER: _ClassVar[int]
    ADR_ACK_REQ_FIELD_NUMBER: _ClassVar[int]
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    ACK_FIELD_NUMBER: _ClassVar[int]
    F_CNT_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CONF_F_CNT_FIELD_NUMBER: _ClassVar[int]
    TX_DR_IDX_FIELD_NUMBER: _ClassVar[int]
    TX_CH_IDX_FIELD_NUMBER: _ClassVar[int]
    F_OPTS_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    f_nwk_s_int_key: bytes
    s_nwk_s_int_key: bytes
    nwk_s_enc_key: bytes
    app_s_key: bytes
    adr: bool
    adr_ack_req: bool
    confirmed: bool
    ack: bool
    f_cnt: int
    f_port: int
    frm_payload: bytes
    conf_f_cnt: int
    tx_dr_idx: int
    tx_ch_idx: int
    f_opts: bytes
    def __init__(self, dev_addr: _Optional[bytes] = ..., f_nwk_s_int_key: _Optional[bytes] = ..., s_nwk_s_int_key: _Optional[bytes] = ..., nwk_s_enc_key: _Optional[bytes] = ..., app_s_key: _Optional[bytes] = ..., adr: bool = ..., adr_ack_req: bool = ..., confirmed: bool = ..., ack: bool = ..., f_cnt: _Optional[int] = ..., f_port: _Optional[int] = ..., frm_payload: _Optional[bytes] = ..., conf_f_cnt: _Optional[int] = ..., tx_dr_idx: _Optional[int] = ..., tx_ch_idx: _Optional[int] = ..., f_opts: _Optional[bytes] = ...) -> None: ...
