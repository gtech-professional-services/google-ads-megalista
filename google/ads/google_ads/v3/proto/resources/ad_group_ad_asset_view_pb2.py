# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/ad_group_ad_asset_view.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.common import policy_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_policy__pb2
from google.ads.google_ads.v3.proto.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_asset__field__type__pb2
from google.ads.google_ads.v3.proto.enums import asset_performance_label_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_asset__performance__label__pb2
from google.ads.google_ads.v3.proto.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_policy__approval__status__pb2
from google.ads.google_ads.v3.proto.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_policy__review__status__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/ad_group_ad_asset_view.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\027AdGroupAdAssetViewProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\nDgoogle/ads/googleads_v3/proto/resources/ad_group_ad_asset_view.proto\x12!google.ads.googleads.v3.resources\x1a\x31google/ads/googleads_v3/proto/common/policy.proto\x1a:google/ads/googleads_v3/proto/enums/asset_field_type.proto\x1a\x41google/ads/googleads_v3/proto/enums/asset_performance_label.proto\x1a@google/ads/googleads_v3/proto/enums/policy_approval_status.proto\x1a>google/ads/googleads_v3/proto/enums/policy_review_status.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\x95\x04\n\x12\x41\x64GroupAdAssetView\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x31\n\x0b\x61\x64_group_ad\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05\x61sset\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12T\n\nfield_type\x18\x02 \x01(\x0e\x32@.google.ads.googleads.v3.enums.AssetFieldTypeEnum.AssetFieldType\x12V\n\x0epolicy_summary\x18\x03 \x01(\x0b\x32>.google.ads.googleads.v3.resources.AdGroupAdAssetPolicySummary\x12i\n\x11performance_label\x18\x04 \x01(\x0e\x32N.google.ads.googleads.v3.enums.AssetPerformanceLabelEnum.AssetPerformanceLabel:o\xea\x41l\n+googleads.googleapis.com/AdGroupAdAssetView\x12=customers/{customer}/adGroupAdAssets/{ad_group_ad_asset_view}\"\xb5\x02\n\x1b\x41\x64GroupAdAssetPolicySummary\x12N\n\x14policy_topic_entries\x18\x01 \x03(\x0b\x32\x30.google.ads.googleads.v3.common.PolicyTopicEntry\x12_\n\rreview_status\x18\x02 \x01(\x0e\x32H.google.ads.googleads.v3.enums.PolicyReviewStatusEnum.PolicyReviewStatus\x12\x65\n\x0f\x61pproval_status\x18\x03 \x01(\x0e\x32L.google.ads.googleads.v3.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusB\x84\x02\n%com.google.ads.googleads.v3.resourcesB\x17\x41\x64GroupAdAssetViewProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_policy__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_asset__field__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_asset__performance__label__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_policy__approval__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_policy__review__status__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPADASSETVIEW = _descriptor.Descriptor(
  name='AdGroupAdAssetView',
  full_name='google.ads.googleads.v3.resources.AdGroupAdAssetView',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetView.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group_ad', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetView.ad_group_ad', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetView.asset', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_type', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetView.field_type', index=3,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policy_summary', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetView.policy_summary', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='performance_label', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetView.performance_label', index=5,
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
  serialized_options=_b('\352Al\n+googleads.googleapis.com/AdGroupAdAssetView\022=customers/{customer}/adGroupAdAssets/{ad_group_ad_asset_view}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=1038,
)


_ADGROUPADASSETPOLICYSUMMARY = _descriptor.Descriptor(
  name='AdGroupAdAssetPolicySummary',
  full_name='google.ads.googleads.v3.resources.AdGroupAdAssetPolicySummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_topic_entries', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetPolicySummary.policy_topic_entries', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='review_status', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetPolicySummary.review_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='approval_status', full_name='google.ads.googleads.v3.resources.AdGroupAdAssetPolicySummary.approval_status', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1041,
  serialized_end=1350,
)

_ADGROUPADASSETVIEW.fields_by_name['ad_group_ad'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPADASSETVIEW.fields_by_name['asset'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPADASSETVIEW.fields_by_name['field_type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_asset__field__type__pb2._ASSETFIELDTYPEENUM_ASSETFIELDTYPE
_ADGROUPADASSETVIEW.fields_by_name['policy_summary'].message_type = _ADGROUPADASSETPOLICYSUMMARY
_ADGROUPADASSETVIEW.fields_by_name['performance_label'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_asset__performance__label__pb2._ASSETPERFORMANCELABELENUM_ASSETPERFORMANCELABEL
_ADGROUPADASSETPOLICYSUMMARY.fields_by_name['policy_topic_entries'].message_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_common_dot_policy__pb2._POLICYTOPICENTRY
_ADGROUPADASSETPOLICYSUMMARY.fields_by_name['review_status'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_policy__review__status__pb2._POLICYREVIEWSTATUSENUM_POLICYREVIEWSTATUS
_ADGROUPADASSETPOLICYSUMMARY.fields_by_name['approval_status'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_policy__approval__status__pb2._POLICYAPPROVALSTATUSENUM_POLICYAPPROVALSTATUS
DESCRIPTOR.message_types_by_name['AdGroupAdAssetView'] = _ADGROUPADASSETVIEW
DESCRIPTOR.message_types_by_name['AdGroupAdAssetPolicySummary'] = _ADGROUPADASSETPOLICYSUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupAdAssetView = _reflection.GeneratedProtocolMessageType('AdGroupAdAssetView', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPADASSETVIEW,
  __module__ = 'google.ads.googleads_v3.proto.resources.ad_group_ad_asset_view_pb2'
  ,
  __doc__ = """A link between an AdGroupAd and an Asset.
  
  
  Attributes:
      resource_name:
          The resource name of the ad group ad asset view. Ad group ad
          asset view resource names have the form:  ``customers/{custome
          r_id}/adGroupAdAssets/{AdGroupAdAsset.ad_group_id}~{AdGroupAdA
          sset.ad.ad_id}~{AdGroupAdAsset.asset_id}~{AdGroupAdAsset.asset
          _field_type}``
      ad_group_ad:
          The ad group ad to which the asset is linked.
      asset:
          The asset which is linked to the ad group ad.
      field_type:
          Role that the asset takes in the ad.
      policy_summary:
          Policy information for the ad group ad asset.
      performance_label:
          Performance of an asset linkage.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.AdGroupAdAssetView)
  ))
_sym_db.RegisterMessage(AdGroupAdAssetView)

AdGroupAdAssetPolicySummary = _reflection.GeneratedProtocolMessageType('AdGroupAdAssetPolicySummary', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPADASSETPOLICYSUMMARY,
  __module__ = 'google.ads.googleads_v3.proto.resources.ad_group_ad_asset_view_pb2'
  ,
  __doc__ = """Contains policy information for an ad group ad asset.
  
  
  Attributes:
      policy_topic_entries:
          The list of policy findings for the ad group ad asset.
      review_status:
          Where in the review process this ad group ad asset is.
      approval_status:
          The overall approval status of this ad group ad asset,
          calculated based on the status of its individual policy topic
          entries.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.AdGroupAdAssetPolicySummary)
  ))
_sym_db.RegisterMessage(AdGroupAdAssetPolicySummary)


DESCRIPTOR._options = None
_ADGROUPADASSETVIEW._options = None
# @@protoc_insertion_point(module_scope)
