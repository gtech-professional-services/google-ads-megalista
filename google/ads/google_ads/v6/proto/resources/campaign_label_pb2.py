# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/campaign_label.proto
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
  name='google/ads/googleads/v6/resources/campaign_label.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\022CampaignLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n6google/ads/googleads/v6/resources/campaign_label.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd9\x02\n\rCampaignLabel\x12\x45\n\rresource_name\x18\x01 \x01(\tB.\xe0\x41\x05\xfa\x41(\n&googleads.googleapis.com/CampaignLabel\x12@\n\x08\x63\x61mpaign\x18\x04 \x01(\tB)\xe0\x41\x05\xfa\x41#\n!googleads.googleapis.com/CampaignH\x00\x88\x01\x01\x12:\n\x05label\x18\x05 \x01(\tB&\xe0\x41\x05\xfa\x41 \n\x1egoogleads.googleapis.com/LabelH\x01\x88\x01\x01:l\xea\x41i\n&googleads.googleapis.com/CampaignLabel\x12?customers/{customer_id}/campaignLabels/{campaign_id}~{label_id}B\x0b\n\t_campaignB\x08\n\x06_labelB\xff\x01\n%com.google.ads.googleads.v6.resourcesB\x12\x43\x61mpaignLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNLABEL = _descriptor.Descriptor(
  name='CampaignLabel',
  full_name='google.ads.googleads.v6.resources.CampaignLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.CampaignLabel.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A(\n&googleads.googleapis.com/CampaignLabel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v6.resources.CampaignLabel.campaign', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A#\n!googleads.googleapis.com/Campaign', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.ads.googleads.v6.resources.CampaignLabel.label', index=2,
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
  serialized_options=b'\352Ai\n&googleads.googleapis.com/CampaignLabel\022?customers/{customer_id}/campaignLabels/{campaign_id}~{label_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_campaign', full_name='google.ads.googleads.v6.resources.CampaignLabel._campaign',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_label', full_name='google.ads.googleads.v6.resources.CampaignLabel._label',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=184,
  serialized_end=529,
)

_CAMPAIGNLABEL.oneofs_by_name['_campaign'].fields.append(
  _CAMPAIGNLABEL.fields_by_name['campaign'])
_CAMPAIGNLABEL.fields_by_name['campaign'].containing_oneof = _CAMPAIGNLABEL.oneofs_by_name['_campaign']
_CAMPAIGNLABEL.oneofs_by_name['_label'].fields.append(
  _CAMPAIGNLABEL.fields_by_name['label'])
_CAMPAIGNLABEL.fields_by_name['label'].containing_oneof = _CAMPAIGNLABEL.oneofs_by_name['_label']
DESCRIPTOR.message_types_by_name['CampaignLabel'] = _CAMPAIGNLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignLabel = _reflection.GeneratedProtocolMessageType('CampaignLabel', (_message.Message,), {
  'DESCRIPTOR' : _CAMPAIGNLABEL,
  '__module__' : 'google.ads.googleads.v6.resources.campaign_label_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.CampaignLabel)
  })
_sym_db.RegisterMessage(CampaignLabel)


DESCRIPTOR._options = None
_CAMPAIGNLABEL.fields_by_name['resource_name']._options = None
_CAMPAIGNLABEL.fields_by_name['campaign']._options = None
_CAMPAIGNLABEL.fields_by_name['label']._options = None
_CAMPAIGNLABEL._options = None
# @@protoc_insertion_point(module_scope)
