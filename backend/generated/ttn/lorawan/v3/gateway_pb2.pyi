from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from generated.ttn.lorawan.v3 import contact_info_pb2 as _contact_info_pb2
from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import metadata_pb2 as _metadata_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from ttn.lorawan.v3 import secrets_pb2 as _secrets_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ManagedGatewayNetworkInterfaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_UNSPECIFIED: _ClassVar[ManagedGatewayNetworkInterfaceType]
    MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_CELLULAR: _ClassVar[ManagedGatewayNetworkInterfaceType]
    MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_WIFI: _ClassVar[ManagedGatewayNetworkInterfaceType]
    MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_ETHERNET: _ClassVar[ManagedGatewayNetworkInterfaceType]

class ManagedGatewayNetworkInterfaceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_UNSPECIFIED: _ClassVar[ManagedGatewayNetworkInterfaceStatus]
    MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_DOWN: _ClassVar[ManagedGatewayNetworkInterfaceStatus]
    MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_UP: _ClassVar[ManagedGatewayNetworkInterfaceStatus]
    MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_FAILED: _ClassVar[ManagedGatewayNetworkInterfaceStatus]

class GatewayAntennaPlacement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLACEMENT_UNKNOWN: _ClassVar[GatewayAntennaPlacement]
    INDOOR: _ClassVar[GatewayAntennaPlacement]
    OUTDOOR: _ClassVar[GatewayAntennaPlacement]
MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_UNSPECIFIED: ManagedGatewayNetworkInterfaceType
MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_CELLULAR: ManagedGatewayNetworkInterfaceType
MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_WIFI: ManagedGatewayNetworkInterfaceType
MANAGED_GATEWAY_NETWORK_INTERFACE_TYPE_ETHERNET: ManagedGatewayNetworkInterfaceType
MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_UNSPECIFIED: ManagedGatewayNetworkInterfaceStatus
MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_DOWN: ManagedGatewayNetworkInterfaceStatus
MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_UP: ManagedGatewayNetworkInterfaceStatus
MANAGED_GATEWAY_NETWORK_INTERFACE_STATUS_FAILED: ManagedGatewayNetworkInterfaceStatus
PLACEMENT_UNKNOWN: GatewayAntennaPlacement
INDOOR: GatewayAntennaPlacement
OUTDOOR: GatewayAntennaPlacement

class GatewayBrand(_message.Message):
    __slots__ = ("id", "name", "url", "logos")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    LOGOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    url: str
    logos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., url: _Optional[str] = ..., logos: _Optional[_Iterable[str]] = ...) -> None: ...

class GatewayModel(_message.Message):
    __slots__ = ("brand_id", "id", "name")
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    brand_id: str
    id: str
    name: str
    def __init__(self, brand_id: _Optional[str] = ..., id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GatewayVersionIdentifiers(_message.Message):
    __slots__ = ("brand_id", "model_id", "hardware_version", "firmware_version", "runtime_version")
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_VERSION_FIELD_NUMBER: _ClassVar[int]
    brand_id: str
    model_id: str
    hardware_version: str
    firmware_version: str
    runtime_version: str
    def __init__(self, brand_id: _Optional[str] = ..., model_id: _Optional[str] = ..., hardware_version: _Optional[str] = ..., firmware_version: _Optional[str] = ..., runtime_version: _Optional[str] = ...) -> None: ...

class GatewayRadio(_message.Message):
    __slots__ = ("enable", "chip_type", "frequency", "rssi_offset", "tx_configuration")
    class TxConfiguration(_message.Message):
        __slots__ = ("min_frequency", "max_frequency", "notch_frequency")
        MIN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        MAX_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        NOTCH_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        min_frequency: int
        max_frequency: int
        notch_frequency: int
        def __init__(self, min_frequency: _Optional[int] = ..., max_frequency: _Optional[int] = ..., notch_frequency: _Optional[int] = ...) -> None: ...
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    CHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    RSSI_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TX_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    enable: bool
    chip_type: str
    frequency: int
    rssi_offset: float
    tx_configuration: GatewayRadio.TxConfiguration
    def __init__(self, enable: bool = ..., chip_type: _Optional[str] = ..., frequency: _Optional[int] = ..., rssi_offset: _Optional[float] = ..., tx_configuration: _Optional[_Union[GatewayRadio.TxConfiguration, _Mapping]] = ...) -> None: ...

class GatewayClaimAuthenticationCode(_message.Message):
    __slots__ = ("secret", "valid_from", "valid_to")
    SECRET_FIELD_NUMBER: _ClassVar[int]
    VALID_FROM_FIELD_NUMBER: _ClassVar[int]
    VALID_TO_FIELD_NUMBER: _ClassVar[int]
    secret: _secrets_pb2.Secret
    valid_from: _timestamp_pb2.Timestamp
    valid_to: _timestamp_pb2.Timestamp
    def __init__(self, secret: _Optional[_Union[_secrets_pb2.Secret, _Mapping]] = ..., valid_from: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., valid_to: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Gateway(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "deleted_at", "name", "description", "attributes", "contact_info", "administrative_contact", "technical_contact", "version_ids", "gateway_server_address", "auto_update", "update_channel", "frequency_plan_id", "frequency_plan_ids", "antennas", "status_public", "location_public", "schedule_downlink_late", "enforce_duty_cycle", "downlink_path_constraint", "schedule_anytime_delay", "update_location_from_status", "lbs_lns_secret", "claim_authentication_code", "target_cups_uri", "target_cups_key", "require_authenticated_connection", "lrfhss", "disable_packet_broker_forwarding")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class LRFHSS(_message.Message):
        __slots__ = ("supported",)
        SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        supported: bool
        def __init__(self, supported: bool = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATIVE_CONTACT_FIELD_NUMBER: _ClassVar[int]
    TECHNICAL_CONTACT_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PLAN_IDS_FIELD_NUMBER: _ClassVar[int]
    ANTENNAS_FIELD_NUMBER: _ClassVar[int]
    STATUS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    LOCATION_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_DOWNLINK_LATE_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_DUTY_CYCLE_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_PATH_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ANYTIME_DELAY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_LOCATION_FROM_STATUS_FIELD_NUMBER: _ClassVar[int]
    LBS_LNS_SECRET_FIELD_NUMBER: _ClassVar[int]
    CLAIM_AUTHENTICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_CUPS_URI_FIELD_NUMBER: _ClassVar[int]
    TARGET_CUPS_KEY_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_AUTHENTICATED_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    LRFHSS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_PACKET_BROKER_FORWARDING_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.GatewayIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    name: str
    description: str
    attributes: _containers.ScalarMap[str, str]
    contact_info: _containers.RepeatedCompositeFieldContainer[_contact_info_pb2.ContactInfo]
    administrative_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    technical_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    version_ids: GatewayVersionIdentifiers
    gateway_server_address: str
    auto_update: bool
    update_channel: str
    frequency_plan_id: str
    frequency_plan_ids: _containers.RepeatedScalarFieldContainer[str]
    antennas: _containers.RepeatedCompositeFieldContainer[GatewayAntenna]
    status_public: bool
    location_public: bool
    schedule_downlink_late: bool
    enforce_duty_cycle: bool
    downlink_path_constraint: _enums_pb2.DownlinkPathConstraint
    schedule_anytime_delay: _duration_pb2.Duration
    update_location_from_status: bool
    lbs_lns_secret: _secrets_pb2.Secret
    claim_authentication_code: GatewayClaimAuthenticationCode
    target_cups_uri: str
    target_cups_key: _secrets_pb2.Secret
    require_authenticated_connection: bool
    lrfhss: Gateway.LRFHSS
    disable_packet_broker_forwarding: bool
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., contact_info: _Optional[_Iterable[_Union[_contact_info_pb2.ContactInfo, _Mapping]]] = ..., administrative_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., technical_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., version_ids: _Optional[_Union[GatewayVersionIdentifiers, _Mapping]] = ..., gateway_server_address: _Optional[str] = ..., auto_update: bool = ..., update_channel: _Optional[str] = ..., frequency_plan_id: _Optional[str] = ..., frequency_plan_ids: _Optional[_Iterable[str]] = ..., antennas: _Optional[_Iterable[_Union[GatewayAntenna, _Mapping]]] = ..., status_public: bool = ..., location_public: bool = ..., schedule_downlink_late: bool = ..., enforce_duty_cycle: bool = ..., downlink_path_constraint: _Optional[_Union[_enums_pb2.DownlinkPathConstraint, str]] = ..., schedule_anytime_delay: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., update_location_from_status: bool = ..., lbs_lns_secret: _Optional[_Union[_secrets_pb2.Secret, _Mapping]] = ..., claim_authentication_code: _Optional[_Union[GatewayClaimAuthenticationCode, _Mapping]] = ..., target_cups_uri: _Optional[str] = ..., target_cups_key: _Optional[_Union[_secrets_pb2.Secret, _Mapping]] = ..., require_authenticated_connection: bool = ..., lrfhss: _Optional[_Union[Gateway.LRFHSS, _Mapping]] = ..., disable_packet_broker_forwarding: bool = ...) -> None: ...

class Gateways(_message.Message):
    __slots__ = ("gateways",)
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    gateways: _containers.RepeatedCompositeFieldContainer[Gateway]
    def __init__(self, gateways: _Optional[_Iterable[_Union[Gateway, _Mapping]]] = ...) -> None: ...

class ManagedGateway(_message.Message):
    __slots__ = ("ids", "version_ids", "cellular_imei", "cellular_imsi", "wifi_mac_address", "ethernet_mac_address", "wifi_profile_id", "ethernet_profile_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_IMEI_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_IMSI_FIELD_NUMBER: _ClassVar[int]
    WIFI_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_MAC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    WIFI_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.GatewayIdentifiers
    version_ids: GatewayVersionIdentifiers
    cellular_imei: str
    cellular_imsi: str
    wifi_mac_address: bytes
    ethernet_mac_address: bytes
    wifi_profile_id: str
    ethernet_profile_id: str
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., version_ids: _Optional[_Union[GatewayVersionIdentifiers, _Mapping]] = ..., cellular_imei: _Optional[str] = ..., cellular_imsi: _Optional[str] = ..., wifi_mac_address: _Optional[bytes] = ..., ethernet_mac_address: _Optional[bytes] = ..., wifi_profile_id: _Optional[str] = ..., ethernet_profile_id: _Optional[str] = ...) -> None: ...

class ManagedGatewayWiFiAccessPoint(_message.Message):
    __slots__ = ("ssid", "bssid", "channel", "authentication_mode", "rssi")
    SSID_FIELD_NUMBER: _ClassVar[int]
    BSSID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    ssid: str
    bssid: bytes
    channel: int
    authentication_mode: str
    rssi: float
    def __init__(self, ssid: _Optional[str] = ..., bssid: _Optional[bytes] = ..., channel: _Optional[int] = ..., authentication_mode: _Optional[str] = ..., rssi: _Optional[float] = ...) -> None: ...

class ManagedGatewayWiFiAccessPoints(_message.Message):
    __slots__ = ("access_points",)
    ACCESS_POINTS_FIELD_NUMBER: _ClassVar[int]
    access_points: _containers.RepeatedCompositeFieldContainer[ManagedGatewayWiFiAccessPoint]
    def __init__(self, access_points: _Optional[_Iterable[_Union[ManagedGatewayWiFiAccessPoint, _Mapping]]] = ...) -> None: ...

class ManagedGatewayNetworkInterfaceAddresses(_message.Message):
    __slots__ = ("ip_addresses", "subnet_mask", "gateway", "dns_servers")
    IP_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    SUBNET_MASK_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    DNS_SERVERS_FIELD_NUMBER: _ClassVar[int]
    ip_addresses: _containers.RepeatedScalarFieldContainer[str]
    subnet_mask: str
    gateway: str
    dns_servers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ip_addresses: _Optional[_Iterable[str]] = ..., subnet_mask: _Optional[str] = ..., gateway: _Optional[str] = ..., dns_servers: _Optional[_Iterable[str]] = ...) -> None: ...

class ManagedGatewaySystemStatus(_message.Message):
    __slots__ = ("cpu_temperature",)
    CPU_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    cpu_temperature: _wrappers_pb2.FloatValue
    def __init__(self, cpu_temperature: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class ManagedGatewayControllerConnection(_message.Message):
    __slots__ = ("network_interface_type",)
    NETWORK_INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    network_interface_type: ManagedGatewayNetworkInterfaceType
    def __init__(self, network_interface_type: _Optional[_Union[ManagedGatewayNetworkInterfaceType, str]] = ...) -> None: ...

class ManagedGatewayGatewayServerConnection(_message.Message):
    __slots__ = ("network_interface_type", "address")
    NETWORK_INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    network_interface_type: ManagedGatewayNetworkInterfaceType
    address: str
    def __init__(self, network_interface_type: _Optional[_Union[ManagedGatewayNetworkInterfaceType, str]] = ..., address: _Optional[str] = ...) -> None: ...

class ManagedGatewayNetworkInterfaceInfo(_message.Message):
    __slots__ = ("status", "dhcp_enabled", "addresses")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DHCP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    status: ManagedGatewayNetworkInterfaceStatus
    dhcp_enabled: bool
    addresses: ManagedGatewayNetworkInterfaceAddresses
    def __init__(self, status: _Optional[_Union[ManagedGatewayNetworkInterfaceStatus, str]] = ..., dhcp_enabled: bool = ..., addresses: _Optional[_Union[ManagedGatewayNetworkInterfaceAddresses, _Mapping]] = ...) -> None: ...

class ManagedGatewayCellularBackhaul(_message.Message):
    __slots__ = ("network_interface", "operator", "rssi")
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    network_interface: ManagedGatewayNetworkInterfaceInfo
    operator: str
    rssi: _wrappers_pb2.FloatValue
    def __init__(self, network_interface: _Optional[_Union[ManagedGatewayNetworkInterfaceInfo, _Mapping]] = ..., operator: _Optional[str] = ..., rssi: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class ManagedGatewayWiFiBackhaul(_message.Message):
    __slots__ = ("network_interface", "ssid", "bssid", "channel", "authentication_mode", "rssi")
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    BSSID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATION_MODE_FIELD_NUMBER: _ClassVar[int]
    RSSI_FIELD_NUMBER: _ClassVar[int]
    network_interface: ManagedGatewayNetworkInterfaceInfo
    ssid: str
    bssid: bytes
    channel: int
    authentication_mode: str
    rssi: _wrappers_pb2.FloatValue
    def __init__(self, network_interface: _Optional[_Union[ManagedGatewayNetworkInterfaceInfo, _Mapping]] = ..., ssid: _Optional[str] = ..., bssid: _Optional[bytes] = ..., channel: _Optional[int] = ..., authentication_mode: _Optional[str] = ..., rssi: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class ManagedGatewayEthernetBackhaul(_message.Message):
    __slots__ = ("network_interface",)
    NETWORK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    network_interface: ManagedGatewayNetworkInterfaceInfo
    def __init__(self, network_interface: _Optional[_Union[ManagedGatewayNetworkInterfaceInfo, _Mapping]] = ...) -> None: ...

class ManagedGatewayEventData(_message.Message):
    __slots__ = ("entity", "location", "system_status", "controller_connection", "gateway_server_connection", "cellular_backhaul", "wifi_backhaul", "ethernet_backhaul")
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONTROLLER_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_SERVER_CONNECTION_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_BACKHAUL_FIELD_NUMBER: _ClassVar[int]
    WIFI_BACKHAUL_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_BACKHAUL_FIELD_NUMBER: _ClassVar[int]
    entity: ManagedGateway
    location: _metadata_pb2.Location
    system_status: ManagedGatewaySystemStatus
    controller_connection: ManagedGatewayControllerConnection
    gateway_server_connection: ManagedGatewayGatewayServerConnection
    cellular_backhaul: ManagedGatewayCellularBackhaul
    wifi_backhaul: ManagedGatewayWiFiBackhaul
    ethernet_backhaul: ManagedGatewayEthernetBackhaul
    def __init__(self, entity: _Optional[_Union[ManagedGateway, _Mapping]] = ..., location: _Optional[_Union[_metadata_pb2.Location, _Mapping]] = ..., system_status: _Optional[_Union[ManagedGatewaySystemStatus, _Mapping]] = ..., controller_connection: _Optional[_Union[ManagedGatewayControllerConnection, _Mapping]] = ..., gateway_server_connection: _Optional[_Union[ManagedGatewayGatewayServerConnection, _Mapping]] = ..., cellular_backhaul: _Optional[_Union[ManagedGatewayCellularBackhaul, _Mapping]] = ..., wifi_backhaul: _Optional[_Union[ManagedGatewayWiFiBackhaul, _Mapping]] = ..., ethernet_backhaul: _Optional[_Union[ManagedGatewayEthernetBackhaul, _Mapping]] = ...) -> None: ...

class ManagedGatewayWiFiProfile(_message.Message):
    __slots__ = ("profile_id", "profile_name", "shared", "ssid", "password", "network_interface_addresses")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    SSID_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    profile_name: str
    shared: bool
    ssid: str
    password: str
    network_interface_addresses: ManagedGatewayNetworkInterfaceAddresses
    def __init__(self, profile_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., shared: bool = ..., ssid: _Optional[str] = ..., password: _Optional[str] = ..., network_interface_addresses: _Optional[_Union[ManagedGatewayNetworkInterfaceAddresses, _Mapping]] = ...) -> None: ...

class ManagedGatewayWiFiProfiles(_message.Message):
    __slots__ = ("profiles",)
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    profiles: _containers.RepeatedCompositeFieldContainer[ManagedGatewayWiFiProfile]
    def __init__(self, profiles: _Optional[_Iterable[_Union[ManagedGatewayWiFiProfile, _Mapping]]] = ...) -> None: ...

class ManagedGatewayEthernetProfile(_message.Message):
    __slots__ = ("profile_id", "profile_name", "shared", "network_interface_addresses")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHARED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    profile_name: str
    shared: bool
    network_interface_addresses: ManagedGatewayNetworkInterfaceAddresses
    def __init__(self, profile_id: _Optional[str] = ..., profile_name: _Optional[str] = ..., shared: bool = ..., network_interface_addresses: _Optional[_Union[ManagedGatewayNetworkInterfaceAddresses, _Mapping]] = ...) -> None: ...

class ManagedGatewayEthernetProfiles(_message.Message):
    __slots__ = ("profiles",)
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    profiles: _containers.RepeatedCompositeFieldContainer[ManagedGatewayEthernetProfile]
    def __init__(self, profiles: _Optional[_Iterable[_Union[ManagedGatewayEthernetProfile, _Mapping]]] = ...) -> None: ...

class GetGatewayRequest(_message.Message):
    __slots__ = ("gateway_ids", "field_mask")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetGatewayIdentifiersForEUIRequest(_message.Message):
    __slots__ = ("eui",)
    EUI_FIELD_NUMBER: _ClassVar[int]
    eui: bytes
    def __init__(self, eui: _Optional[bytes] = ...) -> None: ...

class ListGatewaysRequest(_message.Message):
    __slots__ = ("collaborator", "field_mask", "order", "limit", "page", "deleted", "filters")
    class Filter(_message.Message):
        __slots__ = ("updated_since",)
        UPDATED_SINCE_FIELD_NUMBER: _ClassVar[int]
        updated_since: _timestamp_pb2.Timestamp
        def __init__(self, updated_since: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    filters: _containers.RepeatedCompositeFieldContainer[ListGatewaysRequest.Filter]
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ..., filters: _Optional[_Iterable[_Union[ListGatewaysRequest.Filter, _Mapping]]] = ...) -> None: ...

class CreateGatewayRequest(_message.Message):
    __slots__ = ("gateway", "collaborator")
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class UpdateGatewayRequest(_message.Message):
    __slots__ = ("gateway", "field_mask")
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway: Gateway
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway: _Optional[_Union[Gateway, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListGatewayAPIKeysRequest(_message.Message):
    __slots__ = ("gateway_ids", "order", "limit", "page")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    order: str
    limit: int
    page: int
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetGatewayAPIKeyRequest(_message.Message):
    __slots__ = ("gateway_ids", "key_id")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    key_id: str
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class CreateGatewayAPIKeyRequest(_message.Message):
    __slots__ = ("gateway_ids", "name", "rights", "expires_at")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    name: str
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., name: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateGatewayAPIKeyRequest(_message.Message):
    __slots__ = ("gateway_ids", "api_key", "field_mask")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    api_key: _rights_pb2.APIKey
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., api_key: _Optional[_Union[_rights_pb2.APIKey, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteGatewayAPIKeyRequest(_message.Message):
    __slots__ = ("gateway_ids", "key_id")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    key_id: str
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class ListGatewayCollaboratorsRequest(_message.Message):
    __slots__ = ("gateway_ids", "limit", "page", "order")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    limit: int
    page: int
    order: str
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., order: _Optional[str] = ...) -> None: ...

class GetGatewayCollaboratorRequest(_message.Message):
    __slots__ = ("gateway_ids", "collaborator")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class SetGatewayCollaboratorRequest(_message.Message):
    __slots__ = ("gateway_ids", "collaborator")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    collaborator: _rights_pb2.Collaborator
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_rights_pb2.Collaborator, _Mapping]] = ...) -> None: ...

class DeleteGatewayCollaboratorRequest(_message.Message):
    __slots__ = ("gateway_ids", "collaborator_ids")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_IDS_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    collaborator_ids: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., collaborator_ids: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class GatewayAntenna(_message.Message):
    __slots__ = ("gain", "location", "attributes", "placement")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    GAIN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    gain: float
    location: _metadata_pb2.Location
    attributes: _containers.ScalarMap[str, str]
    placement: GatewayAntennaPlacement
    def __init__(self, gain: _Optional[float] = ..., location: _Optional[_Union[_metadata_pb2.Location, _Mapping]] = ..., attributes: _Optional[_Mapping[str, str]] = ..., placement: _Optional[_Union[GatewayAntennaPlacement, str]] = ...) -> None: ...

class GatewayStatus(_message.Message):
    __slots__ = ("time", "boot_time", "versions", "antenna_locations", "ip", "metrics", "advanced")
    class VersionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    TIME_FIELD_NUMBER: _ClassVar[int]
    BOOT_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    boot_time: _timestamp_pb2.Timestamp
    versions: _containers.ScalarMap[str, str]
    antenna_locations: _containers.RepeatedCompositeFieldContainer[_metadata_pb2.Location]
    ip: _containers.RepeatedScalarFieldContainer[str]
    metrics: _containers.ScalarMap[str, float]
    advanced: _struct_pb2.Struct
    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., boot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., versions: _Optional[_Mapping[str, str]] = ..., antenna_locations: _Optional[_Iterable[_Union[_metadata_pb2.Location, _Mapping]]] = ..., ip: _Optional[_Iterable[str]] = ..., metrics: _Optional[_Mapping[str, float]] = ..., advanced: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class GatewayRemoteAddress(_message.Message):
    __slots__ = ("ip",)
    IP_FIELD_NUMBER: _ClassVar[int]
    ip: str
    def __init__(self, ip: _Optional[str] = ...) -> None: ...

class GatewayConnectionStats(_message.Message):
    __slots__ = ("connected_at", "disconnected_at", "protocol", "last_status_received_at", "last_status", "last_uplink_received_at", "uplink_count", "last_downlink_received_at", "downlink_count", "last_tx_acknowledgment_received_at", "tx_acknowledgment_count", "round_trip_times", "sub_bands", "gateway_remote_address")
    class RoundTripTimes(_message.Message):
        __slots__ = ("min", "max", "median", "count")
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        MEDIAN_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        min: _duration_pb2.Duration
        max: _duration_pb2.Duration
        median: _duration_pb2.Duration
        count: int
        def __init__(self, min: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., max: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., median: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...
    class SubBand(_message.Message):
        __slots__ = ("min_frequency", "max_frequency", "downlink_utilization_limit", "downlink_utilization")
        MIN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        MAX_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        DOWNLINK_UTILIZATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
        DOWNLINK_UTILIZATION_FIELD_NUMBER: _ClassVar[int]
        min_frequency: int
        max_frequency: int
        downlink_utilization_limit: float
        downlink_utilization: float
        def __init__(self, min_frequency: _Optional[int] = ..., max_frequency: _Optional[int] = ..., downlink_utilization_limit: _Optional[float] = ..., downlink_utilization: _Optional[float] = ...) -> None: ...
    CONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    DISCONNECTED_AT_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    LAST_STATUS_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPLINK_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    UPLINK_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_DOWNLINK_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_TX_ACKNOWLEDGMENT_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    TX_ACKNOWLEDGMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ROUND_TRIP_TIMES_FIELD_NUMBER: _ClassVar[int]
    SUB_BANDS_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_REMOTE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    connected_at: _timestamp_pb2.Timestamp
    disconnected_at: _timestamp_pb2.Timestamp
    protocol: str
    last_status_received_at: _timestamp_pb2.Timestamp
    last_status: GatewayStatus
    last_uplink_received_at: _timestamp_pb2.Timestamp
    uplink_count: int
    last_downlink_received_at: _timestamp_pb2.Timestamp
    downlink_count: int
    last_tx_acknowledgment_received_at: _timestamp_pb2.Timestamp
    tx_acknowledgment_count: int
    round_trip_times: GatewayConnectionStats.RoundTripTimes
    sub_bands: _containers.RepeatedCompositeFieldContainer[GatewayConnectionStats.SubBand]
    gateway_remote_address: GatewayRemoteAddress
    def __init__(self, connected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., disconnected_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., protocol: _Optional[str] = ..., last_status_received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_status: _Optional[_Union[GatewayStatus, _Mapping]] = ..., last_uplink_received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., uplink_count: _Optional[int] = ..., last_downlink_received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., downlink_count: _Optional[int] = ..., last_tx_acknowledgment_received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., tx_acknowledgment_count: _Optional[int] = ..., round_trip_times: _Optional[_Union[GatewayConnectionStats.RoundTripTimes, _Mapping]] = ..., sub_bands: _Optional[_Iterable[_Union[GatewayConnectionStats.SubBand, _Mapping]]] = ..., gateway_remote_address: _Optional[_Union[GatewayRemoteAddress, _Mapping]] = ...) -> None: ...
