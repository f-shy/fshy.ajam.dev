# Edge Network Storage

> edge.network | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/edge/ | JSON https://fshy.ajam.dev/api/v1/entity/edge.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Edge Network Storage

- `storage/edge-network-storage` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://edge.network/storage/pricing
- free tier: Free tier: '2 buckets / 5 GB storage / S3-compatible API / Zero egress fees'. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 5 GB cap | bytes: 5000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Egress / downloads $0 — Free at every scale.' 'API requests $0 — No per-request charges.'. | metered: yes
- identity: institution
- interface: s3-compatible
- limits:
  - per-object-cap (binding): 5 GB cap [1]
- limits note: Per-object-cap: not stated on the pricing page. quota-cap: 5 GB total; without a card 'hitting the 5 GB cap blocks writes rather than starting a bill — your existing objects stay readable', which is unusually clean behaviour. retention: none stated.
- interface detail: s3
- tooling: Full S3-compatible API 'with presigned URLs, multipart uploads, and access keys included'. Any S3 SDK.
- composes with: 5 GB x unlimited buckets across accounts; 2 buckets per free account. Zero-egress + zero-request-cost makes it a free CDN origin, not a bulk store.
- reliability: Free tier is explicitly hard-capped and does not start billing, so it degrades to read-only rather than into charges. The opposite of most free tiers.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free tier: '2 buckets / 5 GB storage / S3-compatible API / Zero egress fees'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free tier: 2 buckets, 5 GB on NVMe, full S3-compatible API', 'Zero egress fees', 'Egress / downloads $0'
- sources:
  - [1] https://edge.network/storage/pricing
