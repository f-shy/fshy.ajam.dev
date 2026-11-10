# VoltageGPU

> voltagegpu.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/voltagegpu/ | JSON https://fshy.ajam.dev/api/v1/entity/voltagegpu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VoltageGPU

- `compute/voltagegpu` | paid-only | evidence documented | binding none | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:36:22.537Z (live) | stale on 2026-12-04
- url https://voltagegpu.com/
- free tier: No free tier. Prepaid per-second GPU rental in two tiers. Standard tier (no enclave): from USD 0.32 per GPU-hour; floors of USD 0.70 for the A100 80 GB and USD 0.61 for the RTX 4090 on the vendor page, and the index lists the H100 SXM at USD 3.60, the L40S at USD 0.76 and the RTX 4090 at USD 0.70. Confidential VM tier (Intel TDX): H100 USD 6.95, H200 USD 8.08, RTX PRO 6000 Blackwell USD 3.80 per GPU-hour. The index lists no L4. The only allowance is one RTX PRO 6000 hour (USD 3.80) added to a first top-up of USD 10 or more. | unit: none | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: none
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the machine shape
- retention: not applicable | source: [1]
- egress: not published on the pages read | metered: no | source: [1]
- identity: email | detail: unverified: the signup page answered with a login wall. The terms require 'accurate, complete, and current information during registration', and billable use needs a prepaid balance of at least USD 5 paid by card (Stripe), cryptocurrency (Coinbase Commerce) or Bitcoin, so a card is optional. A phone or ID requirement is not stated on the pages read.
- interface: rest, cli, ssh
- limits note: No quota is stated: the wall is the prepaid balance and the per-GPU-hour rate. Capacity is first come, first served and the standard tier is a distributed host network with no enclave.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: REST API at /api/volt/pods with an X-API-Key header, the voltagegpu CLI (pip install voltagegpu-cli) and SSH with root into each machine; templates for PyTorch, Jupyter and Ollama.
- composes with: Per-second billing with a USD 5 minimum top-up makes short GPU runs cheap to start: an L40S at USD 0.76 or a 4090 at USD 0.61 to USD 0.70 an hour. Capacity is first come, first served, with no reservations.
- reliability: The index records 'Prepaid only, no invoicing on credit' and 'No reservations: capacity is first come, first served'; on 8x H100 confidential nodes the NVSwitch fabric is not attested. No outage was observed.
- notes: Found via computeprices (listed there as VoltageGPU). The entity is VOLTAGE EI, France. The index prices the H100 at USD 3.60 on the standard tier, and the vendor page shows USD 6.95 for the confidential tier; the vendor page lists no standard-tier H100 row. A100 and L4 are not on the index page; the A100 80 GB floor is the vendor's.
- evidence:
  - [2] 2026-11-03: the index lists the standard-tier H100 SXM 80 GB at USD 3.60 per GPU-hour, read 2026-11-03 | capture: sha256:a01fb51612a148b42ba5d7f8f819064e60856d9d35f418ea249c1ad1d2109fd2 | quote: | [H100 SXM](https://computeprices.com/providers/voltagegpu/gpus/h100)1× · standard | $3.60/hr |
  - [2] 2026-11-03: the index lists the standard-tier L40S 48 GB at USD 0.76 per GPU-hour | capture: sha256:a01fb51612a148b42ba5d7f8f819064e60856d9d35f418ea249c1ad1d2109fd2 | quote: | [L40S](https://computeprices.com/providers/voltagegpu/gpus/l40s)1× · standard | $0.76/hr |
  - [2] 2026-11-03: the index lists the standard-tier RTX 4090 at USD 0.70 per GPU-hour; the index lists no A100 and no L4 for this provider | capture: sha256:a01fb51612a148b42ba5d7f8f819064e60856d9d35f418ea249c1ad1d2109fd2 | quote: | [RTX 4090](https://computeprices.com/providers/voltagegpu/gpus/rtx4090)1× · standard | $0.70/hr |
  - [3] 2026-11-03: first-party standard-tier floor for the A100 80 GB | capture: sha256:1c7282286f3138004da5a74a0a5624ef7963ef105dc74b09e29a645853263857 | quote: NVIDIA A100 (80 GB), standard tier: from $0.70 per GPU-hour.
  - [3] 2026-11-03: first-party standard-tier floor for the RTX 4090, below the index's USD 0.70 | capture: sha256:1c7282286f3138004da5a74a0a5624ef7963ef105dc74b09e29a645853263857 | quote: NVIDIA RTX 4090 (24 GB), standard tier: from $0.61 per GPU-hour.
  - [1] 2026-11-03: first-party confidential-VM (Intel TDX) rates for the H100 at USD 6.95 and the H200 at USD 8.08 per GPU-hour | capture: sha256:4c96650feb8c303c1d200c444e62af851df2dc77907e6c2cafa403725c5dccf2 | quote: RTX PRO 6000 Blackwell $3.80/hour, H100 $6.95/hour, single-GPU H200 $8.08/hour
  - [1] 2026-11-03: signup is free; a machine needs a prepaid balance; the only free allowance is one RTX PRO 6000 hour on a first top-up of USD 10 or more | capture: sha256:4c96650feb8c303c1d200c444e62af851df2dc77907e6c2cafa403725c5dccf2 | quote: Signing up is free. Using a machine needs a prepaid balance, and your first top-up of $10 or more adds $3.80 automatically, one hour on the RTX PRO 6000 Blackwell Confidential VM, once per account.
  - [1] 2026-11-03: the smallest prepaid top-up is USD 5 | capture: sha256:4c96650feb8c303c1d200c444e62af851df2dc77907e6c2cafa403725c5dccf2 | quote: Minimum top-up is $5.
  - [4] 2026-11-03: the prepaid balance can be funded by card, cryptocurrency or Bitcoin, so a card is not the only route | capture: sha256:4b39c3675f98cd3ddae3c42e907268578e64c7f817dadd3dcac0caccc6621212 | quote: 5.3. Payment methods. We accept credit/debit cards (via Stripe), cryptocurrency (via Coinbase Commerce), and Bitcoin (direct P2P).
  - [4] 2026-11-03: registration collects account details; the terms do not name the fields | capture: sha256:4b39c3675f98cd3ddae3c42e907268578e64c7f817dadd3dcac0caccc6621212 | quote: 3.1. You must provide accurate, complete, and current information during registration.
  - [4] 2026-11-03: billing is prepaid; pods stop when the balance reaches zero | capture: sha256:4b39c3675f98cd3ddae3c42e907268578e64c7f817dadd3dcac0caccc6621212 | quote: 5.1. Pre-paid credit system. You must maintain a positive account balance to use billable services. When your balance reaches zero, running GPU pods will be automatically stopped to prevent negative balances.
  - [2] 2026-11-03: no reservations; capacity is first come, first served | capture: sha256:a01fb51612a148b42ba5d7f8f819064e60856d9d35f418ea249c1ad1d2109fd2 | quote: - No reservations: capacity is first come, first served
- sources:
  - [1] https://voltagegpu.com/pricing
  - [2] https://computeprices.com/providers/voltagegpu
  - [3] https://voltagegpu.com/standard-gpus
  - [4] https://voltagegpu.com/terms
