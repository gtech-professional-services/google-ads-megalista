# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v2/proto/services/mutate_job_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v2.proto.resources import mutate_job_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_mutate__job__pb2
from google.ads.google_ads.v2.proto.services import google_ads_service_pb2 as google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_google__ads__service__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v2/proto/services/mutate_job_service.proto',
  package='google.ads.googleads.v2.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v2.servicesB\025MutateJobServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V2.Services\312\002 Google\\Ads\\GoogleAds\\V2\\Services\352\002$Google::Ads::GoogleAds::V2::Services'),
  serialized_pb=_b('\n?google/ads/googleads_v2/proto/services/mutate_job_service.proto\x12 google.ads.googleads.v2.services\x1a\x38google/ads/googleads_v2/proto/resources/mutate_job.proto\x1a?google/ads/googleads_v2/proto/services/google_ads_service.proto\x1a\x1cgoogle/api/annotations.proto\x1a#google/longrunning/operations.proto\x1a\x17google/rpc/status.proto\x1a\x17google/api/client.proto\"-\n\x16\x43reateMutateJobRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\"0\n\x17\x43reateMutateJobResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\",\n\x13GetMutateJobRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\",\n\x13RunMutateJobRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x9c\x01\n\x1d\x41\x64\x64MutateJobOperationsRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x16\n\x0esequence_token\x18\x02 \x01(\t\x12L\n\x11mutate_operations\x18\x03 \x03(\x0b\x32\x31.google.ads.googleads.v2.services.MutateOperation\"W\n\x1e\x41\x64\x64MutateJobOperationsResponse\x12\x18\n\x10total_operations\x18\x01 \x01(\x03\x12\x1b\n\x13next_sequence_token\x18\x02 \x01(\t\"[\n\x1bListMutateJobResultsRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\"{\n\x1cListMutateJobResultsResponse\x12\x42\n\x07results\x18\x01 \x03(\x0b\x32\x31.google.ads.googleads.v2.services.MutateJobResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xac\x01\n\x0fMutateJobResult\x12\x17\n\x0foperation_index\x18\x01 \x01(\x03\x12\\\n\x19mutate_operation_response\x18\x02 \x01(\x0b\x32\x39.google.ads.googleads.v2.services.MutateOperationResponse\x12\"\n\x06status\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status2\x83\x08\n\x10MutateJobService\x12\xc2\x01\n\x0f\x43reateMutateJob\x12\x38.google.ads.googleads.v2.services.CreateMutateJobRequest\x1a\x39.google.ads.googleads.v2.services.CreateMutateJobResponse\":\x82\xd3\xe4\x93\x02\x34\"//v2/customers/{customer_id=*}/mutateJobs:create:\x01*\x12\xa9\x01\n\x0cGetMutateJob\x12\x35.google.ads.googleads.v2.services.GetMutateJobRequest\x1a,.google.ads.googleads.v2.resources.MutateJob\"4\x82\xd3\xe4\x93\x02.\x12,/v2/{resource_name=customers/*/mutateJobs/*}\x12\xd7\x01\n\x14ListMutateJobResults\x12=.google.ads.googleads.v2.services.ListMutateJobResultsRequest\x1a>.google.ads.googleads.v2.services.ListMutateJobResultsResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/v2/{resource_name=customers/*/mutateJobs/*}:listResults\x12\xa1\x01\n\x0cRunMutateJob\x12\x35.google.ads.googleads.v2.services.RunMutateJobRequest\x1a\x1d.google.longrunning.Operation\";\x82\xd3\xe4\x93\x02\x35\"0/v2/{resource_name=customers/*/mutateJobs/*}:run:\x01*\x12\xe2\x01\n\x16\x41\x64\x64MutateJobOperations\x12?.google.ads.googleads.v2.services.AddMutateJobOperationsRequest\x1a@.google.ads.googleads.v2.services.AddMutateJobOperationsResponse\"E\x82\xd3\xe4\x93\x02?\":/v2/{resource_name=customers/*/mutateJobs/*}:addOperations:\x01*\x1a\x1b\xca\x41\x18googleads.googleapis.comB\xfc\x01\n$com.google.ads.googleads.v2.servicesB\x15MutateJobServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v2/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V2.Services\xca\x02 Google\\Ads\\GoogleAds\\V2\\Services\xea\x02$Google::Ads::GoogleAds::V2::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_mutate__job__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_google__ads__service__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_CREATEMUTATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateMutateJobRequest',
  full_name='google.ads.googleads.v2.services.CreateMutateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v2.services.CreateMutateJobRequest.customer_id', index=0,
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
  serialized_start=341,
  serialized_end=386,
)


_CREATEMUTATEJOBRESPONSE = _descriptor.Descriptor(
  name='CreateMutateJobResponse',
  full_name='google.ads.googleads.v2.services.CreateMutateJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.CreateMutateJobResponse.resource_name', index=0,
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
  serialized_start=388,
  serialized_end=436,
)


_GETMUTATEJOBREQUEST = _descriptor.Descriptor(
  name='GetMutateJobRequest',
  full_name='google.ads.googleads.v2.services.GetMutateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.GetMutateJobRequest.resource_name', index=0,
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
  serialized_start=438,
  serialized_end=482,
)


_RUNMUTATEJOBREQUEST = _descriptor.Descriptor(
  name='RunMutateJobRequest',
  full_name='google.ads.googleads.v2.services.RunMutateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.RunMutateJobRequest.resource_name', index=0,
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
  serialized_start=484,
  serialized_end=528,
)


_ADDMUTATEJOBOPERATIONSREQUEST = _descriptor.Descriptor(
  name='AddMutateJobOperationsRequest',
  full_name='google.ads.googleads.v2.services.AddMutateJobOperationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.AddMutateJobOperationsRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence_token', full_name='google.ads.googleads.v2.services.AddMutateJobOperationsRequest.sequence_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutate_operations', full_name='google.ads.googleads.v2.services.AddMutateJobOperationsRequest.mutate_operations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=531,
  serialized_end=687,
)


_ADDMUTATEJOBOPERATIONSRESPONSE = _descriptor.Descriptor(
  name='AddMutateJobOperationsResponse',
  full_name='google.ads.googleads.v2.services.AddMutateJobOperationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_operations', full_name='google.ads.googleads.v2.services.AddMutateJobOperationsResponse.total_operations', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_sequence_token', full_name='google.ads.googleads.v2.services.AddMutateJobOperationsResponse.next_sequence_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=689,
  serialized_end=776,
)


_LISTMUTATEJOBRESULTSREQUEST = _descriptor.Descriptor(
  name='ListMutateJobResultsRequest',
  full_name='google.ads.googleads.v2.services.ListMutateJobResultsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v2.services.ListMutateJobResultsRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.ads.googleads.v2.services.ListMutateJobResultsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.ads.googleads.v2.services.ListMutateJobResultsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=778,
  serialized_end=869,
)


_LISTMUTATEJOBRESULTSRESPONSE = _descriptor.Descriptor(
  name='ListMutateJobResultsResponse',
  full_name='google.ads.googleads.v2.services.ListMutateJobResultsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v2.services.ListMutateJobResultsResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.ads.googleads.v2.services.ListMutateJobResultsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=871,
  serialized_end=994,
)


_MUTATEJOBRESULT = _descriptor.Descriptor(
  name='MutateJobResult',
  full_name='google.ads.googleads.v2.services.MutateJobResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation_index', full_name='google.ads.googleads.v2.services.MutateJobResult.operation_index', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mutate_operation_response', full_name='google.ads.googleads.v2.services.MutateJobResult.mutate_operation_response', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v2.services.MutateJobResult.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=997,
  serialized_end=1169,
)

_ADDMUTATEJOBOPERATIONSREQUEST.fields_by_name['mutate_operations'].message_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_google__ads__service__pb2._MUTATEOPERATION
_LISTMUTATEJOBRESULTSRESPONSE.fields_by_name['results'].message_type = _MUTATEJOBRESULT
_MUTATEJOBRESULT.fields_by_name['mutate_operation_response'].message_type = google_dot_ads_dot_googleads__v2_dot_proto_dot_services_dot_google__ads__service__pb2._MUTATEOPERATIONRESPONSE
_MUTATEJOBRESULT.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['CreateMutateJobRequest'] = _CREATEMUTATEJOBREQUEST
DESCRIPTOR.message_types_by_name['CreateMutateJobResponse'] = _CREATEMUTATEJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetMutateJobRequest'] = _GETMUTATEJOBREQUEST
DESCRIPTOR.message_types_by_name['RunMutateJobRequest'] = _RUNMUTATEJOBREQUEST
DESCRIPTOR.message_types_by_name['AddMutateJobOperationsRequest'] = _ADDMUTATEJOBOPERATIONSREQUEST
DESCRIPTOR.message_types_by_name['AddMutateJobOperationsResponse'] = _ADDMUTATEJOBOPERATIONSRESPONSE
DESCRIPTOR.message_types_by_name['ListMutateJobResultsRequest'] = _LISTMUTATEJOBRESULTSREQUEST
DESCRIPTOR.message_types_by_name['ListMutateJobResultsResponse'] = _LISTMUTATEJOBRESULTSRESPONSE
DESCRIPTOR.message_types_by_name['MutateJobResult'] = _MUTATEJOBRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateMutateJobRequest = _reflection.GeneratedProtocolMessageType('CreateMutateJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEMUTATEJOBREQUEST,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Request message for [MutateJobService.CreateMutateJobRequest][]
  
  
  Attributes:
      customer_id:
          The ID of the customer for which to create a mutate job.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.CreateMutateJobRequest)
  ))
_sym_db.RegisterMessage(CreateMutateJobRequest)

CreateMutateJobResponse = _reflection.GeneratedProtocolMessageType('CreateMutateJobResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEMUTATEJOBRESPONSE,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Response message for [MutateJobService.CreateMutateJobResponse][]
  
  
  Attributes:
      resource_name:
          The resource name of the MutateJob.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.CreateMutateJobResponse)
  ))
_sym_db.RegisterMessage(CreateMutateJobResponse)

GetMutateJobRequest = _reflection.GeneratedProtocolMessageType('GetMutateJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMUTATEJOBREQUEST,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Request message for
  [MutateJobService.GetMutateJob][google.ads.googleads.v2.services.MutateJobService.GetMutateJob]
  
  
  Attributes:
      resource_name:
          The resource name of the MutateJob to get.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.GetMutateJobRequest)
  ))
_sym_db.RegisterMessage(GetMutateJobRequest)

RunMutateJobRequest = _reflection.GeneratedProtocolMessageType('RunMutateJobRequest', (_message.Message,), dict(
  DESCRIPTOR = _RUNMUTATEJOBREQUEST,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Request message for
  [MutateJobService.RunMutateJob][google.ads.googleads.v2.services.MutateJobService.RunMutateJob]
  
  
  Attributes:
      resource_name:
          The resource name of the MutateJob to run.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.RunMutateJobRequest)
  ))
_sym_db.RegisterMessage(RunMutateJobRequest)

AddMutateJobOperationsRequest = _reflection.GeneratedProtocolMessageType('AddMutateJobOperationsRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDMUTATEJOBOPERATIONSREQUEST,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Request message for
  [MutateJobService.AddMutateJobOperations][google.ads.googleads.v2.services.MutateJobService.AddMutateJobOperations]
  
  
  Attributes:
      resource_name:
          The resource name of the MutateJob.
      sequence_token:
          A token used to enforce sequencing.  The first
          AddMutateJobOperations request for a MutateJob should not set
          sequence\_token. Subsequent requests must set sequence\_token
          to the value of next\_sequence\_token received in the previous
          AddMutateJobOperations response.
      mutate_operations:
          The list of mutates being added.  Operations can use negative
          integers as temp ids to signify dependencies between entities
          created in this MutateJob. For example, a customer with id =
          1234 can create a campaign and an ad group in that same
          campaign by creating a campaign in the first operation with
          the resource name explicitly set to
          "customers/1234/campaigns/-1", and creating an ad group in the
          second operation with the campaign field also set to
          "customers/1234/campaigns/-1".
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.AddMutateJobOperationsRequest)
  ))
_sym_db.RegisterMessage(AddMutateJobOperationsRequest)

AddMutateJobOperationsResponse = _reflection.GeneratedProtocolMessageType('AddMutateJobOperationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDMUTATEJOBOPERATIONSRESPONSE,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Response message for
  [MutateJobService.AddMutateJobOperations][google.ads.googleads.v2.services.MutateJobService.AddMutateJobOperations]
  
  
  Attributes:
      total_operations:
          The total number of operations added so far for this job.
      next_sequence_token:
          The sequence token to be used when calling
          AddMutateJobOperations again if more operations need to be
          added. The next AddMutateJobOperations request must set the
          sequence\_token field to the value of this field.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.AddMutateJobOperationsResponse)
  ))
_sym_db.RegisterMessage(AddMutateJobOperationsResponse)

ListMutateJobResultsRequest = _reflection.GeneratedProtocolMessageType('ListMutateJobResultsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTMUTATEJOBRESULTSREQUEST,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Request message for
  [MutateJobService.ListMutateJobResults][google.ads.googleads.v2.services.MutateJobService.ListMutateJobResults].
  
  
  Attributes:
      resource_name:
          The resource name of the MutateJob whose results are being
          listed.
      page_token:
          Token of the page to retrieve. If not specified, the first
          page of results will be returned. Use the value obtained from
          ``next_page_token`` in the previous response in order to
          request the next page of results.
      page_size:
          Number of elements to retrieve in a single page. When a page
          request is too large, the server may decide to further limit
          the number of returned resources.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ListMutateJobResultsRequest)
  ))
_sym_db.RegisterMessage(ListMutateJobResultsRequest)

ListMutateJobResultsResponse = _reflection.GeneratedProtocolMessageType('ListMutateJobResultsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTMUTATEJOBRESULTSRESPONSE,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """Response message for
  [MutateJobService.ListMutateJobResults][google.ads.googleads.v2.services.MutateJobService.ListMutateJobResults].
  
  
  Attributes:
      results:
          The list of rows that matched the query.
      next_page_token:
          Pagination token used to retrieve the next page of results.
          Pass the content of this string as the ``page_token``
          attribute of the next request. ``next_page_token`` is not
          returned for the last page.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.ListMutateJobResultsResponse)
  ))
_sym_db.RegisterMessage(ListMutateJobResultsResponse)

MutateJobResult = _reflection.GeneratedProtocolMessageType('MutateJobResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEJOBRESULT,
  __module__ = 'google.ads.googleads_v2.proto.services.mutate_job_service_pb2'
  ,
  __doc__ = """MutateJob result.
  
  
  Attributes:
      operation_index:
          Index of the mutate operation.
      mutate_operation_response:
          Response for the mutate. May be empty if errors occurred.
      status:
          Details of the errors when processing the operation.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v2.services.MutateJobResult)
  ))
_sym_db.RegisterMessage(MutateJobResult)


DESCRIPTOR._options = None

_MUTATEJOBSERVICE = _descriptor.ServiceDescriptor(
  name='MutateJobService',
  full_name='google.ads.googleads.v2.services.MutateJobService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=1172,
  serialized_end=2199,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateMutateJob',
    full_name='google.ads.googleads.v2.services.MutateJobService.CreateMutateJob',
    index=0,
    containing_service=None,
    input_type=_CREATEMUTATEJOBREQUEST,
    output_type=_CREATEMUTATEJOBRESPONSE,
    serialized_options=_b('\202\323\344\223\0024\"//v2/customers/{customer_id=*}/mutateJobs:create:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='GetMutateJob',
    full_name='google.ads.googleads.v2.services.MutateJobService.GetMutateJob',
    index=1,
    containing_service=None,
    input_type=_GETMUTATEJOBREQUEST,
    output_type=google_dot_ads_dot_googleads__v2_dot_proto_dot_resources_dot_mutate__job__pb2._MUTATEJOB,
    serialized_options=_b('\202\323\344\223\002.\022,/v2/{resource_name=customers/*/mutateJobs/*}'),
  ),
  _descriptor.MethodDescriptor(
    name='ListMutateJobResults',
    full_name='google.ads.googleads.v2.services.MutateJobService.ListMutateJobResults',
    index=2,
    containing_service=None,
    input_type=_LISTMUTATEJOBRESULTSREQUEST,
    output_type=_LISTMUTATEJOBRESULTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002:\0228/v2/{resource_name=customers/*/mutateJobs/*}:listResults'),
  ),
  _descriptor.MethodDescriptor(
    name='RunMutateJob',
    full_name='google.ads.googleads.v2.services.MutateJobService.RunMutateJob',
    index=3,
    containing_service=None,
    input_type=_RUNMUTATEJOBREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=_b('\202\323\344\223\0025\"0/v2/{resource_name=customers/*/mutateJobs/*}:run:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='AddMutateJobOperations',
    full_name='google.ads.googleads.v2.services.MutateJobService.AddMutateJobOperations',
    index=4,
    containing_service=None,
    input_type=_ADDMUTATEJOBOPERATIONSREQUEST,
    output_type=_ADDMUTATEJOBOPERATIONSRESPONSE,
    serialized_options=_b('\202\323\344\223\002?\":/v2/{resource_name=customers/*/mutateJobs/*}:addOperations:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MUTATEJOBSERVICE)

DESCRIPTOR.services_by_name['MutateJobService'] = _MUTATEJOBSERVICE

# @@protoc_insertion_point(module_scope)
