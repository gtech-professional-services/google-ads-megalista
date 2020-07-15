# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/services/expanded_landing_page_view_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.resources import expanded_landing_page_view_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_expanded__landing__page__view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/services/expanded_landing_page_view_service.proto',
  package='google.ads.googleads.v4.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v4.servicesB#ExpandedLandingPageViewServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V4.Services\312\002 Google\\Ads\\GoogleAds\\V4\\Services\352\002$Google::Ads::GoogleAds::V4::Services'),
  serialized_pb=_b('\nOgoogle/ads/googleads_v4/proto/services/expanded_landing_page_view_service.proto\x12 google.ads.googleads.v4.services\x1aHgoogle/ads/googleads_v4/proto/resources/expanded_landing_page_view.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"t\n!GetExpandedLandingPageViewRequest\x12O\n\rresource_name\x18\x01 \x01(\tB8\xe0\x41\x02\xfa\x41\x32\n0googleads.googleapis.com/ExpandedLandingPageView2\xb1\x02\n\x1e\x45xpandedLandingPageViewService\x12\xf1\x01\n\x1aGetExpandedLandingPageView\x12\x43.google.ads.googleads.v4.services.GetExpandedLandingPageViewRequest\x1a:.google.ads.googleads.v4.resources.ExpandedLandingPageView\"R\x82\xd3\xe4\x93\x02<\x12:/v4/{resource_name=customers/*/expandedLandingPageViews/*}\xda\x41\rresource_name\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x8a\x02\n$com.google.ads.googleads.v4.servicesB#ExpandedLandingPageViewServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V4.Services\xca\x02 Google\\Ads\\GoogleAds\\V4\\Services\xea\x02$Google::Ads::GoogleAds::V4::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_expanded__landing__page__view__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETEXPANDEDLANDINGPAGEVIEWREQUEST = _descriptor.Descriptor(
  name='GetExpandedLandingPageViewRequest',
  full_name='google.ads.googleads.v4.services.GetExpandedLandingPageViewRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.GetExpandedLandingPageViewRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A2\n0googleads.googleapis.com/ExpandedLandingPageView'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=306,
  serialized_end=422,
)

DESCRIPTOR.message_types_by_name['GetExpandedLandingPageViewRequest'] = _GETEXPANDEDLANDINGPAGEVIEWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetExpandedLandingPageViewRequest = _reflection.GeneratedProtocolMessageType('GetExpandedLandingPageViewRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETEXPANDEDLANDINGPAGEVIEWREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.expanded_landing_page_view_service_pb2'
  ,
  __doc__ = """Request message for
  [ExpandedLandingPageViewService.GetExpandedLandingPageView][google.ads.googleads.v4.services.ExpandedLandingPageViewService.GetExpandedLandingPageView].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the expanded landing page view
          to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.GetExpandedLandingPageViewRequest)
  ))
_sym_db.RegisterMessage(GetExpandedLandingPageViewRequest)


DESCRIPTOR._options = None
_GETEXPANDEDLANDINGPAGEVIEWREQUEST.fields_by_name['resource_name']._options = None

_EXPANDEDLANDINGPAGEVIEWSERVICE = _descriptor.ServiceDescriptor(
  name='ExpandedLandingPageViewService',
  full_name='google.ads.googleads.v4.services.ExpandedLandingPageViewService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=425,
  serialized_end=730,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetExpandedLandingPageView',
    full_name='google.ads.googleads.v4.services.ExpandedLandingPageViewService.GetExpandedLandingPageView',
    index=0,
    containing_service=None,
    input_type=_GETEXPANDEDLANDINGPAGEVIEWREQUEST,
    output_type=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_expanded__landing__page__view__pb2._EXPANDEDLANDINGPAGEVIEW,
    serialized_options=_b('\202\323\344\223\002<\022:/v4/{resource_name=customers/*/expandedLandingPageViews/*}\332A\rresource_name'),
  ),
])
_sym_db.RegisterServiceDescriptor(_EXPANDEDLANDINGPAGEVIEWSERVICE)

DESCRIPTOR.services_by_name['ExpandedLandingPageViewService'] = _EXPANDEDLANDINGPAGEVIEWSERVICE

# @@protoc_insertion_point(module_scope)
