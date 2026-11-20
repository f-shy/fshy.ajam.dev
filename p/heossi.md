# Bee by HEOSSI

> heossi.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/heossi/ | JSON https://fshy.ajam.dev/api/v1/entity/heossi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bee by HEOSSI

- `inference/bee` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://bee.heossi.com
- free tier: Bee Cell and API Free are free to start, no card required, with a real OpenAI-compatible API and a generous 5-hour refilling token window backed by a 2M monthly ceiling. | unit: tokens | metered on: wall-clock | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a Bee workspace account; the page states no card required for the free plan
- interface: rest
- limits:
  - volume-quota (binding): 2M monthly token ceiling with a 5-hour refilling token window on the free plan [1]
  - request-rate: the free tier refills a token window every 5 hours [1]
- endpoint: https://api.bee.heossi.com/bee
- tooling: the vendor @heossihq/bee and bee-sdk clients, OpenAI-compatible Chat Completions, MCP and OpenCode integration
- composes with: the 5-hour refilling token window and 2M monthly ceiling bind before the specialist tiers
- reliability: post-quantum protection is applied on every plan; ordinary inference runs on the classical path and QPU jobs are separate and metered
- notes: the free plan has no card gate and a real API, but a 5-hour refilling token window and a 2M monthly ceiling constrain sustained use
- evidence:
  - [1] 2026-11-18: Bee Cell and API Free are free with no card, an OpenAI-compatible API, a 5-hour refilling token window and a 2M monthly ceiling | capture: sha256:d0844787aedd8aef03b240b26b39489be994def1ee8a5aa5e86f30600b7acfbb | quote: Yes. Bee Cell and API Free are free to start - post-quantum-protected, hosted, no card required, with a real OpenAI-compatible API, document retrieval, and a generous 5-hour refilling token window backed by a 2M monthly ceiling.
- sources:
  - [1] https://bee.heossi.com
