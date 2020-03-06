# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/feed_placeholder_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import placeholder_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_placeholder__type__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/feed_placeholder_view.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\030FeedPlaceholderViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nCgoogle/ads/googleads_v3/proto/resources/feed_placeholder_view.proto\x12!google.ads.googleads.v3.resources\x1a:google/ads/googleads_v3/proto/enums/placeholder_type.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\x80\x02\n\x13\x46\x65\x65\x64PlaceholderView\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\\\n\x10placeholder_type\x18\x02 \x01(\x0e\x32\x42.google.ads.googleads.v3.enums.PlaceholderTypeEnum.PlaceholderType:t\xea\x41q\n,googleads.googleapis.com/FeedPlaceholderView\x12\x41\x63ustomers/{customer}/feedPlaceholderViews/{feed_placeholder_view}B\x85\x02\n%com.google.ads.googleads.v3.resourcesB\x18\x46\x65\x65\x64PlaceholderViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_placeholder__type__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_FEEDPLACEHOLDERVIEW = _descriptor.Descriptor(
  name='FeedPlaceholderView',
  full_name='google.ads.googleads.v3.resources.FeedPlaceholderView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.FeedPlaceholderView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placeholder_type', full_name='google.ads.googleads.v3.resources.FeedPlaceholderView.placeholder_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352Aq\n,googleads.googleapis.com/FeedPlaceholderView\022Acustomers/{customer}/feedPlaceholderViews/{feed_placeholder_view}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=480,
)

_FEEDPLACEHOLDERVIEW.fields_by_name['placeholder_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_placeholder__type__pb2._PLACEHOLDERTYPEENUM_PLACEHOLDERTYPE
DESCRIPTOR.message_types_by_name['FeedPlaceholderView'] = _FEEDPLACEHOLDERVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedPlaceholderView = _reflection.GeneratedProtocolMessageType('FeedPlaceholderView', (_message.Message,), dict(
  DESCRIPTOR = _FEEDPLACEHOLDERVIEW,
  __module__ = 'google.ads.googleads_v3.proto.resources.feed_placeholder_view_pb2'
  ,
  __doc__ = """A feed placeholder view.
  
  
  Attributes:
      resource_name:
          The resource name of the feed placeholder view. Feed
          placeholder view resource names have the form:  ``customers/{c
          ustomer_id}/feedPlaceholderViews/{placeholder_type}``
      placeholder_type:
          The placeholder type of the feed placeholder view.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.FeedPlaceholderView)
  ))
_sym_db.RegisterMessage(FeedPlaceholderView)


DESCRIPTOR._options = None
_FEEDPLACEHOLDERVIEW._options = None
# @@protoc_insertion_point(module_scope)
