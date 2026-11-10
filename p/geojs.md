# GeoJS

> geojs.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/geojs/ | JSON https://fshy.ajam.dev/api/v1/entity/geojs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GeoJS

- `data-apis/geojs` | qualifies | evidence documented | binding none | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://www.geojs.io/
- free tier: free REST, JSON and JSONP IP geolocation with no key, HTTPS only, no rate limits (yet); data from MaxMind GeoLite | unit: unlimited | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: not stated
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no key and no account
- interface: rest
- binding note: no quota or rate limit is published
- interface detail: GET https://get.geojs.io/v1/ip/geo/{ip}.json (also country, ptr and the caller's own IP), CORS enabled
- endpoint: part of interface detail
- tooling: any HTTP client or a browser script tag
- composes with: keyless lookups with no stated rate limit over MaxMind GeoLite data; for large volumes the GeoLite databases themselves are the bulk route. Bulk path: none
- reliability: a one-person project behind Cloudflare; the no-rate-limit statement is qualified with yet
- notes: Free requests: no stated quota. Rate limit: none stated (yet). Bulk path: none.
- evidence note: the home page was quoted on 2026-10-30 and a keyless lookup answered HTTP 200; no volume was sent to test for an unstated limit.
- extras:
  - bulk_path: none
  - free_requests: no stated limit
- evidence:
  - [1] 2026-10-30: no rate limits are applied, for now | capture: sha256:d722061abf7ba8660fde3fc9b1e768e9f659bbe05a2c34a3397e664ce877f93a | quote: No rate limits (yet)
  - [1] 2026-10-30: the API is HTTPS only | capture: sha256:d722061abf7ba8660fde3fc9b1e768e9f659bbe05a2c34a3397e664ce877f93a | quote: HTTPS only
  - [1] 2026-10-30: the data comes from MaxMind GeoLite | capture: sha256:d722061abf7ba8660fde3fc9b1e768e9f659bbe05a2c34a3397e664ce877f93a | quote: as all GeoIP data is sourced from their GeoLite database
  - [1] 2026-10-30: the API host | capture: sha256:d722061abf7ba8660fde3fc9b1e768e9f659bbe05a2c34a3397e664ce877f93a | quote: https://get.geojs.io/v1/ip/geo.js
  - [1] 2026-10-30: GeoJS is a one-person project | capture: sha256:d722061abf7ba8660fde3fc9b1e768e9f659bbe05a2c34a3397e664ce877f93a | quote: GeoJS is made with by [jloh](https://jloh.co/).
  - probe:https://get.geojs.io/v1/ip/geo/8.8.8.8.json 2026-10-30: a keyless lookup answered | capture: sha256:28a80940384cd9d04b34c0a375abdddcf633ff776adc4c14a88379df1ce27ffc | quote: "country_code":"US"
- sources:
  - [1] https://www.geojs.io/
