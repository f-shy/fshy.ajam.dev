# Messari

> blockworks.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blockworks/ | JSON https://fshy.ajam.dev/api/v1/entity/blockworks.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Messari (Blockworks Data API)

- `data-apis/messari` | paid-only | evidence documented | binding write-gated | category crypto market and onchain data API (assets, protocols, exchanges, timeseries) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://docs.blockworks.com/getting-started/authentication
- free tier: No free market-data allowance found: every call needs an API key, the Free plan lists no Assets endpoints, and most models need a paid plan; models of the unpaid access tier work with any valid key, and the docs do not list them | unit: none | metered on: none | read on: 2026-11-02 | source: [1] | note: The Data API enforces no rate limit and caches answers for 30 minutes. A keyless call to the tabular assets model answered HTTP 401 although the quickstart calls that model public; the legacy api.messari.io v1 endpoint answered 403 invalid auth mechanism. The Pro plan opens only the Assets endpoints; its price is not on the page.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes | metered: no | source: [1]
- identity: email | detail: A key is made in an account at app.blockworks.com; the sign-up form was not read, so what it asks is unverified: behind a sign-up.
- interface: rest
- limits:
  - write-gated (binding): paid or permission-gated access: a free-plan key answers 403 on models of the paid tier [1]
- limits note: Bulk path: the legacy Bulk API gave CSV or JSONL downloads by subscription tier; the current Datashares are sales-gated. Storage terms: unverified. Rate limit: none enforced by the Data API; the legacy docs gave 200 requests a minute for unpaid keys.
- binding note: Access to a model, not a request count, decides what a free key can read.
- interface detail: GET https://api.blockworks.com/query/tabular/... and /query/timeseries/... with the X-Blockworks-API-Key header; the legacy x-messari-api-key header is still accepted
- endpoint: part of interface detail
- tooling: curl or any HTTP client; an MCP server, warehouse Datashares and spreadsheet plugins are sales-gated
- composes with: Crypto market data from here needs a paid plan; CoinPaprika and CoinLore give keyless prices, DefiLlama keyless DeFi metrics.
- reliability: A keyless call answered HTTP 401 on the assets model the quickstart calls public; the legacy host answered 403.
- notes: No keyless route; a free key reaches only unpaid-tier models. Bulk path: sales-gated. Storage terms: unverified.
- evidence note: Access tiers and the pricing table are first-party; the keyless 401 contradicts the quickstart; the free key was not exercised.
- extras:
  - bulk_path: legacy Bulk API by tier; Datashares by sales
- evidence:
  - [1] 2026-11-02: unpaid-tier models work with any valid key | capture: sha256:1359bc90b5da1124b6cd4de373205c29e73e681201da5307235baaf6a7beefe2 | quote: Any request that carries a valid API key, on any plan.
  - [1] 2026-11-02: paid models refuse a free-plan key with 403 | capture: sha256:1359bc90b5da1124b6cd4de373205c29e73e681201da5307235baaf6a7beefe2 | quote: `403 this model requires a paid subscription` with a free-plan key
  - [1] 2026-11-02: the Data API enforces no rate limit and caches 30 minutes | capture: sha256:1359bc90b5da1124b6cd4de373205c29e73e681201da5307235baaf6a7beefe2 | quote: The Data API itself enforces no rate limit and sends no `RateLimit-*` or `Retry-After` headers.
  - [2] 2026-11-02: Pro opens only the Assets endpoints of the API | capture: sha256:ba3334e423dfa99270a1e1ec42da34af22477ebcd555709147a8eb406d4a449f | quote: Pro provides access to only the Assets endpoints in the API.
  - [3] 2026-11-02: legacy docs set unpaid keys at 200 requests a minute | capture: sha256:f2a86683d9b6aef28b6cca433a6af83e2be0452bf721965b90819a71b83e9d82 | quote: | Unpaid / Lite / Pro | 200 requests / min |
  - probe:https://api.blockworks.com/query/tabular/assets?pageSize=2 2026-11-02: a keyless call to the assets model answered HTTP 401 | capture: sha256:5ade858281fa1069b39c764932b32416c0c8d74e80257bf674c3ef647cf00b39 | quote: "status": 401
  - probe:https://api.blockworks.com/query/tabular/assets?pageSize=2 2026-11-02: the 401 says the model requires authentication | capture: sha256:47c9d8318f3d9d2f8618e615863608039ae059858e7372140c3113e07c95dfd5 | quote: this model requires authentication
- sources:
  - [1] https://docs.blockworks.com/getting-started/authentication
  - [2] https://app.blockworks.com/pricing
  - [3] https://docs.messari.io/api-reference/permissions
