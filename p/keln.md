# Keln

> keln.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keln/ | JSON https://fshy.ajam.dev/api/v1/entity/keln.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Keln

- `inference/keln` | paid-only | evidence documented | binding volume-quota | category agent sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.keln.ai/models-pricing/
- free tier: No free allowance is stated on the pricing page read on 2026-11-18: sandbox time is USD 0.0001 a second on top of tokens, with a 30-second minimum (USD 0.003) for an answer that runs code. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a funded account is required before a sandbox runs
- interface: rest
- limits:
  - volume-quota (binding): USD 0.0001 per second of sandbox time with a 30-second minimum per code-running answer [1]
- endpoint: https://api.keln.ai/v1
- tooling: the vendor API with a code-execution sandbox
- composes with: the 30-second minimum is the scarce link, because a short run still bills the full half minute
- reliability: a per-second meter with a minimum means latency costs money independently of tokens
- evidence:
  - [1] 2026-11-18: sandbox time is USD 0.0001 a second on top of tokens with a 30-second minimum of USD 0.003 per code-running answer | capture: sha256:f5c13a7ea5a568b960ec1a73b86152df95d9016f795ebf9273054741e0d3ee03 | quote: - Code execution bills per second of sandbox time, on top of tokens. Details ↗
- sources:
  - [1] https://docs.keln.ai/models-pricing/
