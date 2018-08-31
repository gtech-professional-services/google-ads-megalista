# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/recommendation_type.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/enums/recommendation_type.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n=google/ads/googleads_v0/proto/enums/recommendation_type.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\x9f\x02\n\x16RecommendationTypeEnum\"\x84\x02\n\x12RecommendationType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x13\n\x0f\x43\x41MPAIGN_BUDGET\x10\x02\x12\x0b\n\x07KEYWORD\x10\x03\x12\x0b\n\x07TEXT_AD\x10\x04\x12\x15\n\x11TARGET_CPA_OPT_IN\x10\x05\x12\x1f\n\x1bMAXIMIZE_CONVERSIONS_OPT_IN\x10\x06\x12\x17\n\x13\x45NHANCED_CPC_OPT_IN\x10\x07\x12\x1a\n\x16SEARCH_PARTNERS_OPT_IN\x10\x08\x12\x1a\n\x16MAXIMIZE_CLICKS_OPT_IN\x10\t\x12\x18\n\x14OPTIMIZE_AD_ROTATION\x10\nB\xc8\x01\n!com.google.ads.googleads.v0.enumsB\x17RecommendationTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE = _descriptor.EnumDescriptor(
  name='RecommendationType',
  full_name='google.ads.googleads.v0.enums.RecommendationTypeEnum.RecommendationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_BUDGET', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_AD', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TARGET_CPA_OPT_IN', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE_CONVERSIONS_OPT_IN', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENHANCED_CPC_OPT_IN', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_PARTNERS_OPT_IN', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE_CLICKS_OPT_IN', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPTIMIZE_AD_ROTATION', index=10, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=124,
  serialized_end=384,
)
_sym_db.RegisterEnumDescriptor(_RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE)


_RECOMMENDATIONTYPEENUM = _descriptor.Descriptor(
  name='RecommendationTypeEnum',
  full_name='google.ads.googleads.v0.enums.RecommendationTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=384,
)

_RECOMMENDATIONTYPEENUM_RECOMMENDATIONTYPE.containing_type = _RECOMMENDATIONTYPEENUM
DESCRIPTOR.message_types_by_name['RecommendationTypeEnum'] = _RECOMMENDATIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecommendationTypeEnum = _reflection.GeneratedProtocolMessageType('RecommendationTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _RECOMMENDATIONTYPEENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.recommendation_type_pb2'
  ,
  __doc__ = """Container for enum describing types of recommendations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.RecommendationTypeEnum)
  ))
_sym_db.RegisterMessage(RecommendationTypeEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\027RecommendationTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
