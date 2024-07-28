include "base.thrift"

service AdminService {
  base.Response takeSnapshot(),
  base.Response addCurrency(1:AddCurrency addCurrency),
  GetCurrencyResponse getCurrency(1:GetCurrencyRequest getCurrencyRequest),
  base.Response changeCurrencyScale(1:ChangeCurrencyScaleRequest changeCurrencyScaleRequest),
  base.Response addContract(1:AddContractRequest addContractRequest),
  GetContractResponse getContract(1:GetContractRequest getContractRequest),
  base.Response changeContractScale(1:ChangeContractScaleRequest changeContractScaleRequest),
  base.Response addOrModifyTierLevel(1: base.Tier addOrModifyTierRequest),
  GetTiersResponse getTiers(),
}

struct AddCurrency {
  1: required i16 id,
  2: required string symbol,
  3: required i32 scale,
}

struct GetCurrencyRequest {
  1: required list<i16> currencyIds,
}

struct GetCurrencyResponse {
  1: i32 status,
  2: i64 sequence,
  3: list<base.Currency> currencies,
}

struct ChangeCurrencyScaleRequest {
  1: required i16 id,
  2: required i32 scale,
}

struct AddContractRequest {
  1: required i16 id,
  2: required string name,
  3: required base.MarketType marketType,
  4: required i16 priceSymbolCode,
  5: required i16 baseCurrencyId,
  6: required i16 quoteCurrencyId,
  7: required i16 settlementCurrencyId,
  8: required i32 baseScale,
  9: required i32 quoteScale,
}

struct GetContractRequest {
  1: required list<i16> contractIds,
}

struct GetContractResponse {
  1: i32 status,
  2: i64 sequence,
  3: list<base.Contract> contracts,
}

struct ChangeContractScaleRequest {
  1: required i16 id,
  2: required i32 baseScale,
  3: required i32 quoteScale,
}

struct GetTiersResponse {
  1: i32 status,
  2: i64 sequence,
  3: list<base.Tier> tiers,
}