from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1_1
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import join_pb2 as _join_pb2
from ttn.lorawan.v3 import keys_pb2 as _keys_pb2
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionKeyRequest(_message.Message):
    __slots__ = ("session_key_id", "dev_eui", "join_eui")
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    DEV_EUI_FIELD_NUMBER: _ClassVar[int]
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    session_key_id: bytes
    dev_eui: bytes
    join_eui: bytes
    def __init__(self, session_key_id: _Optional[bytes] = ..., dev_eui: _Optional[bytes] = ..., join_eui: _Optional[bytes] = ...) -> None: ...

class NwkSKeysResponse(_message.Message):
    __slots__ = ("f_nwk_s_int_key", "s_nwk_s_int_key", "nwk_s_enc_key")
    F_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    S_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    NWK_S_ENC_KEY_FIELD_NUMBER: _ClassVar[int]
    f_nwk_s_int_key: _keys_pb2.KeyEnvelope
    s_nwk_s_int_key: _keys_pb2.KeyEnvelope
    nwk_s_enc_key: _keys_pb2.KeyEnvelope
    def __init__(self, f_nwk_s_int_key: _Optional[_Union[_keys_pb2.KeyEnvelope, _Mapping]] = ..., s_nwk_s_int_key: _Optional[_Union[_keys_pb2.KeyEnvelope, _Mapping]] = ..., nwk_s_enc_key: _Optional[_Union[_keys_pb2.KeyEnvelope, _Mapping]] = ...) -> None: ...

class AppSKeyResponse(_message.Message):
    __slots__ = ("app_s_key",)
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    app_s_key: _keys_pb2.KeyEnvelope
    def __init__(self, app_s_key: _Optional[_Union[_keys_pb2.KeyEnvelope, _Mapping]] = ...) -> None: ...

class CryptoServicePayloadRequest(_message.Message):
    __slots__ = ("ids", "lorawan_version", "payload", "provisioner_id", "provisioning_data")
    IDS_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_VERSION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_DATA_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.EndDeviceIdentifiers
    lorawan_version: _lorawan_pb2.MACVersion
    payload: bytes
    provisioner_id: str
    provisioning_data: _struct_pb2.Struct
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., lorawan_version: _Optional[_Union[_lorawan_pb2.MACVersion, str]] = ..., payload: _Optional[bytes] = ..., provisioner_id: _Optional[str] = ..., provisioning_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CryptoServicePayloadResponse(_message.Message):
    __slots__ = ("payload",)
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    def __init__(self, payload: _Optional[bytes] = ...) -> None: ...

class JoinAcceptMICRequest(_message.Message):
    __slots__ = ("payload_request", "join_request_type", "dev_nonce")
    PAYLOAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
    JOIN_REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEV_NONCE_FIELD_NUMBER: _ClassVar[int]
    payload_request: CryptoServicePayloadRequest
    join_request_type: _lorawan_pb2.JoinRequestType
    dev_nonce: bytes
    def __init__(self, payload_request: _Optional[_Union[CryptoServicePayloadRequest, _Mapping]] = ..., join_request_type: _Optional[_Union[_lorawan_pb2.JoinRequestType, str]] = ..., dev_nonce: _Optional[bytes] = ...) -> None: ...

class DeriveSessionKeysRequest(_message.Message):
    __slots__ = ("ids", "lorawan_version", "join_nonce", "dev_nonce", "net_id", "provisioner_id", "provisioning_data")
    IDS_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_VERSION_FIELD_NUMBER: _ClassVar[int]
    JOIN_NONCE_FIELD_NUMBER: _ClassVar[int]
    DEV_NONCE_FIELD_NUMBER: _ClassVar[int]
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_DATA_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.EndDeviceIdentifiers
    lorawan_version: _lorawan_pb2.MACVersion
    join_nonce: bytes
    dev_nonce: bytes
    net_id: bytes
    provisioner_id: str
    provisioning_data: _struct_pb2.Struct
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., lorawan_version: _Optional[_Union[_lorawan_pb2.MACVersion, str]] = ..., join_nonce: _Optional[bytes] = ..., dev_nonce: _Optional[bytes] = ..., net_id: _Optional[bytes] = ..., provisioner_id: _Optional[str] = ..., provisioning_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class GetRootKeysRequest(_message.Message):
    __slots__ = ("ids", "provisioner_id", "provisioning_data")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_DATA_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.EndDeviceIdentifiers
    provisioner_id: str
    provisioning_data: _struct_pb2.Struct
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., provisioner_id: _Optional[str] = ..., provisioning_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ProvisionEndDevicesRequest(_message.Message):
    __slots__ = ("application_ids", "provisioner_id", "provisioning_data", "list", "range", "from_data")
    class IdentifiersList(_message.Message):
        __slots__ = ("join_eui", "end_device_ids")
        JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
        END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
        join_eui: bytes
        end_device_ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.EndDeviceIdentifiers]
        def __init__(self, join_eui: _Optional[bytes] = ..., end_device_ids: _Optional[_Iterable[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]]] = ...) -> None: ...
    class IdentifiersRange(_message.Message):
        __slots__ = ("join_eui", "start_dev_eui")
        JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
        START_DEV_EUI_FIELD_NUMBER: _ClassVar[int]
        join_eui: bytes
        start_dev_eui: bytes
        def __init__(self, join_eui: _Optional[bytes] = ..., start_dev_eui: _Optional[bytes] = ...) -> None: ...
    class IdentifiersFromData(_message.Message):
        __slots__ = ("join_eui",)
        JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
        join_eui: bytes
        def __init__(self, join_eui: _Optional[bytes] = ...) -> None: ...
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    PROVISIONER_ID_FIELD_NUMBER: _ClassVar[int]
    PROVISIONING_DATA_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    FROM_DATA_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    provisioner_id: str
    provisioning_data: bytes
    list: ProvisionEndDevicesRequest.IdentifiersList
    range: ProvisionEndDevicesRequest.IdentifiersRange
    from_data: ProvisionEndDevicesRequest.IdentifiersFromData
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., provisioner_id: _Optional[str] = ..., provisioning_data: _Optional[bytes] = ..., list: _Optional[_Union[ProvisionEndDevicesRequest.IdentifiersList, _Mapping]] = ..., range: _Optional[_Union[ProvisionEndDevicesRequest.IdentifiersRange, _Mapping]] = ..., from_data: _Optional[_Union[ProvisionEndDevicesRequest.IdentifiersFromData, _Mapping]] = ...) -> None: ...

class ApplicationActivationSettings(_message.Message):
    __slots__ = ("kek_label", "kek", "home_net_id", "application_server_id")
    KEK_LABEL_FIELD_NUMBER: _ClassVar[int]
    KEK_FIELD_NUMBER: _ClassVar[int]
    HOME_NET_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_SERVER_ID_FIELD_NUMBER: _ClassVar[int]
    kek_label: str
    kek: _keys_pb2.KeyEnvelope
    home_net_id: bytes
    application_server_id: str
    def __init__(self, kek_label: _Optional[str] = ..., kek: _Optional[_Union[_keys_pb2.KeyEnvelope, _Mapping]] = ..., home_net_id: _Optional[bytes] = ..., application_server_id: _Optional[str] = ...) -> None: ...

class GetApplicationActivationSettingsRequest(_message.Message):
    __slots__ = ("application_ids", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetApplicationActivationSettingsRequest(_message.Message):
    __slots__ = ("application_ids", "settings", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    settings: ApplicationActivationSettings
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., settings: _Optional[_Union[ApplicationActivationSettings, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class DeleteApplicationActivationSettingsRequest(_message.Message):
    __slots__ = ("application_ids",)
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ...) -> None: ...

class JoinEUIPrefix(_message.Message):
    __slots__ = ("join_eui", "length")
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    join_eui: bytes
    length: int
    def __init__(self, join_eui: _Optional[bytes] = ..., length: _Optional[int] = ...) -> None: ...

class JoinEUIPrefixes(_message.Message):
    __slots__ = ("prefixes",)
    PREFIXES_FIELD_NUMBER: _ClassVar[int]
    prefixes: _containers.RepeatedCompositeFieldContainer[JoinEUIPrefix]
    def __init__(self, prefixes: _Optional[_Iterable[_Union[JoinEUIPrefix, _Mapping]]] = ...) -> None: ...

class GetDefaultJoinEUIResponse(_message.Message):
    __slots__ = ("join_eui",)
    JOIN_EUI_FIELD_NUMBER: _ClassVar[int]
    join_eui: bytes
    def __init__(self, join_eui: _Optional[bytes] = ...) -> None: ...
