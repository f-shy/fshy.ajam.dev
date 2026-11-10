# KINX IXcloud

> kinx.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kinx/ | JSON https://fshy.ajam.dev/api/v1/entity/kinx.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KINX IXcloud

- `compute/kinx-ixcloud` | paid-only | evidence documented | binding none | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.kinx.net/service/price/
- free tier: The 기본 인스턴스 ladder starts at 1 vCPU with 1 GB and a 50 GB volume for KRW 20,000 a month or KRW 30 an hour, and runs to 16 vCPU with 32 GB for KRW 550,000 a month or 770 an hour. The SSD variant starts at KRW 23,500 a month or 35 an hour for the same 1 vCPU / 1 GB / 50 GB shape. A Kubernetes cluster control plane is billed separately at KRW 100 an hour. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: card: the vendor FAQ states IXcloud is a post-paid service 'charged automatically to a registered credit card or account transfer', so a card is the default instrument and an account transfer is the stated alternative. No authorisation or hold amount is stated, and whether debit or prepaid is accepted is not stated: unknown. Whether an individual can open an account without a Korean business number is not established in the record.
- interface: unknown
- limits note: Nothing binds above the scale on this page: the shape is fixed and no traffic allowance is published, and the constraint that matters is price, because KRW 30 an hour for 1 vCPU is about three times the Korean hourly floor.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: KINX is an internet exchange operator selling its own cloud, which makes it the most carrier-grade Korean option found and the least competitive on price; it chains only where a Korean domestic IP with a named operator is the requirement.
- reliability: no reliability event recorded
- notes: Hourly pricing of KRW 30 represents approximately USD 0.02.
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the price table gives 1코어 1기가 as 1 vCPU, 1 GB, 50 GB at 20,000 원 a month or 30 원 an hour, 2코어 4기가 at 64,000 원 or 90 원, 8코어 16기가 at 240,000 원 or 340 원, and 16코어 32기가 at 550,000 원 or 770 원, with the SSD ladder at 23,500 원 or 35 원 for the smallest shape; a Kubernetes cluster is 100 원 an hour
  - [2] 2026-10-22: the vendor's FAQ states that IXcloud is a post-paid service charged automatically to a registered credit card or account transfer
- sources:
  - [1] https://www.kinx.net/service/price/
  - [2] https://www.kinx.net/resource/faq/?lang=en&mod=document&uid=223
