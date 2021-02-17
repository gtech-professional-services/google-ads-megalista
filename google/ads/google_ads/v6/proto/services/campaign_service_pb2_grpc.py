# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import campaign_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__pb2
from google.ads.google_ads.v6.proto.services import campaign_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2


class CampaignServiceStub(object):
    """Proto file describing the Campaign service.

    Service to manage campaigns.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCampaign = channel.unary_unary(
                '/google.ads.googleads.v6.services.CampaignService/GetCampaign',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.GetCampaignRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__pb2.Campaign.FromString,
                )
        self.MutateCampaigns = channel.unary_unary(
                '/google.ads.googleads.v6.services.CampaignService/MutateCampaigns',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.MutateCampaignsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.MutateCampaignsResponse.FromString,
                )


class CampaignServiceServicer(object):
    """Proto file describing the Campaign service.

    Service to manage campaigns.
    """

    def GetCampaign(self, request, context):
        """Returns the requested campaign in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateCampaigns(self, request, context):
        """Creates, updates, or removes campaigns. Operation statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CampaignServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCampaign': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCampaign,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.GetCampaignRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__pb2.Campaign.SerializeToString,
            ),
            'MutateCampaigns': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateCampaigns,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.MutateCampaignsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.MutateCampaignsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.CampaignService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CampaignService(object):
    """Proto file describing the Campaign service.

    Service to manage campaigns.
    """

    @staticmethod
    def GetCampaign(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CampaignService/GetCampaign',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.GetCampaignRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_campaign__pb2.Campaign.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateCampaigns(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CampaignService/MutateCampaigns',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.MutateCampaignsRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_campaign__service__pb2.MutateCampaignsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
