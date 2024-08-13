from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOURCE_UNKNOWN: _ClassVar[LocationSource]
    SOURCE_GPS: _ClassVar[LocationSource]
    SOURCE_REGISTRY: _ClassVar[LocationSource]
    SOURCE_IP_GEOLOCATION: _ClassVar[LocationSource]
    SOURCE_WIFI_RSSI_GEOLOCATION: _ClassVar[LocationSource]
    SOURCE_BT_RSSI_GEOLOCATION: _ClassVar[LocationSource]
    SOURCE_LORA_RSSI_GEOLOCATION: _ClassVar[LocationSource]
    SOURCE_LORA_TDOA_GEOLOCATION: _ClassVar[LocationSource]
    SOURCE_COMBINED_GEOLOCATION: _ClassVar[LocationSource]
SOURCE_UNKNOWN: LocationSource
SOURCE_GPS: LocationSource
SOURCE_REGISTRY: LocationSource
SOURCE_IP_GEOLOCATION: LocationSource
SOURCE_WIFI_RSSI_GEOLOCATION: LocationSource
SOURCE_BT_RSSI_GEOLOCATION: LocationSource
SOURCE_LORA_RSSI_GEOLOCATION: LocationSource
SOURCE_LORA_TDOA_GEOLOCATION: LocationSource
SOURCE_COMBINED_GEOLOCATION: LocationSource

class RxMetadata(_message.Message):
    __slots__ = ("gateway_ids", "packet_broker", "relay", "antenna_index", "time", "timestamp", "fine_timestamp", "encrypted_fine_timestamp", "encrypted_fine_timestamp_key_id", "rssi", "signal_rssi", "channel_rssi", "rssi_standard_deviation", "snr", "frequency_offset", "location", "downlink_path_constraint", "uplink_token", "channel_index", "hopping_width", "frequency_drift", "gps_time", "received_at", "advanced")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    PACKET_BROKER_FIELD_NUMBER: _ClassVar[int]
    RELAY_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_INDEX_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FINE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FINE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_FINE_TIMESTAMP_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_RSSI_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_RSSI_FIELD_NUMBER: _ClassVar[int]
    RSSI_STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    SNR_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_PATH_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    UPLINK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_INDEX_FIELD_NUMBER: _ClassVar[int]
    HOPPING_WIDTH_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_DRIFT_FIELD_NUMBER: _ClassVar[int]
    GPS_TIME_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    packet_broker: PacketBrokerMetadata
    relay: RelayMetadata
    antenna_index: int
    time: _timestamp_pb2.Timestamp
    timestamp: int
    fine_timestamp: int
    encrypted_fine_timestamp: bytes
    encrypted_fine_timestamp_key_id: str
    rssi: float
    signal_rssi: _wrappers_pb2.FloatValue
    channel_rssi: float
    rssi_standard_deviation: float
    snr: float
    frequency_offset: int
    location: Location
    downlink_path_constraint: _enums_pb2.DownlinkPathConstraint
    uplink_token: bytes
    channel_index: int
    hopping_width: int
    frequency_drift: int
    gps_time: _timestamp_pb2.Timestamp
    received_at: _timestamp_pb2.Timestamp
    advanced: _struct_pb2.Struct
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., packet_broker: _Optional[_Union[PacketBrokerMetadata, _Mapping]] = ..., relay: _Optional[_Union[RelayMetadata, _Mapping]] = ..., antenna_index: _Optional[int] = ..., time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., timestamp: _Optional[int] = ..., fine_timestamp: _Optional[int] = ..., encrypted_fine_timestamp: _Optional[bytes] = ..., encrypted_fine_timestamp_key_id: _Optional[str] = ..., rssi: _Optional[float] = ..., signal_rssi: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., channel_rssi: _Optional[float] = ..., rssi_standard_deviation: _Optional[float] = ..., snr: _Optional[float] = ..., frequency_offset: _Optional[int] = ..., location: _Optional[_Union[Location, _Mapping]] = ..., downlink_path_constraint: _Optional[_Union[_enums_pb2.DownlinkPathConstraint, str]] = ..., uplink_token: _Optional[bytes] = ..., channel_index: _Optional[int] = ..., hopping_width: _Optional[int] = ..., frequency_drift: _Optional[int] = ..., gps_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., advanced: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Location(_message.Message):
    __slots__ = ("latitude", "longitude", "altitude", "accuracy", "source")
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    ALTITUDE_FIELD_NUMBER: _ClassVar[int]
    ACCURACY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    altitude: int
    accuracy: int
    source: LocationSource
    def __init__(self, latitude: _Optional[float] = ..., longitude: _Optional[float] = ..., altitude: _Optional[int] = ..., accuracy: _Optional[int] = ..., source: _Optional[_Union[LocationSource, str]] = ...) -> None: ...

class PacketBrokerMetadata(_message.Message):
    __slots__ = ("message_id", "forwarder_net_id", "forwarder_tenant_id", "forwarder_cluster_id", "forwarder_gateway_eui", "forwarder_gateway_id", "home_network_net_id", "home_network_tenant_id", "home_network_cluster_id", "hops")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_NET_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_GATEWAY_EUI_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    HOME_NETWORK_NET_ID_FIELD_NUMBER: _ClassVar[int]
    HOME_NETWORK_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    HOME_NETWORK_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    HOPS_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    forwarder_net_id: bytes
    forwarder_tenant_id: str
    forwarder_cluster_id: str
    forwarder_gateway_eui: bytes
    forwarder_gateway_id: _wrappers_pb2.StringValue
    home_network_net_id: bytes
    home_network_tenant_id: str
    home_network_cluster_id: str
    hops: _containers.RepeatedCompositeFieldContainer[PacketBrokerRouteHop]
    def __init__(self, message_id: _Optional[str] = ..., forwarder_net_id: _Optional[bytes] = ..., forwarder_tenant_id: _Optional[str] = ..., forwarder_cluster_id: _Optional[str] = ..., forwarder_gateway_eui: _Optional[bytes] = ..., forwarder_gateway_id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., home_network_net_id: _Optional[bytes] = ..., home_network_tenant_id: _Optional[str] = ..., home_network_cluster_id: _Optional[str] = ..., hops: _Optional[_Iterable[_Union[PacketBrokerRouteHop, _Mapping]]] = ...) -> None: ...

class PacketBrokerRouteHop(_message.Message):
    __slots__ = ("received_at", "sender_name", "sender_address", "receiver_name", "receiver_agent")
    RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    SENDER_NAME_FIELD_NUMBER: _ClassVar[int]
    SENDER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_NAME_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_AGENT_FIELD_NUMBER: _ClassVar[int]
    received_at: _timestamp_pb2.Timestamp
    sender_name: str
    sender_address: str
    receiver_name: str
    receiver_agent: str
    def __init__(self, received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sender_name: _Optional[str] = ..., sender_address: _Optional[str] = ..., receiver_name: _Optional[str] = ..., receiver_agent: _Optional[str] = ...) -> None: ...

class RelayMetadata(_message.Message):
    __slots__ = ("device_id", "wor_channel")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    WOR_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    wor_channel: _lorawan_pb2.RelayWORChannel
    def __init__(self, device_id: _Optional[str] = ..., wor_channel: _Optional[_Union[_lorawan_pb2.RelayWORChannel, str]] = ...) -> None: ...
