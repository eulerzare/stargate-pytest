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

struct Trader {
  1: required i64 id,
  2: required bool active,
  3: required bool hedgeMode,
  4: required bool usdmMultiAssetMode,
  5: required string makerFee,
  6: required string takerFee,
}
