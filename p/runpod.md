# runpod network

> runpod.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runpod/ | JSON https://fshy.ajam.dev/api/v1/entity/runpod.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunPod

- `compute/runpod` | paid-only | evidence documented | binding request-rate | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-25T15:03:46.646Z (live) | stale on 2026-12-26
- url https://www.runpod.io/pricing
- price parsed USD 116.8/mo
- free tier: On-demand RTX A5000 cloud GPU rental on Runpod. Community Cloud $0.16/hr, Secure Cloud $0.27/hr. | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: Community Cloud is cheaper than Secure Cloud for the same card; the page carries a per-hour and a per-second toggle, and 21 on-demand cards were read on 2026-10-24
- per-object cap: not applicable
- retention: network storage is billed while it exists; a pod keeps its volume only while attached or persisted | days: 0
- egress: The billing FAQ states 'no fees for data transfer'; the pricing page publishes no per-GB egress rate or transfer allowance. | metered: no | source: [1]
- identity: email | detail: Signup at console.runpod.io/signup is by Google, GitHub or email and password with no card; a Pod needs at least one hour of credits in the prepaid balance, and a card is one way to add them.
- interface: rest, cli
- limits:
  - request-rate (binding): no free tier; the cheapest published card is billed per second [1]
  - per-object-cap: up to 64 GPUs in a cluster; 8 vCPU and 8 GiB is not the shape on offer [1]
- limits note: storage from USD 0.05 per GB a month on standard network storage
- binding note: billing is per second with no free allowance, so the metered rate is what binds; there is no quota to exhaust
- interface detail: REST API, CLI and a web console; SSH into a pod
- tooling: runpodctl, the RunPod API, Docker images, network volumes
- composes with: a GPU pod is a server with a GPU, so it can hold a model and serve it; the free tier does not exist
- reliability: no reliability event recorded
- extras:
  - shape.gpu_class: B300
  - shape.gpu_count: 1
  - billing_model: allocated
  - granularity.min_billed_s: 1
  - granularity.rounding_s: 1
  - session_cap.restart_required: no
  - session_cap.note: none; a pod runs until stopped
  - keep_rate.value: 0.0
  - keep_rate.basis: a stopped pod does not bill compute, only storage
  - keep_rate.source: https://www.runpod.io/pricing
  - persistent_storage.price_gib_month: USD 0.05 and up
  - persistent_storage.durability: network volume
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while the volume exists
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a TCP port map and a proxy
  - free_tier_kind: none
  - m10h_usd: 1.6
  - m24h_usd: 116.8
  - price_arithmetic: USD 0.16/h is the cheapest card on the page read on 2026-10-24 (RTX A5000, Community Cloud); 10 h = USD 1.60 and 730 h = USD 116.80.
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: on-demand B300 at USD 6.94/h on Community Cloud and USD 8.99/h on Secure Cloud; H200 at USD 3.59 and USD 5.29
  - [1] 2026-10-24: the full on-demand card list, Community and Secure, quoted from the page's own rate data: RTX A5000 0.16/0.27, RTX 3090 0.22/0.50, RTX A6000 0.33/0.59, RTX 4090 0.34/0.89, A40 0.35/0.59, L4 0.44/0.59, Pro 6000 MIG 24GB 0.50/0.69, L40 0.69/0.82, RTX 5090 0.69/1.19, RTX 6000 Ada 0.74/0.99, L40S 0.79/1.09, Pro 6000 MIG 48GB 1.00/1.29, A100 PCIe 1.19/1.79, A100 SXM 1.39/1.79, RTX Pro 6000 1.69/2.49, H100 PCIe 1.99/2.89, H100 NVL 2.59/3.19, H100 SXM 2.69/3.99, H200 3.59/5.29, B200 5.98/7.99, B300 6.94/8.99. The page carries a per-hour and a per-second toggle, and the B300 and H200 pairs match the 2026-10-22 read
  - [1] 2026-11-25: the page's own product data names the cheapest on-demand card and its two hourly prices | capture: sha256:8dea0f2cfe3279c8e9031f007a5da0e72737525e07a2d40d60bbb95a159158b8 | quote: On-demand RTX A5000 cloud GPU rental on Runpod. Community Cloud $0.16/hr, Secure Cloud $0.27/hr.
  - [2] 2026-11-24: the provider states no charge for data transfer | capture: sha256:7b0684c33d0166d100b07d8b479a06ada3d0a84aec47c0a990ee9fadd97925d2 | quote: All compute and storage charges are billed per second, with no fees for data transfer.
  - [3] 2026-11-24: signup offers Google, GitHub or email and password and does not ask for a card | capture: sha256:27a995795fad949778caffad0367fe17e4466d7732fafa6f899ae7c89547083e | quote: Sign up with Google
  - [1] 2026-11-24: the cheapest published card is USD 0.16/hr on Community Cloud | capture: sha256:8dea0f2cfe3279c8e9031f007a5da0e72737525e07a2d40d60bbb95a159158b8 | quote: On-demand RTX A5000 cloud GPU rental on Runpod. Community Cloud $0.16/hr, Secure Cloud $0.27/hr.
  - [1] 2026-11-24: clusters scale to 64 GPUs | capture: sha256:8dea0f2cfe3279c8e9031f007a5da0e72737525e07a2d40d60bbb95a159158b8 | quote: Launch multi-GPU clusters in minutes with no commitments. Scale up to 64 GPUs, attach shared storage, and pay only for what you use.
  - [1] 2026-11-24: the B300 Community and Secure hourly rates | capture: sha256:8dea0f2cfe3279c8e9031f007a5da0e72737525e07a2d40d60bbb95a159158b8 | quote: On-demand B300 cloud GPU rental on Runpod. Community Cloud $6.94/hr, Secure Cloud $8.99/hr.
  - [1] 2026-11-24: storage starts at USD 0.05 per GB per month | capture: sha256:8dea0f2cfe3279c8e9031f007a5da0e72737525e07a2d40d60bbb95a159158b8 | quote: Flexible and persistent storage options starting at $0.05/GB/mo with standard and high-performance tiers.
  - [1] 2026-11-24: the page states per-second billing with no commitment | capture: sha256:8dea0f2cfe3279c8e9031f007a5da0e72737525e07a2d40d60bbb95a159158b8 | quote: Runpod rents the H100 PCIe at $2.89/hr on Secure Cloud, or from $1.99/hr on Community Cloud, billed per second with no commitment.
  - [2] 2026-11-24: a Pod needs at least one hour of credits in the balance | capture: sha256:7b0684c33d0166d100b07d8b479a06ada3d0a84aec47c0a990ee9fadd97925d2 | quote: To deploy a new Pod, your account must have at least one hour's worth of credits for your selected configuration. If your balance is insufficient, you can deposit additional funds or select a lower-cost GPU.
  - [4] 2026-11-24: account creation at console.runpod.io/signup | capture: sha256:5cb6417953d5ec573e46e9cf9e31e5d4a58b3f6be9de12658a826329917e366d | quote: Sign up for a Runpod account at [console.runpod.io/signup](https://www.console.runpod.io/signup).
- sources:
  - [1] https://www.runpod.io/pricing
  - [2] https://docs.runpod.io/accounts-billing/billing
  - [3] https://console.runpod.io/signup
  - [4] https://docs.runpod.io/accounts-billing/manage-accounts

## runpod network volumes

- `storage/runpod-network-volumes` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:39.272Z (live) | stale on 2026-12-04
- url https://docs.runpod.io/storage/network-volumes
- free tier: Network volumes are paid storage with no free allowance: standard storage is $0.07/GB/month for the first 1 TB and $0.05/GB/month beyond 1 TB; high-performance storage is $0.14/GB/month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: When your account balance reaches $0, Pods with an attached network volume are stopped and storage charges continue to accrue; if the charges cannot be covered the volume may eventually be terminated and its data cannot be recovered. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its…
  - [2] 2026-10-21: cited as the basis of the rejection: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its vo
  - [1] 2026-11-19: standard network-volume storage is priced at $0.07/GB/month for the first 1 TB and $0.05/GB/month beyond | capture: sha256:0f95f2edfbc36e78bf4d8e288f65dc6b68edaed5fba11e2b62b010b9df9144cb | quote: * First 1 TB: \$0.07/GB/month * Beyond 1 TB: \$0.05/GB/month
  - [1] 2026-11-19: a zero balance stops Pods while storage charges keep accruing | capture: sha256:0f95f2edfbc36e78bf4d8e288f65dc6b68edaed5fba11e2b62b010b9df9144cb | quote: When your account balance reaches \$0, Pods with an attached network volume are stopped and your data is preserved on the volume.
- sources:
  - [1] https://docs.runpod.io/storage/network-volumes
  - [2] https://www.runpod.io/pricing
