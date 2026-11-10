# Ubicloud

> ubicloud.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ubicloud/ | JSON https://fshy.ajam.dev/api/v1/entity/ubicloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ubicloud

- `compute/ubicloud` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:17.000Z (live) | stale on 2026-11-22
- url https://www.ubicloud.com/docs/about/pricing
- price parsed USD 22.46/mo
- free tier: no free tier: billed by the minute on provisioned resources, with GitHub Actions runners from $0.00125 a minute for 2 vCPU and 8 GB and burstable VMs from $10.47 a month | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): billed per minute on provisioned resources: $0.00125 a minute for a 2 vCPU, 8 GB runner [1]
  - request-rate (binding): premium runners fall back to standard ones when capacity is full, with no extra wait [1]
  - per-object-cap: runners include dedicated CPU, memory, local block storage and a public IPv4 [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the per-minute and monthly rates with a direct comparison against GitHub. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - shape.vcpu: 2
  - shape.ram: 8
  - shape.disk: 40
  - shape.note: the standard-2 runner: 2 vCPU, 8 GB and 40 GB of block storage
  - session_cap.restart_required: no
  - session_cap.note: a runner exists for the job and is billed by the minute; burstable VMs start at $10.47 a month
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: none
  - m10h_usd: 9.36
  - m24h_usd: 22.46
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - burst_x: 1.0
  - ps.gib: 40
  - ps.price: included with the runner
  - ps.durability: local block storage
  - ps.on_stop: no
  - ps.on_destroy: no
  - ps.retention: the job's lifetime
  - net.out: yes
  - net.in: yes
  - net.ports: a public IPv4 address is included with the runner
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Billing is based on the resources provisioned, pro-rated for the time they are provisioned. We calculate resource consumption at per minute granularity and bill monthly.' with the GitHub Actions table '2 vCPU 8GB $0.00125/min on Ubicloud vs $0.00600/min on GitHub' and 'Burstable VMs start at $10.47/month', quoted
- sources:
  - [1] https://www.ubicloud.com/docs/about/pricing
