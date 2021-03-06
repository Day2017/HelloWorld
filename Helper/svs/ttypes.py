#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING!!!
#
#  options string: py
#
from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
import sys
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None

class LoginResultType(object):
  """
  **line.thrift****

  | Author : GoogleX & Tanysyz
  |
  | Copyright (c) 2018

  """  
  SUCCESS = 1
  REQUIRE_QRCODE = 2
  REQUIRE_DEVICE_CONFIRM = 3
  REQUIRE_SMS_CONFIRM = 4

  _VALUES_TO_NAMES = {
    1: "SUCCESS",
    2: "REQUIRE_QRCODE",
    3: "REQUIRE_DEVICE_CONFIRM",
    4: "REQUIRE_SMS_CONFIRM",
  }

  _NAMES_TO_VALUES = {
    "SUCCESS": 1,
    "REQUIRE_QRCODE": 2,
    "REQUIRE_DEVICE_CONFIRM": 3,
    "REQUIRE_SMS_CONFIRM": 4,
  }

class IdentityProvider(object):
  UNKNOWN = 0
  LINE = 1
  NAVER_KR = 2
  LINE_PHONE = 3

  _VALUES_TO_NAMES = {
    0: "UNKNOWN",
    1: "LINE",
    2: "NAVER_KR",
    3: "LINE_PHONE",
  }

  _NAMES_TO_VALUES = {
    "UNKNOWN": 0,
    "LINE": 1,
    "NAVER_KR": 2,
    "LINE_PHONE": 3,
  }

class ErrorCode(object):
  ILLEGAL_ARGUMENT = 0
  AUTHENTICATION_FAILED = 1
  DB_FAILED = 2
  INVALID_STATE = 3
  EXCESSIVE_ACCESS = 4
  NOT_FOUND = 5
  INVALID_MID = 9
  NOT_A_MEMBER = 10
  INVALID_LENGTH = 6
  NOT_AVAILABLE_USER = 7
  NOT_AUTHORIZED_DEVICE = 8
  NOT_AUTHORIZED_SESSION = 14
  INCOMPATIBLE_APP_VERSION = 11
  NOT_READY = 12
  NOT_AVAILABLE_SESSION = 13
  SYSTEM_ERROR = 15
  NO_AVAILABLE_VERIFICATION_METHOD = 16
  NOT_AUTHENTICATED = 17
  INVALID_IDENTITY_CREDENTIAL = 18
  NOT_AVAILABLE_IDENTITY_IDENTIFIER = 19
  INTERNAL_ERROR = 20
  NO_SUCH_IDENTITY_IDENFIER = 21
  DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY = 22
  ILLEGAL_IDENTITY_CREDENTIAL = 23
  UNKNOWN_CHANNEL = 24
  NO_SUCH_MESSAGE_BOX = 25
  NOT_AVAILABLE_MESSAGE_BOX = 26
  CHANNEL_DOES_NOT_MATCH = 27
  NOT_YOUR_MESSAGE = 28
  MESSAGE_DEFINED_ERROR = 29
  USER_CANNOT_ACCEPT_PRESENTS = 30
  USER_NOT_STICKER_OWNER = 32
  MAINTENANCE_ERROR = 33
  ACCOUNT_NOT_MATCHED = 34
  ABUSE_BLOCK = 35
  NOT_FRIEND = 36
  NOT_ALLOWED_CALL = 37
  BLOCK_FRIEND = 38
  INCOMPATIBLE_VOIP_VERSION = 39
  INVALID_SNS_ACCESS_TOKEN = 40
  EXTERNAL_SERVICE_NOT_AVAILABLE = 41
  NOT_ALLOWED_ADD_CONTACT = 42
  NOT_CERTIFICATED = 43
  NOT_ALLOWED_SECONDARY_DEVICE = 44
  INVALID_PIN_CODE = 45
  NOT_FOUND_IDENTITY_CREDENTIAL = 46
  EXCEED_FILE_MAX_SIZE = 47
  EXCEED_DAILY_QUOTA = 48
  NOT_SUPPORT_SEND_FILE = 49
  MUST_UPGRADE = 50
  NOT_AVAILABLE_PIN_CODE_SESSION = 51
  EXPIRED_REVISION = 52
  NOT_YET_PHONE_NUMBER = 54
  BAD_CALL_NUMBER = 55
  UNAVAILABLE_CALL_NUMBER = 56
  NOT_SUPPORT_CALL_SERVICE = 57
  CONGESTION_CONTROL = 58
  NO_BALANCE = 59
  NOT_PERMITTED_CALLER_ID = 60
  NO_CALLER_ID_LIMIT_EXCEEDED = 61
  CALLER_ID_VERIFICATION_REQUIRED = 62
  NO_CALLER_ID_LIMIT_EXCEEDED_AND_VERIFICATION_REQUIRED = 63
  MESSAGE_NOT_FOUND = 64
  INVALID_ACCOUNT_MIGRATION_PINCODE_FORMAT = 65
  ACCOUNT_MIGRATION_PINCODE_NOT_MATCHED = 66
  ACCOUNT_MIGRATION_PINCODE_BLOCKED = 67
  INVALID_PASSWORD_FORMAT = 69
  FEATURE_RESTRICTED = 70
  MESSAGE_NOT_DESTRUCTIBLE = 71
  PAID_CALL_REDEEM_FAILED = 72
  PREVENTED_JOIN_BY_TICKET = 73
  SEND_MESSAGE_NOT_PERMITTED_FROM_LINE_AT = 75
  SEND_MESSAGE_NOT_PERMITTED_WHILE_AUTO_REPLY = 76
  SECURITY_CENTER_NOT_VERIFIED = 77
  SECURITY_CENTER_BLOCKED_BY_SETTING = 78
  SECURITY_CENTER_BLOCKED = 79
  TALK_PROXY_EXCEPTION = 80
  E2EE_INVALID_PROTOCOL = 81
  E2EE_RETRY_ENCRYPT = 82
  E2EE_UPDATE_SENDER_KEY = 83
  E2EE_UPDATE_RECEIVER_KEY = 84
  E2EE_INVALID_ARGUMENT = 85
  E2EE_INVALID_VERSION = 86
  E2EE_SENDER_DISABLED = 87
  E2EE_RECEIVER_DISABLED = 88
  E2EE_SENDER_NOT_ALLOWED = 89
  E2EE_RECEIVER_NOT_ALLOWED = 90
  E2EE_RESEND_FAIL = 91
  E2EE_RESEND_OK = 92
  HITOKOTO_BACKUP_NO_AVAILABLE_DATA = 93
  E2EE_UPDATE_PRIMARY_DEVICE = 94
  SUCCESS = 95
  CANCEL = 96
  E2EE_PRIMARY_NOT_SUPPORT = 97
  E2EE_RETRY_PLAIN = 98
  E2EE_RECREATE_GROUP_KEY = 99
  E2EE_GROUP_TOO_MANY_MEMBERS = 100
  SERVER_BUSY = 101
  NOT_ALLOWED_ADD_FOLLOW = 102
  INCOMING_FRIEND_REQUEST_LIMIT = 103
  OUTGOING_FRIEND_REQUEST_LIMIT = 104
  OUTGOING_FRIEND_REQUEST_QUOTA = 105
  DUPLICATED = 106
  BANNED = 107

  _VALUES_TO_NAMES = {
    0: "ILLEGAL_ARGUMENT",
    1: "AUTHENTICATION_FAILED",
    2: "DB_FAILED",
    3: "INVALID_STATE",
    4: "EXCESSIVE_ACCESS",
    5: "NOT_FOUND",
    9: "INVALID_MID",
    10: "NOT_A_MEMBER",
    6: "INVALID_LENGTH",
    7: "NOT_AVAILABLE_USER",
    8: "NOT_AUTHORIZED_DEVICE",
    14: "NOT_AUTHORIZED_SESSION",
    11: "INCOMPATIBLE_APP_VERSION",
    12: "NOT_READY",
    13: "NOT_AVAILABLE_SESSION",
    15: "SYSTEM_ERROR",
    16: "NO_AVAILABLE_VERIFICATION_METHOD",
    17: "NOT_AUTHENTICATED",
    18: "INVALID_IDENTITY_CREDENTIAL",
    19: "NOT_AVAILABLE_IDENTITY_IDENTIFIER",
    20: "INTERNAL_ERROR",
    21: "NO_SUCH_IDENTITY_IDENFIER",
    22: "DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY",
    23: "ILLEGAL_IDENTITY_CREDENTIAL",
    24: "UNKNOWN_CHANNEL",
    25: "NO_SUCH_MESSAGE_BOX",
    26: "NOT_AVAILABLE_MESSAGE_BOX",
    27: "CHANNEL_DOES_NOT_MATCH",
    28: "NOT_YOUR_MESSAGE",
    29: "MESSAGE_DEFINED_ERROR",
    30: "USER_CANNOT_ACCEPT_PRESENTS",
    32: "USER_NOT_STICKER_OWNER",
    33: "MAINTENANCE_ERROR",
    34: "ACCOUNT_NOT_MATCHED",
    35: "ABUSE_BLOCK",
    36: "NOT_FRIEND",
    37: "NOT_ALLOWED_CALL",
    38: "BLOCK_FRIEND",
    39: "INCOMPATIBLE_VOIP_VERSION",
    40: "INVALID_SNS_ACCESS_TOKEN",
    41: "EXTERNAL_SERVICE_NOT_AVAILABLE",
    42: "NOT_ALLOWED_ADD_CONTACT",
    43: "NOT_CERTIFICATED",
    44: "NOT_ALLOWED_SECONDARY_DEVICE",
    45: "INVALID_PIN_CODE",
    46: "NOT_FOUND_IDENTITY_CREDENTIAL",
    47: "EXCEED_FILE_MAX_SIZE",
    48: "EXCEED_DAILY_QUOTA",
    49: "NOT_SUPPORT_SEND_FILE",
    50: "MUST_UPGRADE",
    51: "NOT_AVAILABLE_PIN_CODE_SESSION",
    52: "EXPIRED_REVISION",
    54: "NOT_YET_PHONE_NUMBER",
    55: "BAD_CALL_NUMBER",
    56: "UNAVAILABLE_CALL_NUMBER",
    57: "NOT_SUPPORT_CALL_SERVICE",
    58: "CONGESTION_CONTROL",
    59: "NO_BALANCE",
    60: "NOT_PERMITTED_CALLER_ID",
    61: "NO_CALLER_ID_LIMIT_EXCEEDED",
    62: "CALLER_ID_VERIFICATION_REQUIRED",
    63: "NO_CALLER_ID_LIMIT_EXCEEDED_AND_VERIFICATION_REQUIRED",
    64: "MESSAGE_NOT_FOUND",
    65: "INVALID_ACCOUNT_MIGRATION_PINCODE_FORMAT",
    66: "ACCOUNT_MIGRATION_PINCODE_NOT_MATCHED",
    67: "ACCOUNT_MIGRATION_PINCODE_BLOCKED",
    69: "INVALID_PASSWORD_FORMAT",
    70: "FEATURE_RESTRICTED",
    71: "MESSAGE_NOT_DESTRUCTIBLE",
    72: "PAID_CALL_REDEEM_FAILED",
    73: "PREVENTED_JOIN_BY_TICKET",
    75: "SEND_MESSAGE_NOT_PERMITTED_FROM_LINE_AT",
    76: "SEND_MESSAGE_NOT_PERMITTED_WHILE_AUTO_REPLY",
    77: "SECURITY_CENTER_NOT_VERIFIED",
    78: "SECURITY_CENTER_BLOCKED_BY_SETTING",
    79: "SECURITY_CENTER_BLOCKED",
    80: "TALK_PROXY_EXCEPTION",
    81: "E2EE_INVALID_PROTOCOL",
    82: "E2EE_RETRY_ENCRYPT",
    83: "E2EE_UPDATE_SENDER_KEY",
    84: "E2EE_UPDATE_RECEIVER_KEY",
    85: "E2EE_INVALID_ARGUMENT",
    86: "E2EE_INVALID_VERSION",
    87: "E2EE_SENDER_DISABLED",
    88: "E2EE_RECEIVER_DISABLED",
    89: "E2EE_SENDER_NOT_ALLOWED",
    90: "E2EE_RECEIVER_NOT_ALLOWED",
    91: "E2EE_RESEND_FAIL",
    92: "E2EE_RESEND_OK",
    93: "HITOKOTO_BACKUP_NO_AVAILABLE_DATA",
    94: "E2EE_UPDATE_PRIMARY_DEVICE",
    95: "SUCCESS",
    96: "CANCEL",
    97: "E2EE_PRIMARY_NOT_SUPPORT",
    98: "E2EE_RETRY_PLAIN",
    99: "E2EE_RECREATE_GROUP_KEY",
    100: "E2EE_GROUP_TOO_MANY_MEMBERS",
    101: "SERVER_BUSY",
    102: "NOT_ALLOWED_ADD_FOLLOW",
    103: "INCOMING_FRIEND_REQUEST_LIMIT",
    104: "OUTGOING_FRIEND_REQUEST_LIMIT",
    105: "OUTGOING_FRIEND_REQUEST_QUOTA",
    106: "DUPLICATED",
    107: "BANNED",
  }

  _NAMES_TO_VALUES = {
    "ILLEGAL_ARGUMENT": 0,
    "AUTHENTICATION_FAILED": 1,
    "DB_FAILED": 2,
    "INVALID_STATE": 3,
    "EXCESSIVE_ACCESS": 4,
    "NOT_FOUND": 5,
    "INVALID_MID": 9,
    "NOT_A_MEMBER": 10,
    "INVALID_LENGTH": 6,
    "NOT_AVAILABLE_USER": 7,
    "NOT_AUTHORIZED_DEVICE": 8,
    "NOT_AUTHORIZED_SESSION": 14,
    "INCOMPATIBLE_APP_VERSION": 11,
    "NOT_READY": 12,
    "NOT_AVAILABLE_SESSION": 13,
    "SYSTEM_ERROR": 15,
    "NO_AVAILABLE_VERIFICATION_METHOD": 16,
    "NOT_AUTHENTICATED": 17,
    "INVALID_IDENTITY_CREDENTIAL": 18,
    "NOT_AVAILABLE_IDENTITY_IDENTIFIER": 19,
    "INTERNAL_ERROR": 20,
    "NO_SUCH_IDENTITY_IDENFIER": 21,
    "DEACTIVATED_ACCOUNT_BOUND_TO_THIS_IDENTITY": 22,
    "ILLEGAL_IDENTITY_CREDENTIAL": 23,
    "UNKNOWN_CHANNEL": 24,
    "NO_SUCH_MESSAGE_BOX": 25,
    "NOT_AVAILABLE_MESSAGE_BOX": 26,
    "CHANNEL_DOES_NOT_MATCH": 27,
    "NOT_YOUR_MESSAGE": 28,
    "MESSAGE_DEFINED_ERROR": 29,
    "USER_CANNOT_ACCEPT_PRESENTS": 30,
    "USER_NOT_STICKER_OWNER": 32,
    "MAINTENANCE_ERROR": 33,
    "ACCOUNT_NOT_MATCHED": 34,
    "ABUSE_BLOCK": 35,
    "NOT_FRIEND": 36,
    "NOT_ALLOWED_CALL": 37,
    "BLOCK_FRIEND": 38,
    "INCOMPATIBLE_VOIP_VERSION": 39,
    "INVALID_SNS_ACCESS_TOKEN": 40,
    "EXTERNAL_SERVICE_NOT_AVAILABLE": 41,
    "NOT_ALLOWED_ADD_CONTACT": 42,
    "NOT_CERTIFICATED": 43,
    "NOT_ALLOWED_SECONDARY_DEVICE": 44,
    "INVALID_PIN_CODE": 45,
    "NOT_FOUND_IDENTITY_CREDENTIAL": 46,
    "EXCEED_FILE_MAX_SIZE": 47,
    "EXCEED_DAILY_QUOTA": 48,
    "NOT_SUPPORT_SEND_FILE": 49,
    "MUST_UPGRADE": 50,
    "NOT_AVAILABLE_PIN_CODE_SESSION": 51,
    "EXPIRED_REVISION": 52,
    "NOT_YET_PHONE_NUMBER": 54,
    "BAD_CALL_NUMBER": 55,
    "UNAVAILABLE_CALL_NUMBER": 56,
    "NOT_SUPPORT_CALL_SERVICE": 57,
    "CONGESTION_CONTROL": 58,
    "NO_BALANCE": 59,
    "NOT_PERMITTED_CALLER_ID": 60,
    "NO_CALLER_ID_LIMIT_EXCEEDED": 61,
    "CALLER_ID_VERIFICATION_REQUIRED": 62,
    "NO_CALLER_ID_LIMIT_EXCEEDED_AND_VERIFICATION_REQUIRED": 63,
    "MESSAGE_NOT_FOUND": 64,
    "INVALID_ACCOUNT_MIGRATION_PINCODE_FORMAT": 65,
    "ACCOUNT_MIGRATION_PINCODE_NOT_MATCHED": 66,
    "ACCOUNT_MIGRATION_PINCODE_BLOCKED": 67,
    "INVALID_PASSWORD_FORMAT": 69,
    "FEATURE_RESTRICTED": 70,
    "MESSAGE_NOT_DESTRUCTIBLE": 71,
    "PAID_CALL_REDEEM_FAILED": 72,
    "PREVENTED_JOIN_BY_TICKET": 73,
    "SEND_MESSAGE_NOT_PERMITTED_FROM_LINE_AT": 75,
    "SEND_MESSAGE_NOT_PERMITTED_WHILE_AUTO_REPLY": 76,
    "SECURITY_CENTER_NOT_VERIFIED": 77,
    "SECURITY_CENTER_BLOCKED_BY_SETTING": 78,
    "SECURITY_CENTER_BLOCKED": 79,
    "TALK_PROXY_EXCEPTION": 80,
    "E2EE_INVALID_PROTOCOL": 81,
    "E2EE_RETRY_ENCRYPT": 82,
    "E2EE_UPDATE_SENDER_KEY": 83,
    "E2EE_UPDATE_RECEIVER_KEY": 84,
    "E2EE_INVALID_ARGUMENT": 85,
    "E2EE_INVALID_VERSION": 86,
    "E2EE_SENDER_DISABLED": 87,
    "E2EE_RECEIVER_DISABLED": 88,
    "E2EE_SENDER_NOT_ALLOWED": 89,
    "E2EE_RECEIVER_NOT_ALLOWED": 90,
    "E2EE_RESEND_FAIL": 91,
    "E2EE_RESEND_OK": 92,
    "HITOKOTO_BACKUP_NO_AVAILABLE_DATA": 93,
    "E2EE_UPDATE_PRIMARY_DEVICE": 94,
    "SUCCESS": 95,
    "CANCEL": 96,
    "E2EE_PRIMARY_NOT_SUPPORT": 97,
    "E2EE_RETRY_PLAIN": 98,
    "E2EE_RECREATE_GROUP_KEY": 99,
    "E2EE_GROUP_TOO_MANY_MEMBERS": 100,
    "SERVER_BUSY": 101,
    "NOT_ALLOWED_ADD_FOLLOW": 102,
    "INCOMING_FRIEND_REQUEST_LIMIT": 103,
    "OUTGOING_FRIEND_REQUEST_LIMIT": 104,
    "OUTGOING_FRIEND_REQUEST_QUOTA": 105,
    "DUPLICATED": 106,
    "BANNED": 107,
  }

class VerificationMethod(object):
  NO_AVAILABLE = 0
  PIN_VIA_SMS = 1
  CALLERID_INDIGO = 2
  PIN_VIA_TTS = 4
  SKIP = 10

  _VALUES_TO_NAMES = {
    0: "NO_AVAILABLE",
    1: "PIN_VIA_SMS",
    2: "CALLERID_INDIGO",
    4: "PIN_VIA_TTS",
    10: "SKIP",
  }

  _NAMES_TO_VALUES = {
    "NO_AVAILABLE": 0,
    "PIN_VIA_SMS": 1,
    "CALLERID_INDIGO": 2,
    "PIN_VIA_TTS": 4,
    "SKIP": 10,
  }

class TalkException(TException):
  """
  Attributes:
   - code
   - reason
   - parameterMap
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'code', None, None, ), # 1
    (2, TType.STRING, 'reason', None, None, ), # 2
    (3, TType.MAP, 'parameterMap', (TType.STRING,None,TType.STRING,None), None, ), # 3
  )

  def __init__(self, code=None, reason=None, parameterMap=None,):
    self.code = code
    self.reason = reason
    self.parameterMap = parameterMap

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.code = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.reason = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.parameterMap = {}
          (_ktype912, _vtype913, _size911 ) = iprot.readMapBegin()
          for _i915 in xrange(_size911):
            _key916 = iprot.readString()
            _val917 = iprot.readString()
            self.parameterMap[_key916] = _val917
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TalkException')
    if self.code is not None:
      oprot.writeFieldBegin('code', TType.I32, 1)
      oprot.writeI32(self.code)
      oprot.writeFieldEnd()
    if self.reason is not None:
      oprot.writeFieldBegin('reason', TType.STRING, 2)
      oprot.writeString(self.reason)
      oprot.writeFieldEnd()
    if self.parameterMap is not None:
      oprot.writeFieldBegin('parameterMap', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.parameterMap))
      for kiter918,viter919 in self.parameterMap.items():
        oprot.writeString(kiter918)
        oprot.writeString(viter919)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.code)
    value = (value * 31) ^ hash(self.reason)
    value = (value * 31) ^ hash(self.parameterMap)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class VerificationSessionData(object):
  """
  Attributes:
   - sessionId
   - method
   - callback
   - normalizedPhone
   - countryCode
   - nationalSignificantNumber
   - availableVerificationMethods
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'sessionId', None, None, ), # 1
    (2, TType.I32, 'method', None, None, ), # 2
    (3, TType.STRING, 'callback', None, None, ), # 3
    (4, TType.STRING, 'normalizedPhone', None, None, ), # 4
    (5, TType.STRING, 'countryCode', None, None, ), # 5
    (6, TType.STRING, 'nationalSignificantNumber', None, None, ), # 6
    (7, TType.LIST, 'availableVerificationMethods', (TType.I32,None), None, ), # 7
  )

  def __init__(self, sessionId=None, method=None, callback=None, normalizedPhone=None, countryCode=None, nationalSignificantNumber=None, availableVerificationMethods=None,):
    self.sessionId = sessionId
    self.method = method
    self.callback = callback
    self.normalizedPhone = normalizedPhone
    self.countryCode = countryCode
    self.nationalSignificantNumber = nationalSignificantNumber
    self.availableVerificationMethods = availableVerificationMethods

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.sessionId = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.method = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.callback = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.normalizedPhone = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.countryCode = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.nationalSignificantNumber = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.availableVerificationMethods = []
          (_etype272, _size269) = iprot.readListBegin()
          for _i273 in xrange(_size269):
            _elem274 = iprot.readI32()
            self.availableVerificationMethods.append(_elem274)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('VerificationSessionData')
    if self.sessionId is not None:
      oprot.writeFieldBegin('sessionId', TType.STRING, 1)
      oprot.writeString(self.sessionId)
      oprot.writeFieldEnd()
    if self.method is not None:
      oprot.writeFieldBegin('method', TType.I32, 2)
      oprot.writeI32(self.method)
      oprot.writeFieldEnd()
    if self.callback is not None:
      oprot.writeFieldBegin('callback', TType.STRING, 3)
      oprot.writeString(self.callback)
      oprot.writeFieldEnd()
    if self.normalizedPhone is not None:
      oprot.writeFieldBegin('normalizedPhone', TType.STRING, 4)
      oprot.writeString(self.normalizedPhone)
      oprot.writeFieldEnd()
    if self.countryCode is not None:
      oprot.writeFieldBegin('countryCode', TType.STRING, 5)
      oprot.writeString(self.countryCode)
      oprot.writeFieldEnd()
    if self.nationalSignificantNumber is not None:
      oprot.writeFieldBegin('nationalSignificantNumber', TType.STRING, 6)
      oprot.writeString(self.nationalSignificantNumber)
      oprot.writeFieldEnd()
    if self.availableVerificationMethods is not None:
      oprot.writeFieldBegin('availableVerificationMethods', TType.LIST, 7)
      oprot.writeListBegin(TType.I32, len(self.availableVerificationMethods))
      for iter275 in self.availableVerificationMethods:
        oprot.writeI32(iter275)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.sessionId)
    value = (value * 31) ^ hash(self.method)
    value = (value * 31) ^ hash(self.callback)
    value = (value * 31) ^ hash(self.normalizedPhone)
    value = (value * 31) ^ hash(self.countryCode)
    value = (value * 31) ^ hash(self.nationalSignificantNumber)
    value = (value * 31) ^ hash(self.availableVerificationMethods)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LoginResult(object):
  """
  Attributes:
   - authToken
   - certificate
   - verifier
   - pinCode
   - type
   - lastPrimaryBindTime
   - displayMessage
   - sessionForSMSConfirm
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'authToken', None, None, ), # 1
    (2, TType.STRING, 'certificate', None, None, ), # 2
    (3, TType.STRING, 'verifier', None, None, ), # 3
    (4, TType.STRING, 'pinCode', None, None, ), # 4
    (5, TType.I32, 'type', None, None, ), # 5
    (6, TType.I64, 'lastPrimaryBindTime', None, None, ), # 6
    (7, TType.STRING, 'displayMessage', None, None, ), # 7
    (8, TType.STRUCT, 'sessionForSMSConfirm', (VerificationSessionData, VerificationSessionData.thrift_spec), None, ), # 8
  )

  def __init__(self, authToken=None, certificate=None, verifier=None, pinCode=None, type=None, lastPrimaryBindTime=None, displayMessage=None, sessionForSMSConfirm=None,):
    self.authToken = authToken
    self.certificate = certificate
    self.verifier = verifier
    self.pinCode = pinCode
    self.type = type
    self.lastPrimaryBindTime = lastPrimaryBindTime
    self.displayMessage = displayMessage
    self.sessionForSMSConfirm = sessionForSMSConfirm

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.authToken = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.certificate = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.verifier = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.pinCode = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.type = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.lastPrimaryBindTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.displayMessage = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRUCT:
          self.sessionForSMSConfirm = VerificationSessionData()
          self.sessionForSMSConfirm.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LoginResult')
    if self.authToken is not None:
      oprot.writeFieldBegin('authToken', TType.STRING, 1)
      oprot.writeString(self.authToken)
      oprot.writeFieldEnd()
    if self.certificate is not None:
      oprot.writeFieldBegin('certificate', TType.STRING, 2)
      oprot.writeString(self.certificate)
      oprot.writeFieldEnd()
    if self.verifier is not None:
      oprot.writeFieldBegin('verifier', TType.STRING, 3)
      oprot.writeString(self.verifier)
      oprot.writeFieldEnd()
    if self.pinCode is not None:
      oprot.writeFieldBegin('pinCode', TType.STRING, 4)
      oprot.writeString(self.pinCode)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 5)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.lastPrimaryBindTime is not None:
      oprot.writeFieldBegin('lastPrimaryBindTime', TType.I64, 6)
      oprot.writeI64(self.lastPrimaryBindTime)
      oprot.writeFieldEnd()
    if self.displayMessage is not None:
      oprot.writeFieldBegin('displayMessage', TType.STRING, 7)
      oprot.writeString(self.displayMessage)
      oprot.writeFieldEnd()
    if self.sessionForSMSConfirm is not None:
      oprot.writeFieldBegin('sessionForSMSConfirm', TType.STRUCT, 8)
      self.sessionForSMSConfirm.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.authToken)
    value = (value * 31) ^ hash(self.certificate)
    value = (value * 31) ^ hash(self.verifier)
    value = (value * 31) ^ hash(self.pinCode)
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.lastPrimaryBindTime)
    value = (value * 31) ^ hash(self.displayMessage)
    value = (value * 31) ^ hash(self.sessionForSMSConfirm)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class LoginRequest(object):
  """
  Attributes:
   - type
   - identityProvider
   - identifier
   - password
   - keepLoggedIn
   - accessLocation
   - systemName
   - certificate
   - verifier
   - secret
   - e2eeVersion
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.I32, 'identityProvider', None, None, ), # 2
    (3, TType.STRING, 'identifier', None, None, ), # 3
    (4, TType.STRING, 'password', None, None, ), # 4
    (5, TType.BOOL, 'keepLoggedIn', None, None, ), # 5
    (6, TType.STRING, 'accessLocation', None, None, ), # 6
    (7, TType.STRING, 'systemName', None, None, ), # 7
    (8, TType.STRING, 'certificate', None, None, ), # 8
    (9, TType.STRING, 'verifier', None, None, ), # 9
    (10, TType.STRING, 'secret', None, None, ), # 10
    (11, TType.I32, 'e2eeVersion', None, None, ), # 11
  )

  def __init__(self, type=None, identityProvider=None, identifier=None, password=None, keepLoggedIn=None, accessLocation=None, systemName=None, certificate=None, verifier=None, secret=None, e2eeVersion=None,):
    self.type = type
    self.identityProvider = identityProvider
    self.identifier = identifier
    self.password = password
    self.keepLoggedIn = keepLoggedIn
    self.accessLocation = accessLocation
    self.systemName = systemName
    self.certificate = certificate
    self.verifier = verifier
    self.secret = secret
    self.e2eeVersion = e2eeVersion

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.identityProvider = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.identifier = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.password = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.keepLoggedIn = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.accessLocation = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.systemName = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.certificate = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.verifier = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRING:
          self.secret = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I32:
          self.e2eeVersion = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('LoginRequest')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.identityProvider is not None:
      oprot.writeFieldBegin('identityProvider', TType.I32, 2)
      oprot.writeI32(self.identityProvider)
      oprot.writeFieldEnd()
    if self.identifier is not None:
      oprot.writeFieldBegin('identifier', TType.STRING, 3)
      oprot.writeString(self.identifier)
      oprot.writeFieldEnd()
    if self.password is not None:
      oprot.writeFieldBegin('password', TType.STRING, 4)
      oprot.writeString(self.password)
      oprot.writeFieldEnd()
    if self.keepLoggedIn is not None:
      oprot.writeFieldBegin('keepLoggedIn', TType.BOOL, 5)
      oprot.writeBool(self.keepLoggedIn)
      oprot.writeFieldEnd()
    if self.accessLocation is not None:
      oprot.writeFieldBegin('accessLocation', TType.STRING, 6)
      oprot.writeString(self.accessLocation)
      oprot.writeFieldEnd()
    if self.systemName is not None:
      oprot.writeFieldBegin('systemName', TType.STRING, 7)
      oprot.writeString(self.systemName)
      oprot.writeFieldEnd()
    if self.certificate is not None:
      oprot.writeFieldBegin('certificate', TType.STRING, 8)
      oprot.writeString(self.certificate)
      oprot.writeFieldEnd()
    if self.verifier is not None:
      oprot.writeFieldBegin('verifier', TType.STRING, 9)
      oprot.writeString(self.verifier)
      oprot.writeFieldEnd()
    if self.secret is not None:
      oprot.writeFieldBegin('secret', TType.STRING, 10)
      oprot.writeString(self.secret)
      oprot.writeFieldEnd()
    if self.e2eeVersion is not None:
      oprot.writeFieldBegin('e2eeVersion', TType.I32, 11)
      oprot.writeI32(self.e2eeVersion)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.identityProvider)
    value = (value * 31) ^ hash(self.identifier)
    value = (value * 31) ^ hash(self.password)
    value = (value * 31) ^ hash(self.keepLoggedIn)
    value = (value * 31) ^ hash(self.accessLocation)
    value = (value * 31) ^ hash(self.systemName)
    value = (value * 31) ^ hash(self.certificate)
    value = (value * 31) ^ hash(self.verifier)
    value = (value * 31) ^ hash(self.secret)
    value = (value * 31) ^ hash(self.e2eeVersion)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
