include "base.thrift"

service TraderService {
  TraderResponse addTrader(1:AddTrader addTrader),
  TraderResponse blockTrader(1:BlockTrader blockTrader),
  TraderResponse changeTraderFee(1: ChangeTraderFee changeTraderFee),
  base.Response changeTraderMarginMode(1: ChangeTraderMarginMode changeTraderMarginType),
  base.Response changeTraderLeverage(1: ChangeTraderLeverage changeTraderLeverage),
  TraderResponse changeTraderHedgeMode(1: ChangeTraderHedgeMode changeTraderHedgeMode),
  TraderResponse changeTraderUsdmMultiAssetMode(1: ChangeTraderUsdmMultiAssetMode changeTraderUsdmMultiAssetMode),
  TraderAssetResponse getTraderAsset(1:GetTraderAsset getTraderAsset),
  TransferAssetResponse transferAsset(1:TransferAsset transferAsset),
  base.Response placeOrder(1:PlaceOrder placeOrder),
  base.Response cancelOrder(1:CancelOrder cancelOrder),
}

struct AddTrader {
  1: required i64 id,
  2: required string makerFee,
  3: required string takerFee,
}

struct TraderResponse {
  1: i32 status,
  2: i64 sequence,
  3: base.Trader trader,
}

struct BlockTrader {
  1: required i64 id,
  2: required bool active,
}

struct ChangeTraderFee {
  1: required i64 traderId,
  2: string makerFee,
  3: string takerFee,
}

struct ChangeTraderMarginMode {
  1: required i64 traderId,
  2: required i16 contractId,
  3: required base.PositionMarginMode marginMode,
}

struct ChangeTraderLeverage {
  1: required i64 traderId,
  2: required i16 contractId,
  3: required i16 leverage,
}

struct ChangeTraderHedgeMode {
  1: required i64 traderId,
  2: required bool hedgeModeActivate,
}

struct ChangeTraderUsdmMultiAssetMode {
  1: required i64 traderId,
  2: required bool usdmMultiAssetModeActivate,
}

struct GetTraderAsset {
  1: required i64 id,
}

struct TraderAssetResponse {
  1: i32 status,
  2: i64 sequence,
  3: list<base.Asset> assets,
}

struct TransferAssetResponse {
  1: i32 status,
  2: i64 sequence,
  3: base.Asset asset,
}

struct TransferAsset {
  1: required i64 uniqueId,
  2: required i64 traderId,
  3: required base.MarketType marketType,
  4: required i16 currencyId,
  5: required string amount,
}

struct PlaceOrder {
  1: required i64 id,
  2: required i64 traderId,
  3: required i16 contractId,
  4: required base.OrderType orderType,
  5: required base.OrderSide orderSide,
  6: string price,
  7: required string size,
  8: required bool isSizeInBaseCurrency,
}

struct CancelOrder {
  1: required i64 traderId,
  2: required i64 orderId,
}