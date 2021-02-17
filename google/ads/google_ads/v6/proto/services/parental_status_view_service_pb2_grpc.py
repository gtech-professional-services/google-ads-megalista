# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import parental_status_view_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_parental__status__view__pb2
from google.ads.google_ads.v6.proto.services import parental_status_view_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_parental__status__view__service__pb2


class ParentalStatusViewServiceStub(object):
    """Proto file describing the Parental Status View service.

    Service to manage parental status views.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetParentalStatusView = channel.unary_unary(
                '/google.ads.googleads.v6.services.ParentalStatusViewService/GetParentalStatusView',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_parental__status__view__service__pb2.GetParentalStatusViewRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_parental__status__view__pb2.ParentalStatusView.FromString,
                )


class ParentalStatusViewServiceServicer(object):
    """Proto file describing the Parental Status View service.

    Service to manage parental status views.
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
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_parental__status__view__service__pb2.GetParentalStatusViewRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_parental__status__view__pb2.ParentalStatusView.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.ParentalStatusViewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ParentalStatusViewService(object):
    """Proto file describing the Parental Status View service.

    Service to manage parental status views.
    """

    @staticmethod
    def GetParentalStatusView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.ParentalStatusViewService/GetParentalStatusView',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_parental__status__view__service__pb2.GetParentalStatusViewRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_parental__status__view__pb2.ParentalStatusView.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
