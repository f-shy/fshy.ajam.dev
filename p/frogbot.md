# FrogBot

> frogbot.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/frogbot/ | JSON https://fshy.ajam.dev/api/v1/entity/frogbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FrogBot

- `inference/frogbot` | self-hosted, last resort | verdict paid-only | evidence documented | binding volume-quota | category self-hosted inference gateway, BYOK
- needs card no, phone no, ID no, institution yes | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.frogbot.ai/gateway/overview.md
- free tier: The gateway holds upstream keys and does not authenticate callers itself. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: the operator must supply upstream provider API keys to route any model call
- interface: rest
- limits:
  - volume-quota (binding): no FrogBot-hosted free allowance stated [1]
- endpoint: https://app.frogbot.ai/api/v1
- tooling: an OpenAI-compatible key where offered, otherwise the vendor's own client
- composes with: the software is self-hosted and the user supplies all inference credentials; no free hosted inference is published
- reliability: the gateway does not authenticate callers on its own; abuse protection must be added by the operator
- notes: self-hosted: the free part serves no inference itself; it routes to the operator's paid provider keys.
- self hosted: yes
- evidence:
  - [1] 2026-11-18: the gateway holds upstream keys and does not authenticate callers | capture: sha256:b5c8b1cc3295245755faa7874d61b13c051aba42220e26f0607478a23645f389 | quote: the gateway does not authenticate callers on its own
- sources:
  - [1] https://docs.frogbot.ai/gateway/overview.md
