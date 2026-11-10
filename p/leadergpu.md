# LeaderGPU

> leadergpu.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leadergpu/ | JSON https://fshy.ajam.dev/api/v1/entity/leadergpu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LeaderGPU

- `compute/leadergpu` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T08:50:28.019Z (live) | stale on 2026-12-04
- url https://www.leadergpu.com/
- free tier: European dedicated bare-metal GPU servers sold by the month, which is the cheapest per-hour shape for a workload that runs continuously. The page lists per-card monthly prices only, with no hourly rate, no spot or on-demand tier and no stated minimum bill; the hourly figures are derived at 730 hours and USD 1 = EUR 0.89246: RTX 3090 24GB from EUR 125 per card per month, USD 140.06, USD 0.192/hr; RTX A6000 48GB from EUR 181, USD 202.81, USD 0.278/hr; RTX 4090 24GB from EUR 329, USD 368.64, USD 0.505/hr; RTX 5090 32GB from EUR 499, USD 559.13, USD 0.766/hr; A100 40GB 8x at EUR 363 per card, USD 0.557/hr; L40S 8x at EUR 411, USD 0.631/hr; A100 SXM 80GB 8x at EUR 624, USD 0.958/hr; H100 SXM 8x NVLink at EUR 1,488 per card, USD 1,667.30, USD 2.284/hr; H200 1x at EUR 2,987, USD 4.585/hr. The page lists no L4. Each server ships with the CPU, RAM, NVMe and 1 Gbit network named on the row; the page states no setup fees. | unit: GiB | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Storage and network are included in the monthly price on this page; egress terms were not published there and were not established. | metered: no | source: [1]
- identity: card | detail: A monthly bare-metal invoice; no trial and no free lane is offered on the page.
- interface: unknown
- limits:
  - write-gated (binding): The one-month commitment on a bare-metal invoice is the binding term, so the USD 0.192 per hour only exists for a workload that occupies the card for most of 730 hours. [1]
- limits note: The one-month commitment on a bare-metal invoice is the binding term, so the USD 0.192 per hour only exists for a workload that occupies the card for most of 730 hours.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 48 GB A6000 at USD 0.278 per hour is the cheapest 48 GB card found among evaluated providers for continuous use, below Massed Compute at USD 0.55 on demand, and it arrives with a whole server's RAM and 2 TB of NVMe rather than a rented slice.
- reliability: no reliability event recorded
- notes: Every hourly figure is a division of a published monthly price by 730 hours, and it is a break-even only at full occupancy: at 100 hours a month the same A6000 costs USD 2.03 per hour. The 8x rows quote a per-card price with a total beside it, and the total is what an invoice carries, so the smallest orderable unit on those rows is eight cards and not one. Storage and network are included in the monthly price on this page; egress terms were not published there and were not established.
- extras:
  - facets.class: committed-gpu-host
  - facets.free_tier_kind: none
  - facets.shape.ram_gib: 384
  - facets.shape.gpu_class: RTX 3090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
  - facets.shape.disk_gib: 2000
- evidence:
  - [1] 2026-10-22: quoted rate rows: NVIDIA RTX 3090 'from EUR 125 per card / mo' on a 1 to 8 card server; RTX A6000 'from EUR 181'; RTX 4090 'from EUR 329'; RTX 5090 'from EUR 336'; L40S 8x 'EUR 411' per card; H100 SXM 8x NVLink 'EUR 1,488' per card for EUR 11,900 total; H200 1x 'EUR 2,987'
  - [1] 2026-10-22: quoted page description: dedicated bare-metal GPU servers, EU data rooms, no setup fees, deploy in minutes
  - [2] 2026-10-22: USD 1 = EUR 0.89246 on 2026-10-22, used for every conversion and for the 730-hour division
  - [1] 2026-11-03: the RTX 5090 is now listed from EUR 499 per card per month, not EUR 336 | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | NVIDIA RTX 5090 New | 1–8x | 32 GB GDDR7 | from €499 | from €499 |
  - [1] 2026-11-03: the price table was read on this date | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | NVIDIA RTX 4090 Popular | 1–8x | 24 GB GDDR6X | from €329 | from €329 |
  - [1] 2026-11-03: RTX 4090 24 GB is from EUR 329 per card per month | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | NVIDIA RTX 4090 Popular | 1–8x | 24 GB GDDR6X | from €329 | from €329 |
  - [1] 2026-11-03: L40S is sold as an 8x server at EUR 411 per card per month, EUR 3,290 total | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | NVIDIA L40S | 8x | 48 GB GDDR6 ECC | €411 | €3,290 |
  - [1] 2026-11-03: H100 SXM is sold as an 8x NVLink server at EUR 1,488 per card per month, EUR 11,900 total | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | NVIDIA H100 SXM Popular | 8x NVLink | 80 GB HBM3 | €1,488 | €11,900 |
  - [1] 2026-11-03: A100 SXM 80 GB is sold as an 8x NVLink server at EUR 624 per card per month, EUR 4,990 total | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | NVIDIA A100 SXM | 8x NVLink | 80 GB HBM2e | €624 | €4,990 |
  - [1] 2026-11-03: the price table is per card per month; it has no hourly column | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | GPU | Configs | VRAM / GPU | Per card / mo | Total / mo |
  - [1] 2026-11-03: the price table was re-read and the other listed monthly prices match | capture: sha256:8d94522e72ad3d23a796d1f7e6909c6cc5d5df00ad646898a88afb79684cfbbd | quote: | NVIDIA RTX 4090 Popular | 1–8x | 24 GB GDDR6X | from €329 | from €329 |
- sources:
  - [1] https://www.leadergpu.com/
  - [2] https://api.frankfurter.app/latest?from=USD&to=EUR
