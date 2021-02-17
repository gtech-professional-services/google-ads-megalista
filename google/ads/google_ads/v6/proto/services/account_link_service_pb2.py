# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/services/account_link_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.resources import account_link_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_account__link__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/services/account_link_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\027AccountLinkServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n;google/ads/googleads/v6/services/account_link_service.proto\x12 google.ads.googleads.v6.services\x1a\x34google/ads/googleads/v6/resources/account_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"\\\n\x15GetAccountLinkRequest\x12\x43\n\rresource_name\x18\x01 \x01(\tB,\xe0\x41\x02\xfa\x41&\n$googleads.googleapis.com/AccountLink\"\x7f\n\x18\x43reateAccountLinkRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12I\n\x0c\x61\x63\x63ount_link\x18\x02 \x01(\x0b\x32..google.ads.googleads.v6.resources.AccountLinkB\x03\xe0\x41\x02\"2\n\x19\x43reateAccountLinkResponse\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xb4\x01\n\x18MutateAccountLinkRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12N\n\toperation\x18\x02 \x01(\x0b\x32\x36.google.ads.googleads.v6.services.AccountLinkOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xa8\x01\n\x14\x41\x63\x63ountLinkOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12@\n\x06update\x18\x02 \x01(\x0b\x32..google.ads.googleads.v6.resources.AccountLinkH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"f\n\x19MutateAccountLinkResponse\x12I\n\x06result\x18\x01 \x01(\x0b\x32\x39.google.ads.googleads.v6.services.MutateAccountLinkResult\"0\n\x17MutateAccountLinkResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xec\x05\n\x12\x41\x63\x63ountLinkService\x12\xc1\x01\n\x0eGetAccountLink\x12\x37.google.ads.googleads.v6.services.GetAccountLinkRequest\x1a..google.ads.googleads.v6.resources.AccountLink\"F\x82\xd3\xe4\x93\x02\x30\x12./v6/{resource_name=customers/*/accountLinks/*}\xda\x41\rresource_name\x12\xe5\x01\n\x11\x43reateAccountLink\x12:.google.ads.googleads.v6.services.CreateAccountLinkRequest\x1a;.google.ads.googleads.v6.services.CreateAccountLinkResponse\"W\x82\xd3\xe4\x93\x02\x36\"1/v6/customers/{customer_id=*}/accountLinks:create:\x01*\xda\x41\x18\x63ustomer_id,account_link\x12\xe2\x01\n\x11MutateAccountLink\x12:.google.ads.googleads.v6.services.MutateAccountLinkRequest\x1a;.google.ads.googleads.v6.services.MutateAccountLinkResponse\"T\x82\xd3\xe4\x93\x02\x36\"1/v6/customers/{customer_id=*}/accountLinks:mutate:\x01*\xda\x41\x15\x63ustomer_id,operation\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\xfe\x01\n$com.google.ads.googleads.v6.servicesB\x17\x41\x63\x63ountLinkServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_account__link__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETACCOUNTLINKREQUEST = _descriptor.Descriptor(
  name='GetAccountLinkRequest',
  full_name='google.ads.googleads.v6.services.GetAccountLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.GetAccountLinkRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002\372A&\n$googleads.googleapis.com/AccountLink', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=300,
  serialized_end=392,
)


_CREATEACCOUNTLINKREQUEST = _descriptor.Descriptor(
  name='CreateAccountLinkRequest',
  full_name='google.ads.googleads.v6.services.CreateAccountLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.CreateAccountLinkRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account_link', full_name='google.ads.googleads.v6.services.CreateAccountLinkRequest.account_link', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=394,
  serialized_end=521,
)


_CREATEACCOUNTLINKRESPONSE = _descriptor.Descriptor(
  name='CreateAccountLinkResponse',
  full_name='google.ads.googleads.v6.services.CreateAccountLinkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.CreateAccountLinkResponse.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=523,
  serialized_end=573,
)


_MUTATEACCOUNTLINKREQUEST = _descriptor.Descriptor(
  name='MutateAccountLinkRequest',
  full_name='google.ads.googleads.v6.services.MutateAccountLinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.MutateAccountLinkRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='google.ads.googleads.v6.services.MutateAccountLinkRequest.operation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\002', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v6.services.MutateAccountLinkRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v6.services.MutateAccountLinkRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=576,
  serialized_end=756,
)


_ACCOUNTLINKOPERATION = _descriptor.Descriptor(
  name='AccountLinkOperation',
  full_name='google.ads.googleads.v6.services.AccountLinkOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v6.services.AccountLinkOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v6.services.AccountLinkOperation.update', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v6.services.AccountLinkOperation.remove', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='operation', full_name='google.ads.googleads.v6.services.AccountLinkOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=759,
  serialized_end=927,
)


_MUTATEACCOUNTLINKRESPONSE = _descriptor.Descriptor(
  name='MutateAccountLinkResponse',
  full_name='google.ads.googleads.v6.services.MutateAccountLinkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='google.ads.googleads.v6.services.MutateAccountLinkResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=929,
  serialized_end=1031,
)


_MUTATEACCOUNTLINKRESULT = _descriptor.Descriptor(
  name='MutateAccountLinkResult',
  full_name='google.ads.googleads.v6.services.MutateAccountLinkResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v6.services.MutateAccountLinkResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1033,
  serialized_end=1081,
)

_CREATEACCOUNTLINKREQUEST.fields_by_name['account_link'].message_type = google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_account__link__pb2._ACCOUNTLINK
_MUTATEACCOUNTLINKREQUEST.fields_by_name['operation'].message_type = _ACCOUNTLINKOPERATION
_ACCOUNTLINKOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_ACCOUNTLINKOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_account__link__pb2._ACCOUNTLINK
_ACCOUNTLINKOPERATION.oneofs_by_name['operation'].fields.append(
  _ACCOUNTLINKOPERATION.fields_by_name['update'])
_ACCOUNTLINKOPERATION.fields_by_name['update'].containing_oneof = _ACCOUNTLINKOPERATION.oneofs_by_name['operation']
_ACCOUNTLINKOPERATION.oneofs_by_name['operation'].fields.append(
  _ACCOUNTLINKOPERATION.fields_by_name['remove'])
_ACCOUNTLINKOPERATION.fields_by_name['remove'].containing_oneof = _ACCOUNTLINKOPERATION.oneofs_by_name['operation']
_MUTATEACCOUNTLINKRESPONSE.fields_by_name['result'].message_type = _MUTATEACCOUNTLINKRESULT
DESCRIPTOR.message_types_by_name['GetAccountLinkRequest'] = _GETACCOUNTLINKREQUEST
DESCRIPTOR.message_types_by_name['CreateAccountLinkRequest'] = _CREATEACCOUNTLINKREQUEST
DESCRIPTOR.message_types_by_name['CreateAccountLinkResponse'] = _CREATEACCOUNTLINKRESPONSE
DESCRIPTOR.message_types_by_name['MutateAccountLinkRequest'] = _MUTATEACCOUNTLINKREQUEST
DESCRIPTOR.message_types_by_name['AccountLinkOperation'] = _ACCOUNTLINKOPERATION
DESCRIPTOR.message_types_by_name['MutateAccountLinkResponse'] = _MUTATEACCOUNTLINKRESPONSE
DESCRIPTOR.message_types_by_name['MutateAccountLinkResult'] = _MUTATEACCOUNTLINKRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAccountLinkRequest = _reflection.GeneratedProtocolMessageType('GetAccountLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTLINKREQUEST,
  '__module__' : 'google.ads.googleads.v6.services.account_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.GetAccountLinkRequest)
  })
_sym_db.RegisterMessage(GetAccountLinkRequest)

CreateAccountLinkRequest = _reflection.GeneratedProtocolMessageType('CreateAccountLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTLINKREQUEST,
  '__module__' : 'google.ads.googleads.v6.services.account_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CreateAccountLinkRequest)
  })
_sym_db.RegisterMessage(CreateAccountLinkRequest)

CreateAccountLinkResponse = _reflection.GeneratedProtocolMessageType('CreateAccountLinkResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEACCOUNTLINKRESPONSE,
  '__module__' : 'google.ads.googleads.v6.services.account_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.CreateAccountLinkResponse)
  })
_sym_db.RegisterMessage(CreateAccountLinkResponse)

MutateAccountLinkRequest = _reflection.GeneratedProtocolMessageType('MutateAccountLinkRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEACCOUNTLINKREQUEST,
  '__module__' : 'google.ads.googleads.v6.services.account_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateAccountLinkRequest)
  })
_sym_db.RegisterMessage(MutateAccountLinkRequest)

AccountLinkOperation = _reflection.GeneratedProtocolMessageType('AccountLinkOperation', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTLINKOPERATION,
  '__module__' : 'google.ads.googleads.v6.services.account_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.AccountLinkOperation)
  })
_sym_db.RegisterMessage(AccountLinkOperation)

MutateAccountLinkResponse = _reflection.GeneratedProtocolMessageType('MutateAccountLinkResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEACCOUNTLINKRESPONSE,
  '__module__' : 'google.ads.googleads.v6.services.account_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateAccountLinkResponse)
  })
_sym_db.RegisterMessage(MutateAccountLinkResponse)

MutateAccountLinkResult = _reflection.GeneratedProtocolMessageType('MutateAccountLinkResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATEACCOUNTLINKRESULT,
  '__module__' : 'google.ads.googleads.v6.services.account_link_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.MutateAccountLinkResult)
  })
_sym_db.RegisterMessage(MutateAccountLinkResult)


DESCRIPTOR._options = None
_GETACCOUNTLINKREQUEST.fields_by_name['resource_name']._options = None
_CREATEACCOUNTLINKREQUEST.fields_by_name['customer_id']._options = None
_CREATEACCOUNTLINKREQUEST.fields_by_name['account_link']._options = None
_MUTATEACCOUNTLINKREQUEST.fields_by_name['customer_id']._options = None
_MUTATEACCOUNTLINKREQUEST.fields_by_name['operation']._options = None

_ACCOUNTLINKSERVICE = _descriptor.ServiceDescriptor(
  name='AccountLinkService',
  full_name='google.ads.googleads.v6.services.AccountLinkService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=1084,
  serialized_end=1832,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAccountLink',
    full_name='google.ads.googleads.v6.services.AccountLinkService.GetAccountLink',
    index=0,
    containing_service=None,
    input_type=_GETACCOUNTLINKREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_account__link__pb2._ACCOUNTLINK,
    serialized_options=b'\202\323\344\223\0020\022./v6/{resource_name=customers/*/accountLinks/*}\332A\rresource_name',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateAccountLink',
    full_name='google.ads.googleads.v6.services.AccountLinkService.CreateAccountLink',
    index=1,
    containing_service=None,
    input_type=_CREATEACCOUNTLINKREQUEST,
    output_type=_CREATEACCOUNTLINKRESPONSE,
    serialized_options=b'\202\323\344\223\0026\"1/v6/customers/{customer_id=*}/accountLinks:create:\001*\332A\030customer_id,account_link',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateAccountLink',
    full_name='google.ads.googleads.v6.services.AccountLinkService.MutateAccountLink',
    index=2,
    containing_service=None,
    input_type=_MUTATEACCOUNTLINKREQUEST,
    output_type=_MUTATEACCOUNTLINKRESPONSE,
    serialized_options=b'\202\323\344\223\0026\"1/v6/customers/{customer_id=*}/accountLinks:mutate:\001*\332A\025customer_id,operation',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTLINKSERVICE)

DESCRIPTOR.services_by_name['AccountLinkService'] = _ACCOUNTLINKSERVICE

# @@protoc_insertion_point(module_scope)
