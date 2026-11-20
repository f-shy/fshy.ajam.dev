# JoinGonka

> joingonka.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/joingonka/ | JSON https://fshy.ajam.dev/api/v1/entity/joingonka.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JoinGonka

- `inference/joingonka` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://gate.joingonka.ai/docs/models
- free tier: No free inference allowance is stated. Prices are in dollars per 1M tokens at the current GNK rate and charges are in GNK; the model lineup changes through network votes. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a gateway key is needed for inference; public model and capability endpoints need no key
- interface: rest
- limits:
  - volume-quota (binding): charges in GNK at a dollar-per-million-token reference rate [1]
- endpoint: https://gate.joingonka.ai/v1
- tooling: an OpenAI-compatible gateway reachable through the Gonka network, with public model, capability and status endpoints
- composes with: the GNK-denominated charge and the network-voted lineup are the scarce links; no free tier is published
- reliability: a model the network stops serving disappears from GET /v1/models and returns 503 model_unavailable; a larger max_tokens is silently trimmed to the model cap
- notes: no standing free inference allowance is published; charges are in GNK and the lineup is set by network votes
- evidence:
  - [1] 2026-11-18: gateway prices are shown in dollars per million tokens but charges are in GNK; the model lineup is set by network votes | capture: sha256:50d81a5df4800661260b90eb095586c22dc6c6c9efe94f36b2c538932878e7ce | quote: Prices are in dollars per 1M tokens at the current GNK rate; charges are in GNK
- sources:
  - [1] https://gate.joingonka.ai/docs/models
