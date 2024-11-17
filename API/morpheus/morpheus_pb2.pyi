from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PredictProductNamesRequest(_message.Message):
    __slots__ = ("receipt", "token")
    RECEIPT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    receipt: str
    token: str
    def __init__(self, receipt: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class PredictedProductNames(_message.Message):
    __slots__ = ("predictedName",)
    PREDICTEDNAME_FIELD_NUMBER: _ClassVar[int]
    predictedName: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, predictedName: _Optional[_Iterable[str]] = ...) -> None: ...

class PredictProductNamesResponse(_message.Message):
    __slots__ = ("predictedProductNamesList",)
    PREDICTEDPRODUCTNAMESLIST_FIELD_NUMBER: _ClassVar[int]
    predictedProductNamesList: _containers.RepeatedCompositeFieldContainer[PredictedProductNames]
    def __init__(self, predictedProductNamesList: _Optional[_Iterable[_Union[PredictedProductNames, _Mapping]]] = ...) -> None: ...
