# ip2geo.dev

> ip2geo.dev | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ip2geo/ | JSON https://fshy.ajam.dev/api/v1/entity/ip2geo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ip2geo.dev

- `data-apis/ip2geo-dev` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-31T06:24:05.368Z (live) | stale on 2026-12-01
- url https://ip2geo.dev/pricing
- free tier: Free plan: 1,000 conversions a month, no card, no rate limits, up to 5,000 IPs per bulk request | unit: requests | metered on: request-count | read on: 2026-10-30 | source: [1] | note: Starter is USD 10 a month for 10,000 conversions
- per-object cap: 5,000 IPs per bulk request | source: [1]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an email address that receives a sign-in code; no card
- interface: rest
- limits:
  - volume-quota (binding): 1,000 conversions a month [1]
  - per-object-cap: 5,000 IPs per bulk request [1]
- interface detail: GET api.ip2geo.dev/convert?ip=IP with a secret or website key; API, four SDKs and a CLI
- endpoint: https://api.ip2geo.dev/convert
- tooling: any HTTP client; vendor SDKs and CLI
- composes with: 1,000 conversions a month is a test allowance; bulk requests take 5,000 IPs but draw on the same monthly count. Bulk path: the bulk request
- reliability: no rate limits stated
- notes: Free requests: 1,000 a month. Rate limit: none stated. Bulk path: 5,000-IP bulk requests within the same monthly count.
- evidence note: the pricing and sign-in pages were quoted on 2026-10-30 and 2026-10-31; no keyed lookup was made.
- extras:
  - bulk_path: 5,000-IP bulk requests
  - free_requests: 1,000 a month
- evidence:
  - [1] 2026-10-30: the free plan is 1,000 conversions a month | capture: sha256:6bb5236dece78b3b9d5cfd9067e330abc05e9fe961d013934801321344813a51 | quote: 1,000 conversions a month
  - [1] 2026-10-30: no card is needed | capture: sha256:6bb5236dece78b3b9d5cfd9067e330abc05e9fe961d013934801321344813a51 | quote: No card required
  - [1] 2026-10-30: a bulk request takes 5,000 IPs | capture: sha256:6bb5236dece78b3b9d5cfd9067e330abc05e9fe961d013934801321344813a51 | quote: 5,000 IPs per bulk request
  - [1] 2026-10-30: no rate limits | capture: sha256:6bb5236dece78b3b9d5cfd9067e330abc05e9fe961d013934801321344813a51 | quote: No rate limits
  - [1] 2026-10-30: Starter is 10,000 conversions a month | capture: sha256:6bb5236dece78b3b9d5cfd9067e330abc05e9fe961d013934801321344813a51 | quote: 10,000 conversions a month
  - [1] 2026-10-30: Starter is USD 10 a month | capture: sha256:6bb5236dece78b3b9d5cfd9067e330abc05e9fe961d013934801321344813a51 | quote: $10 /month
  - [2] 2026-10-31: sign-up is by an emailed code | capture: sha256:5421acfb0d46714908bb81d75791b7cfd97c523e50e4c9ab7edea7e3f18096bb | quote: Enter your email and we'll send you a sign-in code. No account yet? The same code creates one.
  - [2] 2026-10-31: the API endpoint | capture: sha256:5421acfb0d46714908bb81d75791b7cfd97c523e50e4c9ab7edea7e3f18096bb | quote: curl "api.ip2geo.dev/convert?ip=8.8.4.4"
- sources:
  - [1] https://ip2geo.dev/pricing
  - [2] https://ip2geo.dev/auth
