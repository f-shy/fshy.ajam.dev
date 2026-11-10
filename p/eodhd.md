# EOD Historical Data

> eodhd.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/eodhd/ | JSON https://fshy.ajam.dev/api/v1/entity/eodhd.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EOD Historical Data (EODHD)

- `data-apis/eodhd` | qualifies-with-caveat | evidence documented | binding request-rate | category market data API (end-of-day prices, splits, dividends, forex, crypto) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis
- free tier: Free plan: 20 API calls a day, plus 500 welcome-bonus calls, past year of data only, your own key and no credit card; up to 1,000 requests per minute | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Most calls cost 1 API call; intraday, technical and news cost 5, fundamentals and options 10, whole-exchange bulk 100. The daily count resets at midnight GMT. Bulk downloads and fundamentals are not on the Free plan. The first paid plan is EOD Historical All-World at USD 19.99 a month with 100,000 calls a day.
- per-object cap: not stated | source: [2]
- retention: not applicable | note: Free history is the past year of every ticker; paid plans give 30+ years.
- egress: not metered in bytes; the daily call count bounds a Free key | metered: no | source: [2]
- identity: email | detail: The sign-up page offers Google or GitHub sign-in; the Free plan needs no credit card per the vendor.
- interface: rest
- limits:
  - request-rate (binding): 20 API calls per day on the Free plan, reset at midnight GMT [2]
  - request-rate (binding): 1,000 requests per minute on every plan [2]
- limits note: Bulk path: the whole-exchange bulk API costs 100 calls and is not on the Free plan. History is the past year on Free. Storage terms: unverified, no page read states one.
- binding note: 20 calls a day is met long before the 1,000 per minute limit.
- interface detail: GET https://eodhd.com/api/eod/TICKER.US?api_token=TOKEN&fmt=json; a keyless call answered HTTP 401
- endpoint: part of interface detail
- tooling: curl or any HTTP client; Python and R libraries and Excel and Google Sheets add-ons exist
- composes with: Free end-of-day prices for a year of any ticker at 20 calls a day; Tiingo and Alpha Vantage cover the same ground.
- reliability: A call with no token answered HTTP 401.
- notes: Free key with a tiny daily count and one year of history. Bulk path: paid only. Storage terms: unverified.
- evidence note: Limits are read from vendor docs; a keyless call answered 401; the Free token was not exercised.
- extras:
  - bulk_path: whole-exchange bulk API at 100 calls, paid plans
  - history_depth: past year on Free; 30+ years on paid plans
- evidence:
  - [1] 2026-11-02: Free is 20 calls a day plus 500 bonus calls, past year | capture: sha256:da94fc9b7189a22eddd7099a0393fc00e7d252ea60ef644d01a70efdac8b6590 | quote: 20 API calls a day, plus 500 welcome-bonus calls. Past year of data.
  - [1] 2026-11-02: the Free plan needs no credit card | capture: sha256:da94fc9b7189a22eddd7099a0393fc00e7d252ea60ef644d01a70efdac8b6590 | quote: Your own key No credit card required
  - [2] 2026-11-02: Free plan is 20 API calls per day | capture: sha256:f79e0d45d6ef330918ae4af59969d677d655bc8d6b05475d9f55b108e2d6b6cf | quote: Free plan — 20 API calls per day.
  - [2] 2026-11-02: 1,000 requests per minute limit | capture: sha256:f79e0d45d6ef330918ae4af59969d677d655bc8d6b05475d9f55b108e2d6b6cf | quote: the API accepts no more than
  - [2] 2026-11-02: whole-exchange bulk costs 100 calls | capture: sha256:f79e0d45d6ef330918ae4af59969d677d655bc8d6b05475d9f55b108e2d6b6cf | quote: | [Bulk API](https://eodhd.com/financial-apis/bulk-api-eod-splits-dividends), whole exchange | 100 |
  - [3] 2026-11-02: bulk downloads are not on the Free plan | capture: sha256:85252520445c3367a8eed39fff7485c4657b8d20d8e959c9fa8ad4f61941ff77 | quote: Bulk downloads are not part of the Free plan
  - [4] 2026-11-02: sign-up is by Google or GitHub | capture: sha256:e591a6f89d4ed13dc92595f466dbc1a314e1aa82b03029451d9e6e28d43e4447 | quote: Sign up with ... Google ... GitHub
  - probe:https://eodhd.com/api/eod/AAPL.US?fmt=json 2026-11-03: a call with no token answered HTTP 401 | capture: sha256:13f093e648134768556be2eb4ab65f903eb241be4edddf5ea15915d0bb1cf037 | quote: "status": 401
- sources:
  - [1] https://eodhd.com/financial-apis/quick-start-with-our-financial-data-apis
  - [2] https://eodhd.com/financial-apis/api-limits
  - [3] https://eodhd.com/financial-apis/bulk-api-eod-splits-dividends
  - [4] https://eodhd.com/register
