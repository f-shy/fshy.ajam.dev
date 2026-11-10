# Unblock Master IP

> unblockmaster.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/unblockmaster/ | JSON https://fshy.ajam.dev/api/v1/entity/unblockmaster.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Unblock Master IP

- `data-apis/unblock-master-ip` | qualifies | evidence measured | binding request-rate | category IP geolocation API | tier Free keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://www.unblockmaster.com/free-ip-api/
- free tier: free keyless API with no signup: 60 requests a minute per client; country, city, coordinates, network operator and a datacenter or VPN flag for any IPv4 or IPv6 address | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: no daily or monthly quota is stated; past the limit the API answers HTTP 429 with Retry-After.
- per-object cap: one IP address per request (GET /api/v1/ip/<ip>) | source: [1]
- retention: not applicable: a lookup API; the service caches each address for an hour | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: no API key and no signup
- interface: rest
- limits:
  - request-rate (binding): 60 requests per minute per client; HTTP 429 rate_limited with Retry-After past it [1]
- binding note: 60 requests a minute is the only published cap; no daily or monthly quota is stated.
- interface detail: GET https://www.unblockmaster.com/api/v1/ip/<ip> answers JSON for any IPv4 or IPv6 address and GET /api/v1/ip answers for the caller; CORS enabled; X-RateLimit-Limit and X-RateLimit-Remaining headers on every successful answer
- endpoint: https://www.unblockmaster.com/api/v1/ip/{ip}
- tooling: any HTTP client
- composes with: Keyless country, city, network operator and datacenter or VPN flag at 60 lookups a minute per caller; the same API backs the vendor's VPN checker. Bulk path: none.
- reliability: a best-effort service with no uptime guarantee; past 60 requests a minute it answers HTTP 429 with Retry-After; is_vpn is null when the lookup could not be completed
- notes: Free requests: no quota stated; 60 a minute per client. Rate limit: HTTP 429 with Retry-After. The service caches each address for an hour. Bulk path: none.
- evidence note: A keyless lookup of 8.8.8.8 was probed on 2026-11-02 and returned HTTP 200 with X-RateLimit-Limit 60; the limit was not exhausted.
- extras:
  - bulk_path: none
  - free_requests: 60 a minute per client, no key
- evidence:
  - [1] 2026-11-02: a lookup returns country, city, operator and a datacenter or VPN flag with no key and no signup | capture: sha256:ac8904de6dd0bb28fde91b6c3f1c709eaf0bbeabe658f03158ae784942550598 | quote: Give it an IP address, get back its country, city, network operator and whether it belongs to a datacenter or VPN. No API key. No signup. No cost.
  - [1] 2026-11-02: the limit is 60 requests a minute per client | capture: sha256:ac8904de6dd0bb28fde91b6c3f1c709eaf0bbeabe658f03158ae784942550598 | quote: The limit is 60 requests per minute per client.
  - [1] 2026-11-02: past the limit the API answers HTTP 429 with Retry-After | capture: sha256:ac8904de6dd0bb28fde91b6c3f1c709eaf0bbeabe658f03158ae784942550598 | quote: | 429 | `rate_limited` | Over the limit. Honour the Retry-After header. |
  - [1] 2026-11-02: any IPv4 or IPv6 address can be looked up | capture: sha256:ac8904de6dd0bb28fde91b6c3f1c709eaf0bbeabe658f03158ae784942550598 | quote: Looks up any IPv4 or IPv6 address.
  - [1] 2026-11-02: the page asks callers to cache results | capture: sha256:ac8904de6dd0bb28fde91b6c3f1c709eaf0bbeabe658f03158ae784942550598 | quote: Cache results on your side where you can. Geolocation does not change minute to minute.
  - [1] 2026-11-02: the service caches each address for an hour | capture: sha256:ac8904de6dd0bb28fde91b6c3f1c709eaf0bbeabe658f03158ae784942550598 | quote: We cache each address for an hour, so repeated lookups of the same IP are cheap for both of us.
  - [1] 2026-11-02: no uptime guarantee | capture: sha256:ac8904de6dd0bb28fde91b6c3f1c709eaf0bbeabe658f03158ae784942550598 | quote: This is a best-effort free service with no uptime guarantee.
  - probe:https://www.unblockmaster.com/api/v1/ip/8.8.8.8 2026-11-02: a keyless GET of /api/v1/ip/8.8.8.8 answered HTTP 200 | capture: sha256:3a99224f36e174c51fe87abfb7c75e8c5dc99e9babcae3b4a2bf98bea32e1a49 | quote: "status": 200
  - probe:https://www.unblockmaster.com/api/v1/ip/8.8.8.8 2026-11-02: the answer advertises a limit of 60 | capture: sha256:3a99224f36e174c51fe87abfb7c75e8c5dc99e9babcae3b4a2bf98bea32e1a49 | quote: "x-ratelimit-limit": "60"
  - probe:https://www.unblockmaster.com/api/v1/ip/8.8.8.8 2026-11-02: the answer carries country, country code and city | capture: sha256:ba0cc77ddf2b7f988c495156fcd11deaa4759cf4c3ca9c223adb42d4dcc28952 | quote: "country": "United States", "country_code": "US", "city": "Ashburn"
- sources:
  - [1] https://www.unblockmaster.com/free-ip-api/
