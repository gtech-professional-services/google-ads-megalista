# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/search_term_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import search_term_targeting_status_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_search__term__targeting__status__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/search_term_view.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\023SearchTermViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\n>google/ads/googleads_v3/proto/resources/search_term_view.proto\x12!google.ads.googleads.v3.resources\x1a\x46google/ads/googleads_v3/proto/enums/search_term_targeting_status.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xd9\x02\n\x0eSearchTermView\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x31\n\x0bsearch_term\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x61\x64_group\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x66\n\x06status\x18\x04 \x01(\x0e\x32V.google.ads.googleads.v3.enums.SearchTermTargetingStatusEnum.SearchTermTargetingStatus:e\xea\x41\x62\n\'googleads.googleapis.com/SearchTermView\x12\x37\x63ustomers/{customer}/searchTermViews/{search_term_view}B\x80\x02\n%com.google.ads.googleads.v3.resourcesB\x13SearchTermViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_search__term__targeting__status__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SEARCHTERMVIEW = _descriptor.Descriptor(
  name='SearchTermView',
  full_name='google.ads.googleads.v3.resources.SearchTermView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.SearchTermView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_term', full_name='google.ads.googleads.v3.resources.SearchTermView.search_term', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v3.resources.SearchTermView.ad_group', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v3.resources.SearchTermView.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_options=_b('\352Ab\n\'googleads.googleapis.com/SearchTermView\0227customers/{customer}/searchTermViews/{search_term_view}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=608,
)

_SEARCHTERMVIEW.fields_by_name['search_term'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEARCHTERMVIEW.fields_by_name['ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEARCHTERMVIEW.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_search__term__targeting__status__pb2._SEARCHTERMTARGETINGSTATUSENUM_SEARCHTERMTARGETINGSTATUS
DESCRIPTOR.message_types_by_name['SearchTermView'] = _SEARCHTERMVIEW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchTermView = _reflection.GeneratedProtocolMessageType('SearchTermView', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHTERMVIEW,
  __module__ = 'google.ads.googleads_v3.proto.resources.search_term_view_pb2'
  ,
  __doc__ = """A search term view with metrics aggregated by search term at the ad
  group level.
  
  
  Attributes:
      resource_name:
          The resource name of the search term view. Search term view
          resource names have the form:  ``customers/{customer_id}/searc
          hTermViews/{campaign_id}~{ad_group_id}~{URL-
          base64_search_term}``
      search_term:
          The search term.
      ad_group:
          The ad group the search term served in.
      status:
          Indicates whether the search term is currently one of your
          targeted or excluded keywords.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.SearchTermView)
  ))
_sym_db.RegisterMessage(SearchTermView)


DESCRIPTOR._options = None
_SEARCHTERMVIEW._options = None
# @@protoc_insertion_point(module_scope)
