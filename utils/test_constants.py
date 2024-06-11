from stargate_thrift_classes.admin.ttypes import AddCurrency, AddContractRequest
from stargate_thrift_classes.base.ttypes import MarketType
from stargate_thrift_classes.trader.ttypes import AddTrader

ADD_CURRENCY_BTC = AddCurrency(id=1, symbol="btC", scale=13)
ADD_CURRENCY_USDT = AddCurrency(id=2, symbol="usdT", scale=8)
ADD_CURRENCY_IRT = AddCurrency(id=3, symbol="IRT", scale=0)
ADD_CURRENCY_ETH = AddCurrency(id=4, symbol="eth", scale=12)
ADD_CURRENCY_TRX = AddCurrency(id=5, symbol="trx", scale=11)
ADD_CURRENCY_PAXG = AddCurrency(id=6, symbol="PAXG", scale=11)
ADD_CURRENCY_LTC = AddCurrency(id=7, symbol="ltc", scale=11)
ADD_CURRENCY_SHIB = AddCurrency(id=52, symbol="SHIB", scale=0)

ADD_CURRENCY_EMPTY = AddCurrency(id=32767, symbol="", scale=12)

ADD_CURRENCY_ALL = [
    ADD_CURRENCY_BTC, ADD_CURRENCY_USDT, ADD_CURRENCY_IRT,
    ADD_CURRENCY_ETH, ADD_CURRENCY_TRX, ADD_CURRENCY_PAXG,
    ADD_CURRENCY_LTC, ADD_CURRENCY_SHIB
]

ADD_TRADER_01 = AddTrader(id=1, makerFee="0.0001", takerFee="0.0002")
ADD_TRADER_02 = AddTrader(id=2, makerFee="0.0001", takerFee="0.0002")
ADD_TRADER_03 = AddTrader(id=3, makerFee="0.0001", takerFee="0.0002")
ADD_TRADER_04 = AddTrader(id=4, makerFee="0.0001", takerFee="0.0002")
ADD_TRADER_05 = AddTrader(id=5, makerFee="0.0001", takerFee="0.0002")

ADD_TRADER_ALL = [
    ADD_TRADER_01, ADD_TRADER_02, ADD_TRADER_03, ADD_TRADER_04, ADD_TRADER_05
]

CONTRACT_BTCUSDT_PERPETUAL = AddContractRequest(
    1, "BTCUSDT Perpetual", MarketType.PERPETUAL_USDM,
    ADD_CURRENCY_BTC.id, ADD_CURRENCY_USDT.id, ADD_CURRENCY_USDT.id,
    3, 2
)
CONTRACT_ETHUSDT_PERPETUAL = AddContractRequest(
    2, "ETHUSDT Perpetual", MarketType.PERPETUAL_USDM,
    ADD_CURRENCY_ETH.id, ADD_CURRENCY_USDT.id, ADD_CURRENCY_USDT.id,
    4, 3
)
CONTRACT_TRXUSDT_PERPETUAL = AddContractRequest(
    3, "TRXUSDT Perpetual", MarketType.PERPETUAL_USDM,
    ADD_CURRENCY_TRX.id, ADD_CURRENCY_USDT.id, ADD_CURRENCY_USDT.id,
    5, 4
)
ADD_CONTRACT_EMPTY = AddContractRequest(
    32767, "", MarketType.PERPETUAL_USDM,
    ADD_CURRENCY_TRX.id, ADD_CURRENCY_USDT.id, ADD_CURRENCY_USDT.id,
    5, 4
)

CONTRACTS_ALL = [
    CONTRACT_BTCUSDT_PERPETUAL, CONTRACT_ETHUSDT_PERPETUAL, CONTRACT_TRXUSDT_PERPETUAL
]
