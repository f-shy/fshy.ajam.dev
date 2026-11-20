# Crusoe

> crusoe.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crusoe/ | JSON https://fshy.ajam.dev/api/v1/entity/crusoe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Crusoe

- `compute/crusoe` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:26.530Z (live) | stale on 2026-12-04
- url https://www.crusoe.ai/cloud/pricing
- free tier: no free tier: hourly GPU capacity including GB200 NVL72 and MI355X, and dedicated inference endpoints that need no sales engagement | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): on demand, per GPU-hour: NVIDIA H100 80GB HGX $3.90, A100 80GB SXM $2.30, A100 80GB PCIe $2.00, L40S 48GB $1.50; from Dec 1, 2026 the H100 80GB HGX on-demand rate is $4.50 and the A100 and L40S rates are unchanged; billed per hour or per second with no minimum commitment; spot is stated as discounted with no figure; the page lists no GeForce RTX card and no L4; no free allowance [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and describes hourly GPU and dedicated-endpoint pricing. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.gpu_class: NVIDIA GB200 NVL72
  - shape.note: GB200 NVL72 and AMD MI355X are the named new classes
  - session_cap.restart_required: no
  - session_cap.note: hourly billing on instances and endpoints; the page states no reap
  - free_tier_kind: none
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Access the latest high-performance GPUs including NVIDIA GB200 NVL72 and AMD MI355X. Pay by the hour for maximum agility and unthrottled compute' and 'Spin up dedicated endpoints for open and fine-tuned models in minutes - no sales engagement required', quoted
  - [1] 2026-11-03: the Current on-demand column of the GPU instances table, in row order H100 80GB HGX, A100 80GB SXM, A100 80GB PCIe, L40S 48GB, gives $3.90, $2.30, $2.00, $1.50 per GPU-hr (the reader output keeps the row order, not row labels; the H100 figure agrees with the vendor support article) | capture: sha256:bb04c65a0e0662833b010a97e468a4559a1d1845e7d8c1e53d170c9655d7eb34 | quote: $3.90 / GPU-hr $2.30 / GPU-hr $2.00 / GPU-hr $1.50 / GPU-hr
  - [1] 2026-11-03: billing granularity of on-demand capacity is per hour or per second, with no minimum commitment; spot discount is stated without a figure | capture: sha256:bb04c65a0e0662833b010a97e468a4559a1d1845e7d8c1e53d170c9655d7eb34 | quote: On-demand pricing is our most flexible option, billed per-hour (or per-second) with no minimum commitment
  - [1] 2026-11-03: Self-Serve Deployments (dedicated inference endpoints) price the H100 80GB HGX at $5.50 per GPU-hr now and $6.30 per GPU-hr from Dec 1, 2026 | capture: sha256:bb04c65a0e0662833b010a97e468a4559a1d1845e7d8c1e53d170c9655d7eb34 | quote: #### [NVIDIA H100 80GB HGX](https://www.crusoe.ai/cloud/gpus/nvidia-h100) $5.50 / GPU-hr $6.30 / GPU-hr
  - [2] 2026-11-03: a vendor support article last updated Oct 20, 2025 gives the H100 80GB SXM at $3.90 per GPU-hour on demand across 8 GPUs, agreeing with the pricing page; its A100 and L40S rows are older rates and are not used | capture: sha256:f6bf3dab3db9dc3d1f9f13b73b9c74770ec2bd9cce5c430ae25d1994f0484cf2 | quote: | NVIDIA H100 80GB SXM | $3.90/hr | 8 | $31.20/hr |
  - [1] 2026-11-03: GPU instances are pay-by-the-hour with no free allowance stated | capture: sha256:bb04c65a0e0662833b010a97e468a4559a1d1845e7d8c1e53d170c9655d7eb34 | quote: Pay by the hour for maximum agility and unthrottled compute
- sources:
  - [1] https://www.crusoe.ai/cloud/pricing
  - [2] https://support.crusoecloud.com/hc/en-us/articles/37421109850907-FAQ-Determining-On-Demand-Pricing-for-Crusoe-Offerings
