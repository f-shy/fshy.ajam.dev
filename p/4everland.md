# 4EVERLAND

> 4everland.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/4everland/ | JSON https://fshy.ajam.dev/api/v1/entity/4everland.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 4EVERLAND (IPFS + S3-compatible Bucket)

- `storage/4everland` | fails-egress | evidence reported | binding per-ip-shaping | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://docs.4everland.org/get-started/billing-and-pricing/pricing-model.md
- free tier: Standard free package: 'IPFS Storage: 6 GB/month', 'Arweave Storage: Total 100 MB', 'Bandwidth: 10 GB/month', resets on the 1st. Separate 7-day Trial: 1 GB IPFS, 10 MB Arweave, 1 GB bandwidth. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: metered at 10 GB/month on the free Standard package, then $0.1/GB pay-as-you-go. Not free. | metered: yes | free allowance: 10 GB per month
- identity: card
- interface: s3-compatible
- limits:
  - per-ip-shaping (binding): 2 GB/day [1]
- limits note: per-object-cap: none stated. bandwidth-cap: 10 GB/month egress is the binding limit, and it is far below any useful serving volume. retention: storage is rented per second (ipfs_fee = X * unit_price * Time), so it decays with balance. Free package resets rather than accumulates.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: s3
- tooling: 'Bucket API - S3 Compatible .. fully compatible with the Amazon S3 Cloud Storage service'. AWS SDKs for Go/Java/JS/.NET/PHP/Python/Ruby all documented.
- composes with: 6 GB/month resets monthly, and the free package is 'Unconditional' for Standard but requires 'on-chain identity registration and account activation'. Unlimited accounts x 6 GB with monthly reset means chained accounts can hold a rolling 6 GB each, not accumulate.
- reliability: Egress allowance is 10 GB per month with paid overage at $0.1 per GB.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Standard free package: 'IPFS Storage: 6 GB/month', 'Arweave Storage: Total 100 MB', 'Bandwidth: 10 GB/month', resets on the 1st. Separate 7-day Trial: 1 GB IPFS, 10 MB Arweave, 1 GB bandwidth.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'IPFS Storage: 6 GB/month', 'Bandwidth: 10 GB/month', 'Bandwidth $0.1/GB'
  - [2] 2026-10-21: S3-compatible Bucket API
  - withheld 2026-10-21: probe: DNS for ipfs.4everland.io and <cid>.ipfs.4everland.io -> NXDOMAIN (gateway hostnames do not resolve from here)
- sources:
  - [1] https://docs.4everland.org/get-started/billing-and-pricing/pricing-model.md
  - [2] https://docs.4everland.org/storage/bucket/bucket-api-s3-compatible.md
