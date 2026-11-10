# GPU.LAND

> gpu.land | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gpu-2/ | JSON https://fshy.ajam.dev/api/v1/entity/gpu-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GPU.LAND

- `compute/gpu-land` | paid-only | evidence documented | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://gpu.land/
- free tier: USD 0.25/hour for a vGPU instance, the vendor's own headline figure: 'Affordable GPU pricing for lower-power instances' beside '$0.25/h', with 'vGPUs lower costs by letting multiple workloads share the same hardware' and '10x Savings over reserving a whole GPU for smaller workloads'. No core count, RAM figure, disk size, GPU model or location is stated on the page read. The tracker's rows for the same provider are three whole-V100 offers whose 'Monthly price' reads USD 722.70 for the 1x card, with billing interval 'Hourly', 8 cores, 61 GB and a 10,000 Mbit unmetered port. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the vendor page read. The tracker row for the whole-V100 offers states 'Unmetered Inbound, Unmetered Outbound' on a 10,000 Mbit uplink | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits note: No quota of any kind is stated on the vendor page: the wall is the hourly rate and whatever the minimum billing unit is, and neither a transfer allowance nor a port speed appears in the extract.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the vendor page read; the tracker lists KVM as the virtualization type on the whole-V100 offers
- composes with: A shared vGPU at USD 0.25 an hour is the cheapest way among evaluated providers to get a CUDA device for an hour at a time without committing to a whole card, which fits a notebook-style loop or a single fine-tune. The catch is that the page states no VRAM, so whether the instance can hold a model at all is unverified.
- reliability: no reliability event observed; the aggregator's price row for this provider contradicts the vendor's own headline by three orders of magnitude, which is a reporting defect rather than an outage.
- notes: Found via serverhunter, then read first-party at gpu.land. land and gpu-land, no record). The record is documented for the price because the vendor page printed it, and null for every shape field because the page printed none; the tracker's USD 722.70 row is quoted in evidence only so the disagreement is visible. verification criteria: the vendor's console or docs page for VRAM per vGPU tier and the billing minimum.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: vGPU (model not stated on the page read)
- evidence:
  - [1] 2026-10-22: page quoted: 'Affordable GPU Compute', 'vGPUs lower costs by letting multiple workloads share the same hardware while keeping startup fast for training and deployment', '10x Savings over reserving a whole GPU for smaller workloads', '$0.25/h Affordable GPU pricing for lower-power instances', '< 10s Fast instance startup for experiments and deployments'
  - [2] 2026-10-22: the provider page states 'Domain gpu.land', 'Domain registration date 27th of September 2020', 'Amount of offers 3 offers', and lists '1x NVIDIA Tesla V100', '4x NVIDIA Tesla V100', '8x NVIDIA Tesla V100'
  - [3] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): Monthly price USD 722.70, 'Billing interval Hourly', 'Product type VPS', 'Virtualization type KVM', 'Processor cores 8 cores', 'Memory amount 61 GB', 'Uplink 10,000 Mbit', 'Traffic Unlimited'. A USD 722.70 monthly figure beside an hourly interval and 61 GB of RAM does not describe a single V100 and is recorded as an aggregator artifact, not as the card's rate
- sources:
  - [1] https://gpu.land/
  - [2] https://www.serverhunter.com/company/gpu-land/
  - [3] https://www.serverhunter.com/offer/gpu-land-1x-nvidia-tesla-v100/
