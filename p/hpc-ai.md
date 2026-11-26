# HPC-AI.COM

> hpc-ai.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hpc-ai/ | JSON https://fshy.ajam.dev/api/v1/entity/hpc-ai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HPC-AI.COM

- `compute/hpc-ai` | paid-only | evidence documented | binding write-gated | category GPU cloud | tier On-Demand Cloud GPU (per GPU-hour)
- needs card yes, phone no, ID no, institution no | verified 2026-11-24T10:11:14.823Z (live) | stale on 2026-12-25
- url https://www.hpc-ai.com/pricing
- free tier: No standing free tier: the pricing page lists on-demand GPUs from $0.48 per GPU-hour (RTX-4090), a $0.03 per CPU-hour instance and $0.000100 per GB-hour of high-speed storage. The quickstart offers free credits on signup and top-up, but the voucher amounts are not published on the read pages and all funds deposited are non-refundable. | unit: none | metered on: unstated | read on: 2026-11-24 | source: [1] | note: The rate at published shape is per GPU-hour: B200 SXM from $7.50, H200 SXM from $2.68, H100 SXM from $2.42, RTX-4090 from $0.48 and RTX-5090 from $0.62 per GPU-hour; full-machine rentals are 8 cards only. Instances bill per minute with a one-minute minimum. Promotional voucher amounts are unverified: behind a sign-up and top-up.
- per-object cap: not applicable: the unit is a GPU instance or a remote storage volume, not a stored object; no per-object size cap is published | source: [1]
- retention: Data disks are not persistent once an instance is terminated; for On-Demand and Spot instances the data disk is cleared when the instance is stopped. A remote Storage Volume must be attached to keep data across stop or termination, and storage is billed per day on actual GB used. Local storage on instances is covered at no additional cost. | source: [2] | note: If an instance is terminated for insufficient credits, associated storage may be reclaimed; prepaid instances preserve the data disk until the prepaid period expires.
- egress: No per-GB egress price or free traffic allowance is published on the pricing, billing or quickstart pages read; the only published traffic-adjacent sentence is that the local storage on instances is covered at no additional cost. Remote storage is charged per day per GB used, not by bytes out. | metered: no | source: [1]
- identity: card | detail: Signup asks for details and optionally a Google account and requires email verification. Adding funds supports Stripe with credit or debit cards, Google Pay and Link; a card added through the console becomes the default for automatic payment. No phone number or ID document is requested on the read pages; the exact signup form fields are unverified: behind a sign-up.
- interface: ssh, browser, rest
- limits:
  - write-gated (binding): to launch an instance, the account must have enough credits to cover at least one hour of runtime at the selected specification; if the balance runs out, all active instances are stopped and local data disk contents are cleared [3]
  - volume-quota: GPU instances bill per minute with a one-minute minimum: RTX-4090 from $0.48/gpu/hour up to B200 SXM from $7.50/gpu/hour; CPU instances are a fixed $0.24 per CPU instance/hour and remote storage bills per day per GB used [1]
  - per-object-cap: full-machine rentals are supported with 8 cards only; Spot instances are interruptible by Prepaid or On-Demand instances [1]
- limits note: Membership plans ($1,000, $5,000 and $10,000 a month) grant monthly credits that apply only to on-demand pricing and expire 30 days after payment. Vouchers are deducted first, then monthly credits, then the balance. Unused balances are non-refundable.
- binding note: A new user without credits cannot launch any instance until a payment is made and the balance covers at least one hour at the chosen rate, so the prepaid balance gates before any GPU price or storage charge accrues.
- interface detail: Instances are reached by SSH with an uploaded public key or through a JupyterLab web button; the platform also exposes an OpenAI-compatible model API at https://api.hpc-ai.com/inference/v1 with a published OpenAI-compatible SDK package.
- endpoint: part of interface detail
- tooling: An SSH client with an uploaded key, the JupyterLab web interface, preconfigured CUDA, PyTorch and Colossal-AI images, Docker support and the @ai-sdk/openai-compatible package for the model API.
- composes with: A prepaid GPU cloud that runs training and inference jobs and attaches a remote Storage Volume for data that must survive an instance stop; with no published egress price, moving large results out needs a separate egress or storage record for a predictable cost.
- reliability: Instances stop when the balance runs out and local data disk contents are cleared; AutoPay checks run on an independent hourly schedule and a zero balance before the next check stops active instances. Spot instances are interruptible, and data disks are cleared on stop for On-Demand and Spot instances.
- notes: A prepaid GPU cloud at $0.48 to $7.50 per GPU-hour with per-minute billing and a one-minute minimum. No standing free allowance is published; the quickstart mentions signup and top-up vouchers whose amounts are not on the read pages. Data disks are cleared on stop, so a remote Storage Volume is needed for durable data. The model API at api.hpc-ai.com/inference/v1 is a separate product from the GPU instances priced here.
- evidence note: Rates, billing model, storage terms, prepayment gate, signup and payment methods, SSH and JupyterLab access are quoted from HPC-AI's own pricing, billing and quickstart pages read on 2026-11-24; the model API base and count come from models.dev the same day. Signup form details and voucher amounts are unverified behind a sign-up.
- extras:
  - shape.vcpu: 25
  - shape.ram_gib: 40
  - shape.disk_gib: 180
  - shape.gpu_class: NVIDIA RTX-4090
  - shape.gpu_count: 1
  - shape.note: cheapest on-demand machine in the published table: RTX-4090, 40 GB VRAM, 180 GB nvme, 25 CPU cores
  - billing_model: per-minute on-demand from $0.48/gpu/hour, prepaid balance, membership credits and spot
  - free_tier_kind: none-published
  - term: pay as you go with prepaid balance; no published long-term commitment
  - price_arithmetic: $0.48 per RTX-4090 GPU-hour x 730 hours = USD 350.40 a month at full utilisation; computed from the quoted hourly rate only
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: not stated for the on-demand instance tier
  - session_cap.restart_required: no
  - session_cap.note: bills per minute with a one-minute minimum; instances stop when the balance runs out
- evidence:
  - [1] 2026-11-24: the cheapest published GPU rate is the RTX-4090 at from $0.48 per GPU-hour | capture: sha256:fcee184fc05b067debc90992b6c0f33b8fc4cbc9b323f83a0ca071552743fe0d | quote: | RTX-4090 | 40 GB VRAM, 180 GB nvme, 25 CPU Cores | From $0.48/gpu/hour |
  - [1] 2026-11-24: the published on-demand GPU rate table spans $0.48 to $7.50 per GPU-hour and full-machine rentals are 8 cards only | capture: sha256:fcee184fc05b067debc90992b6c0f33b8fc4cbc9b323f83a0ca071552743fe0d | quote: | B200 SXM | 200 GB RAM, 1000 GB nvme, 25 CPU Cores | From $7.50/gpu/hour |
  - [1] 2026-11-24: the CPU instance rate is $0.03 per CPU-hour and high-speed storage from $0.000100 per GB-hour | capture: sha256:fcee184fc05b067debc90992b6c0f33b8fc4cbc9b323f83a0ca071552743fe0d | quote: | CPU instance | 8 vCPUs, 18GB RAM, 50GB nvme | $0.03/cpu/hour |
  - [1] 2026-11-24: high-speed storage is priced per GB-hour with no egress price published | capture: sha256:fcee184fc05b067debc90992b6c0f33b8fc4cbc9b323f83a0ca071552743fe0d | quote: | High-Speed Storage | Low-latency storage optimized for high-throughput AI workloads | From $0.000100/GB/hour |
  - [3] 2026-11-24: instances stop when the balance runs out | capture: sha256:a83593833458677f31ad16874295ff17fe3075783a957e150d52b1171b5f605b | quote: If your balance runs out, all active instances will be stopped, and you will get a notification.
  - [3] 2026-11-24: launching requires credits covering at least one hour at the chosen specification | capture: sha256:a83593833458677f31ad16874295ff17fe3075783a957e150d52b1171b5f605b | quote: To launch an instance, your account must have enough credits to cover at least one hour of runtime at the selected specification.
  - [2] 2026-11-24: email verification is required and funds are added through Stripe with cards, Google Pay or Link | capture: sha256:154fdc147523cc0e338a9e4866615c76b254f3c965088f8b229aae12e3e12beb | quote: 2. Verify your email address to activate your account.
  - [2] 2026-11-24: the payment methods accepted are credit or debit cards, Google Pay and Link via Stripe | capture: sha256:154fdc147523cc0e338a9e4866615c76b254f3c965088f8b229aae12e3e12beb | quote: Our platform currently supports payments via Stripe using Credit/Debit Cards, Google Pay, and Link for quick and easy transactions.
  - [2] 2026-11-24: instances are reached by JupyterLab or SSH with an uploaded public key | capture: sha256:154fdc147523cc0e338a9e4866615c76b254f3c965088f8b229aae12e3e12beb | quote: There are two ways to access your GPU instance once its status is 'Running': img_9.png 1. Click the JupyterLab button to access the instance via the web interface. 2. Copy the SSH command to connect to the instance via terminal.
  - [4] 2026-11-24: models.dev lists 9 HPC-AI models at API base https://api.hpc-ai.com/inference/v1 | capture: sha256:bb1bf57c417ee226ff9eb61ff437013bdc6eee8a721d10aa44c88f75c2494f93 | quote: API https://api.hpc-ai.com/inference/v1
- sources:
  - [1] https://www.hpc-ai.com/pricing
  - [2] https://www.hpc-ai.com/doc/docs/quickstart/
  - [3] https://www.hpc-ai.com/doc/docs/billing/
  - [4] https://models.dev/providers/hpc-ai
