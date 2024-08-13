from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1_1
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import lorawan_pb2 as _lorawan_pb2
from ttn.lorawan.v3 import messages_pb2 as _messages_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerateDevAddrResponse(_message.Message):
    __slots__ = ("dev_addr",)
    DEV_ADDR_FIELD_NUMBER: _ClassVar[int]
    dev_addr: bytes
    def __init__(self, dev_addr: _Optional[bytes] = ...) -> None: ...

class GetDefaultMACSettingsRequest(_message.Message):
    __slots__ = ("frequency_plan_id", "lorawan_phy_version")
    FREQUENCY_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    LORAWAN_PHY_VERSION_FIELD_NUMBER: _ClassVar[int]
    frequency_plan_id: str
    lorawan_phy_version: _lorawan_pb2.PHYVersion
    def __init__(self, frequency_plan_id: _Optional[str] = ..., lorawan_phy_version: _Optional[_Union[_lorawan_pb2.PHYVersion, str]] = ...) -> None: ...

class GetNetIDResponse(_message.Message):
    __slots__ = ("net_id",)
    NET_ID_FIELD_NUMBER: _ClassVar[int]
    net_id: bytes
    def __init__(self, net_id: _Optional[bytes] = ...) -> None: ...

class GetDeviceAdressPrefixesResponse(_message.Message):
    __slots__ = ("dev_addr_prefixes",)
    DEV_ADDR_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    dev_addr_prefixes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, dev_addr_prefixes: _Optional[_Iterable[bytes]] = ...) -> None: ...
