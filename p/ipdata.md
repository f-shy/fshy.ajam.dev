# ipdata

> ipdata.co | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipdata/ | JSON https://fshy.ajam.dev/api/v1/entity/ipdata.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipdata (ipdata.free)

- `data-apis/ipdata` | qualifies | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://ipdata.co/pricing.html
- free tier: 1,000 city-level lookups a day with no API key, then country-level and ASN data without limit; no credit card | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: served at ipdata.free; paid plans start at USD 50 a month (Startup)
- per-object cap: not stated: single-IP lookups
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no key and no account on ipdata.free; the keyed api.ipdata.co answers 401 without a key
- interface: rest
- limits:
  - volume-quota (binding): 1,000 city-level lookups a day with no key, then country and ASN only [1]
- interface detail: GET https://ipdata.free/{ip} with no key, JSON with ip, city, region, country, latitude, longitude, asn, org, postal and timezone; RateLimit-Limit, RateLimit-Remaining and RateLimit-Reset headers on every answer
- endpoint: part of interface detail
- tooling: any HTTP client
- composes with: 1,000 city-level lookups a day with no account, then unlimited country and ASN answers; the keyed api.ipdata.co plans add threat and company data. Bulk path: none free
- reliability: past the daily city-level quota answers narrow to country and ASN fields rather than failing
- notes: Free requests: 1,000 city-level a day with no key, then unlimited country and ASN. Rate limit: none beyond the daily count; RateLimit headers report it. Bulk path: none free.
- evidence note: the pricing page was quoted on 2026-10-30, and a keyless lookup of ipdata.free answered HTTP 200 with RateLimit-Limit 1000; the keyed endpoint answered HTTP 401 without a key.
- extras:
  - bulk_path: none free
  - free_requests: 1,000 city-level a day, then unlimited country and ASN
- evidence:
  - [1] 2026-10-30: the free tier is 1,000 city-level a day, then country-level without limit, with no key | capture: sha256:552be6fff0a0a5bf901172f7a67f9cfb2228e2ce262278ecd01d1e84a99767f5 | quote: 1,000 city-level a day, then country-level without limit, no key
  - [1] 2026-10-30: country and ASN data continue without limit | capture: sha256:552be6fff0a0a5bf901172f7a67f9cfb2228e2ce262278ecd01d1e84a99767f5 | quote: You get 1,000 city-level lookups a day with no API key at all, and country and ASN data without limit after that.
  - [1] 2026-10-30: no card is needed | capture: sha256:552be6fff0a0a5bf901172f7a67f9cfb2228e2ce262278ecd01d1e84a99767f5 | quote: No credit card required
  - [1] 2026-10-30: Startup is USD 50 a month | capture: sha256:552be6fff0a0a5bf901172f7a67f9cfb2228e2ce262278ecd01d1e84a99767f5 | quote: Startup $50/ mo
  - probe:https://ipdata.free/8.8.8.8 2026-10-31: a keyless answer carried a 1000-request limit | capture: sha256:9acf8e6d9637158c4caa6ce887df0c6da310d241360f19ca7d6e7b95ceeeeb82 | quote: "ratelimit-limit": "1000"
  - probe:https://ipdata.free/8.8.8.8 2026-10-30: a keyless lookup answered with network data | capture: sha256:1f64611fea583482515c3e7861037a9aa72949cad58af3845806fde707cea520 | quote: "org": "Google LLC"
  - probe:https://api.ipdata.co/8.8.8.8 2026-10-30: the keyed endpoint refuses a keyless call | capture: sha256:2e796e4a24c88f85b7119a203f84c9b5ae28ae79d652999f456bf0cdf37c87cd | quote: You have not provided a valid API Key.
- sources:
  - [1] https://ipdata.co/pricing.html
