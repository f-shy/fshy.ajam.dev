# Instatus

> instatus.com | Developer services; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/instatus/ | JSON https://fshy.ajam.dev/api/v1/entity/instatus.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Instatus

- `dev-services/instatus` | qualifies-with-caveat | evidence documented | binding volume-quota | category status pages with uptime monitoring and on-call alerting | tier Starter
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-01T18:13:30.918Z (live) | stale on 2026-12-02
- url https://instatus.com/pricing
- free tier: Starter plan, free: 15 monitors at a 2-minute check interval, email alerts, 5 team members, 2 on-call members and a public status page with 200 subscribers; no custom domain | unit: objects | metered on: object-count | read on: 2026-11-01 | source: [1] | note: The unit counted is the monitor. The pricing text read shows the Starter plan as Free and leaves the Pro and Business prices blank, so no paid price is recorded. Which plans include the API is not stated on the pricing page.
- per-object cap: not applicable: a monitor checks a target; nothing is stored per object
- retention: unverified: no history retention period is stated on the pricing page
- egress: not applicable: an outbound checker and a status page host; incidents and page data are read through the REST API | metered: no | source: [2]
- identity: email | detail: The sign-up page text shows Continue with Google behind an hCaptcha and an agreement to the terms; whether an email and password form exists, and whether a card or phone number is asked later, is unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): 15 monitors, 5 team members, 2 on-call members and 200 subscribers on Starter [1]
  - request-rate: 2-minute check interval on Starter, 30 seconds on Pro and Business [1]
- limits note: Starter alerts by email only, while Pro adds SMS and Business adds calls; a custom domain starts on Pro.
- binding note: The 15-monitor cap and the 200-subscriber cap fill before the 2-minute check interval matters for an app with a few endpoints.
- interface detail: A REST API at api.instatus.com takes JSON and an API token as a Bearer token in the Authorization header, created in the dashboard under User settings, Developer settings. Whether the Starter plan may use it is unverified: the pricing page lists no API row.
- endpoint: https://api.instatus.com
- tooling: the web dashboard and the REST API
- composes with: A public status page and 2-minute checks on up to 15 endpoints of free-hosted services, with incidents opened and updated through the API.
- reliability: no throttle, ban or data loss is stated on the pages read
- evidence note: Plan limits are quoted from the first-party pricing page and the API from its documentation. No account was opened, so the sign-up fields, the card term and the API access on Starter are unverified: behind a sign-up.
- evidence:
  - [1] 2026-11-01: the Starter plan is free | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: ### Starter Free
  - [1] 2026-11-01: Starter has 15 monitors against 50 on Pro and 1,000 on Business | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | Monitors | 15 | 50 | 1,000 |
  - [1] 2026-11-01: Starter checks every 2 minutes | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | Checks | 2 min | 30 sec | 30 sec |
  - [1] 2026-11-01: Starter alerts by email, Pro by email and SMS, Business by SMS and calls | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | Alerts | Email | Email & SMS | SMS & Calls |
  - [1] 2026-11-01: Starter has 5 team members | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | Team members | 5 | 50 | |
  - [1] 2026-11-01: Starter has 2 on-call members | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | On-call members | 2 | 20 | 50 |
  - [1] 2026-11-01: Starter has a public status page | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | Status page type | Public | Public | All |
  - [1] 2026-11-01: Starter has no custom domain, which starts on Pro | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | Custom domain | | 1+ | 3+ |
  - [1] 2026-11-01: Starter allows 200 subscribers | capture: sha256:423bde751d6321d4a244ced554c4cece410ab68c30d118b1cc728cbbfef5091c | quote: | Subscribers | 200 | 5,000 | 25,000 |
  - [2] 2026-11-01: the REST API is served at api.instatus.com | capture: sha256:983485d545e9bad1ea029059f95eab56f2269228d213f4ffb23ac66f75a9b3a4 | quote: All endpoints are under the URL `https://api.instatus.com`. They generally follow the REST architecture.
  - [2] 2026-11-01: the API takes a token in the Authorization header | capture: sha256:983485d545e9bad1ea029059f95eab56f2269228d213f4ffb23ac66f75a9b3a4 | quote: Requests to Instatus API must provide an API token through the Authorization header:
  - [2] 2026-11-01: the API key is created in the dashboard under User settings, Developer settings | capture: sha256:983485d545e9bad1ea029059f95eab56f2269228d213f4ffb23ac66f75a9b3a4 | quote: You can get your API key from User settings → [Developer settings](https://dashboard.instatus.com/developer)
  - [3] 2026-11-01: the sign-up page offers Continue with Google behind an hCaptcha | capture: sha256:8200038f2051a9da2976c6be84002f8795ef96bd877b78bab5d151b02b2b2bc8 | quote: # Sign up Continue with Google
- sources:
  - [1] https://instatus.com/pricing
  - [2] https://instatus.com/help/api
  - [3] https://instatus.com/get
