# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indigo_influx.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='indigo_influx.proto',
  package='indigo_influx',
  syntax='proto3',
  serialized_options=b'\n\037smurfless.com/grpc/indigoinfluxB\020IndigoInfluxGrpcZ\037smurfless.com/grpc/indigoinflux',
  serialized_pb=b'\n\x13indigo_influx.proto\x12\rindigo_influx\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"e\n\tInfluxTag\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x66older\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xbf\x01\n\x0bInfluxEvent\x12\x31\n\x0bmeasurement\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12&\n\x04tags\x18\x03 \x01(\x0b\x32\x18.indigo_influx.InfluxTag\x12+\n\x06\x66ields\x18\x04 \x01(\x0b\x32\x1b.indigo_influx.InfluxFields\"\xae\x02\n\x0cInfluxFields\x12&\n\x02on\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\nbrightness\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x31\n\x0c\x63oolSetpoint\x18\x14 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x31\n\x0cheatSetpoint\x18\x15 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x30\n\x0btemperature\x18\x16 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12-\n\x08humidity\x18\x17 \x01(\x0b\x32\x1b.google.protobuf.FloatValueBT\n\x1fsmurfless.com/grpc/indigoinfluxB\x10IndigoInfluxGrpcZ\x1fsmurfless.com/grpc/indigoinfluxb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_INFLUXTAG = _descriptor.Descriptor(
  name='InfluxTag',
  full_name='indigo_influx.InfluxTag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='indigo_influx.InfluxTag.name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folder', full_name='indigo_influx.InfluxTag.folder', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=103,
  serialized_end=204,
)


_INFLUXEVENT = _descriptor.Descriptor(
  name='InfluxEvent',
  full_name='indigo_influx.InfluxEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='measurement', full_name='indigo_influx.InfluxEvent.measurement', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='indigo_influx.InfluxEvent.time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='indigo_influx.InfluxEvent.tags', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='indigo_influx.InfluxEvent.fields', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=207,
  serialized_end=398,
)


_INFLUXFIELDS = _descriptor.Descriptor(
  name='InfluxFields',
  full_name='indigo_influx.InfluxFields',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='on', full_name='indigo_influx.InfluxFields.on', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brightness', full_name='indigo_influx.InfluxFields.brightness', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coolSetpoint', full_name='indigo_influx.InfluxFields.coolSetpoint', index=2,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heatSetpoint', full_name='indigo_influx.InfluxFields.heatSetpoint', index=3,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='indigo_influx.InfluxFields.temperature', index=4,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='indigo_influx.InfluxFields.humidity', index=5,
      number=23, type=11, cpp_type=10, label=1,
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
  serialized_start=401,
  serialized_end=703,
)

_INFLUXTAG.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_INFLUXTAG.fields_by_name['folder'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_INFLUXEVENT.fields_by_name['measurement'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_INFLUXEVENT.fields_by_name['time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_INFLUXEVENT.fields_by_name['tags'].message_type = _INFLUXTAG
_INFLUXEVENT.fields_by_name['fields'].message_type = _INFLUXFIELDS
_INFLUXFIELDS.fields_by_name['on'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_INFLUXFIELDS.fields_by_name['brightness'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_INFLUXFIELDS.fields_by_name['coolSetpoint'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_INFLUXFIELDS.fields_by_name['heatSetpoint'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_INFLUXFIELDS.fields_by_name['temperature'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
_INFLUXFIELDS.fields_by_name['humidity'].message_type = google_dot_protobuf_dot_wrappers__pb2._FLOATVALUE
DESCRIPTOR.message_types_by_name['InfluxTag'] = _INFLUXTAG
DESCRIPTOR.message_types_by_name['InfluxEvent'] = _INFLUXEVENT
DESCRIPTOR.message_types_by_name['InfluxFields'] = _INFLUXFIELDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InfluxTag = _reflection.GeneratedProtocolMessageType('InfluxTag', (_message.Message,), {
  'DESCRIPTOR' : _INFLUXTAG,
  '__module__' : 'indigo_influx_pb2'
  # @@protoc_insertion_point(class_scope:indigo_influx.InfluxTag)
  })
_sym_db.RegisterMessage(InfluxTag)

InfluxEvent = _reflection.GeneratedProtocolMessageType('InfluxEvent', (_message.Message,), {
  'DESCRIPTOR' : _INFLUXEVENT,
  '__module__' : 'indigo_influx_pb2'
  # @@protoc_insertion_point(class_scope:indigo_influx.InfluxEvent)
  })
_sym_db.RegisterMessage(InfluxEvent)

InfluxFields = _reflection.GeneratedProtocolMessageType('InfluxFields', (_message.Message,), {
  'DESCRIPTOR' : _INFLUXFIELDS,
  '__module__' : 'indigo_influx_pb2'
  # @@protoc_insertion_point(class_scope:indigo_influx.InfluxFields)
  })
_sym_db.RegisterMessage(InfluxFields)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
