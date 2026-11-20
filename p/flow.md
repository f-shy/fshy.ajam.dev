# Flow Swiss Mac Bare Metal

> flow.swiss | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flow/ | JSON https://fshy.ajam.dev/api/v1/entity/flow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Flow Swiss Mac Bare Metal

- `compute/flow-swiss-mac` | paid-only | evidence documented | binding retention-clamped | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:52.367Z (live) | stale on 2026-11-22
- url https://doc.flow.swiss/platform/pricing/mac-bare-metal
- free tier: no free tier: Mac hardware from CHF 0.27 an hour or CHF 199 a month, with a 24-hour minimum allocation and billing while the device is stopped | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - retention-clamped (binding):  [1]
  - request-rate: CHF 0.27 an hour or CHF 199 a month [1]
  - per-ip-shaping: 20 TB of outbound traffic a month is included; inbound and internal traffic is free [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the Mac bare-metal pricing page was read on 2026-10-22 and states the hourly rate, the 24-hour minimum, that a stopped device still bills, and the 20 TB egress allowance. The record's USD 24 credit is not on the page
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.gpu_class: Apple Silicon
  - shape.gpu_count: 1
  - shape.note: Mac mini and Mac Studio on demand, with instant activation
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: a 24-hour minimum allocation forced by Apple's licence, and a stopped device still bills, so stopping is not a pause
  - free_tier_kind: none
  - granularity.min_billed_s: 86400
  - ps.price: SSD priced as a separate line
  - ps.durability: SSD on the device
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the allocation
  - net.out: yes
  - net.in: yes
  - net.ports: a free elastic public IPv4 per device
  - net.static_ip: yes
  - net.allowance: 20 TB a month outbound per organisation account
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Billing is per hour with a 24-hour minimum allocation period to comply with the Apple macOS License Agreement. Billing also takes place when the device is' stopped, 'Starting at CHF 0.27/hr or CHF 199/mo', 'Each Mac device comes with a free elastic public IPv4 address' and '20 TB of outbound traffic per month is included', quoted
- sources:
  - [1] https://doc.flow.swiss/platform/pricing/mac-bare-metal
