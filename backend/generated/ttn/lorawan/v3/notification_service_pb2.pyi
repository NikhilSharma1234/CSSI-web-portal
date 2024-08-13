from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1_1
from ttn.lorawan.v3 import enums_pb2 as _enums_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationReceiver(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_RECEIVER_UNKNOWN: _ClassVar[NotificationReceiver]
    NOTIFICATION_RECEIVER_COLLABORATOR: _ClassVar[NotificationReceiver]
    NOTIFICATION_RECEIVER_ADMINISTRATIVE_CONTACT: _ClassVar[NotificationReceiver]
    NOTIFICATION_RECEIVER_TECHNICAL_CONTACT: _ClassVar[NotificationReceiver]

class NotificationStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_STATUS_UNSEEN: _ClassVar[NotificationStatus]
    NOTIFICATION_STATUS_SEEN: _ClassVar[NotificationStatus]
    NOTIFICATION_STATUS_ARCHIVED: _ClassVar[NotificationStatus]
NOTIFICATION_RECEIVER_UNKNOWN: NotificationReceiver
NOTIFICATION_RECEIVER_COLLABORATOR: NotificationReceiver
NOTIFICATION_RECEIVER_ADMINISTRATIVE_CONTACT: NotificationReceiver
NOTIFICATION_RECEIVER_TECHNICAL_CONTACT: NotificationReceiver
NOTIFICATION_STATUS_UNSEEN: NotificationStatus
NOTIFICATION_STATUS_SEEN: NotificationStatus
NOTIFICATION_STATUS_ARCHIVED: NotificationStatus

class Notification(_message.Message):
    __slots__ = ("id", "created_at", "entity_ids", "notification_type", "data", "sender_ids", "receivers", "email", "status", "status_updated_at")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SENDER_IDS_FIELD_NUMBER: _ClassVar[int]
    RECEIVERS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    entity_ids: _identifiers_pb2.EntityIdentifiers
    notification_type: str
    data: _any_pb2.Any
    sender_ids: _identifiers_pb2.UserIdentifiers
    receivers: _containers.RepeatedScalarFieldContainer[NotificationReceiver]
    email: bool
    status: NotificationStatus
    status_updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., entity_ids: _Optional[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]] = ..., notification_type: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., sender_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., receivers: _Optional[_Iterable[_Union[NotificationReceiver, str]]] = ..., email: bool = ..., status: _Optional[_Union[NotificationStatus, str]] = ..., status_updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateNotificationRequest(_message.Message):
    __slots__ = ("entity_ids", "notification_type", "data", "sender_ids", "receivers", "email")
    ENTITY_IDS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SENDER_IDS_FIELD_NUMBER: _ClassVar[int]
    RECEIVERS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    entity_ids: _identifiers_pb2.EntityIdentifiers
    notification_type: str
    data: _any_pb2.Any
    sender_ids: _identifiers_pb2.UserIdentifiers
    receivers: _containers.RepeatedScalarFieldContainer[NotificationReceiver]
    email: bool
    def __init__(self, entity_ids: _Optional[_Union[_identifiers_pb2.EntityIdentifiers, _Mapping]] = ..., notification_type: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., sender_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., receivers: _Optional[_Iterable[_Union[NotificationReceiver, str]]] = ..., email: bool = ...) -> None: ...

class CreateNotificationResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ListNotificationsRequest(_message.Message):
    __slots__ = ("receiver_ids", "status", "limit", "page")
    RECEIVER_IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    receiver_ids: _identifiers_pb2.UserIdentifiers
    status: _containers.RepeatedScalarFieldContainer[NotificationStatus]
    limit: int
    page: int
    def __init__(self, receiver_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., status: _Optional[_Iterable[_Union[NotificationStatus, str]]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class ListNotificationsResponse(_message.Message):
    __slots__ = ("notifications",)
    NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    notifications: _containers.RepeatedCompositeFieldContainer[Notification]
    def __init__(self, notifications: _Optional[_Iterable[_Union[Notification, _Mapping]]] = ...) -> None: ...

class UpdateNotificationStatusRequest(_message.Message):
    __slots__ = ("receiver_ids", "ids", "status")
    RECEIVER_IDS_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    receiver_ids: _identifiers_pb2.UserIdentifiers
    ids: _containers.RepeatedScalarFieldContainer[str]
    status: NotificationStatus
    def __init__(self, receiver_ids: _Optional[_Union[_identifiers_pb2.UserIdentifiers, _Mapping]] = ..., ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[NotificationStatus, str]] = ...) -> None: ...

class EntityStateChangedNotification(_message.Message):
    __slots__ = ("state", "state_description")
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    state: _enums_pb2.State
    state_description: str
    def __init__(self, state: _Optional[_Union[_enums_pb2.State, str]] = ..., state_description: _Optional[str] = ...) -> None: ...
