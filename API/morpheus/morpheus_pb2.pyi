from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PredictedName(_message.Message):
    __slots__ = ("name", "productGroup")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUP_FIELD_NUMBER: _ClassVar[int]
    name: str
    productGroup: int
    def __init__(self, name: _Optional[str] = ..., productGroup: _Optional[int] = ...) -> None: ...

class PredictProductNamesRequest(_message.Message):
    __slots__ = ("token", "products", "productGroups")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTGROUPS_FIELD_NUMBER: _ClassVar[int]
    token: str
    products: _containers.RepeatedScalarFieldContainer[str]
    productGroups: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, token: _Optional[str] = ..., products: _Optional[_Iterable[str]] = ..., productGroups: _Optional[_Iterable[int]] = ...) -> None: ...

class PredictedProductNames(_message.Message):
    __slots__ = ("predictedName", "nameOnReceipt")
    PREDICTEDNAME_FIELD_NUMBER: _ClassVar[int]
    NAMEONRECEIPT_FIELD_NUMBER: _ClassVar[int]
    predictedName: _containers.RepeatedCompositeFieldContainer[PredictedName]
    nameOnReceipt: str
    def __init__(self, predictedName: _Optional[_Iterable[_Union[PredictedName, _Mapping]]] = ..., nameOnReceipt: _Optional[str] = ...) -> None: ...

class PredictProductNamesResponse(_message.Message):
    __slots__ = ("predictedProductNamesList",)
    PREDICTEDPRODUCTNAMESLIST_FIELD_NUMBER: _ClassVar[int]
    predictedProductNamesList: _containers.RepeatedCompositeFieldContainer[PredictedProductNames]
    def __init__(self, predictedProductNamesList: _Optional[_Iterable[_Union[PredictedProductNames, _Mapping]]] = ...) -> None: ...

class DeleteProductGroupsRequest(_message.Message):
    __slots__ = ("productGroups",)
    PRODUCTGROUPS_FIELD_NUMBER: _ClassVar[int]
    productGroups: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, productGroups: _Optional[_Iterable[int]] = ...) -> None: ...

class SendFeedbackRequest(_message.Message):
    __slots__ = ("token", "goodPredictions", "badPredictions")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    GOODPREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    BADPREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    token: str
    goodPredictions: _containers.RepeatedCompositeFieldContainer[PredictedProductNames]
    badPredictions: _containers.RepeatedCompositeFieldContainer[PredictedProductNames]
    def __init__(self, token: _Optional[str] = ..., goodPredictions: _Optional[_Iterable[_Union[PredictedProductNames, _Mapping]]] = ..., badPredictions: _Optional[_Iterable[_Union[PredictedProductNames, _Mapping]]] = ...) -> None: ...
