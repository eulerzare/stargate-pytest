import unittest

from decouple import config
from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket, TTransport

from stargate_thrift_classes.admin.AdminService import Client as AdminClient
from stargate_thrift_classes.admin.ttypes import AddCurrency, GetCurrencyRequest, GetContractRequest, \
    AddContractRequest, GetCurrencyResponse, GetContractResponse
from stargate_thrift_classes.base.ttypes import Response, MarketType, OrderType, OrderSide
from stargate_thrift_classes.trader.TraderService import Client as TraderClient
from stargate_thrift_classes.trader.ttypes import AddTrader, TraderAssetResponse, GetTraderAsset, TransferAsset, \
    PlaceOrder
from utils.test_constants import ADD_CURRENCY_ALL, ADD_TRADER_ALL, CONTRACTS_ALL, ADD_TRADER_01, ADD_CURRENCY_USDT, \
    ADD_TRADER_02, CONTRACT_BTCUSDT_PERPETUAL, ADD_TRADER_03, ADD_TRADER_04, ADD_TRADER_05

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
    def test_take_snapshot(self):
        admin_client.takeSnapshot()

    def test_define_currencies(self):
        for currency in ADD_CURRENCY_ALL:
            currency: AddCurrency
            response: Response = admin_client.addCurrency(currency)
            print(response)

    def test_define_trader(self):
        for trader in ADD_TRADER_ALL:
            trader: AddTrader
            response: Response = trader_client.addTrader(trader)
            print(response)

    def test_add_contracts(self):
        for contract in CONTRACTS_ALL:
            contract: AddContractRequest
            response: Response = admin_client.addContract(contract)
            print(response)

    def test_get_currencies(self):
        response: GetCurrencyResponse = admin_client.getCurrency(GetCurrencyRequest(currencyIds=list(range(1, 9))))
        for currency in response.currencies:
            print(currency)

    def test_get_contracts(self):
        response: GetContractResponse = admin_client.getContract(GetContractRequest(contractIds=list(range(1, 4))))
        for contract in response.contracts:
            print(contract)

    def test_get_traders_assets(self):
        for trader in ADD_TRADER_ALL:
            trader: AddTrader
            response: TraderAssetResponse = trader_client.getTraderAsset(GetTraderAsset(id=trader.id))
            print(response.assets)

    def test_transfer_asset(self):
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=1,
            traderId=ADD_TRADER_01.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="100000.45436609"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=2,
            traderId=ADD_TRADER_02.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="100000.436436"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=3,
            traderId=ADD_TRADER_03.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="80000.436436"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=4,
            traderId=ADD_TRADER_04.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="90000.436436"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=5,
            traderId=ADD_TRADER_05.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="91234.87654321"
        )))

    def test_place_order(self):
        print(trader_client.placeOrder(PlaceOrder(
            id=1,
            traderId=ADD_TRADER_01.id,
            contractId=CONTRACT_BTCUSDT_PERPETUAL.id,
            orderType=OrderType.LIMIT,
            orderSide=OrderSide.ASK,
            price="59990.0",
            size="1000",
            isSizeInBaseCurrency=False,
            leverage=5,
            isCrossMargin=False,
        )))

    def tearDown(self):
        transport.close()