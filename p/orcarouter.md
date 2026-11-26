# OrcaRouter

> orcarouter.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/orcarouter/ | JSON https://fshy.ajam.dev/api/v1/entity/orcarouter.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OrcaRouter

- `inference/orcarouter` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://docs.orcarouter.ai/routing/free-models.md
- free tier: Models ending in -free are priced at $0 and never touch the wallet; they are limited by per-minute and per-day request ceilings and, on the lowest tier, a per-request prompt-size cap, with an established GitHub account required to avoid an access-denied rejection. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an established GitHub account linked to the workspace owner is required unless lifetime spend exempts it
- interface: rest
- limits:
  - request-rate (binding): -free ids have rpm/rpd windows and a per-request prompt cap on the lowest tier; numbers published live at GET /api/free-package/public [1]
- endpoint: https://api.orcarouter.ai/v1
- composes with: the per-request prompt cap and the GitHub link gate bind before the rate windows
- reliability: free ids never fall back to paid and the lineup rotates as capacity allows
- evidence:
  - [1] 2026-11-18: the -free tier serves models at $0 under a suffix, limited by request windows and a prompt cap | capture: sha256:1151d26cc9c31ee0885230b6f9378a1f2afc0eb4e97657832c33ea2436d3a995 | quote: Some models are served at no charge under a model id ending in
- sources:
  - [1] https://docs.orcarouter.ai/routing/free-models.md
