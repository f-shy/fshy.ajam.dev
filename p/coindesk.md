# CryptoCompare

> coindesk.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coindesk/ | JSON https://fshy.ajam.dev/api/v1/entity/coindesk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CryptoCompare (CoinDesk Data)

- `data-apis/cryptocompare-coindesk-data` | trial-only | evidence documented | binding volume-quota | category crypto market data API (prices, OHLCV, reference rates, order books) | tier Personal
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://developers.coindesk.com/pricing
- free tier: Personal plan for non-commercial projects with capped lifetime calls (cap not stated), by contact request; the free API tier was retired on 21 May 2026 and accounts without a subscription lost access | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Start-Up and Enterprise plans are contact-only with no published price. A call to the legacy keyless endpoint answered HTTP 401.
- per-object cap: not stated | source: [1]
- retention: not applicable | note: Personal: 365 days of daily, 7 days of hourly, latest hour of minute history.
- egress: not metered in bytes; the lifetime call cap bounds a Personal account | metered: no | source: [1]
- identity: email | detail: The Personal plan button leads to a Contact form, not a self-serve sign-up; what the form asks is unverified: behind a contact request.
- interface: rest
- limits:
  - volume-quota (binding): capped lifetime calls on the Personal plan, cap not stated [1]
- limits note: Bulk path: Enterprise delivery to Amazon S3, Azure Blob or Google BigQuery only. Storage terms: unverified, the licence agreement page was not read.
- binding note: A lifetime call cap on the only free-looking plan binds first, and its size is unpublished.
- interface detail: GET https://min-api.cryptocompare.com/data/... (legacy) and https://data-api.coindesk.com/... with the key as api_key or an Authorization or x-api-key header
- endpoint: part of interface detail
- tooling: curl or any HTTP client
- composes with: No self-serve free key remains; CoinPaprika, CoinLore and CoinGecko give crypto prices with a key-free or email-only free route.
- reliability: A keyless call answered HTTP 401 asking for an API key; accounts without a subscription stopped returning data after 21 May 2026.
- notes: Free tier retired 21 May 2026; only a capped-lifetime Personal plan by contact remains listed. Bulk path: Enterprise only. Storage terms: unverified.
- evidence note: The retirement notice and the plan card are first-party and disagree on whether a free Personal plan is still issued; a keyless probe answered 401.
- extras:
  - bulk_path: Enterprise delivery to S3, Azure Blob or BigQuery
  - history_depth: 365 days daily, 7 days hourly, 1 hour minute on Personal
- evidence:
  - [2] 2026-11-02: the free API tier was retired as of 21 May 2026 | capture: sha256:00e99545d296af988ee0828ecae953bc6434de76a9f4aae049716dc9e79a69f2 | quote: we will be retiring our free API tier and accounts without a subscription will no longer have API access.
  - [2] 2026-11-02: an account with no API subscription stops returning data | capture: sha256:00e99545d296af988ee0828ecae953bc6434de76a9f4aae049716dc9e79a69f2 | quote: your current access will stop returning data
  - [1] 2026-11-02: the Personal plan is non-commercial with capped lifetime calls | capture: sha256:91b2cf732b44efb0ff3f84d5c015c93e8a43dae3294d443de8aeba372b2b5440 | quote: For personal / non-commercial projects. Capped lifetime calls.
  - [1] 2026-11-02: Personal history depth | capture: sha256:91b2cf732b44efb0ff3f84d5c015c93e8a43dae3294d443de8aeba372b2b5440 | quote: Latest 7 days for all pairs on all exchanges including CCCAGG
  - [1] 2026-11-02: Enterprise delivers to cloud storage | capture: sha256:91b2cf732b44efb0ff3f84d5c015c93e8a43dae3294d443de8aeba372b2b5440 | quote: Amazon S3, Azure Blob, Google BQ & More
  - probe:https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD 2026-11-03: a keyless call answered HTTP 401 | capture: sha256:35ce2dc7335e140d12fe48e1d645d5ac3c4dc56274cc82f36a5dac417644cd14 | quote: "status": 401
  - probe:https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD 2026-11-03: the 401 asks for an API key | capture: sha256:e54a34359ebeb4245031b742ee300e3fdd72ccf608d481d57caca1fc16147f17 | quote: API key required, please refer to the documentation
- sources:
  - [1] https://developers.coindesk.com/pricing
  - [2] https://data.coindesk.com/blogs/changes-to-coindesk-data-indices-api-free-tier-access
