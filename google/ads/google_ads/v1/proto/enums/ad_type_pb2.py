# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/ad_type.proto

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
  name='google/ads/googleads_v1/proto/enums/ad_type.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\013AdTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n1google/ads/googleads_v1/proto/enums/ad_type.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\xb2\x03\n\nAdTypeEnum\"\xa3\x03\n\x06\x41\x64Type\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0b\n\x07TEXT_AD\x10\x02\x12\x14\n\x10\x45XPANDED_TEXT_AD\x10\x03\x12\x10\n\x0c\x43\x41LL_ONLY_AD\x10\x06\x12\x1e\n\x1a\x45XPANDED_DYNAMIC_SEARCH_AD\x10\x07\x12\x0c\n\x08HOTEL_AD\x10\x08\x12\x15\n\x11SHOPPING_SMART_AD\x10\t\x12\x17\n\x13SHOPPING_PRODUCT_AD\x10\n\x12\x0c\n\x08VIDEO_AD\x10\x0c\x12\x0c\n\x08GMAIL_AD\x10\r\x12\x0c\n\x08IMAGE_AD\x10\x0e\x12\x18\n\x14RESPONSIVE_SEARCH_AD\x10\x0f\x12 \n\x1cLEGACY_RESPONSIVE_DISPLAY_AD\x10\x10\x12\n\n\x06\x41PP_AD\x10\x11\x12\x19\n\x15LEGACY_APP_INSTALL_AD\x10\x12\x12\x19\n\x15RESPONSIVE_DISPLAY_AD\x10\x13\x12\x13\n\x0fHTML5_UPLOAD_AD\x10\x15\x12\x14\n\x10\x44YNAMIC_HTML5_AD\x10\x16\x12\x15\n\x11\x41PP_ENGAGEMENT_AD\x10\x17\x42\xe0\x01\n!com.google.ads.googleads.v1.enumsB\x0b\x41\x64TypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ADTYPEENUM_ADTYPE = _descriptor.EnumDescriptor(
  name='AdType',
  full_name='google.ads.googleads.v1.enums.AdTypeEnum.AdType',
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
      name='TEXT_AD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPANDED_TEXT_AD', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALL_ONLY_AD', index=4, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPANDED_DYNAMIC_SEARCH_AD', index=5, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_AD', index=6, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_SMART_AD', index=7, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOPPING_PRODUCT_AD', index=8, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_AD', index=9, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GMAIL_AD', index=10, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_AD', index=11, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSIVE_SEARCH_AD', index=12, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEGACY_RESPONSIVE_DISPLAY_AD', index=13, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_AD', index=14, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEGACY_APP_INSTALL_AD', index=15, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESPONSIVE_DISPLAY_AD', index=16, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML5_UPLOAD_AD', index=17, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DYNAMIC_HTML5_AD', index=18, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APP_ENGAGEMENT_AD', index=19, number=23,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=130,
  serialized_end=549,
)
_sym_db.RegisterEnumDescriptor(_ADTYPEENUM_ADTYPE)


_ADTYPEENUM = _descriptor.Descriptor(
  name='AdTypeEnum',
  full_name='google.ads.googleads.v1.enums.AdTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ADTYPEENUM_ADTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=549,
)

_ADTYPEENUM_ADTYPE.containing_type = _ADTYPEENUM
DESCRIPTOR.message_types_by_name['AdTypeEnum'] = _ADTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdTypeEnum = _reflection.GeneratedProtocolMessageType('AdTypeEnum', (_message.Message,), dict(
  DESCRIPTOR = _ADTYPEENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.ad_type_pb2'
  ,
  __doc__ = """Container for enum describing possible types of an ad.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.AdTypeEnum)
  ))
_sym_db.RegisterMessage(AdTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
