# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AS_redis.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='AS_redis.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x41S_redis.proto\"6\n\x07User_AI\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x0e\n\x06Key_op\x18\x02 \x01(\t\x12\x0f\n\x07Key_tgs\x18\x03 \x01(\tb\x06proto3')
)




_USER_AI = _descriptor.Descriptor(
  name='User_AI',
  full_name='User_AI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='User_AI.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Key_op', full_name='User_AI.Key_op', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Key_tgs', full_name='User_AI.Key_tgs', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=18,
  serialized_end=72,
)

DESCRIPTOR.message_types_by_name['User_AI'] = _USER_AI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User_AI = _reflection.GeneratedProtocolMessageType('User_AI', (_message.Message,), dict(
  DESCRIPTOR = _USER_AI,
  __module__ = 'AS_redis_pb2'
  # @@protoc_insertion_point(class_scope:User_AI)
  ))
_sym_db.RegisterMessage(User_AI)


# @@protoc_insertion_point(module_scope)