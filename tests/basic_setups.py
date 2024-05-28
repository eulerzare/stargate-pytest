import unittest

from decouple import config
from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket, TTransport

from stargate_thrift_classes.admin.AdminService import Client as AdminClient
from stargate_thrift_classes.trader.TraderService import Client as TraderClient

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

    def tearDown(self):
        transport.close()
