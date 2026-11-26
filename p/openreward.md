# OpenReward Sandboxes

> openreward.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openreward/ | JSON https://fshy.ajam.dev/api/v1/entity/openreward.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenReward Sandboxes

- `compute/openreward` | fails-identity | evidence documented | binding write-gated | category container and VM sandbox
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T05:18:27.432Z (live) | stale on 2026-12-26
- url https://openreward.ai/pricing
- free tier: no free tier for compute: CPU USD 0.0504 per vCPU-hour, memory USD 0.0162 per GiB-hour and NVIDIA L4 GPU USD 1.51 per GPU-hour, billed by the second; credits exist only through an academic programme that has to be applied for | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
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
  - [1] 2026-11-25: the page states resources are paid for and billed by the second, with no free compute tier | capture: sha256:415c4eca29c66b35e2f27e19379ce588f225c10c17dc0a775dec7405089fd184 | quote: Simple, transparent pricing. You only pay for the resources you use, billed by the second.
  - [1] 2026-11-24: the pricing page states per-second billing with no free compute tier | capture: sha256:415c4eca29c66b35e2f27e19379ce588f225c10c17dc0a775dec7405089fd184 | quote: Simple, transparent pricing. You only pay for the resources you use, billed by the second.
  - [1] 2026-11-24: the only published credit route is an academic programme reached by contacting the vendor | capture: sha256:415c4eca29c66b35e2f27e19379ce588f225c10c17dc0a775dec7405089fd184 | quote: We support researchers with credits. Get in touch to learn more about our academic program.
- sources:
  - [1] https://openreward.ai/pricing
