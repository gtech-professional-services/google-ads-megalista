# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/errors/bidding_strategy_error.proto

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
  name='google/ads/googleads_v2/proto/errors/bidding_strategy_error.proto',
  package='google.ads.googleads.v2.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v2.errorsB\031BiddingStrategyErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V2.Errors\312\002\036Google\\Ads\\GoogleAds\\V2\\Errors\352\002\"Google::Ads::GoogleAds::V2::Errors'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v2/proto/errors/bidding_strategy_error.proto\x12\x1egoogle.ads.googleads.v2.errors\x1a\x1cgoogle/api/annotations.proto\"\x9b\x02\n\x18\x42iddingStrategyErrorEnum\"\xfe\x01\n\x14\x42iddingStrategyError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x12\n\x0e\x44UPLICATE_NAME\x10\x02\x12\'\n#CANNOT_CHANGE_BIDDING_STRATEGY_TYPE\x10\x03\x12%\n!CANNOT_REMOVE_ASSOCIATED_STRATEGY\x10\x04\x12\"\n\x1e\x42IDDING_STRATEGY_NOT_SUPPORTED\x10\x05\x12@\n<INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE\x10\x06\x42\xf4\x01\n\"com.google.ads.googleads.v2.errorsB\x19\x42iddingStrategyErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v2/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V2.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V2\\Errors\xea\x02\"Google::Ads::GoogleAds::V2::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_BIDDINGSTRATEGYERRORENUM_BIDDINGSTRATEGYERROR = _descriptor.EnumDescriptor(
  name='BiddingStrategyError',
  full_name='google.ads.googleads.v2.errors.BiddingStrategyErrorEnum.BiddingStrategyError',
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
      name='DUPLICATE_NAME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CHANGE_BIDDING_STRATEGY_TYPE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REMOVE_ASSOCIATED_STRATEGY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIDDING_STRATEGY_NOT_SUPPORTED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=161,
  serialized_end=415,
)
_sym_db.RegisterEnumDescriptor(_BIDDINGSTRATEGYERRORENUM_BIDDINGSTRATEGYERROR)


_BIDDINGSTRATEGYERRORENUM = _descriptor.Descriptor(
  name='BiddingStrategyErrorEnum',
  full_name='google.ads.googleads.v2.errors.BiddingStrategyErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BIDDINGSTRATEGYERRORENUM_BIDDINGSTRATEGYERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=415,
)

_BIDDINGSTRATEGYERRORENUM_BIDDINGSTRATEGYERROR.containing_type = _BIDDINGSTRATEGYERRORENUM
DESCRIPTOR.message_types_by_name['BiddingStrategyErrorEnum'] = _BIDDINGSTRATEGYERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingStrategyErrorEnum = _reflection.GeneratedProtocolMessageType('BiddingStrategyErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _BIDDINGSTRATEGYERRORENUM,
  __module__ = 'google.ads.googleads_v2.proto.errors.bidding_strategy_error_pb2'
  ,
  __doc__ = """Container for enum describing possible bidding strategy errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.errors.BiddingStrategyErrorEnum)
  ))
_sym_db.RegisterMessage(BiddingStrategyErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
