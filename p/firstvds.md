# firstvds vds

> firstvds.ru | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/firstvds/ | JSON https://fshy.ajam.dev/api/v1/entity/firstvds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FirstVDS

- `compute/firstvds` | trial-only | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://firstvds.ru/products/vps-vds-gpu
- free tier: No free GPU trial; the minimum paid period is one day, and daily billing means only the days used are charged. Four vGPU profiles slice one Nvidia L40S into 4, 8, 12 and 16 GB shares: the smallest is vGPU 4, an L40S-4Q with 4 GB of video memory, 2 cores, 4 GB RAM and 50 GB NVMe, at RUB 299 a day or RUB 8,970 a month; vGPU 8 is RUB 549 a day, vGPU 12 RUB 799 and vGPU 16 RUB 949. Whole-card passthrough runs from RUB 1,150 a day for an L4 with 24 GB, RUB 2,055 a day for an RTX 4090 and RUB 2,550 a day for an L40S with 48 GB. A CPU-only server gets a different offer: one to three days free, granted by the sales department after a request in the control panel, unavailable for the warming tariff and for Windows. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: approval-gated-trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): The only free capacity is the one-to-three-day CPU trial, and it is gated on a sales department decision rather than on a form, so it can be refused; the GPU lane has no free hours at all and the cheapest entry is RUB 299 for one day. [1]
- limits note: The only free capacity is the one-to-three-day CPU trial, and it is gated on a sales department decision rather than on a form, so it can be refused; the GPU lane has no free hours at all and the cheapest entry is RUB 299 for one day.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The daily billing is the composition: a 4 GB L40S slice for RUB 299 is 12 hours of fine-tuning for the price of a meal, and it composes with free storage elsewhere because the machine carries 50 GB NVMe locally, which is enough for a dataset slice rather than for a corpus.
- reliability: no reliability event recorded
- notes: Arithmetic: 299 x 30 = 8,970, so monthly billing is exactly 30 days and the daily price carries no premium; 299 / 24 = 12.46 RUB an hour. The entity-only title on the promotions page is the same contradiction that appears at AdminVPS, and found it twice in two different providers, so both should be treated as unresolved. Not established: whether a foreign card reaches the balance, and whether a vGPU profile can be held for under a day.
- extras:
  - facets.class: regional-gpu
  - facets.free_tier_kind: approval-gated-trial
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.gpu_class: Nvidia L40S-4Q vGPU profile, 4 GB VRAM
  - facets.shape.gpu_count: 1
  - facets.shape.disk_gib: 50
- evidence:
  - [1] 2026-10-22: vGPU from RUB 299 a day on an Nvidia L40S with profiles from 4 to 16 GB of video memory, passthrough from RUB 1,150 a day for L4, RTX 4090, RTX 5090 and L40S, daily or monthly billing, and 'there is no free trial period, but you can order a server for 1 day, the minimum paid period', quoted and translated
  - [2] 2026-10-22: the free CPU test is one to three days by agreement with the sales department, requested through the cart and a control-panel ticket, with an answer promised within one business day, and is unavailable for the warming tariff and Windows servers, quoted and translated
  - [3] 2026-10-22: the promotions page titles the same offer as a trial period for legal entities, which contradicts the blog page that addresses clients without that restriction
  - [4] 2026-10-22: a third-party price table dated 2026 lists the same FirstVDS profiles at RUB 299, 549, 799 and 949 a day and RUB 8,970 to 28,470 a month, and lists VDSina's L4 shape at RUB 159 a day as the cheapest GPU in the market
  - [5] 2026-10-22: an independent price archive records the L40S vGPU rate at RUB 299 a day observed since 27 August 2026 and still holding on 15 October 2026
- sources:
  - [1] https://firstvds.ru/products/vps-vds-gpu
  - [2] https://firstvds.ru/blog/besplatnyy-testovyy-period
  - [3] https://firstvds.ru/actions
  - [4] https://freerank.ru/best/gpu-server
  - [5] https://zeroquant.ru/arenda/istoriya-cen/firstvds

## firstvds vds storage (russia)

- `storage/firstvds-vds-storage` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://firstvds.ru/storage-vds
- free tier: None reachable: The base plan is 300 GB for ₽949-1,249/mo. $38.31/TB/mo at best. And expansion is priced at ₽125/mo per 50 GB without redundancy or ₽185/mo per 50 GB with, which is ₽2,500-3,700 per TB/mon. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The base plan is 300 GB for ₽949-1,249/mo — $38.31/TB/mo at best — and expansion is priced at ₽125/mo per 50 GB without redundancy or ₽185/mo per 50 GB with, which is ₽2,500-3,700 per…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The base plan is 300 GB for ₽949-1,249/mo — $38.31/TB/mo at best — and expansion is priced at ₽125/mo per 50 GB without redundancy or ₽185/mo per 50 GB with, which is ₽2,500-3,700 per…
  - [2] 2026-10-21: cited as the basis of the rejection: The base plan is 300 GB for ₽949-1,249/mo — $38.31/TB/mo at best — and expansion is priced at ₽125/mo per 50 GB without redundancy or ₽185/mo per 50 GB with, which is ₽2,500-3,700 per TB/mon
  - [3] 2026-10-21: cited as the basis of the rejection: The base plan is 300 GB for ₽949-1,249/mo — $38.31/TB/mo at best — and expansion is priced at ₽125/mo per 50 GB without redundancy or ₽185/mo per 50 GB with, which is ₽2,500-3,700 per TB/mon
- sources:
  - [1] https://firstvds.ru/storage-vds
  - [2] https://firstvds.ru/blog/snizili-ceny-na-vds-storage-20-i-vds-lxd-arm-nvme-beta
  - [3] https://firstvds.ru/blog/all_price_increase_01-03-26
