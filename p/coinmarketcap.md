# CoinMarketCap API

> coinmarketcap.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coinmarketcap/ | JSON https://fshy.ajam.dev/api/v1/entity/coinmarketcap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoinMarketCap API

- `data-apis/coinmarketcap` | qualifies-with-caveat | evidence documented | binding request-rate | category crypto market data API (listings, quotes, metadata, global metrics, DEX data) | tier Basic
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://coinmarketcap.com/api/pricing/
- free tier: Basic plan, free: 15,000 monthly call credits at 50 requests per minute, 1 API key, 1 year of daily quote history; a keyless public API on a shared per-IP pool also exists | unit: credits | metered on: request-count | read on: 2026-11-02 | source: [1] | note: The keyed host is pro-api.coinmarketcap.com with the X-CMC_PRO_API_KEY header; the keyless root adds /public-api and serves 18 standard and 17 DEX endpoints. A keyless call answered HTTP 429 with error 1022 on its first request from a residential ISP address. Builder is the first paid plan at USD 29 a month billed yearly for 150,000 credits.
- per-object cap: not stated | source: [1] | note: One currency conversion per call on Basic.
- retention: not applicable | note: Basic reaches 1 year of daily quotes and 1 month of intraday; all-time history starts at the Startup plan.
- egress: not metered in bytes; credits per call bound what a Basic key can pull | metered: no | source: [1]
- identity: email | detail: A Basic key needs a Developer Portal account: the sign-up form asks for Email, Name and Password and a plan choice; the vendor says no credit card. The keyless public API needs no account, but it answers 429 once its shared anonymous limit is reached.
- interface: rest
- limits:
  - request-rate (binding): 15,000 call credits per month on the Basic plan [1]
  - request-rate (binding): 50 requests per minute on the Basic plan, reset every 60 seconds [1]
  - per-ip-shaping: keyless public API: a shared IP-based rate pool, size not published; error 1022 once the anonymous limit is reached [2]
- limits note: Bulk path: none on Basic; all-time history and OHLCV start on paid plans. Storage terms: unverified, the commercial terms page rendered as an empty shell.
- binding note: 15,000 credits a month, with more than 1 credit for larger responses, is spent before the 50 requests per minute matter.
- interface detail: GET https://pro-api.coinmarketcap.com/... with the key in the X-CMC_PRO_API_KEY header; GET https://pro-api.coinmarketcap.com/public-api/... with no key
- endpoint: part of interface detail
- tooling: curl or any HTTP client; official Python, JavaScript and Go SDKs, an MCP server and an OpenAPI file are published
- composes with: A free key gives 15,000 credits a month of listings and quotes; CoinPaprika and CoinLore give keyless prices with no monthly key.
- reliability: Keyless calls share an IP pool and answered HTTP 429 (error 1022) on the first probe; keyed calls past the minute limit answer 429 and wait 60 seconds.
- notes: Free key with a monthly credit count; the keyless route is a shared pool that can already be exhausted. Bulk path: none on Basic. Storage terms: unverified.
- evidence note: Plan numbers are read from the vendor pricing and guide pages; a keyless probe measured the 429. The key was not exercised.
- extras:
  - bulk_path: none on Basic
  - history_depth: 1 year of daily quotes and 1 month of intraday on Basic
- evidence:
  - [3] 2026-11-02: Basic is the free authenticated tier with 15,000 credits and 50 requests per minute | capture: sha256:3f0c7136ca4fce3c450dc2a8e71fd985293d98f6924aee431d778a427fb0c044 | quote: The current pricing page lists Basic as the free authenticated tier with 15,000 monthly call credits and 50 requests per minute.
  - [1] 2026-11-02: a free plan by sign-up and a public API with no key | capture: sha256:5a5cf49697df492c2eb2bf9e76e0ed6cd08f3a28f4132bd77be7f50da48a578a | quote: Explore CoinMarketCap's API with our free plan by signing up, or just use our public API that doesn't require an API key.
  - [1] 2026-11-02: Basic daily quote history is 1 year | capture: sha256:5a5cf49697df492c2eb2bf9e76e0ed6cd08f3a28f4132bd77be7f50da48a578a | quote: Quotes Historical - Daily (1d–1y) ... 1 year
  - [1] 2026-11-02: Builder is USD 29 a month | capture: sha256:5a5cf49697df492c2eb2bf9e76e0ed6cd08f3a28f4132bd77be7f50da48a578a | quote: Builder ... $29/mo
  - [2] 2026-11-02: keyless requests share an IP-based pool | capture: sha256:3dacb206011005e5772fd237a1ca2cb649ba77065c1c4af3b38746fbc496d6c3 | quote: Keyless requests share an IP-based rate pool that keeps the public endpoint fast and stable for everyone.
  - [2] 2026-11-02: 18 standard and 17 DEX endpoints are keyless | capture: sha256:3dacb206011005e5772fd237a1ca2cb649ba77065c1c4af3b38746fbc496d6c3 | quote: 18 Standard API and 17 DEX endpoints, keyless.
  - [2] 2026-11-02: a free key needs no card | capture: sha256:3dacb206011005e5772fd237a1ca2cb649ba77065c1c4af3b38746fbc496d6c3 | quote: (no credit card) raises the rate limits
  - [4] 2026-11-02: the minute limit resets every 60 seconds and answers 429 | capture: sha256:ea150fcbc59b737a1c527795bd2bac6daed4e49990538f37f5d9a874319f19f1 | quote: This limit scales with the [usage tier](https://coinmarketcap.com/api/pricing/) and resets every 60 seconds.
  - [5] 2026-11-02: the sign-up form asks for email, name and password | capture: sha256:5f6b82bb0ec3d4104df57778674a18432d655db3b73d63dfc66d2893a717cbc6 | quote: Email ... Name ... Password
  - probe:https://pro-api.coinmarketcap.com/public-api/v2/simple/price?symbol=BTC&convert=USD 2026-11-03: the keyless call answered HTTP 429 | capture: sha256:51bb247bc3326745bdc781bd3e558fa2bd887c05be0f5ddb377d76b7d80203f6 | quote: "status": 429
  - probe:https://pro-api.coinmarketcap.com/public-api/v2/simple/price?symbol=BTC&convert=USD 2026-11-03: the keyless 429 names the anonymous limit and points to a free plan | capture: sha256:c482dfb44cc6aa20624d82986184f9c6f9d150242807725d7cb6bb324e89f9a5 | quote: You've reached the limit for anonymous access. Sign in to activate a free API plan or upgrade for higher limits.
- sources:
  - [1] https://coinmarketcap.com/api/pricing/
  - [2] https://coinmarketcap.com/api/documentation/pro-api-reference/keyless-public-api
  - [3] https://coinmarketcap.com/api/
  - [4] https://coinmarketcap.com/api/documentation/guides/errors-and-rate-limits/
  - [5] https://pro.coinmarketcap.com/signup
