from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import oauth_pb2 as _oauth_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from ttn.lorawan.v3 import user_pb2 as _user_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthInfoResponse(_message.Message):
    __slots__ = ("api_key", "oauth_access_token", "user_session", "gateway_token", "universal_rights", "is_admin")
    class APIKeyAccess(_message.Message):
        __slots__ = ("api_key", "entity_ids")
        API_KEY_FIELD_NUMBER: _ClassVar[int]
        ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
        api_key: _rights_pb2.APIKey
        entity_ids: _identifiers_pb2.EntityIdentifiers
        def __init__(self, api_key: _Optional[_Union[_rights_pb2.APIKey, _Mapping]] = ..., entity_ids: _Optional[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]] = ...) -> None: ...
    class GatewayToken(_message.Message):
        __slots__ = ("gateway_ids", "rights")
        GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
        RIGHTS_FIELD_NUMBER: _ClassVar[int]
        gateway_ids: _identifiers_pb2.GatewayIdentifiers
        rights: _containers.RepeatedScalarFieldContainer[_rights_pb2.Right]
        def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., rights: _Optional[_Iterable[_Union[_rights_pb2.Right, str]]] = ...) -> None: ...
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    OAUTH_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_SESSION_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNIVERSAL_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    api_key: AuthInfoResponse.APIKeyAccess
    oauth_access_token: _oauth_pb2.OAuthAccessToken
    user_session: _user_pb2.UserSession
    gateway_token: AuthInfoResponse.GatewayToken
    universal_rights: _rights_pb2.Rights
    is_admin: bool
    def __init__(self, api_key: _Optional[_Union[AuthInfoResponse.APIKeyAccess, _Mapping]] = ..., oauth_access_token: _Optional[_Union[_oauth_pb2.OAuthAccessToken, _Mapping]] = ..., user_session: _Optional[_Union[_user_pb2.UserSession, _Mapping]] = ..., gateway_token: _Optional[_Union[AuthInfoResponse.GatewayToken, _Mapping]] = ..., universal_rights: _Optional[_Union[_rights_pb2.Rights, _Mapping]] = ..., is_admin: bool = ...) -> None: ...

class GetIsConfigurationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class IsConfiguration(_message.Message):
    __slots__ = ("user_registration", "profile_picture", "end_device_picture", "user_rights", "user_login", "admin_rights", "collaborator_rights")
    class UserRegistration(_message.Message):
        __slots__ = ("invitation", "contact_info_validation", "admin_approval", "password_requirements", "enabled")
        class Invitation(_message.Message):
            __slots__ = ("required", "token_ttl")
            REQUIRED_FIELD_NUMBER: _ClassVar[int]
            TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
            required: _wrappers_pb2.BoolValue
            token_ttl: _duration_pb2.Duration
            def __init__(self, required: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., token_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class ContactInfoValidation(_message.Message):
            __slots__ = ("required", "token_ttl", "retry_interval")
            REQUIRED_FIELD_NUMBER: _ClassVar[int]
            TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
            RETRY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
            required: _wrappers_pb2.BoolValue
            token_ttl: _duration_pb2.Duration
            retry_interval: _duration_pb2.Duration
            def __init__(self, required: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., token_ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., retry_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class AdminApproval(_message.Message):
            __slots__ = ("required",)
            REQUIRED_FIELD_NUMBER: _ClassVar[int]
            required: _wrappers_pb2.BoolValue
            def __init__(self, required: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
        class PasswordRequirements(_message.Message):
            __slots__ = ("min_length", "max_length", "min_uppercase", "min_digits", "min_special")
            MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
            MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
            MIN_UPPERCASE_FIELD_NUMBER: _ClassVar[int]
            MIN_DIGITS_FIELD_NUMBER: _ClassVar[int]
            MIN_SPECIAL_FIELD_NUMBER: _ClassVar[int]
            min_length: _wrappers_pb2.UInt32Value
            max_length: _wrappers_pb2.UInt32Value
            min_uppercase: _wrappers_pb2.UInt32Value
            min_digits: _wrappers_pb2.UInt32Value
            min_special: _wrappers_pb2.UInt32Value
            def __init__(self, min_length: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., max_length: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., min_uppercase: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., min_digits: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., min_special: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...
        INVITATION_FIELD_NUMBER: _ClassVar[int]
        CONTACT_INFO_VALIDATION_FIELD_NUMBER: _ClassVar[int]
        ADMIN_APPROVAL_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        invitation: IsConfiguration.UserRegistration.Invitation
        contact_info_validation: IsConfiguration.UserRegistration.ContactInfoValidation
        admin_approval: IsConfiguration.UserRegistration.AdminApproval
        password_requirements: IsConfiguration.UserRegistration.PasswordRequirements
        enabled: bool
        def __init__(self, invitation: _Optional[_Union[IsConfiguration.UserRegistration.Invitation, _Mapping]] = ..., contact_info_validation: _Optional[_Union[IsConfiguration.UserRegistration.ContactInfoValidation, _Mapping]] = ..., admin_approval: _Optional[_Union[IsConfiguration.UserRegistration.AdminApproval, _Mapping]] = ..., password_requirements: _Optional[_Union[IsConfiguration.UserRegistration.PasswordRequirements, _Mapping]] = ..., enabled: bool = ...) -> None: ...
    class ProfilePicture(_message.Message):
        __slots__ = ("disable_upload", "use_gravatar")
        DISABLE_UPLOAD_FIELD_NUMBER: _ClassVar[int]
        USE_GRAVATAR_FIELD_NUMBER: _ClassVar[int]
        disable_upload: _wrappers_pb2.BoolValue
        use_gravatar: _wrappers_pb2.BoolValue
        def __init__(self, disable_upload: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., use_gravatar: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class EndDevicePicture(_message.Message):
        __slots__ = ("disable_upload",)
        DISABLE_UPLOAD_FIELD_NUMBER: _ClassVar[int]
        disable_upload: _wrappers_pb2.BoolValue
        def __init__(self, disable_upload: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class UserRights(_message.Message):
        __slots__ = ("create_applications", "create_clients", "create_gateways", "create_organizations")
        CREATE_APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
        CREATE_CLIENTS_FIELD_NUMBER: _ClassVar[int]
        CREATE_GATEWAYS_FIELD_NUMBER: _ClassVar[int]
        CREATE_ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
        create_applications: _wrappers_pb2.BoolValue
        create_clients: _wrappers_pb2.BoolValue
        create_gateways: _wrappers_pb2.BoolValue
        create_organizations: _wrappers_pb2.BoolValue
        def __init__(self, create_applications: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., create_clients: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., create_gateways: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., create_organizations: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class UserLogin(_message.Message):
        __slots__ = ("disable_credentials_login",)
        DISABLE_CREDENTIALS_LOGIN_FIELD_NUMBER: _ClassVar[int]
        disable_credentials_login: _wrappers_pb2.BoolValue
        def __init__(self, disable_credentials_login: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class AdminRights(_message.Message):
        __slots__ = ("all",)
        ALL_FIELD_NUMBER: _ClassVar[int]
        all: _wrappers_pb2.BoolValue
        def __init__(self, all: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    class CollaboratorRights(_message.Message):
        __slots__ = ("set_others_as_contacts",)
        SET_OTHERS_AS_CONTACTS_FIELD_NUMBER: _ClassVar[int]
        set_others_as_contacts: _wrappers_pb2.BoolValue
        def __init__(self, set_others_as_contacts: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...
    USER_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    USER_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    USER_LOGIN_FIELD_NUMBER: _ClassVar[int]
    ADMIN_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    user_registration: IsConfiguration.UserRegistration
    profile_picture: IsConfiguration.ProfilePicture
    end_device_picture: IsConfiguration.EndDevicePicture
    user_rights: IsConfiguration.UserRights
    user_login: IsConfiguration.UserLogin
    admin_rights: IsConfiguration.AdminRights
    collaborator_rights: IsConfiguration.CollaboratorRights
    def __init__(self, user_registration: _Optional[_Union[IsConfiguration.UserRegistration, _Mapping]] = ..., profile_picture: _Optional[_Union[IsConfiguration.ProfilePicture, _Mapping]] = ..., end_device_picture: _Optional[_Union[IsConfiguration.EndDevicePicture, _Mapping]] = ..., user_rights: _Optional[_Union[IsConfiguration.UserRights, _Mapping]] = ..., user_login: _Optional[_Union[IsConfiguration.UserLogin, _Mapping]] = ..., admin_rights: _Optional[_Union[IsConfiguration.AdminRights, _Mapping]] = ..., collaborator_rights: _Optional[_Union[IsConfiguration.CollaboratorRights, _Mapping]] = ...) -> None: ...

class GetIsConfigurationResponse(_message.Message):
    __slots__ = ("configuration",)
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    configuration: IsConfiguration
    def __init__(self, configuration: _Optional[_Union[IsConfiguration, _Mapping]] = ...) -> None: ...
