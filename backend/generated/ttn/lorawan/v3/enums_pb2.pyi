from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DownlinkPathConstraint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOWNLINK_PATH_CONSTRAINT_NONE: _ClassVar[DownlinkPathConstraint]
    DOWNLINK_PATH_CONSTRAINT_PREFER_OTHER: _ClassVar[DownlinkPathConstraint]
    DOWNLINK_PATH_CONSTRAINT_NEVER: _ClassVar[DownlinkPathConstraint]

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_REQUESTED: _ClassVar[State]
    STATE_APPROVED: _ClassVar[State]
    STATE_REJECTED: _ClassVar[State]
    STATE_FLAGGED: _ClassVar[State]
    STATE_SUSPENDED: _ClassVar[State]

class ClusterRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[ClusterRole]
    ENTITY_REGISTRY: _ClassVar[ClusterRole]
    ACCESS: _ClassVar[ClusterRole]
    GATEWAY_SERVER: _ClassVar[ClusterRole]
    NETWORK_SERVER: _ClassVar[ClusterRole]
    APPLICATION_SERVER: _ClassVar[ClusterRole]
    JOIN_SERVER: _ClassVar[ClusterRole]
    CRYPTO_SERVER: _ClassVar[ClusterRole]
    DEVICE_TEMPLATE_CONVERTER: _ClassVar[ClusterRole]
    DEVICE_CLAIMING_SERVER: _ClassVar[ClusterRole]
    GATEWAY_CONFIGURATION_SERVER: _ClassVar[ClusterRole]
    QR_CODE_GENERATOR: _ClassVar[ClusterRole]
    PACKET_BROKER_AGENT: _ClassVar[ClusterRole]
    DEVICE_REPOSITORY: _ClassVar[ClusterRole]
DOWNLINK_PATH_CONSTRAINT_NONE: DownlinkPathConstraint
DOWNLINK_PATH_CONSTRAINT_PREFER_OTHER: DownlinkPathConstraint
DOWNLINK_PATH_CONSTRAINT_NEVER: DownlinkPathConstraint
STATE_REQUESTED: State
STATE_APPROVED: State
STATE_REJECTED: State
STATE_FLAGGED: State
STATE_SUSPENDED: State
NONE: ClusterRole
ENTITY_REGISTRY: ClusterRole
ACCESS: ClusterRole
GATEWAY_SERVER: ClusterRole
NETWORK_SERVER: ClusterRole
APPLICATION_SERVER: ClusterRole
JOIN_SERVER: ClusterRole
CRYPTO_SERVER: ClusterRole
DEVICE_TEMPLATE_CONVERTER: ClusterRole
DEVICE_CLAIMING_SERVER: ClusterRole
GATEWAY_CONFIGURATION_SERVER: ClusterRole
QR_CODE_GENERATOR: ClusterRole
PACKET_BROKER_AGENT: ClusterRole
DEVICE_REPOSITORY: ClusterRole
