# EmpirioLabs AI

> empiriolabs.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/empiriolabs/ | JSON https://fshy.ajam.dev/api/v1/entity/empiriolabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EmpirioLabs AI

- `inference/empiriolabs` | qualifies-with-caveat | evidence documented | binding none | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://empiriolabs.ai/pricing
- free tier: Free models at no cost, with a USD 0 starting balance; the Lite subscription is USD 19.90 a month. | unit: unlimited | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup is required; the page states no card for the free models
- interface: rest
- limits:
  - volume-quota: free models at no cost, with no stated cap [1]
- endpoint: https://api.empiriolabs.ai/v1
- tooling: the vendor console and an OpenAI-compatible key
- composes with: a free model list is the scarce link, because the paid catalogue needs the USD 19.90 subscription
- reliability: a free model list with no published rate limit, so a sweep depends on the vendor's throttling
- evidence:
  - [1] 2026-11-18: free models are offered at no cost while the Lite plan is USD 19.90 a month | capture: sha256:80f72d7754267d669ea66df5b0c90eb8069d810e0c5eb3906ae27253516d5bd7 | quote: Free models at no cost
- sources:
  - [1] https://empiriolabs.ai/pricing
