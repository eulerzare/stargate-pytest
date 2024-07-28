import unittest

from decouple import config
from thrift.protocol import TBinaryProtocol, TMultiplexedProtocol
from thrift.transport import TSocket, TTransport

from stargate_thrift_classes.admin.AdminService import Client as AdminClient
from stargate_thrift_classes.admin.ttypes import AddCurrency, GetCurrencyRequest, GetContractRequest, \
    AddContractRequest, GetCurrencyResponse, GetContractResponse, GetTiersResponse
from stargate_thrift_classes.base.ttypes import Response, MarketType, OrderType, OrderSide, PositionMarginMode, Tier
from stargate_thrift_classes.trader.TraderService import Client as TraderClient
from stargate_thrift_classes.trader.ttypes import AddTrader, TraderAssetResponse, GetTraderAsset, TransferAsset, \
    PlaceOrder, ChangeTraderHedgeMode, TraderResponse, ChangeTraderUsdmMultiAssetMode, ChangeTraderFee, CancelOrder, \
    ChangeTraderLeverage, ModifyOrder, ChangeTraderMarginMode, GetTraderOrderPosition, TraderOrderPositionResponse
from utils.test_constants import ADD_CURRENCY_ALL, ADD_TRADER_ALL, CONTRACTS_ALL, ADD_TRADER_01, ADD_CURRENCY_USDT, \
    ADD_TRADER_02, CONTRACT_BTCUSDT_PERPETUAL, ADD_TRADER_03, ADD_TRADER_04, ADD_TRADER_05, CONTRACT_ETHUSDT_PERPETUAL

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

    def test_define_traders(self):
        for trader in ADD_TRADER_ALL:
            trader: AddTrader
            response: TraderResponse = trader_client.addTrader(trader)
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

    def test_get_trader_order_position(self):
        for trader in ADD_TRADER_ALL:
            trader: AddTrader
            response: TraderOrderPositionResponse = trader_client.getTraderOrderPosition(GetTraderOrderPosition(id=trader.id))
            print(response.orders)
            print(response.positions)

    def test_change_trader_hedge_mode(self):
        trader: AddTrader = ADD_TRADER_01
        response: TraderResponse = trader_client.changeTraderHedgeMode(
            ChangeTraderHedgeMode(traderId=trader.id, hedgeModeActivate=True)
        )
        print(response)

    def test_change_usdm_multi_asset_mode(self):
        trader: AddTrader = ADD_TRADER_01
        response: TraderResponse = trader_client.changeTraderUsdmMultiAssetMode(
            ChangeTraderUsdmMultiAssetMode(traderId=trader.id, usdmMultiAssetModeActivate=True)
        )
        print(response)

    def test_change_trader_fee(self):
        trader: AddTrader = ADD_TRADER_01
        response: TraderResponse = trader_client.changeTraderFee(
            ChangeTraderFee(traderId=trader.id, makerFee="0.0015", takerFee="0.00032")
        )
        print(response)

    def test_change_trader_leverage(self):
        response: Response = trader_client.changeTraderLeverage(ChangeTraderLeverage(
            traderId=ADD_TRADER_01.id, contractId=CONTRACT_BTCUSDT_PERPETUAL.id, leverage=2
        ))
        print(response)

    def test_change_trader_margin_mode(self):
        response: Response = trader_client.changeTraderMarginMode(ChangeTraderMarginMode(
            traderId=ADD_TRADER_02.id, contractId=CONTRACT_BTCUSDT_PERPETUAL.id, marginMode=PositionMarginMode.CROSS
        ))
        print(response)

    def test_add_or_change_tiers(self):
        response: Response = admin_client.addOrModifyTierLevel(Tier(
            "600000", 80, "", ""
        ))
        print(response)

    def test_get_tiers(self):
        response: GetTiersResponse = admin_client.getTiers()
        for tier in response.tiers:
            print(tier)

    def test_transfer_asset(self):
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=1,
            traderId=ADD_TRADER_01.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="100000"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=2,
            traderId=ADD_TRADER_02.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="100000"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=3,
            traderId=ADD_TRADER_03.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="100000"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=4,
            traderId=ADD_TRADER_04.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="100000"
        )))
        print(trader_client.transferAsset(TransferAsset(
            uniqueId=5,
            traderId=ADD_TRADER_05.id,
            marketType=MarketType.PERPETUAL_USDM,
            currencyId=ADD_CURRENCY_USDT.id,
            amount="100000"
        )))

    def test_place_order(self):
        print(trader_client.placeOrder(PlaceOrder(
            id=4,
            traderId=ADD_TRADER_02.id,
            contractId=CONTRACT_BTCUSDT_PERPETUAL.id,
            orderType=OrderType.LIMIT,
            orderSide=OrderSide.BUY,
            price="62000",
            size="8",
            isSizeInBaseCurrency=True,
        )))

    def test_cancel_order(self):
        print(trader_client.cancelOrder(CancelOrder(
            traderId=ADD_TRADER_01.id,
            orderId=1,
        )))

    def test_modify_order(self):
        print(trader_client.modifyOrder(ModifyOrder(
            traderId=ADD_TRADER_01.id,
            orderId=5,
            price="63000",
            size="2",
            isSizeInBaseCurrency=True,
        )))

    def tearDown(self):
        transport.close()
