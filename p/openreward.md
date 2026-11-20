# OpenReward Sandboxes

> openreward.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openreward/ | JSON https://fshy.ajam.dev/api/v1/entity/openreward.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenReward Sandboxes

- `compute/openreward` | fails-identity | evidence documented | binding write-gated | category container and VM sandbox
- needs card no, phone no, ID no, institution yes | verified 2026-10-22T04:47:36.024Z (live) | stale on 2026-11-22
- url https://openreward.ai/pricing
- free tier: no free tier for compute: resources bill by the second per vCPU-hour; credits exist only through an academic programme that has to be applied for | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: institution | detail: 'We support researchers with credits. Get in touch to learn more about our academic program.' - the free path is an academic programme, quoted from openreward.ai/pricing read 2026-10-22
- interface: unknown
- limits:
  - request-rate: per vCPU-hour, billed by the second [1]
  - write-gated (binding): the only free credit route is an academic programme that must be applied for [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states per-second billing with no free allowance. The only credit is an academic programme, which is an identity gate rather than a tier
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: billed by the second; the page states no clock
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Simple, transparent pricing. You only pay for the resources you use, billed by the second.' with a per-vCPU-hour rate and 'We support researchers with credits. Get in touch to learn more about our academic program.', quoted
- sources:
  - [1] https://openreward.ai/pricing
