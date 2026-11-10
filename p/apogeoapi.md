# ApogeoAPI

> apogeoapi.com | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/apogeoapi/ | JSON https://fshy.ajam.dev/api/v1/entity/apogeoapi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ApogeoAPI

- `data-apis/apogeoapi` | trial-only | evidence documented | binding volume-quota | category geographic reference data and IP geolocation API | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-02T00:23:42.887Z (live) | stale on 2026-12-03
- url https://apogeoapi.com/pricing
- free tier: Free plan, USD 0 a month: 1,000 requests a month at 5 requests a minute, with countries and states data and no expiry; IP geolocation, cities, global search and live currency rates are on a 14-day full-access trial given to every new account, then on the Basic plan at USD 19 a month (15,000 requests a month, 30 a minute) | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: Starter is USD 29 a month for 100,000 requests and Professional USD 79 for 500,000; the quota is a hard cap and the API answers HTTP 429 once it is reached.
- per-object cap: not stated | source: [1]
- retention: not applicable: a lookup API | source: [2]
- egress: not applicable: JSON answers, not metered in bytes | metered: no | source: [1]
- identity: email | detail: an account with email sign-up; no credit card for the trial
- interface: rest
- limits:
  - volume-quota (binding): 1,000 requests a month on the Free plan; hard-capped, HTTP 429 once reached [2]
  - request-rate: 5 requests a minute on the Free plan [3]
- binding note: the IP geolocation module is open for 14 days only; after that the 1,000 requests a month of the Free plan cover countries and states, not IP lookups.
- interface detail: GET https://api.apogeoapi.com/v1/ip/{ip} with an X-API-Key header answers JSON; a call without a key answers HTTP 401
- endpoint: part of interface detail
- tooling: any HTTP client; quickstarts for cURL, JavaScript, Python and PHP; X-RateLimit-Remaining and Retry-After headers on 429 answers
- composes with: IP geolocation is free for the 14-day trial only; after that it needs Basic, USD 19 a month; the free plan keeps countries and states data at 1,000 requests a month. Bulk path: none stated.
- reliability: the monthly quota is a hard cap with HTTP 429 until the next cycle; email alerts at 80% and 100% usage; a keyless call answered HTTP 401 with a Spanish message
- notes: Free requests: 1,000 a month and 5 a minute, for countries and states after the 14-day trial; IP geolocation is trial-only, then Basic at USD 19 a month. Rate limit: 5 a minute free; HTTP 429 with Retry-After. Bulk path: none stated.
- evidence note: The pricing, documentation, sign-up and terms pages were quoted on 2026-11-02 and a keyless call answered HTTP 401; no keyed lookup was made, so the trial lookups were not exercised.
- extras:
  - bulk_path: none stated
  - free_requests: 1,000 a month, IP geolocation only in the 14-day trial
- evidence:
  - [1] 2026-11-02: the free plan keeps countries and states; every new account gets 14 days of full access including IP geolocation | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: Free forever with countries and states. Every new account gets 14 days of full access to cities, exchange rates, IP geolocation, and more — no credit card required. Upgrade anytime to keep premium features.
  - [1] 2026-11-02: the Free plan allows 1,000 requests a month | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: - 1,000 requests/month
  - [1] 2026-11-02: the Free plan allows 5 requests a minute | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: - 5 requests/min
  - [1] 2026-11-02: IP geolocation is marked a 14-day trial on the Free plan | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: - IP geolocation14-day trial
  - [1] 2026-11-02: Basic costs USD 19 a month | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: $19/mo
  - [1] 2026-11-02: Basic allows 15,000 requests a month | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: - 15,000 requests/month
  - [1] 2026-11-02: Basic allows 30 requests a minute | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: - 30 requests/min
  - [1] 2026-11-02: requests are blocked once the monthly quota is reached; alerts at 80% and 100% | capture: sha256:03b74f9ad88998ba84a7ee6f7224babd2d507b1a5179446dd5f78a213fd400b2 | quote: You'll receive email alerts at 80% and 100% usage. Requests are blocked once your monthly quota is reached — upgrade anytime to continue.
  - [3] 2026-11-02: the Free tier is 5 a minute and 1,000 a month | capture: sha256:4da918945b36b41dca561f5675083c4133e669ef79dce1b18a3cc7c131d0c59b | quote: - Free: 5 req/min · 1,000/mo
  - [3] 2026-11-02: every request needs an X-API-Key header; the free key comes with a 14-day trial | capture: sha256:4da918945b36b41dca561f5675083c4133e669ef79dce1b18a3cc7c131d0c59b | quote: All requests require an `X-API-Key` header. Create your free key in the [dashboard](https://app.apogeoapi.com/register) — 1,000 requests/month on the free tier plus a 14-day full-access trial.
  - [2] 2026-11-02: the monthly quota is a hard cap with HTTP 429 | capture: sha256:f56bb5ee3f283d4597354fd93bb1b0c13a450f9a6dbdae607800d9e2d843286f | quote: All plans, including paid plans, are hard-capped at their monthly request quota. Once the quota is reached, requests return a 429 error until the next billing cycle.
  - [2] 2026-11-02:  | capture: sha256:f56bb5ee3f283d4597354fd93bb1b0c13a450f9a6dbdae607800d9e2d843286f
  - [4] 2026-11-02: the sign-up needs no credit card | capture: sha256:05f4df5cf6b0a9aa874c005ee4740d770f1b4c79ea0b3a89f6fecc140ff0160e | quote: Start your 14-day free trial — no credit card required
  - [4] 2026-11-02: email sign-up is offered | capture: sha256:05f4df5cf6b0a9aa874c005ee4740d770f1b4c79ea0b3a89f6fecc140ff0160e | quote: or continue with email
  - probe:https://api.apogeoapi.com/v1/ip/8.8.8.8 2026-11-02: a keyless GET of /v1/ip/8.8.8.8 answered HTTP 401 | capture: sha256:6b9c415e433f4403b7d3328995567a45ee071bddfc75b471fb53ec77a7fda5ac | quote: "status": 401
  - probe:https://api.apogeoapi.com/v1/ip/8.8.8.8 2026-11-02: the answer asks for an X-API-Key header | capture: sha256:759c123d9ca52683f1d907347fb5bf69b4f761261c882eb162187ce79c22986f | quote: API key requerida. Incluir en header: X-API-Key
- sources:
  - [1] https://apogeoapi.com/pricing
  - [2] https://apogeoapi.com/terms
  - [3] https://apogeoapi.com/docs
  - [4] https://app.apogeoapi.com/register
