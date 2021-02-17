# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/ad_schedule_view.proto
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
  name='google/ads/googleads/v6/resources/ad_schedule_view.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\023AdScheduleViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/ads/googleads/v6/resources/ad_schedule_view.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xcc\x01\n\x0e\x41\x64ScheduleView\x12\x46\n\rresource_name\x18\x01 \x01(\tB/\xe0\x41\x03\xfa\x41)\n\'googleads.googleapis.com/AdScheduleView:r\xea\x41o\n\'googleads.googleapis.com/AdScheduleView\x12\x44\x63ustomers/{customer_id}/adScheduleViews/{campaign_id}~{criterion_id}B\x80\x02\n%com.google.ads.googleads.v6.resourcesB\x13\x41\x64ScheduleViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADSCHEDULEVIEW = _descriptor.Descriptor(
  name='AdScheduleView',
  full_name='google.ads.googleads.v6.resources.AdScheduleView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.AdScheduleView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A)\n\'googleads.googleapis.com/AdScheduleView', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ao\n\'googleads.googleapis.com/AdScheduleView\022Dcustomers/{customer_id}/adScheduleViews/{campaign_id}~{criterion_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=186,
  serialized_end=390,
)

DESCRIPTOR.message_types_by_name['AdScheduleView'] = _ADSCHEDULEVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdScheduleView = _reflection.GeneratedProtocolMessageType('AdScheduleView', (_message.Message,), {
  'DESCRIPTOR' : _ADSCHEDULEVIEW,
  '__module__' : 'google.ads.googleads.v6.resources.ad_schedule_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.AdScheduleView)
  })
_sym_db.RegisterMessage(AdScheduleView)


DESCRIPTOR._options = None
_ADSCHEDULEVIEW.fields_by_name['resource_name']._options = None
_ADSCHEDULEVIEW._options = None
# @@protoc_insertion_point(module_scope)
