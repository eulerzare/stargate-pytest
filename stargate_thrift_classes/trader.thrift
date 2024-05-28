include "base.thrift"

service TraderService {
  TraderResponse addTrader(1:AddTader addTader),
  TraderResponse blockTrader(1:BlockTader blockTader),
  TraderAssetResponse getTraderAsset(1:GetTraderAsset getTraderAsset),
  TransferAssetResponse transferAsset(1:TransferAsset transferAsset),
  base.Response placeOrder(1:PlaceOrder placeOrder)
}

struct AddTader {
  1: required i64 id,
}

struct TraderResponse {
  1: i32 status,
  2: string message,
  3: i64 sequence,
  4: base.Trader trader,
}

struct BlockTader {
  1: required i64 id,
  2: required bool active,
}

struct GetTraderAsset {
  1: required i64 id,
}

struct TraderAssetResponse {
  1: i32 status,
  2: string message,
  3: i64 sequence,
  4: list<base.Asset> assets,
}

struct TransferAssetResponse {
  1: i32 status,
  2: string message,
  3: i64 sequence,
  4: base.Asset asset,
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
  7: required string sizeInBaseCurrency,
  8: required i16 leverage,
}