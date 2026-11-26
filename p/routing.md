# routing.run

> routing.run | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/routing/ | JSON https://fshy.ajam.dev/api/v1/entity/routing.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## routing.run

- `inference/routing-run` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://routing.run/pricing
- free tier: Top up from$5Credits you buy don't expire. No plan, no seats. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign in with GitHub, Google, Discord, Apple or an email link, then top up from USD 5
- interface: rest
- limits:
  - volume-quota (binding): minimum USD 5 top-up; credits do not expire [1]
- endpoint: https://api.routing.run/v1
- composes with: The docs /api-reference/models route was rate-limited on retry; the first-party apex pricing page was used instead. No free tier is published.
- reliability: 503 with a short message when a model is unavailable
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: routing.run sells pay-as-you-go credits from USD 5 with no free allowance stated | capture: sha256:fd3a33990e0551cc8c231f62e4d104caad7114050a334e3e52a81baf822562f7 | quote: Top up from$5Credits you buy don't expire. No plan, no seats.
- sources:
  - [1] https://routing.run/pricing
