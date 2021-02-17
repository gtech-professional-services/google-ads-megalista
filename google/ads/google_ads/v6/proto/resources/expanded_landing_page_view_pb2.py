# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/expanded_landing_page_view.proto
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
  name='google/ads/googleads/v6/resources/expanded_landing_page_view.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\034ExpandedLandingPageViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nBgoogle/ads/googleads/v6/resources/expanded_landing_page_view.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xb3\x02\n\x17\x45xpandedLandingPageView\x12O\n\rresource_name\x18\x01 \x01(\tB8\xe0\x41\x03\xfa\x41\x32\n0googleads.googleapis.com/ExpandedLandingPageView\x12$\n\x12\x65xpanded_final_url\x18\x03 \x01(\tB\x03\xe0\x41\x03H\x00\x88\x01\x01:\x89\x01\xea\x41\x85\x01\n0googleads.googleapis.com/ExpandedLandingPageView\x12Qcustomers/{customer_id}/expandedLandingPageViews/{expanded_final_url_fingerprint}B\x15\n\x13_expanded_final_urlB\x89\x02\n%com.google.ads.googleads.v6.resourcesB\x1c\x45xpandedLandingPageViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_EXPANDEDLANDINGPAGEVIEW = _descriptor.Descriptor(
  name='ExpandedLandingPageView',
  full_name='google.ads.googleads.v6.resources.ExpandedLandingPageView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.ExpandedLandingPageView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A2\n0googleads.googleapis.com/ExpandedLandingPageView', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expanded_final_url', full_name='google.ads.googleads.v6.resources.ExpandedLandingPageView.expanded_final_url', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\205\001\n0googleads.googleapis.com/ExpandedLandingPageView\022Qcustomers/{customer_id}/expandedLandingPageViews/{expanded_final_url_fingerprint}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_expanded_final_url', full_name='google.ads.googleads.v6.resources.ExpandedLandingPageView._expanded_final_url',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=196,
  serialized_end=503,
)

_EXPANDEDLANDINGPAGEVIEW.oneofs_by_name['_expanded_final_url'].fields.append(
  _EXPANDEDLANDINGPAGEVIEW.fields_by_name['expanded_final_url'])
_EXPANDEDLANDINGPAGEVIEW.fields_by_name['expanded_final_url'].containing_oneof = _EXPANDEDLANDINGPAGEVIEW.oneofs_by_name['_expanded_final_url']
DESCRIPTOR.message_types_by_name['ExpandedLandingPageView'] = _EXPANDEDLANDINGPAGEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExpandedLandingPageView = _reflection.GeneratedProtocolMessageType('ExpandedLandingPageView', (_message.Message,), {
  'DESCRIPTOR' : _EXPANDEDLANDINGPAGEVIEW,
  '__module__' : 'google.ads.googleads.v6.resources.expanded_landing_page_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.ExpandedLandingPageView)
  })
_sym_db.RegisterMessage(ExpandedLandingPageView)


DESCRIPTOR._options = None
_EXPANDEDLANDINGPAGEVIEW.fields_by_name['resource_name']._options = None
_EXPANDEDLANDINGPAGEVIEW.fields_by_name['expanded_final_url']._options = None
_EXPANDEDLANDINGPAGEVIEW._options = None
# @@protoc_insertion_point(module_scope)
