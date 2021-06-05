# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/WidgetStates.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import Common_pb2 as streamlit_dot_proto_dot_Common__pb2
from streamlit.proto import ArrowTable_pb2 as streamlit_dot_proto_dot_ArrowTable__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/WidgetStates.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"streamlit/proto/WidgetStates.proto\x1a\x1cstreamlit/proto/Common.proto\x1a streamlit/proto/ArrowTable.proto\"-\n\x0cWidgetStates\x12\x1d\n\x07widgets\x18\x01 \x03(\x0b\x32\x0c.WidgetState\"\xe8\x02\n\x0bWidgetState\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\rtrigger_value\x18\x02 \x01(\x08H\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x12\x13\n\tint_value\x18\x05 \x01(\x12H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x12*\n\x12\x64ouble_array_value\x18\x07 \x01(\x0b\x32\x0c.DoubleArrayH\x00\x12\'\n\x0fint_array_value\x18\x08 \x01(\x0b\x32\x0c.SInt64ArrayH\x00\x12*\n\x12string_array_value\x18\t \x01(\x0b\x32\x0c.StringArrayH\x00\x12\x14\n\njson_value\x18\n \x01(\tH\x00\x12\"\n\x0b\x61rrow_value\x18\x0b \x01(\x0b\x32\x0b.ArrowTableH\x00\x12\x15\n\x0b\x62ytes_value\x18\x0c \x01(\x0cH\x00\x42\x07\n\x05valueb\x06proto3'
  ,
  dependencies=[streamlit_dot_proto_dot_Common__pb2.DESCRIPTOR,streamlit_dot_proto_dot_ArrowTable__pb2.DESCRIPTOR,])




_WIDGETSTATES = _descriptor.Descriptor(
  name='WidgetStates',
  full_name='WidgetStates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='widgets', full_name='WidgetStates.widgets', index=0,
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
  serialized_start=102,
  serialized_end=147,
)


_WIDGETSTATE = _descriptor.Descriptor(
  name='WidgetState',
  full_name='WidgetState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WidgetState.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trigger_value', full_name='WidgetState.trigger_value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='WidgetState.bool_value', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='WidgetState.double_value', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_value', full_name='WidgetState.int_value', index=4,
      number=5, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='WidgetState.string_value', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_array_value', full_name='WidgetState.double_array_value', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_array_value', full_name='WidgetState.int_array_value', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_array_value', full_name='WidgetState.string_array_value', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_value', full_name='WidgetState.json_value', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arrow_value', full_name='WidgetState.arrow_value', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='WidgetState.bytes_value', index=11,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
      name='value', full_name='WidgetState.value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=150,
  serialized_end=510,
)

_WIDGETSTATES.fields_by_name['widgets'].message_type = _WIDGETSTATE
_WIDGETSTATE.fields_by_name['double_array_value'].message_type = streamlit_dot_proto_dot_Common__pb2._DOUBLEARRAY
_WIDGETSTATE.fields_by_name['int_array_value'].message_type = streamlit_dot_proto_dot_Common__pb2._SINT64ARRAY
_WIDGETSTATE.fields_by_name['string_array_value'].message_type = streamlit_dot_proto_dot_Common__pb2._STRINGARRAY
_WIDGETSTATE.fields_by_name['arrow_value'].message_type = streamlit_dot_proto_dot_ArrowTable__pb2._ARROWTABLE
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['trigger_value'])
_WIDGETSTATE.fields_by_name['trigger_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['bool_value'])
_WIDGETSTATE.fields_by_name['bool_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['double_value'])
_WIDGETSTATE.fields_by_name['double_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['int_value'])
_WIDGETSTATE.fields_by_name['int_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['string_value'])
_WIDGETSTATE.fields_by_name['string_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['double_array_value'])
_WIDGETSTATE.fields_by_name['double_array_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['int_array_value'])
_WIDGETSTATE.fields_by_name['int_array_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['string_array_value'])
_WIDGETSTATE.fields_by_name['string_array_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['json_value'])
_WIDGETSTATE.fields_by_name['json_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['arrow_value'])
_WIDGETSTATE.fields_by_name['arrow_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
_WIDGETSTATE.oneofs_by_name['value'].fields.append(
  _WIDGETSTATE.fields_by_name['bytes_value'])
_WIDGETSTATE.fields_by_name['bytes_value'].containing_oneof = _WIDGETSTATE.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['WidgetStates'] = _WIDGETSTATES
DESCRIPTOR.message_types_by_name['WidgetState'] = _WIDGETSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WidgetStates = _reflection.GeneratedProtocolMessageType('WidgetStates', (_message.Message,), {
  'DESCRIPTOR' : _WIDGETSTATES,
  '__module__' : 'streamlit.proto.WidgetStates_pb2'
  # @@protoc_insertion_point(class_scope:WidgetStates)
  })
_sym_db.RegisterMessage(WidgetStates)

WidgetState = _reflection.GeneratedProtocolMessageType('WidgetState', (_message.Message,), {
  'DESCRIPTOR' : _WIDGETSTATE,
  '__module__' : 'streamlit.proto.WidgetStates_pb2'
  # @@protoc_insertion_point(class_scope:WidgetState)
  })
_sym_db.RegisterMessage(WidgetState)


# @@protoc_insertion_point(module_scope)
