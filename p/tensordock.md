# TensorDock floor

> tensordock.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tensordock/ | JSON https://fshy.ajam.dev/api/v1/entity/tensordock.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TensorDock

- `compute/tensordock` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:35.127Z (live) | stale on 2026-12-04
- url https://www.tensordock.com/
- free tier: no free tier: homepage 'From' rates per hour on a marketplace of independent hosts where the same GPU has multiple prices: H100 SXM5 $2.25, A100 SXM4 $1.80 (memory size not stated), RTX 4090 $0.35, consumer GPUs from $0.12. L40S and L4 are not named on the homepage, and the 45-model catalogue is behind a login. A $5 minimum is needed to start, root access is included, and the deploy page states 'Billed per second, no minimum' | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no ingress or egress fees | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): from $0.12 an hour for a consumer GPU to $2.25 for an H100 SXM5 [1]
  - write-gated: a $5 minimum balance is needed to launch a server [1]
  - per-object-cap: 45 GPU models are offered, with root access and dedicated cards [1]
- limits note: Session cap, idle-reap and network policy are not documented. GPU only.
- interface detail: Access interface not documented in published terms.
- tooling: part of the free tier
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the GPU ladder, the $5 starting point and root access. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - shape.gpu_class: RTX 4090 to HGX H100 SXM5
  - shape.gpu_count: 1
  - shape.note: 45 GPU models, from consumer cards at $0.12 an hour to an HGX H100 SXM5 at $2.25
  - session_cap.restart_required: no
  - session_cap.note: a server launches in 30 seconds and bills while it exists; the page states no reap
  - free_tier_kind: none
  - ps.price: storage is part of the server
  - ps.durability: the server's own disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the server exists
  - net.out: yes
  - net.in: yes
  - net.ports: root access with full OS control
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'H100s from $2.25/hr. No quotas, no commitments.' with 'Start with just $5 and launch a server in 30 seconds', 'consumer GPUs from $0.12/hr', '45 available GPU models' and 'Root access and dedicated GPUs', quoted
  - [1] 2026-11-03: the H100 SXM5 is from $2.25/hr | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: ### H100 SXM5 From $2.25/hr For builders needing training and inference with no compromises.
  - [1] 2026-11-03: the A100 SXM4 is from $1.80/hr | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: ### A100 SXM4 From $1.80/hr The best balance between price and performance for AI inference.
  - [1] 2026-11-03: the RTX 4090 is from $0.35/hr | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: ### RTX 4090 From $0.35/hr Truly unbeatable value for gaming, image processing, and rendering.
  - [1] 2026-11-03: prices are set by independent hosts, so one GPU has several prices | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: We're a marketplace of independent hosts who compete and set their own pricing.
  - [2] 2026-11-03: the deploy page cost estimate states per-second billing with no minimum | capture: sha256:402d3249d1020442d042617b26ff9ac13c218956a1b299e6bad141831799c2df | quote: Billed per second, no minimum • Monthly estimates based on 730 hours
  - [1] 2026-11-03: the GPU cloud has no ingress or egress fees | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: Our globally distributed GPU fleet. 99.99% uptime standard and no ingress/egress fees.
- sources:
  - [1] https://www.tensordock.com/
  - [2] https://dashboard.tensordock.com/deploy

## TensorDock floor

- `compute/tensordock-floor` | paid-only | evidence reported | binding none | category GPU cloud
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T08:50:36.649Z (live) | stale on 2026-11-18
- url https://www.tensordock.com/
- free tier: The vendor's home page lists three cards with a 'From' price, per hour: H100 SXM5 from $2.25, A100 SXM4 from $1.80 (no memory size named) and RTX 4090 from $0.35, and quotes 'consumer GPUs from $0.12/hr' across '45 available GPU models'. The tier is on demand on a marketplace of independent hosts that set their own prices, so each figure is a floor and not a fixed rate. The page lists no L40S, no L4 and no A100 80 GB price. Billing is pay as you go: a deposit is deducted continuously after a server is deployed, with a $5 start; no billing granularity and no minimum bill are stated beyond that. An independent tracker on the same day prices the cheapest TensorDock card at USD 0.10 an hour and an RTX 4090 at USD 0.35, the first of which is below the vendor's own published floor. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: Unchanged from the existing record: a USD 5 minimum balance is the entry charge.
- interface: unknown
- limits note: The binding constraint is the host's, not the platform's: prices are set by third-party hosts on a marketplace, so the card exists at the rate but the rate moves with supply.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A USD 0.10 16 GB hour is the smallest possible entry among documented hosts, and with a USD 5 minimum deposit it buys 50 card-hours, which is a complete small fine-tune for the smallest possible outlay.
- reliability: no reliability event recorded
- notes: Corrects the existing tensordock.json record, which says only 'GPU servers from USD 0.12 an hour for a consumer card'. The honest statement is that the floor is between USD 0.10 and USD 0.12. The vendor page also claims 45 models, which is more than any other single host.
- extras:
  - facets.class: gpu-marketplace
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX A4000
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 16
- evidence:
  - [1] 2026-10-22: quoted: 'consumer GPUs from $0.12/hr'; 'H100s from $2.25/hr. No quotas, no commitments'; '45 available GPU models'; 'Start with just $5'
  - [2] 2026-10-22: quoted: RTX A4000 on-demand from USD 0.10 at TensorDock across 3 providers, below the vendor's own USD 0.12 claim
  - [3] 2026-10-22: the tracker reads TensorDock as the on-demand floor for RTX 4090 at USD 0.35, RTX 3090 at USD 0.20, V100 at USD 0.17 and RTX 6000 Ada at USD 0.75
  - [1] 2026-11-03: the home page lists an H100 SXM5 from USD 2.25 an hour | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: H100 SXM5 From $2.25/hr
  - [1] 2026-11-03: the home page lists an A100 SXM4 from USD 1.80 an hour, with no memory size named | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: A100 SXM4 From $1.80/hr
  - [1] 2026-11-03: the home page lists an RTX 4090 from USD 0.35 an hour | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: RTX 4090 From $0.35/hr
  - [1] 2026-11-03: billing is a prepaid deposit deducted continuously after deployment | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: We operate on a pay as you go model. Users deposit funds, and we deduct balance continuously after a server is deployed.
  - [1] 2026-11-03: the page states a USD 5 start | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: Start with just $5 and launch a server in 30 seconds.
  - [1] 2026-11-03: the 'From' prices are marketplace floors set by independent hosts, so the tier is on demand at a host-set rate | capture: sha256:6703c0ffa0c7fa03c053e943360aef622a3da803837ef92b4c8876e309721fef | quote: We're a marketplace of independent hosts who compete and set their own pricing.
- sources:
  - [1] https://www.tensordock.com/
  - [2] https://gpurentalprices.com/rtx-a4000
  - [3] https://gpurentalprices.com/providers/tensordock
