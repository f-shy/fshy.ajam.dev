# currencyapi

> currencyapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/currencyapi/ | JSON https://fshy.ajam.dev/api/v1/entity/currencyapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## currencyapi (currencyapi.com)

- `data-apis/currencyapi-com` | qualifies-with-caveat | evidence documented | binding volume-quota | category currency exchange rate API (fiat, crypto and metals, with history back to 1999) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:51.279Z (live) | stale on 2026-12-03
- url https://currencyapi.com/pricing/
- free tier: Free plan, USD 0, no card: 300 requests a month, 1 API key, 10 requests a minute, daily rate updates, latest and historical rates back to 1999; private use only. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Only successful calls count against the quota; validation errors and errors on the vendor side do not. Each date of a historical call costs one request, and one call takes up to 31 dates. The convert endpoint starts on Small at USD 9.99 a month for 15,000 requests; the range endpoint (JSON, CSV or Excel time series) starts on Medium at USD 39.99 a month.
- per-object cap: up to 31 dates in one historical call; each date costs one request | source: [2]
- retention: not applicable
- egress: not metered in bytes; the 300 requests a month bound what a free key can pull | metered: no | source: [1]
- identity: email | detail: Sign-up by email, or Google, GitHub or GitLab sign-in; the pricing page says no credit card is required. The email form has no field list in the captured text, so its fields are unverified.
- interface: rest
- limits:
  - volume-quota (binding): 300 requests a month on the Free plan [1]
  - request-rate: 10 requests a minute on the Free plan, then HTTP 429 until the end of the minute [3]
  - per-object-cap: up to 31 dates per historical call, each date one request [2]
- limits note: Bulk path: none on the free plan; the range endpoint (time series, CSV) starts on Medium. A free key can pull at most 300 dates a month through the historical endpoint.
- binding note: 300 requests a month ends first: the 10 a minute rate would spend it in 30 minutes.
- interface detail: GET https://api.currencyapi.com/v3/latest and /v3/historical with the key in the apikey header or parameter; json, csv or xlsx output on the data endpoints
- endpoint: part of interface detail
- tooling: curl or any HTTP client
- composes with: 300 requests a month is enough for a daily latest-rate pull and a few hundred dated lookups. For a monthly history pull, one historical call takes 31 dates at 31 requests.
- reliability: Past the monthly quota or the per-minute rate the API answers HTTP 429; the free plan's minute headers count per gateway node, so the limit is 5 on each of two nodes.
- notes: Free requests: 300 a month. Rate limit: 10 requests a minute. Bulk path: none on the free plan; up to 31 dates a historical call within the 300 requests.
- evidence note: Quota, rate, history and licence fields are read from first-party pricing, rate-limit and docs pages. No key was created, so no call was made against the quota.
- extras:
  - bulk_path: none on the free plan; up to 31 dates per historical call, each one request
  - free_requests: 300 a month, 10 a minute
  - history_depth: daily rates back to 1999 on every plan
- evidence:
  - [1] 2026-11-02: the free plan is 300 requests a month, 10 a minute, for private use, with no card | capture: sha256:ecf5459a87da5bcb442c0e6134fa85147f10eea501bb7355f28198e291a25b01 | quote: 300 requests a month, 1 API key, daily rate updates, 10 requests per minute, latest rates and historical rates. It is for private use only and needs no credit card.
  - [1] 2026-11-02: the plan table gives 300 requests a month for Free | capture: sha256:ecf5459a87da5bcb442c0e6134fa85147f10eea501bb7355f28198e291a25b01 | quote: | Requests per month | 300 | 15,000 | 600,000 | 1,700,000 | More than 1,700,000 |
  - [1] 2026-11-02: the free plan includes historical rates back to 1999 | capture: sha256:ecf5459a87da5bcb442c0e6134fa85147f10eea501bb7355f28198e291a25b01 | quote: Every plan includes historical exchange rates back to 1999, including the Free plan.
  - [1] 2026-11-02: the convert endpoint is not on the free plan | capture: sha256:ecf5459a87da5bcb442c0e6134fa85147f10eea501bb7355f28198e291a25b01 | quote: | Convert endpoint (`/v3/convert`) | Not included | Included | Included | Included | Included |
  - [1] 2026-11-02: the range and time series endpoint starts on Medium | capture: sha256:ecf5459a87da5bcb442c0e6134fa85147f10eea501bb7355f28198e291a25b01 | quote: | Range / time series (`/v3/range`, CSV) | Not included | Not included | Included | Included | Included |
  - [1] 2026-11-02: Small is USD 9.99 a month and Medium USD 39.99 a month | capture: sha256:ecf5459a87da5bcb442c0e6134fa85147f10eea501bb7355f28198e291a25b01 | quote: | Price, billed monthly | $0 | $9.99/mo | $39.99/mo | $79.99/mo | On request |
  - [3] 2026-11-02: the free plan has a 10 requests a minute limit | capture: sha256:bec1e31c984778ed051bbce06af3ba6d3e09d07303d586c0c2fde30cc6509471 | quote: We also enforce a minute rate limit on the free plan: up to 10 requests per minute.
  - [3] 2026-11-02: only successful calls count against the quota | capture: sha256:bec1e31c984778ed051bbce06af3ba6d3e09d07303d586c0c2fde30cc6509471 | quote: Only successful calls count against your quota.
  - [3] 2026-11-02: past the monthly quota the API answers 429 until the end of the month | capture: sha256:bec1e31c984778ed051bbce06af3ba6d3e09d07303d586c0c2fde30cc6509471 | quote: the API returns a `429` HTTP status code, and you either need to upgrade your plan or wait until the end of the month.
  - [3] 2026-11-02: the minute limit is 5 on each of two gateway nodes | capture: sha256:bec1e31c984778ed051bbce06af3ba6d3e09d07303d586c0c2fde30cc6509471 | quote: with our two gateway nodes that makes the 10 requests per minute of the free plan.
  - [2] 2026-11-02: each date of a historical call costs one request | capture: sha256:9fcca4bffc8bd91e7bea561d7b69761b9ae338e9ca0a97b7f309c6a06cf997ef | quote: Every date costs one request of your quota, as it would on its own
  - [2] 2026-11-02: a historical call takes up to 31 dates | capture: sha256:9fcca4bffc8bd91e7bea561d7b69761b9ae338e9ca0a97b7f309c6a06cf997ef | quote: up to 31 dates, comma-separated
  - [2] 2026-11-02: historical data reaches back to 1999 | capture: sha256:9fcca4bffc8bd91e7bea561d7b69761b9ae338e9ca0a97b7f309c6a06cf997ef | quote: Data are available all the way back to 1999.
  - [1] 2026-11-02: the free plan needs no card | capture: sha256:ecf5459a87da5bcb442c0e6134fa85147f10eea501bb7355f28198e291a25b01 | quote: No credit card required
  - [4] 2026-11-02: the register page offers Google sign-in | capture: sha256:202889407969df1c1db74e1174757d59dcbff814e490902e90341d98a2db4382 | quote: Sign up with Google
  - [4] 2026-11-02: the register page offers GitLab sign-in | capture: sha256:202889407969df1c1db74e1174757d59dcbff814e490902e90341d98a2db4382 | quote: Sign up with GitLab
  - [4] 2026-11-02: the register page offers email sign-up | capture: sha256:202889407969df1c1db74e1174757d59dcbff814e490902e90341d98a2db4382 | quote: Sign up with email
  - [5] 2026-11-02:  | capture: sha256:26a1ee927dd16c8602b2bb60f4ed6dcb714dfe0d69f824f2b274962505085523
  - [2] 2026-11-02: the historical endpoint answers in json, csv or xlsx | capture: sha256:9fcca4bffc8bd91e7bea561d7b69761b9ae338e9ca0a97b7f309c6a06cf997ef | quote: `json` (default), `csv` or `xlsx`.
  - [6] 2026-11-02: the key goes in the apikey header or parameter | capture: sha256:25418f4887f711d6a4f28ad0ba904de4aab20381cc4bf7639337269319051f66 | quote: Send the key in the `apikey` header, or as the `apikey` query parameter
- sources:
  - [1] https://currencyapi.com/pricing/
  - [2] https://currencyapi.com/docs/historical/
  - [3] https://currencyapi.com/docs/rate-limit/
  - [4] https://app.currencyapi.com/register
  - [5] https://currencyapi.com/terms-of-service/
  - [6] https://currencyapi.com/llms.txt
