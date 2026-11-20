# Latitude.sh

> latitude.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/latitude/ | JSON https://fshy.ajam.dev/api/v1/entity/latitude.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Latitude.sh

- `compute/latitude-sh` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:17.953Z (live) | stale on 2026-11-22
- url https://www.latitude.sh/pricing
- free tier: no free compute tier: metal, VM and GPU instances are priced with 20 TB of free outbound per month and unlimited inbound; a yearly commitment is 65% cheaper than hourly | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: hourly, monthly or yearly billing with 50% and 65% discounts for the longer terms [1]
  - per-ip-shaping (binding): 20 TB of free outbound a month and unlimited inbound on every plan; up to 200 Gbps of network on metal [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and publishes the instance tables with the egress allowance. There is no free instance, so the verdict moves to paid-only, and the 20 TB egress is the fact that decides it for a high-transfer workload.
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: instances bill by the hour, month or year; the page states no reap
  - free_tier_kind: none
  - burst_x: 1.0
  - burst_bill: min 1 h
  - ps.price: storage is priced on a separate page
  - ps.durability: NVMe or block volume
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the instance exists
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.allowance: 20 TB a month outbound free, unlimited inbound
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Network 20 TB free out / ∞ in' on the Metal, VM and bare-metal tables, and 'Paid yearly 65% cheaper than hourly' with 'Monthly 50% cheaper than hourly', quoted
- sources:
  - [1] https://www.latitude.sh/pricing
