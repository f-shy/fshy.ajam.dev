# Capy

> capy.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/capy/ | JSON https://fshy.ajam.dev/api/v1/entity/capy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Capy

- `compute/capy` | paid-only | evidence documented | binding write-gated | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:03:49.122Z (live) | stale on 2026-12-26
- url https://capy.ai
- free tier: $0 on your own computers, with agents on your own computers, your own subscriptions and keys, 100 review credits a month, Captains and integrations and unlimited members. Paid plans include machine minutes, review credits and model usage every month; the entry paid tier is Capy Lite at $1first week, then $20/mo billed monthly with 30,000 machine minutes, 250 review credits, $20 of model usage and machines up to 4 CPU / 16 GB | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
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
  - [1] 2026-11-25: the pricing page states a $0 free tier for one's own computers and the Capy Lite paid tier at $1 first week then $20 a month with its machine minutes, credits and CPU/RAM ceiling | capture: sha256:0a0ec8890e04b6d7feb83102a74b5f48b9e2d10e9a525cd22b2b57f529ad24e3 | quote: Free on your own computers. Paid plans include machine minutes, review credits and model usage every month. Unlimited members on every plan. ... $0 ... - Agents on your own computers - Your own subscriptions and keys - 100 review credits a month - Captains and integrations - Unlimited members ... $1first week, then $20/mo ... Billed monthly ... - 30,000 machine minutes - 250 review credits - $20 of model usage - Machines up to 4 CPU / 16 GB
  - [1] 2026-11-25: the pricing page still states the $0 own-computers tier and the Capy Lite price and shape | capture: sha256:0a0ec8890e04b6d7feb83102a74b5f48b9e2d10e9a525cd22b2b57f529ad24e3 | quote: Free on your own computers. Paid plans include machine minutes, review credits and model usage every month. Unlimited members on every plan. ... $0 ... - Agents on your own computers - Your own subscriptions and keys - 100 review credits a month - Captains and integrations - Unlimited members ... $1first week, then $20/mo ... Billed monthly ... - 30,000 machine minutes - 250 review credits - $20 of model usage - Machines up to 4 CPU / 16 GB
- sources:
  - [1] https://capy.ai
