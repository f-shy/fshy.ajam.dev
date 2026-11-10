# Capy

> capy.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/capy/ | JSON https://fshy.ajam.dev/api/v1/entity/capy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Capy

- `compute/capy` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T04:46:28.287Z (live) | stale on 2026-11-22
- url https://capy.ai
- free tier: no free tier: the entry offer is $1 for 7 days on a verified card, then $20 a month | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: card | detail: 'Your first week costs $1 with a verified card' - the card is the gate to the entry price, quoted from capy.ai read 2026-10-22
- interface: unknown
- limits:
  - request-rate: $1 for the first 7 days, then $20 a month with $20 of credits [1]
  - per-object-cap: cloud machines up to 4 CPU and 16 GB on the $20 tier, 8 CPU and 32 GB on the $100 tier [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes only paid tiers, with a $1 first week behind a verified card. That is a discounted first period, not a free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 4
  - shape.ram: 16
  - shape.note: the ceiling on the $20 tier; 8 CPU and 32 GB on $100
  - session_cap.restart_required: no
  - session_cap.note: plans set monthly credits and cloud machine limits; the page states no machine clock
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Your first week costs $1 with a verified card, then $20/mo' and 'Unlimited members on every plan. Plans set your monthly credits and cloud machine limits' with 'Cloud machines up to 4 CPU / 16 GB' at the $20 tier, quoted
- sources:
  - [1] https://capy.ai
