# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: booking.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'booking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x12\x07\x62ooking\"\x07\n\x05\x45mpty\"\x18\n\x06UserId\x12\x0e\n\x06userid\x18\x01 \x01(\t\"9\n\x08\x42ookings\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x1d\n\x05\x64\x61tes\x18\x02 \x03(\x0b\x32\x0e.booking.Dates\"%\n\x05\x44\x61tes\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"\x18\n\x05Movie\x12\x0f\n\x07movieid\x18\x01 \x01(\t\"$\n\x12\x41\x64\x64\x42ookingResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xf4\x01\n\x07\x42ooking\x12\x32\n\x0bGetBookings\x12\x0e.booking.Empty\x1a\x11.booking.Bookings0\x01\x12\x39\n\x13GetBookingsByUserId\x12\x0f.booking.UserId\x1a\x11.booking.Bookings\x12\x32\n\x0fGetMoviesByDate\x12\r.booking.Date\x1a\x0e.booking.Dates0\x01\x12\x46\n\x12\x41\x64\x64\x42ookingByUserId\x12\x11.booking.Bookings\x1a\x1b.booking.AddBookingResponse(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=26
  _globals['_EMPTY']._serialized_end=33
  _globals['_USERID']._serialized_start=35
  _globals['_USERID']._serialized_end=59
  _globals['_BOOKINGS']._serialized_start=61
  _globals['_BOOKINGS']._serialized_end=118
  _globals['_DATES']._serialized_start=120
  _globals['_DATES']._serialized_end=157
  _globals['_DATE']._serialized_start=159
  _globals['_DATE']._serialized_end=179
  _globals['_MOVIE']._serialized_start=181
  _globals['_MOVIE']._serialized_end=205
  _globals['_ADDBOOKINGRESPONSE']._serialized_start=207
  _globals['_ADDBOOKINGRESPONSE']._serialized_end=243
  _globals['_BOOKING']._serialized_start=246
  _globals['_BOOKING']._serialized_end=490
# @@protoc_insertion_point(module_scope)
