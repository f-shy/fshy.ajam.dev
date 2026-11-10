# FRED

> stlouisfed.org | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stlouisfed/ | JSON https://fshy.ajam.dev/api/v1/entity/stlouisfed.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FRED (Federal Reserve Bank of St. Louis)

- `data-apis/fred` | qualifies | evidence documented | binding request-rate | category economic data API (FRED and ALFRED time series, releases, vintages)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:28:53.390Z (live) | stale on 2026-12-04
- url https://fred.stlouisfed.org/docs/api/fred/
- free tier: Free API key: no request count per day or month is stated; up to 120 requests per minute before HTTP 429; v1 series observations return up to 100,000 rows per call, and v2 release observations return up to 500,000 observations per call for all series on a release, with a cursor for the rest | unit: requests | metered on: request-count | read on: 2026-10-31 | source: [1] | note: The API is offered free; no paid plan is named. Not complying with the 120 per minute throttle can bring a temporary block. The terms reserve the right to set a bandwidth or transaction ceiling at any time. A single series also downloads as CSV with no key from fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES (GDP answered HTTP 200, 6419 bytes).
- per-object cap: 100,000 observations per v1 series/observations call; 500,000 observations per v2 release/observations call | source: [2]
- retention: not applicable
- egress: not metered in bytes; the 120 requests per minute bound what a key can pull | metered: no | source: [1]
- identity: email | detail: Every API request needs a key, and a key is requested from a fredaccount.stlouisfed.org account. The account asks only for a valid email address and a password, and is active as soon as the form is submitted; no card, no phone. The keyless fredgraph.csv download and the website need no account.
- interface: rest
- limits:
  - request-rate (binding): 120 requests per minute, then HTTP 429 and possibly a temporary block [1]
  - per-object-cap: 500,000 observations per v2 release/observations call, cursor paging for the rest [2]
  - per-object-cap: 100,000 observations per v1 series/observations call [3]
- limits note: Bulk path: API v2 fred/v2/release/observations returns every series on a release with its entire history, 500,000 observations a call with next_cursor paging; one series is also a keyless CSV at fredgraph.csv.
- binding note: No daily or monthly count is published, so the 120 per minute throttle is the only stated ceiling; v2 release pulls of 500,000 observations a call keep it far away.
- interface detail: v1: GET https://api.stlouisfed.org/fred/... with api_key (a 32-character lower-case key) as a query parameter, JSON or XML. v2: GET https://api.stlouisfed.org/fred/v2/release/observations with the key in an Authorization: Bearer header and next_cursor paging. A call with no key answered HTTP 400.
- endpoint: part of interface detail
- tooling: curl or any HTTP client; fredgraph.csv serves one series as CSV with no key
- composes with: Whole economic releases in one paged v2 pull at no cost; it pairs with a market source such as Tiingo or CoinGecko when macro series sit beside prices.
- reliability: Past 120 requests a minute the API answers HTTP 429, and ignoring the throttle can bring a temporary block; an error answer is an HTTP status with an XML or JSON body that carries the error.
- notes: Free with an email-only key, no stated daily or monthly count, and a documented bulk path (v2 release observations). The series notes name them.
- evidence note: The rate, the row caps and the account fields are documented on the FRED API and help pages. Probes measured that a keyless API call answers HTTP 400 and that fredgraph.csv serves GDP as CSV with no key. The 429 message text, any reset moment and the length of a temporary block need a key to measure (unverified: behind a sign-up).
- extras:
  - bulk_path: API v2 fred/v2/release/observations: all series on a release with full history, 500,000 observations per call, cursor paging
  - keyless_path: fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES returns one series as CSV with no key
- evidence:
  - [1] 2026-10-31: up to 120 requests per minute are allowed before HTTP 429, and ignoring the throttle can bring a temporary block | capture: sha256:a913528b88b24c286d01e03d06236796dd70da9b582e293534eeebbf96400a54 | quote: 429 Too Many Requests (Up to 120 requests per minute are allowed before being served a 429 error code. Not complying with the throttling can result in a temporary block.)
  - [4] 2026-10-31: every request needs an API key | capture: sha256:4548b785ab6a4a4a15bf62bf865d0f9a2ca4d3d7703db4681a8625618e4c064b | quote: All web service requests require an API key to identify requests.
  - [5] 2026-10-31: API use needs a registered key | capture: sha256:9862c1410ba1e74e25a1f5710cb0e64a461ca797db722c511b34a70c8d88de63 | quote: In order to use the FRED® API, you must have register for an API Key.
  - [6] 2026-10-31: the FRED API is offered free | capture: sha256:0dbe8b49a93477a64d8ed8a3e9e9f319d706386bae93a7274fb71bfd9d5f56de
  - [4] 2026-10-31: the v1 key is a 32-character lower-case string passed as api_key | capture: sha256:4548b785ab6a4a4a15bf62bf865d0f9a2ca4d3d7703db4681a8625618e4c064b | quote: The API key is set using the api\_key variable, a 32 character lower-cased alpha-numeric string.
  - [7] 2026-10-31: the account asks only for an email address and a password | capture: sha256:3b211191e6e5c6eb702d4c49a546e794b4656e7b3af4dd54db9d2c9c0d41f28a | quote: For a user account, we require only a valid email address and password of your choice.
  - [7] 2026-10-31: the account is active as soon as the form is submitted | capture: sha256:3b211191e6e5c6eb702d4c49a546e794b4656e7b3af4dd54db9d2c9c0d41f28a | quote: Your account will be activated immediately after submitting the form.
  - [8] 2026-10-31: the website shows data with no account | capture: sha256:849e6f1e27abac0693224cca61bed8ef17bc43bcd395e5cb083a89c6edcaad9f | quote: A user account is not needed to view data on [FRED](https://fred.stlouisfed.org/) website.
  - [9] 2026-10-31: API v2 retrieves all series on a release in bulk with the entire history | capture: sha256:41ee1db2423fbe762f0eb60b91b8ea9e77e4571959a66da05a7821287d2aca85 | quote: The FRED® API, Version 2 is ideal for anyone who is interested to retrieve observations for all series on a release in bulk and obtain the entire history.
  - [2] 2026-10-31: the v2 endpoint returns the observations of every series on a release | capture: sha256:f519b3aafb8bc3ffabcca236b26a31fe27cb714aaa53b3f4a05616627ef70205 | quote: Get the observations for all series on a release of economic data.
  - [2] 2026-10-31: a v2 call returns up to 500,000 observations | capture: sha256:f519b3aafb8bc3ffabcca236b26a31fe27cb714aaa53b3f4a05616627ef70205 | quote: - integer between 1 and 500000, optional, default: 500000
  - [10] 2026-10-31: v2 takes the key in a request header | capture: sha256:76dfaacc019109cb2bae75a08cf3b5fa92883b820d16ef09a622435611899a05 | quote: An API key must be specified in the request header in the following way:
  - [3] 2026-10-31: a v1 series/observations call returns up to 100,000 rows | capture: sha256:4b19fa58c81cb87985a8f5402ea041a573fa110502969b1b0f72b915aa7ee89f | quote: - integer between 1 and 100000, optional, default: 100000
  - [6] 2026-10-31:  | capture: sha256:0dbe8b49a93477a64d8ed8a3e9e9f319d706386bae93a7274fb71bfd9d5f56de | quote: - View, download, and print FRED content
  - probe:https://api.stlouisfed.org/fred/series/observations?series_id=GDP&file_type=json 2026-10-31: an API call with no key answered HTTP 400 | capture: sha256:27a7fa7677d85ac9c8186b256d1be9536b341a2ee9a49d9c5ab9e7e1e34e88a5 | quote: "status": 400
  - probe:https://api.stlouisfed.org/fred/series/observations?series_id=GDP&file_type=json 2026-10-31: the API refuses a call that carries no api_key | capture: sha256:da3c632f9a98b4c8f641de2b0763d513b4642316fe56d52d883002e011a892ff | quote: Variable api_key is not set.
  - probe:https://fred.stlouisfed.org/graph/fredgraph.csv?id=GDP 2026-10-31: fredgraph.csv answered HTTP 200 with no key | capture: sha256:82f459e71f9b9d34ff6f57fa64db27f21f5063b6693955cf4d95a5b586d77f5c | quote: "status": 200
  - probe:https://fred.stlouisfed.org/graph/fredgraph.csv?id=GDP 2026-10-31: the keyless CSV carries the GDP series with its dates | capture: sha256:209e45690e4a85a6e99578c0a2ad6f1860875f61824dd2f67f9cba25386abd9e | quote: observation_date,GDP
  - [1] 2026-11-02: 429 past 120 requests a minute, with a possible temporary block | capture: sha256:ff59aa7539e23db095b5b6ac60f1507ac03e382773359dafd70d3cc16f048c2f | quote: 429 Too Many Requests (Up to 120 requests per minute are allowed before being served a 429 error code. Not complying with the throttling can result in a temporary block.)
  - [1] 2026-11-02: an error answer is an HTTP status with an XML or JSON body | capture: sha256:ff59aa7539e23db095b5b6ac60f1507ac03e382773359dafd70d3cc16f048c2f | quote: If an error occurs, the web service will return an HTTP response with the error status code and an XML or JSON body containing the error.
  - [1] 2026-11-02: the 120 per minute throttle is documented | capture: sha256:ff59aa7539e23db095b5b6ac60f1507ac03e382773359dafd70d3cc16f048c2f | quote: 429 Too Many Requests (Up to 120 requests per minute are allowed before being served a 429 error code. Not complying with the throttling can result in a temporary block.)
  - [1] 2026-11-02: the 120 per minute throttle is unchanged | capture: sha256:ff59aa7539e23db095b5b6ac60f1507ac03e382773359dafd70d3cc16f048c2f | quote: 429 Too Many Requests (Up to 120 requests per minute are allowed before being served a 429 error code. Not complying with the throttling can result in a temporary block.)
- sources:
  - [1] https://fred.stlouisfed.org/docs/api/fred/errors.html
  - [2] https://fred.stlouisfed.org/docs/api/fred/v2/release_observations.html
  - [3] https://fred.stlouisfed.org/docs/api/fred/series_observations.html
  - [4] https://fred.stlouisfed.org/docs/api/api_key.html
  - [5] https://fred.stlouisfed.org/docs/api/terms_of_use.html
  - [6] https://fred.stlouisfed.org/legal/
  - [7] https://fredhelp.stlouisfed.org/fred/account/fred-account-features/register/
  - [8] https://fredaccount.stlouisfed.org/login/secure/
  - [9] https://fred.stlouisfed.org/docs/api/fred/v2/index.html
  - [10] https://fred.stlouisfed.org/docs/api/fred/v2/api_key.html
