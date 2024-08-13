from google.protobuf import timestamp_pb2 as _timestamp_pb2
from generated.third_party.thethings.json import annotations_pb2 as _annotations_pb2
from generated.third_party.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ALCSyncCommandIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALCSYNC_CID_PKG_VERSION: _ClassVar[ALCSyncCommandIdentifier]
    ALCSYNC_CID_APP_TIME: _ClassVar[ALCSyncCommandIdentifier]
    ALCSYNC_CID_APP_DEV_TIME_PERIODICITY: _ClassVar[ALCSyncCommandIdentifier]
    ALCSYNC_CID_FORCE_DEV_RESYNC: _ClassVar[ALCSyncCommandIdentifier]
ALCSYNC_CID_PKG_VERSION: ALCSyncCommandIdentifier
ALCSYNC_CID_APP_TIME: ALCSyncCommandIdentifier
ALCSYNC_CID_APP_DEV_TIME_PERIODICITY: ALCSyncCommandIdentifier
ALCSYNC_CID_FORCE_DEV_RESYNC: ALCSyncCommandIdentifier

class ALCSyncCommand(_message.Message):
    __slots__ = ("cid", "app_time_req", "app_time_ans")
    class AppTimeReq(_message.Message):
        __slots__ = ("DeviceTime", "TokenReq", "AnsRequired")
        DEVICETIME_FIELD_NUMBER: _ClassVar[int]
        TOKENREQ_FIELD_NUMBER: _ClassVar[int]
        ANSREQUIRED_FIELD_NUMBER: _ClassVar[int]
        DeviceTime: _timestamp_pb2.Timestamp
        TokenReq: int
        AnsRequired: bool
        def __init__(self, DeviceTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., TokenReq: _Optional[int] = ..., AnsRequired: bool = ...) -> None: ...
    class AppTimeAns(_message.Message):
        __slots__ = ("TimeCorrection", "TokenAns")
        TIMECORRECTION_FIELD_NUMBER: _ClassVar[int]
        TOKENANS_FIELD_NUMBER: _ClassVar[int]
        TimeCorrection: int
        TokenAns: int
        def __init__(self, TimeCorrection: _Optional[int] = ..., TokenAns: _Optional[int] = ...) -> None: ...
    CID_FIELD_NUMBER: _ClassVar[int]
    APP_TIME_REQ_FIELD_NUMBER: _ClassVar[int]
    APP_TIME_ANS_FIELD_NUMBER: _ClassVar[int]
    cid: ALCSyncCommandIdentifier
    app_time_req: ALCSyncCommand.AppTimeReq
    app_time_ans: ALCSyncCommand.AppTimeAns
    def __init__(self, cid: _Optional[_Union[ALCSyncCommandIdentifier, str]] = ..., app_time_req: _Optional[_Union[ALCSyncCommand.AppTimeReq, _Mapping]] = ..., app_time_ans: _Optional[_Union[ALCSyncCommand.AppTimeAns, _Mapping]] = ...) -> None: ...
