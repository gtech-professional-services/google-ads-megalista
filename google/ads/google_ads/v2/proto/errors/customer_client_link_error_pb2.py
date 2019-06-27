# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/errors/customer_client_link_error.proto

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
  name='google/ads/googleads_v2/proto/errors/customer_client_link_error.proto',
  package='google.ads.googleads.v2.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v2.errorsB\034CustomerClientLinkErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Errors\312\002\036Google\\Ads\\GoogleAds\\V2\\Errors\352\002\"Google::Ads::GoogleAds::V2::Errors'),
  serialized_pb=_b('\nEgoogle/ads/googleads_v2/proto/errors/customer_client_link_error.proto\x12\x1egoogle.ads.googleads.v2.errors\x1a\x1cgoogle/api/annotations.proto\"\xed\x02\n\x1b\x43ustomerClientLinkErrorEnum\"\xcd\x02\n\x17\x43ustomerClientLinkError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12*\n&CLIENT_ALREADY_INVITED_BY_THIS_MANAGER\x10\x02\x12\'\n#CLIENT_ALREADY_MANAGED_IN_HIERARCHY\x10\x03\x12\x1b\n\x17\x43YCLIC_LINK_NOT_ALLOWED\x10\x04\x12\"\n\x1e\x43USTOMER_HAS_TOO_MANY_ACCOUNTS\x10\x05\x12#\n\x1f\x43LIENT_HAS_TOO_MANY_INVITATIONS\x10\x06\x12*\n&CANNOT_HIDE_OR_UNHIDE_MANAGER_ACCOUNTS\x10\x07\x12-\n)CUSTOMER_HAS_TOO_MANY_ACCOUNTS_AT_MANAGER\x10\x08\x42\xf7\x01\n\"com.google.ads.googleads.v2.errorsB\x1c\x43ustomerClientLinkErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Errors\xea\x02\"Google::Ads::GoogleAds::V2::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CUSTOMERCLIENTLINKERRORENUM_CUSTOMERCLIENTLINKERROR = _descriptor.EnumDescriptor(
  name='CustomerClientLinkError',
  full_name='google.ads.googleads.v2.errors.CustomerClientLinkErrorEnum.CustomerClientLinkError',
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
      name='CLIENT_ALREADY_INVITED_BY_THIS_MANAGER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_ALREADY_MANAGED_IN_HIERARCHY', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CYCLIC_LINK_NOT_ALLOWED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_HAS_TOO_MANY_ACCOUNTS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_HAS_TOO_MANY_INVITATIONS', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_HIDE_OR_UNHIDE_MANAGER_ACCOUNTS', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_HAS_TOO_MANY_ACCOUNTS_AT_MANAGER', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=168,
  serialized_end=501,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMERCLIENTLINKERRORENUM_CUSTOMERCLIENTLINKERROR)


_CUSTOMERCLIENTLINKERRORENUM = _descriptor.Descriptor(
  name='CustomerClientLinkErrorEnum',
  full_name='google.ads.googleads.v2.errors.CustomerClientLinkErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMERCLIENTLINKERRORENUM_CUSTOMERCLIENTLINKERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=501,
)

_CUSTOMERCLIENTLINKERRORENUM_CUSTOMERCLIENTLINKERROR.containing_type = _CUSTOMERCLIENTLINKERRORENUM
DESCRIPTOR.message_types_by_name['CustomerClientLinkErrorEnum'] = _CUSTOMERCLIENTLINKERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerClientLinkErrorEnum = _reflection.GeneratedProtocolMessageType('CustomerClientLinkErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERCLIENTLINKERRORENUM,
  __module__ = 'google.ads.googleads_v2.proto.errors.customer_client_link_error_pb2'
  ,
  __doc__ = """Container for enum describing possible CustomeClientLink errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.errors.CustomerClientLinkErrorEnum)
  ))
_sym_db.RegisterMessage(CustomerClientLinkErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
