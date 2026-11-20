# Hexgrid Cloud

> hexgrid.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hexgrid/ | JSON https://fshy.ajam.dev/api/v1/entity/hexgrid.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hexgrid Cloud

- `compute/hexgrid-cloud` | paid-only | evidence documented | binding none | category GPU cloud | tier Secure Cloud on-demand
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:21.683Z (live) | stale on 2026-12-04
- url https://hexgrid.cloud/gpus
- free tier: no free tier: dedicated GPUs by the hour, billed per minute, 13 models from $0.20 to $7.50 per GPU-hour. H100 80 GB SXM $2.99 (PCIe $2.75), A100 80 GB $1.49 (PCIe and SXM), L40S $1.00, RTX 4090 $0.45. The page lists no L4. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable: the unit is a GPU-hour, not an object | source: [1]
- retention: the home page says models, custom nodes, workflows and outputs are kept in persistent storage for the ComfyUI workspace product; no retention period is stated for GPU instances | source: [2]
- egress: the GPU page says 'One rate per GPU hour, whatever you run on it. No instance-type maths, no egress surprises.'; no egress price is published on the pages read | metered: no | source: [1]
- identity: email | detail: unverified: the home page sends the visitor to a dashboard to deploy and the docs do not describe signup; no form was read, so email is the assumed minimum and card, phone and company checks are not established.
- interface: ssh
- limits note: no session cap, idle reap or quota is published on the pages read; the home page states hourly billing with no minimums
- binding note: no cap is published; the cost is per GPU-hour, billed per minute, with no minimums
- interface detail: the home page says to connect over SSH with full root access; a web dashboard launches instances. No API is documented on the pages read.
- tooling: a web dashboard and SSH with root access on a dedicated GPU; a separate ComfyUI workspace product launches preconfigured image and video workflows on a private GPU. The docs site is built on Mintlify and lists two products, ComfyUI Cloud and GPU Instances.
- composes with: unverified: no API, CLI or template route is documented on the pages read, so scripted launches are not established.
- reliability: unverified: no status page or incident history was read
- notes: the vendor also sells ComfyUI workspaces on a private GPU; this record prices the GPU rental page.
- evidence note: the hourly rates are read on the vendor's own GPU page on 2026-11-03; the identity cost is unverified
- evidence:
  - [1] 2026-11-03: H100 80 GB SXM at $2.99 per GPU-hour on the vendor's own page | capture: sha256:df66c913877086ef7452062809b43b06603314a3ad41ca33b7759c6e826951a9 | quote: ### NVIDIA H100 80GB SXM ↗ 1–8× Secure Cloud vRAM: 80 GB Per GB vRAM: $0.037/hr $2.99per GPU-hr
  - [1] 2026-11-03: A100 80 GB SXM at $1.49 per GPU-hour | capture: sha256:df66c913877086ef7452062809b43b06603314a3ad41ca33b7759c6e826951a9 | quote: ### NVIDIA A100 80GB SXM ↗ 1–8× Secure Cloud vRAM: 80 GB Per GB vRAM: $0.019/hr $1.49per GPU-hr
  - [1] 2026-11-03: L40S at $1.00 per GPU-hour | capture: sha256:df66c913877086ef7452062809b43b06603314a3ad41ca33b7759c6e826951a9 | quote: ### NVIDIA L40S ↗ 1–8× Secure Cloud vRAM: 48 GB Per GB vRAM: $0.021/hr $1.00per GPU-hr
  - [1] 2026-11-03: RTX 4090 at $0.45 per GPU-hour | capture: sha256:df66c913877086ef7452062809b43b06603314a3ad41ca33b7759c6e826951a9 | quote: ### RTX 4090 ↗ 1–8× Secure Cloud vRAM: 24 GB Per GB vRAM: $0.019/hr $0.45per GPU-hr
  - [1] 2026-11-03: 13 GPU models, billing per GPU-hour by the minute | capture: sha256:df66c913877086ef7452062809b43b06603314a3ad41ca33b7759c6e826951a9 | quote: 13 GPUs · $0.20–$7.50/hr
  - [1] 2026-11-03: rates are per GPU-hour billed per minute | capture: sha256:df66c913877086ef7452062809b43b06603314a3ad41ca33b7759c6e826951a9 | quote: All rates are per GPU hour, billed per minute.
  - [1] 2026-11-03: the page makes a no-egress-surprises statement and publishes no egress price | capture: sha256:df66c913877086ef7452062809b43b06603314a3ad41ca33b7759c6e826951a9 | quote: One rate per GPU hour, whatever you run on it. No instance-type maths, no egress surprises.
  - [2] 2026-11-03: persistent storage for the ComfyUI workspace product | capture: sha256:fd12e19e2e7f156a3243fab9765cc27796626f01c15630520f96d8c85fcab19d | quote: Keep your models, custom nodes, workflows, and outputs in persistent storage.
  - [2] 2026-11-03: hourly billing with no minimums | capture: sha256:fd12e19e2e7f156a3243fab9765cc27796626f01c15630520f96d8c85fcab19d | quote: Hourly billing · no minimums
  - [2] 2026-11-03: dedicated hardware over SSH with full root access | capture: sha256:fd12e19e2e7f156a3243fab9765cc27796626f01c15630520f96d8c85fcab19d | quote: Choose dedicated hardware by the hour, connect over SSH, and run your own stack with full root access.
  - [2] 2026-11-03: a content rule of the platform | capture: sha256:fd12e19e2e7f156a3243fab9765cc27796626f01c15630520f96d8c85fcab19d | quote: PS: NSFW content creation is NOT allowed on the platform.
  - [3] 2026-11-03: the price index agrees on the H100 SXM rate | capture: sha256:a7b2542d69af6a624d7b44938651494060d63cb228c51a19ea24f73238d0b398 | quote: | [H100 SXM](https://computeprices.com/providers/hexgrid/gpus/h100)1× | $2.99/hr |
- sources:
  - [1] https://hexgrid.cloud/gpus
  - [2] https://hexgrid.cloud/
  - [3] https://computeprices.com/providers/hexgrid
