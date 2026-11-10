# Denvr

> gpuperhour.com | Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gpuperhour/ | JSON https://fshy.ajam.dev/api/v1/entity/gpuperhour.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cirrascale

- `compute/cirrascale` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-06T18:41:34.653Z (live) | stale on 2026-11-21
- url https://gpuperhour.com/providers/cirrascale
- free tier: USD 0.27 per GPU-hour for an 8-GPU NVIDIA RTX A4000 node with 16 GB per card: 40 vCPU, 256 GB RAM, 2610 GB storage, in the United States. The 8x A5000 24 GB node is USD 0.41 per GPU-hour on the same host shape, and the page lists 11 GPU models across 49 instances in one region. The provider is described as 'An AI Innovation Cloud targeting deep learning and HPC research with dedicated performance on non-virtualized hardware', established 2010. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published on the page read | metered: no | source: [1]
- identity: email | detail: not stated
- interface: rest
- limits note: No quota is stated on the page: price, VRAM, host specs, region and status are all it publishes. The practical wall is the shape, because the cheapest rate is on an eight-card node and the row's total is USD 2.16 an hour.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: USD 0.27 per GPU-hour is the cheapest GPU rate of any provider among evaluated providers, on an A4000 with 16 GB and a 40-vCPU host, which is a batch-inference shape: many small workers with a big CPU headroom and no need for a large card. The eight-card minimum is what turns that rate into USD 2.16 an hour, so it suits a queue that keeps eight workers busy and wastes money on a single notebook session.
- reliability: no reliability event recorded
- notes: Per-card rates on the gpuperhour page read on 2026-11-06: H100 SXM5 80GB USD 2.49 per GPU-hour, A100 PCIe 80GB USD 2.60 per GPU-hour, and RTX A4000 16GB USD 0.27 per GPU-hour on an eight-card node (USD 2.16 an hour for the node); L40S, RTX 4090 and L4 are not listed. The vendor's own pricing page read the same day prices GB300, B300, B200, RTX PRO 6000, MI355X, MI350 and Qualcomm AI 100 Ultra only, and states that it does not list everything it sells, so the H100 and A100 figures rest on the aggregator. No free tier, credit or free GPU hours are stated. Whether a single A4000 can be booked rather than only a full node is not stated.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 40
  - facets.shape.ram_gib: 256
  - facets.shape.disk_gib: 2610
  - facets.shape.gpu_class: NVIDIA RTX A4000 16GB
  - facets.shape.gpu_count: 8
- evidence:
  - [1] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): Cirrascale | 8xNVIDIA RTX A4000 16GB VRAM | 16GB | 40 vCPU 256GB RAM 2610GB Storage | United States | $0.27/GPU/hr $2.16/hr total (8x)
  - [1] 2026-10-22: page, transcribed and joined (unquoted values are not verbatim): 'An AI Innovation Cloud targeting deep learning and HPC research with dedicated performance on non-virtualized hardware', '49 Instances', '1 Regions', '49 Available', and 'Cirrascale offers 11 GPU models'; the A5000 row reads $0.41/GPU/hr $3.28/hr total (8x)
  - [1] 2026-11-06: the page prices an H100 SXM5 80GB at USD 2.49 per GPU-hour | capture: sha256:bb0cd0cc13380017201b5f563ce61efac6ee23b68644efaa56aff69b0f0c46a3 | quote: H100 SXM5 80GB VRAM $2.49/hr
  - [1] 2026-11-06: the page prices an A100 PCIe 80GB at USD 2.60 per GPU-hour | capture: sha256:bb0cd0cc13380017201b5f563ce61efac6ee23b68644efaa56aff69b0f0c46a3 | quote: A100 PCIe 80GB 80GB VRAM $2.60/hr
  - [1] 2026-11-06: the A4000 rate is per GPU-hour on an eight-card node, USD 2.16 an hour for the node | capture: sha256:bb0cd0cc13380017201b5f563ce61efac6ee23b68644efaa56aff69b0f0c46a3 | quote: $0.27/GPU/hr$2.16/hr total (8×)
  - [2] 2026-11-06: the vendor pricing page lists GB300, B300, B200, RTX PRO 6000, MI355X, MI350 and Qualcomm AI 100 Ultra, and no H100, A100, L40S, RTX 4090 or L4 | capture: sha256:04fe14bd0d901ec21b25467b1d13bc89b2aa6b18b81f0f323f019b95755d5e2f | quote: NVIDIA HGX B200 Dual 64-Core 2TB 960 NVMe (4) 3.84TB NVMe 25Gb Bonded (3200Gb Available) As low as $4.79/GPUhr
  - [1] 2026-11-06: the cheapest listed row is still an eight-card A4000 node at USD 0.27 per GPU-hour and USD 2.16 an hour for the node | capture: sha256:bb0cd0cc13380017201b5f563ce61efac6ee23b68644efaa56aff69b0f0c46a3 | quote: | CirrascaleCirrascale | 8×NVIDIA RTX A400016GB VRAM | 16GB | 40 vCPU256GB RAM2610GB Storage | United States | $0.27/GPU/hr$2.16/hr total (8×) |
- sources:
  - [1] https://gpuperhour.com/providers/cirrascale
  - [2] https://www.cirrascale.com/pricing

## Denvr

- `compute/denvr` | paid-only | evidence reported | binding none | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:26.531Z (live) | stale on 2026-11-18
- url https://gpuperhour.com/providers/denvr
- free tier: no free tier. The vendor pricing page lists on-demand rates per GPU-hour: H100 SXM (8 GPUs, 80 GB) USD 2.45; A100 SXM (8 GPUs, 80 GB) USD 1.45; A100 SXM (8 GPUs, 40 GB) USD 1.15; A100 PCIe (4 GPUs, 40 GB) USD 1.15; A100 MIG (1 GPU, 20 GB) USD 0.58; A40 (4 GPUs, 48 GB) USD 0.65; GH200 (1 GPU, 96 GB) USD 3.87; Intel Gaudi 2 (8 GPUs, 96 GB) USD 1.10; H200 SXM reserved only. The page lists no L40S, no L4 and no GeForce RTX card. 'Per-Minute Billing': on-demand instances are billed by the minute. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not published on the page read | metered: no | source: [2]
- identity: email | detail: the pricing page states 'Pay securely with prepaid credit cards or via invoiced bank transfer.'; unverified: the sign-up form fields are behind a sign-up
- interface: unknown
- limits note: No quota is stated on the vendor pricing page: it publishes price per GPU, GPU count, VRAM, vCPUs, memory, local storage and interconnect. Instances come in 1, 2, 4 or 8 GPUs on bare metal or virtualized; the A100 MIG row is a single 20 GB slice at USD 0.58 an hour. Reserved contracts save up to 20 percent.
- binding note: No quota is stated on the page: it publishes price, VRAM, host specs, region and status. The wall is the node shape, because the cheapest rate is a four-card node at USD 2.60 an hour total.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read
- composes with: The Gaudi 2 row at USD 1.10 per GPU-hour with 96 GB of accelerator memory is the cheapest large-memory device among evaluated providers and the only non-NVIDIA entry besides Sesterce's AMD lines, so it is the row that matters if the workload can use a non-CUDA toolchain. 30 TB of local storage on that node also makes it a candidate for a job that reads a large corpus once.
- reliability: no reliability event recorded
- notes: Found via gpuperhour. json, which mentions the name). verification criteria: the vendor's own pricing page for the billing unit and whether a single A40 can be booked.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 128
  - facets.shape.ram_gib: 512
  - facets.shape.disk_gib: 7600
  - facets.shape.gpu_class: NVIDIA A40 48GB
  - facets.shape.gpu_count: 4
- evidence:
  - [2] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): Denvr | 4xNVIDIA A40 48GB VRAM | 48GB | 128 vCPU 512GB RAM 7600GB Storage | Virginia | $0.65/GPU/hr $2.60/hr total (4x)
  - [2] 2026-10-22: further rows, transcribed and joined (unquoted values are not verbatim): 8xIntel Gaudi 2 96GB VRAM | 96GB | 160 vCPU 1024GB RAM 30400GB Storage | Virginia | $1.10/GPU/hr; 4xNVIDIA A100 PCIe 80GB | 80GB | 64 vCPU 512GB RAM 7600GB Storage | Virginia | $1.15/GPU/hr; '7 offers available'
  - [1] 2026-11-03: the vendor pricing table row for the H100 SXM: 8 GPUs of 80 GB, 208 vCPUs, 1024 GB memory, price $2.45 per GPU; the same table lists A100 SXM 80 GB at $1.45, A100 SXM 40 GB and A100 PCIe 40 GB at $1.15, A100 MIG at $0.58, A40 at $0.65 | capture: sha256:442d38757ae672890abf903263ccd27e6aaef0e26b69bea81b6aa3abbe1c2631 | quote: NVIDIA H100 SXM 8 80 GB 208 1024 GB 6x 3.8TB NVMe IB 3200G $2.45 / GPU
  - [1] 2026-11-03: the vendor pricing page states per-minute billing for on-demand instances | capture: sha256:442d38757ae672890abf903263ccd27e6aaef0e26b69bea81b6aa3abbe1c2631 | quote: Scale up or down instantly with on-demand instances billed by the minute.
  - [1] 2026-11-03: instances come in 1, 2, 4 or 8 GPUs, bare metal or virtualized, so the node shape is not a floor of four cards | capture: sha256:442d38757ae672890abf903263ccd27e6aaef0e26b69bea81b6aa3abbe1c2631 | quote: Available in bare metal and virtualized configurations with 1, 2, 4 or 8 multi-GPUs.
  - [1] 2026-11-03: the vendor names prepaid credit cards or invoiced bank transfer as its payment methods; the sign-up form was not read | capture: sha256:442d38757ae672890abf903263ccd27e6aaef0e26b69bea81b6aa3abbe1c2631 | quote: Pay securely with prepaid credit cards or via invoiced bank transfer.
  - [1] 2026-11-03: billing granularity of on-demand instances is one minute; no minimum bill is stated | capture: sha256:442d38757ae672890abf903263ccd27e6aaef0e26b69bea81b6aa3abbe1c2631 | quote: Scale up or down instantly with on-demand instances billed by the minute.
  - [1] 2026-11-03: the vendor page publishes on-demand and reserved rates and states no free allowance | capture: sha256:442d38757ae672890abf903263ccd27e6aaef0e26b69bea81b6aa3abbe1c2631 | quote: Save up to 20% with multi-month or annual commitments.
- sources:
  - [1] https://www.denvr.com/pricing
  - [2] https://gpuperhour.com/providers/denvr

## Lyceum

- `compute/lyceum` | paid-only | evidence documented | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:28.020Z (live) | stale on 2026-12-04
- url https://gpuperhour.com/providers/lyceum
- free tier: GPUs are billed per second with no subscription. USD per GPU hour, on demand / spot: NVIDIA H100 80 GB $4.69 / $2.39, NVIDIA A100 80 GB $2.29 / $1.19, NVIDIA L40S 48 GB $1.99 / not offered. The page lists no RTX 4090 or L4 and states no minimum bill. A third-party index lists the L40S in Europe with 12 vCPU, 128 GB RAM and 100 GB storage at the same USD 1.99 per GPU-hour, and an A100 PCIe 80 GB at USD 2.29 per GPU-hour on a 16 vCPU, 120 GB host. | unit: hours | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not published on the page read | metered: no | source: [2]
- identity: email | detail: not stated
- interface: rest
- limits note: No quota is stated on the page: price, VRAM, host specs, region and status are all it publishes. The page's own differentiator is per-second billing and a spot book exposed through an API, neither of which is a quota.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: the about block states 'On-demand and spot price book exposed through the API' and 'Email and webhook GPU availability r', the sentence truncated in the extract; no API documentation URL is given
- composes with: The 100 GB disk is small for a training job, so checkpoints have to go elsewhere
- reliability: no reliability event observed; the 8x configuration of the same card was Sold Out while the 1x and 2x were Available on the read, which is the kind of movement the index records.
- notes: Found via gpuperhour. verification criteria: the vendor's own price book through its API, which the about block says exists but does not link.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 12
  - facets.shape.ram_gib: 128
  - facets.shape.disk_gib: 100
  - facets.shape.gpu_class: NVIDIA L40S 48GB
  - facets.shape.gpu_count: 1
- evidence:
  - [2] 2026-10-22: row fields, transcribed and joined (unquoted values are not verbatim): Lyceum | NVIDIA L40S 48GB VRAM | 48GB | 12 vCPU 128GB RAM 100GB Storage | Europe | $1.99/GPU/hr | Available; the 8x row at the same rate reads 'Sold Out'
  - [2] 2026-10-22: about block, transcribed and joined: 'Founded 2024', 'Berlin, Germany and Zurich, Switzerland', Best For: European GPU data residency, On-demand and spot H100, H200, and A100 virtual machines, Per-second GPU workloads, Reserved multi-node InfiniBand clusters; '24 offers available'
  - [1] 2026-11-03: the vendor pricing page bills GPUs per second with no subscription and lists H100, A100 and L40S rates on demand and spot | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: USD per GPU hour, billed per second with no subscription
  - [1] 2026-11-03: the stated rates are read on the vendor's page | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: USD per GPU hour, billed per second with no subscription
  - [1] 2026-11-03: the vendor pricing page was read on this date | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: USD per GPU hour, billed per second with no subscription
  - [1] 2026-11-03: the rates and billing granularity are first-party | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: USD per GPU hour, billed per second with no subscription
  - [1] 2026-11-03: H100 80 GB is USD 4.69 per GPU hour on demand and USD 2.39 spot | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: NVIDIA H10080 GB$4.69$2.39
  - [1] 2026-11-03: A100 80 GB is USD 2.29 per GPU hour on demand and USD 1.19 spot | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: NVIDIA A10080 GB$2.29$1.19
  - [1] 2026-11-03: L40S 48 GB is USD 1.99 per GPU hour on demand and not offered on spot | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: NVIDIA L40S48 GB$1.99Not offered
  - [2] 2026-11-03: the third-party index lists an A100 PCIe 80 GB on a 16 vCPU, 120 GB host | capture: sha256:2a3e13f70770616ec70d96ce8714bc50231cd0641b9606fa598b4ba39ec914db | quote: NVIDIA A100 PCIe 80GB80GB VRAM | 80GB | 16 vCPU120GB RAM100GB Storage
  - [1] 2026-11-03: the vendor pricing page confirms per-second billing and the listed GPU rates | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: USD per GPU hour, billed per second with no subscription
- sources:
  - [1] https://www.lyceum.technology/pricing
  - [2] https://gpuperhour.com/providers/lyceum

## QuantaCloud

- `compute/quantacloud` | paid-only | evidence reported | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://gpuperhour.com/
- free tier: Named by a live stock-and-price tracker as the cheapest H100 PCIe offer with stock on 2026-10-22: H100 PCIe 80GB at USD 2.59 per GPU-hour, across five providers that report stock on that model. The tracker counts 20,068 configurations from 31 providers, reads secure on-demand listings only, and requires a stock observation within 15 minutes of its refresh. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: unverified: the vendor page was not read and no signup route was established, so the identity kind is unknown. The reconcile pass should treat this as a gap rather than a finding.
- interface: unknown
- limits note: Terms and limits beyond published hourly rates are unconfirmed in available documentation.
- binding note: Binding constraints beyond published rates are unconfirmed in available documentation.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A 2.59 PCIe H100 undercuts the USD 3.29 H100 median and is close to the USD 2.27 preemptible H100 on Daytona, but with no preemption penalty if the listing is a secure offer.
- reliability: no reliability event recorded
- notes: It is recorded because the PCIe part sits between the two well-covered shapes, a 1.80 PCIe H100 at HyperAI and a 2.73 SXM H100 at Massed Compute, and a session pricing a PCIe H100 otherwise has no third point. The tracker's own caveat applies: an offer count is a count of configurations, not of physical GPUs.
- extras:
  - facets.class: gpu-broker-rate-floor
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: H100 PCIe
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 80
- evidence:
  - [1] 2026-10-22: quoted: 'The cheapest current H100 PCIe is $2.59 per GPU-hour on QuantaCloud', with 5 providers reporting stock on that model
  - [1] 2026-10-22: quoted method: 'All figures are the cheapest current secure on-demand price per GPU-hour tracked by GPUPerHour, excluding spot and peer-to-peer marketplace listings', 31 providers and 20,068 configurations, stock observation within 15 minutes
- sources:
  - [1] https://gpuperhour.com/
