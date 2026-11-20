# Meganova

> meganova.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/meganova/ | JSON https://fshy.ajam.dev/api/v1/entity/meganova.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Meganova

- `inference/meganova` | qualifies-with-caveat | evidence documented | binding request-rate | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:33.000Z (live) | stale on 2026-12-19
- url https://docs.meganova.ai/tiers.md
- free tier: Tier 1 gives free registration with no credit card, free access to models under 100B (including Manta Mini), 50-500 free-model requests per day and a 20-200 RPM limit; higher tiers require a USD 1, 10 or 100 payment. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: Tier 1 registration is free and needs no credit card
- interface: rest
- limits:
  - request-rate (binding): Tier 1: 50-500 free-model requests per day and 20-200 RPM [1]
- endpoint: https://api.meganova.ai/v1
- composes with: the Tier 1 daily request cap and the under-100B model restriction bind first
- reliability: free models on Tier 1 are capped at under 100B and at a low daily request count
- notes: Tier 1 comparison table lists 50-500 free-model RPD and 20-200 RPM.
- evidence:
  - [1] 2026-11-18: Tier 1 gives free access to models under 100B including Manta Mini without a card | capture: sha256:81c7bfa9c6b1b07adceafda5f1b5fd36c3e5bc951781c09779e0a86807f941da | quote: Free Access Models (<100B), including Manta Mini
- sources:
  - [1] https://docs.meganova.ai/tiers.md
