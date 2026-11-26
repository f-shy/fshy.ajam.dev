# XDN IDC

> xdn.kr | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xdn/ | JSON https://fshy.ajam.dev/api/v1/entity/xdn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## XDN IDC

- `compute/xdn-idc` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T15:03:48.800Z (live) | stale on 2026-12-26
- url https://idc.xdn.kr/vm.html
- free tier: | VM-XS | 1 | 1GB | 25GB | 600GB/월 | 5,040원 | | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: the price table gives VM-XS as 1 vCPU, 1 GB, 25 GB HDD and 600 GB monthly outbound at 5,040, and lists VM-S at 11,790, VM-M at 21,600, VM-L at 31,500 and VM-XL at 41,400, all on a 12-month commitment with inbound unlimited; the page also states overage at 70 per GB to 1,000 GB and 60 per GB above, and an extra public IP at 3,300 a month | metered: yes | source: [1]
- identity: card
- interface: unknown
- limits:
  - volume-quota (binding): 600 GB of monthly outbound, then KRW 70 per GB; the 12-month commitment is the second constraint, because the price is quoted only on that term and a 24-month term discounts it 5 percent and 36 months 10 percent. [1]
- limits note: 600 GB of monthly outbound, then KRW 70 per GB; the 12-month commitment is the second constraint, because the price is quoted only on that term and a 24-month term discounts it 5 percent and 36 months 10 percent.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At KRW 5,040 on an annual term this is the lowest Korean monthly figure found, and it is the shape a reseller competes on: the same page prices a competitor's entry box at KRW 4,500 with a 30 percent promotion, which is the actual Korean floor for a 1 GB shared box.
- reliability: no reliability event recorded
- notes: XDN is a one-site reseller in Seoul and its page is written as a price comparison against iwinv, which it names; the comparison rows are reported and the XDN rows are documented. The disk is HDD, not NVMe, which is why the price undercuts iwinv. A reseller of this size carries the reliability risk this class is defined by, and no suspension or disappearance event was found for it, so the reliability note is that nothing was observed either way.
- extras:
  - facets.class: regional-reseller
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the price table gives VM-XS as 1 vCPU, 1 GB, 25 GB HDD and 600 GB monthly outbound at 5,040 원, and lists VM-S at 11,790 원, VM-M at 21,600 원, VM-L at 31,500 원 and VM-XL at 41,400 원, all on a 12-month commitment with inbound unlimited; the page also states overage at 70 원 per GB to 1,000 GB and 60 원 per GB above, and an extra public IP at 3,300 원 a month
  - [1] 2026-11-25: the price table states the VM-XS shape and monthly price | capture: sha256:2bd5cf6024a5294fc296ce204eb55b099637dc55905bd2839c5611cf016d3208 | quote: | VM-XS | 1 | 1GB | 25GB | 600GB/월 | 5,040원 |
  - [1] 2026-11-25: the price table still states the VM-XS shape and monthly price | capture: sha256:2bd5cf6024a5294fc296ce204eb55b099637dc55905bd2839c5611cf016d3208 | quote: | VM-XS | 1 | 1GB | 25GB | 600GB/월 | 5,040원 |
- sources:
  - [1] https://idc.xdn.kr/vm.html
