# SCX.ai

> scx.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scx/ | JSON https://fshy.ajam.dev/api/v1/entity/scx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SCX.ai

- `inference/scx-ai` | paid-only | evidence documented | binding none | category inference gateway (sovereign infrastructure)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://scx.ai
- free tier: Open-weight and private models, deployed where you need them, at predictable cost per token. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign in at platform.scx.ai; the captured page states no free signup credit
- interface: rest
- limits:
  - volume-quota: per-token pricing; several sovereign models are price-on-application only [1]
- endpoint: https://api.scx.ai/v1
- composes with: The platform.scx.ai/docs route returned HTTP 403; the first-party apex page was used instead. No free allowance is published.
- reliability: not observed
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: SCX.ai sells per-token inference on open-weight models with no free tier stated | capture: sha256:0cbbf3555c9f630027408ed776834a8094c213d269df59d70855268f8060f40d | quote: Open-weight and private models, deployed where you need them, at predictable cost per token.
- sources:
  - [1] https://scx.ai
