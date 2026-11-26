# NeoSmith

> neosmith.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neosmith/ | JSON https://fshy.ajam.dev/api/v1/entity/neosmith.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NeoSmith

- `inference/neosmith` | paid-only | evidence documented | binding none | category inference gateway (custom models)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://neosmith.ai/pricing
- free tier: No charge for setup, idle time or a training run that does not beat your current AI. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: a self-serve console exists in early access; no free text inference allowance stated
- interface: rest
- limits:
  - volume-quota: NeoSmith Code tiers bill per million tokens; Model Factory is quoted per job [1]
- endpoint: https://router.neosmith.ai/v1
- composes with: The word Free on the pricing page covers unshipped training runs and idle time, not free inference.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: NeoSmith charges per job or per million tokens, with free only for setup, idle time and failed training runs | capture: sha256:72672758b6baa69e4db817566873479ef169e45ccee1ed70a76dc3fcdbf29d2d | quote: No charge for setup, idle time or a training run that does not beat your current AI.
- sources:
  - [1] https://neosmith.ai/pricing
