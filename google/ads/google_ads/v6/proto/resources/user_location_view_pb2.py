# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/resources/user_location_view.proto
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
  name='google/ads/googleads/v6/resources/user_location_view.proto',
  package='google.ads.googleads.v6.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v6.resourcesB\025UserLocationViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V6.Resources\312\002!Google\\Ads\\GoogleAds\\V6\\Resources\352\002%Google::Ads::GoogleAds::V6::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:google/ads/googleads/v6/resources/user_location_view.proto\x12!google.ads.googleads.v6.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xe6\x02\n\x10UserLocationView\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0\x41\x03\xfa\x41+\n)googleads.googleapis.com/UserLocationView\x12&\n\x14\x63ountry_criterion_id\x18\x04 \x01(\x03\x42\x03\xe0\x41\x03H\x00\x88\x01\x01\x12$\n\x12targeting_location\x18\x05 \x01(\x08\x42\x03\xe0\x41\x03H\x01\x88\x01\x01:\x89\x01\xea\x41\x85\x01\n)googleads.googleapis.com/UserLocationView\x12Xcustomers/{customer_id}/userLocationViews/{country_criterion_id}~{is_targeting_location}B\x17\n\x15_country_criterion_idB\x15\n\x13_targeting_locationB\x82\x02\n%com.google.ads.googleads.v6.resourcesB\x15UserLocationViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v6/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V6.Resources\xca\x02!Google\\Ads\\GoogleAds\\V6\\Resources\xea\x02%Google::Ads::GoogleAds::V6::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_USERLOCATIONVIEW = _descriptor.Descriptor(
  name='UserLocationView',
  full_name='google.ads.googleads.v6.resources.UserLocationView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.resources.UserLocationView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003\372A+\n)googleads.googleapis.com/UserLocationView', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_criterion_id', full_name='google.ads.googleads.v6.resources.UserLocationView.country_criterion_id', index=1,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targeting_location', full_name='google.ads.googleads.v6.resources.UserLocationView.targeting_location', index=2,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\205\001\n)googleads.googleapis.com/UserLocationView\022Xcustomers/{customer_id}/userLocationViews/{country_criterion_id}~{is_targeting_location}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_country_criterion_id', full_name='google.ads.googleads.v6.resources.UserLocationView._country_criterion_id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_targeting_location', full_name='google.ads.googleads.v6.resources.UserLocationView._targeting_location',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=188,
  serialized_end=546,
)

_USERLOCATIONVIEW.oneofs_by_name['_country_criterion_id'].fields.append(
  _USERLOCATIONVIEW.fields_by_name['country_criterion_id'])
_USERLOCATIONVIEW.fields_by_name['country_criterion_id'].containing_oneof = _USERLOCATIONVIEW.oneofs_by_name['_country_criterion_id']
_USERLOCATIONVIEW.oneofs_by_name['_targeting_location'].fields.append(
  _USERLOCATIONVIEW.fields_by_name['targeting_location'])
_USERLOCATIONVIEW.fields_by_name['targeting_location'].containing_oneof = _USERLOCATIONVIEW.oneofs_by_name['_targeting_location']
DESCRIPTOR.message_types_by_name['UserLocationView'] = _USERLOCATIONVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserLocationView = _reflection.GeneratedProtocolMessageType('UserLocationView', (_message.Message,), {
  'DESCRIPTOR' : _USERLOCATIONVIEW,
  '__module__' : 'google.ads.googleads.v6.resources.user_location_view_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.resources.UserLocationView)
  })
_sym_db.RegisterMessage(UserLocationView)


DESCRIPTOR._options = None
_USERLOCATIONVIEW.fields_by_name['resource_name']._options = None
_USERLOCATIONVIEW.fields_by_name['country_criterion_id']._options = None
_USERLOCATIONVIEW.fields_by_name['targeting_location']._options = None
_USERLOCATIONVIEW._options = None
# @@protoc_insertion_point(module_scope)
