# BLS Public Data API

> bls.gov | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bls-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/bls-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BLS Public Data API (Bureau of Labor Statistics)

- `data-apis/bls-public-data-api` | qualifies | evidence documented | binding request-rate | category government economic data API (CPI, employment, wages, productivity time series) | tier Version 1.0 (unregistered)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://www.bls.gov/developers/api_faqs.htm
- free tier: Version 1.0, no registration: 25 queries a day, 25 series a query, 10 years a query, 50 requests per 10 seconds; Version 2.0 with a free registration key: 500 queries a day, 50 series, 20 years | unit: requests | metered on: request-count | read on: 2026-11-03 | source: [1] | note: Version 2.0 also returns net and percent changes, annual averages and series descriptions, and the key must be renewed at least once a year. A keyless v1 time-series call answered HTTP 200. The www.bls.gov pages answered HTTP 403 to an automated page fetch with no declared agent.
- per-object cap: 25 series per query unregistered, 50 registered | source: [1]
- retention: not applicable | note: 10 years per query unregistered, 20 registered.
- egress: not metered in bytes; the daily query count bounds a caller | metered: no | source: [1]
- identity: email | detail: Version 1.0 needs nothing. A Version 2.0 key needs an email address and an organization name and a CAPTCHA on the registration page, with the key emailed back.
- interface: rest
- limits:
  - request-rate (binding): 25 queries per day unregistered, 500 registered [1]
  - request-rate (binding): 50 requests per 10 seconds on both versions [1]
  - per-object-cap: 25 series and 10 years per query unregistered; 50 series and 20 years registered [1]
- limits note: Bulk path: flat files under download.bls.gov/pub/time.series/, one directory per survey, with no key.
- binding note: 25 queries a day unregistered, 500 registered, is met long before the 50 per 10 seconds rate.
- interface detail: GET or POST https://api.bls.gov/publicAPI/v1/timeseries/data/SERIESID with no key; v2 adds the registrationkey with the same signatures
- endpoint: part of interface detail
- tooling: curl or any HTTP client; sample code is published for several languages
- composes with: US labour and price series for free; they pair with FRED and Fiscal Data when a model mixes macro sources.
- reliability: Too many requests answer HTTP 429; the key expires unless renewed once a year.
- notes: Keyless v1 at 25 queries a day; a free emailed key raises it to 500. Bulk path: flat files. Storage terms: unverified.
- evidence note: Limits are read from the vendor FAQ and a keyless v1 call answered 200; the v2 key was not exercised.
- extras:
  - bulk_path: flat files at download.bls.gov/pub/time.series/
- evidence:
  - [1] 2026-11-03: daily query limit 500 registered and 25 unregistered | capture: sha256:515cba799e867c65fdcdbb6fbfd80cb1db4dcd439f8793115154ddf7d98993ff | quote: | Daily query limit | 500 | 25 |
  - [1] 2026-11-03: series per query limits | capture: sha256:515cba799e867c65fdcdbb6fbfd80cb1db4dcd439f8793115154ddf7d98993ff | quote: | Series per query limit | 50 | 25 |
  - [1] 2026-11-03: years per query limits | capture: sha256:515cba799e867c65fdcdbb6fbfd80cb1db4dcd439f8793115154ddf7d98993ff | quote: | Years per query limit | 20 | 10 |
  - [1] 2026-11-03: request rate is 50 per 10 seconds on both versions | capture: sha256:515cba799e867c65fdcdbb6fbfd80cb1db4dcd439f8793115154ddf7d98993ff | quote: | Request rate limit | 50 requests per 10 seconds | 50 requests per 10 seconds |
  - [1] 2026-11-03: registration asks for an email address and organization name plus a CAPTCHA | capture: sha256:515cba799e867c65fdcdbb6fbfd80cb1db4dcd439f8793115154ddf7d98993ff | quote: enter your email address and organization name. Complete the CAPTCHA.
  - [1] 2026-11-03: the registration must be renewed yearly | capture: sha256:515cba799e867c65fdcdbb6fbfd80cb1db4dcd439f8793115154ddf7d98993ff | quote: Users must renew registration with the BLS Public Data API at least once a year.
  - [2] 2026-11-03: flat-file survey directories are published for download | capture: sha256:6f2ed89dbcc939d6bbd3c6ea30c6a654c2c62b03c95a244262a9938b5734113f | quote: download.bls.gov - /pub/time.series/
  - probe:https://api.bls.gov/publicAPI/v1/timeseries/data/LNS14000000 2026-11-03: a keyless v1 call answered HTTP 200 | capture: sha256:f56cf09f9e9f3254bc4373dd24418b296e571512c197e300f6a15fe6529863d7 | quote: "status": 200
- sources:
  - [1] https://www.bls.gov/developers/api_faqs.htm
  - [2] https://download.bls.gov/pub/time.series/
