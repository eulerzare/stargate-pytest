enum MarketType {
  PERPETUAL_USDM = 1,
  PERPETUAL_COINM = 2,
}

enum OrderType {
  LIMIT = 1,
}

enum OrderSide {
  BUY = 1,
  SELL = 2,
  OPEN_LONG = 3,
  CLOSE_LONG = 4,
  OPEN_SHORT = 5,
  CLOSE_SHORT = 6,
}

enum PositionSide {
  LONG = 1,
  SHORT = 2,
}

enum PositionMarginMode {
  ISOLATED = 1,
  CROSS = 2,
}

struct Response {
  1: i32 status,
  2: i64 sequence,
}

struct Currency {
  1: required i16 id,
  2: required string symbol,
  3: required i32 scale,
}

struct Asset {
  1: required i64 traderId,
  2: required MarketType marketType,
  3: required i16 currencyId,
  4: required string balance,
}

struct Contract {
  1: required i16 id,
  2: required string name,
  3: required MarketType marketType,
  4: required i16 baseCurrencyId,
  5: required i16 quoteCurrencyId,
  6: required i16 settlementCurrencyId,
  7: required i32 baseScale,
  8: required i32 quoteScale,
}

struct TraderContractInfo {
  1: required i16 contractId
  2: required PositionMarginMode positionMarginMode,
  3: required i16 leverage,
}

struct Trader {
  1: required i64 id,
  2: required bool active,
  3: required bool hedgeMode,
  4: required bool usdmMultiAssetMode,
  5: required string makerFee,
  6: required string takerFee,
  7: required list<TraderContractInfo> traderContractInfos,
}

struct Order {
  1: required i64 id,
  2: required i64 creationTimeMs,
  3: required i64 traderId,
  4: required i16 contractId,
  5: required OrderType orderType,
  6: required OrderSide orderSide,
  7: required string price,
  8: required string size,
  9: required string filled,
}

struct Position {
  1: required i64 id,
  3: required i64 traderId,
  4: required i16 contractId,
  5: required PositionSide positionSide,
  6: required PositionMarginMode positionMarginMode,
  7: required string avgEntryPrice,
  8: required string size,
  9: required string margin,
  10: required string maintenanceMargin,
}

struct Tier {
  1: required string bracketMax,
  2: required i16 maxLeverage,
  3: required string maintenanceMarginRate,
  4: required string maintenanceAmountUsdt,
}