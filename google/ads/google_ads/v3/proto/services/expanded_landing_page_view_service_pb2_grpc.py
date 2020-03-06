# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v3.proto.resources import expanded_landing_page_view_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_expanded__landing__page__view__pb2
from google.ads.google_ads.v3.proto.services import expanded_landing_page_view_service_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_expanded__landing__page__view__service__pb2


class ExpandedLandingPageViewServiceStub(object):
  """Proto file describing the expanded landing page view service.

  Service to fetch expanded landing page views.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetExpandedLandingPageView = channel.unary_unary(
        '/google.ads.googleads.v3.services.ExpandedLandingPageViewService/GetExpandedLandingPageView',
        request_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_expanded__landing__page__view__service__pb2.GetExpandedLandingPageViewRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_expanded__landing__page__view__pb2.ExpandedLandingPageView.FromString,
        )


class ExpandedLandingPageViewServiceServicer(object):
  """Proto file describing the expanded landing page view service.

  Service to fetch expanded landing page views.
  """

  def GetExpandedLandingPageView(self, request, context):
    """Returns the requested expanded landing page view in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExpandedLandingPageViewServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetExpandedLandingPageView': grpc.unary_unary_rpc_method_handler(
          servicer.GetExpandedLandingPageView,
          request_deserializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_services_dot_expanded__landing__page__view__service__pb2.GetExpandedLandingPageViewRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v3_dot_proto_dot_resources_dot_expanded__landing__page__view__pb2.ExpandedLandingPageView.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v3.services.ExpandedLandingPageViewService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
