# smol machines

> smolmachines.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/smolmachines/ | JSON https://fshy.ajam.dev/api/v1/entity/smolmachines.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## smol machines

- `compute/smol-machines` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:03.850Z (live) | stale on 2026-11-22
- url https://smolmachines.com/pricing
- free tier: $100 of one-time credit that behaves as ordinary prepaid balance and does not expire; a running machine costs $0.04 an hour as a base plus $0.05 a vCPU-hour and $0.0162 a GB-hour of memory | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.04 a machine-hour as a base for the isolated slot, plus $0.05 a vCPU-hour and $0.0162 a GB-hour of memory [1]
  - per-object-cap: an accounting model on active RSS and used disk, not on provisioned size: disk is $0.0001 a GB-hour used [1]
  - per-ip-shaping: network egress is $0.05 a GB [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The pricing page read on 2026-10-22 documents a one-time signup credit that does not expire and a base-plus-usage billing model.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 8
  - shape.ram: 16
  - shape.note: the free plan allows 8 vCPU and 16 GB per machine; the disk limit is stated as not published
  - session_cap.restart_required: no
  - session_cap.note: idle apps scale to zero on every paid plan; the base fee applies only while a machine is running, with a one-minute minimum
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 60
  - burst_x: 1.0
  - ps.price: $0.0001 a GB-hour used, about $0.073 a GB-month
  - ps.durability: disk billed on bytes used
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the machine exists
  - net.out: yes
  - net.in: yes
  - net.allowance: $0.05 a GB of egress
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Sign-up credit is granted once. New accounts receive $100.00 of credit when they are created. It is ordinary prepaid balance: it is drawn down as you use the platform, it does not reset monthly, and whatever is left stays yours.' with 'Base (running machine) per machine-hour running (1-minute minimum) $0.04' and 'Memory (active RSS) per GB-hour in use $0.0162', quoted
- sources:
  - [1] https://smolmachines.com/pricing
