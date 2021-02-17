# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/ad_group_label.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/resources/ad_group_label.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\021AdGroupLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads/v6/resources/ad_group_label.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd4\x02\n\x0c\x41\x64GroupLabel\x12\x44\n\rresource_name\x18\x01 \x01(\tB-\xe0\x41\x05\xfa\x41\'\n%googleads.googleapis.com/AdGroupLabel\x12?\n\x08\x61\x64_group\x18\x04 \x01(\tB(\xe0\x41\x05\xfa\x41\"\n googleads.googleapis.com/AdGroupH\x00\x88\x01\x01\x12:\n\x05label\x18\x05 \x01(\tB&\xe0\x41\x05\xfa\x41 \n\x1egoogleads.googleapis.com/LabelH\x01\x88\x01\x01:j\xea\x41g\n%googleads.googleapis.com/AdGroupLabel\x12>customers/{customer_id}/adGroupLabels/{ad_group_id}~{label_id}B\x0b\n\t_ad_groupB\x08\n\x06_labelB\xfe\x01\n%com.google.ads.googleads.v6.resourcesB\x11\x41\x64GroupLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPLABEL = _descriptor.Descriptor(
  name='AdGroupLabel',
  full_name='google.ads.googleads.v6.resources.AdGroupLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.AdGroupLabel.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A\'\n%googleads.googleapis.com/AdGroupLabel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v6.resources.AdGroupLabel.ad_group', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A\"\n googleads.googleapis.com/AdGroup', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.ads.googleads.v6.resources.AdGroupLabel.label', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A \n\036googleads.googleapis.com/Label', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ag\n%googleads.googleapis.com/AdGroupLabel\022>customers/{customer_id}/adGroupLabels/{ad_group_id}~{label_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_ad_group', full_name='google.ads.googleads.v6.resources.AdGroupLabel._ad_group',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_label', full_name='google.ads.googleads.v6.resources.AdGroupLabel._label',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=184,
  serialized_end=524,
)

_ADGROUPLABEL.oneofs_by_name['_ad_group'].fields.append(
  _ADGROUPLABEL.fields_by_name['ad_group'])
_ADGROUPLABEL.fields_by_name['ad_group'].containing_oneof = _ADGROUPLABEL.oneofs_by_name['_ad_group']
_ADGROUPLABEL.oneofs_by_name['_label'].fields.append(
  _ADGROUPLABEL.fields_by_name['label'])
_ADGROUPLABEL.fields_by_name['label'].containing_oneof = _ADGROUPLABEL.oneofs_by_name['_label']
DESCRIPTOR.message_types_by_name['AdGroupLabel'] = _ADGROUPLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupLabel = _reflection.GeneratedProtocolMessageType('AdGroupLabel', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPLABEL,
  '__module__' : 'google.ads.googleads.v6.resources.ad_group_label_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.AdGroupLabel)
  })
_sym_db.RegisterMessage(AdGroupLabel)


DESCRIPTOR._options = None
_ADGROUPLABEL.fields_by_name['resource_name']._options = None
_ADGROUPLABEL.fields_by_name['ad_group']._options = None
_ADGROUPLABEL.fields_by_name['label']._options = None
_ADGROUPLABEL._options = None
# @@protoc_insertion_point(module_scope)
