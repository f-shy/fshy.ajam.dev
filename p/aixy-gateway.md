# Aixy

> aixy-gateway.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aixy-gateway/ | JSON https://fshy.ajam.dev/api/v1/entity/aixy-gateway.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aixy

- `inference/aixy` | paid-only | evidence documented | binding volume-quota | category inference gateway, BYOK
- needs card no, phone no, ID no, institution yes | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.aixy-gateway.com/quickstart.md
- free tier: No free allowance is stated on the quickstart read 2026-11-18: the operator connects their own provider API key, and model calls use that provider account and may incur charges. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: an organization/project with a connected provider API key is required before any model call
- interface: rest
- limits:
  - volume-quota (binding): charges accrue on the connected provider account; no Aixy free allowance stated [1]
- endpoint: https://api.aixy-gateway.com/v1
- tooling: an OpenAI-compatible key where offered, otherwise the vendor's own client
- composes with: the BYOK model is the scarce link: inference is billed to the user's own provider account, not free from Aixy
- reliability: model access and spend depend on the external provider account, whose quota Aixy does not control
- evidence:
  - [1] 2026-11-18: model calls use the connected provider account and may incur charges | capture: sha256:e14c024c7d5b54a661c12df7f5cf804be601d00207f525f7ac6a67594010534b | quote: Model calls use your provider account and may incur charges.
- sources:
  - [1] https://docs.aixy-gateway.com/quickstart.md
