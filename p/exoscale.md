# Exoscale

> exoscale.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exoscale/ | JSON https://fshy.ajam.dev/api/v1/entity/exoscale.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Exoscale

- `compute/exoscale` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:46:50.454Z (live) | stale on 2026-11-22
- url https://www.exoscale.com/pricing/
- price parsed USD 35.61/mo
- free tier: no free instance: resources bill by the second across all zones, with outbound traffic carrying a free tier of 1.42 GiB an hour and inbound traffic free | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate: billed by the second with a flat rate across zones and no commitment [1]
  - per-ip-shaping (binding): outbound traffic carries a free tier of 1.42 GiB an hour, about 34 GiB a day; inbound and intra-zone traffic are free [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: The 1.42 GiB an hour outbound free tier provides high-transfer bandwidth.
- extras:
  - keep_rate: 1.0
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: an instance can be started, stopped and scaled with no penalty; the page states no reap
  - price_note: a VPS bills by the month with an hourly rate capped at the monthly figure, so the two columns answer two questions: destroying the box between runs versus keeping it up.
  - free_tier_kind: none
  - m10h_usd: 14.0
  - m24h_usd: 35.61
  - price_basis: 10 h/day column = 300 h at the hourly rate, which is what a server destroyed between runs costs; 24/7 column = the monthly cap, because a VPS kept up all month stops at the cap.
  - burst_x: 1.0
  - ps.price: local SSD is part of the instance; block storage is priced separately
  - ps.durability: local SSD or block volume
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the volume exists
  - net.out: yes
  - net.in: yes
  - net.ports: any
  - net.static_ip: yes
  - net.ipv6: yes
  - net.allowance: 1.42 GiB an hour free outbound, about 34 GiB a day
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Resources are billed by the second, with a no-surprise flat rate across all zones. No up-front costs, and no long-term commitments.' with 'Traffic OUTBOUND: free tier of 1.42 GiB / hr', 'Traffic INBOUND: FREE' and 'Traffic INTRA: between all instances FREE', quoted
- sources:
  - [1] https://www.exoscale.com/pricing/
