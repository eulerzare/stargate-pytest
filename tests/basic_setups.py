import unittest

from decouple import config
from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket, TTransport

from stargate_thrift_classes.admin.AdminService import Client as AdminClient
from stargate_thrift_classes.admin.ttypes import AddCurrency
from stargate_thrift_classes.base.ttypes import Response
from stargate_thrift_classes.trader.TraderService import Client as TraderClient
from stargate_thrift_classes.trader.ttypes import AddTrader
from utils.test_constants import ADD_CURRENCY_ALL, ADD_TRADER_ALL

host = config("THRIFT_HOST", cast=str)
port = config("THRIFT_PORT", cast=int)
transport = TSocket.TSocket(host, port)
# transport.setTimeout(10000.)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

admin_client = AdminClient(TMultiplexedProtocol.TMultiplexedProtocol(protocol, "AdminService"))
trader_client = TraderClient(TMultiplexedProtocol.TMultiplexedProtocol(protocol, "TraderService"))
transport.open()


class BasicSetups(unittest.TestCase):
    @staticmethod
    def test_take_snapshot():
        admin_client.takeSnapshot()

    @staticmethod
    def test_define_currencies():
        for currency in ADD_CURRENCY_ALL:
            currency: AddCurrency
            response: Response = admin_client.addCurrency(currency)
            print(response)

    @staticmethod
    def test_define_trader():
        for trader in ADD_TRADER_ALL:
            trader: AddTrader
            response: Response = trader_client.addTrader(trader)
            print(response)

    def tearDown(self):
        transport.close()
