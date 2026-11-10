# HackMyIP

> hackmyip.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hackmyip/ | JSON https://fshy.ajam.dev/api/v1/entity/hackmyip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HackMyIP

- `data-apis/hackmyip` | qualifies | evidence measured | binding request-rate | category IP geolocation API | tier Free keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://hackmyip.com/api
- free tier: free keyless API with no signup: 100 requests a minute per IP address on /api (X-RateLimit-Limit 100 over a 60-second window) and 60 a minute on /api/v1; IP geolocation, ISP, ASN and privacy flags as JSON; POST /api/bulk takes up to 50 IPs | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: no daily or monthly quota is stated; past the per-minute limit the API answers HTTP 429 with Retry-After.
- per-object cap: POST /api/bulk takes up to 50 IPs in one request; GET /api/lookup takes one | source: [2]
- retention: not applicable: a lookup API; answers are cacheable for an hour | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: no signup, no key and no authentication
- interface: rest
- limits:
  - request-rate (binding): 100 requests a minute per IP address on /api (X-RateLimit-Limit 100, window 60 seconds); 60 a minute on /api/v1 [1]
  - per-object-cap: 50 IPs per POST /api/bulk request [2]
- binding note: the per-minute limit per IP address is the only published cap; no daily or monthly quota is stated.
- interface detail: GET https://hackmyip.com/api/lookup?ip={ip} and GET /api/v1/ip/{ip} answer JSON with CORS enabled; POST /api/bulk takes a JSON body with an ips array; GET /api/ip answers for the caller
- endpoint: part of interface detail
- tooling: any HTTP client; X-RateLimit-Limit, X-RateLimit-Remaining and X-RateLimit-Window headers on every answer; an npm package named hackmyip is offered
- composes with: Keyless city, ISP, ASN and VPN or datacenter flags from Cloudflare Workers at 100 requests a minute per IP. Bulk path: POST /api/bulk, 50 IPs a request, keyless, inside the same per-minute limit.
- reliability: past the per-minute limit the API answers HTTP 429 with Retry-After; if the upstream lookup is briefly unavailable it answers HTTP 503 with success false
- notes: Free requests: no quota stated; 100 a minute per IP on /api, 60 a minute on /api/v1. Rate limit: HTTP 429 with Retry-After. Bulk path: POST /api/bulk, up to 50 IPs a request, keyless.
- evidence note: A keyless lookup of 8.8.8.8 was probed on 2026-11-02 and returned HTTP 200 with X-RateLimit-Limit 100 and X-RateLimit-Window 60; the page states 100 a minute on /api and 60 a minute on /api/v1, and the limits were not exhausted.
- extras:
  - bulk_path: POST /api/bulk, up to 50 IPs a request, keyless
  - free_requests: 100 a minute per IP, no key
- evidence:
  - [1] 2026-11-02: the API needs no key and asks for under 100 requests a minute | capture: sha256:bbff4aac18ef4cf528cc2e18b8b542047b49d8e149d95b6b7cd430a30522cb7e | quote: No API key required. JSON response, CORS enabled. Please keep it under 100 requests per minute.
  - [1] 2026-11-02: the advertised limit is 100 a minute over 60 seconds; /api/v1 is capped at 60 a minute | capture: sha256:bbff4aac18ef4cf528cc2e18b8b542047b49d8e149d95b6b7cd430a30522cb7e | quote: Please keep it under 100 requests per minute, the limit our response headers advertise (`X-RateLimit-Limit: 100`, `X-RateLimit-Window: 60`). The `/api/v1/` endpoints are capped at 60 requests per minute.
  - [1] 2026-11-02: answers are cacheable for an hour | capture: sha256:bbff4aac18ef4cf528cc2e18b8b542047b49d8e149d95b6b7cd430a30522cb7e | quote: Results are cacheable for an hour.
  - [1] 2026-11-02: the bulk endpoint takes up to 50 IPs in one POST | capture: sha256:bbff4aac18ef4cf528cc2e18b8b542047b49d8e149d95b6b7cd430a30522cb7e | quote: Batch lookup up to 50 IPs in a single POST request. Faster than sequential /api/lookup calls.
  - [2] 2026-11-02: the bulk endpoint returns one result per IP, 50 IPs a request | capture: sha256:b7ea6a08377b003ab92caa4ae8143143e2ace91962dc877738221ec732cae55f | quote: takes up to 50 IPs in a single POST and returns a result per IP
  - [3] 2026-11-02: the v1 limit is 60 requests a minute per IP address | capture: sha256:33e0d084628edd59dacbf0a8c460aa56755ebbfc0fea805c85971d366eeeab4c | quote: 60 requests / minutePer IP address. Resets every 60 seconds. No burst limits.
  - [3] 2026-11-02: past the limit the API answers HTTP 429 with Retry-After | capture: sha256:33e0d084628edd59dacbf0a8c460aa56755ebbfc0fea805c85971d366eeeab4c | quote: 429 Too Many RequestsReturned when rate limit is exceeded. Includes Retry-After header.
  - [3] 2026-11-02: no signup and no key | capture: sha256:33e0d084628edd59dacbf0a8c460aa56755ebbfc0fea805c85971d366eeeab4c | quote: Free IP geolocation, DNS lookup, WHOIS, and HTTP header inspection API. No signup. No API key. Just send a request and get JSON back.
  - [4] 2026-11-02: the API needs no sign-up | capture: sha256:5692a92ae16bcfdab160af5c330481e778a2dd72a66e5f80859d09f57b0582a4 | quote: HackMyIP provides free network and privacy tools and a free API, with no sign-up required.
  - probe:https://hackmyip.com/api/lookup?ip=8.8.8.8 2026-11-02: a keyless GET of /api/lookup?ip=8.8.8.8 answered HTTP 200 | capture: sha256:851a614e3e60affbe722450618fd8d7ade7477aa68d3cd713d4d2f0c15a9a0c9 | quote: "status": 200
  - probe:https://hackmyip.com/api/lookup?ip=8.8.8.8 2026-11-02: the answer advertises a limit of 100 | capture: sha256:851a614e3e60affbe722450618fd8d7ade7477aa68d3cd713d4d2f0c15a9a0c9 | quote: "x-ratelimit-limit": "100"
  - probe:https://hackmyip.com/api/lookup?ip=8.8.8.8 2026-11-02: the limit window is 60 seconds | capture: sha256:851a614e3e60affbe722450618fd8d7ade7477aa68d3cd713d4d2f0c15a9a0c9 | quote: "x-ratelimit-window": "60"
  - probe:https://hackmyip.com/api/lookup?ip=8.8.8.8 2026-11-02: the answer carries a location for the looked-up IP | capture: sha256:5f5b1a6c9518d0c11332e4903da1ae3192a6a633124433e16df4b4b1cdde3272 | quote: "country_name": "United States"
- sources:
  - [1] https://hackmyip.com/api
  - [2] https://hackmyip.com/bulk-ip-lookup
  - [3] https://hackmyip.com/api-docs
  - [4] https://hackmyip.com/terms
