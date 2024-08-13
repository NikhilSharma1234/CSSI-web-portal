from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1
from generated.ttn.lorawan.v3 import contact_info_pb2 as _contact_info_pb2
from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import picture_pb2 as _picture_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsoleTheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSOLE_THEME_SYSTEM: _ClassVar[ConsoleTheme]
    CONSOLE_THEME_LIGHT: _ClassVar[ConsoleTheme]
    CONSOLE_THEME_DARK: _ClassVar[ConsoleTheme]

class DashboardLayout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DASHBOARD_LAYOUT_TABLE: _ClassVar[DashboardLayout]
    DASHBOARD_LAYOUT_LIST: _ClassVar[DashboardLayout]
    DASHBOARD_LAYOUT_GRID: _ClassVar[DashboardLayout]
CONSOLE_THEME_SYSTEM: ConsoleTheme
CONSOLE_THEME_LIGHT: ConsoleTheme
CONSOLE_THEME_DARK: ConsoleTheme
DASHBOARD_LAYOUT_TABLE: DashboardLayout
DASHBOARD_LAYOUT_LIST: DashboardLayout
DASHBOARD_LAYOUT_GRID: DashboardLayout

class UserConsolePreferences(_message.Message):
    __slots__ = ("console_theme", "dashboard_layouts", "sort_by")
    class DashboardLayouts(_message.Message):
        __slots__ = ("api_key", "application", "collaborator", "end_device", "gateway", "organization", "overview", "user")
        API_KEY_FIELD_NUMBER: _ClassVar[int]
        APPLICATION_FIELD_NUMBER: _ClassVar[int]
        COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
        END_DEVICE_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
        OVERVIEW_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        api_key: DashboardLayout
        application: DashboardLayout
        collaborator: DashboardLayout
        end_device: DashboardLayout
        gateway: DashboardLayout
        organization: DashboardLayout
        overview: DashboardLayout
        user: DashboardLayout
        def __init__(self, api_key: _Optional[_Union[DashboardLayout, str]] = ..., application: _Optional[_Union[DashboardLayout, str]] = ..., collaborator: _Optional[_Union[DashboardLayout, str]] = ..., end_device: _Optional[_Union[DashboardLayout, str]] = ..., gateway: _Optional[_Union[DashboardLayout, str]] = ..., organization: _Optional[_Union[DashboardLayout, str]] = ..., overview: _Optional[_Union[DashboardLayout, str]] = ..., user: _Optional[_Union[DashboardLayout, str]] = ...) -> None: ...
    class SortBy(_message.Message):
        __slots__ = ("api_key", "application", "collaborator", "end_device", "gateway", "organization", "user")
        API_KEY_FIELD_NUMBER: _ClassVar[int]
        APPLICATION_FIELD_NUMBER: _ClassVar[int]
        COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
        END_DEVICE_FIELD_NUMBER: _ClassVar[int]
        GATEWAY_FIELD_NUMBER: _ClassVar[int]
        ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
        USER_FIELD_NUMBER: _ClassVar[int]
        api_key: str
        application: str
        collaborator: str
        end_device: str
        gateway: str
        organization: str
        user: str
        def __init__(self, api_key: _Optional[str] = ..., application: _Optional[str] = ..., collaborator: _Optional[str] = ..., end_device: _Optional[str] = ..., gateway: _Optional[str] = ..., organization: _Optional[str] = ..., user: _Optional[str] = ...) -> None: ...
    CONSOLE_THEME_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_LAYOUTS_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    console_theme: ConsoleTheme
    dashboard_layouts: UserConsolePreferences.DashboardLayouts
    sort_by: UserConsolePreferences.SortBy
    def __init__(self, console_theme: _Optional[_Union[ConsoleTheme, str]] = ..., dashboard_layouts: _Optional[_Union[UserConsolePreferences.DashboardLayouts, _Mapping]] = ..., sort_by: _Optional[_Union[UserConsolePreferences.SortBy, _Mapping]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "deleted_at", "name", "description", "attributes", "contact_info", "primary_email_address", "primary_email_address_validated_at", "password", "password_updated_at", "require_password_update", "state", "state_description", "admin", "temporary_password", "temporary_password_created_at", "temporary_password_expires_at", "profile_picture", "console_preferences")
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
    PRIMARY_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_EMAIL_ADDRESS_VALIDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PASSWORD_UPDATE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ADMIN_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PASSWORD_CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PASSWORD_EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.UserIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    deleted_at: _timestamp_pb2.Timestamp
    name: str
    description: str
    attributes: _containers.ScalarMap[str, str]
    contact_info: _containers.RepeatedCompositeFieldContainer[_contact_info_pb2.ContactInfo]
    primary_email_address: str
    primary_email_address_validated_at: _timestamp_pb2.Timestamp
    password: str
    password_updated_at: _timestamp_pb2.Timestamp
    require_password_update: bool
    state: _enums_pb2.State
    state_description: str
    admin: bool
    temporary_password: str
    temporary_password_created_at: _timestamp_pb2.Timestamp
    temporary_password_expires_at: _timestamp_pb2.Timestamp
    profile_picture: _picture_pb2.Picture
    console_preferences: UserConsolePreferences
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., contact_info: _Optional[_Iterable[_Union[_contact_info_pb2.ContactInfo, _Mapping]]] = ..., primary_email_address: _Optional[str] = ..., primary_email_address_validated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., password: _Optional[str] = ..., password_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., require_password_update: bool = ..., state: _Optional[_Union[_enums_pb2.State, str]] = ..., state_description: _Optional[str] = ..., admin: bool = ..., temporary_password: _Optional[str] = ..., temporary_password_created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., temporary_password_expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., profile_picture: _Optional[_Union[_picture_pb2.Picture, _Mapping]] = ..., console_preferences: _Optional[_Union[UserConsolePreferences, _Mapping]] = ...) -> None: ...

class Users(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, users: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ("user_ids", "field_mask")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("field_mask", "order", "limit", "page", "deleted")
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    order: str
    limit: int
    page: int
    deleted: bool
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., order: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., deleted: bool = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ("user", "invitation_token")
    USER_FIELD_NUMBER: _ClassVar[int]
    INVITATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user: User
    invitation_token: str
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., invitation_token: _Optional[str] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ("user", "field_mask")
    USER_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    user: User
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class CreateTemporaryPasswordRequest(_message.Message):
    __slots__ = ("user_ids",)
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ...) -> None: ...

class UpdateUserPasswordRequest(_message.Message):
    __slots__ = ("user_ids", "new", "old", "revoke_all_access")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    NEW_FIELD_NUMBER: _ClassVar[int]
    OLD_FIELD_NUMBER: _ClassVar[int]
    REVOKE_ALL_ACCESS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    new: str
    old: str
    revoke_all_access: bool
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., new: _Optional[str] = ..., old: _Optional[str] = ..., revoke_all_access: bool = ...) -> None: ...

class ListUserAPIKeysRequest(_message.Message):
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

class GetUserAPIKeyRequest(_message.Message):
    __slots__ = ("user_ids", "key_id")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    key_id: str
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class CreateUserAPIKeyRequest(_message.Message):
    __slots__ = ("user_ids", "name", "rights", "expires_at")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RIGHTS_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    name: str
    rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., name: _Optional[str] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateUserAPIKeyRequest(_message.Message):
    __slots__ = ("user_ids", "api_key", "field_mask")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    api_key: _rights_pb2.APIKey
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., api_key: _Optional[_Union[_rights_pb2.APIKey, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteUserAPIKeyRequest(_message.Message):
    __slots__ = ("user_ids", "key_id")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    key_id: str
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., key_id: _Optional[str] = ...) -> None: ...

class Invitation(_message.Message):
    __slots__ = ("email", "token", "expires_at", "created_at", "updated_at", "accepted_at", "accepted_by")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    ACCEPTED_BY_FIELD_NUMBER: _ClassVar[int]
    email: str
    token: str
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    accepted_at: _timestamp_pb2.Timestamp
    accepted_by: _identifiers_pb2.UserIdentifiers
    def __init__(self, email: _Optional[str] = ..., token: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., accepted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., accepted_by: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ...) -> None: ...

class ListInvitationsRequest(_message.Message):
    __slots__ = ("limit", "page")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    limit: int
    page: int
    def __init__(self, limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class Invitations(_message.Message):
    __slots__ = ("invitations",)
    INVITATIONS_FIELD_NUMBER: _ClassVar[int]
    invitations: _containers.RepeatedCompositeFieldContainer[Invitation]
    def __init__(self, invitations: _Optional[_Iterable[_Union[Invitation, _Mapping]]] = ...) -> None: ...

class SendInvitationRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class DeleteInvitationRequest(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class UserSessionIdentifiers(_message.Message):
    __slots__ = ("user_ids", "session_id")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    session_id: str
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...

class UserSession(_message.Message):
    __slots__ = ("user_ids", "session_id", "created_at", "updated_at", "expires_at", "session_secret")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    SESSION_SECRET_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    session_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    session_secret: str
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., session_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., session_secret: _Optional[str] = ...) -> None: ...

class UserSessions(_message.Message):
    __slots__ = ("sessions",)
    SESSIONS_FIELD_NUMBER: _ClassVar[int]
    sessions: _containers.RepeatedCompositeFieldContainer[UserSession]
    def __init__(self, sessions: _Optional[_Iterable[_Union[UserSession, _Mapping]]] = ...) -> None: ...

class ListUserSessionsRequest(_message.Message):
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

class LoginToken(_message.Message):
    __slots__ = ("user_ids", "created_at", "updated_at", "expires_at", "token", "used")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    token: str
    used: bool
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., token: _Optional[str] = ..., used: bool = ...) -> None: ...

class CreateLoginTokenRequest(_message.Message):
    __slots__ = ("user_ids", "skip_email")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    SKIP_EMAIL_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    skip_email: bool
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., skip_email: bool = ...) -> None: ...

class CreateLoginTokenResponse(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class UserBookmark(_message.Message):
    __slots__ = ("user_ids", "entity_ids", "created_at")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    entity_ids: _identifiers_pb2.EntityIdentifiers
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., entity_ids: _Optional[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UserBookmarks(_message.Message):
    __slots__ = ("bookmarks",)
    BOOKMARKS_FIELD_NUMBER: _ClassVar[int]
    bookmarks: _containers.RepeatedCompositeFieldContainer[UserBookmark]
    def __init__(self, bookmarks: _Optional[_Iterable[_Union[UserBookmark, _Mapping]]] = ...) -> None: ...

class CreateUserBookmarkRequest(_message.Message):
    __slots__ = ("user_ids", "entity_ids")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    entity_ids: _identifiers_pb2.EntityIdentifiers
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., entity_ids: _Optional[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]] = ...) -> None: ...

class ListUserBookmarksRequest(_message.Message):
    __slots__ = ("user_ids", "limit", "page", "order", "deleted", "entity_types")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    limit: int
    page: int
    order: str
    deleted: bool
    entity_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., order: _Optional[str] = ..., deleted: bool = ..., entity_types: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteUserBookmarkRequest(_message.Message):
    __slots__ = ("user_ids", "entity_ids")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    entity_ids: _identifiers_pb2.EntityIdentifiers
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., entity_ids: _Optional[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]] = ...) -> None: ...

class BatchDeleteUserBookmarksRequest(_message.Message):
    __slots__ = ("user_ids", "entity_ids")
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    user_ids: _identifiers_pb2.UserIdentifiers
    entity_ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.EntityIdentifiers]
    def __init__(self, user_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., entity_ids: _Optional[_Iterable[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]]] = ...) -> None: ...
