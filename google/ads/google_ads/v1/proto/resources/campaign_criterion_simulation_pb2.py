# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/campaign_criterion_simulation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.common import simulation_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_simulation__pb2
from google.ads.google_ads.v1.proto.enums import simulation_modification_method_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_simulation__modification__method__pb2
from google.ads.google_ads.v1.proto.enums import simulation_type_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_simulation__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/campaign_criterion_simulation.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB CampaignCriterionSimulationProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\nKgoogle/ads/googleads_v1/proto/resources/campaign_criterion_simulation.proto\x12!google.ads.googleads.v1.resources\x1a\x35google/ads/googleads_v1/proto/common/simulation.proto\x1aHgoogle/ads/googleads_v1/proto/enums/simulation_modification_method.proto\x1a\x39google/ads/googleads_v1/proto/enums/simulation_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xb7\x04\n\x1b\x43\x61mpaignCriterionSimulation\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x30\n\x0b\x63\x61mpaign_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x31\n\x0c\x63riterion_id\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12N\n\x04type\x18\x04 \x01(\x0e\x32@.google.ads.googleads.v1.enums.SimulationTypeEnum.SimulationType\x12y\n\x13modification_method\x18\x05 \x01(\x0e\x32\\.google.ads.googleads.v1.enums.SimulationModificationMethodEnum.SimulationModificationMethod\x12\x30\n\nstart_date\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x65nd_date\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x61\n\x17\x62id_modifier_point_list\x18\x08 \x01(\x0b\x32>.google.ads.googleads.v1.common.BidModifierSimulationPointListH\x00\x42\x0c\n\npoint_listB\x8d\x02\n%com.google.ads.googleads.v1.resourcesB CampaignCriterionSimulationProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_simulation__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_simulation__modification__method__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_simulation__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CAMPAIGNCRITERIONSIMULATION = _descriptor.Descriptor(
  name='CampaignCriterionSimulation',
  full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.campaign_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='criterion_id', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.criterion_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modification_method', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.modification_method', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_date', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.start_date', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_date', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.end_date', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bid_modifier_point_list', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.bid_modifier_point_list', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='point_list', full_name='google.ads.googleads.v1.resources.CampaignCriterionSimulation.point_list',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=365,
  serialized_end=932,
)

_CAMPAIGNCRITERIONSIMULATION.fields_by_name['campaign_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNCRITERIONSIMULATION.fields_by_name['criterion_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CAMPAIGNCRITERIONSIMULATION.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_simulation__type__pb2._SIMULATIONTYPEENUM_SIMULATIONTYPE
_CAMPAIGNCRITERIONSIMULATION.fields_by_name['modification_method'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_simulation__modification__method__pb2._SIMULATIONMODIFICATIONMETHODENUM_SIMULATIONMODIFICATIONMETHOD
_CAMPAIGNCRITERIONSIMULATION.fields_by_name['start_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNCRITERIONSIMULATION.fields_by_name['end_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CAMPAIGNCRITERIONSIMULATION.fields_by_name['bid_modifier_point_list'].message_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_common_dot_simulation__pb2._BIDMODIFIERSIMULATIONPOINTLIST
_CAMPAIGNCRITERIONSIMULATION.oneofs_by_name['point_list'].fields.append(
  _CAMPAIGNCRITERIONSIMULATION.fields_by_name['bid_modifier_point_list'])
_CAMPAIGNCRITERIONSIMULATION.fields_by_name['bid_modifier_point_list'].containing_oneof = _CAMPAIGNCRITERIONSIMULATION.oneofs_by_name['point_list']
DESCRIPTOR.message_types_by_name['CampaignCriterionSimulation'] = _CAMPAIGNCRITERIONSIMULATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignCriterionSimulation = _reflection.GeneratedProtocolMessageType('CampaignCriterionSimulation', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNCRITERIONSIMULATION,
  __module__ = 'google.ads.googleads_v1.proto.resources.campaign_criterion_simulation_pb2'
  ,
  __doc__ = """A campaign criterion simulation. Supported combinations of advertising
  channel type, criterion ids, simulation type and simulation modification
  method is detailed below respectively.
  
  SEARCH 30000,30001,30002 BID\_MODIFIER UNIFORM DISPLAY 30001
  BID\_MODIFIER UNIFORM
  
  
  Attributes:
      resource_name:
          The resource name of the campaign criterion simulation.
          Campaign criterion simulation resource names have the form:  `
          `customers/{customer_id}/campaignCriterionSimulations/{campaig
          n_id}~{criterion_id}~{type}~{modification_method}~{start_date}
          ~{end_date}``
      campaign_id:
          Campaign ID of the simulation.
      criterion_id:
          Criterion ID of the simulation.
      type:
          The field that the simulation modifies.
      modification_method:
          How the simulation modifies the field.
      start_date:
          First day on which the simulation is based, in YYYY-MM-DD
          format.
      end_date:
          Last day on which the simulation is based, in YYYY-MM-DD
          format.
      point_list:
          List of simulation points.
      bid_modifier_point_list:
          Simulation points if the simulation type is BID\_MODIFIER.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.CampaignCriterionSimulation)
  ))
_sym_db.RegisterMessage(CampaignCriterionSimulation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
