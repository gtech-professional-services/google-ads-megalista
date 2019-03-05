# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/operating_system_version_constant.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.enums import operating_system_version_operator_type_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_operating__system__version__operator__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/operating_system_version_constant.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB#OperatingSystemVersionConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\nOgoogle/ads/googleads_v1/proto/resources/operating_system_version_constant.proto\x12!google.ads.googleads.v1.resources\x1aPgoogle/ads/googleads_v1/proto/enums/operating_system_version_operator_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xfb\x02\n\x1eOperatingSystemVersionConstant\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x10os_major_version\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x10os_minor_version\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x7f\n\roperator_type\x18\x06 \x01(\x0e\x32h.google.ads.googleads.v1.enums.OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorTypeB\x90\x02\n%com.google.ads.googleads.v1.resourcesB#OperatingSystemVersionConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_operating__system__version__operator__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_OPERATINGSYSTEMVERSIONCONSTANT = _descriptor.Descriptor(
  name='OperatingSystemVersionConstant',
  full_name='google.ads.googleads.v1.resources.OperatingSystemVersionConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.OperatingSystemVersionConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v1.resources.OperatingSystemVersionConstant.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v1.resources.OperatingSystemVersionConstant.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os_major_version', full_name='google.ads.googleads.v1.resources.OperatingSystemVersionConstant.os_major_version', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='os_minor_version', full_name='google.ads.googleads.v1.resources.OperatingSystemVersionConstant.os_minor_version', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operator_type', full_name='google.ads.googleads.v1.resources.OperatingSystemVersionConstant.operator_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=263,
  serialized_end=642,
)

_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['os_major_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['os_minor_version'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_OPERATINGSYSTEMVERSIONCONSTANT.fields_by_name['operator_type'].enum_type = google_dot_ads_dot_googleads__v1_dot_proto_dot_enums_dot_operating__system__version__operator__type__pb2._OPERATINGSYSTEMVERSIONOPERATORTYPEENUM_OPERATINGSYSTEMVERSIONOPERATORTYPE
DESCRIPTOR.message_types_by_name['OperatingSystemVersionConstant'] = _OPERATINGSYSTEMVERSIONCONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OperatingSystemVersionConstant = _reflection.GeneratedProtocolMessageType('OperatingSystemVersionConstant', (_message.Message,), dict(
  DESCRIPTOR = _OPERATINGSYSTEMVERSIONCONSTANT,
  __module__ = 'google.ads.googleads_v1.proto.resources.operating_system_version_constant_pb2'
  ,
  __doc__ = """A mobile operating system version or a range of versions, depending on
  'operator\_type'. The complete list of available mobile platforms is
  available <a
  
  href="https://developers.google.com/adwords/api/docs/appendix/codes-formats#mobile-platforms>
  here.
  
  
  Attributes:
      resource_name:
          The resource name of the operating system version constant.
          Operating system version constant resource names have the
          form:  ``operatingSystemVersionConstants/{criterion_id}``
      id:
          The ID of the operating system version.
      name:
          Name of the operating system.
      os_major_version:
          The OS Major Version number.
      os_minor_version:
          The OS Minor Version number.
      operator_type:
          Determines whether this constant represents a single version
          or a range of versions.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.OperatingSystemVersionConstant)
  ))
_sym_db.RegisterMessage(OperatingSystemVersionConstant)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
