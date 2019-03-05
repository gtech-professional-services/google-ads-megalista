# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/services/domain_category_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.resources import domain_category_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_domain__category__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/services/domain_category_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v1.servicesB\032DomainCategoryServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services'),
  serialized_pb=_b('\nDgoogle/ads/googleads_v1/proto/services/domain_category_service.proto\x12 google.ads.googleads.v1.services\x1a=google/ads/googleads_v1/proto/resources/domain_category.proto\x1a\x1cgoogle/api/annotations.proto\"1\n\x18GetDomainCategoryRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xd8\x01\n\x15\x44omainCategoryService\x12\xbe\x01\n\x11GetDomainCategory\x12:.google.ads.googleads.v1.services.GetDomainCategoryRequest\x1a\x31.google.ads.googleads.v1.resources.DomainCategory\":\x82\xd3\xe4\x93\x02\x34\x12\x32/v1/{resource_name=customers/*/domainCategories/*}B\x81\x02\n$com.google.ads.googleads.v1.servicesB\x1a\x44omainCategoryServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_domain__category__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETDOMAINCATEGORYREQUEST = _descriptor.Descriptor(
  name='GetDomainCategoryRequest',
  full_name='google.ads.googleads.v1.services.GetDomainCategoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetDomainCategoryRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=199,
  serialized_end=248,
)

DESCRIPTOR.message_types_by_name['GetDomainCategoryRequest'] = _GETDOMAINCATEGORYREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetDomainCategoryRequest = _reflection.GeneratedProtocolMessageType('GetDomainCategoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETDOMAINCATEGORYREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.domain_category_service_pb2'
  ,
  __doc__ = """Request message for
  [DomainCategoryService.GetDomainCategory][google.ads.googleads.v1.services.DomainCategoryService.GetDomainCategory].
  
  
  Attributes:
      resource_name:
          Resource name of the domain category to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetDomainCategoryRequest)
  ))
_sym_db.RegisterMessage(GetDomainCategoryRequest)


DESCRIPTOR._options = None

_DOMAINCATEGORYSERVICE = _descriptor.ServiceDescriptor(
  name='DomainCategoryService',
  full_name='google.ads.googleads.v1.services.DomainCategoryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=251,
  serialized_end=467,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetDomainCategory',
    full_name='google.ads.googleads.v1.services.DomainCategoryService.GetDomainCategory',
    index=0,
    containing_service=None,
    input_type=_GETDOMAINCATEGORYREQUEST,
    output_type=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_domain__category__pb2._DOMAINCATEGORY,
    serialized_options=_b('\202\323\344\223\0024\0222/v1/{resource_name=customers/*/domainCategories/*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_DOMAINCATEGORYSERVICE)

DESCRIPTOR.services_by_name['DomainCategoryService'] = _DOMAINCATEGORYSERVICE

# @@protoc_insertion_point(module_scope)
