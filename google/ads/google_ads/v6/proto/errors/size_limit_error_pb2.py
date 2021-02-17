# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/errors/size_limit_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/errors/size_limit_error.proto',
  package='google.ads.googleads.v6.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.errorsB\023SizeLimitErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Errors\312\002\036Google\\Ads\\GoogleAds\\V6\\Errors\352\002\"Google::Ads::GoogleAds::V6::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/ads/googleads/v6/errors/size_limit_error.proto\x12\x1egoogle.ads.googleads.v6.errors\x1a\x1cgoogle/api/annotations.proto\"\x87\x01\n\x12SizeLimitErrorEnum\"q\n\x0eSizeLimitError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1f\n\x1bREQUEST_SIZE_LIMIT_EXCEEDED\x10\x02\x12 \n\x1cRESPONSE_SIZE_LIMIT_EXCEEDED\x10\x03\x42\xee\x01\n\"com.google.ads.googleads.v6.errorsB\x13SizeLimitErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Errors\xea\x02\"Google::Ads::GoogleAds::V6::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_SIZELIMITERRORENUM_SIZELIMITERROR = _descriptor.EnumDescriptor(
  name='SizeLimitError',
  full_name='google.ads.googleads.v6.errors.SizeLimitErrorEnum.SizeLimitError',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_SIZE_LIMIT_EXCEEDED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESPONSE_SIZE_LIMIT_EXCEEDED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=142,
  serialized_end=255,
)
_sym_db.RegisterEnumDescriptor(_SIZELIMITERRORENUM_SIZELIMITERROR)


_SIZELIMITERRORENUM = _descriptor.Descriptor(
  name='SizeLimitErrorEnum',
  full_name='google.ads.googleads.v6.errors.SizeLimitErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SIZELIMITERRORENUM_SIZELIMITERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=255,
)

_SIZELIMITERRORENUM_SIZELIMITERROR.containing_type = _SIZELIMITERRORENUM
DESCRIPTOR.message_types_by_name['SizeLimitErrorEnum'] = _SIZELIMITERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SizeLimitErrorEnum = _reflection.GeneratedProtocolMessageType('SizeLimitErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _SIZELIMITERRORENUM,
  '__module__' : 'google.ads.googleads.v6.errors.size_limit_error_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.errors.SizeLimitErrorEnum)
  })
_sym_db.RegisterMessage(SizeLimitErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
