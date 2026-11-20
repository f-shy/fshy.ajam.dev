# OpenReason

> openreason.app | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openreason/ | JSON https://fshy.ajam.dev/api/v1/entity/openreason.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenReason

- `inference/openreason` | paid-only | evidence documented | binding volume-quota | category inference spend monitoring (no inference endpoint)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://openreason.app/pricing
- free tier: No card to start. You stay on Free until you pass 10 engineers. | unit: users | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign up with Google or email; no card is required on the Free tier
- interface: rest
- limits:
  - volume-quota (binding): Free tier covers under 10 engineers; Pro is USD 20 per engineer per month [1]
- endpoint: https://api.openreason.app/v1
- composes with: The free tier is for spend reporting, not model inference. The product routes requests to the user's own provider plans or keys.
- reliability: the reporter reads local Claude Code and Codex session files; no upstream inference is served
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: OpenReason has a free spend-reporting tier for under 10 engineers with no card, but no free model inference endpoint | capture: sha256:12822621857a7d4681085db3f9fa4d8202f9fe83f066c5befdd0cd0da5db0675 | quote: No card to start. You stay on Free until you pass 10 engineers.
- sources:
  - [1] https://openreason.app/pricing
