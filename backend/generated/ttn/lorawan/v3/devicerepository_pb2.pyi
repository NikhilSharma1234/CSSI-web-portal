from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2_1_1
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from ttn.lorawan.v3 import messages_pb2 as _messages_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeyProvisioning(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_PROVISIONING_UNKNOWN: _ClassVar[KeyProvisioning]
    KEY_PROVISIONING_CUSTOM: _ClassVar[KeyProvisioning]
    KEY_PROVISIONING_JOIN_SERVER: _ClassVar[KeyProvisioning]
    KEY_PROVISIONING_MANIFEST: _ClassVar[KeyProvisioning]

class KeySecurity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    KEY_SECURITY_UNKNOWN: _ClassVar[KeySecurity]
    KEY_SECURITY_NONE: _ClassVar[KeySecurity]
    KEY_SECURITY_READ_PROTECTED: _ClassVar[KeySecurity]
    KEY_SECURITY_SECURE_ELEMENT: _ClassVar[KeySecurity]
KEY_PROVISIONING_UNKNOWN: KeyProvisioning
KEY_PROVISIONING_CUSTOM: KeyProvisioning
KEY_PROVISIONING_JOIN_SERVER: KeyProvisioning
KEY_PROVISIONING_MANIFEST: KeyProvisioning
KEY_SECURITY_UNKNOWN: KeySecurity
KEY_SECURITY_NONE: KeySecurity
KEY_SECURITY_READ_PROTECTED: KeySecurity
KEY_SECURITY_SECURE_ELEMENT: KeySecurity

class EndDeviceBrand(_message.Message):
    __slots__ = ("brand_id", "name", "private_enterprise_number", "organization_unique_identifiers", "lora_alliance_vendor_id", "website", "email", "logo")
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_ENTERPRISE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_UNIQUE_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    LORA_ALLIANCE_VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    brand_id: str
    name: str
    private_enterprise_number: int
    organization_unique_identifiers: _containers.RepeatedScalarFieldContainer[str]
    lora_alliance_vendor_id: int
    website: str
    email: str
    logo: str
    def __init__(self, brand_id: _Optional[str] = ..., name: _Optional[str] = ..., private_enterprise_number: _Optional[int] = ..., organization_unique_identifiers: _Optional[_Iterable[str]] = ..., lora_alliance_vendor_id: _Optional[int] = ..., website: _Optional[str] = ..., email: _Optional[str] = ..., logo: _Optional[str] = ...) -> None: ...

class EndDeviceModel(_message.Message):
    __slots__ = ("brand_id", "model_id", "name", "description", "hardware_versions", "firmware_versions", "sensors", "dimensions", "weight", "battery", "operating_conditions", "ip_code", "key_provisioning", "key_security", "photos", "videos", "product_url", "datasheet_url", "resellers", "compliances", "additional_radios")
    class HardwareVersion(_message.Message):
        __slots__ = ("version", "numeric", "part_number")
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NUMERIC_FIELD_NUMBER: _ClassVar[int]
        PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
        version: str
        numeric: int
        part_number: str
        def __init__(self, version: _Optional[str] = ..., numeric: _Optional[int] = ..., part_number: _Optional[str] = ...) -> None: ...
    class FirmwareVersion(_message.Message):
        __slots__ = ("version", "numeric", "supported_hardware_versions", "profiles")
        class Profile(_message.Message):
            __slots__ = ("vendor_id", "profile_id", "lorawan_certified", "codec_id")
            VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
            PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
            LORAWAN_CERTIFIED_FIELD_NUMBER: _ClassVar[int]
            CODEC_ID_FIELD_NUMBER: _ClassVar[int]
            vendor_id: str
            profile_id: str
            lorawan_certified: bool
            codec_id: str
            def __init__(self, vendor_id: _Optional[str] = ..., profile_id: _Optional[str] = ..., lorawan_certified: bool = ..., codec_id: _Optional[str] = ...) -> None: ...
        class ProfilesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: EndDeviceModel.FirmwareVersion.Profile
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[EndDeviceModel.FirmwareVersion.Profile, _Mapping]] = ...) -> None: ...
        VERSION_FIELD_NUMBER: _ClassVar[int]
        NUMERIC_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_HARDWARE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
        PROFILES_FIELD_NUMBER: _ClassVar[int]
        version: str
        numeric: int
        supported_hardware_versions: _containers.RepeatedScalarFieldContainer[str]
        profiles: _containers.MessageMap[str, EndDeviceModel.FirmwareVersion.Profile]
        def __init__(self, version: _Optional[str] = ..., numeric: _Optional[int] = ..., supported_hardware_versions: _Optional[_Iterable[str]] = ..., profiles: _Optional[_Mapping[str, EndDeviceModel.FirmwareVersion.Profile]] = ...) -> None: ...
    class Dimensions(_message.Message):
        __slots__ = ("width", "height", "diameter", "length")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        DIAMETER_FIELD_NUMBER: _ClassVar[int]
        LENGTH_FIELD_NUMBER: _ClassVar[int]
        width: _wrappers_pb2.FloatValue
        height: _wrappers_pb2.FloatValue
        diameter: _wrappers_pb2.FloatValue
        length: _wrappers_pb2.FloatValue
        def __init__(self, width: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., height: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., diameter: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., length: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...
    class Battery(_message.Message):
        __slots__ = ("replaceable", "type")
        REPLACEABLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        replaceable: _wrappers_pb2.BoolValue
        type: str
        def __init__(self, replaceable: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...
    class OperatingConditions(_message.Message):
        __slots__ = ("temperature", "relative_humidity")
        class Limits(_message.Message):
            __slots__ = ("min", "max")
            MIN_FIELD_NUMBER: _ClassVar[int]
            MAX_FIELD_NUMBER: _ClassVar[int]
            min: _wrappers_pb2.FloatValue
            max: _wrappers_pb2.FloatValue
            def __init__(self, min: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., max: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...
        TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        RELATIVE_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
        temperature: EndDeviceModel.OperatingConditions.Limits
        relative_humidity: EndDeviceModel.OperatingConditions.Limits
        def __init__(self, temperature: _Optional[_Union[EndDeviceModel.OperatingConditions.Limits, _Mapping]] = ..., relative_humidity: _Optional[_Union[EndDeviceModel.OperatingConditions.Limits, _Mapping]] = ...) -> None: ...
    class Photos(_message.Message):
        __slots__ = ("main", "other")
        MAIN_FIELD_NUMBER: _ClassVar[int]
        OTHER_FIELD_NUMBER: _ClassVar[int]
        main: str
        other: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, main: _Optional[str] = ..., other: _Optional[_Iterable[str]] = ...) -> None: ...
    class Videos(_message.Message):
        __slots__ = ("main", "other")
        MAIN_FIELD_NUMBER: _ClassVar[int]
        OTHER_FIELD_NUMBER: _ClassVar[int]
        main: str
        other: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, main: _Optional[str] = ..., other: _Optional[_Iterable[str]] = ...) -> None: ...
    class Reseller(_message.Message):
        __slots__ = ("name", "region", "url")
        NAME_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        name: str
        region: _containers.RepeatedScalarFieldContainer[str]
        url: str
        def __init__(self, name: _Optional[str] = ..., region: _Optional[_Iterable[str]] = ..., url: _Optional[str] = ...) -> None: ...
    class Compliances(_message.Message):
        __slots__ = ("safety", "radio_equipment")
        class Compliance(_message.Message):
            __slots__ = ("body", "norm", "standard", "version")
            BODY_FIELD_NUMBER: _ClassVar[int]
            NORM_FIELD_NUMBER: _ClassVar[int]
            STANDARD_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            body: str
            norm: str
            standard: str
            version: str
            def __init__(self, body: _Optional[str] = ..., norm: _Optional[str] = ..., standard: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
        SAFETY_FIELD_NUMBER: _ClassVar[int]
        RADIO_EQUIPMENT_FIELD_NUMBER: _ClassVar[int]
        safety: _containers.RepeatedCompositeFieldContainer[EndDeviceModel.Compliances.Compliance]
        radio_equipment: _containers.RepeatedCompositeFieldContainer[EndDeviceModel.Compliances.Compliance]
        def __init__(self, safety: _Optional[_Iterable[_Union[EndDeviceModel.Compliances.Compliance, _Mapping]]] = ..., radio_equipment: _Optional[_Iterable[_Union[EndDeviceModel.Compliances.Compliance, _Mapping]]] = ...) -> None: ...
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HARDWARE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    FIRMWARE_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    SENSORS_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    OPERATING_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    IP_CODE_FIELD_NUMBER: _ClassVar[int]
    KEY_PROVISIONING_FIELD_NUMBER: _ClassVar[int]
    KEY_SECURITY_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    VIDEOS_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_URL_FIELD_NUMBER: _ClassVar[int]
    DATASHEET_URL_FIELD_NUMBER: _ClassVar[int]
    RESELLERS_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_RADIOS_FIELD_NUMBER: _ClassVar[int]
    brand_id: str
    model_id: str
    name: str
    description: str
    hardware_versions: _containers.RepeatedCompositeFieldContainer[EndDeviceModel.HardwareVersion]
    firmware_versions: _containers.RepeatedCompositeFieldContainer[EndDeviceModel.FirmwareVersion]
    sensors: _containers.RepeatedScalarFieldContainer[str]
    dimensions: EndDeviceModel.Dimensions
    weight: _wrappers_pb2.FloatValue
    battery: EndDeviceModel.Battery
    operating_conditions: EndDeviceModel.OperatingConditions
    ip_code: str
    key_provisioning: _containers.RepeatedScalarFieldContainer[KeyProvisioning]
    key_security: KeySecurity
    photos: EndDeviceModel.Photos
    videos: EndDeviceModel.Videos
    product_url: str
    datasheet_url: str
    resellers: _containers.RepeatedCompositeFieldContainer[EndDeviceModel.Reseller]
    compliances: EndDeviceModel.Compliances
    additional_radios: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, brand_id: _Optional[str] = ..., model_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., hardware_versions: _Optional[_Iterable[_Union[EndDeviceModel.HardwareVersion, _Mapping]]] = ..., firmware_versions: _Optional[_Iterable[_Union[EndDeviceModel.FirmwareVersion, _Mapping]]] = ..., sensors: _Optional[_Iterable[str]] = ..., dimensions: _Optional[_Union[EndDeviceModel.Dimensions, _Mapping]] = ..., weight: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., battery: _Optional[_Union[EndDeviceModel.Battery, _Mapping]] = ..., operating_conditions: _Optional[_Union[EndDeviceModel.OperatingConditions, _Mapping]] = ..., ip_code: _Optional[str] = ..., key_provisioning: _Optional[_Iterable[_Union[KeyProvisioning, str]]] = ..., key_security: _Optional[_Union[KeySecurity, str]] = ..., photos: _Optional[_Union[EndDeviceModel.Photos, _Mapping]] = ..., videos: _Optional[_Union[EndDeviceModel.Videos, _Mapping]] = ..., product_url: _Optional[str] = ..., datasheet_url: _Optional[str] = ..., resellers: _Optional[_Iterable[_Union[EndDeviceModel.Reseller, _Mapping]]] = ..., compliances: _Optional[_Union[EndDeviceModel.Compliances, _Mapping]] = ..., additional_radios: _Optional[_Iterable[str]] = ...) -> None: ...

class GetEndDeviceBrandRequest(_message.Message):
    __slots__ = ("application_ids", "brand_id", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    brand_id: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., brand_id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListEndDeviceBrandsRequest(_message.Message):
    __slots__ = ("application_ids", "limit", "page", "order_by", "search", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    limit: int
    page: int
    order_by: str
    search: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., order_by: _Optional[str] = ..., search: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetEndDeviceModelRequest(_message.Message):
    __slots__ = ("application_ids", "brand_id", "model_id", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    brand_id: str
    model_id: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., brand_id: _Optional[str] = ..., model_id: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListEndDeviceModelsRequest(_message.Message):
    __slots__ = ("application_ids", "brand_id", "limit", "page", "order_by", "search", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    BRAND_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    brand_id: str
    limit: int
    page: int
    order_by: str
    search: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., brand_id: _Optional[str] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., order_by: _Optional[str] = ..., search: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class GetTemplateRequest(_message.Message):
    __slots__ = ("application_ids", "version_ids", "end_device_profile_ids")
    class EndDeviceProfileIdentifiers(_message.Message):
        __slots__ = ("vendor_id", "vendor_profile_id")
        VENDOR_ID_FIELD_NUMBER: _ClassVar[int]
        VENDOR_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
        vendor_id: int
        vendor_profile_id: int
        def __init__(self, vendor_id: _Optional[int] = ..., vendor_profile_id: _Optional[int] = ...) -> None: ...
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_PROFILE_IDS_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    end_device_profile_ids: GetTemplateRequest.EndDeviceProfileIdentifiers
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., end_device_profile_ids: _Optional[_Union[GetTemplateRequest.EndDeviceProfileIdentifiers, _Mapping]] = ...) -> None: ...

class GetPayloadFormatterRequest(_message.Message):
    __slots__ = ("application_ids", "version_ids", "field_mask")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    VERSION_IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    version_ids: _identifiers_pb2.EndDeviceVersionIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., version_ids: _Optional[_Union[_identifiers_pb2.EndDeviceVersionIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListEndDeviceBrandsResponse(_message.Message):
    __slots__ = ("brands",)
    BRANDS_FIELD_NUMBER: _ClassVar[int]
    brands: _containers.RepeatedCompositeFieldContainer[EndDeviceBrand]
    def __init__(self, brands: _Optional[_Iterable[_Union[EndDeviceBrand, _Mapping]]] = ...) -> None: ...

class ListEndDeviceModelsResponse(_message.Message):
    __slots__ = ("models",)
    MODELS_FIELD_NUMBER: _ClassVar[int]
    models: _containers.RepeatedCompositeFieldContainer[EndDeviceModel]
    def __init__(self, models: _Optional[_Iterable[_Union[EndDeviceModel, _Mapping]]] = ...) -> None: ...

class EncodedMessagePayload(_message.Message):
    __slots__ = ("f_port", "frm_payload", "warnings", "errors")
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    FRM_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    f_port: int
    frm_payload: bytes
    warnings: _containers.RepeatedScalarFieldContainer[str]
    errors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, f_port: _Optional[int] = ..., frm_payload: _Optional[bytes] = ..., warnings: _Optional[_Iterable[str]] = ..., errors: _Optional[_Iterable[str]] = ...) -> None: ...

class DecodedMessagePayload(_message.Message):
    __slots__ = ("data", "warnings", "errors")
    DATA_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    data: _struct_pb2.Struct
    warnings: _containers.RepeatedScalarFieldContainer[str]
    errors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., warnings: _Optional[_Iterable[str]] = ..., errors: _Optional[_Iterable[str]] = ...) -> None: ...

class MessagePayloadDecoder(_message.Message):
    __slots__ = ("formatter", "formatter_parameter", "codec_id", "examples")
    class Example(_message.Message):
        __slots__ = ("description", "input", "output")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        description: str
        input: EncodedMessagePayload
        output: DecodedMessagePayload
        def __init__(self, description: _Optional[str] = ..., input: _Optional[_Union[EncodedMessagePayload, _Mapping]] = ..., output: _Optional[_Union[DecodedMessagePayload, _Mapping]] = ...) -> None: ...
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    CODEC_ID_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    formatter: _messages_pb2.PayloadFormatter
    formatter_parameter: str
    codec_id: str
    examples: _containers.RepeatedCompositeFieldContainer[MessagePayloadDecoder.Example]
    def __init__(self, formatter: _Optional[_Union[_messages_pb2.PayloadFormatter, str]] = ..., formatter_parameter: _Optional[str] = ..., codec_id: _Optional[str] = ..., examples: _Optional[_Iterable[_Union[MessagePayloadDecoder.Example, _Mapping]]] = ...) -> None: ...

class MessagePayloadEncoder(_message.Message):
    __slots__ = ("formatter", "formatter_parameter", "codec_id", "examples")
    class Example(_message.Message):
        __slots__ = ("description", "input", "output")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        description: str
        input: DecodedMessagePayload
        output: EncodedMessagePayload
        def __init__(self, description: _Optional[str] = ..., input: _Optional[_Union[DecodedMessagePayload, _Mapping]] = ..., output: _Optional[_Union[EncodedMessagePayload, _Mapping]] = ...) -> None: ...
    FORMATTER_FIELD_NUMBER: _ClassVar[int]
    FORMATTER_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    CODEC_ID_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    formatter: _messages_pb2.PayloadFormatter
    formatter_parameter: str
    codec_id: str
    examples: _containers.RepeatedCompositeFieldContainer[MessagePayloadEncoder.Example]
    def __init__(self, formatter: _Optional[_Union[_messages_pb2.PayloadFormatter, str]] = ..., formatter_parameter: _Optional[str] = ..., codec_id: _Optional[str] = ..., examples: _Optional[_Iterable[_Union[MessagePayloadEncoder.Example, _Mapping]]] = ...) -> None: ...
