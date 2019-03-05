# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/user_list_closing_reason.proto

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
  name='google/ads/googleads_v1/proto/enums/user_list_closing_reason.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\032UserListClosingReasonProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\nBgoogle/ads/googleads_v1/proto/enums/user_list_closing_reason.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"^\n\x19UserListClosingReasonEnum\"A\n\x15UserListClosingReason\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\n\n\x06UNUSED\x10\x02\x42\xef\x01\n!com.google.ads.googleads.v1.enumsB\x1aUserListClosingReasonProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_USERLISTCLOSINGREASONENUM_USERLISTCLOSINGREASON = _descriptor.EnumDescriptor(
  name='UserListClosingReason',
  full_name='google.ads.googleads.v1.enums.UserListClosingReasonEnum.UserListClosingReason',
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
      name='UNUSED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=160,
  serialized_end=225,
)
_sym_db.RegisterEnumDescriptor(_USERLISTCLOSINGREASONENUM_USERLISTCLOSINGREASON)


_USERLISTCLOSINGREASONENUM = _descriptor.Descriptor(
  name='UserListClosingReasonEnum',
  full_name='google.ads.googleads.v1.enums.UserListClosingReasonEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERLISTCLOSINGREASONENUM_USERLISTCLOSINGREASON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=131,
  serialized_end=225,
)

_USERLISTCLOSINGREASONENUM_USERLISTCLOSINGREASON.containing_type = _USERLISTCLOSINGREASONENUM
DESCRIPTOR.message_types_by_name['UserListClosingReasonEnum'] = _USERLISTCLOSINGREASONENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserListClosingReasonEnum = _reflection.GeneratedProtocolMessageType('UserListClosingReasonEnum', (_message.Message,), dict(
  DESCRIPTOR = _USERLISTCLOSINGREASONENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.user_list_closing_reason_pb2'
  ,
  __doc__ = """Indicates the reason why the userlist was closed. This enum is only used
  when a list is auto-closed by the system.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.UserListClosingReasonEnum)
  ))
_sym_db.RegisterMessage(UserListClosingReasonEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
