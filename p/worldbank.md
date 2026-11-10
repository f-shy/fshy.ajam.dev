# World Bank Open Data

> worldbank.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/worldbank/ | JSON https://fshy.ajam.dev/api/v1/entity/worldbank.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## World Bank Open Data (Indicators API v2)

- `debrid/world-bank-open-data` | qualifies | evidence measured | binding request-rate | category development statistics API | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation
- price USD 0
- free tier: 'API keys and other authentication methods are no longer necessary to access the API.' Nearly 16,000 time series indicators across over 45 databases, many series back over 50 years. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: No rate limit is published anywhere on the API documentation.
- per-object cap: not applicable: JSON or XML per call, with per_page up to 32,000 rows on some indicators. The responses measured here were 9,735-13,760 bytes each at per_page=50. | source: [2]
- retention: the indicator series are revised in place; there is no versioned snapshot endpoint documented | source: [1]
- egress: Free and unmetered. No key, no account. | metered: no | free allowance: no byte allowance published | source: [1]
- identity: anonymous | detail: No key: 'API keys and other authentication methods are no longer necessary'. Anonymous GET returned 200 and 324 bytes for per_page=1.
- interface: rest, cli
- limits:
  - request-rate (binding): none published; measured 24 requests in 2.061 s at 8 connections (about 18 requests/second over the request phase) with no 429, and 20 requests in 43.774 s sequentially (latency-bound at about 2.2 s per call) probe:https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=50
- binding note: The API returns about 11 KB per call, so 1 TiB would take roughly 95 million calls; per-call latency, not any byte quota, is what limits a day. Parallel calls help here, unlike on the file hosts.
- interface detail: GET https://api.worldbank.org/v2/country/{codes}/indicator/{code}?format=json&per_page=N&page=N; format=xml also accepted.
- endpoint: https://api.worldbank.org/v2/
- tooling: curl/python-requests; wbgapi and pandas-datareader wrap it. No SDK needed.
- composes with: The economic and social join keys for any national-level dataset; it is metadata-density, not byte-volume, so it pairs with a large byte source rather than replacing one.
- reliability: Sequential calls cost about 2.2 s each from this machine, so an unparallelised harvest spends its day in latency; the API answered all 44 calls made here without a single 429.
- notes: A useful contrast among debrid providers: on the file hosts, more connections made things slower; here eight connections made the same 24 calls 21 times faster than one. The difference is latency-bound JSON versus bandwidth-bound files.
- evidence note: 44 calls were made and counted, at 1 and 8 connections, with bytes per response recorded. What is not measured is the point at which throttling starts, because none was reached.
- extras:
  - one_conn_20_req_ms: 43774
  - eight_conn_24_req_ms: 2061
  - mean_bytes_per_response: 10615.8
  - observed_rps: 18.3
  - first_response_sha256: a9dc0be3cba1c4bff059bfe695824288b4b542ddf13bb529ee2582bf5bcdadc3
- evidence:
  - [1] 2026-10-23: 'API keys and other authentication methods are no longer necessary to access the API' and 'nearly 16,000 time series indicators'
  - probe:https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=50 2026-10-23: 20 sequential requests in 43,774 ms, 19x200 and 1 transport error, mean 10,615.8 bytes per response; sha256 of the first response a9dc0be3cba1c4bff059bfe695824288b4b542ddf13bb529ee2582bf5bcdadc3
  - probe:https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=50 (8 connections, 3 rounds) 2026-10-23: 24 requests in 2,061 ms wall, all 200, 9,735-13,760 bytes per response - no 429 at about 18 requests/second
- sources:
  - [1] https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation
  - [2] https://api.worldbank.org/v2/country/all/indicator/NY.GDP.MKTP.CD?format=json&per_page=50
