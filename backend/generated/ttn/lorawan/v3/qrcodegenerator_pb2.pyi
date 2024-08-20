from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from ttn.lorawan.v3 import end_device_pb2 as _end_device_pb2
from ttn.lorawan.v3 import picture_pb2 as _picture_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QRCodeFormat(_message.Message):
    __slots__ = ("name", "description", "field_mask")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class QRCodeFormats(_message.Message):
    __slots__ = ("formats",)
    class FormatsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: QRCodeFormat
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[QRCodeFormat, _Mapping]] = ...) -> None: ...
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    formats: _containers.MessageMap[str, QRCodeFormat]
    def __init__(self, formats: _Optional[_Mapping[str, QRCodeFormat]] = ...) -> None: ...

class GetQRCodeFormatRequest(_message.Message):
    __slots__ = ("format_id",)
    FORMAT_ID_FIELD_NUMBER: _ClassVar[int]
    format_id: str
    def __init__(self, format_id: _Optional[str] = ...) -> None: ...

class GenerateEndDeviceQRCodeRequest(_message.Message):
    __slots__ = ("format_id", "end_device", "image")
    class Image(_message.Message):
        __slots__ = ("image_size",)
        IMAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        image_size: int
        def __init__(self, image_size: _Optional[int] = ...) -> None: ...
    FORMAT_ID_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    format_id: str
    end_device: _end_device_pb2.EndDevice
    image: GenerateEndDeviceQRCodeRequest.Image
    def __init__(self, format_id: _Optional[str] = ..., end_device: _Optional[_Union[_end_device_pb2.EndDevice, _Mapping]] = ..., image: _Optional[_Union[GenerateEndDeviceQRCodeRequest.Image, _Mapping]] = ...) -> None: ...

class GenerateQRCodeResponse(_message.Message):
    __slots__ = ("text", "image")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    text: str
    image: _picture_pb2.Picture
    def __init__(self, text: _Optional[str] = ..., image: _Optional[_Union[_picture_pb2.Picture, _Mapping]] = ...) -> None: ...

class ParseEndDeviceQRCodeRequest(_message.Message):
    __slots__ = ("format_id", "qr_code")
    FORMAT_ID_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_FIELD_NUMBER: _ClassVar[int]
    format_id: str
    qr_code: bytes
    def __init__(self, format_id: _Optional[str] = ..., qr_code: _Optional[bytes] = ...) -> None: ...

class ParseEndDeviceQRCodeResponse(_message.Message):
    __slots__ = ("format_id", "end_device_template")
    FORMAT_ID_FIELD_NUMBER: _ClassVar[int]
    END_DEVICE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    format_id: str
    end_device_template: _end_device_pb2.EndDeviceTemplate
    def __init__(self, format_id: _Optional[str] = ..., end_device_template: _Optional[_Union[_end_device_pb2.EndDeviceTemplate, _Mapping]] = ...) -> None: ...
