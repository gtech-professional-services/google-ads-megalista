# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v1.proto.resources import campaign_bid_modifier_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__bid__modifier__pb2
from google.ads.google_ads.v1.proto.services import campaign_bid_modifier_service_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__bid__modifier__service__pb2


class CampaignBidModifierServiceStub(object):
  """Service to manage campaign bid modifiers.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCampaignBidModifier = channel.unary_unary(
        '/google.ads.googleads.v1.services.CampaignBidModifierService/GetCampaignBidModifier',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__bid__modifier__service__pb2.GetCampaignBidModifierRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__bid__modifier__pb2.CampaignBidModifier.FromString,
        )
    self.MutateCampaignBidModifiers = channel.unary_unary(
        '/google.ads.googleads.v1.services.CampaignBidModifierService/MutateCampaignBidModifiers',
        request_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__bid__modifier__service__pb2.MutateCampaignBidModifiersRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__bid__modifier__service__pb2.MutateCampaignBidModifiersResponse.FromString,
        )


class CampaignBidModifierServiceServicer(object):
  """Service to manage campaign bid modifiers.
  """

  def GetCampaignBidModifier(self, request, context):
    """Returns the requested campaign bid modifier in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCampaignBidModifiers(self, request, context):
    """Creates, updates, or removes campaign bid modifiers.
    Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CampaignBidModifierServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCampaignBidModifier': grpc.unary_unary_rpc_method_handler(
          servicer.GetCampaignBidModifier,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__bid__modifier__service__pb2.GetCampaignBidModifierRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_campaign__bid__modifier__pb2.CampaignBidModifier.SerializeToString,
      ),
      'MutateCampaignBidModifiers': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCampaignBidModifiers,
          request_deserializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__bid__modifier__service__pb2.MutateCampaignBidModifiersRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v1_dot_proto_dot_services_dot_campaign__bid__modifier__service__pb2.MutateCampaignBidModifiersResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v1.services.CampaignBidModifierService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
