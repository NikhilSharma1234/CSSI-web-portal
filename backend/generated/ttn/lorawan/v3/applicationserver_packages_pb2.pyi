from generated.third_party.google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from generated.third_party.thethings.flags import annotations_pb2 as _annotations_pb2_1_1
from generated.ttn.lorawan.v3 import identifiers_pb2 as _identifiers_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationPackage(_message.Message):
    __slots__ = ("name", "default_f_port")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_F_PORT_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_f_port: int
    def __init__(self, name: _Optional[str] = ..., default_f_port: _Optional[int] = ...) -> None: ...

class ApplicationPackages(_message.Message):
    __slots__ = ("packages",)
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.RepeatedCompositeFieldContainer[ApplicationPackage]
    def __init__(self, packages: _Optional[_Iterable[_Union[ApplicationPackage, _Mapping]]] = ...) -> None: ...

class ApplicationPackageAssociationIdentifiers(_message.Message):
    __slots__ = ("end_device_ids", "f_port")
    END_DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    end_device_ids: _identifiers_pb2.EndDeviceIdentifiers
    f_port: int
    def __init__(self, end_device_ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., f_port: _Optional[int] = ...) -> None: ...

class ApplicationPackageAssociation(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "package_name", "data")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationPackageAssociationIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    package_name: str
    data: _struct_pb2.Struct
    def __init__(self, ids: _Optional[_Union[ApplicationPackageAssociationIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., package_name: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ApplicationPackageAssociations(_message.Message):
    __slots__ = ("associations",)
    ASSOCIATIONS_FIELD_NUMBER: _ClassVar[int]
    associations: _containers.RepeatedCompositeFieldContainer[ApplicationPackageAssociation]
    def __init__(self, associations: _Optional[_Iterable[_Union[ApplicationPackageAssociation, _Mapping]]] = ...) -> None: ...

class GetApplicationPackageAssociationRequest(_message.Message):
    __slots__ = ("ids", "field_mask")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationPackageAssociationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[ApplicationPackageAssociationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListApplicationPackageAssociationRequest(_message.Message):
    __slots__ = ("ids", "limit", "page", "field_mask")
    IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.EndDeviceIdentifiers
    limit: int
    page: int
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.EndDeviceIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetApplicationPackageAssociationRequest(_message.Message):
    __slots__ = ("association", "field_mask")
    ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    association: ApplicationPackageAssociation
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, association: _Optional[_Union[ApplicationPackageAssociation, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ApplicationPackageDefaultAssociationIdentifiers(_message.Message):
    __slots__ = ("application_ids", "f_port")
    APPLICATION_IDS_FIELD_NUMBER: _ClassVar[int]
    F_PORT_FIELD_NUMBER: _ClassVar[int]
    application_ids: _identifiers_pb2.ApplicationIdentifiers
    f_port: int
    def __init__(self, application_ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., f_port: _Optional[int] = ...) -> None: ...

class ApplicationPackageDefaultAssociation(_message.Message):
    __slots__ = ("ids", "created_at", "updated_at", "package_name", "data")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationPackageDefaultAssociationIdentifiers
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    package_name: str
    data: _struct_pb2.Struct
    def __init__(self, ids: _Optional[_Union[ApplicationPackageDefaultAssociationIdentifiers, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., package_name: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class ApplicationPackageDefaultAssociations(_message.Message):
    __slots__ = ("defaults",)
    DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    defaults: _containers.RepeatedCompositeFieldContainer[ApplicationPackageDefaultAssociation]
    def __init__(self, defaults: _Optional[_Iterable[_Union[ApplicationPackageDefaultAssociation, _Mapping]]] = ...) -> None: ...

class GetApplicationPackageDefaultAssociationRequest(_message.Message):
    __slots__ = ("ids", "field_mask")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: ApplicationPackageDefaultAssociationIdentifiers
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[ApplicationPackageDefaultAssociationIdentifiers, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class ListApplicationPackageDefaultAssociationRequest(_message.Message):
    __slots__ = ("ids", "limit", "page", "field_mask")
    IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ids: _identifiers_pb2.ApplicationIdentifiers
    limit: int
    page: int
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, ids: _Optional[_Union[_identifiers_pb2.ApplicationIdentifiers, _Mapping]] = ..., limit: _Optional[int] = ..., page: _Optional[int] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class SetApplicationPackageDefaultAssociationRequest(_message.Message):
    __slots__ = ("default", "field_mask")
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    default: ApplicationPackageDefaultAssociation
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, default: _Optional[_Union[ApplicationPackageDefaultAssociation, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...
