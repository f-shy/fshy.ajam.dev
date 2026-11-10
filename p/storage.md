# storage.to

> storage.to | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/storage/ | JSON https://fshy.ajam.dev/api/v1/entity/storage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## storage.to

- `storage/storage-to` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://storage.to
- free tier: No permanent free storage: anonymous 100 GB upload / 24h per visitor token (500 GB / 24h per IP), free-account token = unlimited upload bandwidth and no daily file cap, but every free file expires in 3-7 days; permanent storage starts at $5/mo for 100 GB | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 25 GB/file | bytes: 25000000000 | source: [1] | note: not stated
- retention: No permanent free storage: anonymous 100 GB upload / 24h per visitor token (500 GB / 24h per IP), free-account token = unlimited upload bandwidth and no daily file cap, but every free file expires in 3-7 days; permanent storage starts at $5/mo for 100 GB | days: 7 | source: [1] | note: not stated
- egress: Downloads 'unlimited and unthrottled'. This is the most generous free egress found in the niche, it just cannot hold data. | metered: no
- identity: card
- interface: rest, rclone, cli
- limits:
  - per-ip-shaping: 500 GB / 24h [1]
  - per-ip-shaping: 100 GB/24h [1]
  - per-object-cap (binding): 25 GB/file [1]
  - retention-clamped: expires in 3-7 days [1]
- limits note: 25 GB/file (100 GB paid); 100 GB/24h per visitor token, 500 GB/24h per IP; 50 files/24h anonymous; expiry 3 days default, 7 max; 60-500 req/min per endpoint
- interface detail: rest
- tooling: documented 33-endpoint REST API (init -> presigned PUT -> confirm), presigned URLs point at r2.cloudflarestorage.com; CLI + desktop app + ShareX; no rclone
- composes with: The upload quota is per visitor token AND per IP, so 100 GB/24h x N tokens (up to the 500 GB/IP ceiling) x N IPs. A throughput engine rather than a store; pairs well as the write side in front of a permanent store.
- reliability: objects live on Cloudflare R2 behind presigned URLs and are garbage-collected at expiry; anonymous files need the returned owner_token to mutate anything and it cannot be recovered
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: No permanent free storage: anonymous 100 GB upload / 24h per visitor token (500 GB / 24h per IP), free-account token = unlimited upload bandwidth and no daily file cap, but every free file expires in 3-7 days; permanent storage starts at $5/mo for 100 GB
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'No token: 100 GB / 24 hours (500 GB per IP), files expire after 3 days'; 'Free account token: Unlimited upload bandwidth, no daily file cap'; 'downloads are unlimited and unthrottled'
  - [2] 2026-10-21: permanence is paid: Personal $5/mo 100 GB, 'Files never expire'
  - [3] 2026-10-21: probe: POST /api/upload/init -> 200 presigned URL at 7291236a05b5feaef8f8a13dc7957e8b.r2.cloudflarestorage.com; PUT -> 200; POST /api/upload/confirm -> 200 {"file":{"url":"","expires_at":"2026-10-24T14:49:29+00:00"}} (3-day expiry confirmed live)
- sources:
  - [1] https://storage.to/docs/api
  - [2] https://storage.to/premium
  - [3] https://storage.to/b9PYWolbj
