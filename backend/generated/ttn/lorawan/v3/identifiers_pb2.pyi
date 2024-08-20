from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationIdentifiers(_message.Message):
    __slots__ = ("application_id",)
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    def __init__(self, application_id: _Optional[str] = ...) -> None: ...

class ClientIdentifiers(_message.Message):
    __slots__ = ("client_id",)
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    def __init__(self, client_id: _Optional[str] = ...) -> None: ...

class EndDeviceIdentifiers(_message.Message):
    __slots__ = ("device_id", "application_ids", "dev_eui", "join_eui", "dev_addr")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    application_ids: ApplicationIdentifiers
    dev_eui: bytes
    join_eui: bytes
    dev_addr: bytes
    def __init__(self, device_id: _Optional[str] = ..., application_ids: _Optional[_Union[ApplicationIdentifiers, _Mapping]] = ..., dev_eui: _Optional[bytes] = ..., join_eui: _Optional[bytes] = ..., dev_addr: _Optional[bytes] = ...) -> None: ...

class GatewayIdentifiers(_message.Message):
    __slots__ = ("gateway_id", "eui")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    EUI_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    eui: bytes
    def __init__(self, gateway_id: _Optional[str] = ..., eui: _Optional[bytes] = ...) -> None: ...

class OrganizationIdentifiers(_message.Message):
    __slots__ = ("organization_id",)
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    organization_id: str
    def __init__(self, organization_id: _Optional[str] = ...) -> None: ...

class UserIdentifiers(_message.Message):
    __slots__ = ("user_id", "email")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    email: str
    def __init__(self, user_id: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class OrganizationOrUserIdentifiers(_message.Message):
    __slots__ = ("organization_ids", "user_ids")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    organization_ids: OrganizationIdentifiers
    user_ids: UserIdentifiers
    def __init__(self, organization_ids: _Optional[_Union[OrganizationIdentifiers, _Mapping]] = ..., user_ids: _Optional[_Union[UserIdentifiers, _Mapping]] = ...) -> None: ...

class EntityIdentifiers(_message.Message):
    __slots__ = ("application_ids", "client_ids", "device_ids", "gateway_ids", "organization_ids", "user_ids")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    application_ids: ApplicationIdentifiers
    client_ids: ClientIdentifiers
    device_ids: EndDeviceIdentifiers
    gateway_ids: GatewayIdentifiers
    organization_ids: OrganizationIdentifiers
    user_ids: UserIdentifiers
    def __init__(self, application_ids: _Optional[_Union[ApplicationIdentifiers, _Mapping]] = ..., client_ids: _Optional[_Union[ClientIdentifiers, _Mapping]] = ..., device_ids: _Optional[_Union[EndDeviceIdentifiers, _Mapping]] = ..., gateway_ids: _Optional[_Union[GatewayIdentifiers, _Mapping]] = ..., organization_ids: _Optional[_Union[OrganizationIdentifiers, _Mapping]] = ..., user_ids: _Optional[_Union[UserIdentifiers, _Mapping]] = ...) -> None: ...

class EndDeviceVersionIdentifiers(_message.Message):
    __slots__ = ("brand_id", "model_id", "hardware_version", "firmware_version", "band_id")
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
    BAND_ID_FIELD_NUMBER: _ClassVar[int]
    brand_id: str
    model_id: str
    hardware_version: str
    firmware_version: str
    band_id: str
    def __init__(self, brand_id: _Optional[str] = ..., model_id: _Optional[str] = ..., hardware_version: _Optional[str] = ..., firmware_version: _Optional[str] = ..., band_id: _Optional[str] = ...) -> None: ...

class NetworkIdentifiers(_message.Message):
    __slots__ = ("net_id", "ns_id", "tenant_id", "cluster_id", "cluster_address", "tenant_address")
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    NS_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    net_id: bytes
    ns_id: bytes
    tenant_id: str
    cluster_id: str
    cluster_address: str
    tenant_address: str
    def __init__(self, net_id: _Optional[bytes] = ..., ns_id: _Optional[bytes] = ..., tenant_id: _Optional[str] = ..., cluster_id: _Optional[str] = ..., cluster_address: _Optional[str] = ..., tenant_address: _Optional[str] = ...) -> None: ...

class LoRaAllianceProfileIdentifiers(_message.Message):
    __slots__ = ("vendor_id", "vendor_profile_id")
    VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    vendor_id: int
    vendor_profile_id: int
    def __init__(self, vendor_id: _Optional[int] = ..., vendor_profile_id: _Optional[int] = ...) -> None: ...

class EndDeviceIdentifiersList(_message.Message):
    __slots__ = ("end_device_ids",)
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _containers.RepeatedCompositeFieldContainer[EndDeviceIdentifiers]
    def __init__(self, end_device_ids: _Optional[_Iterable[_Union[EndDeviceIdentifiers, _Mapping]]] = ...) -> None: ...

class GatewayIdentifiersList(_message.Message):
    __slots__ = ("gateway_ids",)
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _containers.RepeatedCompositeFieldContainer[GatewayIdentifiers]
    def __init__(self, gateway_ids: _Optional[_Iterable[_Union[GatewayIdentifiers, _Mapping]]] = ...) -> None: ...
