# IP.City

> ip.city | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip/ | JSON https://fshy.ajam.dev/api/v1/entity/ip.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IP.City

- `data-apis/ip-city` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://www.ip.city/users.php
- free tier: 100 free requests per API key each day, after the email address is verified; meant for the development phase | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1]
- per-object cap: not stated
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: email, password and name with an arithmetic check; the key activates after email verification
- interface: rest
- limits:
  - volume-quota (binding): 100 requests per API key a day; 0 until the email is verified [1]
- interface detail: GET https://ip.city/api.php?ip=IP&key=KEY, JSON with a status field
- endpoint: part of interface detail
- tooling: any HTTP client
- composes with: 100 lookups a day per key is a development allowance. Bulk path: none
- reliability: past 100 requests in a day the API returns an error message
- notes: Free requests: 100 a day per verified key. Rate limit: not stated. Bulk path: none.
- evidence note: the API access page was quoted on 2026-10-30; no keyed lookup was made.
- extras:
  - bulk_path: none
  - free_requests: 100 a day
- evidence:
  - [1] 2026-10-30: 100 free requests per key a day | capture: sha256:4e15576602131a78e2b54d0cda2304b984923b82d9c5a27513815122cb5a17f8 | quote: This service allows free 100 request per API key each day.
  - [1] 2026-10-30: the free plan is for development | capture: sha256:4e15576602131a78e2b54d0cda2304b984923b82d9c5a27513815122cb5a17f8 | quote: Free plan is considered for development phase
  - [1] 2026-10-30: an unverified email gets 0 requests | capture: sha256:4e15576602131a78e2b54d0cda2304b984923b82d9c5a27513815122cb5a17f8 | quote: Unverified email: 0req/day - $0/mo
  - [1] 2026-10-30: the form asks a name | capture: sha256:4e15576602131a78e2b54d0cda2304b984923b82d9c5a27513815122cb5a17f8 | quote: _Your Name:_
  - [1] 2026-10-30: the key activates after email verification | capture: sha256:938cff1d38eea6f7b4ea3a77b8bdb963ee10766369c8949284b369b2c836c672 | quote: You need to verify your email address or purchase a plan in order to activate the API code.
  - [1] 2026-10-30: the API endpoint | capture: sha256:938cff1d38eea6f7b4ea3a77b8bdb963ee10766369c8949284b369b2c836c672 | quote: https://ip.city/api.php?ip=[IP]&key=[YOUR_API_KEY]
- sources:
  - [1] https://www.ip.city/users.php
