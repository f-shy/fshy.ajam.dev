# CurrencyApi

> currencyapi.net | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/currencyapi-2/ | JSON https://fshy.ajam.dev/api/v1/entity/currencyapi-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CurrencyApi (currencyapi.net)

- `data-apis/currencyapi-net` | qualifies-with-caveat | evidence documented | binding volume-quota | category currency exchange rate API (fiat, 12 crypto assets and metals) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:51.279Z (live) | stale on 2026-12-03
- url https://currencyapi.net/pricing/
- free tier: Free plan, USD 0, no card: 500 monthly requests, 10 requests a minute, 1 API key, live rates updated every 60 minutes with a fixed base currency, no historical rates. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Crypto rates for 12 assets are in the same live rates call on every plan, the free plan included. Essential is USD 9.99 a month for 20,000 requests and adds convert, history from 2000, any base currency. The pricing page and the free-API page disagree on the free plan's feature bullets, because the free-API page lost its check and cross marks in text; the pricing page and the FAQ on the free-API page both say live rates only.
- per-object cap: not stated | source: [1]
- retention: not applicable
- egress: not metered in bytes; the 500 requests a month bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: The free-API page says to sign up with an email and that no credit card is required. The form fields are unverified: no copy of the sign-up page is in the sources.
- interface: rest
- limits:
  - volume-quota (binding): 500 monthly requests on the Free plan [1]
  - request-rate: 10 requests a minute on the Free plan [1]
- limits note: History: none on the free plan; history from 2000 starts on Essential and the timeframe range on StartUp. Bulk path: none on the free plan.
- binding note: 500 requests a month ends first: the 10 a minute rate would spend it in 50 minutes.
- interface detail: GET https://currencyapi.net/api/v2/rates?key=KEY&base=USD&output=JSON; JSON or XML
- endpoint: part of interface detail
- tooling: curl or any HTTP client; vendor SDKs for Python, Node.js, PHP and Go
- composes with: Hourly live fiat and crypto rates at 500 a month is about 16 a day, so an hourly poll does not fit; a few polls a day do.
- reliability: The docs list HTTP 429 among the error codes; the free-plan cut-off behaviour was not read.
- notes: Free requests: 500 a month. Rate limit: 10 requests a minute. No caching clause was found. Bulk path: none on the free plan; the timeframe range endpoint starts on StartUp.
- evidence note: Plan numbers come from the pricing page and the free-API FAQ. The sign-up form fields and the free plan's cut-off are unverified; no key was created.
- extras:
  - bulk_path: none on the free plan; /api/v2/timeframe starts on StartUp
  - free_requests: 500 a month, 10 a minute
  - history_depth: none on the free plan; from 2000 on Essential
- evidence:
  - [1] 2026-11-02: the free plan is 500 monthly requests | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: - 500 monthly requests
  - [1] 2026-11-02: the free plan is 10 requests a minute | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: - 10 requests per min
  - [1] 2026-11-02: free rates update every 60 minutes | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: - Updated every 60 minutes
  - [1] 2026-11-02: the free plan has no historical rates | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: - No Historical Rates
  - [1] 2026-11-02: the free plan has a fixed base currency | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: - Fixed base currency
  - [1] 2026-11-02:  | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb
  - [1] 2026-11-02: the free plan is not | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: No, our free plan is not permitted.
  - [1] 2026-11-02: Essential allows 20,000 monthly requests | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: - 20,000 monthly requests
  - [2] 2026-11-02: free sign-up is by email with no card | capture: sha256:dfa01239718b24f5f448348b68b0901cd81a607cd3450380d7232a301e159e5a | quote: Sign up with your email above - no credit card required.
  - [2] 2026-11-02: free accounts are limited to 10 a minute and 500 a month | capture: sha256:dfa01239718b24f5f448348b68b0901cd81a607cd3450380d7232a301e159e5a | quote: Yes, free accounts are limited to 10 requests per minute and 500 requests per month.
  - [2] 2026-11-02: the free plan has live rates only | capture: sha256:dfa01239718b24f5f448348b68b0901cd81a607cd3450380d7232a301e159e5a | quote: No. The free plan provides live rates only.
  - [3] 2026-11-02: live crypto rates are on the free plan | capture: sha256:01a73aef57b2c16fb0503625bfc42591747a351955ff8bd518f802674d7b5754 | quote: Live crypto rates are available on all plans including the free tier.
  - [3] 2026-11-02: the API covers 12 crypto assets | capture: sha256:01a73aef57b2c16fb0503625bfc42591747a351955ff8bd518f802674d7b5754 | quote: 12 crypto assets
  - [4] 2026-11-02:  | capture: sha256:867b2836ae7b473be2a03bc4db4e02d2017b2fe89b1c68a7b88b2394565ac946
  - [4] 2026-11-02:  | capture: sha256:867b2836ae7b473be2a03bc4db4e02d2017b2fe89b1c68a7b88b2394565ac946
  - [5] 2026-11-02: the timeframe range endpoint starts on StartUp | capture: sha256:cd067a8b702ccfbfa1facd88f029abaa761d1fdced37d7b0577e844ac6fce9e2 | quote: Perfect for chart data, backtesting ranges, compliance exports. Available on StartUp plans and above.
  - [1] 2026-11-02: Essential is USD 9.99 a month | capture: sha256:bf1fbdf3a2d0ffa4772a5a0182b1192ad118b4ac13b647f4a5c78e77eff504bb | quote: $9.99/month
  - [2] 2026-11-02: history from 2000 starts on Essential | capture: sha256:dfa01239718b24f5f448348b68b0901cd81a607cd3450380d7232a301e159e5a | quote: Historical exchange rate data — going back to January 1, 2000 (25+ years) — is available on Essential plans and above via the /api/v2/history and /api/v2/timeframe endpoints.
  - [2] 2026-11-02: the vendor provides SDKs for Python, Node.js, PHP and Go | capture: sha256:dfa01239718b24f5f448348b68b0901cd81a607cd3450380d7232a301e159e5a | quote: We provide SDKs for Python, Node.js, PHP, and Go.
- sources:
  - [1] https://currencyapi.net/pricing/
  - [2] https://currencyapi.net/free-exchange-rate-api/
  - [3] https://currencyapi.net/cryptocurrency-exchange-rate-api/
  - [4] https://currencyapi.net/terms/
  - [5] https://currencyapi.net/historical-exchange-rate-api/
