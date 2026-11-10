# Cafe24 virtual

> cafe24.com | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cafe24/ | JSON https://fshy.ajam.dev/api/v1/entity/cafe24.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cafe24 quick server (kr) hdd expansion

- `storage/cafe24-quick-server-hdd-expansion` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-30T18:09:47.044Z (inherited) | stale on 2026-11-14
- url https://hosting.cafe24.com/?controller=new_product_page&page=quick
- free tier: no free allowance: Quick server plans are paid monthly from KRW 90,000 (VAT excluded) for Quick 라이트업 Pro, with free setup; a SATA3 4TB HDD option is listed at KRW 16,000 | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: The marginal HDD expansion rate is ₩16,000 per month per 4 TB (₩4,000/TB, approximately $3.02/TB). It is an add-on to a dedicated server starting at ₩90,000 per month ($67.87).
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
  - [1] 2026-10-30: the Quick server plans carry a monthly fee from KRW 90,000 (VAT excluded); no free plan is listed | capture: sha256:a3ca8af2d0d4d5a75339896d9cfb64b6ac3184642f082614b6389e44f3c67f5a | quote: | 월 사용료 (VAT 별도) | 90,000원 | 110,000원 | 140,000원 | 180,000원 |
  - [1] 2026-10-30: a SATA3 4TB HDD option is listed at KRW 16,000 | capture: sha256:a3ca8af2d0d4d5a75339896d9cfb64b6ac3184642f082614b6389e44f3c67f5a | quote: | SATA3 4TB, 3.5" | 16,000원 | |
- sources:
  - [1] https://hosting.cafe24.com/?controller=new_product_page&page=quick
  - [2] https://xetown.com/board/1791132

## Cafe24 virtual server

- `compute/cafe24-virtual-server` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://hosting.cafe24.com/?controller=new_product_page&page=virtual
- free tier: The entry shape is KRW 9,000 a month including VAT for 1 GB RAM, 30 GB SSD and 300 GB of monthly traffic. Above it: 16,000 for 2 GB and 40 GB and 500 GB, 22,000 for 3 GB and 50 GB and 800 GB, 33,000 for 4 GB and 100 GB and 1.2 TB, 55,000 for 6 GB and 150 GB and 1.5 TB. Every plan carries a KRW 22,000 setup fee and an overage charge of KRW 165 per GB. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - volume-quota (binding): 300 GB of monthly traffic on the entry plan, then KRW 165 per GB; the overage is the expensive part, because 1 TiB above the allowance would cost more than the server, so the volume quota fails long before the CPU does. [1]
- limits note: 300 GB of monthly traffic on the entry plan, then KRW 165 per GB; the overage is the expensive part, because 1 TiB above the allowance would cost more than the server, so the volume quota fails long before the CPU does.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Cafe24 is the only Korean host found that sells a real Linux VM at KRW 9,000 including tax with no minimum term; it does not chain, because the 300 GB allowance and the KRW 165 per GB overage make it a host for a small service rather than a data mover.
- reliability: no reliability event recorded
- notes: The vCPU count is not on the plan table, so it is left null rather than guessed. Cafe24 raised the entry price from KRW 7,000 to 9,000 on the day a Korean trade paper reported, citing SSD and memory cost; the raise is a reliability fact about the Korean floor, not a defect. The setup fee is the detail that changes the arithmetic for a one-month test: KRW 22,000 is more than two months of the server itself.
- extras:
  - facets.class: regional-paid-floor
  - facets.free_tier_kind: none
  - facets.shape.ram_gib: 1
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the plan table gives 일반형 at 9,000 원 a month including VAT with 1 GB RAM, 30 GB SSD and 300 GB monthly traffic, 비즈니스 at 16,000, 퍼스트클래스 at 22,000, 자이언트 at 33,000 and 자이언트플러스 at 55,000, with a 22,000 원 setup fee on every plan and 165 원 per GB of excess traffic
- sources:
  - [1] https://hosting.cafe24.com/?controller=new_product_page&page=virtual
