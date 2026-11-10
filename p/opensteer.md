# Opensteer

> opensteer.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opensteer/ | JSON https://fshy.ajam.dev/api/v1/entity/opensteer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Opensteer

- `compute/opensteer` | qualifies-with-caveat | evidence documented | binding request-rate | category browser host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:20.763Z (live) | stale on 2026-12-05
- url https://opensteer.com/pricing
- free tier: $5 of model credits at signup plus $5 a month of platform credits, no card; a bring-your-own subscription runs agents free | unit: mixed | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://opensteer.com/pricing prices browser runtime and computer runtime at USD 0.20 an hour and lists no data-transfer allowance or price | metered: no | source: [1]
- identity: email | detail: 'no credit card needed to start', quoted from the pricing page read 2026-10-22
- interface: unknown
- limits:
  - request-rate (binding): $5 of model credits at signup and $5 a month of platform credits; the paid tier is $50/mo [1]
- interface detail: a web sign-in and a downloadable app; no REST API, CLI or SSH page was read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. The free tier is two separate purses, model credits and platform credits, which is why the unit is mixed: the platform credits pay for browsers and computers, the model credits for tokens
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no session cap published; the monthly platform credit is the bound
  - free_tier_kind: recurring-credit
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · $5 model credits to start · $5/mo platform credits · no credit card needed to start · Bring your own Claude or ChatGPT subscription - agents run free on your plan', quoted
  - [1] 2026-11-03: browser runtime is priced per hour; no transfer figure is listed | capture: sha256:f8fcc3754cc593a352f62e042e7cfb3098bb36bd3e48efe3d85a092da5118a53 | quote: browser runtime$0.20/hr
  - [2] 2026-11-03: agents run in the cloud or on a machine | capture: sha256:9f4abeed0d3060a2eae2f2f1edf15f816f1003a1a1698fdb4f2fd706f0a76782 | quote: Specialized AI agents that do real work. They browse the web, use your tools, and run on schedules, in the cloud or on your machine.
- sources:
  - [1] https://opensteer.com/pricing
  - [2] https://opensteer.com/
