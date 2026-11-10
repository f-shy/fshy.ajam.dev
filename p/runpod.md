# runpod network

> runpod.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runpod/ | JSON https://fshy.ajam.dev/api/v1/entity/runpod.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RunPod

- `compute/runpod` | paid-only | evidence documented | binding request-rate | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.runpod.io/pricing
- price parsed USD 116.8/mo
- free tier: no free GPU tier is published; the on-demand card list runs from an RTX A5000 at USD 0.16 an hour on Community Cloud to a B300 at USD 8.99 on Secure Cloud, across 21 cards | unit: none | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: Community Cloud is cheaper than Secure Cloud for the same card; the page carries a per-hour and a per-second toggle, and 21 on-demand cards were read on 2026-10-24
- per-object cap: not applicable
- retention: network storage is billed while it exists; a pod keeps its volume only while attached or persisted | days: 0
- egress: not published as a per-GB line on the page read | metered: no | source: [1]
- identity: card | detail: a card is required to launch a pod
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
  - [1] 2026-10-22: network storage starts at USD 0.05 per GB a month
  - [1] 2026-10-24: the full on-demand card list, Community and Secure, quoted from the page's own rate data: RTX A5000 0.16/0.27, RTX 3090 0.22/0.50, RTX A6000 0.33/0.59, RTX 4090 0.34/0.89, A40 0.35/0.59, L4 0.44/0.59, Pro 6000 MIG 24GB 0.50/0.69, L40 0.69/0.82, RTX 5090 0.69/1.19, RTX 6000 Ada 0.74/0.99, L40S 0.79/1.09, Pro 6000 MIG 48GB 1.00/1.29, A100 PCIe 1.19/1.79, A100 SXM 1.39/1.79, RTX Pro 6000 1.69/2.49, H100 PCIe 1.99/2.89, H100 NVL 2.59/3.19, H100 SXM 2.69/3.99, H200 3.59/5.29, B200 5.98/7.99, B300 6.94/8.99. The page carries a per-hour and a per-second toggle, and the B300 and H200 pairs match the 2026-10-22 read
- sources:
  - [1] https://www.runpod.io/pricing

## runpod network volumes

- `storage/runpod-network-volumes` | paid-only | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.runpod.io/storage/network-volumes
- free tier: none reachable: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its…
  - [2] 2026-10-21: cited as the basis of the rejection: Correct architecture, wrong economics: network volumes are $0.07/GB/mo for the first 1 TB ($0.05 beyond), i.e. ~$72/TB/mo, and there is no free allowance. An account at $0 balance has its vo
- sources:
  - [1] https://docs.runpod.io/storage/network-volumes
  - [2] https://www.runpod.io/pricing
