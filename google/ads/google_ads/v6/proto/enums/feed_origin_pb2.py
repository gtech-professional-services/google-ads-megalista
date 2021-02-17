# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/feed_origin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/feed_origin.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\017FeedOriginProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/google/ads/googleads/v6/enums/feed_origin.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"R\n\x0e\x46\x65\x65\x64OriginEnum\"@\n\nFeedOrigin\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x08\n\x04USER\x10\x02\x12\n\n\x06GOOGLE\x10\x03\x42\xe4\x01\n!com.google.ads.googleads.v6.enumsB\x0f\x46\x65\x65\x64OriginProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDORIGINENUM_FEEDORIGIN = _descriptor.EnumDescriptor(
  name='FeedOrigin',
  full_name='google.ads.googleads.v6.enums.FeedOriginEnum.FeedOrigin',
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
      name='USER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=130,
  serialized_end=194,
)
_sym_db.RegisterEnumDescriptor(_FEEDORIGINENUM_FEEDORIGIN)


_FEEDORIGINENUM = _descriptor.Descriptor(
  name='FeedOriginEnum',
  full_name='google.ads.googleads.v6.enums.FeedOriginEnum',
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
    _FEEDORIGINENUM_FEEDORIGIN,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=194,
)

_FEEDORIGINENUM_FEEDORIGIN.containing_type = _FEEDORIGINENUM
DESCRIPTOR.message_types_by_name['FeedOriginEnum'] = _FEEDORIGINENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedOriginEnum = _reflection.GeneratedProtocolMessageType('FeedOriginEnum', (_message.Message,), {
  'DESCRIPTOR' : _FEEDORIGINENUM,
  '__module__' : 'google.ads.googleads.v6.enums.feed_origin_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.FeedOriginEnum)
  })
_sym_db.RegisterMessage(FeedOriginEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
