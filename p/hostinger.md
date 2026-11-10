# Hostinger VPS

> hostinger.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostinger/ | JSON https://fshy.ajam.dev/api/v1/entity/hostinger.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hostinger VPS

- `compute/hostinger-vps` | paid-only | evidence documented | binding request-rate | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:06.000Z (live) | stale on 2026-11-22
- url https://www.hostinger.com/vps-hosting
- price parsed USD 14.99/mo
- free tier: no free tier: VPS from $6.49 a month on a two-year term, renewing at $11.99 a month, with 1 vCPU, 50 GB of NVMe and 4 TB of bandwidth | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $6.49 a month on a two-year term, renewing at $11.99; the entry shape is 1 vCPU and 50 GB of NVMe [1]
  - per-ip-shaping: 4 TB of bandwidth on the entry plan [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the VPS page was read on 2026-10-22 and prices the ladder with its renewal rates. There is no free tier and no trial credit, only a 30-day money-back guarantee
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - shape.vcpu: 1
  - shape.disk: 50
  - shape.note: the entry plan: 1 vCPU, 50 GB of NVMe, 4 TB of bandwidth
  - session_cap.restart_required: no
  - session_cap.note: a monthly VPS with root access; no session clock
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: none
  - m10h_usd: 10.06
  - m24h_usd: 14.99
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - granularity.min_billed_s: 3600
  - burst_x: 1.0
  - burst_bill: min 1 h
  - ps.gib: 50
  - ps.price: included in the monthly price
  - ps.durability: NVMe
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the rental term
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.ipv6: yes
  - net.allowance: 4 TB a month on the entry plan
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'From $6.49/mo' with 'Renews at $11.99/mo for 2 years', '1 vCPU core', '50 GB NVMe disk space', '4 TB bandwidth', and '30-day money-back guarantee', quoted
- sources:
  - [1] https://www.hostinger.com/vps-hosting
