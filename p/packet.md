# Packet AI

> packet.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/packet/ | JSON https://fshy.ajam.dev/api/v1/entity/packet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Packet AI

- `compute/packet-ai` | paid-only | evidence documented | binding write-gated | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:36:22.304Z (live) | stale on 2026-12-04
- url https://packet.ai/pricing
- free tier: no free GPU tier is published; the rate card read on 2026-11-03 shows A100 80GB at USD 0.89 an hour on the Dynamic plan and USD 1.43 on the Dedicated plan, L40S 48GB at USD 0.92 on the Dedicated plan, RTX 6000 Pro at USD 0.66 and B200 at USD 3.75 Dynamic and USD 6.99 Dedicated. The RTX 4090 row shows no on-demand price on the rate card; the comparison table lists 'RTX 4090' at USD 0.39 as the packet.ai starting rate. H100 SXM and H200 are labelled 'Coming soon'. No L4 is listed. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: Dynamic is a shared card with scheduler-enforced isolation; Dedicated is a whole card; hourly pods are billed in 30-minute periods from a prepaid wallet
- per-object cap: not applicable | source: [1] | note: pods are one or more cards
- retention: not applicable | source: [2] | note: a stopped pod keeps its GPU and disk and is billed at the full hourly rate; a terminated pod's disk is destroyed
- egress: not published on the pages read | metered: no | source: [1]
- identity: card | detail: Account creation is by GitHub, Google or email and the sign-up page says 'No credit card needed'; launching a pod needs a wallet top-up of USD 5 to USD 10,000 through Stripe Checkout, which saves the card for auto top-up. No phone or ID document is stated on the pages read.
- interface: rest, cli, ssh
- limits:
  - write-gated (binding): a launch needs a funded wallet: the minimum to launch is the first 30 minutes at the pod's hourly rate; Premium GPUs unlock after the first paid top-up and a voucher alone does not launch them [3]
- limits note: A pod launch is gated on a funded wallet (USD 5 to USD 10,000 per top-up by Stripe Checkout); there is no free allowance.
- binding note: the same as limits note
- interface detail: taken from the documentation index, which lists a REST API reference, a CLI and browser or SSH terminal access; not probed
- tooling: REST API with an API key, a CLI, SSH and a browser terminal, Jupyter and VS Code Server one-click apps, vLLM model serving, persistent storage volumes
- composes with: Hourly A100 80GB and L40S at USD 0.89 to USD 1.43 and USD 0.92 with SSH and an API, plus a token-billed serverless catalog drawing on the same wallet.
- reliability: The aggregator profile states B200s sold out and H200s coming soon; the provider is listed as newer with limited locations. The rate card's H100 SXM and H200 rows read 'Coming soon' on 2026-11-03.
- notes: Found via computeprices.com (provider slug packet-ai). The aggregator shows A100 SXM at USD 0.890, L40S at USD 0.920 and RTX 4090 at USD 0.390 in US East Virginia; the provider rate card places the A100 80GB in EU Frankfurt. Not read: the RTX 4090 on-demand rate and region.
- evidence:
  - [1] 2026-11-03: A100 80GB Dynamic plan rate is USD 0.89 an hour | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: NVIDIA A100 80GB 80GB HBM2eAmpere EU · Frankfurt [Dynamic$0.89/hr Deploy Dynamic]
  - [1] 2026-11-03: A100 80GB Dedicated plan rate is USD 1.43 an hour | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: [Dedicated$1.43/hr Deploy Dedicated]
  - [1] 2026-11-03: L40S Dedicated plan rate is USD 0.92 an hour | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: [Dedicated$0.92/hr Deploy Dedicated]
  - [1] 2026-11-03: the comparison table lists RTX 4090 with a packet.ai starting rate of USD 0.39 | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: RTX 4090 24 GB GDDR6X $0.39~30% avg $0.69 $0.35
  - [1] 2026-11-03: H100 SXM is labelled Coming soon | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: NVIDIA H100 SXM 80GB HBM3HopperComing soon
  - [2] 2026-11-03: wallet top-ups are USD 5 to USD 10,000 through Stripe Checkout | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: Pick a preset amount or type your own in Other $ — any amount from $5 to $10,000. Add funds opens Stripe Checkout
  - [3] 2026-11-03: a funded wallet is required before a pod launches | capture: sha256:7aa2178803f6d3792ff4cab93b9aa2c71c61f4acae2057a55a184bdcfe715e43 | quote: A funded wallet** — go to Billing → Payments → Add funds.
  - [4] 2026-11-03: the account page offers sign-up without a card | capture: sha256:cb51a4fdb37cc2b864b10d1feeb3718a2d4d424e07c40f675be82ca5f56b68eb | quote: Get started in 30 seconds. No credit card needed.
  - [5] 2026-11-03: listed on the computeprices index | capture: sha256:6c9afa1786a205645e396ca910152693444b509f5be6d2e824bd97018ebe7bb6 | quote: Packet AI is the cheapest provider for A100 SXM, RTX PR
  - [1] 2026-11-03: the L40S Dedicated rate of USD 0.92 an hour on the rate card | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: ### NVIDIA L40S 48GB GDDR6Ada Lovelace US East · Virginia [Dedicated$0.92/hr Deploy Dedicated]
  - [1] 2026-11-03: the A100 80GB Dedicated rate of USD 1.43 per GPU-hour and the Dynamic rate of USD 0.89 on the rate card | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: An NVIDIA A100 80 GB is $1.43/GPU-hr on packet.ai
  - [1] 2026-11-03: the A100 80GB Dynamic rate of USD 0.89 an hour | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: Dynamic$0.89/hr Deploy Dynamic
  - [1] 2026-11-03: the published card set: an H100 SXM and an H200 are not yet orderable, and no L4 is listed | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: Published today: RTX 4090, RTX 5090, RTX 6000 Pro, L40S, A100 80GB, and B200. H100 SXM and H200 are launching soon
  - [1] 2026-11-03: no ingress and no egress fee, with local NVMe storage included up to 2 TB per node | capture: sha256:4f8856aa3395c5d5a3d4c69cf38f5ef96c873abd555fb67095277d6816c0059a | quote: No platform fees, no ingress. No Egress (vs $0.09/GB on AWS). NVMe local storage included up to 2 TB per node.
  - [6] 2026-11-03: the RTX 4090 Dedicated starting rate of USD 0.39 per GPU-hour, the cheapest Dedicated card | capture: sha256:d75c04387461048a0e31d06830096e136ec0ef6032a7361f4c73d94615e35398 | quote: Dedicated starts at $0.39/GPU-hr (RTX 4090) up to $6.99/GPU-hr (B200).
  - [7] 2026-11-03: the Dynamic page marks the RTX 4090 as not yet orderable | capture: sha256:4fc8b5c50d25b5c82cee45162875189fcff386c48084d8cba64e062b2747d47b | quote: ### RTX 4090 24GB GDDR6XAda Lovelace Launching soon
  - [8] 2026-11-03: the home page lists an H100 at USD 2.50 an hour with a waitlist link rather than a deploy link | capture: sha256:c6b59e3a9c81c567af1618f3d93c75b5d0314015c6e51337df9480b411b0bbcd | quote: H100NVIDIA Hopper80GB HBM3 $2.50 [Join waitlist](https://packet.ai/gpu/h100)
  - [4] 2026-11-03: the account form says no credit card is needed to create the account and offers an email sign-up | capture: sha256:cb51a4fdb37cc2b864b10d1feeb3718a2d4d424e07c40f675be82ca5f56b68eb | quote: Get started in 30 seconds. No credit card needed.
  - [2] 2026-11-03: GPU pods bill from a prepaid wallet in 30-minute periods | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: GPU pods are paid for either from a prepaid wallet in 30-minute periods, or on a monthly commitment billed to your card.
  - [2] 2026-11-03: wallet top-ups run from USD 5 to USD 10,000 through Stripe Checkout | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: Pick a preset amount or type your own in Other $ — any amount from $5 to $10,000. Add funds opens Stripe Checkout
  - [2] 2026-11-03: the card used to top up is saved | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: the balance updates as soon as the payment completes and the card you use is saved for auto top-up.
  - [2] 2026-11-03: a launch is refused when the wallet cannot cover the first 30 minutes | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: If the balance can't cover it the launch is refused
  - [2] 2026-11-03: a stopped pod is billed at the full hourly rate | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: A stopped pod is billed at the full hourly rate
  - [2] 2026-11-03: premium GPUs unlock after the first paid top-up | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: Premium GPUs unlock after your first paid top-up.
  - [2] 2026-11-03: shared volumes of an account with a negative balance are scheduled for deletion after a 3-day grace period | capture: sha256:ee9b6a2921470c8581e7d16f89b3b1212b0924548735f665d95a885b49f7169c | quote: Schedules your shared volumes for deletion after a 3-day grace period
  - [3] 2026-11-03: pods authenticate with a password over SSH by default | capture: sha256:7aa2178803f6d3792ff4cab93b9aa2c71c61f4acae2057a55a184bdcfe715e43 | quote: Pods authenticate with a password out of the box.
  - [9] 2026-11-03: a REST API authorised with an API key | capture: sha256:745aa62533dcff6111c1a6181ee222c82c5ff29728969028dd2615bff19515a9 | quote: Authorize with an API key and try each endpoint from the page
  - [10] 2026-11-03: a price tracker lists the provider with 43 offers, RTX 4090 at USD 0.39 per GPU-hour and every offer shown Sold Out on that date | capture: sha256:1868f97ee710d6faffe86422ce8924e29bc97706bbbeabc72e9f66de39cc322c | quote: | Packet.aiPacket.ai | 2×NVIDIA GeForce RTX 409024GB VRAM | 24GB | 32 vCPU128GB RAM500GB Storage | Dallas, Texas | $0.39/GPU/hr$0.77/hr total (2×) | Sold Out | | |
- sources:
  - [1] https://packet.ai/pricing
  - [2] https://dash.packet.ai/docs/billing
  - [3] https://dash.packet.ai/docs/getting-started
  - [4] https://dash.packet.ai/account
  - [5] https://computeprices.com/providers/packet-ai
  - [6] https://packet.ai/dedicated-gpu-cloud
  - [7] https://packet.ai/dynamic-gpu-cloud
  - [8] https://packet.ai/
  - [9] https://dash.packet.ai/docs
  - [10] https://gpuperhour.com/providers/packetai
