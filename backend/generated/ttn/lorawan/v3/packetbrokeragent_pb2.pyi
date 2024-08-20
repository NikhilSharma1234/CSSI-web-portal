from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1_1
from generated.ttn.lorawan.v3 import contact_info_pb2 as _contact_info_pb2
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from ttn.lorawan.v3 import gateway_pb2 as _gateway_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import messages_pb2 as _messages_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PacketBrokerGateway(_message.Message):
    __slots__ = ("ids", "contact_info", "administrative_contact", "technical_contact", "antennas", "status_public", "location_public", "frequency_plan_ids", "update_location_from_status", "online", "rx_rate", "tx_rate")
    class GatewayIdentifiers(_message.Message):
        __slots__ = ("gateway_id", "eui")
        GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
        EUI_FIELD_NUMBER: _ClassVar[int]
        gateway_id: str
        eui: bytes
        def __init__(self, gateway_id: _Optional[str] = ..., eui: _Optional[bytes] = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATIVE_CONTACT_FIELD_NUMBER: _ClassVar[int]
    TECHNICAL_CONTACT_FIELD_NUMBER: _ClassVar[int]
    ANTENNAS_FIELD_NUMBER: _ClassVar[int]
    STATUS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    LOCATION_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PLAN_IDS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_LOCATION_FROM_STATUS_FIELD_NUMBER: _ClassVar[int]
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    RX_RATE_FIELD_NUMBER: _ClassVar[int]
    TX_RATE_FIELD_NUMBER: _ClassVar[int]
    ids: PacketBrokerGateway.GatewayIdentifiers
    contact_info: _containers.RepeatedCompositeFieldContainer[_contact_info_pb2.ContactInfo]
    administrative_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    technical_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    antennas: _containers.RepeatedCompositeFieldContainer[_gateway_pb2.GatewayAntenna]
    status_public: bool
    location_public: bool
    frequency_plan_ids: _containers.RepeatedScalarFieldContainer[str]
    update_location_from_status: bool
    online: bool
    rx_rate: _wrappers_pb2.FloatValue
    tx_rate: _wrappers_pb2.FloatValue
    def __init__(self, ids: _Optional[_Union[PacketBrokerGateway.GatewayIdentifiers, _Mapping]] = ..., contact_info: _Optional[_Iterable[_Union[_contact_info_pb2.ContactInfo, _Mapping]]] = ..., administrative_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., technical_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., antennas: _Optional[_Iterable[_Union[_gateway_pb2.GatewayAntenna, _Mapping]]] = ..., status_public: bool = ..., location_public: bool = ..., frequency_plan_ids: _Optional[_Iterable[str]] = ..., update_location_from_status: bool = ..., online: bool = ..., rx_rate: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., tx_rate: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class UpdatePacketBrokerGatewayRequest(_message.Message):
    __slots__ = ("gateway", "field_mask")
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway: PacketBrokerGateway
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway: _Optional[_Union[PacketBrokerGateway, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePacketBrokerGatewayResponse(_message.Message):
    __slots__ = ("online_ttl",)
    ONLINE_TTL_FIELD_NUMBER: _ClassVar[int]
    online_ttl: _duration_pb2.Duration
    def __init__(self, online_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PacketBrokerNetworkIdentifier(_message.Message):
    __slots__ = ("net_id", "tenant_id")
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    net_id: int
    tenant_id: str
    def __init__(self, net_id: _Optional[int] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class PacketBrokerDevAddrBlock(_message.Message):
    __slots__ = ("dev_addr_prefix", "home_network_cluster_id")
    DEV_ADDR_PREFIX_FIELD_NUMBER: _ClassVar[int]
    HOME_NETWORK_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    dev_addr_prefix: _end_device_pb2.DevAddrPrefix
    home_network_cluster_id: str
    def __init__(self, dev_addr_prefix: _Optional[_Union[_end_device_pb2.DevAddrPrefix, _Mapping]] = ..., home_network_cluster_id: _Optional[str] = ...) -> None: ...

class PacketBrokerNetwork(_message.Message):
    __slots__ = ("id", "name", "dev_addr_blocks", "contact_info", "administrative_contact", "technical_contact", "listed")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_BLOCKS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    ADMINISTRATIVE_CONTACT_FIELD_NUMBER: _ClassVar[int]
    TECHNICAL_CONTACT_FIELD_NUMBER: _ClassVar[int]
    LISTED_FIELD_NUMBER: _ClassVar[int]
    id: PacketBrokerNetworkIdentifier
    name: str
    dev_addr_blocks: _containers.RepeatedCompositeFieldContainer[PacketBrokerDevAddrBlock]
    contact_info: _containers.RepeatedCompositeFieldContainer[_contact_info_pb2.ContactInfo]
    administrative_contact: _contact_info_pb2.ContactInfo
    technical_contact: _contact_info_pb2.ContactInfo
    listed: bool
    def __init__(self, id: _Optional[_Union[PacketBrokerNetworkIdentifier, _Mapping]] = ..., name: _Optional[str] = ..., dev_addr_blocks: _Optional[_Iterable[_Union[PacketBrokerDevAddrBlock, _Mapping]]] = ..., contact_info: _Optional[_Iterable[_Union[_contact_info_pb2.ContactInfo, _Mapping]]] = ..., administrative_contact: _Optional[_Union[_contact_info_pb2.ContactInfo, _Mapping]] = ..., technical_contact: _Optional[_Union[_contact_info_pb2.ContactInfo, _Mapping]] = ..., listed: bool = ...) -> None: ...

class PacketBrokerNetworks(_message.Message):
    __slots__ = ("networks",)
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    networks: _containers.RepeatedCompositeFieldContainer[PacketBrokerNetwork]
    def __init__(self, networks: _Optional[_Iterable[_Union[PacketBrokerNetwork, _Mapping]]] = ...) -> None: ...

class PacketBrokerInfo(_message.Message):
    __slots__ = ("registration", "forwarder_enabled", "home_network_enabled", "register_enabled")
    REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HOME_NETWORK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REGISTER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    registration: PacketBrokerNetwork
    forwarder_enabled: bool
    home_network_enabled: bool
    register_enabled: bool
    def __init__(self, registration: _Optional[_Union[PacketBrokerNetwork, _Mapping]] = ..., forwarder_enabled: bool = ..., home_network_enabled: bool = ..., register_enabled: bool = ...) -> None: ...

class PacketBrokerRegisterRequest(_message.Message):
    __slots__ = ("listed",)
    LISTED_FIELD_NUMBER: _ClassVar[int]
    listed: _wrappers_pb2.BoolValue
    def __init__(self, listed: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class PacketBrokerRoutingPolicyUplink(_message.Message):
    __slots__ = ("join_request", "mac_data", "application_data", "signal_quality", "localization")
    JOIN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MAC_DATA_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_DATA_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_QUALITY_FIELD_NUMBER: _ClassVar[int]
    LOCALIZATION_FIELD_NUMBER: _ClassVar[int]
    join_request: bool
    mac_data: bool
    application_data: bool
    signal_quality: bool
    localization: bool
    def __init__(self, join_request: bool = ..., mac_data: bool = ..., application_data: bool = ..., signal_quality: bool = ..., localization: bool = ...) -> None: ...

class PacketBrokerRoutingPolicyDownlink(_message.Message):
    __slots__ = ("join_accept", "mac_data", "application_data")
    JOIN_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    MAC_DATA_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_DATA_FIELD_NUMBER: _ClassVar[int]
    join_accept: bool
    mac_data: bool
    application_data: bool
    def __init__(self, join_accept: bool = ..., mac_data: bool = ..., application_data: bool = ...) -> None: ...

class PacketBrokerDefaultRoutingPolicy(_message.Message):
    __slots__ = ("updated_at", "uplink", "downlink")
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPLINK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    updated_at: _timestamp_pb2.Timestamp
    uplink: PacketBrokerRoutingPolicyUplink
    downlink: PacketBrokerRoutingPolicyDownlink
    def __init__(self, updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., uplink: _Optional[_Union[PacketBrokerRoutingPolicyUplink, _Mapping]] = ..., downlink: _Optional[_Union[PacketBrokerRoutingPolicyDownlink, _Mapping]] = ...) -> None: ...

class PacketBrokerRoutingPolicy(_message.Message):
    __slots__ = ("forwarder_id", "home_network_id", "updated_at", "uplink", "downlink")
    FORWARDER_ID_FIELD_NUMBER: _ClassVar[int]
    HOME_NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPLINK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    forwarder_id: PacketBrokerNetworkIdentifier
    home_network_id: PacketBrokerNetworkIdentifier
    updated_at: _timestamp_pb2.Timestamp
    uplink: PacketBrokerRoutingPolicyUplink
    downlink: PacketBrokerRoutingPolicyDownlink
    def __init__(self, forwarder_id: _Optional[_Union[PacketBrokerNetworkIdentifier, _Mapping]] = ..., home_network_id: _Optional[_Union[PacketBrokerNetworkIdentifier, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., uplink: _Optional[_Union[PacketBrokerRoutingPolicyUplink, _Mapping]] = ..., downlink: _Optional[_Union[PacketBrokerRoutingPolicyDownlink, _Mapping]] = ...) -> None: ...

class SetPacketBrokerDefaultRoutingPolicyRequest(_message.Message):
    __slots__ = ("uplink", "downlink")
    UPLINK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    uplink: PacketBrokerRoutingPolicyUplink
    downlink: PacketBrokerRoutingPolicyDownlink
    def __init__(self, uplink: _Optional[_Union[PacketBrokerRoutingPolicyUplink, _Mapping]] = ..., downlink: _Optional[_Union[PacketBrokerRoutingPolicyDownlink, _Mapping]] = ...) -> None: ...

class ListHomeNetworkRoutingPoliciesRequest(_message.Message):
    __slots__ = ("limit", "page")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page: int
    def __init__(self, limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class PacketBrokerRoutingPolicies(_message.Message):
    __slots__ = ("policies",)
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[PacketBrokerRoutingPolicy]
    def __init__(self, policies: _Optional[_Iterable[_Union[PacketBrokerRoutingPolicy, _Mapping]]] = ...) -> None: ...

class SetPacketBrokerRoutingPolicyRequest(_message.Message):
    __slots__ = ("home_network_id", "uplink", "downlink")
    HOME_NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    UPLINK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    home_network_id: PacketBrokerNetworkIdentifier
    uplink: PacketBrokerRoutingPolicyUplink
    downlink: PacketBrokerRoutingPolicyDownlink
    def __init__(self, home_network_id: _Optional[_Union[PacketBrokerNetworkIdentifier, _Mapping]] = ..., uplink: _Optional[_Union[PacketBrokerRoutingPolicyUplink, _Mapping]] = ..., downlink: _Optional[_Union[PacketBrokerRoutingPolicyDownlink, _Mapping]] = ...) -> None: ...

class PacketBrokerGatewayVisibility(_message.Message):
    __slots__ = ("location", "antenna_placement", "antenna_count", "fine_timestamps", "contact_info", "status", "frequency_plan", "packet_rates")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    ANTENNA_COUNT_FIELD_NUMBER: _ClassVar[int]
    FINE_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    CONTACT_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PLAN_FIELD_NUMBER: _ClassVar[int]
    PACKET_RATES_FIELD_NUMBER: _ClassVar[int]
    location: bool
    antenna_placement: bool
    antenna_count: bool
    fine_timestamps: bool
    contact_info: bool
    status: bool
    frequency_plan: bool
    packet_rates: bool
    def __init__(self, location: bool = ..., antenna_placement: bool = ..., antenna_count: bool = ..., fine_timestamps: bool = ..., contact_info: bool = ..., status: bool = ..., frequency_plan: bool = ..., packet_rates: bool = ...) -> None: ...

class PacketBrokerDefaultGatewayVisibility(_message.Message):
    __slots__ = ("updated_at", "visibility")
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    updated_at: _timestamp_pb2.Timestamp
    visibility: PacketBrokerGatewayVisibility
    def __init__(self, updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., visibility: _Optional[_Union[PacketBrokerGatewayVisibility, _Mapping]] = ...) -> None: ...

class SetPacketBrokerDefaultGatewayVisibilityRequest(_message.Message):
    __slots__ = ("visibility",)
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    visibility: PacketBrokerGatewayVisibility
    def __init__(self, visibility: _Optional[_Union[PacketBrokerGatewayVisibility, _Mapping]] = ...) -> None: ...

class ListPacketBrokerNetworksRequest(_message.Message):
    __slots__ = ("limit", "page", "with_routing_policy", "tenant_id_contains", "name_contains")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    WITH_ROUTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page: int
    with_routing_policy: bool
    tenant_id_contains: str
    name_contains: str
    def __init__(self, limit: _Optional[int] = ..., page: _Optional[int] = ..., with_routing_policy: bool = ..., tenant_id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ...) -> None: ...

class ListPacketBrokerHomeNetworksRequest(_message.Message):
    __slots__ = ("limit", "page", "tenant_id_contains", "name_contains")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page: int
    tenant_id_contains: str
    name_contains: str
    def __init__(self, limit: _Optional[int] = ..., page: _Optional[int] = ..., tenant_id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ...) -> None: ...

class ListForwarderRoutingPoliciesRequest(_message.Message):
    __slots__ = ("home_network_id", "limit", "page")
    HOME_NETWORK_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    home_network_id: PacketBrokerNetworkIdentifier
    limit: int
    page: int
    def __init__(self, home_network_id: _Optional[_Union[PacketBrokerNetworkIdentifier, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class PacketBrokerAgentUplinkToken(_message.Message):
    __slots__ = ("forwarder_net_id", "forwarder_tenant_id", "forwarder_cluster_id")
    FORWARDER_NET_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    forwarder_net_id: bytes
    forwarder_tenant_id: str
    forwarder_cluster_id: str
    def __init__(self, forwarder_net_id: _Optional[bytes] = ..., forwarder_tenant_id: _Optional[str] = ..., forwarder_cluster_id: _Optional[str] = ...) -> None: ...

class PacketBrokerAgentGatewayUplinkToken(_message.Message):
    __slots__ = ("gateway_uid", "token")
    GATEWAY_UID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    gateway_uid: str
    token: bytes
    def __init__(self, gateway_uid: _Optional[str] = ..., token: _Optional[bytes] = ...) -> None: ...

class PacketBrokerAgentCompoundUplinkToken(_message.Message):
    __slots__ = ("gateway", "forwarder", "agent")
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    FORWARDER_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    gateway: bytes
    forwarder: bytes
    agent: PacketBrokerAgentUplinkToken
    def __init__(self, gateway: _Optional[bytes] = ..., forwarder: _Optional[bytes] = ..., agent: _Optional[_Union[PacketBrokerAgentUplinkToken, _Mapping]] = ...) -> None: ...

class PacketBrokerAgentEncryptedPayload(_message.Message):
    __slots__ = ("ciphertext", "nonce")
    CIPHERTEXT_FIELD_NUMBER: _ClassVar[int]
    NONCE_FIELD_NUMBER: _ClassVar[int]
    ciphertext: bytes
    nonce: bytes
    def __init__(self, ciphertext: _Optional[bytes] = ..., nonce: _Optional[bytes] = ...) -> None: ...
