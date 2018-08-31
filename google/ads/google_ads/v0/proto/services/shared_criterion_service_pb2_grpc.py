# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v0.proto.resources import shared_criterion_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2
from google.ads.google_ads.v0.proto.services import shared_criterion_service_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_shared__criterion__service__pb2


class SharedCriterionServiceStub(object):
  """Service to manage shared criteria.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSharedCriterion = channel.unary_unary(
        '/google.ads.googleads.v0.services.SharedCriterionService/GetSharedCriterion',
        request_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_shared__criterion__service__pb2.GetSharedCriterionRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2.SharedCriterion.FromString,
        )
    self.MutateSharedCriteria = channel.unary_unary(
        '/google.ads.googleads.v0.services.SharedCriterionService/MutateSharedCriteria',
        request_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_shared__criterion__service__pb2.MutateSharedCriteriaRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_shared__criterion__service__pb2.MutateSharedCriteriaResponse.FromString,
        )


class SharedCriterionServiceServicer(object):
  """Service to manage shared criteria.
  """

  def GetSharedCriterion(self, request, context):
    """Returns the requested shared criterion in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateSharedCriteria(self, request, context):
    """Creates or removes shared criteria. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SharedCriterionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSharedCriterion': grpc.unary_unary_rpc_method_handler(
          servicer.GetSharedCriterion,
          request_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_shared__criterion__service__pb2.GetSharedCriterionRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__criterion__pb2.SharedCriterion.SerializeToString,
      ),
      'MutateSharedCriteria': grpc.unary_unary_rpc_method_handler(
          servicer.MutateSharedCriteria,
          request_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_shared__criterion__service__pb2.MutateSharedCriteriaRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_shared__criterion__service__pb2.MutateSharedCriteriaResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v0.services.SharedCriterionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
