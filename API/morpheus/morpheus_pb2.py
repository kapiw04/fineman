# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: morpheus.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'morpheus.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emorpheus.proto\x12\x08morpheus\x1a\x1bgoogle/protobuf/empty.proto\"3\n\rPredictedName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cproductGroup\x18\x02 \x01(\x04\"T\n\x1aPredictProductNamesRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08products\x18\x02 \x03(\t\x12\x15\n\rproductGroups\x18\x03 \x03(\x04\"^\n\x15PredictedProductNames\x12.\n\rpredictedName\x18\x01 \x03(\x0b\x32\x17.morpheus.PredictedName\x12\x15\n\rnameOnReceipt\x18\x02 \x01(\t\"a\n\x1bPredictProductNamesResponse\x12\x42\n\x19predictedProductNamesList\x18\x01 \x03(\x0b\x32\x1f.morpheus.PredictedProductNames\"3\n\x1a\x44\x65leteProductGroupsRequest\x12\x15\n\rproductGroups\x18\x01 \x03(\x04\"\x97\x01\n\x13SendFeedbackRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x38\n\x0fgoodPredictions\x18\x02 \x03(\x0b\x32\x1f.morpheus.PredictedProductNames\x12\x37\n\x0e\x62\x61\x64Predictions\x18\x03 \x03(\x0b\x32\x1f.morpheus.PredictedProductNames2\x90\x02\n\x08Morpheus\x12\x64\n\x13PredictProductNames\x12$.morpheus.PredictProductNamesRequest\x1a%.morpheus.PredictProductNamesResponse\"\x00\x12G\n\x0cSendFeedback\x12\x1d.morpheus.SendFeedbackRequest\x1a\x16.google.protobuf.Empty\"\x00\x12U\n\x13\x44\x65leteProductGroups\x12$.morpheus.DeleteProductGroupsRequest\x1a\x16.google.protobuf.Empty\"\x00\x42\x0eZ\x0csrc/protogenb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'morpheus_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\014src/protogen'
  _globals['_PREDICTEDNAME']._serialized_start=57
  _globals['_PREDICTEDNAME']._serialized_end=108
  _globals['_PREDICTPRODUCTNAMESREQUEST']._serialized_start=110
  _globals['_PREDICTPRODUCTNAMESREQUEST']._serialized_end=194
  _globals['_PREDICTEDPRODUCTNAMES']._serialized_start=196
  _globals['_PREDICTEDPRODUCTNAMES']._serialized_end=290
  _globals['_PREDICTPRODUCTNAMESRESPONSE']._serialized_start=292
  _globals['_PREDICTPRODUCTNAMESRESPONSE']._serialized_end=389
  _globals['_DELETEPRODUCTGROUPSREQUEST']._serialized_start=391
  _globals['_DELETEPRODUCTGROUPSREQUEST']._serialized_end=442
  _globals['_SENDFEEDBACKREQUEST']._serialized_start=445
  _globals['_SENDFEEDBACKREQUEST']._serialized_end=596
  _globals['_MORPHEUS']._serialized_start=599
  _globals['_MORPHEUS']._serialized_end=871
# @@protoc_insertion_point(module_scope)
