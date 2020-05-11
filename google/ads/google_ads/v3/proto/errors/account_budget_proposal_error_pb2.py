# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/errors/account_budget_proposal_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/errors/account_budget_proposal_error.proto',
  package='google.ads.googleads.v3.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v3.errorsB\037AccountBudgetProposalErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V3.Errors\312\002\036Google\\Ads\\GoogleAds\\V3\\Errors\352\002\"Google::Ads::GoogleAds::V3::Errors'),
  serialized_pb=_b('\nHgoogle/ads/googleads_v3/proto/errors/account_budget_proposal_error.proto\x12\x1egoogle.ads.googleads.v3.errors\x1a\x1cgoogle/api/annotations.proto\"\xf2\x06\n\x1e\x41\x63\x63ountBudgetProposalErrorEnum\"\xcf\x06\n\x1a\x41\x63\x63ountBudgetProposalError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16\x46IELD_MASK_NOT_ALLOWED\x10\x02\x12\x13\n\x0fIMMUTABLE_FIELD\x10\x03\x12\x1a\n\x16REQUIRED_FIELD_MISSING\x10\x04\x12#\n\x1f\x43\x41NNOT_CANCEL_APPROVED_PROPOSAL\x10\x05\x12#\n\x1f\x43\x41NNOT_REMOVE_UNAPPROVED_BUDGET\x10\x06\x12 \n\x1c\x43\x41NNOT_REMOVE_RUNNING_BUDGET\x10\x07\x12 \n\x1c\x43\x41NNOT_END_UNAPPROVED_BUDGET\x10\x08\x12\x1e\n\x1a\x43\x41NNOT_END_INACTIVE_BUDGET\x10\t\x12\x18\n\x14\x42UDGET_NAME_REQUIRED\x10\n\x12\x1c\n\x18\x43\x41NNOT_UPDATE_OLD_BUDGET\x10\x0b\x12\x16\n\x12\x43\x41NNOT_END_IN_PAST\x10\x0c\x12\x1a\n\x16\x43\x41NNOT_EXTEND_END_TIME\x10\r\x12\"\n\x1ePURCHASE_ORDER_NUMBER_REQUIRED\x10\x0e\x12\"\n\x1ePENDING_UPDATE_PROPOSAL_EXISTS\x10\x0f\x12=\n9MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP\x10\x10\x12/\n+CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET\x10\x11\x12\x36\n2SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED\x10\x12\x12\x13\n\x0fUPDATE_IS_NO_OP\x10\x13\x12#\n\x1f\x45ND_TIME_MUST_FOLLOW_START_TIME\x10\x14\x12\x35\n1BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP\x10\x15\x12\x12\n\x0eNOT_AUTHORIZED\x10\x16\x12\x19\n\x15INVALID_BILLING_SETUP\x10\x17\x12\x1c\n\x18OVERLAPS_EXISTING_BUDGET\x10\x18\x42\xfa\x01\n\"com.google.ads.googleads.v3.errorsB\x1f\x41\x63\x63ountBudgetProposalErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v3/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V3.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V3\\Errors\xea\x02\"Google::Ads::GoogleAds::V3::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_ACCOUNTBUDGETPROPOSALERRORENUM_ACCOUNTBUDGETPROPOSALERROR = _descriptor.EnumDescriptor(
  name='AccountBudgetProposalError',
  full_name='google.ads.googleads.v3.errors.AccountBudgetProposalErrorEnum.AccountBudgetProposalError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIELD_MASK_NOT_ALLOWED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMMUTABLE_FIELD', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUIRED_FIELD_MISSING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CANCEL_APPROVED_PROPOSAL', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REMOVE_UNAPPROVED_BUDGET', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REMOVE_RUNNING_BUDGET', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_END_UNAPPROVED_BUDGET', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_END_INACTIVE_BUDGET', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDGET_NAME_REQUIRED', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_OLD_BUDGET', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_END_IN_PAST', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_EXTEND_END_TIME', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURCHASE_ORDER_NUMBER_REQUIRED', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING_UPDATE_PROPOSAL_EXISTS', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_IS_NO_OP', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END_TIME_MUST_FOLLOW_START_TIME', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_AUTHORIZED', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_BILLING_SETUP', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAPS_EXISTING_BUDGET', index=24, number=24,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=174,
  serialized_end=1021,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTBUDGETPROPOSALERRORENUM_ACCOUNTBUDGETPROPOSALERROR)


_ACCOUNTBUDGETPROPOSALERRORENUM = _descriptor.Descriptor(
  name='AccountBudgetProposalErrorEnum',
  full_name='google.ads.googleads.v3.errors.AccountBudgetProposalErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACCOUNTBUDGETPROPOSALERRORENUM_ACCOUNTBUDGETPROPOSALERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=1021,
)

_ACCOUNTBUDGETPROPOSALERRORENUM_ACCOUNTBUDGETPROPOSALERROR.containing_type = _ACCOUNTBUDGETPROPOSALERRORENUM
DESCRIPTOR.message_types_by_name['AccountBudgetProposalErrorEnum'] = _ACCOUNTBUDGETPROPOSALERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountBudgetProposalErrorEnum = _reflection.GeneratedProtocolMessageType('AccountBudgetProposalErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTBUDGETPROPOSALERRORENUM,
  __module__ = 'google.ads.googleads_v3.proto.errors.account_budget_proposal_error_pb2'
  ,
  __doc__ = """Container for enum describing possible account budget proposal errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.errors.AccountBudgetProposalErrorEnum)
  ))
_sym_db.RegisterMessage(AccountBudgetProposalErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
