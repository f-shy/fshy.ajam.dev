# IPGEO

> techniknews.net | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/techniknews/ | JSON https://fshy.ajam.dev/api/v1/entity/techniknews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPGEO (api.techniknews.net)

- `data-apis/ipgeo-techniknews` | qualifies-with-caveat | evidence measured | binding none | category IP geolocation API | tier Free keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://api.techniknews.net/ipgeo/
- free tier: keyless GET /ipgeo/{ip} returns country, region, city, coordinates, timezone, currency, ISP, ASN and proxy and hosting flags as JSON; a lookup of 8.8.8.8 answered HTTP 200 with no key, no account and no credit card | unit: requests | metered on: unstated | read on: 2026-11-02 | source: [1] | note: unverified: no request quota, rate limit or terms page is published on the host; a public API directory describes it as unlimited and free.
- per-object cap: one IP address per request, in the URL path | source: [1]
- retention: not applicable: a lookup API; answers are cached for 900 seconds (cache-control max-age=900; cached true in the body) | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: no key, account or header: a plain GET answered HTTP 200
- interface: rest
- limits:
  - request-rate: unverified: no rate limit or quota is published on the host [1]
- binding note: no limit is published, so none could be named; the service caches answers for 900 seconds.
- interface detail: GET https://api.techniknews.net/ipgeo/{ip} answers JSON with Access-Control-Allow-Origin *; the host root lists IP, IPgeo, Radiodata and Speedtest endpoints
- endpoint: part of interface detail
- tooling: any HTTP client; the JSON field names follow the ip-api.com shape (status, country, countryCode, regionName, city, zip, lat, lon, timezone, isp, org, as)
- composes with: Free keyless IP to location, ISP, ASN and hosting-flag lookups with no published quota; one IP per call. Bulk path: none listed.
- reliability: a lookup of 8.8.8.8 answered HTTP 200 in about 560 ms and the answer was served from a cache (cached true); no rate-limit header is returned
- notes: Free requests: no quota stated on the host (a public API directory says unlimited). Rate limit: not stated. The service caches answers for 900 seconds. Bulk path: none listed.
- evidence note: One keyless lookup of 8.8.8.8 was probed on 2026-11-02 and the host root page was read; no quota, rate limit or terms page exists on the host, so those values stay unverified.
- extras:
  - bulk_path: none listed
  - free_requests: no quota stated
- evidence:
  - [1] 2026-11-02: the API host lists the IPgeo endpoint | capture: sha256:a5f66413f55f70d67668df005fa832e21e7e22d588949fd25da200d65c595edb | quote: [IPgeo - get IP-data](https://api.techniknews.net/ipgeo/)
  - probe:https://api.techniknews.net/ipgeo/8.8.8.8 2026-11-02: a keyless GET of /ipgeo/8.8.8.8 answered HTTP 200 | capture: sha256:23897c1b643e3064a4f4dace788b4c6237024871d5b3135f659223761fa295be | quote: "status": 200
  - probe:https://api.techniknews.net/ipgeo/8.8.8.8 2026-11-02: the answer carries a location with country and country code | capture: sha256:87682429d3686c52b2e8a05ddf74a1f508c1d0eb4575abe470c2beca36bc51c8 | quote: "status":"success","continent":"North America","country":"United States","countryCode":"US"
  - probe:https://api.techniknews.net/ipgeo/8.8.8.8 2026-11-02: the answer carries ISP, organisation and ASN | capture: sha256:87682429d3686c52b2e8a05ddf74a1f508c1d0eb4575abe470c2beca36bc51c8 | quote: "isp":"Google LLC","org":"Google Public DNS","as":"AS15169 Google LLC"
  - probe:https://api.techniknews.net/ipgeo/8.8.8.8 2026-11-02: the answer carries mobile, proxy and hosting flags | capture: sha256:87682429d3686c52b2e8a05ddf74a1f508c1d0eb4575abe470c2beca36bc51c8 | quote: "mobile":false,"proxy":true,"hosting":true
  - probe:https://api.techniknews.net/ipgeo/8.8.8.8 2026-11-02: the answer is served from a cache with a cache timestamp | capture: sha256:87682429d3686c52b2e8a05ddf74a1f508c1d0eb4575abe470c2beca36bc51c8 | quote: "cached":true,"cacheTimestamp":1793577857
  - probe:https://api.techniknews.net/ipgeo/8.8.8.8 2026-11-02: the answer is cacheable for 900 seconds | capture: sha256:23897c1b643e3064a4f4dace788b4c6237024871d5b3135f659223761fa295be | quote: "cache-control": "max-age=900"
  - probe:https://api.techniknews.net/ipgeo/8.8.8.8 2026-11-02: the answer allows cross-origin reads | capture: sha256:23897c1b643e3064a4f4dace788b4c6237024871d5b3135f659223761fa295be | quote: "access-control-allow-origin": "*"
  - [2] 2026-11-02: a third-party API directory describes the endpoint as an unlimited free IP address API | capture: sha256:2275585bfa9f0f687ef1cba4918c22249deb7bebaaede534ec38325313c9c0af | quote: Unlimited free IP Address API with useful information
- sources:
  - [1] https://api.techniknews.net/
  - [2] https://openpublicapis.com/api/ipgeo
