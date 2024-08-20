from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyEnvelope(_message.Message):
    __slots__ = ("key", "kek_label", "encrypted_key")
    KEY_FIELD_NUMBER: _ClassVar[int]
    KEK_LABEL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_KEY_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    kek_label: str
    encrypted_key: bytes
    def __init__(self, key: _Optional[bytes] = ..., kek_label: _Optional[str] = ..., encrypted_key: _Optional[bytes] = ...) -> None: ...

class RootKeys(_message.Message):
    __slots__ = ("root_key_id", "app_key", "nwk_key")
    ROOT_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    APP_KEY_FIELD_NUMBER: _ClassVar[int]
    NWK_KEY_FIELD_NUMBER: _ClassVar[int]
    root_key_id: str
    app_key: KeyEnvelope
    nwk_key: KeyEnvelope
    def __init__(self, root_key_id: _Optional[str] = ..., app_key: _Optional[_Union[KeyEnvelope, _Mapping]] = ..., nwk_key: _Optional[_Union[KeyEnvelope, _Mapping]] = ...) -> None: ...

class SessionKeys(_message.Message):
    __slots__ = ("session_key_id", "f_nwk_s_int_key", "s_nwk_s_int_key", "nwk_s_enc_key", "app_s_key")
    SESSION_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    F_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    S_NWK_S_INT_KEY_FIELD_NUMBER: _ClassVar[int]
    NWK_S_ENC_KEY_FIELD_NUMBER: _ClassVar[int]
    APP_S_KEY_FIELD_NUMBER: _ClassVar[int]
    session_key_id: bytes
    f_nwk_s_int_key: KeyEnvelope
    s_nwk_s_int_key: KeyEnvelope
    nwk_s_enc_key: KeyEnvelope
    app_s_key: KeyEnvelope
    def __init__(self, session_key_id: _Optional[bytes] = ..., f_nwk_s_int_key: _Optional[_Union[KeyEnvelope, _Mapping]] = ..., s_nwk_s_int_key: _Optional[_Union[KeyEnvelope, _Mapping]] = ..., nwk_s_enc_key: _Optional[_Union[KeyEnvelope, _Mapping]] = ..., app_s_key: _Optional[_Union[KeyEnvelope, _Mapping]] = ...) -> None: ...
