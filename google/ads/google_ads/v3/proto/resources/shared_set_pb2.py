# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v3/proto/resources/shared_set.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v3.proto.enums import shared_set_status_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_shared__set__status__pb2
from google.ads.google_ads.v3.proto.enums import shared_set_type_pb2 as google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_shared__set__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v3/proto/resources/shared_set.proto',
  package='google.ads.googleads.v3.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v3.resourcesB\016SharedSetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V3.Resources\312\002!Google\\Ads\\GoogleAds\\V3\\Resources\352\002%Google::Ads::GoogleAds::V3::Resources'),
  serialized_pb=_b('\n8google/ads/googleads_v3/proto/resources/shared_set.proto\x12!google.ads.googleads.v3.resources\x1a;google/ads/googleads_v3/proto/enums/shared_set_status.proto\x1a\x39google/ads/googleads_v3/proto/enums/shared_set_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\x9e\x04\n\tSharedSet\x12\x41\n\rresource_name\x18\x01 \x01(\tB*\xe0\x41\x05\xfa\x41$\n\"googleads.googleapis.com/SharedSet\x12,\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12Q\n\x04type\x18\x03 \x01(\x0e\x32>.google.ads.googleads.v3.enums.SharedSetTypeEnum.SharedSetTypeB\x03\xe0\x41\x05\x12*\n\x04name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12W\n\x06status\x18\x05 \x01(\x0e\x32\x42.google.ads.googleads.v3.enums.SharedSetStatusEnum.SharedSetStatusB\x03\xe0\x41\x03\x12\x36\n\x0cmember_count\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03\x12\x39\n\x0freference_count\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x03\xe0\x41\x03:U\xea\x41R\n\"googleads.googleapis.com/SharedSet\x12,customers/{customer}/sharedSets/{shared_set}B\xfb\x01\n%com.google.ads.googleads.v3.resourcesB\x0eSharedSetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v3/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V3.Resources\xca\x02!Google\\Ads\\GoogleAds\\V3\\Resources\xea\x02%Google::Ads::GoogleAds::V3::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_shared__set__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_shared__set__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SHAREDSET = _descriptor.Descriptor(
  name='SharedSet',
  full_name='google.ads.googleads.v3.resources.SharedSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v3.resources.SharedSet.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005\372A$\n\"googleads.googleapis.com/SharedSet'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v3.resources.SharedSet.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v3.resources.SharedSet.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\005'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v3.resources.SharedSet.name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v3.resources.SharedSet.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_count', full_name='google.ads.googleads.v3.resources.SharedSet.member_count', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference_count', full_name='google.ads.googleads.v3.resources.SharedSet.reference_count', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\003'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\352AR\n\"googleads.googleapis.com/SharedSet\022,customers/{customer}/sharedSets/{shared_set}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=880,
)

_SHAREDSET.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SHAREDSET.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_shared__set__type__pb2._SHAREDSETTYPEENUM_SHAREDSETTYPE
_SHAREDSET.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SHAREDSET.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v3_dot_proto_dot_enums_dot_shared__set__status__pb2._SHAREDSETSTATUSENUM_SHAREDSETSTATUS
_SHAREDSET.fields_by_name['member_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SHAREDSET.fields_by_name['reference_count'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['SharedSet'] = _SHAREDSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedSet = _reflection.GeneratedProtocolMessageType('SharedSet', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSET,
  __module__ = 'google.ads.googleads_v3.proto.resources.shared_set_pb2'
  ,
  __doc__ = """SharedSets are used for sharing criterion exclusions across multiple
  campaigns.
  
  
  Attributes:
      resource_name:
          Immutable. The resource name of the shared set. Shared set
          resource names have the form:
          ``customers/{customer_id}/sharedSets/{shared_set_id}``
      id:
          Output only. The ID of this shared set. Read only.
      type:
          Immutable. The type of this shared set: each shared set holds
          only a single kind of resource. Required. Immutable.
      name:
          The name of this shared set. Required. Shared Sets must have
          names that are unique among active shared sets of the same
          type. The length of this string should be between 1 and 255
          UTF-8 bytes, inclusive.
      status:
          Output only. The status of this shared set. Read only.
      member_count:
          Output only. The number of shared criteria within this shared
          set. Read only.
      reference_count:
          Output only. The number of campaigns associated with this
          shared set. Read only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v3.resources.SharedSet)
  ))
_sym_db.RegisterMessage(SharedSet)


DESCRIPTOR._options = None
_SHAREDSET.fields_by_name['resource_name']._options = None
_SHAREDSET.fields_by_name['id']._options = None
_SHAREDSET.fields_by_name['type']._options = None
_SHAREDSET.fields_by_name['status']._options = None
_SHAREDSET.fields_by_name['member_count']._options = None
_SHAREDSET.fields_by_name['reference_count']._options = None
_SHAREDSET._options = None
# @@protoc_insertion_point(module_scope)
