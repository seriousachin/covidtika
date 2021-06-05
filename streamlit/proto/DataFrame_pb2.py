# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/DataFrame.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import Common_pb2 as streamlit_dot_proto_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/DataFrame.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fstreamlit/proto/DataFrame.proto\x1a\x1cstreamlit/proto/Common.proto\"m\n\tDataFrame\x12\x14\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x06.Table\x12\x15\n\x05index\x18\x02 \x01(\x0b\x32\x06.Index\x12\x17\n\x07\x63olumns\x18\x03 \x01(\x0b\x32\x06.Index\x12\x1a\n\x05style\x18\x04 \x01(\x0b\x32\x0b.TableStyle\"\x9f\x02\n\x05Index\x12\"\n\x0bplain_index\x18\x01 \x01(\x0b\x32\x0b.PlainIndexH\x00\x12\"\n\x0brange_index\x18\x02 \x01(\x0b\x32\x0b.RangeIndexH\x00\x12\"\n\x0bmulti_index\x18\x04 \x01(\x0b\x32\x0b.MultiIndexH\x00\x12(\n\x0e\x64\x61tetime_index\x18\x06 \x01(\x0b\x32\x0e.DatetimeIndexH\x00\x12*\n\x0ftimedelta_index\x18\x07 \x01(\x0b\x32\x0f.TimedeltaIndexH\x00\x12#\n\x0cint_64_index\x18\t \x01(\x0b\x32\x0b.Int64IndexH\x00\x12\'\n\x0e\x66loat_64_index\x18\x0b \x01(\x0b\x32\r.Float64IndexH\x00\x42\x06\n\x04type\"%\n\nPlainIndex\x12\x17\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\t.AnyArray\")\n\nRangeIndex\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0c\n\x04stop\x18\x02 \x01(\x03\"A\n\nMultiIndex\x12\x16\n\x06levels\x18\x01 \x03(\x0b\x32\x06.Index\x12\x1b\n\x06labels\x18\x02 \x03(\x0b\x32\x0b.Int32Array\"+\n\rDatetimeIndex\x12\x1a\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0c.StringArray\"+\n\x0eTimedeltaIndex\x12\x19\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0b.Int64Array\"\'\n\nInt64Index\x12\x19\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0b.Int64Array\"*\n\x0c\x46loat64Index\x12\x1a\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0c.DoubleArray\"+\n\x08\x43SSStyle\x12\x10\n\x08property\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"U\n\tCellStyle\x12\x16\n\x03\x63ss\x18\x01 \x03(\x0b\x32\t.CSSStyle\x12\x15\n\rdisplay_value\x18\x02 \x01(\t\x12\x19\n\x11has_display_value\x18\x03 \x01(\x08\",\n\x0e\x43\x65llStyleArray\x12\x1a\n\x06styles\x18\x01 \x03(\x0b\x32\n.CellStyle\"\xb9\x01\n\x08\x41nyArray\x12\x1f\n\x07strings\x18\x01 \x01(\x0b\x32\x0c.StringArrayH\x00\x12\x1f\n\x07\x64oubles\x18\x02 \x01(\x0b\x32\x0c.DoubleArrayH\x00\x12\x1d\n\x06int64s\x18\x03 \x01(\x0b\x32\x0b.Int64ArrayH\x00\x12!\n\tdatetimes\x18\x04 \x01(\x0b\x32\x0c.StringArrayH\x00\x12!\n\ntimedeltas\x18\x05 \x01(\x0b\x32\x0b.Int64ArrayH\x00\x42\x06\n\x04type\" \n\x05Table\x12\x17\n\x04\x63ols\x18\x01 \x03(\x0b\x32\t.AnyArray\"+\n\nTableStyle\x12\x1d\n\x04\x63ols\x18\x01 \x03(\x0b\x32\x0f.CellStyleArrayb\x06proto3'
  ,
  dependencies=[streamlit_dot_proto_dot_Common__pb2.DESCRIPTOR,])




_DATAFRAME = _descriptor.Descriptor(
  name='DataFrame',
  full_name='DataFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DataFrame.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='DataFrame.index', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='columns', full_name='DataFrame.columns', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='style', full_name='DataFrame.style', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=65,
  serialized_end=174,
)


_INDEX = _descriptor.Descriptor(
  name='Index',
  full_name='Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='plain_index', full_name='Index.plain_index', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='range_index', full_name='Index.range_index', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multi_index', full_name='Index.multi_index', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datetime_index', full_name='Index.datetime_index', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timedelta_index', full_name='Index.timedelta_index', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int_64_index', full_name='Index.int_64_index', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='float_64_index', full_name='Index.float_64_index', index=6,
      number=11, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='type', full_name='Index.type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=177,
  serialized_end=464,
)


_PLAININDEX = _descriptor.Descriptor(
  name='PlainIndex',
  full_name='PlainIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PlainIndex.data', index=0,
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
  serialized_start=466,
  serialized_end=503,
)


_RANGEINDEX = _descriptor.Descriptor(
  name='RangeIndex',
  full_name='RangeIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='RangeIndex.start', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stop', full_name='RangeIndex.stop', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=505,
  serialized_end=546,
)


_MULTIINDEX = _descriptor.Descriptor(
  name='MultiIndex',
  full_name='MultiIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='levels', full_name='MultiIndex.levels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='MultiIndex.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=548,
  serialized_end=613,
)


_DATETIMEINDEX = _descriptor.Descriptor(
  name='DatetimeIndex',
  full_name='DatetimeIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DatetimeIndex.data', index=0,
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
  serialized_start=615,
  serialized_end=658,
)


_TIMEDELTAINDEX = _descriptor.Descriptor(
  name='TimedeltaIndex',
  full_name='TimedeltaIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='TimedeltaIndex.data', index=0,
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
  serialized_start=660,
  serialized_end=703,
)


_INT64INDEX = _descriptor.Descriptor(
  name='Int64Index',
  full_name='Int64Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Int64Index.data', index=0,
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
  serialized_start=705,
  serialized_end=744,
)


_FLOAT64INDEX = _descriptor.Descriptor(
  name='Float64Index',
  full_name='Float64Index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Float64Index.data', index=0,
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
  serialized_start=746,
  serialized_end=788,
)


_CSSSTYLE = _descriptor.Descriptor(
  name='CSSStyle',
  full_name='CSSStyle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='property', full_name='CSSStyle.property', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='CSSStyle.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=790,
  serialized_end=833,
)


_CELLSTYLE = _descriptor.Descriptor(
  name='CellStyle',
  full_name='CellStyle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='css', full_name='CellStyle.css', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_value', full_name='CellStyle.display_value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_display_value', full_name='CellStyle.has_display_value', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=835,
  serialized_end=920,
)


_CELLSTYLEARRAY = _descriptor.Descriptor(
  name='CellStyleArray',
  full_name='CellStyleArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='styles', full_name='CellStyleArray.styles', index=0,
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
  serialized_start=922,
  serialized_end=966,
)


_ANYARRAY = _descriptor.Descriptor(
  name='AnyArray',
  full_name='AnyArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='strings', full_name='AnyArray.strings', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='doubles', full_name='AnyArray.doubles', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='int64s', full_name='AnyArray.int64s', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datetimes', full_name='AnyArray.datetimes', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timedeltas', full_name='AnyArray.timedeltas', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='type', full_name='AnyArray.type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=969,
  serialized_end=1154,
)


_TABLE = _descriptor.Descriptor(
  name='Table',
  full_name='Table',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cols', full_name='Table.cols', index=0,
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
  serialized_start=1156,
  serialized_end=1188,
)


_TABLESTYLE = _descriptor.Descriptor(
  name='TableStyle',
  full_name='TableStyle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cols', full_name='TableStyle.cols', index=0,
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
  serialized_start=1190,
  serialized_end=1233,
)

_DATAFRAME.fields_by_name['data'].message_type = _TABLE
_DATAFRAME.fields_by_name['index'].message_type = _INDEX
_DATAFRAME.fields_by_name['columns'].message_type = _INDEX
_DATAFRAME.fields_by_name['style'].message_type = _TABLESTYLE
_INDEX.fields_by_name['plain_index'].message_type = _PLAININDEX
_INDEX.fields_by_name['range_index'].message_type = _RANGEINDEX
_INDEX.fields_by_name['multi_index'].message_type = _MULTIINDEX
_INDEX.fields_by_name['datetime_index'].message_type = _DATETIMEINDEX
_INDEX.fields_by_name['timedelta_index'].message_type = _TIMEDELTAINDEX
_INDEX.fields_by_name['int_64_index'].message_type = _INT64INDEX
_INDEX.fields_by_name['float_64_index'].message_type = _FLOAT64INDEX
_INDEX.oneofs_by_name['type'].fields.append(
  _INDEX.fields_by_name['plain_index'])
_INDEX.fields_by_name['plain_index'].containing_oneof = _INDEX.oneofs_by_name['type']
_INDEX.oneofs_by_name['type'].fields.append(
  _INDEX.fields_by_name['range_index'])
_INDEX.fields_by_name['range_index'].containing_oneof = _INDEX.oneofs_by_name['type']
_INDEX.oneofs_by_name['type'].fields.append(
  _INDEX.fields_by_name['multi_index'])
_INDEX.fields_by_name['multi_index'].containing_oneof = _INDEX.oneofs_by_name['type']
_INDEX.oneofs_by_name['type'].fields.append(
  _INDEX.fields_by_name['datetime_index'])
_INDEX.fields_by_name['datetime_index'].containing_oneof = _INDEX.oneofs_by_name['type']
_INDEX.oneofs_by_name['type'].fields.append(
  _INDEX.fields_by_name['timedelta_index'])
_INDEX.fields_by_name['timedelta_index'].containing_oneof = _INDEX.oneofs_by_name['type']
_INDEX.oneofs_by_name['type'].fields.append(
  _INDEX.fields_by_name['int_64_index'])
_INDEX.fields_by_name['int_64_index'].containing_oneof = _INDEX.oneofs_by_name['type']
_INDEX.oneofs_by_name['type'].fields.append(
  _INDEX.fields_by_name['float_64_index'])
_INDEX.fields_by_name['float_64_index'].containing_oneof = _INDEX.oneofs_by_name['type']
_PLAININDEX.fields_by_name['data'].message_type = _ANYARRAY
_MULTIINDEX.fields_by_name['levels'].message_type = _INDEX
_MULTIINDEX.fields_by_name['labels'].message_type = streamlit_dot_proto_dot_Common__pb2._INT32ARRAY
_DATETIMEINDEX.fields_by_name['data'].message_type = streamlit_dot_proto_dot_Common__pb2._STRINGARRAY
_TIMEDELTAINDEX.fields_by_name['data'].message_type = streamlit_dot_proto_dot_Common__pb2._INT64ARRAY
_INT64INDEX.fields_by_name['data'].message_type = streamlit_dot_proto_dot_Common__pb2._INT64ARRAY
_FLOAT64INDEX.fields_by_name['data'].message_type = streamlit_dot_proto_dot_Common__pb2._DOUBLEARRAY
_CELLSTYLE.fields_by_name['css'].message_type = _CSSSTYLE
_CELLSTYLEARRAY.fields_by_name['styles'].message_type = _CELLSTYLE
_ANYARRAY.fields_by_name['strings'].message_type = streamlit_dot_proto_dot_Common__pb2._STRINGARRAY
_ANYARRAY.fields_by_name['doubles'].message_type = streamlit_dot_proto_dot_Common__pb2._DOUBLEARRAY
_ANYARRAY.fields_by_name['int64s'].message_type = streamlit_dot_proto_dot_Common__pb2._INT64ARRAY
_ANYARRAY.fields_by_name['datetimes'].message_type = streamlit_dot_proto_dot_Common__pb2._STRINGARRAY
_ANYARRAY.fields_by_name['timedeltas'].message_type = streamlit_dot_proto_dot_Common__pb2._INT64ARRAY
_ANYARRAY.oneofs_by_name['type'].fields.append(
  _ANYARRAY.fields_by_name['strings'])
_ANYARRAY.fields_by_name['strings'].containing_oneof = _ANYARRAY.oneofs_by_name['type']
_ANYARRAY.oneofs_by_name['type'].fields.append(
  _ANYARRAY.fields_by_name['doubles'])
_ANYARRAY.fields_by_name['doubles'].containing_oneof = _ANYARRAY.oneofs_by_name['type']
_ANYARRAY.oneofs_by_name['type'].fields.append(
  _ANYARRAY.fields_by_name['int64s'])
_ANYARRAY.fields_by_name['int64s'].containing_oneof = _ANYARRAY.oneofs_by_name['type']
_ANYARRAY.oneofs_by_name['type'].fields.append(
  _ANYARRAY.fields_by_name['datetimes'])
_ANYARRAY.fields_by_name['datetimes'].containing_oneof = _ANYARRAY.oneofs_by_name['type']
_ANYARRAY.oneofs_by_name['type'].fields.append(
  _ANYARRAY.fields_by_name['timedeltas'])
_ANYARRAY.fields_by_name['timedeltas'].containing_oneof = _ANYARRAY.oneofs_by_name['type']
_TABLE.fields_by_name['cols'].message_type = _ANYARRAY
_TABLESTYLE.fields_by_name['cols'].message_type = _CELLSTYLEARRAY
DESCRIPTOR.message_types_by_name['DataFrame'] = _DATAFRAME
DESCRIPTOR.message_types_by_name['Index'] = _INDEX
DESCRIPTOR.message_types_by_name['PlainIndex'] = _PLAININDEX
DESCRIPTOR.message_types_by_name['RangeIndex'] = _RANGEINDEX
DESCRIPTOR.message_types_by_name['MultiIndex'] = _MULTIINDEX
DESCRIPTOR.message_types_by_name['DatetimeIndex'] = _DATETIMEINDEX
DESCRIPTOR.message_types_by_name['TimedeltaIndex'] = _TIMEDELTAINDEX
DESCRIPTOR.message_types_by_name['Int64Index'] = _INT64INDEX
DESCRIPTOR.message_types_by_name['Float64Index'] = _FLOAT64INDEX
DESCRIPTOR.message_types_by_name['CSSStyle'] = _CSSSTYLE
DESCRIPTOR.message_types_by_name['CellStyle'] = _CELLSTYLE
DESCRIPTOR.message_types_by_name['CellStyleArray'] = _CELLSTYLEARRAY
DESCRIPTOR.message_types_by_name['AnyArray'] = _ANYARRAY
DESCRIPTOR.message_types_by_name['Table'] = _TABLE
DESCRIPTOR.message_types_by_name['TableStyle'] = _TABLESTYLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataFrame = _reflection.GeneratedProtocolMessageType('DataFrame', (_message.Message,), {
  'DESCRIPTOR' : _DATAFRAME,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:DataFrame)
  })
_sym_db.RegisterMessage(DataFrame)

Index = _reflection.GeneratedProtocolMessageType('Index', (_message.Message,), {
  'DESCRIPTOR' : _INDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:Index)
  })
_sym_db.RegisterMessage(Index)

PlainIndex = _reflection.GeneratedProtocolMessageType('PlainIndex', (_message.Message,), {
  'DESCRIPTOR' : _PLAININDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:PlainIndex)
  })
_sym_db.RegisterMessage(PlainIndex)

RangeIndex = _reflection.GeneratedProtocolMessageType('RangeIndex', (_message.Message,), {
  'DESCRIPTOR' : _RANGEINDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:RangeIndex)
  })
_sym_db.RegisterMessage(RangeIndex)

MultiIndex = _reflection.GeneratedProtocolMessageType('MultiIndex', (_message.Message,), {
  'DESCRIPTOR' : _MULTIINDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:MultiIndex)
  })
_sym_db.RegisterMessage(MultiIndex)

DatetimeIndex = _reflection.GeneratedProtocolMessageType('DatetimeIndex', (_message.Message,), {
  'DESCRIPTOR' : _DATETIMEINDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:DatetimeIndex)
  })
_sym_db.RegisterMessage(DatetimeIndex)

TimedeltaIndex = _reflection.GeneratedProtocolMessageType('TimedeltaIndex', (_message.Message,), {
  'DESCRIPTOR' : _TIMEDELTAINDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:TimedeltaIndex)
  })
_sym_db.RegisterMessage(TimedeltaIndex)

Int64Index = _reflection.GeneratedProtocolMessageType('Int64Index', (_message.Message,), {
  'DESCRIPTOR' : _INT64INDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:Int64Index)
  })
_sym_db.RegisterMessage(Int64Index)

Float64Index = _reflection.GeneratedProtocolMessageType('Float64Index', (_message.Message,), {
  'DESCRIPTOR' : _FLOAT64INDEX,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:Float64Index)
  })
_sym_db.RegisterMessage(Float64Index)

CSSStyle = _reflection.GeneratedProtocolMessageType('CSSStyle', (_message.Message,), {
  'DESCRIPTOR' : _CSSSTYLE,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:CSSStyle)
  })
_sym_db.RegisterMessage(CSSStyle)

CellStyle = _reflection.GeneratedProtocolMessageType('CellStyle', (_message.Message,), {
  'DESCRIPTOR' : _CELLSTYLE,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:CellStyle)
  })
_sym_db.RegisterMessage(CellStyle)

CellStyleArray = _reflection.GeneratedProtocolMessageType('CellStyleArray', (_message.Message,), {
  'DESCRIPTOR' : _CELLSTYLEARRAY,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:CellStyleArray)
  })
_sym_db.RegisterMessage(CellStyleArray)

AnyArray = _reflection.GeneratedProtocolMessageType('AnyArray', (_message.Message,), {
  'DESCRIPTOR' : _ANYARRAY,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:AnyArray)
  })
_sym_db.RegisterMessage(AnyArray)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {
  'DESCRIPTOR' : _TABLE,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:Table)
  })
_sym_db.RegisterMessage(Table)

TableStyle = _reflection.GeneratedProtocolMessageType('TableStyle', (_message.Message,), {
  'DESCRIPTOR' : _TABLESTYLE,
  '__module__' : 'streamlit.proto.DataFrame_pb2'
  # @@protoc_insertion_point(class_scope:TableStyle)
  })
_sym_db.RegisterMessage(TableStyle)


# @@protoc_insertion_point(module_scope)
