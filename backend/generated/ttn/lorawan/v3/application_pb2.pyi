from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from generated.ttn.lorawan.v3 import contact_info_pb2 as _contact_info_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Application(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "deleted_at", "name", "description", "attributes", "contact_info", "administrative_contact", "technical_contact", "network_server_address", "application_server_address", "join_server_address", "dev_eui_counter")
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
    NETWORK_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    JOIN_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_COUNTER_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.ApplicationIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    name: str
    description: str
    attributes: _containers.ScalarMap[str, str]
    contact_info: _containers.RepeatedCompositeFieldContainer[_contact_info_pb2.ContactInfo]
    administrative_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    technical_contact: _identifiers_pb2.OrganizationOrUserIdentifiers
    network_server_address: str
    application_server_address: str
    join_server_address: str
    dev_eui_counter: int
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., contact_info: _Optional[_Iterable[_Union[_contact_info_pb2.ContactInfo, _Mapping]]] = ..., administrative_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., technical_contact: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., network_server_address: _Optional[str] = ..., application_server_address: _Optional[str] = ..., join_server_address: _Optional[str] = ..., dev_eui_counter: _Optional[int] = ...) -> None: ...

class Applications(_message.Message):
    __slots__ = ("applications",)
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[Application]
    def __init__(self, applications: _Optional[_Iterable[_Union[Application, _Mapping]]] = ...) -> None: ...

class IssueDevEUIResponse(_message.Message):
    __slots__ = ("dev_eui",)
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    dev_eui: bytes
    def __init__(self, dev_eui: _Optional[bytes] = ...) -> None: ...

class GetApplicationRequest(_message.Message):
    __slots__ = ("application_ids", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListApplicationsRequest(_message.Message):
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

class CreateApplicationRequest(_message.Message):
    __slots__ = ("application", "collaborator")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    application: Application
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class UpdateApplicationRequest(_message.Message):
    __slots__ = ("application", "field_mask")
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application: Application
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application: _Optional[_Union[Application, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListApplicationAPIKeysRequest(_message.Message):
    __slots__ = ("application_ids", "order", "limit", "page")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    order: str
    limit: int
    page: int
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class GetApplicationAPIKeyRequest(_message.Message):
    __slots__ = ("application_ids", "key_id")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    key_id: str
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class CreateApplicationAPIKeyRequest(_message.Message):
    __slots__ = ("application_ids", "name", "rights", "expires_at")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    name: str
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., name: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateApplicationAPIKeyRequest(_message.Message):
    __slots__ = ("application_ids", "api_key", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    api_key: _rights_pb2.APIKey
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., api_key: _Optional[_Union[_rights_pb2.APIKey, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteApplicationAPIKeyRequest(_message.Message):
    __slots__ = ("application_ids", "key_id")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    key_id: str
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class ListApplicationCollaboratorsRequest(_message.Message):
    __slots__ = ("application_ids", "limit", "page", "order")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    limit: int
    page: int
    order: str
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., order: _Optional[str] = ...) -> None: ...

class GetApplicationCollaboratorRequest(_message.Message):
    __slots__ = ("application_ids", "collaborator")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...

class SetApplicationCollaboratorRequest(_message.Message):
    __slots__ = ("application_ids", "collaborator")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    collaborator: _rights_pb2.Collaborator
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., collaborator: _Optional[_Union[_rights_pb2.Collaborator, _Mapping]] = ...) -> None: ...

class DeleteApplicationCollaboratorRequest(_message.Message):
    __slots__ = ("application_ids", "collaborator_ids")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_IDS_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    collaborator_ids: _identifiers_pb2.OrganizationOrUserIdentifiers
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., collaborator_ids: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ...) -> None: ...
