# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/ClientState.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import WidgetStates_pb2 as streamlit_dot_proto_dot_WidgetStates__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/ClientState.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!streamlit/proto/ClientState.proto\x1a\"streamlit/proto/WidgetStates.proto\"I\n\x0b\x43lientState\x12\x14\n\x0cquery_string\x18\x01 \x01(\t\x12$\n\rwidget_states\x18\x02 \x01(\x0b\x32\r.WidgetStatesb\x06proto3'
  ,
  dependencies=[streamlit_dot_proto_dot_WidgetStates__pb2.DESCRIPTOR,])




_CLIENTSTATE = _descriptor.Descriptor(
  name='ClientState',
  full_name='ClientState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_string', full_name='ClientState.query_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='widget_states', full_name='ClientState.widget_states', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=73,
  serialized_end=146,
)

_CLIENTSTATE.fields_by_name['widget_states'].message_type = streamlit_dot_proto_dot_WidgetStates__pb2._WIDGETSTATES
DESCRIPTOR.message_types_by_name['ClientState'] = _CLIENTSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientState = _reflection.GeneratedProtocolMessageType('ClientState', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSTATE,
  '__module__' : 'streamlit.proto.ClientState_pb2'
  # @@protoc_insertion_point(class_scope:ClientState)
  })
_sym_db.RegisterMessage(ClientState)


# @@protoc_insertion_point(module_scope)
