# Auriko

> auriko.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/auriko/ | JSON https://fshy.ajam.dev/api/v1/entity/auriko.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Auriko

- `inference/auriko` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference router
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://www.auriko.ai/pricing
- free tier: Free plan at USD 0 plus pay-as-you-go provider costs, with zero price markup: 1K platform RPM, 10K BYOK RPM, 5M BYOK monthly cap. Pro trial is 14 days with no credit card. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup for the free plan at auriko.ai; the page states no card, and BYOK needs the caller's provider keys
- interface: rest
- limits:
  - volume-quota (binding): Free plan 5M BYOK monthly cap [1]
  - request-rate: Free plan 1K platform RPM and 10K BYOK RPM [1]
- endpoint: https://api.auriko.ai/v1
- tooling: native Python and TypeScript SDKs, an OpenAI-compatible Chat Completions and Response API, and BYOK
- composes with: the 5M BYOK monthly cap and the need for the caller's own provider keys bind before the router markup, which is zero
- reliability: budget controls can cap spend at workspace or key level; a request over the platform RPM is throttled
- notes: the free plan grants routed requests but the caller supplies provider keys and pays provider token costs, so inference tokens are not free
- evidence:
  - [1] 2026-11-18: the Free plan has 1,000 platform RPM, 10,000 BYOK RPM and a 5M BYOK monthly cap, at USD 0 with zero provider price markup | capture: sha256:2916f8116945b82f96ba6231dfea5f9177a87cfb6820d3cbd7db918a9b093cfe | quote: - 1K platform RPM - 10K BYOK RPM - 5M BYOK monthly cap
- sources:
  - [1] https://www.auriko.ai/pricing
