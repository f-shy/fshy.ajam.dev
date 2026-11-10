# 缤纷云 Bitiful

> bitiful.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitiful/ | JSON https://fshy.ajam.dev/api/v1/entity/bitiful.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 缤纷云 Bitiful

- `netdisk-pan/bitiful` | fails-egress | evidence reported | binding per-ip-shaping | category object storage, S3-compatible
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.bitiful.com
- free tier: 50 GB of storage and 10 GB of egress a month, free | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [1]
- retention: Not published | source: [1]
- egress: 10 GB a month free, metered beyond. This is the disqualifier: 10 GB a month is 0.3 GB a day | metered: yes | free allowance: 10 GB per month | source: [2]
- identity: country-phone | detail: a Chinese-language signup | country: 86
- interface: s3
- limits:
  - per-ip-shaping (binding): 10 GB of egress a month on the free tier [1]
  - write-gated: a public bucket requires a CNY 10 top-up: '免费其实要先充10块进去' [1]
- binding note: 10 GB a month is 0.3 GB a day, which is. The storage is irrelevant at that egress allowance.
- tooling: S3-compatible, so rclone s3 and any S3 SDK apply. The forum pairs it with R2 behind a DNS split
- composes with: 50 GB per account and public buckets require a top-up ('设置为公开桶必须要充值'), so the free tier is private-read-write only, which blocks the CDN-front requirement as well as the volume
- reliability: A small domestic vendor with six or more years of forum awareness and no shutdown reports. Private-only buckets plus metered egress make it unusable for serving regardless of the storage
- notes: An S3-compatible domestic storage provider offering an active free tier. Outbound transfer is strictly constrained by the 10 GB monthly egress ceiling.
- extras:
  - access_mode: registration-gated
  - public_bucket_requires_topup: yes
- evidence:
  - [1] 2026-10-21: '缤纷云 免费50GB，每个月免费10GB流量，不过说是免费其实要先充10块进去'
  - [2] 2026-10-21: '缤纷云免费额度只支持私有读写'
- sources:
  - [1] https://linux.do/t/topic/1074108
  - [2] https://linux.do/t/topic/734000
