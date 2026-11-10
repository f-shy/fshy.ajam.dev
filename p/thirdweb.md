# thirdweb Storage

> thirdweb.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thirdweb/ | JSON https://fshy.ajam.dev/api/v1/entity/thirdweb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## thirdweb Storage

- `storage/thirdweb-storage` | fails-quota | evidence reported | binding none | category p2p
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://thirdweb.com/storage
- free tier: 1 GB included free; 1 GB–1 TB at $0.05/GB/month; 1–10 TB at $0.04; 10 TB+ at $0.03. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Bundled with storage; a 'Download Rate Limit' line exists in the pricing table but no free bandwidth allowance is published. Dedicated gateway bandwidth is priced separately on higher tiers. | metered: yes
- identity: card
- interface: s3-compatible, cli
- limits note: 1 GB free; per-GB-month above that.
- interface detail: s3
- tooling: S3-compatible API, TypeScript SDK (thirdweb), CLI.
- composes with: 1 GB free per project. Chaining projects multiplies 1 GB, not 500 GB.
- reliability: Purely a paid product with a 1 GB taste. No free-tier angle at all.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB included free; 1 GB–1 TB at $0.05/GB/month; 1–10 TB at $0.04; 10 TB+ at $0.03.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Storage: '1 GB Included', '1GB - 1TB $0.05 GB / month', '1TB - 10TB $0.04 GB / month'
  - [2] 2026-10-21: 'S3-compatible APIs'; IPFS pinning
- sources:
  - [1] https://thirdweb.com/pricing
  - [2] https://thirdweb.com/storage
