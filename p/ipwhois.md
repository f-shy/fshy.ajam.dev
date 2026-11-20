# ipwhois.io

> ipwhois.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipwhois/ | JSON https://fshy.ajam.dev/api/v1/entity/ipwhois.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ipwhois.io (ipwho.is)

- `data-apis/ipwhois-io` | qualifies | evidence documented | binding volume-quota | category IP geolocation API | tier Free Endpoint
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://ipwhois.io/documentation
- free tier: free endpoint ipwho.is with no API key: 1,000 requests a day per client IP address; no bulk endpoint | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: requests from a website through CORS count per domain, not per visitor; Pro starts at USD 19.99 a month
- per-object cap: single lookups; the bulk endpoint (up to 100 IPs a call) is Pro only | source: [2]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: anonymous | detail: no API key and no account on the free endpoint
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests a day per client IP address; HTTP 429 for 24 hours past it [1]
- interface detail: GET https://ipwho.is/{ip} (HTTP or HTTPS), no key, JSON with location, connection, time zone and flag data
- endpoint: part of interface detail
- tooling: any HTTP client
- composes with: 1,000 keyless lookups a day from one address with city, ASN and time zone. Bulk path: none free
- reliability: past the daily limit the endpoint answers HTTP 429 until it restores itself after 24 hours
- notes: Free requests: 1,000 a day per client IP, no key. Rate limit: HTTP 429 for 24 hours past it. Bulk path: none free.
- evidence note: the documentation and pricing pages were quoted on 2026-10-30, and a keyless lookup answered HTTP 200; the daily limit was not exhausted.
- extras:
  - bulk_path: none free
  - free_requests: 1,000 a day per IP
- evidence:
  - [1] 2026-10-30: the free endpoint needs no key | capture: sha256:8efaad35981fc770edb1c68828378592b3323c28e9f6a70c7f533eced697c866 | quote: No API key required
  - [1] 2026-10-30: 1,000 requests a day per client IP | capture: sha256:8efaad35981fc770edb1c68828378592b3323c28e9f6a70c7f533eced697c866 | quote: The Free endpoint is limited to `1,000 requests per day` per client IP address.
  - [1] 2026-10-30: CORS requests count per domain | capture: sha256:8efaad35981fc770edb1c68828378592b3323c28e9f6a70c7f533eced697c866 | quote: When using CORS (JavaScript requests from your website), requests are counted per domain, not per individual visitor IP.
  - [1] 2026-10-30: HTTP 429 for 24 hours past the limit | capture: sha256:8efaad35981fc770edb1c68828378592b3323c28e9f6a70c7f533eced697c866 | quote: If you exceed the rate limit, further requests will return `HTTP 429 (Too Many Requests)`. Access will be restored automatically after 24 hours.
  - [2] 2026-10-30: the pricing page restates 1,000 a day | capture: sha256:734de8b9eb09863f656d15a1a62054087cb2b6dd44a14bb18cc74e64303f8734 | quote: 1,000 requests / day
  - [2] 2026-10-30: the free endpoint has no bulk endpoint | capture: sha256:734de8b9eb09863f656d15a1a62054087cb2b6dd44a14bb18cc74e64303f8734 | quote: No Bulk endpoint
  - [2] 2026-10-30: Pro starts at USD 19.99 a month | capture: sha256:734de8b9eb09863f656d15a1a62054087cb2b6dd44a14bb18cc74e64303f8734 | quote: Pro Endpointfrom $19.99/mo
  - [2] 2026-10-30: the Pro bulk endpoint takes up to 100 IPs | capture: sha256:734de8b9eb09863f656d15a1a62054087cb2b6dd44a14bb18cc74e64303f8734 | quote: Bulk Endpoint (up to 100 IPs / call)
  - probe:https://ipwho.is/8.8.8.8 2026-10-30: a keyless lookup succeeded | capture: sha256:f0ec9cec063457637a3d5ae56e6cc857d72fa549e949d1e65c378ad148e41b26 | quote: "success":true
- sources:
  - [1] https://ipwhois.io/documentation
  - [2] https://ipwhois.io/pricing
