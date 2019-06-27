# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/errors/field_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/errors/field_error.proto',
  package='google.ads.googleads.v2.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v2.errorsB\017FieldErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Errors\312\002\036Google\\Ads\\GoogleAds\\V2\\Errors\352\002\"Google::Ads::GoogleAds::V2::Errors'),
  serialized_pb=_b('\n6google/ads/googleads_v2/proto/errors/field_error.proto\x12\x1egoogle.ads.googleads.v2.errors\x1a\x1cgoogle/api/annotations.proto\"\xdc\x01\n\x0e\x46ieldErrorEnum\"\xc9\x01\n\nFieldError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08REQUIRED\x10\x02\x12\x13\n\x0fIMMUTABLE_FIELD\x10\x03\x12\x11\n\rINVALID_VALUE\x10\x04\x12\x17\n\x13VALUE_MUST_BE_UNSET\x10\x05\x12\x1a\n\x16REQUIRED_NONEMPTY_LIST\x10\x06\x12\x1b\n\x17\x46IELD_CANNOT_BE_CLEARED\x10\x07\x12\x15\n\x11\x42LACKLISTED_VALUE\x10\x08\x42\xea\x01\n\"com.google.ads.googleads.v2.errorsB\x0f\x46ieldErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Errors\xea\x02\"Google::Ads::GoogleAds::V2::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FIELDERRORENUM_FIELDERROR = _descriptor.EnumDescriptor(
  name='FieldError',
  full_name='google.ads.googleads.v2.errors.FieldErrorEnum.FieldError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMMUTABLE_FIELD', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_VALUE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_MUST_BE_UNSET', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRED_NONEMPTY_LIST', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIELD_CANNOT_BE_CLEARED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLACKLISTED_VALUE', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=140,
  serialized_end=341,
)
_sym_db.RegisterEnumDescriptor(_FIELDERRORENUM_FIELDERROR)


_FIELDERRORENUM = _descriptor.Descriptor(
  name='FieldErrorEnum',
  full_name='google.ads.googleads.v2.errors.FieldErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIELDERRORENUM_FIELDERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=341,
)

_FIELDERRORENUM_FIELDERROR.containing_type = _FIELDERRORENUM
DESCRIPTOR.message_types_by_name['FieldErrorEnum'] = _FIELDERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FieldErrorEnum = _reflection.GeneratedProtocolMessageType('FieldErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _FIELDERRORENUM,
  __module__ = 'google.ads.googleads_v2.proto.errors.field_error_pb2'
  ,
  __doc__ = """Container for enum describing possible field errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.errors.FieldErrorEnum)
  ))
_sym_db.RegisterMessage(FieldErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
