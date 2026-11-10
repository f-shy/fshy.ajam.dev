# Tart + Orchard

> tart.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tart/ | JSON https://fshy.ajam.dev/api/v1/entity/tart.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tart + Orchard (Cirrus Labs)

- `compute/tart-orchard` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding per-object-cap | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:09.501Z (live) | stale on 2026-11-22
- url https://tart.run/licensing/
- free tier: a Free Tier licence that applies with no purchase: 100 CPU cores across Tart and 4 Orchard workers; Gold is $12,000 a year for 500 cores and Platinum $36,000 for 3,000 | unit: objects | metered on: identity-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - per-object-cap (binding): 100 CPU cores across Tart and 4 Orchard workers on the Free Tier licence [1]
  - write-gated: the free licence applies by default; exceeding it requires a paid licence from $12,000 a year [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the licensing page was read on 2026-10-22 and states the free tier's two caps, with worked examples on either side of them. The unit is CPU cores rather than hours, and the examples make the boundary concrete
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon host
  - shape.note: the licence counts host CPU cores: 100 on Free, 500 on Gold, 3,000 on Platinum
  - session_cap.restart_required: no
  - session_cap.note: the cap is a core count, not a clock: 12 Mac Minis at 8 CPUs each fits, 13 does not
  - free_tier_kind: allowance
  - ps.price: a user's own Mac hardware
  - ps.durability: a user's own Macs
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: as long as a user keeps the hardware
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'By default, when no license is purchased, it is assumed that an organization is using a Free Tier license.' with 'Free Tier license has a 100 CPU core limit for Tart and 4 Orchard Workers limit for Orchard', and the worked examples: 12 Mac Minis with 8 CPUs each fits, 13 does not. Gold is $12,000 a year for 500 cores
- sources:
  - [1] https://tart.run/licensing/
