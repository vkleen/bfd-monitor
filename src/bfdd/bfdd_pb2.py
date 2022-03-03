# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bfdd.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bfdd.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbfdd.proto\x12\x03\x61pi\x1a\x1bgoogle/protobuf/empty.proto\"-\n\x0cStartRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\r\"\r\n\x0bStopRequest\")\n\x0e\x41\x64\x64PeerRequest\x12\x17\n\x04peer\x18\x01 \x01(\x0b\x32\t.api.Peer\"\x1f\n\x0f\x41\x64\x64PeerResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\":\n\x11UpdatePeerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x17\n\x04peer\x18\x02 \x01(\x0b\x32\t.api.Peer\"!\n\x11\x44\x65letePeerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"\x11\n\x0fListPeerRequest\"9\n\x10ListPeerResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x17\n\x04peer\x18\x02 \x01(\x0b\x32\t.api.Peer\"#\n\x13GetPeerStateRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"\"\n\x12MonitorPeerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"R\n\x11PeerStateResponse\x12\x1d\n\x05local\x18\x01 \x01(\x0b\x32\x0e.api.PeerState\x12\x1e\n\x06remote\x18\x02 \x01(\x0b\x32\x0e.api.PeerState\"\"\n\x12\x44isablePeerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"!\n\x11\x45nablePeerRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\"\xc6\x01\n\x04Peer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x1f\n\x17\x64\x65sired_min_tx_interval\x18\x03 \x01(\r\x12 \n\x18required_min_rx_interval\x18\x04 \x01(\r\x12\x19\n\x11\x64\x65tect_multiplier\x18\x05 \x01(\r\x12\x14\n\x0cis_multi_hop\x18\x06 \x01(\x08\x12+\n\x0e\x61uthentication\x18\x07 \x01(\x0b\x32\x13.api.Authentication\"I\n\x0e\x41uthentication\x12%\n\x04type\x18\x01 \x01(\x0e\x32\x17.api.AuthenticationType\x12\x10\n\x08password\x18\x02 \x01(\t\"V\n\tPeerState\x12 \n\x05state\x18\x01 \x01(\x0e\x32\x11.api.SessionState\x12\'\n\ndiagnostic\x18\x02 \x01(\x0e\x32\x13.api.DiagnosticCode*:\n\x0cSessionState\x12\x0e\n\nADMIN_DOWN\x10\x00\x12\x08\n\x04\x44OWN\x10\x01\x12\x08\n\x04INIT\x10\x02\x12\x06\n\x02UP\x10\x03*\x8b\x02\n\x0e\x44iagnosticCode\x12\x11\n\rNO_DIAGNOSTIC\x10\x00\x12\"\n\x1e\x43ONTROL_DETECTION_TIME_EXPIRED\x10\x01\x12\x18\n\x14\x45\x43HO_FUNCTION_FAILED\x10\x02\x12\"\n\x1eNEIGHBOR_SIGNALED_SESSION_DOWN\x10\x03\x12\x1a\n\x16\x46ORWARDING_PLANE_RESET\x10\x04\x12\r\n\tPATH_DOWN\x10\x05\x12\x1a\n\x16\x43ONCATENATED_PATH_DOWN\x10\x06\x12\x19\n\x15\x41\x44MINISTRATIVELY_DOWN\x10\x07\x12\"\n\x1eREVERSE_CONCATENATED_PATH_DOWN\x10\x08*\x87\x01\n\x12\x41uthenticationType\x12\x08\n\x04NONE\x10\x00\x12\x13\n\x0fSIMPLE_PASSWORD\x10\x01\x12\r\n\tKEYED_MD5\x10\x02\x12\x18\n\x14METICULOUS_KEYED_MD5\x10\x03\x12\x0e\n\nKEYED_SHA1\x10\x04\x12\x19\n\x15METICULOUS_KEYED_SHA1\x10\x05\x32\xdd\x04\n\x06\x42\x66\x64\x41pi\x12\x32\n\x05Start\x12\x11.api.StartRequest\x1a\x16.google.protobuf.Empty\x12\x30\n\x04Stop\x12\x10.api.StopRequest\x1a\x16.google.protobuf.Empty\x12\x34\n\x07\x41\x64\x64Peer\x12\x13.api.AddPeerRequest\x1a\x14.api.AddPeerResponse\x12<\n\nUpdatePeer\x12\x16.api.UpdatePeerRequest\x1a\x16.google.protobuf.Empty\x12<\n\nDeletePeer\x12\x16.api.DeletePeerRequest\x1a\x16.google.protobuf.Empty\x12\x39\n\x08ListPeer\x12\x14.api.ListPeerRequest\x1a\x15.api.ListPeerResponse0\x01\x12@\n\x0cGetPeerState\x12\x18.api.GetPeerStateRequest\x1a\x16.api.PeerStateResponse\x12@\n\x0bMonitorPeer\x12\x17.api.MonitorPeerRequest\x1a\x16.api.PeerStateResponse0\x01\x12>\n\x0b\x44isablePeer\x12\x17.api.DisablePeerRequest\x1a\x16.google.protobuf.Empty\x12<\n\nEnablePeer\x12\x16.api.EnablePeerRequest\x1a\x16.google.protobuf.Emptyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_SESSIONSTATE = _descriptor.EnumDescriptor(
  name='SessionState',
  full_name='api.SessionState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADMIN_DOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INIT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=951,
  serialized_end=1009,
)
_sym_db.RegisterEnumDescriptor(_SESSIONSTATE)

SessionState = enum_type_wrapper.EnumTypeWrapper(_SESSIONSTATE)
_DIAGNOSTICCODE = _descriptor.EnumDescriptor(
  name='DiagnosticCode',
  full_name='api.DiagnosticCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_DIAGNOSTIC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONTROL_DETECTION_TIME_EXPIRED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ECHO_FUNCTION_FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEIGHBOR_SIGNALED_SESSION_DOWN', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FORWARDING_PLANE_RESET', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PATH_DOWN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONCATENATED_PATH_DOWN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADMINISTRATIVELY_DOWN', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REVERSE_CONCATENATED_PATH_DOWN', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1012,
  serialized_end=1279,
)
_sym_db.RegisterEnumDescriptor(_DIAGNOSTICCODE)

DiagnosticCode = enum_type_wrapper.EnumTypeWrapper(_DIAGNOSTICCODE)
_AUTHENTICATIONTYPE = _descriptor.EnumDescriptor(
  name='AuthenticationType',
  full_name='api.AuthenticationType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_PASSWORD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYED_MD5', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METICULOUS_KEYED_MD5', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KEYED_SHA1', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METICULOUS_KEYED_SHA1', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1282,
  serialized_end=1417,
)
_sym_db.RegisterEnumDescriptor(_AUTHENTICATIONTYPE)

AuthenticationType = enum_type_wrapper.EnumTypeWrapper(_AUTHENTICATIONTYPE)
ADMIN_DOWN = 0
DOWN = 1
INIT = 2
UP = 3
NO_DIAGNOSTIC = 0
CONTROL_DETECTION_TIME_EXPIRED = 1
ECHO_FUNCTION_FAILED = 2
NEIGHBOR_SIGNALED_SESSION_DOWN = 3
FORWARDING_PLANE_RESET = 4
PATH_DOWN = 5
CONCATENATED_PATH_DOWN = 6
ADMINISTRATIVELY_DOWN = 7
REVERSE_CONCATENATED_PATH_DOWN = 8
NONE = 0
SIMPLE_PASSWORD = 1
KEYED_MD5 = 2
METICULOUS_KEYED_MD5 = 3
KEYED_SHA1 = 4
METICULOUS_KEYED_SHA1 = 5



_STARTREQUEST = _descriptor.Descriptor(
  name='StartRequest',
  full_name='api.StartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='api.StartRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='api.StartRequest.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=48,
  serialized_end=93,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='api.StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=95,
  serialized_end=108,
)


_ADDPEERREQUEST = _descriptor.Descriptor(
  name='AddPeerRequest',
  full_name='api.AddPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='api.AddPeerRequest.peer', index=0,
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
  serialized_start=110,
  serialized_end=151,
)


_ADDPEERRESPONSE = _descriptor.Descriptor(
  name='AddPeerResponse',
  full_name='api.AddPeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.AddPeerResponse.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  ],
  serialized_start=153,
  serialized_end=184,
)


_UPDATEPEERREQUEST = _descriptor.Descriptor(
  name='UpdatePeerRequest',
  full_name='api.UpdatePeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.UpdatePeerRequest.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer', full_name='api.UpdatePeerRequest.peer', index=1,
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
  serialized_start=186,
  serialized_end=244,
)


_DELETEPEERREQUEST = _descriptor.Descriptor(
  name='DeletePeerRequest',
  full_name='api.DeletePeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.DeletePeerRequest.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  ],
  serialized_start=246,
  serialized_end=279,
)


_LISTPEERREQUEST = _descriptor.Descriptor(
  name='ListPeerRequest',
  full_name='api.ListPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=281,
  serialized_end=298,
)


_LISTPEERRESPONSE = _descriptor.Descriptor(
  name='ListPeerResponse',
  full_name='api.ListPeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.ListPeerResponse.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer', full_name='api.ListPeerResponse.peer', index=1,
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
  serialized_start=300,
  serialized_end=357,
)


_GETPEERSTATEREQUEST = _descriptor.Descriptor(
  name='GetPeerStateRequest',
  full_name='api.GetPeerStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.GetPeerStateRequest.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  ],
  serialized_start=359,
  serialized_end=394,
)


_MONITORPEERREQUEST = _descriptor.Descriptor(
  name='MonitorPeerRequest',
  full_name='api.MonitorPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.MonitorPeerRequest.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  ],
  serialized_start=396,
  serialized_end=430,
)


_PEERSTATERESPONSE = _descriptor.Descriptor(
  name='PeerStateResponse',
  full_name='api.PeerStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='local', full_name='api.PeerStateResponse.local', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remote', full_name='api.PeerStateResponse.remote', index=1,
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
  serialized_start=432,
  serialized_end=514,
)


_DISABLEPEERREQUEST = _descriptor.Descriptor(
  name='DisablePeerRequest',
  full_name='api.DisablePeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.DisablePeerRequest.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  ],
  serialized_start=516,
  serialized_end=550,
)


_ENABLEPEERREQUEST = _descriptor.Descriptor(
  name='EnablePeerRequest',
  full_name='api.EnablePeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='api.EnablePeerRequest.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  ],
  serialized_start=552,
  serialized_end=585,
)


_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='api.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.Peer.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='api.Peer.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desired_min_tx_interval', full_name='api.Peer.desired_min_tx_interval', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='required_min_rx_interval', full_name='api.Peer.required_min_rx_interval', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detect_multiplier', full_name='api.Peer.detect_multiplier', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_multi_hop', full_name='api.Peer.is_multi_hop', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authentication', full_name='api.Peer.authentication', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=588,
  serialized_end=786,
)


_AUTHENTICATION = _descriptor.Descriptor(
  name='Authentication',
  full_name='api.Authentication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='api.Authentication.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='api.Authentication.password', index=1,
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
  serialized_start=788,
  serialized_end=861,
)


_PEERSTATE = _descriptor.Descriptor(
  name='PeerState',
  full_name='api.PeerState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='api.PeerState.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='diagnostic', full_name='api.PeerState.diagnostic', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=863,
  serialized_end=949,
)

_ADDPEERREQUEST.fields_by_name['peer'].message_type = _PEER
_UPDATEPEERREQUEST.fields_by_name['peer'].message_type = _PEER
_LISTPEERRESPONSE.fields_by_name['peer'].message_type = _PEER
_PEERSTATERESPONSE.fields_by_name['local'].message_type = _PEERSTATE
_PEERSTATERESPONSE.fields_by_name['remote'].message_type = _PEERSTATE
_PEER.fields_by_name['authentication'].message_type = _AUTHENTICATION
_AUTHENTICATION.fields_by_name['type'].enum_type = _AUTHENTICATIONTYPE
_PEERSTATE.fields_by_name['state'].enum_type = _SESSIONSTATE
_PEERSTATE.fields_by_name['diagnostic'].enum_type = _DIAGNOSTICCODE
DESCRIPTOR.message_types_by_name['StartRequest'] = _STARTREQUEST
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['AddPeerRequest'] = _ADDPEERREQUEST
DESCRIPTOR.message_types_by_name['AddPeerResponse'] = _ADDPEERRESPONSE
DESCRIPTOR.message_types_by_name['UpdatePeerRequest'] = _UPDATEPEERREQUEST
DESCRIPTOR.message_types_by_name['DeletePeerRequest'] = _DELETEPEERREQUEST
DESCRIPTOR.message_types_by_name['ListPeerRequest'] = _LISTPEERREQUEST
DESCRIPTOR.message_types_by_name['ListPeerResponse'] = _LISTPEERRESPONSE
DESCRIPTOR.message_types_by_name['GetPeerStateRequest'] = _GETPEERSTATEREQUEST
DESCRIPTOR.message_types_by_name['MonitorPeerRequest'] = _MONITORPEERREQUEST
DESCRIPTOR.message_types_by_name['PeerStateResponse'] = _PEERSTATERESPONSE
DESCRIPTOR.message_types_by_name['DisablePeerRequest'] = _DISABLEPEERREQUEST
DESCRIPTOR.message_types_by_name['EnablePeerRequest'] = _ENABLEPEERREQUEST
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
DESCRIPTOR.message_types_by_name['Authentication'] = _AUTHENTICATION
DESCRIPTOR.message_types_by_name['PeerState'] = _PEERSTATE
DESCRIPTOR.enum_types_by_name['SessionState'] = _SESSIONSTATE
DESCRIPTOR.enum_types_by_name['DiagnosticCode'] = _DIAGNOSTICCODE
DESCRIPTOR.enum_types_by_name['AuthenticationType'] = _AUTHENTICATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.StartRequest)
  })
_sym_db.RegisterMessage(StartRequest)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOPREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.StopRequest)
  })
_sym_db.RegisterMessage(StopRequest)

AddPeerRequest = _reflection.GeneratedProtocolMessageType('AddPeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDPEERREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.AddPeerRequest)
  })
_sym_db.RegisterMessage(AddPeerRequest)

AddPeerResponse = _reflection.GeneratedProtocolMessageType('AddPeerResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDPEERRESPONSE,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.AddPeerResponse)
  })
_sym_db.RegisterMessage(AddPeerResponse)

UpdatePeerRequest = _reflection.GeneratedProtocolMessageType('UpdatePeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPEERREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdatePeerRequest)
  })
_sym_db.RegisterMessage(UpdatePeerRequest)

DeletePeerRequest = _reflection.GeneratedProtocolMessageType('DeletePeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPEERREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.DeletePeerRequest)
  })
_sym_db.RegisterMessage(DeletePeerRequest)

ListPeerRequest = _reflection.GeneratedProtocolMessageType('ListPeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPEERREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.ListPeerRequest)
  })
_sym_db.RegisterMessage(ListPeerRequest)

ListPeerResponse = _reflection.GeneratedProtocolMessageType('ListPeerResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPEERRESPONSE,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.ListPeerResponse)
  })
_sym_db.RegisterMessage(ListPeerResponse)

GetPeerStateRequest = _reflection.GeneratedProtocolMessageType('GetPeerStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPEERSTATEREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.GetPeerStateRequest)
  })
_sym_db.RegisterMessage(GetPeerStateRequest)

MonitorPeerRequest = _reflection.GeneratedProtocolMessageType('MonitorPeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _MONITORPEERREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.MonitorPeerRequest)
  })
_sym_db.RegisterMessage(MonitorPeerRequest)

PeerStateResponse = _reflection.GeneratedProtocolMessageType('PeerStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEERSTATERESPONSE,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.PeerStateResponse)
  })
_sym_db.RegisterMessage(PeerStateResponse)

DisablePeerRequest = _reflection.GeneratedProtocolMessageType('DisablePeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DISABLEPEERREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.DisablePeerRequest)
  })
_sym_db.RegisterMessage(DisablePeerRequest)

EnablePeerRequest = _reflection.GeneratedProtocolMessageType('EnablePeerRequest', (_message.Message,), {
  'DESCRIPTOR' : _ENABLEPEERREQUEST,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.EnablePeerRequest)
  })
_sym_db.RegisterMessage(EnablePeerRequest)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), {
  'DESCRIPTOR' : _PEER,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.Peer)
  })
_sym_db.RegisterMessage(Peer)

Authentication = _reflection.GeneratedProtocolMessageType('Authentication', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATION,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.Authentication)
  })
_sym_db.RegisterMessage(Authentication)

PeerState = _reflection.GeneratedProtocolMessageType('PeerState', (_message.Message,), {
  'DESCRIPTOR' : _PEERSTATE,
  '__module__' : 'bfdd_pb2'
  # @@protoc_insertion_point(class_scope:api.PeerState)
  })
_sym_db.RegisterMessage(PeerState)



_BFDAPI = _descriptor.ServiceDescriptor(
  name='BfdApi',
  full_name='api.BfdApi',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1420,
  serialized_end=2025,
  methods=[
  _descriptor.MethodDescriptor(
    name='Start',
    full_name='api.BfdApi.Start',
    index=0,
    containing_service=None,
    input_type=_STARTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Stop',
    full_name='api.BfdApi.Stop',
    index=1,
    containing_service=None,
    input_type=_STOPREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddPeer',
    full_name='api.BfdApi.AddPeer',
    index=2,
    containing_service=None,
    input_type=_ADDPEERREQUEST,
    output_type=_ADDPEERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdatePeer',
    full_name='api.BfdApi.UpdatePeer',
    index=3,
    containing_service=None,
    input_type=_UPDATEPEERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeletePeer',
    full_name='api.BfdApi.DeletePeer',
    index=4,
    containing_service=None,
    input_type=_DELETEPEERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListPeer',
    full_name='api.BfdApi.ListPeer',
    index=5,
    containing_service=None,
    input_type=_LISTPEERREQUEST,
    output_type=_LISTPEERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPeerState',
    full_name='api.BfdApi.GetPeerState',
    index=6,
    containing_service=None,
    input_type=_GETPEERSTATEREQUEST,
    output_type=_PEERSTATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MonitorPeer',
    full_name='api.BfdApi.MonitorPeer',
    index=7,
    containing_service=None,
    input_type=_MONITORPEERREQUEST,
    output_type=_PEERSTATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DisablePeer',
    full_name='api.BfdApi.DisablePeer',
    index=8,
    containing_service=None,
    input_type=_DISABLEPEERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EnablePeer',
    full_name='api.BfdApi.EnablePeer',
    index=9,
    containing_service=None,
    input_type=_ENABLEPEERREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BFDAPI)

DESCRIPTOR.services_by_name['BfdApi'] = _BFDAPI

# @@protoc_insertion_point(module_scope)
