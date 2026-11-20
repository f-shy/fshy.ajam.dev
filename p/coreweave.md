# CoreWeave

> coreweave.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/coreweave/ | JSON https://fshy.ajam.dev/api/v1/entity/coreweave.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoreWeave

- `compute/coreweave` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-06T18:41:34.658Z (live) | stale on 2026-12-07
- url https://www.coreweave.com/pricing
- free tier: no free tier: GPU capacity at on-demand rates per 8-GPU node from $10.00 an hour for an L40 node to $68.80 for an HGX B200 node, with spot at about 40 to 63 percent of the on-demand rate on the rows that list both and no free allowance | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no egress charge: data transfer between CoreWeave and the internet is listed as Free, as are egress and input/output operations per second and the NAT gateway | metered: no | free allowance: unmetered: data transfer between CoreWeave and the internet is Free | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): on demand, per instance-hour, each row a node of 8 GPUs unless stated: $18.00 for L40S, $20.00 for RTX PRO 6000 Blackwell (High Memory), $21.60 for A100 80 GB, $49.24 for HGX H100, $68.80 for HGX B200; the page lists no RTX 4090 or L4 [1]
  - request-rate (binding): spot runs at $34.11 to $35.84 an hour on the rows shown, roughly half on-demand [1]
  - per-object-cap: local storage is priced per TB alongside the GPU [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: No free tier makes this a paid-only product, not a closed one; `dead` is reserved for a product that is withdrawn or unreachable. Per-card rates on the pricing page read on 2026-11-06: HGX H100 USD 49.24 per hour for an 8-GPU node, USD 6.16 per GPU-hour; A100 80GB USD 21.60 per hour for an 8-GPU node, USD 2.70 per GPU-hour; L40S USD 18.00 per hour for an 8-GPU node, USD 2.25 per GPU-hour; L40 USD 10.00 per hour for an 8-GPU node, USD 1.25 per GPU-hour; RTX 4090 and L4 are not listed. Egress is free: data transfer between CoreWeave and the internet is listed as Free.
- evidence note: the pricing page was read on 2026-10-22 and publishes on-demand, spot and inference rates. There is no free tier, so the verdict moves to paid-only and the spot rate is recorded as the discount path
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: NVIDIA RTX PRO 6000 Blackwell Server Edition
  - shape.gpu_count: 8
  - shape.note: the cheapest named row at $20.00 an hour; larger nodes run to $68.80
  - session_cap.restart_required: no
  - session_cap.note: on-demand and spot instances bill per hour; the page states no reap
  - free_tier_kind: none
  - reclassified_from: dead
  - ps.price: local storage priced per TB per hour
  - ps.durability: local NVMe
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the instance's life
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'On-Demand Price: $42.00 / Hour', 'On-Demand Price: $68.80 / Hour' with 'Spot Price: $34.11 / Hour', 'Inference Single CPU Price: $8.60 / Hour' and 'NVIDIA RTX PRO 6000 Blackwell Server Edition (High Memory) On-Demand Price: $20.00 / Hour', quoted
  - [1] 2026-11-03: the HGX H100 row has GPU Count 8 and an on-demand price of $49.24 per hour, so the price is for the 8-GPU node, not one GPU | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: ### NVIDIA HGX H100 8 80 128 2,048 61.44 $49.24
  - [1] 2026-11-03: HGX H100 node: on demand $49.24 per hour, spot $19.71 per hour, single-GPU inference $6.16 per hour | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: On-Demand Price: $49.24 / Hour Spot Price: $19.71 / Hour Inference Single CPU Price: $6.16 / Hour
  - [1] 2026-11-03: the $20.00 per hour row is an 8-GPU node with 96 GB VRAM per GPU, 128 vCPU and 1,024 GB RAM | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: ### NVIDIA RTX PRO 6000 Blackwell Server Edition (High Memory) 8 96 128 1,024 7.68 $20.00
  - [1] 2026-11-03: L40S node of 8 GPUs with 48 GB VRAM each, North America: on demand $18.00 per hour, spot $7.88 per hour, single-GPU inference $2.25 per hour; the Europe table lists the same on-demand price with spot N/A | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: On-Demand Price: $18.00 / Hour Spot Price: $7.88 / Hour Inference Single CPU Price: $2.25 / Hour
  - [1] 2026-11-03: A100 node of 8 GPUs with 80 GB VRAM each, North America: on demand $21.60 per hour, spot $9.65 per hour, single-GPU inference $2.70 per hour; Europe spot is $9.51; the page lists no RTX 4090 or L4 and states no billing increment or minimum bill | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: On-Demand Price: $21.60 / Hour Spot Price: $9.65 / Hour Inference Single CPU Price: $2.70 / Hour
  - [1] 2026-11-03: on-demand, spot and committed-use rates are published and no free allowance is stated | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: CoreWeave offers up to 60% discounts over our On-Demand prices for committed usage.
  - [1] 2026-11-03: the L40 row is an 8-GPU node at $10.00 an hour on demand, the cheapest 8-GPU on-demand row on the page (L40S is $18.00, RTX PRO 6000 High Memory is $20.00) | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: ### NVIDIA L40 8 48 128 1,024 7.68 $10.00
  - [1] 2026-11-03: L40 North America: on demand $10.00 per hour and spot $6.27 per hour, so spot is the highest share of on-demand on the page; the Europe table lists L40 spot as N/A | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: On-Demand Price: $10.00 / Hour Spot Price: $6.27 / Hour
  - [1] 2026-11-03: HGX H100 Europe: on demand $49.24 and spot $19.51, the lowest share of on-demand on the page | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: On-Demand Price: $49.24 / Hour Spot Price: $19.51 / Hour
  - [1] 2026-11-03: HGX B200 8-GPU node: on demand $68.80 per hour, the highest 8-GPU on-demand price listed | capture: sha256:93b95f326539af056f2839f881057a44efc5ca542a2d698295f9d3e7d3803250 | quote: On-Demand Price: $68.80 / Hour Spot Price: $34.11 / Hour
  - [1] 2026-11-06: an HGX H100 node of 8 GPUs is USD 49.24 per hour on demand and the page's single-GPU price is USD 6.16 per hour | capture: sha256:cd21170e75938f104fccb563ba66b9bd95eec248f3b7dc4cc4e08e637a450bcf | quote: On-Demand Price: $49.24 / Hour Spot Price: $19.71 / Hour Inference Single CPU Price: $6.16 / Hour
  - [1] 2026-11-06: an A100 80GB node of 8 GPUs is USD 21.60 per hour on demand, USD 2.70 per GPU-hour | capture: sha256:cd21170e75938f104fccb563ba66b9bd95eec248f3b7dc4cc4e08e637a450bcf | quote: On-Demand Price: $21.60 / Hour Spot Price: $9.65 / Hour Inference Single CPU Price: $2.70 / Hour
  - [1] 2026-11-06: an L40S node of 8 GPUs is USD 18.00 per hour on demand, USD 2.25 per GPU-hour | capture: sha256:cd21170e75938f104fccb563ba66b9bd95eec248f3b7dc4cc4e08e637a450bcf | quote: On-Demand Price: $18.00 / Hour Spot Price: $7.88 / Hour Inference Single CPU Price: $2.25 / Hour
  - [1] 2026-11-06: data transfer between CoreWeave and the internet is listed as Free | capture: sha256:cd21170e75938f104fccb563ba66b9bd95eec248f3b7dc4cc4e08e637a450bcf | quote: ### Data transfer between CoreWeave and internet Free
  - [1] 2026-11-06: the A100 row is 8 GPUs of 80 GB VRAM at USD 21.60 an hour, so the per-card figure is the node price divided by 8 | capture: sha256:cd21170e75938f104fccb563ba66b9bd95eec248f3b7dc4cc4e08e637a450bcf | quote: ### NVIDIA A100 8 80 128 2,048 7.68 $21.60
- sources:
  - [1] https://www.coreweave.com/pricing
