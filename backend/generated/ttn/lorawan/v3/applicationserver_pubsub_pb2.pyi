from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationPubSubIdentifiers(_message.Message):
    __slots__ = ("application_ids", "pub_sub_id")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    PUB_SUB_ID_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    pub_sub_id: str
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., pub_sub_id: _Optional[str] = ...) -> None: ...

class ApplicationPubSub(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "format", "nats", "mqtt", "aws_iot", "base_topic", "downlink_push", "downlink_replace", "uplink_message", "uplink_normalized", "join_accept", "downlink_ack", "downlink_nack", "downlink_sent", "downlink_failed", "downlink_queued", "downlink_queue_invalidated", "location_solved", "service_data")
    class NATSProvider(_message.Message):
        __slots__ = ("server_url",)
        SERVER_URL_FIELD_NUMBER: _ClassVar[int]
        server_url: str
        def __init__(self, server_url: _Optional[str] = ...) -> None: ...
    class MQTTProvider(_message.Message):
        __slots__ = ("server_url", "client_id", "username", "password", "subscribe_qos", "publish_qos", "use_tls", "tls_ca", "tls_client_cert", "tls_client_key", "headers")
        class QoS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AT_MOST_ONCE: _ClassVar[ApplicationPubSub.MQTTProvider.QoS]
            AT_LEAST_ONCE: _ClassVar[ApplicationPubSub.MQTTProvider.QoS]
            EXACTLY_ONCE: _ClassVar[ApplicationPubSub.MQTTProvider.QoS]
        AT_MOST_ONCE: ApplicationPubSub.MQTTProvider.QoS
        AT_LEAST_ONCE: ApplicationPubSub.MQTTProvider.QoS
        EXACTLY_ONCE: ApplicationPubSub.MQTTProvider.QoS
        class HeadersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        SERVER_URL_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIBE_QOS_FIELD_NUMBER: _ClassVar[int]
        PUBLISH_QOS_FIELD_NUMBER: _ClassVar[int]
        USE_TLS_FIELD_NUMBER: _ClassVar[int]
        TLS_CA_FIELD_NUMBER: _ClassVar[int]
        TLS_CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
        TLS_CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        server_url: str
        client_id: str
        username: str
        password: str
        subscribe_qos: ApplicationPubSub.MQTTProvider.QoS
        publish_qos: ApplicationPubSub.MQTTProvider.QoS
        use_tls: bool
        tls_ca: bytes
        tls_client_cert: bytes
        tls_client_key: bytes
        headers: _containers.ScalarMap[str, str]
        def __init__(self, server_url: _Optional[str] = ..., client_id: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ..., subscribe_qos: _Optional[_Union[ApplicationPubSub.MQTTProvider.QoS, str]] = ..., publish_qos: _Optional[_Union[ApplicationPubSub.MQTTProvider.QoS, str]] = ..., use_tls: bool = ..., tls_ca: _Optional[bytes] = ..., tls_client_cert: _Optional[bytes] = ..., tls_client_key: _Optional[bytes] = ..., headers: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class AWSIoTProvider(_message.Message):
        __slots__ = ("region", "access_key", "assume_role", "endpoint_address", "default")
        class AccessKey(_message.Message):
            __slots__ = ("access_key_id", "secret_access_key", "session_token")
            ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
            SESSION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            access_key_id: str
            secret_access_key: str
            session_token: str
            def __init__(self, access_key_id: _Optional[str] = ..., secret_access_key: _Optional[str] = ..., session_token: _Optional[str] = ...) -> None: ...
        class AssumeRole(_message.Message):
            __slots__ = ("arn", "external_id", "session_duration")
            ARN_FIELD_NUMBER: _ClassVar[int]
            EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
            SESSION_DURATION_FIELD_NUMBER: _ClassVar[int]
            arn: str
            external_id: str
            session_duration: _duration_pb2.Duration
            def __init__(self, arn: _Optional[str] = ..., external_id: _Optional[str] = ..., session_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...
        class DefaultIntegration(_message.Message):
            __slots__ = ("stack_name",)
            STACK_NAME_FIELD_NUMBER: _ClassVar[int]
            stack_name: str
            def __init__(self, stack_name: _Optional[str] = ...) -> None: ...
        REGION_FIELD_NUMBER: _ClassVar[int]
        ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        ASSUME_ROLE_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_FIELD_NUMBER: _ClassVar[int]
        region: str
        access_key: ApplicationPubSub.AWSIoTProvider.AccessKey
        assume_role: ApplicationPubSub.AWSIoTProvider.AssumeRole
        endpoint_address: str
        default: ApplicationPubSub.AWSIoTProvider.DefaultIntegration
        def __init__(self, region: _Optional[str] = ..., access_key: _Optional[_Union[ApplicationPubSub.AWSIoTProvider.AccessKey, _Mapping]] = ..., assume_role: _Optional[_Union[ApplicationPubSub.AWSIoTProvider.AssumeRole, _Mapping]] = ..., endpoint_address: _Optional[str] = ..., default: _Optional[_Union[ApplicationPubSub.AWSIoTProvider.DefaultIntegration, _Mapping]] = ...) -> None: ...
    class Message(_message.Message):
        __slots__ = ("topic",)
        TOPIC_FIELD_NUMBER: _ClassVar[int]
        topic: str
        def __init__(self, topic: _Optional[str] = ...) -> None: ...
    IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    NATS_FIELD_NUMBER: _ClassVar[int]
    MQTT_FIELD_NUMBER: _ClassVar[int]
    AWS_IOT_FIELD_NUMBER: _ClassVar[int]
    BASE_TOPIC_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_PUSH_FIELD_NUMBER: _ClassVar[int]
    DOWNLINK_REPLACE_FIELD_NUMBER: _ClassVar[int]
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
    ids: ApplicationPubSubIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    format: str
    nats: ApplicationPubSub.NATSProvider
    mqtt: ApplicationPubSub.MQTTProvider
    aws_iot: ApplicationPubSub.AWSIoTProvider
    base_topic: str
    downlink_push: ApplicationPubSub.Message
    downlink_replace: ApplicationPubSub.Message
    uplink_message: ApplicationPubSub.Message
    uplink_normalized: ApplicationPubSub.Message
    join_accept: ApplicationPubSub.Message
    downlink_ack: ApplicationPubSub.Message
    downlink_nack: ApplicationPubSub.Message
    downlink_sent: ApplicationPubSub.Message
    downlink_failed: ApplicationPubSub.Message
    downlink_queued: ApplicationPubSub.Message
    downlink_queue_invalidated: ApplicationPubSub.Message
    location_solved: ApplicationPubSub.Message
    service_data: ApplicationPubSub.Message
    def __init__(self, ids: _Optional[_Union[ApplicationPubSubIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., format: _Optional[str] = ..., nats: _Optional[_Union[ApplicationPubSub.NATSProvider, _Mapping]] = ..., mqtt: _Optional[_Union[ApplicationPubSub.MQTTProvider, _Mapping]] = ..., aws_iot: _Optional[_Union[ApplicationPubSub.AWSIoTProvider, _Mapping]] = ..., base_topic: _Optional[str] = ..., downlink_push: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., downlink_replace: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., uplink_message: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., uplink_normalized: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., join_accept: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., downlink_ack: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., downlink_nack: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., downlink_sent: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., downlink_failed: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., downlink_queued: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., downlink_queue_invalidated: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., location_solved: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ..., service_data: _Optional[_Union[ApplicationPubSub.Message, _Mapping]] = ...) -> None: ...

class ApplicationPubSubs(_message.Message):
    __slots__ = ("pubsubs",)
    PUBSUBS_FIELD_NUMBER: _ClassVar[int]
    pubsubs: _containers.RepeatedCompositeFieldContainer[ApplicationPubSub]
    def __init__(self, pubsubs: _Optional[_Iterable[_Union[ApplicationPubSub, _Mapping]]] = ...) -> None: ...

class ApplicationPubSubFormats(_message.Message):
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

class GetApplicationPubSubRequest(_message.Message):
    __slots__ = ("ids", "field_mask")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationPubSubIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[ApplicationPubSubIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListApplicationPubSubsRequest(_message.Message):
    __slots__ = ("application_ids", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetApplicationPubSubRequest(_message.Message):
    __slots__ = ("pubsub", "field_mask")
    PUBSUB_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    pubsub: ApplicationPubSub
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, pubsub: _Optional[_Union[ApplicationPubSub, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
