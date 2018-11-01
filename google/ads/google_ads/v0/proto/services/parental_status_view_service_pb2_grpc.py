# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v0.proto.resources import parental_status_view_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_parental__status__view__pb2
from google.ads.google_ads.v0.proto.services import parental_status_view_service_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_parental__status__view__service__pb2


class ParentalStatusViewServiceStub(object):
  """Service to manage parental status views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetParentalStatusView = channel.unary_unary(
        '/google.ads.googleads.v0.services.ParentalStatusViewService/GetParentalStatusView',
        request_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_parental__status__view__service__pb2.GetParentalStatusViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_parental__status__view__pb2.ParentalStatusView.FromString,
        )


class ParentalStatusViewServiceServicer(object):
  """Service to manage parental status views.
  """

  def GetParentalStatusView(self, request, context):
    """Returns the requested parental status view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ParentalStatusViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetParentalStatusView': grpc.unary_unary_rpc_method_handler(
          servicer.GetParentalStatusView,
          request_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_parental__status__view__service__pb2.GetParentalStatusViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_parental__status__view__pb2.ParentalStatusView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v0.services.ParentalStatusViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
