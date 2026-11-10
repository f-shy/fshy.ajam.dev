# Weights & Biases

> wandb.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wandb/ | JSON https://fshy.ajam.dev/api/v1/entity/wandb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Weights & Biases / CoreWeave Forge (academic free tier)

- `storage/weights-biases-coreweave-forge` | fails-quota | evidence reported | binding none | category ml-hub
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://wandb.ai/site/pricing
- free tier: Free plan: 5 GB/month of storage. Pro: 100 GB/month. 'Free forever for academic research' tier: 200 GB of cloud storage, unlimited tracked hours, up to 25 GB/month Weave ingestion, up to 100 seats. Requires an active academic email address. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered separately for artifact reads; storage is billed as a rolling 30-day consumption average in GB-days, so churn does not help you. | metered: yes
- identity: institution
- interface: s3, rest
- limits note: 5 GB on the ordinary free tier is the number that bites; academic tier requires a .edu-affiliated active email; the 30-day rolling average means a short burst still costs you; artifact TTL features exist but do not raise the cap.
- interface detail: rest
- tooling: Wandb Python SDK, `wandb artifact` API, artifacts pull via `wandb artifact get`; W&B also accepts 'reference artifacts' pointing at an external bucket (S3/GCS) which do NOT count against quota. That is the real trick here.
- composes with: 200 GB per academic account x up to 100 seats in one academic org = 20 TB of quota, but the seats clause is about people, not storage pools. Storage is per-entity and would need to be checked. The clean multiplier is reference artifacts: unlimited pointers to external storage at zero quota cost (useful as an index layer over Kaggle/Modal bytes, not as storage itself).
- reliability: Migrated from wandb.ai branding to CoreWeave Forge (the pricing page 301s to coreweave.com/forge-pricing). Product continuity is fine, but as an academic user you are now depending on a GPU-cloud vendor's free tier.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free plan: 5 GB/month of storage. Pro: 100 GB/month. 'Free forever for academic research' tier: 200 GB of cloud storage, unlimited tracked hours, up to 25 GB/month Weave ingestion, up to 100 seats — requires an active academic email address.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: > https://coreweave.com/forge-pricing — plan table: 'Storage Free 5 GB/mo, Pro 100 GB/mo, Additional storage $0.03/GB'
  - [2] 2026-10-21: 'Free forever for academic research ... 200GB free cloud storage ... up to 25 GB per month of Weave data ingestion, and up to 100 seats. An active academic email address is required.'
  - [2] 2026-10-21: 'Does tracked data stored on an external server count against my storage quota? No. ... Reference artifacts and data stored in an external storage bucket will not count.'
- sources:
  - [1] https://wandb.ai/site/pricing
  - [2] https://coreweave.com/forge-pricing
