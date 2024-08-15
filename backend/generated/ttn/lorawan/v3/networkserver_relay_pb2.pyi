from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRelayRequest(_message.Message):
    __slots__ = ("end_device_ids", "settings")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    settings: _end_device_pb2.RelaySettings
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., settings: _Optional[_Union[_end_device_pb2.RelaySettings, _Mapping]] = ...) -> None: ...

class CreateRelayResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _end_device_pb2.RelaySettings
    def __init__(self, settings: _Optional[_Union[_end_device_pb2.RelaySettings, _Mapping]] = ...) -> None: ...

class GetRelayRequest(_message.Message):
    __slots__ = ("end_device_ids", "field_mask")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetRelayResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _end_device_pb2.RelaySettings
    def __init__(self, settings: _Optional[_Union[_end_device_pb2.RelaySettings, _Mapping]] = ...) -> None: ...

class UpdateRelayRequest(_message.Message):
    __slots__ = ("end_device_ids", "settings", "field_mask")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    settings: _end_device_pb2.RelaySettings
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., settings: _Optional[_Union[_end_device_pb2.RelaySettings, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRelayResponse(_message.Message):
    __slots__ = ("settings",)
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: _end_device_pb2.RelaySettings
    def __init__(self, settings: _Optional[_Union[_end_device_pb2.RelaySettings, _Mapping]] = ...) -> None: ...

class DeleteRelayRequest(_message.Message):
    __slots__ = ("end_device_ids",)
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ...) -> None: ...

class DeleteRelayResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateRelayUplinkForwardingRuleRequest(_message.Message):
    __slots__ = ("end_device_ids", "index", "rule")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    index: int
    rule: _end_device_pb2.RelayUplinkForwardingRule
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., index: _Optional[int] = ..., rule: _Optional[_Union[_end_device_pb2.RelayUplinkForwardingRule, _Mapping]] = ...) -> None: ...

class CreateRelayUplinkForwardingRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: _end_device_pb2.RelayUplinkForwardingRule
    def __init__(self, rule: _Optional[_Union[_end_device_pb2.RelayUplinkForwardingRule, _Mapping]] = ...) -> None: ...

class GetRelayUplinkForwardingRuleRequest(_message.Message):
    __slots__ = ("end_device_ids", "index", "field_mask")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    index: int
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., index: _Optional[int] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetRelayUplinkForwardingRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: _end_device_pb2.RelayUplinkForwardingRule
    def __init__(self, rule: _Optional[_Union[_end_device_pb2.RelayUplinkForwardingRule, _Mapping]] = ...) -> None: ...

class ListRelayUplinkForwardingRulesRequest(_message.Message):
    __slots__ = ("end_device_ids", "field_mask")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListRelayUplinkForwardingRulesResponse(_message.Message):
    __slots__ = ("rules",)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[_end_device_pb2.RelayUplinkForwardingRule]
    def __init__(self, rules: _Optional[_Iterable[_Union[_end_device_pb2.RelayUplinkForwardingRule, _Mapping]]] = ...) -> None: ...

class UpdateRelayUplinkForwardingRuleRequest(_message.Message):
    __slots__ = ("end_device_ids", "index", "rule", "field_mask")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    index: int
    rule: _end_device_pb2.RelayUplinkForwardingRule
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., index: _Optional[int] = ..., rule: _Optional[_Union[_end_device_pb2.RelayUplinkForwardingRule, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateRelayUplinkForwardingRuleResponse(_message.Message):
    __slots__ = ("rule",)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: _end_device_pb2.RelayUplinkForwardingRule
    def __init__(self, rule: _Optional[_Union[_end_device_pb2.RelayUplinkForwardingRule, _Mapping]] = ...) -> None: ...

class DeleteRelayUplinkForwardingRuleRequest(_message.Message):
    __slots__ = ("end_device_ids", "index")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    index: int
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., index: _Optional[int] = ...) -> None: ...

class DeleteRelayUplinkForwardingRuleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
