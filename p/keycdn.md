# KeyCDN IP

> keycdn.com | Data APIs, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keycdn/ | JSON https://fshy.ajam.dev/api/v1/entity/keycdn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KeyCDN IP Location Finder

- `data-apis/keycdn-ip-location-finder` | qualifies | evidence measured | binding request-rate | category IP geolocation API | tier Free keyless
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2027-01-02
- url https://tools.keycdn.com/geo
- free tier: keyless REST API answering JSON, rate limited to 3 requests a second; the User-Agent header must have the form keycdn-tools:https://your-site; data from MaxMind GeoLite | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: no daily or monthly quota is stated; a request with a missing or invalid User-Agent is blocked.
- per-object cap: one host name or IP address per request (the host parameter) | source: [1]
- retention: not stated | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: anonymous | detail: no key and no account; a User-Agent header naming the calling site is required
- interface: rest
- limits:
  - request-rate (binding): 3 requests a second [1]
- binding note: 3 requests a second is the only published cap; no daily or monthly quota is stated.
- interface detail: GET https://tools.keycdn.com/geo.json?host={ip or hostname} answers JSON; the User-Agent header names the calling site in the form keycdn-tools:https://example.com
- endpoint: part of interface detail
- tooling: curl with the User-Agent header shown in the page's example
- composes with: Keyless MaxMind GeoLite city and ASN lookups at 3 requests a second; one host per request. Bulk path: none.
- reliability: requests without a valid keycdn-tools User-Agent are blocked, and the page says the service is rate limited to avoid overload
- notes: Free requests: no quota stated; 3 requests a second. Rate limit: 3 per second. Bulk path: none; one host per request.
- evidence note: A keyless lookup of 8.8.8.8 with the User-Agent form from the page's own example was probed on 2026-11-02 and returned HTTP 200; the rate limit is quoted from the page and was not exhausted.
- extras:
  - bulk_path: none
  - free_requests: 3 a second, no quota stated
- evidence:
  - [1] 2026-11-02: the REST API answers JSON and is rate limited to 3 requests a second | capture: sha256:aadd2e5add6d64a45586a5e34756e244254c6ef53a4678ad52ec2be8076c52a6 | quote: Get the IP geolocation data through the simple REST API. All the responses are JSON encoded. We are rate limiting requests (3r/s) to avoid overload of the system.
  - [1] 2026-11-02: a User-Agent header naming the calling site is required | capture: sha256:aadd2e5add6d64a45586a5e34756e244254c6ef53a4678ad52ec2be8076c52a6 | quote: It is required to set the request header `User-Agent` in the format `keycdn-tools:https?://.*`, which must include the website you are using the API for.
  - [1] 2026-11-02: a missing or invalid User-Agent is blocked | capture: sha256:aadd2e5add6d64a45586a5e34756e244254c6ef53a4678ad52ec2be8076c52a6 | quote: Missing attributions or invalid values will be blocked.
  - [1] 2026-11-02: the data comes from MaxMind GeoLite | capture: sha256:aadd2e5add6d64a45586a5e34756e244254c6ef53a4678ad52ec2be8076c52a6 | quote: This product includes GeoLite Data created by MaxMind, available from [https://www.maxmind.com](https://www.maxmind.com/).
  - [1] 2026-11-02: the documented call is a GET of /geo.json with a host parameter and the User-Agent header | capture: sha256:aadd2e5add6d64a45586a5e34756e244254c6ef53a4678ad52ec2be8076c52a6
  - probe:https://tools.keycdn.com/geo.json?host=8.8.8.8 2026-11-02: a keyless GET of /geo.json?host=8.8.8.8 with the documented User-Agent form answered HTTP 200 | capture: sha256:55e9c651ac5e6730b8b5a41eaf072ad7b319961863138ec815ac54c07323c10f | quote: "status": 200
  - probe:https://tools.keycdn.com/geo.json?host=8.8.8.8 2026-11-02: the answer reports success | capture: sha256:d392369c3089d1243c48883093a27063b88090d42c712e20bdaa410ebf0342e2 | quote: "status":"success","description":"Data successfully received."
  - probe:https://tools.keycdn.com/geo.json?host=8.8.8.8 2026-11-02: the answer carries ASN, ISP and country | capture: sha256:d392369c3089d1243c48883093a27063b88090d42c712e20bdaa410ebf0342e2 | quote: "asn":15169,"isp":"Google LLC","country_name":"United States","country_code":"US"
- sources:
  - [1] https://tools.keycdn.com/geo

## KeyCDN Push Zone (CDN storage)

- `storage/keycdn-push-zone` | fails-egress | evidence reported | binding none | category object-storage
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.keycdn.com/cdn-storage
- price $120/TB stored (Push Zone, $0.12/GB); $40/TB delivered ($0.04/GB above 1 TB); Pull Zone storage $0. | parsed USD 120/TB-mo
- free tier: Unlimited volume. Push Zone storage '$0.12/GB per month and charged on a daily basis' = $120/TB/mo. Tiered down to $0.04/GB above 1 TB/month of stored bytes. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Interconnect from the storage cluster to the edge is free ('Interconnect traffic from our storage cluster to our edge servers is free'), but edge delivery is billed at $0.04/GB (= $40/TB) above the first 500 GB/month, and the 500 GB is itself priced at $0.12/GB. Pull Zone storage has no extra cost. You supply the origin. | metered: yes | free allowance: 500 GB per month | price per TB: $40/TB
- identity: email | detail: email
- interface: ftp, rsync, ssh
- limits note: per-object-cap: none published. Trial is 14 days / 25 GB traffic. Log forwarding $1/day, image processing $0.40/1k ops.
- interface detail: ftp + ssh
- tooling: FTP(S) and rsync-over-SSH for uploads; pull/push zones over HTTP. Free 14-day trial, no card.
- composes with: The free-interconnect-to-edge idea is right and the price is an order of magnitude wrong: $120/TB at rest versus $6 Telnyx. Only viable as a free 14-day trial. The genuinely useful configuration is a Pull Zone (free storage) pointed at one of the free origins above. Then KeyCDN charges you $40/TB for delivery and nothing for storage.
- reliability: European DCs, TLS included. 14-day/25 GB trial is one of the weaker on-ramps in the sector.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Unlimited volume. Push Zone storage '$0.12/GB per month and charged on a daily basis' = $120/TB/mo. Tiered down to $0.04/GB above 1 TB/month of stored bytes.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $120/TB stored (Push Zone, $0.12/GB); $40/TB delivered ($0.04/GB above 1 TB); Pull Zone storage $0.
- evidence:
  - [1] 2026-10-21: 'How is storage billed? Pull Zone storage has no additional cost. Push Zone storage starts at $0.12/GB per month and is charged on a daily basis.'
  - [2] 2026-10-21: 'First 500 GB per month $0.12/GB | Next 500 GB $0.08/GB | Above 1 TB $0.04/GB'; 'The first 3 Zones are included for free'
  - [3] 2026-10-21: 'Accelerated uploads … FTP(S) or rsync over SSH'; 'Interconnect traffic from our storage cluster to our edge servers is free'
- sources:
  - [1] https://www.keycdn.com/faq
  - [2] https://www.keycdn.com/pricing
  - [3] https://www.keycdn.com/cdn-storage
