from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import error_pb2 as _error_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClaimEndDeviceRequest(_message.Message):
    __slots__ = ("authenticated_identifiers", "qr_code", "target_application_ids", "target_device_id")
    class AuthenticatedIdentifiers(_message.Message):
        __slots__ = ("join_eui", "dev_eui", "authentication_code")
        JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
        DEV_EUI_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_CODE_FIELD_NUMBER: _ClassVar[int]
        join_eui: bytes
        dev_eui: bytes
        authentication_code: str
        def __init__(self, join_eui: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ..., authentication_code: _Optional[str] = ...) -> None: ...
    AUTHENTICATED_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_FIELD_NUMBER: _ClassVar[int]
    TARGET_APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    authenticated_identifiers: ClaimEndDeviceRequest.AuthenticatedIdentifiers
    qr_code: bytes
    target_application_ids: _identifiers_pb2.ApplicationIdentifiers
    target_device_id: str
    def __init__(self, authenticated_identifiers: _Optional[_Union[ClaimEndDeviceRequest.AuthenticatedIdentifiers, _Mapping]] = ..., qr_code: _Optional[bytes] = ..., target_application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., target_device_id: _Optional[str] = ...) -> None: ...

class AuthorizeApplicationRequest(_message.Message):
    __slots__ = ("application_ids", "api_key")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    api_key: str
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., api_key: _Optional[str] = ...) -> None: ...

class GetInfoByJoinEUIRequest(_message.Message):
    __slots__ = ("join_eui",)
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    join_eui: bytes
    def __init__(self, join_eui: _Optional[bytes] = ...) -> None: ...

class GetInfoByJoinEUIResponse(_message.Message):
    __slots__ = ("join_eui", "supports_claiming")
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLAIMING_FIELD_NUMBER: _ClassVar[int]
    join_eui: bytes
    supports_claiming: bool
    def __init__(self, join_eui: _Optional[bytes] = ..., supports_claiming: bool = ...) -> None: ...

class GetInfoByJoinEUIsRequest(_message.Message):
    __slots__ = ("requests",)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[GetInfoByJoinEUIRequest]
    def __init__(self, requests: _Optional[_Iterable[_Union[GetInfoByJoinEUIRequest, _Mapping]]] = ...) -> None: ...

class GetInfoByJoinEUIsResponse(_message.Message):
    __slots__ = ("infos",)
    INFOS_FIELD_NUMBER: _ClassVar[int]
    infos: _containers.RepeatedCompositeFieldContainer[GetInfoByJoinEUIResponse]
    def __init__(self, infos: _Optional[_Iterable[_Union[GetInfoByJoinEUIResponse, _Mapping]]] = ...) -> None: ...

class GetClaimStatusResponse(_message.Message):
    __slots__ = ("end_device_ids", "home_net_id", "home_ns_id", "vendor_specific")
    class VendorSpecific(_message.Message):
        __slots__ = ("organization_unique_identifier", "data")
        ORGANIZATION_UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        organization_unique_identifier: int
        data: _struct_pb2.Struct
        def __init__(self, organization_unique_identifier: _Optional[int] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    HOME_NET_ID_FIELD_NUMBER: _ClassVar[int]
    HOME_NS_ID_FIELD_NUMBER: _ClassVar[int]
    VENDOR_SPECIFIC_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    home_net_id: bytes
    home_ns_id: bytes
    vendor_specific: GetClaimStatusResponse.VendorSpecific
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., home_net_id: _Optional[bytes] = ..., home_ns_id: _Optional[bytes] = ..., vendor_specific: _Optional[_Union[GetClaimStatusResponse.VendorSpecific, _Mapping]] = ...) -> None: ...

class BatchUnclaimEndDevicesRequest(_message.Message):
    __slots__ = ("application_ids", "device_ids")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    device_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., device_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchUnclaimEndDevicesResponse(_message.Message):
    __slots__ = ("application_ids", "failed")
    class FailedEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _error_pb2.ErrorDetails
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_error_pb2.ErrorDetails, _Mapping]] = ...) -> None: ...
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    failed: _containers.MessageMap[str, _error_pb2.ErrorDetails]
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., failed: _Optional[_Mapping[str, _error_pb2.ErrorDetails]] = ...) -> None: ...

class CUPSRedirection(_message.Message):
    __slots__ = ("target_cups_uri", "current_gateway_key", "target_cups_trust", "client_tls", "auth_token")
    class ClientTLS(_message.Message):
        __slots__ = ("cert", "key")
        CERT_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        cert: bytes
        key: bytes
        def __init__(self, cert: _Optional[bytes] = ..., key: _Optional[bytes] = ...) -> None: ...
    TARGET_CUPS_URI_FIELD_NUMBER: _ClassVar[int]
    CURRENT_GATEWAY_KEY_FIELD_NUMBER: _ClassVar[int]
    TARGET_CUPS_TRUST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_TLS_FIELD_NUMBER: _ClassVar[int]
    AUTH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    target_cups_uri: str
    current_gateway_key: str
    target_cups_trust: bytes
    client_tls: CUPSRedirection.ClientTLS
    auth_token: str
    def __init__(self, target_cups_uri: _Optional[str] = ..., current_gateway_key: _Optional[str] = ..., target_cups_trust: _Optional[bytes] = ..., client_tls: _Optional[_Union[CUPSRedirection.ClientTLS, _Mapping]] = ..., auth_token: _Optional[str] = ...) -> None: ...

class ClaimGatewayRequest(_message.Message):
    __slots__ = ("authenticated_identifiers", "qr_code", "collaborator", "target_gateway_id", "target_gateway_server_address", "cups_redirection", "target_frequency_plan_id", "target_frequency_plan_ids")
    class AuthenticatedIdentifiers(_message.Message):
        __slots__ = ("gateway_eui", "authentication_code")
        GATEWAY_EUI_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_CODE_FIELD_NUMBER: _ClassVar[int]
        gateway_eui: bytes
        authentication_code: bytes
        def __init__(self, gateway_eui: _Optional[bytes] = ..., authentication_code: _Optional[bytes] = ...) -> None: ...
    AUTHENTICATED_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_FIELD_NUMBER: _ClassVar[int]
    COLLABORATOR_FIELD_NUMBER: _ClassVar[int]
    TARGET_GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_GATEWAY_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CUPS_REDIRECTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FREQUENCY_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FREQUENCY_PLAN_IDS_FIELD_NUMBER: _ClassVar[int]
    authenticated_identifiers: ClaimGatewayRequest.AuthenticatedIdentifiers
    qr_code: bytes
    collaborator: _identifiers_pb2.OrganizationOrUserIdentifiers
    target_gateway_id: str
    target_gateway_server_address: str
    cups_redirection: CUPSRedirection
    target_frequency_plan_id: str
    target_frequency_plan_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, authenticated_identifiers: _Optional[_Union[ClaimGatewayRequest.AuthenticatedIdentifiers, _Mapping]] = ..., qr_code: _Optional[bytes] = ..., collaborator: _Optional[_Union[_identifiers_pb2.OrganizationOrUserIdentifiers, _Mapping]] = ..., target_gateway_id: _Optional[str] = ..., target_gateway_server_address: _Optional[str] = ..., cups_redirection: _Optional[_Union[CUPSRedirection, _Mapping]] = ..., target_frequency_plan_id: _Optional[str] = ..., target_frequency_plan_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AuthorizeGatewayRequest(_message.Message):
    __slots__ = ("gateway_ids", "api_key")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    api_key: str
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., api_key: _Optional[str] = ...) -> None: ...

class GetInfoByGatewayEUIRequest(_message.Message):
    __slots__ = ("eui",)
    EUI_FIELD_NUMBER: _ClassVar[int]
    eui: bytes
    def __init__(self, eui: _Optional[bytes] = ...) -> None: ...

class GetInfoByGatewayEUIResponse(_message.Message):
    __slots__ = ("eui", "supports_claiming", "is_managed")
    EUI_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_CLAIMING_FIELD_NUMBER: _ClassVar[int]
    IS_MANAGED_FIELD_NUMBER: _ClassVar[int]
    eui: bytes
    supports_claiming: bool
    is_managed: bool
    def __init__(self, eui: _Optional[bytes] = ..., supports_claiming: bool = ..., is_managed: bool = ...) -> None: ...
