# CLOUDV

> cloudv.kr | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloudv/ | JSON https://fshy.ajam.dev/api/v1/entity/cloudv.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CLOUDV

- `compute/cloudv` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.cloudv.kr/server/index.html
- free tier: The MAXIO Linux virtual server is 1 core, 2 GB RAM, 100 GB SSD on a 6 Gbps RAID array with 1,200 GB of monthly traffic at KRW 31,500 a month, provisioned immediately. Traffic is billed outbound only, inbound is free, excess is KRW 70 per GB billed the following month, and the vendor states that it does not throttle the port when the allowance is exceeded. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the billing page states that only outbound traffic is charged, that inbound is not charged, that the basic allowance is 2,400GB on a leased server with 70 per GB above it billed the following month, and that the connection is not throttled when the allowance is exceeded | metered: yes | source: [2]
- identity: card
- interface: rest
- limits:
  - volume-quota (binding): 1,200 GB of monthly outbound, then KRW 70 per GB with no bandwidth throttle, which means an unattended job that moves a terabyte over the allowance adds KRW 70,000 to the invoice instead of failing. [1]
- limits note: 1,200 GB of monthly outbound, then KRW 70 per GB with no bandwidth throttle, which means an unattended job that moves a terabyte over the allowance adds KRW 70,000 to the invoice instead of failing.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The no-throttle policy makes CLOUDV different from the rest of the Korean market: every other host found either throttles or stops at the allowance, and CLOUDV turns an overrun into an invoice instead.
- reliability: no reliability event recorded
- notes: CLOUDV is the cloud brand of SmileServ, the same company that runs iwinv, so the two records describe one operator at two price points: iwinv is the per-day shared line at KRW 5,600, CLOUDV is the monthly RAID-backed box at KRW 31,500. Prices exclude VAT. The vendor also lists bare-metal leases by the month with a 24-month term, which are not virtual machines and are recorded here only as the shape above them.
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 2
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the page lists 가상서버-VPS MAXIO LINUX at 31,500 원 a month with 1Core, 2GB RAM, SSD 100GB and 1,200GB of traffic, on 6Gbps SSD RAID, available immediately
  - [2] 2026-10-22: the billing page states that only outbound traffic is charged, that inbound is not charged, that the basic allowance is 2,400GB on a leased server with 70 원 per GB above it billed the following month, and that the connection is not throttled when the allowance is exceeded
  - [3] 2026-10-22: the vendor states that its own IDC in Gasan keeps low traffic rates and bills outbound only
- sources:
  - [1] https://www.cloudv.kr/server/index.html
  - [2] https://www.cloudv.kr/customer/billing.html
  - [3] https://www.cloudv.kr/modal/feature/payment.html
