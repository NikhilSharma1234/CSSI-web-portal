from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1
from generated.ttn.lorawan.v3 import contact_info_pb2 as _contact_info_pb2
from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRANT_AUTHORIZATION_CODE: _ClassVar[GrantType]
    GRANT_PASSWORD: _ClassVar[GrantType]
    GRANT_REFRESH_TOKEN: _ClassVar[GrantType]
GRANT_AUTHORIZATION_CODE: GrantType
GRANT_PASSWORD: GrantType
GRANT_REFRESH_TOKEN: GrantType

class Client(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "deleted_at", "name", "description", "attributes", "contact_info", "administrative_contact", "technical_contact", "secret", "redirect_uris", "logout_redirect_uris", "state", "state_description", "skip_authorization", "endorsed", "grants", "rights")
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
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
    SECRET_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    LOGOUT_REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SKIP_AUTHORIZATION_FIELD_NUMBER: _ClassVar[int]
    ENDORSED_FIELD_NUMBER: _ClassVar[int]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.ClientIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    name: str
    description: str
    attributes: _containers.ScalarMap[str, str]
    contact_info: _containers.RepeatedCompositeFieldContainer[_contact_info_pb2.ContactInfo]
    administrative_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    technical_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    secret: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    logout_redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    state: _enums_pb2.State
    state_description: str
    skip_authorization: bool
    endorsed: bool
    grants: _containers.RepeatedScalarFieldContainer[GrantType]
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., contact_info: _Optional[_Iterable[_Union[_contact_info_pb2.ContactInfo, _Mapping]]] = ..., administrative_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., technical_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., secret: _Optional[str] = ..., redirect_uris: _Optional[_Iterable[str]] = ..., logout_redirect_uris: _Optional[_Iterable[str]] = ..., state: _Optional[_Union[_enums_pb2.State, str]] = ..., state_description: _Optional[str] = ..., skip_authorization: bool = ..., endorsed: bool = ..., grants: _Optional[_Iterable[_Union[GrantType, str]]] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ...) -> None: ...

class Clients(_message.Message):
    __slots__ = ("clients",)
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[Client]
    def __init__(self, clients: _Optional[_Iterable[_Union[Client, _Mapping]]] = ...) -> None: ...

class GetClientRequest(_message.Message):
    __slots__ = ("client_ids", "field_mask")
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    client_ids: _identifiers_pb2.ClientIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListClientsRequest(_message.Message):
    __slots__ = ("collaborator", "field_mask", "order", "limit", "page", "deleted")
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    def __init__(self, collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class CreateClientRequest(_message.Message):
    __slots__ = ("client", "collaborator")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    client: Client
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class UpdateClientRequest(_message.Message):
    __slots__ = ("client", "field_mask")
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    client: Client
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, client: _Optional[_Union[Client, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListClientCollaboratorsRequest(_message.Message):
    __slots__ = ("client_ids", "limit", "page", "order")
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    client_ids: _identifiers_pb2.ClientIdentifiers
    limit: int
    page: int
    order: str
    def __init__(self, client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., order: _Optional[str] = ...) -> None: ...

class GetClientCollaboratorRequest(_message.Message):
    __slots__ = ("client_ids", "collaborator")
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    client_ids: _identifiers_pb2.ClientIdentifiers
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class SetClientCollaboratorRequest(_message.Message):
    __slots__ = ("client_ids", "collaborator")
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    client_ids: _identifiers_pb2.ClientIdentifiers
    collaborator: _rights_pb2.Collaborator
    def __init__(self, client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_rights_pb2.Collaborator, _Mapping]] = ...) -> None: ...

class DeleteClientCollaboratorRequest(_message.Message):
    __slots__ = ("client_ids", "collaborator_ids")
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_IDS_FIELD_NUMBER: _ClassVar[int]
    client_ids: _identifiers_pb2.ClientIdentifiers
    collaborator_ids: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., collaborator_ids: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...
