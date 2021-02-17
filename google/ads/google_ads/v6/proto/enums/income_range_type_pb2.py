# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/enums/income_range_type.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/enums/income_range_type.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\024IncomeRangeTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5google/ads/googleads/v6/enums/income_range_type.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\x83\x02\n\x13IncomeRangeTypeEnum\"\xeb\x01\n\x0fIncomeRangeType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x17\n\x11INCOME_RANGE_0_50\x10\xb1\x90\x1f\x12\x18\n\x12INCOME_RANGE_50_60\x10\xb2\x90\x1f\x12\x18\n\x12INCOME_RANGE_60_70\x10\xb3\x90\x1f\x12\x18\n\x12INCOME_RANGE_70_80\x10\xb4\x90\x1f\x12\x18\n\x12INCOME_RANGE_80_90\x10\xb5\x90\x1f\x12\x18\n\x12INCOME_RANGE_90_UP\x10\xb6\x90\x1f\x12\x1f\n\x19INCOME_RANGE_UNDETERMINED\x10\xb0\x90\x1f\x42\xe9\x01\n!com.google.ads.googleads.v6.enumsB\x14IncomeRangeTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_INCOMERANGETYPEENUM_INCOMERANGETYPE = _descriptor.EnumDescriptor(
  name='IncomeRangeType',
  full_name='google.ads.googleads.v6.enums.IncomeRangeTypeEnum.IncomeRangeType',
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
      name='INCOME_RANGE_0_50', index=2, number=510001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_50_60', index=3, number=510002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_60_70', index=4, number=510003,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_70_80', index=5, number=510004,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_80_90', index=6, number=510005,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_90_UP', index=7, number=510006,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCOME_RANGE_UNDETERMINED', index=8, number=510000,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=143,
  serialized_end=378,
)
_sym_db.RegisterEnumDescriptor(_INCOMERANGETYPEENUM_INCOMERANGETYPE)


_INCOMERANGETYPEENUM = _descriptor.Descriptor(
  name='IncomeRangeTypeEnum',
  full_name='google.ads.googleads.v6.enums.IncomeRangeTypeEnum',
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
    _INCOMERANGETYPEENUM_INCOMERANGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=378,
)

_INCOMERANGETYPEENUM_INCOMERANGETYPE.containing_type = _INCOMERANGETYPEENUM
DESCRIPTOR.message_types_by_name['IncomeRangeTypeEnum'] = _INCOMERANGETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IncomeRangeTypeEnum = _reflection.GeneratedProtocolMessageType('IncomeRangeTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _INCOMERANGETYPEENUM,
  '__module__' : 'google.ads.googleads.v6.enums.income_range_type_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.IncomeRangeTypeEnum)
  })
_sym_db.RegisterMessage(IncomeRangeTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
