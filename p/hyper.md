# HyperAI

> hyper.ai | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hyper/ | JSON https://fshy.ajam.dev/api/v1/entity/hyper.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HyperAI

- `compute/hyperai` | paid-only | evidence documented | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://hyper.ai/en/docs/membership
- free tier: A membership whose monthly fee buys a fixed block of GPU hours, which is the cheapest denominator found anywhere among evaluated providers. Quoted: HyperAI Pro at USD 4.99 per month includes 30 GPU hours per month usable on a single RTX 5090, so a fully used month is USD 0.1663 per 32 GB GPU-hour, with no carry-over: 'Any remaining quota will be cleared at the beginning of the following month'. On-demand rates on the same site: RTX 5090 32GB USD 0.35/hr, RTX PRO 6000 96GB USD 0.80/hr, H100 PCIe 80GB USD 1.80/hr. Basic is quoted at USD 0.00 to get started with 20 GB of storage and a free CPU container of 2 vCPU and 4 GB RAM. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits note: no binding constraint identified
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: no open question recorded
- evidence:
  - [1] 2026-10-22: quoted benefits table: HyperAI Pro at US$4.99/Month gives 'Receive 30 GPU hours per month (supports Single RTX 5090)'; Basic gets 'No free quota; Pay As You Go'
  - [1] 2026-10-22: quoted: 'Any remaining quota will be cleared at the beginning of the following month, cannot be carried over, and cannot be transferred to other accounts'; and 'GPU resources are not reserved or dedicated to individual members. If the cluster is at full capacity, you will need to wait'
  - [2] 2026-10-22: quoted GPU rates: GeForce RTX 5090 32GB USD 0.35/h, RTX PRO 6000 96GB USD 0.80/h, H100 80GB USD 1.80/h; Basic membership USD 0.00; a Free Laboratory with 2 vCPU and 4 GB RAM
  - [3] 2026-10-22: quoted: 'Each user will receive 20GB of free storage space after registration'; and 'For projects that have been inactive for one full calendar month ... HyperAI will permanently delete them'
  - [4] 2026-10-22: independent tracker checked 2026-10-22 names HyperAI as the cheapest on-demand H100 at USD 1.80/hr across 38 providers and the cheapest RTX PRO 6000 at USD 0.80/hr
- sources:
  - [1] https://hyper.ai/en/docs/membership
  - [2] https://hyper.ai/en/en/pricing
  - [3] https://hyper.ai/en/docs/getting-started/quota-and-usage
  - [4] https://gpurentalprices.com/

## HyperAI (hyper.ai) — free CPU workspace + storage

- `storage/hyperai-free-cpu-workspace-storage` | fails-quota | evidence reported | binding none | category iaas
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://hyper.ai
- free tier: Free tier storage is 'Free 20 GB + Extra 50 GB, totaling 70 GB'. But the 70 GB is explicitly a Pro benefit ('Upgrade to HyperAI Pro, Unlock More Benefits .. 3.5× more storage: Free 20 GB + Extra 50 GB, totaling 70 GB'). So free is 20 GB, and 70 GB costs $4.99/month. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered on the free tier; storage tiers are the paid dimension (a discounted tier table exists for scalable storage). | metered: yes
- identity: email | detail: email.
- interface: s3, rest, cli
- limits note: 20 GB free, 2 vCPU / 4 GB RAM, 2 h max continuous CPU runtime (8 h on Pro), 30 h/month compute on Pro. Storage is workspace-scoped, not bucket-scoped.
- interface detail: rest
- tooling: Web console + app.hyper.ai notebooks; no documented S3/CLI blob API found. Storage is attached to notebooks rather than exposed as a bucket.
- composes with: 20 GB per account is too small to multiply usefully; 500 accounts per 10 TiB.
- reliability: Small aggregator-style GPU marketplace; the storage is a notebook side-car, so data tied to a workspace that may be reclaimed.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free tier storage is 'Free 20 GB + Extra 50 GB, totaling 70 GB' — but the 70 GB is explicitly a Pro benefit ('Upgrade to HyperAI Pro, Unlock More Benefits ... 3.5× more storage: Free 20 GB + Extra 50 GB, totaling 70 GB'). So free is 20 GB, and 70 GB costs $4.99/month.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: 'Run experiments and light workloads on our Free CPU—2 vCPU · 4 GB RAM'; Pro block: '3.5× more storage — Free 20 GB + Extra 50 GB, totaling 70 GB'
- sources:
  - [1] https://hyper.ai/pricing
