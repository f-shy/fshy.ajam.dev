# Load Network

> load.network | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/load/ | JSON https://fshy.ajam.dev/api/v1/entity/load.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Load Network — Load S3 (LS3)

- `storage/load-network-load-s3` | fails-quota | evidence reported | binding none | category S3-compatible onchain-backed object storage
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.load.network/cloud
- price $3.00 (0.003/GB/mo); permanent tier $11,900/TB one-time
- free tier: No free tier found. $0.003/GB/month (~$3/TB/month) with a permanent-storage alternative at $11.9/GB one-time. S3 1:1 compatible. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: $0.003/GB/month (~$3/TB/month) with a permanent-storage alternative at $11.9/GB one-time | source: [1] | note: not stated
- egress: Not stated on the pricing page. Unresolved, and it matters more than the storage price. | metered: no
- identity: email | detail: email
- interface: s3-compatible, cli
- limits note: No free allowance. $3/TB/month with an S3 API is at the same price floor as HostBrr.
- interface detail: S3-compatible; an HTTP agent at load-s3-agent.load.network with bearer-key auth; load-pools CLI for bulk dataset pushes (explicit HF and GitHub import).
- tooling: aws-cli / any S3 SDK; pip install load-pools.
- composes with: The pools CLI is designed for exactly the workload shape. Push an entire existing dataset tree into S3.
- reliability: Marketing describes the underlying network as 'fully ruggable' (their own words, in the comparison table). That is an honest durability warning for anything relying on the permanent tier.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: No free tier found. $0.003/GB/month (~$3/TB/month) with a permanent-storage alternative at $11.9/GB one-time. S3 1:1 compatible.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $3.00 (0.003/GB/mo); permanent tier $11,900/TB one-time
- evidence:
  - [1] 2026-10-21: '$0.003 gb/mo', '$11.9 gb permanent', 'S3 storage for 7.7x less than AWS', '1:1 compatible with the S3 interface'
  - [2] 2026-10-21: 'no longer required to directly contact us to acquire Load S3 access keys'
  - [3] 2026-10-21: 'pip install load-pools … push entire datasets to Load S3 with support for Hugging Face and GitHub'
- sources:
  - [1] https://www.load.network/cloud
  - [2] https://docs.load.network/load-cloud-platform-lcp/ls3-with-load_acc
  - [3] https://blog.load.network/pools-cli/
