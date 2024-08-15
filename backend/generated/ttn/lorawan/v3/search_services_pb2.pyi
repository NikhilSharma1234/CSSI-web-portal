from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.ttn.lorawan.v3 import application_pb2 as _application_pb2
from ttn.lorawan.v3 import client_pb2 as _client_pb2
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from ttn.lorawan.v3 import gateway_pb2 as _gateway_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import organization_pb2 as _organization_pb2
from ttn.lorawan.v3 import user_pb2 as _user_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchApplicationsRequest(_message.Message):
    __slots__ = ("query", "id_contains", "name_contains", "description_contains", "attributes_contain", "field_mask", "order", "limit", "page", "deleted")
    class AttributesContainEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_CONTAIN_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    query: str
    id_contains: str
    name_contains: str
    description_contains: str
    attributes_contain: _containers.ScalarMap[str, str]
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    def __init__(self, query: _Optional[str] = ..., id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ..., description_contains: _Optional[str] = ..., attributes_contain: _Optional[_Mapping[str, str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class SearchClientsRequest(_message.Message):
    __slots__ = ("query", "id_contains", "name_contains", "description_contains", "attributes_contain", "state", "field_mask", "order", "limit", "page", "deleted")
    class AttributesContainEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_CONTAIN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    query: str
    id_contains: str
    name_contains: str
    description_contains: str
    attributes_contain: _containers.ScalarMap[str, str]
    state: _containers.RepeatedScalarFieldContainer[_enums_pb2.State]
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    def __init__(self, query: _Optional[str] = ..., id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ..., description_contains: _Optional[str] = ..., attributes_contain: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Iterable[_Union[_enums_pb2.State, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class SearchGatewaysRequest(_message.Message):
    __slots__ = ("query", "id_contains", "name_contains", "description_contains", "attributes_contain", "eui_contains", "field_mask", "order", "limit", "page", "deleted")
    class AttributesContainEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_CONTAIN_FIELD_NUMBER: _ClassVar[int]
    EUI_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    query: str
    id_contains: str
    name_contains: str
    description_contains: str
    attributes_contain: _containers.ScalarMap[str, str]
    eui_contains: str
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    def __init__(self, query: _Optional[str] = ..., id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ..., description_contains: _Optional[str] = ..., attributes_contain: _Optional[_Mapping[str, str]] = ..., eui_contains: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class SearchOrganizationsRequest(_message.Message):
    __slots__ = ("query", "id_contains", "name_contains", "description_contains", "attributes_contain", "field_mask", "order", "limit", "page", "deleted")
    class AttributesContainEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_CONTAIN_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    query: str
    id_contains: str
    name_contains: str
    description_contains: str
    attributes_contain: _containers.ScalarMap[str, str]
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    def __init__(self, query: _Optional[str] = ..., id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ..., description_contains: _Optional[str] = ..., attributes_contain: _Optional[_Mapping[str, str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class SearchUsersRequest(_message.Message):
    __slots__ = ("query", "id_contains", "name_contains", "description_contains", "attributes_contain", "state", "field_mask", "order", "limit", "page", "deleted")
    class AttributesContainEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_CONTAIN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    query: str
    id_contains: str
    name_contains: str
    description_contains: str
    attributes_contain: _containers.ScalarMap[str, str]
    state: _containers.RepeatedScalarFieldContainer[_enums_pb2.State]
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    def __init__(self, query: _Optional[str] = ..., id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ..., description_contains: _Optional[str] = ..., attributes_contain: _Optional[_Mapping[str, str]] = ..., state: _Optional[_Iterable[_Union[_enums_pb2.State, str]]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class SearchAccountsRequest(_message.Message):
    __slots__ = ("query", "only_users", "application_ids", "client_ids", "gateway_ids", "organization_ids", "complement_collaborators")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ONLY_USERS_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_IDS_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_COLLABORATORS_FIELD_NUMBER: _ClassVar[int]
    query: str
    only_users: bool
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    client_ids: _identifiers_pb2.ClientIdentifiers
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    organization_ids: _identifiers_pb2.OrganizationIdentifiers
    complement_collaborators: bool
    def __init__(self, query: _Optional[str] = ..., only_users: bool = ..., application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., organization_ids: _Optional[_Union[_identifiers_pb2.OrganizationIdentifiers, _Mapping]] = ..., complement_collaborators: bool = ...) -> None: ...

class SearchAccountsResponse(_message.Message):
    __slots__ = ("account_ids",)
    ACCOUNT_IDS_FIELD_NUMBER: _ClassVar[int]
    account_ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.OrganizationOrUserIdentifiers]
    def __init__(self, account_ids: _Optional[_Iterable[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]]] = ...) -> None: ...

class SearchEndDevicesRequest(_message.Message):
    __slots__ = ("application_ids", "query", "id_contains", "name_contains", "description_contains", "attributes_contain", "dev_eui_contains", "join_eui_contains", "dev_addr_contains", "field_mask", "order", "limit", "page")
    class AttributesContainEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    ID_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    NAME_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_CONTAIN_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    JOIN_EUI_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    DEV_ADDR_CONTAINS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    query: str
    id_contains: str
    name_contains: str
    description_contains: str
    attributes_contain: _containers.ScalarMap[str, str]
    dev_eui_contains: str
    join_eui_contains: str
    dev_addr_contains: str
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., query: _Optional[str] = ..., id_contains: _Optional[str] = ..., name_contains: _Optional[str] = ..., description_contains: _Optional[str] = ..., attributes_contain: _Optional[_Mapping[str, str]] = ..., dev_eui_contains: _Optional[str] = ..., join_eui_contains: _Optional[str] = ..., dev_addr_contains: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...
