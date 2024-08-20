from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from ttn.lorawan.v3 import gateway_pb2 as _gateway_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.ttn.lorawan.v3 import rights_pb2 as _rights_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PullGatewayConfigurationRequest(_message.Message):
    __slots__ = ("gateway_ids", "field_mask")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _identifiers_pb2.GatewayIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, gateway_ids: _Optional[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class AssertGatewayRightsRequest(_message.Message):
    __slots__ = ("gateway_ids", "required")
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.GatewayIdentifiers]
    required: _rights_pb2.Rights
    def __init__(self, gateway_ids: _Optional[_Iterable[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]]] = ..., required: _Optional[_Union[_rights_pb2.Rights, _Mapping]] = ...) -> None: ...

class BatchDeleteGatewaysRequest(_message.Message):
    __slots__ = ("gateway_ids",)
    GATEWAY_IDS_FIELD_NUMBER: _ClassVar[int]
    gateway_ids: _containers.RepeatedCompositeFieldContainer[_identifiers_pb2.GatewayIdentifiers]
    def __init__(self, gateway_ids: _Optional[_Iterable[_Union[_identifiers_pb2.GatewayIdentifiers, _Mapping]]] = ...) -> None: ...
