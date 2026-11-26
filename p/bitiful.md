# 缤纷云 Bitiful

> bitiful.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitiful/ | JSON https://fshy.ajam.dev/api/v1/entity/bitiful.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 缤纷云 Bitiful

- `netdisk-pan/bitiful` | fails-egress | evidence reported | binding per-ip-shaping | category object storage, S3-compatible
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T13:26:30.704Z (live) | stale on 2026-12-10
- url https://www.bitiful.com
- free tier: - 前 50 GiB 存储 | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [1]
- retention: Not published | source: [1]
- egress: 10 GB a month free, metered beyond. This is the disqualifier: 10 GB a month is 0.3 GB a day | metered: yes | free allowance: 10 GB per month | source: [2]
- identity: country-phone | detail: a Chinese-language signup | country: 86
- interface: s3
- limits:
  - per-ip-shaping (binding): 免费额度为每月每项10GB，但为防止滥用，目前限制每天用量不能超过5GB（当天超过5GB后会开始计费） [1]
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
  - [1] 2026-11-19: a current forum thread restates the Bitiful free 50GB storage and 10GB monthly traffic | capture: sha256:b7ddf1219e5f934c3d791a36654439bcbee3aa774f2d7a5308c9eb4852130e2a | quote: 我看 缤纷云 免费50GB，每个月免费10GB流量，挺不错的
  - [2] 2026-11-19: a forum answer still states the Bitiful free allowance supports private read-write only | capture: sha256:d85b04eaba7e2be89eb4d3fc278e37ca80a42146393c8a827541ead742a83f58 | quote: 缤纷云免费额度只支持私有读写
  - [3] 2026-11-25: the first-party documentation states this value | capture: sha256:348195c755b8cbfacf3f42a551c84116e06621bcdd38d8e71ff6518ebeaead31 | quote: - 前 50 GiB 存储
  - [4] 2026-11-25: the first-party documentation states this value | capture: sha256:10ec37ba48cc0cb1a883a6055a028383e2507b2df82ee553c3b4cac8ef4d383e | quote: 免费额度为每月每项10GB，但为防止滥用，目前限制每天用量不能超过5GB（当天超过5GB后会开始计费）
  - [3] 2026-11-25: the free storage allowance is 50 GiB | capture: sha256:348195c755b8cbfacf3f42a551c84116e06621bcdd38d8e71ff6518ebeaead31 | quote: - 前 50 GiB 存储
  - [4] 2026-11-25: the free traffic allowance is 10 GB per month per item with a 5 GB daily cap | capture: sha256:10ec37ba48cc0cb1a883a6055a028383e2507b2df82ee553c3b4cac8ef4d383e | quote: 免费额度为每月每项10GB，但为防止滥用，目前限制每天用量不能超过5GB（当天超过5GB后会开始计费）
- sources:
  - [1] https://linux.do/t/topic/1074108
  - [2] https://linux.do/t/topic/734000
  - [3] https://docs.bitiful.com/prices/basic
  - [4] https://docs.bitiful.com/prices/detail/transfer-prices.md
