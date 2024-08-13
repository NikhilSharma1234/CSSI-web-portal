from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GatewayToken(_message.Message):
    __slots__ = ("key_id", "payload", "checksum")
    class Payload(_message.Message):
        __slots__ = ("gateway_ids", "rights", "created_at")
        GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
        RIGHTS_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        gateway_ids: _identifiers_pb2.GatewayIdentifiers
        rights: _rights_pb2.Rights
        created_at: _timestamp_pb2.Timestamp
        def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., rights: _Optional[_Union[_rights_pb2.Rights, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    payload: GatewayToken.Payload
    checksum: bytes
    def __init__(self, key_id: _Optional[str] = ..., payload: _Optional[_Union[GatewayToken.Payload, _Mapping]] = ..., checksum: _Optional[bytes] = ...) -> None: ...
