# SteadyRouter

> steadyrouter.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/steadyrouter/ | JSON https://fshy.ajam.dev/api/v1/entity/steadyrouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SteadyRouter

- `inference/steadyrouter` | trial-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://www.steadyrouter.com/site/docs.html
- free tier: New accounts currently start with USD 0.05 of credit on a key already set to the lowest-price route, and top-ups run from USD 10 to USD 500 by card, Apple Pay or Google Pay. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: top-ups by card, Apple Pay or Google Pay from USD 10; the starting credit needs only an account
- interface: rest
- limits:
  - volume-quota (binding): USD 0.05 of starting credit, then top-ups from USD 10 [1]
- endpoint: https://api.steadyrouter.com/v1
- composes with: USD 0.05 is a single request, so the starting credit cannot carry a sweep
- reliability: a starting credit that covers one call makes the free path a demonstration rather than an allowance
- evidence:
  - [1] 2026-11-18: new accounts start with USD 0.05 of credit and top-ups run from USD 10 to USD 500 | capture: sha256:1cac048bfeb0dab92a1864c5beaa29d14365782124d0e581d60dd15f7f2cc01b | quote: New accounts currently start with US$0.05 of credit, and the key they come with is already on “Lowest price”. To make it last, start with a smaller model; see the setup guides.
- sources:
  - [1] https://www.steadyrouter.com/site/docs.html
