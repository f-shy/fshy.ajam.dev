# Standard Compute

> standardcompute.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/standardcompute/ | JSON https://fshy.ajam.dev/api/v1/entity/standardcompute.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Standard Compute

- `inference/standardcompute` | trial-only | evidence documented | binding volume-quota | category flat-rate inference subscription with no-card trial
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://standardcompute.com/
- free tier: a USD 0.25 trial with no credit card for eligible new accounts, to test the service in an agent; paid plans carry a 7-day fair refund; the gateway has one flat-rate smart-routing model id | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: eligible new accounts receive the USD 0.25 trial with no credit card; the eligibility rule is not published on the apex page
- interface: rest
- limits:
  - volume-quota (binding): USD 0.25 trial for eligible new accounts, no credit card [1]
- binding note: the small one-time trial binds before any rate
- endpoint: https://api.stdcmpt.com/v1
- tooling: an OpenAI-compatible key against a single flat-rate smart-routing model id
- composes with: pairs with a coding agent through the gateway; the scarce link is the USD 0.25 trial and the eligibility rule
- reliability: no reliability event recorded
- notes: the free offer is a small trial credit, not a standing tier.
- evidence:
  - [1] 2026-11-18: eligible new accounts get a USD 0.25 no-card trial | capture: sha256:f37f74c7eeb73e9ffad1fa1b7292f942efb03124c9926f4e476bd749a61e2efa | quote: You’ll know before you pay. Eligible new accounts get a $0.25 trial with no credit card, so you can test it in your own agent first.
- sources:
  - [1] https://standardcompute.com/
