# IP-API.io

> ip-api.io | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip-api-2/ | JSON https://fshy.ajam.dev/api/v1/entity/ip-api-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IP-API.io

- `data-apis/ip-api-io` | qualifies-with-caveat | evidence documented | binding volume-quota | category IP geolocation and VPN detection API | tier Free tier (key required)
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://ip-api.io/
- free tier: a free tier with an API key and no credit card; its allowance is not published; a keyless single lookup answers HTTP 401; plans from EUR 10 a month for 100,000 requests | unit: requests | metered on: unstated | read on: 2026-11-02 | source: [1] | note: unverified: the free allowance; no page states a number. Medium is EUR 20 a month for 300,000 requests and Large EUR 49 for 1,000,000.
- per-object cap: one IP per GET /api/v1/ip/{ip}; POST /api/v1/ip/batch takes up to 100 IPs | source: [2]
- retention: not stated | source: [1]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: email | detail: first name, last name, email and password on the sign-up form; no credit card required
- interface: rest
- limits:
  - volume-quota (binding): unverified: the free tier's allowance is not published [1]
  - per-object-cap: up to 100 IPs per batch request [2]
- binding note: the free allowance is unpublished; the paid plans are metered in requests a month.
- interface detail: GET https://ip-api.io/api/v1/ip/{ip}?api_key={key} answers JSON with location, ISP, ASN and suspicious_factors; POST https://ip-api.io/api/v1/ip/batch takes up to 100 IPs, and the key is optional there
- endpoint: part of interface detail
- tooling: any HTTP client or the official SDKs
- composes with: Location plus VPN, proxy, Tor and threat flags in one answer; the free allowance is unpublished, so the paid plans from EUR 10 a month are the stated working route. Bulk path: POST /api/v1/ip/batch, up to 100 IPs, one credit per unique IP.
- reliability: a keyless single lookup answers HTTP 401 Valid API key is required; anonymous batch requests are rate limited per IP with no published limit
- notes: Free requests: unverified; no page states the free allowance. Rate limit: anonymous batch requests are rate limited per IP, limit not published. Bulk path: POST /api/v1/ip/batch, up to 100 IPs, key optional, one credit per unique IP.
- evidence note: The home, product, bulk and sign-up pages were quoted on 2026-11-02 and a keyless single lookup answered HTTP 401; no keyed lookup was made and no page states the free allowance, so it is unverified.
- extras:
  - bulk_path: POST /api/v1/ip/batch, up to 100 IPs, key optional
  - free_requests: unverified: allowance unpublished
- evidence:
  - [1] 2026-11-02: a free tier exists and needs no card | capture: sha256:ffca0f8ee6eb2f030612b95ca6a470c25705bb3fa6097a5e704c39029300356c | quote: Free tier available, no card required.
  - [3] 2026-11-02: paid plans start at EUR 10 a month | capture: sha256:57c052ae9c12542a24c8c616e9f7cb81b4db23ee696b580f040c23fb2994cbd8 | quote: Plans from €10/month • Cancel anytime
  - [2] 2026-11-02: the EUR 10 plan allows 100,000 requests a month | capture: sha256:df2e741448f40cf12ed4ef720c4ce8e4b0c1c027d11654589f76667c88962a7a | quote: 100,000 geo IP requests / month
  - [2] 2026-11-02: the EUR 20 plan allows 300,000 requests a month | capture: sha256:df2e741448f40cf12ed4ef720c4ce8e4b0c1c027d11654589f76667c88962a7a | quote: 300,000 geo IP requests / month
  - [2] 2026-11-02: the EUR 49 plan allows 1,000,000 requests a month | capture: sha256:df2e741448f40cf12ed4ef720c4ce8e4b0c1c027d11654589f76667c88962a7a | quote: 1,000,000 geo IP requests / month
  - [2] 2026-11-02: the batch endpoint takes up to 100 IPs | capture: sha256:df2e741448f40cf12ed4ef720c4ce8e4b0c1c027d11654589f76667c88962a7a | quote: For the API, send a JSON object with an `ips` array containing up to 100 addresses in a single `POST` to `https://ip-api.io/api/v1/ip/batch`.
  - [2] 2026-11-02: the batch endpoint takes anonymous requests, rate limited per IP | capture: sha256:df2e741448f40cf12ed4ef720c4ce8e4b0c1c027d11654589f76667c88962a7a | quote: API key is optional — anonymous requests are rate-limited by your IP address.
  - [2] 2026-11-02: a batch costs one credit per unique IP, charged only on success | capture: sha256:df2e741448f40cf12ed4ef720c4ce8e4b0c1c027d11654589f76667c88962a7a | quote: API credits are deducted only after a batch completes successfully — one credit per unique IP address.
  - [4] 2026-11-02: the sign-up needs no credit card | capture: sha256:ae13464fb4be2f081c1e71a635582166711a82f8415b5ebd636c5989be0bb391 | quote: No credit card required Cancel anytime Plans from €10/mo
  - [4] 2026-11-02: the sign-up form asks for first name, last name, email and a confirmed password | capture: sha256:ae13464fb4be2f081c1e71a635582166711a82f8415b5ebd636c5989be0bb391 | quote: First name Last name Email Password Confirm password
  - [5] 2026-11-02: a keyless single lookup answers HTTP 401 and asks for a key | capture: sha256:2b7235d74a6882fdb504b5237c8825f490d4a9858ff54e725f0ccac64ab9a4e0 | quote: Valid API key is required. Please visit https://ip-api.io to obtain an API key.
  - [5] 2026-11-02: the keyless single lookup status is HTTP 401 | capture: sha256:2b7235d74a6882fdb504b5237c8825f490d4a9858ff54e725f0ccac64ab9a4e0 | quote: HTTP/1.1 401 Unauthorized
- sources:
  - [1] https://ip-api.io/ip-geolocation-api
  - [2] https://ip-api.io/bulk-ip-lookup
  - [3] https://ip-api.io/
  - [4] https://ip-api.io/registrations/new
  - [5] https://ip-api.io/api/v1/ip/8.8.8.8
