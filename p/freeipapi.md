# FreeIPAPI

> freeipapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freeipapi/ | JSON https://fshy.ajam.dev/api/v1/entity/freeipapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FreeIPAPI

- `data-apis/freeipapi` | qualifies | evidence documented | binding request-rate | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://freeipapi.com/
- free tier: free.freeipapi.com with no account or key: 60 requests a minute (10 per 10 seconds), servers in Europe only | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1]
- per-object cap: single lookups; bulk IP lookups are not on the free plan | source: [1]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no account, key or whitelisting on the free server
- interface: rest
- limits:
  - request-rate (binding): 60 requests a minute, 10 per 10 seconds [2]
- interface detail: GET or POST https://free.freeipapi.com/api/v1/json/{ip} (or xml), no key; paid servers use /api/ with a key or a whitelisted IP or domain
- endpoint: https://free.freeipapi.com/api/v1/
- tooling: any HTTP client
- composes with: 60 keyless lookups a minute from one address, every minute of the day. Bulk path: none free
- reliability: the free server runs in Europe only; a paid key does not lift limits on the free server
- notes: Free requests: 60 a minute, no account. Rate limit: 10 per 10 seconds. Bulk path: none free.
- evidence note: the home page and the API reference were quoted on 2026-10-30, and a keyless lookup answered HTTP 200; the rate limit was not exhausted.
- extras:
  - bulk_path: none free
  - free_requests: 60 a minute
- evidence:
  - [1] 2026-10-30: the free API needs no account and allows 60 a minute | capture: sha256:dc3bf72f7f92e42819b0613742fcfb1a7f422c8e1f2ab33aae21600591b51eef | quote: FreeIPAPI is still FREE with no account required! We're introducing subscriptions for users who want to increase the request limit to more than 60 requests per minute
  - [1] 2026-10-30: 60 requests a minute on the free plan | capture: sha256:dc3bf72f7f92e42819b0613742fcfb1a7f422c8e1f2ab33aae21600591b51eef | quote: Included: 60 Requests per minute
  - [1] 2026-10-30: free servers are in Europe only | capture: sha256:dc3bf72f7f92e42819b0613742fcfb1a7f422c8e1f2ab33aae21600591b51eef | quote: Included: Servers in Europe only
  - [1] 2026-10-30: no bulk lookups on the free plan | capture: sha256:dc3bf72f7f92e42819b0613742fcfb1a7f422c8e1f2ab33aae21600591b51eef | quote: Not included: Bulk IP Lookups
  - [1] 2026-10-30:  | capture: sha256:dc3bf72f7f92e42819b0613742fcfb1a7f422c8e1f2ab33aae21600591b51eef
  - [2] 2026-10-30: the free server allows 10 per 10 seconds, 60 a minute, with no authentication | capture: sha256:784013c3a9cadec2462aff6ed0a569fa098147d3f27285932842033c18167aec | quote: | Free | `free.freeipapi.com` | `/api/v1/` | None | 10 requests per 10 seconds, up to 60 per minute |
  - [2] 2026-10-30: the free endpoint and its lack of authentication | capture: sha256:784013c3a9cadec2462aff6ed0a569fa098147d3f27285932842033c18167aec | quote: Use `https://free.freeipapi.com/api/v1/` for single IP lookups in JSON or XML. No account, API key, or whitelisting is required.
  - [2] 2026-10-30: the free server keeps its limits | capture: sha256:784013c3a9cadec2462aff6ed0a569fa098147d3f27285932842033c18167aec | quote: A paid subscription or API key does not remove limits from requests sent to the free server.
  - probe:https://free.freeipapi.com/api/json/8.8.8.8 2026-10-30: a keyless lookup answered with city data | capture: sha256:d76010a2c45e299de745472e1bd030be20608bc722253b963041dcbee04c2292 | quote: "cityName":"Mountain View"
- sources:
  - [1] https://freeipapi.com/
  - [2] https://freeipapi.com/docs/api-reference/api-introduction
