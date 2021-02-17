# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v6/services/payments_account_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v6.proto.resources import payments_account_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_payments__account__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v6/services/payments_account_service.proto',
  package='google.ads.googleads.v6.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v6.servicesB\033PaymentsAccountServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V6.Services\312\002 Google\\Ads\\GoogleAds\\V6\\Services\352\002$Google::Ads::GoogleAds::V6::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?google/ads/googleads/v6/services/payments_account_service.proto\x12 google.ads.googleads.v6.services\x1a\x38google/ads/googleads/v6/resources/payments_account.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\"7\n\x1bListPaymentsAccountsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\"m\n\x1cListPaymentsAccountsResponse\x12M\n\x11payments_accounts\x18\x01 \x03(\x0b\x32\x32.google.ads.googleads.v6.resources.PaymentsAccount2\xbd\x02\n\x16PaymentsAccountService\x12\xdb\x01\n\x14ListPaymentsAccounts\x12=.google.ads.googleads.v6.services.ListPaymentsAccountsRequest\x1a>.google.ads.googleads.v6.services.ListPaymentsAccountsResponse\"D\x82\xd3\xe4\x93\x02\x30\x12./v6/customers/{customer_id=*}/paymentsAccounts\xda\x41\x0b\x63ustomer_id\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x82\x02\n$com.google.ads.googleads.v6.servicesB\x1bPaymentsAccountServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v6/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V6.Services\xca\x02 Google\\Ads\\GoogleAds\\V6\\Services\xea\x02$Google::Ads::GoogleAds::V6::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_payments__account__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,])




_LISTPAYMENTSACCOUNTSREQUEST = _descriptor.Descriptor(
  name='ListPaymentsAccountsRequest',
  full_name='google.ads.googleads.v6.services.ListPaymentsAccountsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v6.services.ListPaymentsAccountsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=247,
  serialized_end=302,
)


_LISTPAYMENTSACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='ListPaymentsAccountsResponse',
  full_name='google.ads.googleads.v6.services.ListPaymentsAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payments_accounts', full_name='google.ads.googleads.v6.services.ListPaymentsAccountsResponse.payments_accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=304,
  serialized_end=413,
)

_LISTPAYMENTSACCOUNTSRESPONSE.fields_by_name['payments_accounts'].message_type = google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_payments__account__pb2._PAYMENTSACCOUNT
DESCRIPTOR.message_types_by_name['ListPaymentsAccountsRequest'] = _LISTPAYMENTSACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['ListPaymentsAccountsResponse'] = _LISTPAYMENTSACCOUNTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListPaymentsAccountsRequest = _reflection.GeneratedProtocolMessageType('ListPaymentsAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPAYMENTSACCOUNTSREQUEST,
  '__module__' : 'google.ads.googleads.v6.services.payments_account_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.ListPaymentsAccountsRequest)
  })
_sym_db.RegisterMessage(ListPaymentsAccountsRequest)

ListPaymentsAccountsResponse = _reflection.GeneratedProtocolMessageType('ListPaymentsAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPAYMENTSACCOUNTSRESPONSE,
  '__module__' : 'google.ads.googleads.v6.services.payments_account_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.services.ListPaymentsAccountsResponse)
  })
_sym_db.RegisterMessage(ListPaymentsAccountsResponse)


DESCRIPTOR._options = None
_LISTPAYMENTSACCOUNTSREQUEST.fields_by_name['customer_id']._options = None

_PAYMENTSACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='PaymentsAccountService',
  full_name='google.ads.googleads.v6.services.PaymentsAccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=416,
  serialized_end=733,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListPaymentsAccounts',
    full_name='google.ads.googleads.v6.services.PaymentsAccountService.ListPaymentsAccounts',
    index=0,
    containing_service=None,
    input_type=_LISTPAYMENTSACCOUNTSREQUEST,
    output_type=_LISTPAYMENTSACCOUNTSRESPONSE,
    serialized_options=b'\202\323\344\223\0020\022./v6/customers/{customer_id=*}/paymentsAccounts\332A\013customer_id',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYMENTSACCOUNTSERVICE)

DESCRIPTOR.services_by_name['PaymentsAccountService'] = _PAYMENTSACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
