# Network Data Labs

> networkdatalabs.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/networkdatalabs/ | JSON https://fshy.ajam.dev/api/v1/entity/networkdatalabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Network Data Labs

- `data-apis/network-data-labs` | fails-quota | evidence documented | binding volume-quota | category IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.369Z (live) | stale on 2026-12-03
- url https://www.networkdatalabs.com/pricing
- free tier: Free plan, USD 0 a month: 1,000 requests per UTC calendar month at 1 request a second, one API key, geolocation and ASN fields, usage alerts at 80% and 100%. | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: A hard cap with no buffer that resets on the 1st; past it, and past 1 request a second, the API answers HTTP 429 with Retry-After. The home page demo allows 10 lookups a day with no sign-up. Starter is USD 9 a month for 100k requests a month; no plan has overage charges.
- per-object cap: single lookups on Free; the bulk call takes up to 100 IPs a request on paid plans only | source: [2]
- retention: not stated
- egress: not applicable | metered: no | source: [1]
- identity: email | detail: an email address and password; the API key is issued after email confirmation; a card is stated as required only for the 14-day Growth trial
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests per UTC calendar month on the Free plan, a hard cap with no buffer [2]
  - request-rate: 1 request a second on the Free plan, no burst [2]
- binding note: 1,000 requests a month is used up long before 1 request a second can matter.
- interface detail: GET https://api.networkdatalabs.com/v0/ip/{ip} with Authorization: Bearer KEY, POST /v0/bulk on paid plans, GET /v0/asn/{asn}; JSON with location, accuracy radius, confidence, network and traits; HTTP 401 UNAUTHORIZED without a key
- endpoint: part of interface detail
- tooling: any HTTP client
- composes with: 1,000 keyed lookups a month with geolocation, accuracy radius, confidence and ASN, at 1 request a second. Bulk path: POST /v0/bulk, up to 100 IPs a request, paid plans only; database downloads are announced as coming soon
- reliability: Counters live in memory on a single Fly VM, and the Free tier is best-effort with no SLA.
- notes: Free requests: 1,000 per UTC calendar month at 1 request a second (the pricing page and the documentation state a month, not a day); the home page demo gives 10 a day with no sign-up. Rate limit: 1 request a second, no burst (HTTP 429). Bulk path: POST /v0/bulk, 100 IPs a request, paid plans only.
- evidence note: The pricing, documentation, privacy and terms pages were read on 2026-11-02, and a keyless call answered HTTP 401 UNAUTHORIZED; no keyed lookup was made, so the quota and the rate limit are as published.
- extras:
  - bulk_path: POST /v0/bulk, up to 100 IPs a request, paid plans only; database downloads announced as coming soon
  - free_requests: 1,000 a month
- evidence:
  - [1] 2026-11-02: the Free plan has geolocation and ASN | capture: sha256:b536b378b5aca694916165e4dd69c71151d06cd29492082eb738de060b16bf76 | quote: Free includes geolocation + ASN. Paid plans add risk flags, bulk lookups.
  - [1] 2026-11-02: no plan has overage charges | capture: sha256:b536b378b5aca694916165e4dd69c71151d06cd29492082eb738de060b16bf76 | quote: No overage charges on any plan.
  - [1] 2026-11-02: Starter is USD 9 a month | capture: sha256:b536b378b5aca694916165e4dd69c71151d06cd29492082eb738de060b16bf76 | quote: $9 / mo or $90/yr · 2 months free
  - [1] 2026-11-02: Starter includes 100k requests a month | capture: sha256:b536b378b5aca694916165e4dd69c71151d06cd29492082eb738de060b16bf76 | quote: 100k req / mo
  - [1] 2026-11-02: a card is required for the Growth 14-day trial | capture: sha256:b536b378b5aca694916165e4dd69c71151d06cd29492082eb738de060b16bf76 | quote: Card required · Cancel anytime before day 14 and you won’t be charged
  - [2] 2026-11-02: the Free plan is 1 request a second and 1,000 requests per UTC calendar month | capture: sha256:6d86be09ce4cbd1cd0c7969da4070aecebaea371010b7fee77c2c38a57157250 | quote: The Free plan includes 1 request/second and 1,000 requests per UTC calendar month.
  - [2] 2026-11-02: the Free quota is a hard cap with no buffer and resets on the 1st | capture: sha256:6d86be09ce4cbd1cd0c7969da4070aecebaea371010b7fee77c2c38a57157250 | quote: Free is 1 request/second with no burst, and a hard 1,000 requests per UTC calendar month (no buffer; resets on the 1st).
  - [2] 2026-11-02: exceeding the rate limit or the quota returns HTTP 429 | capture: sha256:6d86be09ce4cbd1cd0c7969da4070aecebaea371010b7fee77c2c38a57157250 | quote: Exceeding the rate limit or the account quota returns `429` with `limit`, `reset_at`, `plan` (current plan), and `upgrade_url`
  - [2] 2026-11-02: counters are per account and held in memory on a single VM | capture: sha256:6d86be09ce4cbd1cd0c7969da4070aecebaea371010b7fee77c2c38a57157250 | quote: Counters are per account (all keys combined) and live in memory on the API machine (a single Fly VM today), refreshed from stored usage every few minutes.
  - [2] 2026-11-02: a free account is created at sign-up and the key follows email confirmation | capture: sha256:6d86be09ce4cbd1cd0c7969da4070aecebaea371010b7fee77c2c38a57157250 | quote: Sign up below to create a free account and get your API key instantly after email confirmation.
  - [2] 2026-11-02:  | capture: sha256:6d86be09ce4cbd1cd0c7969da4070aecebaea371010b7fee77c2c38a57157250
  - [2] 2026-11-02: bulk lookup is paid-only | capture: sha256:6d86be09ce4cbd1cd0c7969da4070aecebaea371010b7fee77c2c38a57157250 | quote: bulk lookup is paid-only.
  - [3] 2026-11-02: the bulk call takes up to 100 IPs a request on paid plans | capture: sha256:a97ad2fc5ee09a170cf1cf1373c32a215c46e453b44e4eb83e8cd467c3522dd6 | quote: Have a list? `POST /v0/bulk` (paid plans) takes up to 100 IPs per request with the same schema
  - [4] 2026-11-02: the home page demo gives 10 free lookups a day with no signup | capture: sha256:3a98a5f92dc1e51815285624bbd248a1199c3b3dd9a8e0cc7df33dc72c22bcf6 | quote: Uses your IP if empty. 10 free lookups per day. No signup.
  - [4] 2026-11-02: database downloads are announced as coming soon | capture: sha256:3a98a5f92dc1e51815285624bbd248a1199c3b3dd9a8e0cc7df33dc72c22bcf6 | quote: DB downloads · coming soon
  - [5] 2026-11-02: the Free tier has no hard SLA | capture: sha256:04a69aaed33a3a94c75ba71e5d3a65d96908789422d7c7bad8ade6acd7f235da | quote: The Free tier is best-effort. We do not offer a hard SLA on Free.
  - [6] 2026-11-02: sign-up for an API key takes an email address and a password | capture: sha256:35d6903952df4cf801edb1a40f659dae7629808f3b0e08bd0ffa32a65b8aa6af | quote: email and password when you sign up for an API key through the dashboard.
  - [7] 2026-11-02: the paid plans are USD 9, USD 29 and USD 79 a month | capture: sha256:7a4d6602e7c29275b7f6f1503cb9193105589d9aa5f1c81db6519964ed666684 | quote: Risk flags (`is_hosting`, `is_vpn`, `is_tor`, `is_relay`) are on paid plans: $9, $29 and $79/month, or $90, $290 and $790/year, with no overage charges.
  - probe:https://api.networkdatalabs.com/v0/ip/8.8.8.8 2026-11-02: a call with no key answered HTTP 401 | capture: sha256:693a6178df069c11a68936ff36c8ae10f65327d633b15cc80775f26bfc42e7d9 | quote: "status": 401
  - probe:https://api.networkdatalabs.com/v0/ip/8.8.8.8 2026-11-02: the keyless answer is UNAUTHORIZED: Missing or invalid API key | capture: sha256:6e2dfdebd7dd77f38b272811a97e39ddafcb3c9c565bdbd69be9b93844e40bd4 | quote: {"error":{"code":"UNAUTHORIZED","message":"Missing or invalid API key"}}
- sources:
  - [1] https://www.networkdatalabs.com/pricing
  - [2] https://www.networkdatalabs.com/docs
  - [3] https://www.networkdatalabs.com/ip-geolocation-api
  - [4] https://www.networkdatalabs.com/
  - [5] https://www.networkdatalabs.com/terms
  - [6] https://www.networkdatalabs.com/privacy
  - [7] https://www.networkdatalabs.com/hosting-ip-detection-api
