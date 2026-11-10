# OpenBayes

> openbayes.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openbayes/ | JSON https://fshy.ajam.dev/api/v1/entity/openbayes.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenBayes (openbayes.com) — Chinese GPU cloud with per-tier workspace storage

- `storage/openbayes-chinese-gpu-cloud-with-per-tier-workspace-stor` | fails-quota | evidence reported | binding per-object-cap | category iaas
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://openbayes.com
- free tier: Free/entry tier attaches 50 GB of workspace storage; the upper tiers attach 200 GB. Additional storage is priced at 0.5 CNY/GB/month. I.e. storage is a metered dimension above the included amount, not a free pool. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap published | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not separately metered; the storage line (0.5 CNY/GB/mo) is the paid dimension. | metered: yes
- identity: email | detail: email + +86 phone (Chinese GPU cloud; prior rounds found real-name/phone gates on this class).
- interface: s3-compatible, rest, cli
- limits:
  - per-object-cap (binding): No per-file cap published [1]
- limits note: 50 GB workspace on the entry tier, 200 GB on higher tiers, then 0.5 CNY/GB/mo. GPU SKUs 32 GB-640 GB VRAM. No per-file cap published.
- interface detail: rest
- tooling: Web console + CLI (openbayes CLI) + Jupyter workspaces. Datasets are mounted into containers at a fixed path. No S3 API.
- composes with: 50 GB per account on the entry tier; 200 GB on the higher tier which is a paid plan. 10 TiB would require 205 free accounts.
- reliability: Data lives in a workspace tied to a compute product; over-quota is billed rather than refused, so it can silently cost money.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free/entry tier attaches 50 GB of workspace storage; the upper tiers attach 200 GB. Additional storage is priced at 0.5 CNY/GB/month — i.e. storage is a metered dimension above the included amount, not a free pool.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live: '50 GB 工作空间' on the entry tier and '200 GB 工作空间' on a higher tier; '额外存储空间：0.5 元/GB/月起'
- sources:
  - [1] https://openbayes.com/pricing
