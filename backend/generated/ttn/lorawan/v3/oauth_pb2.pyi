from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OAuthClientAuthorizationIdentifiers(_message.Message):
    __slots__ = ("user_ids", "client_ids")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    client_ids: _identifiers_pb2.ClientIdentifiers
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ...) -> None: ...

class OAuthClientAuthorization(_message.Message):
    __slots__ = ("user_ids", "client_ids", "rights", "created_at", "updated_at")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    client_ids: _identifiers_pb2.ClientIdentifiers
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OAuthClientAuthorizations(_message.Message):
    __slots__ = ("authorizations",)
    AUTHORIZATIONS_FIELD_NUMBER: _ClassVar[int]
    authorizations: _containers.RepeatedCompositeFieldContainer[OAuthClientAuthorization]
    def __init__(self, authorizations: _Optional[_Iterable[_Union[OAuthClientAuthorization, _Mapping]]] = ...) -> None: ...

class ListOAuthClientAuthorizationsRequest(_message.Message):
    __slots__ = ("user_ids", "order", "limit", "page")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    order: str
    limit: int
    page: int
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class OAuthAuthorizationCode(_message.Message):
    __slots__ = ("user_ids", "user_session_id", "client_ids", "rights", "code", "redirect_uri", "state", "created_at", "expires_at")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    user_session_id: str
    client_ids: _identifiers_pb2.ClientIdentifiers
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    code: str
    redirect_uri: str
    state: str
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., user_session_id: _Optional[str] = ..., client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ..., code: _Optional[str] = ..., redirect_uri: _Optional[str] = ..., state: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OAuthAccessTokenIdentifiers(_message.Message):
    __slots__ = ("user_ids", "client_ids", "id")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    client_ids: _identifiers_pb2.ClientIdentifiers
    id: str
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class OAuthAccessToken(_message.Message):
    __slots__ = ("user_ids", "user_session_id", "client_ids", "id", "access_token", "refresh_token", "rights", "created_at", "expires_at")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    USER_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    user_session_id: str
    client_ids: _identifiers_pb2.ClientIdentifiers
    id: str
    access_token: str
    refresh_token: str
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., user_session_id: _Optional[str] = ..., client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., id: _Optional[str] = ..., access_token: _Optional[str] = ..., refresh_token: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OAuthAccessTokens(_message.Message):
    __slots__ = ("tokens",)
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[OAuthAccessToken]
    def __init__(self, tokens: _Optional[_Iterable[_Union[OAuthAccessToken, _Mapping]]] = ...) -> None: ...

class ListOAuthAccessTokensRequest(_message.Message):
    __slots__ = ("user_ids", "client_ids", "order", "limit", "page")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    client_ids: _identifiers_pb2.ClientIdentifiers
    order: str
    limit: int
    page: int
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., client_ids: _Optional[_Union[_identifiers_pb2.ClientIdentifiers, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...
