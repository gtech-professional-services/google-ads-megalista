# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/campaign_shared_set.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import campaign_shared_set_status_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_campaign__shared__set__status__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/campaign_shared_set.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\026CampaignSharedSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nAgoogle/ads/googleads_v3/proto/resources/campaign_shared_set.proto\x12!google.ads.googleads.v3.resources\x1a\x44google/ads/googleads_v3/proto/enums/campaign_shared_set_status.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xe0\x02\n\x11\x43\x61mpaignSharedSet\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12.\n\x08\x63\x61mpaign\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nshared_set\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x62\n\x06status\x18\x02 \x01(\x0e\x32R.google.ads.googleads.v3.enums.CampaignSharedSetStatusEnum.CampaignSharedSetStatus:n\xea\x41k\n*googleads.googleapis.com/CampaignSharedSet\x12=customers/{customer}/campaignSharedSets/{campaign_shared_set}B\x83\x02\n%com.google.ads.googleads.v3.resourcesB\x16\x43\x61mpaignSharedSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_campaign__shared__set__status__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNSHAREDSET = _descriptor.Descriptor(
  name='CampaignSharedSet',
  full_name='google.ads.googleads.v3.resources.CampaignSharedSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.CampaignSharedSet.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='google.ads.googleads.v3.resources.CampaignSharedSet.campaign', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared_set', full_name='google.ads.googleads.v3.resources.CampaignSharedSet.shared_set', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v3.resources.CampaignSharedSet.status', index=3,
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
  serialized_options=_b('\352Ak\n*googleads.googleapis.com/CampaignSharedSet\022=customers/{customer}/campaignSharedSets/{campaign_shared_set}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=616,
)

_CAMPAIGNSHAREDSET.fields_by_name['campaign'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNSHAREDSET.fields_by_name['shared_set'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNSHAREDSET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_campaign__shared__set__status__pb2._CAMPAIGNSHAREDSETSTATUSENUM_CAMPAIGNSHAREDSETSTATUS
DESCRIPTOR.message_types_by_name['CampaignSharedSet'] = _CAMPAIGNSHAREDSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignSharedSet = _reflection.GeneratedProtocolMessageType('CampaignSharedSet', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNSHAREDSET,
  __module__ = 'google.ads.googleads_v3.proto.resources.campaign_shared_set_pb2'
  ,
  __doc__ = """CampaignSharedSets are used for managing the shared sets associated with
  a campaign.
  
  
  Attributes:
      resource_name:
          The resource name of the campaign shared set. Campaign shared
          set resource names have the form:  ``customers/{customer_id}/c
          ampaignSharedSets/{campaign_id}~{shared_set_id}``
      campaign:
          The campaign to which the campaign shared set belongs.
      shared_set:
          The shared set associated with the campaign. This may be a
          negative keyword shared set of another customer. This customer
          should be a manager of the other customer, otherwise the
          campaign shared set will exist but have no serving effect.
          Only negative keyword shared sets can be associated with
          Shopping campaigns. Only negative placement shared sets can be
          associated with Display mobile app campaigns.
      status:
          The status of this campaign shared set. Read only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.CampaignSharedSet)
  ))
_sym_db.RegisterMessage(CampaignSharedSet)


DESCRIPTOR._options = None
_CAMPAIGNSHAREDSET._options = None
# @@protoc_insertion_point(module_scope)
