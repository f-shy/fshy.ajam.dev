# DefiLlama

> defillama.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/defillama/ | JSON https://fshy.ajam.dev/api/v1/entity/defillama.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DefiLlama

- `data-apis/defillama` | qualifies-with-caveat | evidence documented | binding request-rate | category DeFi data API (TVL, prices, yields, stablecoins, fees) | tier Free API
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://api-docs.defillama.com/llms.txt
- free tier: Free API at api.llama.fi: no key, 31 endpoints, standard rate limit (number not published) | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: The API plan is USD 300 a month with 1,000 requests a minute and 1M calls a month; the Free API and the API plan are separate services. A keyless TVL call answered HTTP 200.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered; no quota is stated for the Free API | metered: no | source: [1]
- identity: anonymous | detail: The Free API needs no key and no account: the docs say so and a keyless call answered HTTP 200.
- interface: rest
- limits:
  - request-rate (binding): standard rate limit on the Free API, number not published; the API plan is 1,000 requests per minute [1]
- limits note: Bulk path: CSV downloads of 34 datasets are for Pro and API subscribers only; the Free API serves JSON per endpoint. Storage terms: unverified, no page read states one.
- binding note: Only a request rate applies, and its size is unpublished.
- interface detail: GET https://api.llama.fi/... with no key; the API plan uses https://pro-api.llama.fi/KEY/...
- endpoint: part of interface detail
- tooling: curl or any HTTP client; JavaScript and Python SDKs and an OpenAPI document are published
- composes with: Keyless TVL, token prices and yield pools for DeFi; it pairs with CoinPaprika for market-wide prices.
- reliability: The standard limit has no published number; a 402 from api.llama.fi means the endpoint needs the paid API.
- notes: Keyless with an unpublished standard rate. Bulk path: CSV downloads are paid. Storage terms: unverified.
- evidence note: Terms are read from the vendor docs and a keyless probe answered 200; the Free API rate was not measured.
- extras:
  - bulk_path: CSV downloads of 34 datasets for Pro and API subscribers
- evidence:
  - [1] 2026-11-02: the Free API needs no key; the paid API is USD 300 a month | capture: sha256:cb0a290ffb958a034d57858aeb24aebb2711aebfe9f19a33cd042dbb66bafcd7 | quote: | Auth Required | No | Yes ($300/mo) |
  - [1] 2026-11-02: Free API rate limit is only called standard, and it has 31 endpoints | capture: sha256:cb0a290ffb958a034d57858aeb24aebb2711aebfe9f19a33cd042dbb66bafcd7 | quote: | Rate Limit | Standard | Higher |
  - [1] 2026-11-02: there are only two tiers, free with no key and the API plan | capture: sha256:cb0a290ffb958a034d57858aeb24aebb2711aebfe9f19a33cd042dbb66bafcd7 | quote: There are only two tiers: free (no key) and the API plan.
  - [2] 2026-11-02: the API plan is 1,000 requests a minute and 1M calls a month | capture: sha256:79641101de32f987e8f611e073470072c1bb6162365157d5cf6214e89fe529f0 | quote: Increased rate limit: 1,000 requests / minute, 1M calls / month
  - [2] 2026-11-02: overage beyond the API plan is USD 0.60 per 1,000 calls | capture: sha256:79641101de32f987e8f611e073470072c1bb6162365157d5cf6214e89fe529f0 | quote: $0.60 per 1,000 calls beyond the 1M limit
  - [3] 2026-11-02: CSV dataset downloads are for Pro and API subscribers | capture: sha256:a43a039412c0140eef82486410aeba1aa74e28c44d531becf248aa9d7a4e548a | quote: DefiLlama data is available to subscribers of our Pro and API plans.
  - probe:https://api.llama.fi/tvl/uniswap 2026-11-03: a keyless TVL call answered HTTP 200 | capture: sha256:9c8e8b74ad3c6c890d6eba50d8668a2eed5dc75cd6a4ea0ae2473c9e43dad043 | quote: "status": 200
- sources:
  - [1] https://api-docs.defillama.com/llms.txt
  - [2] https://defillama.com/subscription
  - [3] https://defillama.com/downloads
