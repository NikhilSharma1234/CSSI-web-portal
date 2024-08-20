from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import gateway_pb2 as _gateway_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetGatewayConfigurationRequest(_message.Message):
    __slots__ = ("gateway_ids", "format", "type", "filename")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    format: str
    type: str
    filename: str
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., format: _Optional[str] = ..., type: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...

class GetGatewayConfigurationResponse(_message.Message):
    __slots__ = ("contents",)
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    contents: bytes
    def __init__(self, contents: _Optional[bytes] = ...) -> None: ...

class UpdateManagedGatewayRequest(_message.Message):
    __slots__ = ("gateway", "field_mask")
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway: _gateway_pb2.ManagedGateway
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway: _Optional[_Union[_gateway_pb2.ManagedGateway, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateManagedGatewayWiFiProfileRequest(_message.Message):
    __slots__ = ("profile", "collaborator")
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    profile: _gateway_pb2.ManagedGatewayWiFiProfile
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, profile: _Optional[_Union[_gateway_pb2.ManagedGatewayWiFiProfile, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class UpdateManagedGatewayWiFiProfileRequest(_message.Message):
    __slots__ = ("profile", "collaborator", "field_mask")
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    profile: _gateway_pb2.ManagedGatewayWiFiProfile
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, profile: _Optional[_Union[_gateway_pb2.ManagedGatewayWiFiProfile, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListManagedGatewayWiFiProfilesRequest(_message.Message):
    __slots__ = ("collaborator", "field_mask", "limit", "page")
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    limit: int
    page: int
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetManagedGatewayWiFiProfileRequest(_message.Message):
    __slots__ = ("collaborator", "profile_id", "field_mask")
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    profile_id: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., profile_id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteManagedGatewayWiFiProfileRequest(_message.Message):
    __slots__ = ("collaborator", "profile_id")
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    profile_id: str
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., profile_id: _Optional[str] = ...) -> None: ...

class CreateManagedGatewayEthernetProfileRequest(_message.Message):
    __slots__ = ("profile", "collaborator")
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    profile: _gateway_pb2.ManagedGatewayEthernetProfile
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, profile: _Optional[_Union[_gateway_pb2.ManagedGatewayEthernetProfile, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class UpdateManagedGatewayEthernetProfileRequest(_message.Message):
    __slots__ = ("profile", "collaborator", "field_mask")
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    profile: _gateway_pb2.ManagedGatewayEthernetProfile
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, profile: _Optional[_Union[_gateway_pb2.ManagedGatewayEthernetProfile, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListManagedGatewayEthernetProfilesRequest(_message.Message):
    __slots__ = ("collaborator", "field_mask", "limit", "page")
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    limit: int
    page: int
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetManagedGatewayEthernetProfileRequest(_message.Message):
    __slots__ = ("collaborator", "profile_id", "field_mask")
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    profile_id: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., profile_id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteManagedGatewayEthernetProfileRequest(_message.Message):
    __slots__ = ("collaborator", "profile_id")
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    profile_id: str
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., profile_id: _Optional[str] = ...) -> None: ...
