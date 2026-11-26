# Exoscale

> exoscale.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/exoscale/ | JSON https://fshy.ajam.dev/api/v1/entity/exoscale.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Exoscale

- `compute/exoscale` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- identity a placeholder: card and phone unknown | verified 2026-11-25T11:17:39.909Z (live) | stale on 2026-12-26
- url https://www.exoscale.com/pricing/
- price parsed USD 35.61/mo
- free tier: no free instance: resources bill by the second with a flat rate across all zones and no up-front costs or long-term commitments; outbound traffic carries a free tier of 1.42 GiB an hour, with unused allowance reported on other running instances of the same organization | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
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
  - [1] 2026-11-25: outbound traffic has a 1.42 GiB free tier per instance | capture: sha256:b11080224cd26f2811a3f0c077b7459af6aca4378b71a0c40abfbfb322218ec7 | quote: Traffic is billed hourly and takes into account the number of virtual machines running during the last one-hour period. Effectively, there are 1.42 GiB of free output traffic per instance.
  - [1] 2026-11-25: the page states the 1.42 GiB free output tier per instance, its pooling across an organization and that excess traffic is billed | capture: sha256:b11080224cd26f2811a3f0c077b7459af6aca4378b71a0c40abfbfb322218ec7 | quote: Traffic is billed hourly and takes into account the number of virtual machines running during the last one-hour period. Effectively, there are 1.42 GiB of free output traffic per instance. If an instance doesn’t use its free tier, it is reported on other running instances of the same organization. So, with 5 instances running during the last hour, there are 7.1 GiB of free output traffic. The exceeding traffic is billed.
- sources:
  - [1] https://www.exoscale.com/pricing/
