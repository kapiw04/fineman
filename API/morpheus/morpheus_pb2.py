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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emorpheus.proto\x12\x08morpheus\"<\n\x1aPredictProductNamesRequest\x12\x0f\n\x07receipt\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\".\n\x15PredictedProductNames\x12\x15\n\rpredictedName\x18\x01 \x03(\t\"a\n\x1bPredictProductNamesResponse\x12\x42\n\x19predictedProductNamesList\x18\x01 \x03(\x0b\x32\x1f.morpheus.PredictedProductNames2p\n\x08Morpheus\x12\x64\n\x13PredictProductNames\x12$.morpheus.PredictProductNamesRequest\x1a%.morpheus.PredictProductNamesResponse\"\x00\x42\x0eZ\x0csrc/protogenb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'morpheus_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\014src/protogen'
  _globals['_PREDICTPRODUCTNAMESREQUEST']._serialized_start=28
  _globals['_PREDICTPRODUCTNAMESREQUEST']._serialized_end=88
  _globals['_PREDICTEDPRODUCTNAMES']._serialized_start=90
  _globals['_PREDICTEDPRODUCTNAMES']._serialized_end=136
  _globals['_PREDICTPRODUCTNAMESRESPONSE']._serialized_start=138
  _globals['_PREDICTPRODUCTNAMESRESPONSE']._serialized_end=235
  _globals['_MORPHEUS']._serialized_start=237
  _globals['_MORPHEUS']._serialized_end=349
# @@protoc_insertion_point(module_scope)
