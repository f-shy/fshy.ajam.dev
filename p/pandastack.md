# PandaStack

> pandastack.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pandastack/ | JSON https://fshy.ajam.dev/api/v1/entity/pandastack.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PandaStack

- `compute/pandastack` | qualifies-with-caveat | evidence documented | binding per-object-cap | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:38.758Z (live) | stale on 2026-11-22
- url https://www.pandastack.ai/pricing/
- free tier: a $5.40 free credit, 1 GiB of persistent volume on Free, no charge for egress or inbound on any plan, and hibernation that writes state to disk and stops CPU and RAM metering | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: $5.40 of free credit; a sandbox-hour is metered per second [1]
  - per-object-cap (binding): 1 GiB of persistent volume on Free, 100 GiB on Pro and 2.5 TiB on Team [1]
  - retention-clamped: hibernation writes state to disk and stops metering, and hibernated storage is not billed while that holds [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing FAQ was read on 2026-10-22 and states the credit, the volume quotas and the hibernate and egress rules. The hibernate answer is the state axis and the egress answer is the network axis, both from one page
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: hibernation is a user action; it writes state to disk and stops CPU and RAM metering, and the page states no automatic reap
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.gib: 1
  - ps.price: hibernated state storage is currently included at no extra charge
  - ps.durability: persistent volume plus hibernated state on disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.allowance: egress and inbound are free on every plan, metered for fair use
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'No. Hibernation writes state to disk and stops active vCPU/RAM metering. Storage for hibernated state is currently included at no extra charge.' and 'We don't charge for outbound transfer on any plan, and inbound is free too' and 'What's the $5.40 free credit?' with a Free volume quota of 1 GiB, quoted
- sources:
  - [1] https://www.pandastack.ai/pricing/
