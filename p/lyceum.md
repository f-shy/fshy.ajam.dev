# Lyceum

> lyceum.technology | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lyceum/ | JSON https://fshy.ajam.dev/api/v1/entity/lyceum.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lyceum

- `compute/lyceum` | paid-only | evidence documented | binding none | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-24T18:47:20.587Z (live) | stale on 2026-12-25
- url https://www.lyceum.technology/pricing
- free tier: USD per GPU hour, billed per second with no subscription: NVIDIA H100 USD 5.39 on demand / USD 2.69 spot; NVIDIA A100 USD 2.59 / USD 1.29; NVIDIA L40S USD 2.19 / USD 1.09. | unit: hours | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: none
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: not published on the page read | metered: no | source: [2]
- identity: email | detail: The dashboard sign-up page says 'Sign up or log in' and offers 'Continue with Google', 'Continue with GitHub', 'Continue with SSO' and 'Continue with email'. The page asks for no card, phone number or ID document.
- interface: rest
- limits note: No quota is stated on the page: price, VRAM, host specs, region and status are all it publishes. The page's own differentiator is per-second billing and a spot book exposed through an API, neither of which is a quota.
- binding note: the same as limits note
- interface detail: OpenAI-compatible REST endpoint at https://api.lyceum.technology/openai/v1.
- tooling: OpenAI-compatible endpoint at https://api.lyceum.technology/openai/v1; POST /chat/completions and GET /models; Lyceum API key (lk_...).
- composes with: An L40S in Europe is listed on the vendor page at USD 2.19 per GPU-hour on demand; the third-party index lists the L40S at USD 2.39 per GPU-hour with 12 vCPU and 128 GB RAM.
- reliability: no reliability event observed; the 8x configuration of the same card was Sold Out while the 1x and 2x were Available on the read, which is the kind of movement the index records.
- notes: The GPU rates are on the vendor's pricing page; the bare inference endpoint answers 404 to GET without a key.
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
  - [1] 2026-11-24: H100 80 GB is USD 5.39 per GPU hour on demand and USD 2.69 spot | capture: sha256:d96ca0a94aff717ad52a20678ee0ea5730245e4ae177d95a290181fe24991e5e | quote: NVIDIA H10080 GB$5.39$2.69
  - [1] 2026-11-24: A100 80 GB is USD 2.59 per GPU hour on demand and USD 1.29 spot | capture: sha256:d96ca0a94aff717ad52a20678ee0ea5730245e4ae177d95a290181fe24991e5e | quote: NVIDIA A10080 GB$2.59$1.29
  - [1] 2026-11-24: L40S 48 GB is USD 2.19 per GPU hour on demand and USD 1.09 spot | capture: sha256:d96ca0a94aff717ad52a20678ee0ea5730245e4ae177d95a290181fe24991e5e | quote: NVIDIA L40S48 GB$2.19$1.09
  - [2] 2026-11-03: the third-party index lists an A100 PCIe 80 GB on a 16 vCPU, 120 GB host | capture: sha256:2a3e13f70770616ec70d96ce8714bc50231cd0641b9606fa598b4ba39ec914db | quote: NVIDIA A100 PCIe 80GB80GB VRAM | 80GB | 16 vCPU120GB RAM100GB Storage
  - [1] 2026-11-03: the vendor pricing page confirms per-second billing and the listed GPU rates | capture: sha256:b9913cc9d3ededa9a80fd834142db63e54804b07af3046ba97b466c0f00f8f22 | quote: USD per GPU hour, billed per second with no subscription
  - [1] 2026-11-24: GPU prices are per GPU-hour with per-second billing and no subscription | capture: sha256:d96ca0a94aff717ad52a20678ee0ea5730245e4ae177d95a290181fe24991e5e | quote: USD per GPU hour, billed per second with no subscription
  - [3] 2026-11-24: the inference API has a documented base URL | capture: sha256:51e7ed7fc2d72ae916bb840e48b883c24a228d01d9195bd1a0c9398185bd747c | quote: The base URL for serverless inference is:
  - [3] 2026-11-24: the API requires a Lyceum API key | capture: sha256:51e7ed7fc2d72ae916bb840e48b883c24a228d01d9195bd1a0c9398185bd747c | quote: Authenticate with your Lyceum API key (`lk_...`) as a Bearer token.
  - [2] 2026-11-24: the third-party index lists the L40S at USD 2.39 per GPU-hour with 12 vCPU, 128 GB RAM and 100 GB storage | capture: sha256:36a30c4543a9ccede09db4b59efb6005adf9cdf99ff41ee9b92bdf8e948d286c | quote: NVIDIA L40S48GB VRAM | 48GB | 12 vCPU128GB RAM100GB Storage | 🌍Europe | $2.39/GPU/hr | Available
  - probe:https://api.lyceum.technology/openai/v1 2026-11-24: the bare API endpoint answered HTTP 404 | capture: sha256:6bce8c7607f017f2e00f3717b79fa9531ea3ce2a2dd85155157f363da85c9cf6 | quote: "status": 404
  - [1] 2026-11-24: the pricing page lists reserved blocks and GPU rates but no egress volume terms | capture: sha256:d96ca0a94aff717ad52a20678ee0ea5730245e4ae177d95a290181fe24991e5e | quote: Reserved
  - [4] 2026-11-24: Lyceum account creation is gated by email or an OAuth/SSO account | capture: sha256:2ab46d555e58fb955db09ee542e4afde3a79aacf9e643febec034cfb01ae6449 | quote: Continue with Google Continue with GitHub Continue with SSO Continue with email
  - [4] 2026-11-24: an email or an OAuth/SSO account is the sign-up gate, with no card, phone or ID on the page | capture: sha256:2ab46d555e58fb955db09ee542e4afde3a79aacf9e643febec034cfb01ae6449 | quote: Continue with Google Continue with GitHub Continue with SSO Continue with email
- sources:
  - [1] https://www.lyceum.technology/pricing
  - [2] https://gpuperhour.com/providers/lyceum
  - [3] https://docs.lyceum.technology/docs/inference/serverless
  - [4] https://dashboard.lyceum.technology/
