from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import error_pb2 as _error_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationWebhookIdentifiers(_message.Message):
    __slots__ = ("application_ids", "webhook_id")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    WEBHOOK_ID_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    webhook_id: str
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., webhook_id: _Optional[str] = ...) -> None: ...

class ApplicationWebhookTemplateIdentifiers(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class ApplicationWebhookTemplateField(_message.Message):
    __slots__ = ("id", "name", "description", "secret", "default_value", "optional")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    secret: bool
    default_value: str
    optional: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., secret: bool = ..., default_value: _Optional[str] = ..., optional: bool = ...) -> None: ...

class ApplicationWebhookTemplate(_message.Message):
    __slots__ = ("ids", "name", "description", "logo_url", "info_url", "documentation_url", "base_url", "headers", "format", "fields", "create_downlink_api_key", "uplink_message", "uplink_normalized", "join_accept", "downlink_ack", "downlink_nack", "downlink_sent", "downlink_failed", "downlink_queued", "downlink_queue_invalidated", "location_solved", "service_data", "field_mask")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Message(_message.Message):
        __slots__ = ("path",)
        PATH_FIELD_NUMBER: _ClassVar[int]
        path: str
        def __init__(self, path: _Optional[str] = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    INFO_URL_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_URL_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    CREATE_DOWNLINK_API_KEY_FIELD_NUMBER: _ClassVar[int]
    UPLINK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPLINK_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ACK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_NACK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_SENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FAILED_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_QUEUED_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_QUEUE_INVALIDATED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SOLVED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationWebhookTemplateIdentifiers
    name: str
    description: str
    logo_url: str
    info_url: str
    documentation_url: str
    base_url: str
    headers: _containers.ScalarMap[str, str]
    format: str
    fields: _containers.RepeatedCompositeFieldContainer[ApplicationWebhookTemplateField]
    create_downlink_api_key: bool
    uplink_message: ApplicationWebhookTemplate.Message
    uplink_normalized: ApplicationWebhookTemplate.Message
    join_accept: ApplicationWebhookTemplate.Message
    downlink_ack: ApplicationWebhookTemplate.Message
    downlink_nack: ApplicationWebhookTemplate.Message
    downlink_sent: ApplicationWebhookTemplate.Message
    downlink_failed: ApplicationWebhookTemplate.Message
    downlink_queued: ApplicationWebhookTemplate.Message
    downlink_queue_invalidated: ApplicationWebhookTemplate.Message
    location_solved: ApplicationWebhookTemplate.Message
    service_data: ApplicationWebhookTemplate.Message
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[ApplicationWebhookTemplateIdentifiers, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., logo_url: _Optional[str] = ..., info_url: _Optional[str] = ..., documentation_url: _Optional[str] = ..., base_url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., format: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[ApplicationWebhookTemplateField, _Mapping]]] = ..., create_downlink_api_key: bool = ..., uplink_message: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., uplink_normalized: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., join_accept: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., downlink_ack: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., downlink_nack: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., downlink_sent: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., downlink_failed: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., downlink_queued: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., downlink_queue_invalidated: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., location_solved: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., service_data: _Optional[_Union[ApplicationWebhookTemplate.Message, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ApplicationWebhookTemplates(_message.Message):
    __slots__ = ("templates",)
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[ApplicationWebhookTemplate]
    def __init__(self, templates: _Optional[_Iterable[_Union[ApplicationWebhookTemplate, _Mapping]]] = ...) -> None: ...

class ApplicationWebhookHealth(_message.Message):
    __slots__ = ("healthy", "unhealthy")
    class WebhookHealthStatusHealthy(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class WebhookHealthStatusUnhealthy(_message.Message):
        __slots__ = ("failed_attempts", "last_failed_attempt_at", "last_failed_attempt_details")
        FAILED_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        LAST_FAILED_ATTEMPT_AT_FIELD_NUMBER: _ClassVar[int]
        LAST_FAILED_ATTEMPT_DETAILS_FIELD_NUMBER: _ClassVar[int]
        failed_attempts: int
        last_failed_attempt_at: _timestamp_pb2.Timestamp
        last_failed_attempt_details: _error_pb2.ErrorDetails
        def __init__(self, failed_attempts: _Optional[int] = ..., last_failed_attempt_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_failed_attempt_details: _Optional[_Union[_error_pb2.ErrorDetails, _Mapping]] = ...) -> None: ...
    HEALTHY_FIELD_NUMBER: _ClassVar[int]
    UNHEALTHY_FIELD_NUMBER: _ClassVar[int]
    healthy: ApplicationWebhookHealth.WebhookHealthStatusHealthy
    unhealthy: ApplicationWebhookHealth.WebhookHealthStatusUnhealthy
    def __init__(self, healthy: _Optional[_Union[ApplicationWebhookHealth.WebhookHealthStatusHealthy, _Mapping]] = ..., unhealthy: _Optional[_Union[ApplicationWebhookHealth.WebhookHealthStatusUnhealthy, _Mapping]] = ...) -> None: ...

class ApplicationWebhook(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "base_url", "headers", "format", "template_ids", "template_fields", "downlink_api_key", "uplink_message", "uplink_normalized", "join_accept", "downlink_ack", "downlink_nack", "downlink_sent", "downlink_failed", "downlink_queued", "downlink_queue_invalidated", "location_solved", "service_data", "health_status", "field_mask")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class TemplateFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class Message(_message.Message):
        __slots__ = ("path",)
        PATH_FIELD_NUMBER: _ClassVar[int]
        path: str
        def __init__(self, path: _Optional[str] = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    BASE_URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_IDS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_API_KEY_FIELD_NUMBER: _ClassVar[int]
    UPLINK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPLINK_NORMALIZED_FIELD_NUMBER: _ClassVar[int]
    JOIN_ACCEPT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_ACK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_NACK_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_SENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FAILED_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_QUEUED_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_QUEUE_INVALIDATED_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SOLVED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DATA_FIELD_NUMBER: _ClassVar[int]
    HEALTH_STATUS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationWebhookIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    base_url: str
    headers: _containers.ScalarMap[str, str]
    format: str
    template_ids: ApplicationWebhookTemplateIdentifiers
    template_fields: _containers.ScalarMap[str, str]
    downlink_api_key: str
    uplink_message: ApplicationWebhook.Message
    uplink_normalized: ApplicationWebhook.Message
    join_accept: ApplicationWebhook.Message
    downlink_ack: ApplicationWebhook.Message
    downlink_nack: ApplicationWebhook.Message
    downlink_sent: ApplicationWebhook.Message
    downlink_failed: ApplicationWebhook.Message
    downlink_queued: ApplicationWebhook.Message
    downlink_queue_invalidated: ApplicationWebhook.Message
    location_solved: ApplicationWebhook.Message
    service_data: ApplicationWebhook.Message
    health_status: ApplicationWebhookHealth
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[ApplicationWebhookIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., base_url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., format: _Optional[str] = ..., template_ids: _Optional[_Union[ApplicationWebhookTemplateIdentifiers, _Mapping]] = ..., template_fields: _Optional[_Mapping[str, str]] = ..., downlink_api_key: _Optional[str] = ..., uplink_message: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., uplink_normalized: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., join_accept: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., downlink_ack: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., downlink_nack: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., downlink_sent: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., downlink_failed: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., downlink_queued: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., downlink_queue_invalidated: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., location_solved: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., service_data: _Optional[_Union[ApplicationWebhook.Message, _Mapping]] = ..., health_status: _Optional[_Union[ApplicationWebhookHealth, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ApplicationWebhooks(_message.Message):
    __slots__ = ("webhooks",)
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    webhooks: _containers.RepeatedCompositeFieldContainer[ApplicationWebhook]
    def __init__(self, webhooks: _Optional[_Iterable[_Union[ApplicationWebhook, _Mapping]]] = ...) -> None: ...

class ApplicationWebhookFormats(_message.Message):
    __slots__ = ("formats",)
    class FormatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    formats: _containers.ScalarMap[str, str]
    def __init__(self, formats: _Optional[_Mapping[str, str]] = ...) -> None: ...

class GetApplicationWebhookRequest(_message.Message):
    __slots__ = ("ids", "field_mask")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationWebhookIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[ApplicationWebhookIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListApplicationWebhooksRequest(_message.Message):
    __slots__ = ("application_ids", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetApplicationWebhookRequest(_message.Message):
    __slots__ = ("webhook", "field_mask")
    WEBHOOK_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    webhook: ApplicationWebhook
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, webhook: _Optional[_Union[ApplicationWebhook, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetApplicationWebhookTemplateRequest(_message.Message):
    __slots__ = ("ids", "field_mask")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationWebhookTemplateIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[ApplicationWebhookTemplateIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListApplicationWebhookTemplatesRequest(_message.Message):
    __slots__ = ("field_mask",)
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
