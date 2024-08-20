from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1_1
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import messages_pb2 as _messages_pb2
from ttn.lorawan.v3 import mqtt_pb2 as _mqtt_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationLink(_message.Message):
    __slots__ = ("default_formatters", "skip_payload_crypto")
    DEFAULT_FORMATTERS_FIELD_NUMBER: _ClassVar[int]
    SKIP_PAYLOAD_CRYPTO_FIELD_NUMBER: _ClassVar[int]
    default_formatters: _messages_pb2.MessagePayloadFormatters
    skip_payload_crypto: _wrappers_pb2.BoolValue
    def __init__(self, default_formatters: _Optional[_Union[_messages_pb2.MessagePayloadFormatters, _Mapping]] = ..., skip_payload_crypto: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class GetApplicationLinkRequest(_message.Message):
    __slots__ = ("application_ids", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetApplicationLinkRequest(_message.Message):
    __slots__ = ("application_ids", "link", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    link: ApplicationLink
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., link: _Optional[_Union[ApplicationLink, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ApplicationLinkStats(_message.Message):
    __slots__ = ("linked_at", "network_server_address", "last_up_received_at", "up_count", "last_downlink_forwarded_at", "downlink_count")
    LINKED_AT_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SERVER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LAST_UP_RECEIVED_AT_FIELD_NUMBER: _ClassVar[int]
    UP_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_DOWNLINK_FORWARDED_AT_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_COUNT_FIELD_NUMBER: _ClassVar[int]
    linked_at: _timestamp_pb2.Timestamp
    network_server_address: str
    last_up_received_at: _timestamp_pb2.Timestamp
    up_count: int
    last_downlink_forwarded_at: _timestamp_pb2.Timestamp
    downlink_count: int
    def __init__(self, linked_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., network_server_address: _Optional[str] = ..., last_up_received_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., up_count: _Optional[int] = ..., last_downlink_forwarded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., downlink_count: _Optional[int] = ...) -> None: ...

class AsConfiguration(_message.Message):
    __slots__ = ("pubsub", "webhooks")
    class PubSub(_message.Message):
        __slots__ = ("providers",)
        class Providers(_message.Message):
            __slots__ = ("mqtt", "nats")
            class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ENABLED: _ClassVar[AsConfiguration.PubSub.Providers.Status]
                WARNING: _ClassVar[AsConfiguration.PubSub.Providers.Status]
                DISABLED: _ClassVar[AsConfiguration.PubSub.Providers.Status]
            ENABLED: AsConfiguration.PubSub.Providers.Status
            WARNING: AsConfiguration.PubSub.Providers.Status
            DISABLED: AsConfiguration.PubSub.Providers.Status
            MQTT_FIELD_NUMBER: _ClassVar[int]
            NATS_FIELD_NUMBER: _ClassVar[int]
            mqtt: AsConfiguration.PubSub.Providers.Status
            nats: AsConfiguration.PubSub.Providers.Status
            def __init__(self, mqtt: _Optional[_Union[AsConfiguration.PubSub.Providers.Status, str]] = ..., nats: _Optional[_Union[AsConfiguration.PubSub.Providers.Status, str]] = ...) -> None: ...
        PROVIDERS_FIELD_NUMBER: _ClassVar[int]
        providers: AsConfiguration.PubSub.Providers
        def __init__(self, providers: _Optional[_Union[AsConfiguration.PubSub.Providers, _Mapping]] = ...) -> None: ...
    class Webhooks(_message.Message):
        __slots__ = ("unhealthy_attempts_threshold", "unhealthy_retry_interval")
        UNHEALTHY_ATTEMPTS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        UNHEALTHY_RETRY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        unhealthy_attempts_threshold: int
        unhealthy_retry_interval: _duration_pb2.Duration
        def __init__(self, unhealthy_attempts_threshold: _Optional[int] = ..., unhealthy_retry_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
    PUBSUB_FIELD_NUMBER: _ClassVar[int]
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    pubsub: AsConfiguration.PubSub
    webhooks: AsConfiguration.Webhooks
    def __init__(self, pubsub: _Optional[_Union[AsConfiguration.PubSub, _Mapping]] = ..., webhooks: _Optional[_Union[AsConfiguration.Webhooks, _Mapping]] = ...) -> None: ...

class GetAsConfigurationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAsConfigurationResponse(_message.Message):
    __slots__ = ("configuration",)
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    configuration: AsConfiguration
    def __init__(self, configuration: _Optional[_Union[AsConfiguration, _Mapping]] = ...) -> None: ...

class NsAsHandleUplinkRequest(_message.Message):
    __slots__ = ("application_ups",)
    APPLICATION_UPS_FIELD_NUMBER: _ClassVar[int]
    application_ups: _containers.RepeatedCompositeFieldContainer[_messages_pb2.ApplicationUp]
    def __init__(self, application_ups: _Optional[_Iterable[_Union[_messages_pb2.ApplicationUp, _Mapping]]] = ...) -> None: ...

class EncodeDownlinkRequest(_message.Message):
    __slots__ = ("end_device_ids", "version_ids", "downlink", "formatter", "parameter")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    downlink: _messages_pb2.ApplicationDownlink
    formatter: _messages_pb2.PayloadFormatter
    parameter: str
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., downlink: _Optional[_Union[_messages_pb2.ApplicationDownlink, _Mapping]] = ..., formatter: _Optional[_Union[_messages_pb2.PayloadFormatter, str]] = ..., parameter: _Optional[str] = ...) -> None: ...

class EncodeDownlinkResponse(_message.Message):
    __slots__ = ("downlink",)
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    downlink: _messages_pb2.ApplicationDownlink
    def __init__(self, downlink: _Optional[_Union[_messages_pb2.ApplicationDownlink, _Mapping]] = ...) -> None: ...

class DecodeUplinkRequest(_message.Message):
    __slots__ = ("end_device_ids", "version_ids", "uplink", "formatter", "parameter")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    UPLINK_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    uplink: _messages_pb2.ApplicationUplink
    formatter: _messages_pb2.PayloadFormatter
    parameter: str
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., uplink: _Optional[_Union[_messages_pb2.ApplicationUplink, _Mapping]] = ..., formatter: _Optional[_Union[_messages_pb2.PayloadFormatter, str]] = ..., parameter: _Optional[str] = ...) -> None: ...

class DecodeUplinkResponse(_message.Message):
    __slots__ = ("uplink",)
    UPLINK_FIELD_NUMBER: _ClassVar[int]
    uplink: _messages_pb2.ApplicationUplink
    def __init__(self, uplink: _Optional[_Union[_messages_pb2.ApplicationUplink, _Mapping]] = ...) -> None: ...

class DecodeDownlinkRequest(_message.Message):
    __slots__ = ("end_device_ids", "version_ids", "downlink", "formatter", "parameter")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    downlink: _messages_pb2.ApplicationDownlink
    formatter: _messages_pb2.PayloadFormatter
    parameter: str
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., downlink: _Optional[_Union[_messages_pb2.ApplicationDownlink, _Mapping]] = ..., formatter: _Optional[_Union[_messages_pb2.PayloadFormatter, str]] = ..., parameter: _Optional[str] = ...) -> None: ...

class DecodeDownlinkResponse(_message.Message):
    __slots__ = ("downlink",)
    DOWNLINK_FIELD_NUMBER: _ClassVar[int]
    downlink: _messages_pb2.ApplicationDownlink
    def __init__(self, downlink: _Optional[_Union[_messages_pb2.ApplicationDownlink, _Mapping]] = ...) -> None: ...
