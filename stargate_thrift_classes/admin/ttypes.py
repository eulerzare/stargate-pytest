#
# Autogenerated by Thrift Compiler (0.21.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import (
    TType,
    TMessageType,
    TFrozenDict,
    TException,
    TApplicationException,
)
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import stargate_thrift_classes.base.ttypes

from thrift.transport import TTransport

all_structs = []


class AddCurrency(object):
    """
    Attributes:
     - id
     - symbol
     - scale

    """

    def __init__(
        self,
        id=None,
        symbol=None,
        scale=None,
    ):
        self.id = id
        self.symbol = symbol
        self.scale = scale

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I16:
                    self.id = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.symbol = (
                        iprot.readString().decode("utf-8", errors="replace")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.scale = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("AddCurrency")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I16, 1)
            oprot.writeI16(self.id)
            oprot.writeFieldEnd()
        if self.symbol is not None:
            oprot.writeFieldBegin("symbol", TType.STRING, 2)
            oprot.writeString(
                self.symbol.encode("utf-8") if sys.version_info[0] == 2 else self.symbol
            )
            oprot.writeFieldEnd()
        if self.scale is not None:
            oprot.writeFieldBegin("scale", TType.I32, 3)
            oprot.writeI32(self.scale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        if self.symbol is None:
            raise TProtocolException(message="Required field symbol is unset!")
        if self.scale is None:
            raise TProtocolException(message="Required field scale is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetCurrencyRequest(object):
    """
    Attributes:
     - currencyIds

    """

    def __init__(
        self,
        currencyIds=None,
    ):
        self.currencyIds = currencyIds

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.currencyIds = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readI16()
                        self.currencyIds.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("GetCurrencyRequest")
        if self.currencyIds is not None:
            oprot.writeFieldBegin("currencyIds", TType.LIST, 1)
            oprot.writeListBegin(TType.I16, len(self.currencyIds))
            for iter6 in self.currencyIds:
                oprot.writeI16(iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.currencyIds is None:
            raise TProtocolException(message="Required field currencyIds is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetCurrencyResponse(object):
    """
    Attributes:
     - status
     - message
     - sequence
     - currencies

    """

    def __init__(
        self,
        status=None,
        message=None,
        sequence=None,
        currencies=None,
    ):
        self.status = status
        self.message = message
        self.sequence = sequence
        self.currencies = currencies

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = (
                        iprot.readString().decode("utf-8", errors="replace")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.sequence = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.currencies = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = stargate_thrift_classes.base.ttypes.Currency()
                        _elem12.read(iprot)
                        self.currencies.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("GetCurrencyResponse")
        if self.status is not None:
            oprot.writeFieldBegin("status", TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin("message", TType.STRING, 2)
            oprot.writeString(
                self.message.encode("utf-8")
                if sys.version_info[0] == 2
                else self.message
            )
            oprot.writeFieldEnd()
        if self.sequence is not None:
            oprot.writeFieldBegin("sequence", TType.I64, 3)
            oprot.writeI64(self.sequence)
            oprot.writeFieldEnd()
        if self.currencies is not None:
            oprot.writeFieldBegin("currencies", TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.currencies))
            for iter13 in self.currencies:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChangeCurrencyScaleRequest(object):
    """
    Attributes:
     - id
     - scale

    """

    def __init__(
        self,
        id=None,
        scale=None,
    ):
        self.id = id
        self.scale = scale

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I16:
                    self.id = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.scale = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("ChangeCurrencyScaleRequest")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I16, 1)
            oprot.writeI16(self.id)
            oprot.writeFieldEnd()
        if self.scale is not None:
            oprot.writeFieldBegin("scale", TType.I32, 2)
            oprot.writeI32(self.scale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        if self.scale is None:
            raise TProtocolException(message="Required field scale is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AddContractRequest(object):
    """
    Attributes:
     - id
     - name
     - marketType
     - baseCurrencyId
     - quoteCurrencyId
     - settlementCurrencyId
     - baseScale
     - quoteScale

    """

    def __init__(
        self,
        id=None,
        name=None,
        marketType=None,
        baseCurrencyId=None,
        quoteCurrencyId=None,
        settlementCurrencyId=None,
        baseScale=None,
        quoteScale=None,
    ):
        self.id = id
        self.name = name
        self.marketType = marketType
        self.baseCurrencyId = baseCurrencyId
        self.quoteCurrencyId = quoteCurrencyId
        self.settlementCurrencyId = settlementCurrencyId
        self.baseScale = baseScale
        self.quoteScale = quoteScale

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I16:
                    self.id = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = (
                        iprot.readString().decode("utf-8", errors="replace")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.marketType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.baseCurrencyId = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I16:
                    self.quoteCurrencyId = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I16:
                    self.settlementCurrencyId = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.baseScale = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.quoteScale = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("AddContractRequest")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I16, 1)
            oprot.writeI16(self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin("name", TType.STRING, 2)
            oprot.writeString(
                self.name.encode("utf-8") if sys.version_info[0] == 2 else self.name
            )
            oprot.writeFieldEnd()
        if self.marketType is not None:
            oprot.writeFieldBegin("marketType", TType.I32, 3)
            oprot.writeI32(self.marketType)
            oprot.writeFieldEnd()
        if self.baseCurrencyId is not None:
            oprot.writeFieldBegin("baseCurrencyId", TType.I16, 4)
            oprot.writeI16(self.baseCurrencyId)
            oprot.writeFieldEnd()
        if self.quoteCurrencyId is not None:
            oprot.writeFieldBegin("quoteCurrencyId", TType.I16, 5)
            oprot.writeI16(self.quoteCurrencyId)
            oprot.writeFieldEnd()
        if self.settlementCurrencyId is not None:
            oprot.writeFieldBegin("settlementCurrencyId", TType.I16, 6)
            oprot.writeI16(self.settlementCurrencyId)
            oprot.writeFieldEnd()
        if self.baseScale is not None:
            oprot.writeFieldBegin("baseScale", TType.I32, 7)
            oprot.writeI32(self.baseScale)
            oprot.writeFieldEnd()
        if self.quoteScale is not None:
            oprot.writeFieldBegin("quoteScale", TType.I32, 8)
            oprot.writeI32(self.quoteScale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        if self.name is None:
            raise TProtocolException(message="Required field name is unset!")
        if self.marketType is None:
            raise TProtocolException(message="Required field marketType is unset!")
        if self.baseCurrencyId is None:
            raise TProtocolException(message="Required field baseCurrencyId is unset!")
        if self.quoteCurrencyId is None:
            raise TProtocolException(message="Required field quoteCurrencyId is unset!")
        if self.settlementCurrencyId is None:
            raise TProtocolException(
                message="Required field settlementCurrencyId is unset!"
            )
        if self.baseScale is None:
            raise TProtocolException(message="Required field baseScale is unset!")
        if self.quoteScale is None:
            raise TProtocolException(message="Required field quoteScale is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetContractRequest(object):
    """
    Attributes:
     - contractIds

    """

    def __init__(
        self,
        contractIds=None,
    ):
        self.contractIds = contractIds

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.contractIds = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = iprot.readI16()
                        self.contractIds.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("GetContractRequest")
        if self.contractIds is not None:
            oprot.writeFieldBegin("contractIds", TType.LIST, 1)
            oprot.writeListBegin(TType.I16, len(self.contractIds))
            for iter20 in self.contractIds:
                oprot.writeI16(iter20)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.contractIds is None:
            raise TProtocolException(message="Required field contractIds is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetContractResponse(object):
    """
    Attributes:
     - status
     - message
     - sequence
     - contracts

    """

    def __init__(
        self,
        status=None,
        message=None,
        sequence=None,
        contracts=None,
    ):
        self.status = status
        self.message = message
        self.sequence = sequence
        self.contracts = contracts

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = (
                        iprot.readString().decode("utf-8", errors="replace")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.sequence = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.contracts = []
                    (_etype24, _size21) = iprot.readListBegin()
                    for _i25 in range(_size21):
                        _elem26 = stargate_thrift_classes.base.ttypes.Contract()
                        _elem26.read(iprot)
                        self.contracts.append(_elem26)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("GetContractResponse")
        if self.status is not None:
            oprot.writeFieldBegin("status", TType.I32, 1)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin("message", TType.STRING, 2)
            oprot.writeString(
                self.message.encode("utf-8")
                if sys.version_info[0] == 2
                else self.message
            )
            oprot.writeFieldEnd()
        if self.sequence is not None:
            oprot.writeFieldBegin("sequence", TType.I64, 3)
            oprot.writeI64(self.sequence)
            oprot.writeFieldEnd()
        if self.contracts is not None:
            oprot.writeFieldBegin("contracts", TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.contracts))
            for iter27 in self.contracts:
                iter27.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class ChangeContractScaleRequest(object):
    """
    Attributes:
     - id
     - baseScale
     - quoteScale

    """

    def __init__(
        self,
        id=None,
        baseScale=None,
        quoteScale=None,
    ):
        self.id = id
        self.baseScale = baseScale
        self.quoteScale = quoteScale

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I16:
                    self.id = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.baseScale = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.quoteScale = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(
                oprot._fast_encode(self, [self.__class__, self.thrift_spec])
            )
            return
        oprot.writeStructBegin("ChangeContractScaleRequest")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I16, 1)
            oprot.writeI16(self.id)
            oprot.writeFieldEnd()
        if self.baseScale is not None:
            oprot.writeFieldBegin("baseScale", TType.I32, 2)
            oprot.writeI32(self.baseScale)
            oprot.writeFieldEnd()
        if self.quoteScale is not None:
            oprot.writeFieldBegin("quoteScale", TType.I32, 3)
            oprot.writeI32(self.quoteScale)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        if self.baseScale is None:
            raise TProtocolException(message="Required field baseScale is unset!")
        if self.quoteScale is None:
            raise TProtocolException(message="Required field quoteScale is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(AddCurrency)
AddCurrency.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I16,
        "id",
        None,
        None,
    ),  # 1
    (
        2,
        TType.STRING,
        "symbol",
        "UTF8",
        None,
    ),  # 2
    (
        3,
        TType.I32,
        "scale",
        None,
        None,
    ),  # 3
)
all_structs.append(GetCurrencyRequest)
GetCurrencyRequest.thrift_spec = (
    None,  # 0
    (
        1,
        TType.LIST,
        "currencyIds",
        (TType.I16, None, False),
        None,
    ),  # 1
)
all_structs.append(GetCurrencyResponse)
GetCurrencyResponse.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I32,
        "status",
        None,
        None,
    ),  # 1
    (
        2,
        TType.STRING,
        "message",
        "UTF8",
        None,
    ),  # 2
    (
        3,
        TType.I64,
        "sequence",
        None,
        None,
    ),  # 3
    (
        4,
        TType.LIST,
        "currencies",
        (TType.STRUCT, [stargate_thrift_classes.base.ttypes.Currency, None], False),
        None,
    ),  # 4
)
all_structs.append(ChangeCurrencyScaleRequest)
ChangeCurrencyScaleRequest.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I16,
        "id",
        None,
        None,
    ),  # 1
    (
        2,
        TType.I32,
        "scale",
        None,
        None,
    ),  # 2
)
all_structs.append(AddContractRequest)
AddContractRequest.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I16,
        "id",
        None,
        None,
    ),  # 1
    (
        2,
        TType.STRING,
        "name",
        "UTF8",
        None,
    ),  # 2
    (
        3,
        TType.I32,
        "marketType",
        None,
        None,
    ),  # 3
    (
        4,
        TType.I16,
        "baseCurrencyId",
        None,
        None,
    ),  # 4
    (
        5,
        TType.I16,
        "quoteCurrencyId",
        None,
        None,
    ),  # 5
    (
        6,
        TType.I16,
        "settlementCurrencyId",
        None,
        None,
    ),  # 6
    (
        7,
        TType.I32,
        "baseScale",
        None,
        None,
    ),  # 7
    (
        8,
        TType.I32,
        "quoteScale",
        None,
        None,
    ),  # 8
)
all_structs.append(GetContractRequest)
GetContractRequest.thrift_spec = (
    None,  # 0
    (
        1,
        TType.LIST,
        "contractIds",
        (TType.I16, None, False),
        None,
    ),  # 1
)
all_structs.append(GetContractResponse)
GetContractResponse.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I32,
        "status",
        None,
        None,
    ),  # 1
    (
        2,
        TType.STRING,
        "message",
        "UTF8",
        None,
    ),  # 2
    (
        3,
        TType.I64,
        "sequence",
        None,
        None,
    ),  # 3
    (
        4,
        TType.LIST,
        "contracts",
        (TType.STRUCT, [stargate_thrift_classes.base.ttypes.Contract, None], False),
        None,
    ),  # 4
)
all_structs.append(ChangeContractScaleRequest)
ChangeContractScaleRequest.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I16,
        "id",
        None,
        None,
    ),  # 1
    (
        2,
        TType.I32,
        "baseScale",
        None,
        None,
    ),  # 2
    (
        3,
        TType.I32,
        "quoteScale",
        None,
        None,
    ),  # 3
)
fix_spec(all_structs)
del all_structs
