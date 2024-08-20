from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Right(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    right_invalid: _ClassVar[Right]
    RIGHT_USER_INFO: _ClassVar[Right]
    RIGHT_USER_SETTINGS_BASIC: _ClassVar[Right]
    RIGHT_USER_SETTINGS_API_KEYS: _ClassVar[Right]
    RIGHT_USER_DELETE: _ClassVar[Right]
    RIGHT_USER_AUTHORIZED_CLIENTS: _ClassVar[Right]
    RIGHT_USER_APPLICATIONS_LIST: _ClassVar[Right]
    RIGHT_USER_APPLICATIONS_CREATE: _ClassVar[Right]
    RIGHT_USER_GATEWAYS_LIST: _ClassVar[Right]
    RIGHT_USER_GATEWAYS_CREATE: _ClassVar[Right]
    RIGHT_USER_CLIENTS_LIST: _ClassVar[Right]
    RIGHT_USER_CLIENTS_CREATE: _ClassVar[Right]
    RIGHT_USER_ORGANIZATIONS_LIST: _ClassVar[Right]
    RIGHT_USER_ORGANIZATIONS_CREATE: _ClassVar[Right]
    RIGHT_USER_NOTIFICATIONS_READ: _ClassVar[Right]
    RIGHT_USER_ALL: _ClassVar[Right]
    RIGHT_APPLICATION_INFO: _ClassVar[Right]
    RIGHT_APPLICATION_SETTINGS_BASIC: _ClassVar[Right]
    RIGHT_APPLICATION_SETTINGS_API_KEYS: _ClassVar[Right]
    RIGHT_APPLICATION_SETTINGS_COLLABORATORS: _ClassVar[Right]
    RIGHT_APPLICATION_SETTINGS_PACKAGES: _ClassVar[Right]
    RIGHT_APPLICATION_DELETE: _ClassVar[Right]
    RIGHT_APPLICATION_DEVICES_READ: _ClassVar[Right]
    RIGHT_APPLICATION_DEVICES_WRITE: _ClassVar[Right]
    RIGHT_APPLICATION_DEVICES_READ_KEYS: _ClassVar[Right]
    RIGHT_APPLICATION_DEVICES_WRITE_KEYS: _ClassVar[Right]
    RIGHT_APPLICATION_TRAFFIC_READ: _ClassVar[Right]
    RIGHT_APPLICATION_TRAFFIC_UP_WRITE: _ClassVar[Right]
    RIGHT_APPLICATION_TRAFFIC_DOWN_WRITE: _ClassVar[Right]
    RIGHT_APPLICATION_LINK: _ClassVar[Right]
    RIGHT_APPLICATION_ALL: _ClassVar[Right]
    RIGHT_CLIENT_ALL: _ClassVar[Right]
    RIGHT_CLIENT_INFO: _ClassVar[Right]
    RIGHT_CLIENT_SETTINGS_BASIC: _ClassVar[Right]
    RIGHT_CLIENT_SETTINGS_COLLABORATORS: _ClassVar[Right]
    RIGHT_CLIENT_DELETE: _ClassVar[Right]
    RIGHT_GATEWAY_INFO: _ClassVar[Right]
    RIGHT_GATEWAY_SETTINGS_BASIC: _ClassVar[Right]
    RIGHT_GATEWAY_SETTINGS_API_KEYS: _ClassVar[Right]
    RIGHT_GATEWAY_SETTINGS_COLLABORATORS: _ClassVar[Right]
    RIGHT_GATEWAY_DELETE: _ClassVar[Right]
    RIGHT_GATEWAY_TRAFFIC_READ: _ClassVar[Right]
    RIGHT_GATEWAY_TRAFFIC_DOWN_WRITE: _ClassVar[Right]
    RIGHT_GATEWAY_LINK: _ClassVar[Right]
    RIGHT_GATEWAY_STATUS_READ: _ClassVar[Right]
    RIGHT_GATEWAY_LOCATION_READ: _ClassVar[Right]
    RIGHT_GATEWAY_WRITE_SECRETS: _ClassVar[Right]
    RIGHT_GATEWAY_READ_SECRETS: _ClassVar[Right]
    RIGHT_GATEWAY_ALL: _ClassVar[Right]
    RIGHT_ORGANIZATION_INFO: _ClassVar[Right]
    RIGHT_ORGANIZATION_SETTINGS_BASIC: _ClassVar[Right]
    RIGHT_ORGANIZATION_SETTINGS_API_KEYS: _ClassVar[Right]
    RIGHT_ORGANIZATION_SETTINGS_MEMBERS: _ClassVar[Right]
    RIGHT_ORGANIZATION_DELETE: _ClassVar[Right]
    RIGHT_ORGANIZATION_APPLICATIONS_LIST: _ClassVar[Right]
    RIGHT_ORGANIZATION_APPLICATIONS_CREATE: _ClassVar[Right]
    RIGHT_ORGANIZATION_GATEWAYS_LIST: _ClassVar[Right]
    RIGHT_ORGANIZATION_GATEWAYS_CREATE: _ClassVar[Right]
    RIGHT_ORGANIZATION_CLIENTS_LIST: _ClassVar[Right]
    RIGHT_ORGANIZATION_CLIENTS_CREATE: _ClassVar[Right]
    RIGHT_ORGANIZATION_ADD_AS_COLLABORATOR: _ClassVar[Right]
    RIGHT_ORGANIZATION_ALL: _ClassVar[Right]
    RIGHT_SEND_INVITES: _ClassVar[Right]
    RIGHT_ALL: _ClassVar[Right]
right_invalid: Right
RIGHT_USER_INFO: Right
RIGHT_USER_SETTINGS_BASIC: Right
RIGHT_USER_SETTINGS_API_KEYS: Right
RIGHT_USER_DELETE: Right
RIGHT_USER_AUTHORIZED_CLIENTS: Right
RIGHT_USER_APPLICATIONS_LIST: Right
RIGHT_USER_APPLICATIONS_CREATE: Right
RIGHT_USER_GATEWAYS_LIST: Right
RIGHT_USER_GATEWAYS_CREATE: Right
RIGHT_USER_CLIENTS_LIST: Right
RIGHT_USER_CLIENTS_CREATE: Right
RIGHT_USER_ORGANIZATIONS_LIST: Right
RIGHT_USER_ORGANIZATIONS_CREATE: Right
RIGHT_USER_NOTIFICATIONS_READ: Right
RIGHT_USER_ALL: Right
RIGHT_APPLICATION_INFO: Right
RIGHT_APPLICATION_SETTINGS_BASIC: Right
RIGHT_APPLICATION_SETTINGS_API_KEYS: Right
RIGHT_APPLICATION_SETTINGS_COLLABORATORS: Right
RIGHT_APPLICATION_SETTINGS_PACKAGES: Right
RIGHT_APPLICATION_DELETE: Right
RIGHT_APPLICATION_DEVICES_READ: Right
RIGHT_APPLICATION_DEVICES_WRITE: Right
RIGHT_APPLICATION_DEVICES_READ_KEYS: Right
RIGHT_APPLICATION_DEVICES_WRITE_KEYS: Right
RIGHT_APPLICATION_TRAFFIC_READ: Right
RIGHT_APPLICATION_TRAFFIC_UP_WRITE: Right
RIGHT_APPLICATION_TRAFFIC_DOWN_WRITE: Right
RIGHT_APPLICATION_LINK: Right
RIGHT_APPLICATION_ALL: Right
RIGHT_CLIENT_ALL: Right
RIGHT_CLIENT_INFO: Right
RIGHT_CLIENT_SETTINGS_BASIC: Right
RIGHT_CLIENT_SETTINGS_COLLABORATORS: Right
RIGHT_CLIENT_DELETE: Right
RIGHT_GATEWAY_INFO: Right
RIGHT_GATEWAY_SETTINGS_BASIC: Right
RIGHT_GATEWAY_SETTINGS_API_KEYS: Right
RIGHT_GATEWAY_SETTINGS_COLLABORATORS: Right
RIGHT_GATEWAY_DELETE: Right
RIGHT_GATEWAY_TRAFFIC_READ: Right
RIGHT_GATEWAY_TRAFFIC_DOWN_WRITE: Right
RIGHT_GATEWAY_LINK: Right
RIGHT_GATEWAY_STATUS_READ: Right
RIGHT_GATEWAY_LOCATION_READ: Right
RIGHT_GATEWAY_WRITE_SECRETS: Right
RIGHT_GATEWAY_READ_SECRETS: Right
RIGHT_GATEWAY_ALL: Right
RIGHT_ORGANIZATION_INFO: Right
RIGHT_ORGANIZATION_SETTINGS_BASIC: Right
RIGHT_ORGANIZATION_SETTINGS_API_KEYS: Right
RIGHT_ORGANIZATION_SETTINGS_MEMBERS: Right
RIGHT_ORGANIZATION_DELETE: Right
RIGHT_ORGANIZATION_APPLICATIONS_LIST: Right
RIGHT_ORGANIZATION_APPLICATIONS_CREATE: Right
RIGHT_ORGANIZATION_GATEWAYS_LIST: Right
RIGHT_ORGANIZATION_GATEWAYS_CREATE: Right
RIGHT_ORGANIZATION_CLIENTS_LIST: Right
RIGHT_ORGANIZATION_CLIENTS_CREATE: Right
RIGHT_ORGANIZATION_ADD_AS_COLLABORATOR: Right
RIGHT_ORGANIZATION_ALL: Right
RIGHT_SEND_INVITES: Right
RIGHT_ALL: Right

class Rights(_message.Message):
    __slots__ = ("rights",)
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    rights: _containers.RepeatedScalarFieldContainer[Right]
    def __init__(self, rights: _Optional[_Iterable[_Union[Right, str]]] = ...) -> None: ...

class APIKey(_message.Message):
    __slots__ = ("id", "key", "name", "rights", "created_at", "updated_at", "expires_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    name: str
    rights: _containers.RepeatedScalarFieldContainer[Right]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[Right, str]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class APIKeys(_message.Message):
    __slots__ = ("api_keys",)
    API_KEYS_FIELD_NUMBER: _ClassVar[int]
    api_keys: _containers.RepeatedCompositeFieldContainer[APIKey]
    def __init__(self, api_keys: _Optional[_Iterable[_Union[APIKey, _Mapping]]] = ...) -> None: ...

class Collaborator(_message.Message):
    __slots__ = ("ids", "rights")
    IDS_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.OrganizationOrUserIdentifiers
    rights: _containers.RepeatedScalarFieldContainer[Right]
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., rights: _Optional[_Iterable[_Union[Right, str]]] = ...) -> None: ...

class GetCollaboratorResponse(_message.Message):
    __slots__ = ("ids", "rights")
    IDS_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.OrganizationOrUserIdentifiers
    rights: _containers.RepeatedScalarFieldContainer[Right]
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., rights: _Optional[_Iterable[_Union[Right, str]]] = ...) -> None: ...

class Collaborators(_message.Message):
    __slots__ = ("collaborators",)
    COLLABORATORS_FIELD_NUMBER: _ClassVar[int]
    collaborators: _containers.RepeatedCompositeFieldContainer[Collaborator]
    def __init__(self, collaborators: _Optional[_Iterable[_Union[Collaborator, _Mapping]]] = ...) -> None: ...
