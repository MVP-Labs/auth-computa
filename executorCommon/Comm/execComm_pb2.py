# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execComm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='execComm.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x65xecComm.proto\"\x0c\n\nStageQuery\"\x16\n\x05Stage\x12\r\n\x05stage\x18\x01 \x01(\x05\"\r\n\x0bStatusQuery\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\n\n\x08\x45xitCall\"\x19\n\nExitResult\x12\x0b\n\x03res\x18\x01 \x01(\x05\x32y\n\x08\x45xecComm\x12!\n\x08GetStage\x12\x0b.StageQuery\x1a\x06.Stage\"\x00\x12$\n\tGetStatus\x12\x0c.StatusQuery\x1a\x07.Status\"\x00\x12$\n\x08\x43\x61llExit\x12\t.ExitCall\x1a\x0b.ExitResult\"\x00\x62\x06proto3')
)




_STAGEQUERY = _descriptor.Descriptor(
  name='StageQuery',
  full_name='StageQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_end=30,
)


_STAGE = _descriptor.Descriptor(
  name='Stage',
  full_name='Stage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stage', full_name='Stage.stage', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=32,
  serialized_end=54,
)


_STATUSQUERY = _descriptor.Descriptor(
  name='StatusQuery',
  full_name='StatusQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=56,
  serialized_end=69,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='Status.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=71,
  serialized_end=95,
)


_EXITCALL = _descriptor.Descriptor(
  name='ExitCall',
  full_name='ExitCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=97,
  serialized_end=107,
)


_EXITRESULT = _descriptor.Descriptor(
  name='ExitResult',
  full_name='ExitResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='ExitResult.res', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=109,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['StageQuery'] = _STAGEQUERY
DESCRIPTOR.message_types_by_name['Stage'] = _STAGE
DESCRIPTOR.message_types_by_name['StatusQuery'] = _STATUSQUERY
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['ExitCall'] = _EXITCALL
DESCRIPTOR.message_types_by_name['ExitResult'] = _EXITRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StageQuery = _reflection.GeneratedProtocolMessageType('StageQuery', (_message.Message,), dict(
  DESCRIPTOR = _STAGEQUERY,
  __module__ = 'execComm_pb2'
  # @@protoc_insertion_point(class_scope:StageQuery)
  ))
_sym_db.RegisterMessage(StageQuery)

Stage = _reflection.GeneratedProtocolMessageType('Stage', (_message.Message,), dict(
  DESCRIPTOR = _STAGE,
  __module__ = 'execComm_pb2'
  # @@protoc_insertion_point(class_scope:Stage)
  ))
_sym_db.RegisterMessage(Stage)

StatusQuery = _reflection.GeneratedProtocolMessageType('StatusQuery', (_message.Message,), dict(
  DESCRIPTOR = _STATUSQUERY,
  __module__ = 'execComm_pb2'
  # @@protoc_insertion_point(class_scope:StatusQuery)
  ))
_sym_db.RegisterMessage(StatusQuery)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'execComm_pb2'
  # @@protoc_insertion_point(class_scope:Status)
  ))
_sym_db.RegisterMessage(Status)

ExitCall = _reflection.GeneratedProtocolMessageType('ExitCall', (_message.Message,), dict(
  DESCRIPTOR = _EXITCALL,
  __module__ = 'execComm_pb2'
  # @@protoc_insertion_point(class_scope:ExitCall)
  ))
_sym_db.RegisterMessage(ExitCall)

ExitResult = _reflection.GeneratedProtocolMessageType('ExitResult', (_message.Message,), dict(
  DESCRIPTOR = _EXITRESULT,
  __module__ = 'execComm_pb2'
  # @@protoc_insertion_point(class_scope:ExitResult)
  ))
_sym_db.RegisterMessage(ExitResult)



_EXECCOMM = _descriptor.ServiceDescriptor(
  name='ExecComm',
  full_name='ExecComm',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=136,
  serialized_end=257,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetStage',
    full_name='ExecComm.GetStage',
    index=0,
    containing_service=None,
    input_type=_STAGEQUERY,
    output_type=_STAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStatus',
    full_name='ExecComm.GetStatus',
    index=1,
    containing_service=None,
    input_type=_STATUSQUERY,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CallExit',
    full_name='ExecComm.CallExit',
    index=2,
    containing_service=None,
    input_type=_EXITCALL,
    output_type=_EXITRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXECCOMM)

DESCRIPTOR.services_by_name['ExecComm'] = _EXECCOMM

# @@protoc_insertion_point(module_scope)
