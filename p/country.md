# Country

> country.is | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/country/ | JSON https://fshy.ajam.dev/api/v1/entity/country.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Country (api.country.is)

- `data-apis/country-is` | qualifies | evidence documented | binding request-rate | category IP geolocation API | tier Free hosted API
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://country.is/
- free tier: api.country.is is free with no key and no quotas; country by default, with city, continent, subdivision, postal, location and ASN on request; MaxMind GeoLite2 data refreshed every 24 hours | unit: unlimited | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: up to 100 addresses in one POST | source: [1]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no key and no account
- interface: rest
- limits:
  - request-rate (binding): 10 requests a second per IP [1]
  - per-object-cap: up to 100 addresses per POST [1]
- interface detail: GET https://api.country.is/{ip}, POST a JSON array of up to 100 addresses, ?fields= for the extra fields; HTTP 429 when the rate limit is exceeded
- endpoint: part of interface detail
- tooling: any HTTP client
- composes with: keyless lookups with no quota at up to 10 a second from one address, or 100 addresses a POST. Bulk path: the 100-address POST; the open-source server can also be run on a rented or free machine with MaxMind credentials, last after every hosted route
- reliability: infrastructure rate limit of 10 requests a second per IP answers HTTP 429; running since 2015
- notes: Free requests: no quota, no key. Rate limit: 10 a second per IP. Bulk path: POST of up to 100 addresses; the self-hosted Docker server is the last-resort route.
- evidence note: the home page was quoted on 2026-10-30 and a keyless lookup at api.country.is answered HTTP 200 on 2026-10-31.
- self hosted: no
- extras:
  - bulk_path: POST up to 100 addresses
  - free_requests: no quota
- evidence:
  - [1] 2026-10-30: the hosted API is free with no key and the app is open source | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: is free and requires no key. The app is open source and can be
  - [1] 2026-10-30: no quotas, 10 requests a second per IP | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: No quotas. Infrastructure rate-limits to 10 requests per second per IP to prevent abuse.
  - [1] 2026-10-30: a POST takes up to 100 addresses | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: Look up multiple IPs in one request. Send a JSON array of up to 100 addresses.
  - [1] 2026-10-30: extra fields are available | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: Add extra fields to any lookup: `city`, `continent`, `subdivision`, `postal`, `location`, `asn`.
  - [1] 2026-10-30: the data is MaxMind GeoLite2, updated daily | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: GeoLite2, updated daily.
  - [1] 2026-10-30: data refreshes every 24 hours | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: Returns metadata, including when the data was last updated. Data refreshes every 24 hours.
  - [1] 2026-10-30: running since 2015 | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: Country has been running since 2015.
  - [1] 2026-10-30: the server can be run on a user's own machine | capture: sha256:848fe7e24d15239e281d986b6fd1e1e98a9da97477ffb132e943e27bc20f2c7e | quote: Run your own instance with Docker.
  - [2] 2026-10-31: a keyless lookup answered | capture: sha256:d07eac53c3d1be503608d5ebf844ecce010d917245e4696e68abc99fc5e16f73 | quote: {"ip":"8.8.8.8","country":"US"}
- sources:
  - [1] https://country.is/
  - [2] https://api.country.is/8.8.8.8
