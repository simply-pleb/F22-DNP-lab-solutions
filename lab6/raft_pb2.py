# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"\x0e\n\x0c\x45mptyMessage\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"2\n\x0bPeerMessage\x12\x12\n\ntermNumber\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"4\n\x0fMessageResponse\x12\x10\n\x08received\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xbd\x01\n\x06Server\x12-\n\x0bRequestVote\x12\x0c.PeerMessage\x1a\x10.MessageResponse\x12/\n\rAppendEntries\x12\x0c.PeerMessage\x1a\x10.MessageResponse\x12,\n\tGetLeader\x12\r.EmptyMessage\x1a\x10.MessageResponse\x12%\n\x07Suspend\x12\x08.Message\x1a\x10.MessageResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYMESSAGE._serialized_start=14
  _EMPTYMESSAGE._serialized_end=28
  _MESSAGE._serialized_start=30
  _MESSAGE._serialized_end=56
  _PEERMESSAGE._serialized_start=58
  _PEERMESSAGE._serialized_end=108
  _MESSAGERESPONSE._serialized_start=110
  _MESSAGERESPONSE._serialized_end=162
  _SERVER._serialized_start=165
  _SERVER._serialized_end=354
# @@protoc_insertion_point(module_scope)
