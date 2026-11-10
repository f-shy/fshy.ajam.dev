# Green Mini host

> greenmini.host | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/greenmini/ | JSON https://fshy.ajam.dev/api/v1/entity/greenmini.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Green Mini host

- `compute/greenmini` | paid-only | evidence documented | binding request-rate | category macOS host
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:00.063Z (live) | stale on 2026-11-22
- url https://portal.greenmini.host/checkout/order
- free tier: no free tier: dedicated Apple hardware from EUR 59 a month, with M4 and M6 configurations from EUR 85 | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): EUR 59 to EUR 148 a month depending on the Mac; no hourly rate and no free tier [1]
  - retention-clamped: delivery is quoted per configuration: under 24 hours for one M4 build, up to 3 business days for others [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the order page was read on 2026-10-22 and prices the hardware ladder. The product is a monthly rental of a Mac, which is paid-only
- extras:
  - keep_rate: 1.0
  - keep_rate_basis: always-on by contract
  - billing_model: unclassified
  - shape.vcpu: 10
  - shape.ram: 16
  - shape.disk: 512
  - shape.gpu_class: Apple M4
  - shape.gpu_count: 1
  - shape.note: M4 10-core CPU and 10-core GPU, 16 GB unified memory, 512 GB SSD at EUR 87 a month
  - session_cap.restart_required: no
  - session_cap.note: a monthly rental with no session clock; the machine belongs to the account for the month
  - free_tier_kind: none
  - granularity.min_billed_s: 0
  - ps.gib: 512
  - ps.price: included in the monthly price
  - ps.durability: dedicated SSD
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the checkout page was read on 2026-10-22 and prices Mac mini and Mac Studio hosting from EUR 59 to EUR 148 a month: 'M4 10/10C · 16GB · 512GB SSD €87,00/mo', 'M6 12C/12C · 16GB · 256GB SSD €85,00/mo'. There is no free tier and no free month
- sources:
  - [1] https://portal.greenmini.host/checkout/order
