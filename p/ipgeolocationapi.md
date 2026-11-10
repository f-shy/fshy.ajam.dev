# ipgeolocationapi.io

> ipgeolocationapi.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipgeolocationapi/ | JSON https://fshy.ajam.dev/api/v1/entity/ipgeolocationapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipgeolocationapi.io

- `data-apis/ipgeolocationapi-io` | qualifies-with-caveat | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://ipgeolocationapi.io/pricing
- free tier: Free plan, USD 0: 5,000 requests a day with no key, no account and no credit card, counted per caller IP address and reset at 00:00 UTC; country, city, region, ASN, timezone and currency data as JSON, XML or CSV | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Starter is USD 19 a month for 600,000 requests, Business USD 39 for 3,000,000 and Max USD 99 for 10,000,000. At the cap the API answers HTTP 429 with Retry-After; nothing is billed unless an opt-in surcharge is switched on.
- per-object cap: one IP address per request on the Free plan; the bulk endpoint takes 100 IPs a call on Business and Max | source: [1]
- retention: not applicable: a lookup API; keyless lookups are not stored by the service | source: [2]
- egress: not applicable: JSON, XML and CSV answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: no key, no account and no credit card for the free tier; an API key from an account console is needed only for the security, company and bulk features
- interface: rest
- limits:
  - volume-quota (binding): 5,000 requests a day per caller IP address, reset at 00:00 UTC; HTTP 429 with Retry-After past it [3]
  - per-object-cap: one IP per request on the Free plan; 100 IPs per call on the bulk endpoint (Business and Max) [1]
- binding note: 5,000 requests a day per caller IP is the only published cap of the free tier; no per-second rate is stated.
- interface detail: GET https://ipgeolocationapi.io/{ip} answers JSON, XML or CSV for an IPv4 or IPv6 address or a hostname, and GET / answers for the caller; paid features take a key in the X-API-Key header or the key parameter
- endpoint: part of interface detail
- tooling: any HTTP client; every answer carries X-RateLimit-Limit, X-RateLimit-Remaining and Retry-After headers, and ?rate=1 puts the quota in the JSON body
- composes with: 5,000 keyless lookups a day per caller IP with city, ASN, timezone and currency in one answer. Bulk path: the bulk endpoint (100 IPs a call) and 100,000-row async jobs on Business, USD 39 a month; city, ASN and security database snapshots (CSV, MMDB) on Max, USD 99 a month, or as an add-on.
- reliability: the origin answered HTTP 502 Bad gateway on /pricing at 10:18 and 15:21 UTC and on /8.8.8.8 at 15:21 UTC on 2026-11-02, so no keyless lookup could be completed; past the daily cap the API answers HTTP 429 with Retry-After
- notes: Free requests: 5,000 a day per caller IP, no key. Rate limit: the daily cap with HTTP 429 and Retry-After; no per-second rate is stated. The FAQ says keyless lookups are not stored by the service. Bulk path: the bulk endpoint and async jobs on Business and Max, CSV and MMDB snapshots on Max.
- evidence note: Pricing, documentation, FAQ and terms text was read on 2026-11-02 from stored copies of the pages, because the origin answered HTTP 502 to every direct and pinned read; the free-tier numbers are the vendor's own, and no keyless lookup could be exercised. The Free plan card lists Threat detection and Bulk endpoint, while the comparison table and the documentation make them paid features; the table is followed here. A live keyless lookup with its rate-limit headers would move it to measured.
- extras:
  - bulk_path: bulk endpoint (100 IPs a call) and async jobs on Business and Max; CSV and MMDB snapshots on Max
  - free_requests: 5,000 a day per caller IP, no key
- evidence:
  - [1] 2026-11-02: the Free plan needs no credit card and no key | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: Test and ship small projects. No credit card, no key needed to start.
  - [1] 2026-11-02: Free is 5,000 requests a day; Starter, Business and Max are monthly | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: | Requests | 5,000 / day | 600,000 / mo | 3,000,000 / mo | 10,000,000 / mo |
  - [3] 2026-11-02: the Free plan costs USD 0 and allows 5,000 a day | capture: sha256:f1215c8c3b90f767d5a6cca28b6dd3ea0ffaf4ce1b02bdc53d9e552f933979c4 | quote: | Free | $0 | 5,000/day | , | , |
  - [3] 2026-11-02: the daily cap is counted per caller IP and resets at 00:00 UTC | capture: sha256:f1215c8c3b90f767d5a6cca28b6dd3ea0ffaf4ce1b02bdc53d9e552f933979c4 | quote: The free tier allows 5,000 requests per day, counted per client IP and reset at 00:00 UTC.
  - [3] 2026-11-02: rate-limit headers on every answer and an opt-in quota field in the body | capture: sha256:f1215c8c3b90f767d5a6cca28b6dd3ea0ffaf4ce1b02bdc53d9e552f933979c4 | quote: Every response carries `X-RateLimit-Limit`, `X-RateLimit-Remaining` and `Retry-After` headers. Add `?rate=1` to include quota inside the JSON body.
  - [1] 2026-11-02: past the cap the API answers HTTP 429 with Retry-After | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: Requests return HTTP 429 with a Retry-After header.
  - [1] 2026-11-02: the Free plan answers JSON, XML or CSV | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: - JSON, XML, CSV responses
  - [1] 2026-11-02: the Free plan includes timezone and currency data | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: - Timezone and currency data
  - [1] 2026-11-02: the first plan card lists threat detection and a bulk endpoint, which the comparison table marks No for Free | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: - IPv4 and IPv6 - Threat detection - Bulk endpoint
  - [1] 2026-11-02: the bulk endpoint of 100 IPs a call is Business and Max only | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: | Bulk endpoint (100/call) | No | No | Yes | Yes |
  - [1] 2026-11-02: CSV and MMDB database snapshots are included on Max only | capture: sha256:9c207299f9b18b7cef692253f0251b48f869048a50d2d1a6187d570f1b225263 | quote: | DB snapshots (CSV, MMDB) | No | No | No | Included |
  - [3] 2026-11-02: a key is needed only for security, company and bulk features | capture: sha256:f1215c8c3b90f767d5a6cca28b6dd3ea0ffaf4ce1b02bdc53d9e552f933979c4 | quote: Paid features (security, company, bulk) need an API key from your account console.
  - [3] 2026-11-02: a plain GET with an IP, an IPv6 address or a domain name needs no key | capture: sha256:f1215c8c3b90f767d5a6cca28b6dd3ea0ffaf4ce1b02bdc53d9e552f933979c4 | quote: Send a GET request with an IPv4 address, IPv6 address or a domain name (we resolve it automatically). No API key, no signup:
  - [2] 2026-11-02: keyless lookups are not stored | capture: sha256:19eebc09e1f08475c981cfcaec8b63550f846570b4b3c37fbd20ce2176f3aa5e | quote: Do you store our lookups? Keyless traffic: no. Authenticated: aggregate counters, documented retention.
  - [2] 2026-11-02: the free tier is keyless with no card | capture: sha256:19eebc09e1f08475c981cfcaec8b63550f846570b4b3c37fbd20ce2176f3aa5e | quote: Is the free tier really free? Yes: 5,000 requests a day, keyless, forever. No card, no trial clock.
  - [4] 2026-11-02: free usage needs no account | capture: sha256:6510350181d350167f86cfe532db233f9c0789ec3ce4dc5d312822aae408f6e4 | quote: Free usage requires no account and is rate-limited per client.
  - probe:https://ipgeolocationapi.io/pricing 2026-11-02: the origin answered HTTP 502 on /pricing at 10:18 UTC on 2026-11-02 | capture: sha256:e45af30bfd339ddf829e96a4922a4e25a794cf904ddb611d104806429cb596fa | quote: "status": 502
  - probe:https://ipgeolocationapi.io/pricing 2026-11-02: the origin still answered HTTP 502 on /pricing at 15:21 UTC on 2026-11-02 | capture: sha256:0949e0670a8338938f2e0cca79f650fe315df6738a599d9280e1d89677fcf8ec | quote: "status": 502
  - probe:https://ipgeolocationapi.io/8.8.8.8 2026-11-02: the keyless lookup path /8.8.8.8 answered HTTP 502 at 15:21 UTC on 2026-11-02 | capture: sha256:313d3de2856f86bb52c171790e3c3b2c7513bcfd5dc9b23636fd65d6b62a6574 | quote: "status": 502
- sources:
  - [1] https://ipgeolocationapi.io/pricing
  - [2] https://ipgeolocationapi.io/faq
  - [3] https://ipgeolocationapi.io/docs
  - [4] https://ipgeolocationapi.io/terms
