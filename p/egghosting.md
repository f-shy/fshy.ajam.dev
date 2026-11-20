# Egg Hosting

> egghosting.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/egghosting/ | JSON https://fshy.ajam.dev/api/v1/entity/egghosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Egg Hosting

- `compute/egg-hosting` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://egghosting.com/vps
- free tier: Dedicated-vCPU KVM instances: 2 vCPU with 4 GB RAM and 50 GB NVMe at KRW 24,000 a month excluding VAT, 4 vCPU with 8 GB at 44,000, 4 vCPU with 16 GB at 56,000, 4 vCPU with 32 GB at 80,000, and a 2 vCPU with 8 GB at 29,600. Each carries 300 GB of monthly outbound traffic on a 1 Gbps port, with overage priced in tiers from KRW 49 down to KRW 29 per GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 300 GB of monthly outbound is the whole allowance regardless of shape, so a 4 vCPU box buys no more traffic than the smallest; at KRW 49 per GB for the first excess terabyte, the traffic bill passes the server bill at about 500 GB over the allowance. | metered: yes | source: [1]
- identity: card
- interface: unknown
- limits:
  - volume-quota (binding): 300 GB of monthly outbound is the whole allowance regardless of shape, so a 4 vCPU box buys no more traffic than the smallest; at KRW 49 per GB for the first excess terabyte, the traffic bill passes the server bill at about 500 GB over the allowance. [1]
- limits note: 300 GB of monthly outbound is the whole allowance regardless of shape, so a 4 vCPU box buys no more traffic than the smallest; at KRW 49 per GB for the first excess terabyte, the traffic bill passes the server bill at about 500 GB over the allowance.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Egg undercuts iwinv on dedicated vCPU by about 10 percent and undercuts Cafe24 on storage, so a two-stage chain works: Egg for the always-on Korean box, iwinv for the per-day scratch box; both break at the same place, a 300 GB to 600 GB monthly traffic wall.
- reliability: no reliability event recorded
- notes: The dedicated-vCPU claim is the differentiator against iwinv's shared vgna line and against Cafe24, which does not publish a vCPU count. The vendor's 'lowest in Korea' claim is its own and is recorded as the vendor's claim. 300 GB a month is a hard ceiling for the stated daily volumes, and that ceiling is the finding rather than the price.
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the plan list gives 미디엄 NVMe as 2 vCPU, 4 GB RAM, NVMe 50 GB, 1 Gbps network and 300 GB monthly traffic at 24,000 원 a month, with 미디엄 플러스 at 29,600 원, 라지 at 44,000 원, 라지 플러스 at 56,000 원 and 엑스라지 at 80,000 원, all with dedicated vCPU and full root
  - [2] 2026-10-22: the pricing page states the overage ladder as 49 원 per GB for the first 1,000 GB, 44 for 1,001 to 2,000, 39 to 3,000, 34 to 4,000 and 29 above 4,001 GB
  - [3] 2026-10-22: the vendor's own comparison page states that its 1 vCPU / 2 GB shape is 13,000 원 against a next-best 14,600 원, and its 2 vCPU / 4 GB shape 24,000 원 against a next-best 27,800 원, measured 2026-09; a vendor's own comparison is reported, not independent
- sources:
  - [1] https://egghosting.com/vps
  - [2] https://egghosting.com/pricing
  - [3] https://egghosting.com/vps/compare
