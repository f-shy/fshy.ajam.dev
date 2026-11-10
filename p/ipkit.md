# IPKit

> ipkit.dev | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipkit/ | JSON https://fshy.ajam.dev/api/v1/entity/ipkit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPKit (ipkit.dev)

- `data-apis/ipkit-dev` | qualifies-with-caveat | evidence measured | binding request-rate | category IP geolocation API | tier Free keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://ipkit.dev/docs
- free tier: keyless JSON lookups of any public IPv4 or IPv6 address at https://ipkit.dev/{ip}: 300 requests per 60 seconds per caller IP address, no key; location, ASN, organisation and VPN, proxy and Tor flags from an upstream Ipregistry key held by the operator | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: the limit applies to current-IP and arbitrary lookups; no SLA or uptime promise is published.
- per-object cap: one IP address per request (GET /{ip}); private and reserved ranges answer HTTP 400 RESERVED_IP | source: [1]
- retention: not applicable: a lookup API; specific-IP answers carry cache-control max-age=300 at the caller and s-maxage=3600 at the edge | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: callers send no API key
- interface: rest
- limits:
  - request-rate (binding): 300 requests per 60 seconds per caller IP address; HTTP 429 RATE_LIMITED with Retry-After 60 [1]
- binding note: the per-minute limit per caller IP is the only published cap; arbitrary lookups also depend on one operator-held upstream key and answer HTTP 503 LOOKUP_UNAVAILABLE without it.
- interface detail: GET or HEAD https://ipkit.dev/{ip} and /api/ip/{ip} answer ipkit.v1 JSON; GET /api/my-ip answers for the caller; OPTIONS answers CORS preflight with 204
- endpoint: part of the free tier
- tooling: any HTTP client; branch on the HTTP status and the ipkit.v1 object
- composes with: A keyless front end to Ipregistry data (source ipregistry) at 300 lookups a minute per caller IP, for scripts that need location, ASN and privacy flags with no account. Bulk path: none in the HTTP API.
- reliability: no SLA or uptime promise is published; arbitrary lookups need the operator's upstream key and answer HTTP 503 LOOKUP_UNAVAILABLE when it is missing; past the limit the API answers HTTP 429 with Retry-After 60
- notes: Free requests: the only published limit is 300 per 60 seconds per caller IP. Rate limit: HTTP 429 with Retry-After 60. Bulk path: none in the HTTP API.
- evidence note: A keyless lookup of 8.8.8.8 was probed on 2026-11-02 and returned HTTP 200 with source ipregistry; the 300 requests per 60 seconds limit is quoted from the documentation and was not exhausted.
- extras:
  - bulk_path: none in the HTTP API
  - free_requests: 300 per 60 seconds per caller IP
- evidence:
  - [1] 2026-11-02: callers send no API key | capture: sha256:28114e23d6df0c7a58d334600943cad5f084f0d3c906cca644dce601b6757029 | quote: Callers send no API key.
  - [1] 2026-11-02: no SLA is published | capture: sha256:28114e23d6df0c7a58d334600943cad5f084f0d3c906cca644dce601b6757029 | quote: There is no published SLA; use the service reasonably.
  - [1] 2026-11-02: the limit is 300 requests per 60 seconds per connecting IP | capture: sha256:28114e23d6df0c7a58d334600943cad5f084f0d3c906cca644dce601b6757029 | quote: Lookups are limited to 300 requests per 60 seconds per connecting client IP. The limit applies to current-IP and arbitrary lookups.
  - [1] 2026-11-02: HTTP 429 RATE_LIMITED is the answer past the limit | capture: sha256:28114e23d6df0c7a58d334600943cad5f084f0d3c906cca644dce601b6757029 | quote: The connecting client IP exceeded the lookup limit.
  - [1] 2026-11-02: arbitrary lookups need the operator's Ipregistry key and answer HTTP 503 without it | capture: sha256:28114e23d6df0c7a58d334600943cad5f084f0d3c906cca644dce601b6757029 | quote: Look up a specific public IPv4 or IPv6 address. Always JSON, even in a browser. Example: /8.8.8.8. Invalid syntax returns 400 INVALID_IP. Private and reserved ranges return 400 RESERVED_IP. Requires the Worker secret IPREGISTRY_API_KEY; otherwise 503 LOOKUP_UNAVAILABLE.
  - [1] 2026-11-02: specific-IP answers are public-cacheable | capture: sha256:28114e23d6df0c7a58d334600943cad5f084f0d3c906cca644dce601b6757029 | quote: Specific-IP lookups (/{ip} and /api/ip/{ip}) are Cache-Control: public, max-age=300, s-maxage=3600, stale-while-revalidate=86400.
  - probe:https://ipkit.dev/8.8.8.8 2026-11-02: a keyless GET of /8.8.8.8 answered HTTP 200 | capture: sha256:ffc759588344a99f2d10d86e7ff159519e18bf409102ca53f961675112581864 | quote: "status": 200
  - probe:https://ipkit.dev/8.8.8.8 2026-11-02: the answer comes from the Ipregistry data source | capture: sha256:e8d9dcf7b355ae1b6d9387d2acaf71bb93c65ccf2d50984d5c489cff747df0c4 | quote: "source": "ipregistry"
  - probe:https://ipkit.dev/8.8.8.8 2026-11-02: the answer carries an ASN | capture: sha256:e8d9dcf7b355ae1b6d9387d2acaf71bb93c65ccf2d50984d5c489cff747df0c4 | quote: "asn": "AS15169"
  - probe:https://ipkit.dev/8.8.8.8 2026-11-02: the answer carries the documented cache-control header | capture: sha256:ffc759588344a99f2d10d86e7ff159519e18bf409102ca53f961675112581864 | quote: "cache-control": "public, max-age=300, s-maxage=3600, stale-while-revalidate=86400"
- sources:
  - [1] https://ipkit.dev/docs
