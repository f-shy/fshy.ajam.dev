# OpenComputer

> opencomputer.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/opencomputer/ | JSON https://fshy.ajam.dev/api/v1/entity/opencomputer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenComputer

- `compute/opencomputer` | paid-only | evidence documented | binding per-object-cap | category container and VM sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-10-22T04:47:37.000Z (live) | stale on 2026-11-22
- url https://opencomputer.dev/
- price parsed USD 275.94/mo
- free tier: a Free tier with up to 2 shared vCPU, 2 GB of memory, 3 GB of disk and 5 concurrency, on a machine that stays always on | unit: objects | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not stated
- egress: not published | metered: no | source: [1]
- identity: card | detail: a plan requires a payment
- interface: unknown
- limits:
  - request-rate: 5 concurrency on Free, 50 on Medium and 500 on Large [1]
  - per-object-cap (binding): up to 2 shared vCPU, 2 GB of memory and 3 GB of disk on Free [1]
  - retention-clamped: hibernate keeps the machine; the page describes persistent state as the product [1]
- limits note: USD 0.0063 a minute is USD 0.378 an hour, which is twenty times the cheap sandbox tier
- binding note: the 2 vCPU / 4 GB shape at USD 0.0063 a minute is the ceiling; there is no larger shape at that rate
- interface detail: an API that provisions a machine
- tooling: an API and plan-granted credits
- composes with: the plan credits are the mechanism: 10 times the price in prepaid usage
- reliability: no reliability event recorded
- notes: OpenComputer provides cloud compute with promotional account credits that reduce initial instance costs below published list rates.
- evidence note: the site was read on 2026-10-22. It states a Free tier by shape rather than by credit, which contradicts the USD 10 credit the record carried, and it states the persistence model: always on, with hibernate and wake
- extras:
  - shape.vcpu: 2
  - shape.ram: 2
  - shape.disk: 3
  - shape.note: Free is shared, up to 2 vCPU and 2 GB with 3 GB of disk; Medium is 8 CPU, 16 GB and 50 GB for $300 a month
  - billing_model: allocated
  - session_cap.restart_required: no
  - session_cap.note: always on by default with hibernate and wake as a user choice; the page states no reap, and it sells the persistence
  - free_tier_kind: allowance
  - m10h_usd: 113.4
  - m24h_usd: 275.94
  - price_note: USD 0.0063 a minute is USD 0.378 an hour, so 300 hours is USD 113.40 and 730 is USD 275.94. A plan at 10 times its price in credits cuts the effective rate.
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.gib: 3
  - ps.price: disk is addable on the paid tiers
  - ps.durability: persistent filesystem
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.ports: preview URLs expose ports with auth and custom domains
- evidence:
  - [1] 2026-10-02: USD 0.0063 a minute at 2 vCPU and 4 GB; the USD 20 and USD 200 plans grant 10 times their price in credits
  - [1] 2026-10-22: 'Persistent VMs: Always on with elastic resizing. Scale memory and CPU at runtime, or hibernate and wake when needed.' with 'Free: shared upto 2vCPU, shared upto 2GB memory, 3GB disk, 5 concurrency', 'Medium ($300/mo): 8 CPU, 16GB memory, 50GB disk', 'Large ($3,000/mo): 64 CPU, 512GB memory, 3800GB disk', quoted
- sources:
  - [1] https://opencomputer.dev/
