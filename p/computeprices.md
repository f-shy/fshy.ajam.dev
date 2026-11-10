# Seeweb

> computeprices.com | Compute; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/computeprices/ | JSON https://fshy.ajam.dev/api/v1/entity/computeprices.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Nscale

- `compute/nscale` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:29.744Z (live) | stale on 2026-11-18
- url https://computeprices.com/providers/nscale
- free tier: No price: the index records 'Nscale does not publish public hourly pricing. Contact the provider directly for a quote.' The provider is described as 'a vertically integrated AI hyperscaler offering GPU clusters and managed AI services from data centers in the UK, Europe and the US, with a focus on Blackwell-generation reservations and large-scale training capacity'. No rate row exists to record. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: reserved multi-month and multi-year capacity, plus on-demand instances billed hourly where capacity allows, per the index. No H100, A100, L40S, RTX 4090 or L4 price is listed. unverified: no minimum bill is stated.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: No quota and no price are stated, so nothing in this record binds. The page's own framing is 'Reservation-led capacity', so the wall is a reservation rather than a metered limit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: Sovereign UK and EU capacity for Blackwell-generation reservations serves compliance requirements. With no published rate, pricing is quote-only and reservation-led.
- reliability: no reliability event recorded
- notes: Found via computeprices. Like TensorWave this is a partial finding: no number exists to record and none was invented. Unverified: a quote request or the vendor's own pricing page, neither of which this category attempted.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: NVIDIA Blackwell generation (model per configuration not stated)
- evidence:
  - [1] 2026-10-22: page quoted: 'Nscale is a vertically integrated AI hyperscaler offering GPU clusters and managed AI services from data centers in the UK, Europe and the US, with a focus on Blackwell-generation reservations and large-scale training capacity.' and 'Nscale does not publish public hourly pricing. Contact the provider directly for a quote.'
  - [1] 2026-10-22: the advantages list states 'Reservation-led capacity for newest NVIDIA Blackwell systems' and 'Vertically integrated control of power, networking and cooling'
  - [1] 2026-11-03: the index lists on-demand with hourly billing | capture: sha256:9ad1421ae7ba06b7cddc89304ab6522f5efa7da89e63fe8f9abf818814ff96e8 | quote: Hourly billing for available GPU types where capacity allows
  - [1] 2026-11-03: the index still records no public hourly price for the provider | capture: sha256:9ad1421ae7ba06b7cddc89304ab6522f5efa7da89e63fe8f9abf818814ff96e8 | quote: Nscale does not publish public hourly pricing.
- sources:
  - [1] https://computeprices.com/providers/nscale

## QuickPod

- `compute/quickpod` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://computeprices.com/providers/quickpod
- free tier: USD 0.100 per GPU-hour for a single RTX A4000 with 16 GB in Kansas, US: 12 vCPU, 41 GB RAM. Next rows: the same card at the same rate as a 2x configuration on 8 vCPU and 125 GB in Kentucky; RTX 3060 12 GB at USD 0.120 on 10 vCPU and 35 GB in Indiana; RTX 3090 24 GB at USD 0.180 on 4 vCPU and 31 GB in Kentucky; RTX 3080 10 GB at USD 0.230 in Oxfordshire, GB; RTX 5090 32 GB at USD 0.570 in Queensland, AU. Five models across four US states, the UK and Australia. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: unknown
- limits note: No quota is stated: the page publishes a per-GPU hourly rate, VRAM, vCPU count, RAM and a region. The wall is the hourly rate, and the rate is low enough that the machine-hours are the constraint rather than a byte counter.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the provider is tagged 'docker' and the description says 'docker pod rentals through a streamlined interface'; a console URL at console.quickpod.io is the linked order path
- composes with: Ten cents an hour for a 16 GB card is the cheapest GPU rate among documented hosts, half of Cirrascale's A4000 rate and a third of SwissGPU's RTX 4080. The region is the other half of the offer: US, UK and Australian hosts under one account makes it the row to price when the crawler's source address and the GPU have to sit in the same country
- reliability: no reliability event recorded
- notes: Found via computeprices. The $0.100 row is dated 10/17/2026 on the index while the page's own 'last updated' line reads 21 October 2026, so the per-row date is the one quoted. Unverified: console.quickpod.io for the disk size, the billing minimum and whether the A4000 row is still stocked at ten cents.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 12
  - facets.shape.ram_gib: 41
  - facets.shape.gpu_class: NVIDIA RTX A4000 16GB
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): [RTX A4000] | $0.100/hrKansas, US | 16GB | 1x | 12 | 41 GB | 10/17/2026; the page header reads 'GPU Models 5', 'From / hour $0.10' and 'Prices last updated: October 21, 2026'
  - [1] 2026-10-22: provider quoted: 'QuickPod offers CPU and GPU docker pod rentals through a streamlined interface', tagged 'GPU-focused', 'budget', 'docker'; further rows RTX 3090 at $0.180/hr in Kentucky, RTX 3060 at $0.120/hr in Indiana, RTX 3080 at $0.230/hr in Oxfordshire GB, RTX 5090 at $0.570/hr in Queensland AU
- sources:
  - [1] https://computeprices.com/providers/quickpod

## Seeweb

- `compute/seeweb` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:33.436Z (live) | stale on 2026-11-18
- url https://computeprices.com/providers/seeweb
- free tier: Hourly list prices in EUR on the vendor's Cloud Server GPU page, the same figure printed under its Standard and Spot headings: H100 (GPU SXM, 320 GB GPU RAM, 128 cores, 1,024 GB RAM) EUR 1.89; A100 (GPU PCI, 80 GB) EUR 0.99; L40S 48 GB EUR 0.85; L4 24 GB EUR 0.38; RTX A6000 48 GB EUR 0.74; Quadro RTX 6000 and A30 EUR 0.29 each. No RTX4090 is listed. Billing is for the hours of use with no advance payment. The GPU count of the H100 shape is unverified: the page gives 320 GB GPU RAM and no count. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not published on the page read | metered: no | source: [2]
- identity: email | detail: not stated
- interface: unknown
- limits note: No quota is stated: the page publishes a per-GPU hourly rate, VRAM and a count per row. The wall is the hourly rate and whatever minimum the vendor's own order page sets.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: Ten models from one Italian vendor, including AMD MI300X with 192 GB at USD 2.64 an hour, provides specialized accelerator capacity. The 24 GB GPU tier at USD 0.325 compares with an A4000 or RTX 4080.
- reliability: no reliability event recorded
- notes: The index row carries no vCPU, RAM or disk, so those shape fields are null rather than guessed, and the vendor page it links was not fetched. Unverified: seeweb.it's GPU cloud page for the host shape that comes with each card.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: NVIDIA Quadro RTX 6000 24GB
  - facets.shape.gpu_count: 1
- evidence:
  - [2] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): [Quadro RTX 6000] | $0.325/hr | 24GB | 1x | 10/22/2026; the page header reads 'From / hour $0.33' and 'Prices last updated: October 22, 2026'
  - [2] 2026-10-22: provider quoted: 'Italian cloud provider with NVIDIA and AMD GPU cloud servers', 'part of the Dominion Hosting Holding group, offering GPU-accelerated cloud servers with NVIDIA and AMD accelerators, pay-per-hour billing, and data centers across Europe'; other rows as listed above, including MI300X at $2.64/hr
  - [1] 2026-11-03: the H100 shape is listed at EUR 1.89 per hour | capture: sha256:d9afa50ad567c0e30955431f076c4e6a48417bd1284e9ecfbe5e13c6646c2622 | quote: ## CLOUD GPU NVIDIA H100 GPU SXM | 320 GB GPU RAM 128 CORE | 1024 GB RAM 6 TB Disk space ### Hourly Cost 1.89 €
  - [1] 2026-11-03: the vendor page lists the L4 at EUR 0.38 per hour | capture: sha256:d9afa50ad567c0e30955431f076c4e6a48417bd1284e9ecfbe5e13c6646c2622 | quote: ## CLOUD GPU NVIDIA L4 GPU PCI | 24 GB GPU RAM 4 CORE | 32 GB RAM 100 GB Disk space ### Hourly Cost 0.38 €
  - [1] 2026-11-03: billing is by hours of use, not by stored bytes | capture: sha256:d9afa50ad567c0e30955431f076c4e6a48417bd1284e9ecfbe5e13c6646c2622 | quote: you will be billed only for the hours of use. The billing will start after the product activation, with no advance payment.
  - [1] 2026-11-03: the A100 80 GB PCI shape is listed at EUR 0.99 per hour | capture: sha256:d9afa50ad567c0e30955431f076c4e6a48417bd1284e9ecfbe5e13c6646c2622 | quote: ## CLOUD GPU NVIDIA A100 GPU PCI | 80 GB GPU RAM 16 CORE | 128 GB RAM 1 TB Disk space ### Hourly Cost 0.99 €
  - [1] 2026-11-03: the L40S shape is listed at EUR 0.85 per hour | capture: sha256:d9afa50ad567c0e30955431f076c4e6a48417bd1284e9ecfbe5e13c6646c2622 | quote: ## CLOUD GPU NVIDIA L40S GPU PCI | 48 GB GPU RAM 8 CORE | 32 GB RAM 500 GB Disk space ### Hourly Cost 0.85 €
  - [2] 2026-11-03: a third-party index converts the vendor's L4 price to USD 0.426 per hour, collected 2026-11-03 | capture: sha256:4d8ccb4c4b17130b48e7716954ed928d4d87ecf3f95c2d401964ba16c866f666 | quote: | [L4](https://computeprices.com/providers/seeweb/gpus/l4) | $0.426/hr | 24GB | 1× | 11/3/2026 | [Rent](https://www.seeweb.it/en/products/cloud-server-gpu?utm_source=computeprices&utm_medium=referral&utm_campaign=gpu-pricing) |
  - [1] 2026-11-03: billing is by hours of use with no advance payment | capture: sha256:d9afa50ad567c0e30955431f076c4e6a48417bd1284e9ecfbe5e13c6646c2622 | quote: you will be billed only for the hours of use. The billing will start after the product activation, with no advance payment.
- sources:
  - [1] https://www.seeweb.it/en/products/cloud-server-gpu
  - [2] https://computeprices.com/providers/seeweb

## Sesterce

- `compute/sesterce` | paid-only | evidence reported | binding none | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T08:50:33.436Z (live) | stale on 2026-11-18
- url https://computeprices.com/providers/sesterce
- free tier: On-demand GPU-hour list prices on a third-party index, collected 2026-11-02, cheapest zone for each card: H100 SXM 1x Zone 2 USD 2.19; A100 PCIe 80GB 1x Zone 5 USD 1.49; L40S 1x Zone 13 USD 0.97; RTX 4090 8x Zone 22 USD 0.44; L4 1x Zone 19 USD 1.04; A10 1x Zone 7 USD 1.42. Twenty GPU models in 80 configurations. Billing is On-Demand from a prepaid credit balance that is debited every minute. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: The vendor documentation table, last updated about a year earlier, prints H100 2.48, A100 80G 1.65, L40s 1.10 and RTX4090 0.66 USD per hour and lists no L4.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: An account created by email or OAuth (GitHub or Google). Instances run on a prepaid credit balance that is topped up by credit card, bank transfer, Cash App Pay, Google Pay or Link; at zero credit the instances are stopped and storage volumes are deleted. Whether a card or a minimum top-up is needed before the first instance is unverified: behind a sign-up.
- interface: unknown
- limits note: No quota is stated: the page publishes a per-GPU hourly rate, VRAM, vCPU count, RAM and a zone label. The page header also prints 'From / hour $0.17' without naming the card or zone, so the true floor is below the cheapest row that carries a specification and is unverified.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: An A10 with 30 vCPU and 200 GB of system RAM for USD 1.42 an hour is the most CPU-per-GPU shape among documented hosts, which is what a data pipeline that touches the accelerator intermittently wants: the 24 GB card is small enough for embedding and inference work, and the 200 GB of RAM is where the batch lives. The zone labels are the reason not to read this as one price, because the same card is printed at different rates per zone
- reliability: no reliability event recorded
- notes: Found via computeprices. The zone naming ('Zone 5', 'Zone 7', 'Zone 13') is the index's own, and the vendor's zone-to-city mapping was not read. Unverified: cloud.sesterce.com's price list for what each zone is and the disk that ships with the A10 row.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 30
  - facets.shape.ram_gib: 200
  - facets.shape.gpu_class: NVIDIA A10 24GB
  - facets.shape.gpu_count: 1
- evidence:
  - [1] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): [A10] | $1.42/hrZone 7 | 24GB | 1x | 30 | 200 GB | 10/22/2026; the page header reads 'GPU Models 17' and 'From / hour $0.17'
  - [1] 2026-10-22: provider, transcribed and joined: 'Sovereign European AI factories and on-demand GPU cloud', 'a self-serve GPU cloud with on-demand VMs, bare-metal servers and dedicated clusters. Its self-serve on-demand catalog lists regions across North America, Europe and Asia-Pacific'; further rows [A100 PCIe 80GB] | $1.49/hr | 80GB | 1x | 28 | 120 GB and [A100 SXM] | $1.52/hrZone 13 | 80GB | 1x 8x | 14 | 100 GB
  - [1] 2026-11-03: the index lists the L4 at USD 1.04 per hour, one GPU, Zone 19 | capture: sha256:9e418376693df6153e0ee3d00e2a31abf3f8bb55d15df60f622f135685f8c487 | quote: | [L4](https://computeprices.com/providers/sesterce/gpus/l4)1× · Zone 19 | $1.04/hr | | #18 of 22 providers | +26% | |
  - [2] 2026-11-03: the vendor compute catalogue prints USD 0.97 per hour beside L40S | capture: sha256:6df882c3de8d7702c36299da54cda5c794f154e968b5bf456301ab1efe17200d | quote: L40S0.97$/h
  - [2] 2026-11-03: the vendor compute catalogue prints USD 1.05 per hour beside L4 | capture: sha256:6df882c3de8d7702c36299da54cda5c794f154e968b5bf456301ab1efe17200d | quote: L41.05$/h
  - [3] 2026-11-03: the vendor documentation table prints RTX4090 at USD 0.66 per hour, on a page last updated about a year earlier | capture: sha256:1bb58b2d7c2213bc9d219f913618c6e9da3dec07d5970810e69e04a96b24c5ab | quote: RTX4090 Hourly Price $0.66
  - [4] 2026-11-03: the prepaid credit balance is debited every minute | capture: sha256:c7325f138846e08f26b6b119947ef10f1f0fc45c6e70df9ae5313a3d9c27ccd8 | quote: Your credit balance is debited in real time, every minute, according to your instances and volumes utilization.
  - [4] 2026-11-03: the vendor sells On-Demand pricing | capture: sha256:c7325f138846e08f26b6b119947ef10f1f0fc45c6e70df9ae5313a3d9c27ccd8 | quote: Currently, Sesterce Cloud offers “On-Demand” pricing.
  - [3] 2026-11-03: the vendor documentation table prints H100 at USD 2.48 per hour | capture: sha256:1bb58b2d7c2213bc9d219f913618c6e9da3dec07d5970810e69e04a96b24c5ab | quote: H100 Hourly Price $2.48
  - [5] 2026-11-03: an account is created by email or OAuth with GitHub or Google | capture: sha256:0dc8e0d77096d84ca4f9a0ee3f380804ed635c404852e3107173e03e62f61d7e | quote: You can create an account via email or oAuth (Github or Google)
  - [1] 2026-11-03: the index lists 20 GPU models across 80 configurations | capture: sha256:9e418376693df6153e0ee3d00e2a31abf3f8bb55d15df60f622f135685f8c487 | quote: 20 GPU models across 80 configurations.
- sources:
  - [1] https://computeprices.com/providers/sesterce
  - [2] https://cloud.sesterce.com/compute
  - [3] https://docs.sesterce.com/
  - [4] https://docs.sesterce.com/welcome-on-sesterce-cloud/payment-and-billing.md
  - [5] https://docs.sesterce.com/welcome-on-sesterce-cloud/account-creation.md

## SwissGPU

- `compute/swissgpu` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:35.125Z (live) | stale on 2026-11-18
- url https://computeprices.com/providers/swissgpu
- free tier: Prices in CHF per hour, VM / bare metal: RTX 4090 24 GB 0.40 / 0.50 (16 cores, 32 GB RAM, 1 TB NVMe); RTX 4080 16 GB 0.25 / 0.35; RTX 5080 16 GB 0.30 / 0.40; RTX 3090 24 GB 0.25 / 0.35; RTX 5090 32 GB 0.50 / 0.60; RTX 6000 ADA 48 GB 1.50 / 2.00; RTX 6000 PRO 96 GB 2.00 / 3.00. H100, A100 80 GB, L40S and L4 are not listed. Per-minute billing while the server runs; no additional storage or network charges; electricity is billed separately at CHF 0.30 per kWh; a CHF 0.50 reinstall fee applies to VMs and Linux bare metal; VM billing and lifecycle details are marked work in progress | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not published on the page read | metered: no | source: [2]
- identity: email | detail: not stated
- interface: unknown
- limits note: No quota is stated: the page publishes a per-GPU hourly rate, VRAM, vCPU count and RAM. The wall is the hourly rate.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: Sixteen gigabytes holds a 7B model at 4-bit, which is the useful floor for local inference experiments
- reliability: no reliability event recorded
- notes: Found via computeprices. The description calls the servers bare-metal while the index prices them per GPU-hour on a vCPU count, which is not a contradiction only if the host is dedicated and the billing is hourly; the page does not resolve it. Unverified: swissgpu.ch/pricing, which the index links, for the billing unit and the disk size.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 12
  - facets.shape.ram_gib: 32
  - facets.shape.gpu_class: NVIDIA RTX 4080 16GB
  - facets.shape.gpu_count: 1
- evidence:
  - [2] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): [RTX 4080] | $0.303/hr | 16GB | 1x | 12 | 32 GB | 10/21/2026; the page header reads 'GPU Models 5', 'From / hour $0.30' and 'Prices last updated: October 21, 2026'
  - [2] 2026-10-22: provider quoted: 'Swiss-based GPU servers with low latency', 'Provider of bare-metal GPU servers fully hosted in Switzerland.'; further rows RTX 5080 at $0.364/hr, RTX 4090 at $0.486/hr, RTX 5090 at $0.607/hr, RTX 6000 Ada at $1.82/hr
  - [1] 2026-11-03: the RTX 4090 is 0.40 CHF/h as a VM and 0.50 CHF/h as bare metal | capture: sha256:07e9926b130fbc787923497a73c5d965d0d90ed77f32e8adea5629989be89062 | quote: | [Nvidia RTX 4090](https://www.nvidia.com/en-eu/geforce/graphics-cards/40-series/rtx-4090/)Ada Lovelace - 24 GB | CPU: 16 cores RAM: 32 GB - DISK: 1 TB NVMe | 0.40 CHF/h | 0.50 CHF/h |
  - [1] 2026-11-03: billing is per minute | capture: sha256:07e9926b130fbc787923497a73c5d965d0d90ed77f32e8adea5629989be89062 | quote: We use simple per-minute billing, so you only pay for the time your server is running.
  - [1] 2026-11-03: stopping ends billing and there are no storage or network charges | capture: sha256:07e9926b130fbc787923497a73c5d965d0d90ed77f32e8adea5629989be89062 | quote: Bare metal servers cannot be paused. Stopping a server ends billing; expect to lose its data unless retention is agreed as part of a custom configuration. There are no additional storage or network charges.
  - [1] 2026-11-03: electricity and reinstall fees | capture: sha256:07e9926b130fbc787923497a73c5d965d0d90ed77f32e8adea5629989be89062 | quote: Electricity is billed separately at CHF 0.30 per kWh. A CHF 0.50 reinstall fee applies only to VMs and Linux bare metal servers to prevent abuse.
- sources:
  - [1] https://swissgpu.ch/pricing
  - [2] https://computeprices.com/providers/swissgpu

## TensorWave

- `compute/tensorwave` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:36.650Z (live) | stale on 2026-11-18
- url https://computeprices.com/providers/tensorwave
- free tier: No price: the vendor's home page lists only AMD Instinct MI455X, MI355X, MI325X and MI300X accelerators and prints no hourly rate, so no NVIDIA card is listed and no tier, billing granularity or minimum is stated. The index records the provider as quote-only, stating 'TensorWave does not publish public hourly pricing. Contact the provider directly for a quote.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits note: No quota and no price are stated, so nothing in this record binds. The wall is a sales conversation: the provider publishes no hourly rate at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the page states the software stack is ROCm; no API documentation is named
- composes with: Provides dedicated AMD MI300X capacity with 192 GB or 288 GB memory for workloads where CUDA is not mandatory. Pricing is available on request.
- reliability: no reliability event recorded
- notes: Found via computeprices. This is a partial finding by construction: the provider is real, sells the capacity, and publishes no number, so the price fields are empty rather than estimated. Unverified: a quote request, which this category does not make because it would require an account.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: AMD Instinct MI300X / MI325X / MI355X / MI455X (model per configuration not stated)
- evidence:
  - [1] 2026-10-22: page, transcribed and joined (unquoted values are not verbatim): TensorWave is an AMD-first AI cloud with bare-metal and managed clusters built on Instinct MI300X/MI325X/MI355X/MI455X accelerators with large VRAM and ROCm. and 'TensorWave does not publish public hourly pricing. Contact the provider directly for a quote.'
  - [1] 2026-10-22: the pages advantages list states First-to-market with latest AMD accelerators (MI455X, MI355X, MI325X)', 'High VRAM capacity up to 288GB per GPU', 'SOC 2 Type II and ISO 27001 certified and HIPAA compliant', 'Utilizes an open-source software stack (ROCm)'
  - [2] 2026-11-03: the vendor home page prints no price and routes enquiries to sales | capture: sha256:e5bbeb0f426a1149fcc5b8e85bd8b015ebb2a1d55cf8790812d7339d294088fb | quote: Get in touch with our team to discuss your infrastructure needs and explore how we can power your next breakthrough.
  - [1] 2026-11-03: the index records the provider as quote-only | capture: sha256:34c6f45efc0592350d3111116dc3d1fb3a016682c98f1ebc846417ee0c849171 | quote: TensorWave does not publish public hourly pricing.
- sources:
  - [1] https://computeprices.com/providers/tensorwave
  - [2] https://tensorwave.com/
