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


class AddTrader(object):
    """
    Attributes:
     - id

    """

    def __init__(
        self,
        id=None,
    ):
        self.id = id

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
                if ftype == TType.I64:
                    self.id = iprot.readI64()
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
        oprot.writeStructBegin("AddTrader")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TraderResponse(object):
    """
    Attributes:
     - status
     - message
     - sequence
     - trader

    """

    def __init__(
        self,
        status=None,
        message=None,
        sequence=None,
        trader=None,
    ):
        self.status = status
        self.message = message
        self.sequence = sequence
        self.trader = trader

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
                if ftype == TType.STRUCT:
                    self.trader = stargate_thrift_classes.base.ttypes.Trader()
                    self.trader.read(iprot)
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
        oprot.writeStructBegin("TraderResponse")
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
        if self.trader is not None:
            oprot.writeFieldBegin("trader", TType.STRUCT, 4)
            self.trader.write(oprot)
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


class BlockTrader(object):
    """
    Attributes:
     - id
     - active

    """

    def __init__(
        self,
        id=None,
        active=None,
    ):
        self.id = id
        self.active = active

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
                if ftype == TType.I64:
                    self.id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.active = iprot.readBool()
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
        oprot.writeStructBegin("BlockTrader")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        if self.active is not None:
            oprot.writeFieldBegin("active", TType.BOOL, 2)
            oprot.writeBool(self.active)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        if self.active is None:
            raise TProtocolException(message="Required field active is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetTraderAsset(object):
    """
    Attributes:
     - id

    """

    def __init__(
        self,
        id=None,
    ):
        self.id = id

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
                if ftype == TType.I64:
                    self.id = iprot.readI64()
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
        oprot.writeStructBegin("GetTraderAsset")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TraderAssetResponse(object):
    """
    Attributes:
     - status
     - message
     - sequence
     - assets

    """

    def __init__(
        self,
        status=None,
        message=None,
        sequence=None,
        assets=None,
    ):
        self.status = status
        self.message = message
        self.sequence = sequence
        self.assets = assets

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
                    self.assets = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = stargate_thrift_classes.base.ttypes.Asset()
                        _elem5.read(iprot)
                        self.assets.append(_elem5)
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
        oprot.writeStructBegin("TraderAssetResponse")
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
        if self.assets is not None:
            oprot.writeFieldBegin("assets", TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.assets))
            for iter6 in self.assets:
                iter6.write(oprot)
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


class TransferAssetResponse(object):
    """
    Attributes:
     - status
     - message
     - sequence
     - asset

    """

    def __init__(
        self,
        status=None,
        message=None,
        sequence=None,
        asset=None,
    ):
        self.status = status
        self.message = message
        self.sequence = sequence
        self.asset = asset

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
                if ftype == TType.STRUCT:
                    self.asset = stargate_thrift_classes.base.ttypes.Asset()
                    self.asset.read(iprot)
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
        oprot.writeStructBegin("TransferAssetResponse")
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
        if self.asset is not None:
            oprot.writeFieldBegin("asset", TType.STRUCT, 4)
            self.asset.write(oprot)
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


class TransferAsset(object):
    """
    Attributes:
     - uniqueId
     - traderId
     - marketType
     - currencyId
     - amount

    """

    def __init__(
        self,
        uniqueId=None,
        traderId=None,
        marketType=None,
        currencyId=None,
        amount=None,
    ):
        self.uniqueId = uniqueId
        self.traderId = traderId
        self.marketType = marketType
        self.currencyId = currencyId
        self.amount = amount

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
                if ftype == TType.I64:
                    self.uniqueId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.traderId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.marketType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I16:
                    self.currencyId = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.amount = (
                        iprot.readString().decode("utf-8", errors="replace")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
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
        oprot.writeStructBegin("TransferAsset")
        if self.uniqueId is not None:
            oprot.writeFieldBegin("uniqueId", TType.I64, 1)
            oprot.writeI64(self.uniqueId)
            oprot.writeFieldEnd()
        if self.traderId is not None:
            oprot.writeFieldBegin("traderId", TType.I64, 2)
            oprot.writeI64(self.traderId)
            oprot.writeFieldEnd()
        if self.marketType is not None:
            oprot.writeFieldBegin("marketType", TType.I32, 3)
            oprot.writeI32(self.marketType)
            oprot.writeFieldEnd()
        if self.currencyId is not None:
            oprot.writeFieldBegin("currencyId", TType.I16, 4)
            oprot.writeI16(self.currencyId)
            oprot.writeFieldEnd()
        if self.amount is not None:
            oprot.writeFieldBegin("amount", TType.STRING, 5)
            oprot.writeString(
                self.amount.encode("utf-8") if sys.version_info[0] == 2 else self.amount
            )
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.uniqueId is None:
            raise TProtocolException(message="Required field uniqueId is unset!")
        if self.traderId is None:
            raise TProtocolException(message="Required field traderId is unset!")
        if self.marketType is None:
            raise TProtocolException(message="Required field marketType is unset!")
        if self.currencyId is None:
            raise TProtocolException(message="Required field currencyId is unset!")
        if self.amount is None:
            raise TProtocolException(message="Required field amount is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PlaceOrder(object):
    """
    Attributes:
     - id
     - traderId
     - contractId
     - orderType
     - orderSide
     - price
     - size
     - isSizeInBaseCurrency
     - leverage
     - isCrossMargin

    """

    def __init__(
        self,
        id=None,
        traderId=None,
        contractId=None,
        orderType=None,
        orderSide=None,
        price=None,
        size=None,
        isSizeInBaseCurrency=None,
        leverage=None,
        isCrossMargin=None,
    ):
        self.id = id
        self.traderId = traderId
        self.contractId = contractId
        self.orderType = orderType
        self.orderSide = orderSide
        self.price = price
        self.size = size
        self.isSizeInBaseCurrency = isSizeInBaseCurrency
        self.leverage = leverage
        self.isCrossMargin = isCrossMargin

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
                if ftype == TType.I64:
                    self.id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.traderId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.contractId = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.orderType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.orderSide = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.price = (
                        iprot.readString().decode("utf-8", errors="replace")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.size = (
                        iprot.readString().decode("utf-8", errors="replace")
                        if sys.version_info[0] == 2
                        else iprot.readString()
                    )
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.BOOL:
                    self.isSizeInBaseCurrency = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I16:
                    self.leverage = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.BOOL:
                    self.isCrossMargin = iprot.readBool()
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
        oprot.writeStructBegin("PlaceOrder")
        if self.id is not None:
            oprot.writeFieldBegin("id", TType.I64, 1)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        if self.traderId is not None:
            oprot.writeFieldBegin("traderId", TType.I64, 2)
            oprot.writeI64(self.traderId)
            oprot.writeFieldEnd()
        if self.contractId is not None:
            oprot.writeFieldBegin("contractId", TType.I16, 3)
            oprot.writeI16(self.contractId)
            oprot.writeFieldEnd()
        if self.orderType is not None:
            oprot.writeFieldBegin("orderType", TType.I32, 4)
            oprot.writeI32(self.orderType)
            oprot.writeFieldEnd()
        if self.orderSide is not None:
            oprot.writeFieldBegin("orderSide", TType.I32, 5)
            oprot.writeI32(self.orderSide)
            oprot.writeFieldEnd()
        if self.price is not None:
            oprot.writeFieldBegin("price", TType.STRING, 6)
            oprot.writeString(
                self.price.encode("utf-8") if sys.version_info[0] == 2 else self.price
            )
            oprot.writeFieldEnd()
        if self.size is not None:
            oprot.writeFieldBegin("size", TType.STRING, 7)
            oprot.writeString(
                self.size.encode("utf-8") if sys.version_info[0] == 2 else self.size
            )
            oprot.writeFieldEnd()
        if self.isSizeInBaseCurrency is not None:
            oprot.writeFieldBegin("isSizeInBaseCurrency", TType.BOOL, 8)
            oprot.writeBool(self.isSizeInBaseCurrency)
            oprot.writeFieldEnd()
        if self.leverage is not None:
            oprot.writeFieldBegin("leverage", TType.I16, 9)
            oprot.writeI16(self.leverage)
            oprot.writeFieldEnd()
        if self.isCrossMargin is not None:
            oprot.writeFieldBegin("isCrossMargin", TType.BOOL, 10)
            oprot.writeBool(self.isCrossMargin)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.id is None:
            raise TProtocolException(message="Required field id is unset!")
        if self.traderId is None:
            raise TProtocolException(message="Required field traderId is unset!")
        if self.contractId is None:
            raise TProtocolException(message="Required field contractId is unset!")
        if self.orderType is None:
            raise TProtocolException(message="Required field orderType is unset!")
        if self.orderSide is None:
            raise TProtocolException(message="Required field orderSide is unset!")
        if self.size is None:
            raise TProtocolException(message="Required field size is unset!")
        if self.isSizeInBaseCurrency is None:
            raise TProtocolException(
                message="Required field isSizeInBaseCurrency is unset!"
            )
        if self.leverage is None:
            raise TProtocolException(message="Required field leverage is unset!")
        if self.isCrossMargin is None:
            raise TProtocolException(message="Required field isCrossMargin is unset!")
        return

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


all_structs.append(AddTrader)
AddTrader.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I64,
        "id",
        None,
        None,
    ),  # 1
)
all_structs.append(TraderResponse)
TraderResponse.thrift_spec = (
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
        TType.STRUCT,
        "trader",
        [stargate_thrift_classes.base.ttypes.Trader, None],
        None,
    ),  # 4
)
all_structs.append(BlockTrader)
BlockTrader.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I64,
        "id",
        None,
        None,
    ),  # 1
    (
        2,
        TType.BOOL,
        "active",
        None,
        None,
    ),  # 2
)
all_structs.append(GetTraderAsset)
GetTraderAsset.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I64,
        "id",
        None,
        None,
    ),  # 1
)
all_structs.append(TraderAssetResponse)
TraderAssetResponse.thrift_spec = (
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
        "assets",
        (TType.STRUCT, [stargate_thrift_classes.base.ttypes.Asset, None], False),
        None,
    ),  # 4
)
all_structs.append(TransferAssetResponse)
TransferAssetResponse.thrift_spec = (
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
        TType.STRUCT,
        "asset",
        [stargate_thrift_classes.base.ttypes.Asset, None],
        None,
    ),  # 4
)
all_structs.append(TransferAsset)
TransferAsset.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I64,
        "uniqueId",
        None,
        None,
    ),  # 1
    (
        2,
        TType.I64,
        "traderId",
        None,
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
        "currencyId",
        None,
        None,
    ),  # 4
    (
        5,
        TType.STRING,
        "amount",
        "UTF8",
        None,
    ),  # 5
)
all_structs.append(PlaceOrder)
PlaceOrder.thrift_spec = (
    None,  # 0
    (
        1,
        TType.I64,
        "id",
        None,
        None,
    ),  # 1
    (
        2,
        TType.I64,
        "traderId",
        None,
        None,
    ),  # 2
    (
        3,
        TType.I16,
        "contractId",
        None,
        None,
    ),  # 3
    (
        4,
        TType.I32,
        "orderType",
        None,
        None,
    ),  # 4
    (
        5,
        TType.I32,
        "orderSide",
        None,
        None,
    ),  # 5
    (
        6,
        TType.STRING,
        "price",
        "UTF8",
        None,
    ),  # 6
    (
        7,
        TType.STRING,
        "size",
        "UTF8",
        None,
    ),  # 7
    (
        8,
        TType.BOOL,
        "isSizeInBaseCurrency",
        None,
        None,
    ),  # 8
    (
        9,
        TType.I16,
        "leverage",
        None,
        None,
    ),  # 9
    (
        10,
        TType.BOOL,
        "isCrossMargin",
        None,
        None,
    ),  # 10
)
fix_spec(all_structs)
del all_structs