from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2
from generated.ttn.lorawan.v3 import contact_info_pb2 as _contact_info_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Organization(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "deleted_at", "name", "description", "attributes", "contact_info", "administrative_contact", "technical_contact", "fanout_notifications")
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
    FANOUT_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.OrganizationIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    name: str
    description: str
    attributes: _containers.ScalarMap[str, str]
    contact_info: _containers.RepeatedCompositeFieldContainer[_contact_info_pb2.ContactInfo]
    administrative_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    technical_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    fanout_notifications: bool
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., contact_info: _Optional[_Iterable[_Union[_contact_info_pb2.ContactInfo, _Mapping]]] = ..., administrative_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., technical_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., fanout_notifications: bool = ...) -> None: ...

class Organizations(_message.Message):
    __slots__ = ("organizations",)
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[Organization]
    def __init__(self, organizations: _Optional[_Iterable[_Union[Organization, _Mapping]]] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ("organization_ids", "field_mask")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListOrganizationsRequest(_message.Message):
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

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("organization", "collaborator")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("organization", "field_mask")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListOrganizationAPIKeysRequest(_message.Message):
    __slots__ = ("organization_ids", "order", "limit", "page")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    order: str
    limit: int
    page: int
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetOrganizationAPIKeyRequest(_message.Message):
    __slots__ = ("organization_ids", "key_id")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    key_id: str
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class CreateOrganizationAPIKeyRequest(_message.Message):
    __slots__ = ("organization_ids", "name", "rights", "expires_at")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    name: str
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., name: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateOrganizationAPIKeyRequest(_message.Message):
    __slots__ = ("organization_ids", "api_key", "field_mask")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    api_key: _rights_pb2.APIKey
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., api_key: _Optional[_Union[_rights_pb2.APIKey, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteOrganizationAPIKeyRequest(_message.Message):
    __slots__ = ("organization_ids", "key_id")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    key_id: str
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class ListOrganizationCollaboratorsRequest(_message.Message):
    __slots__ = ("organization_ids", "limit", "page", "order")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    limit: int
    page: int
    order: str
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., order: _Optional[str] = ...) -> None: ...

class GetOrganizationCollaboratorRequest(_message.Message):
    __slots__ = ("organization_ids", "collaborator")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class SetOrganizationCollaboratorRequest(_message.Message):
    __slots__ = ("organization_ids", "collaborator")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    collaborator: _rights_pb2.Collaborator
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_rights_pb2.Collaborator, _Mapping]] = ...) -> None: ...

class DeleteOrganizationCollaboratorRequest(_message.Message):
    __slots__ = ("organization_ids", "collaborator_ids")
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_IDS_FIELD_NUMBER: _ClassVar[int]
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    collaborator_ids: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., collaborator_ids: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...
