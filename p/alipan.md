# Aliyun Drive

> alipan.com | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alipan/ | JSON https://fshy.ajam.dev/api/v1/entity/alipan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Aliyun Drive (阿里云盘, alipan)

- `netdisk-pan/aliyun-drive` | fails-quota | evidence reported | binding per-ip-shaping | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.alipan.com
- free tier: 100 GB free; paid tiers 100 GB, 200 GB, 2 TB and above | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [2]
- retention: Capacity grants are re-evaluated and expire; over-quota accounts are functional-restricted rather than deleted | source: [2]
- egress: No per-GB charge; free accounts are throttled to about 0.5 MB/s per the Wikipedia table | metered: yes | source: [1]
- identity: country-phone | detail: +86 only, and the open platform needs an application reviewed on top of that. The token-exchange tool still requires you to log into an Aliyun Drive account to mint the refresh token | country: 86
- interface: rest
- limits:
  - per-ip-shaping (binding): about 0.5 MB/s on a free account [1]
  - request-rate: 60-minute and 10-request refresh-token rate limit on the token broker [3]
  - write-gated: the open platform needs an application reviewed by Alibaba on top of an existing account [4]
- binding note: 100 GB free, and 0.5 MB/s is 43 GB a day at best, so the shaping binds before the identity gate is even reached. The identity gate is the second lock.
- tooling: an open platform at alipan.com/developer with OAuth and app review; the OpenList aliyundrive_open driver ships a built-in key pair so no app registration is needed; no official rclone backend
- composes with: 100 GB per phone-verified Alibaba account is 200 accounts per 20 TiB, which is a non-starter against the effort. The anonymous API surface exists and answers structured NotFound errors, which proves the routes resolve, but every share token needs a share that exists
- reliability: Over-quota accounts are restricted from playback, upload, download and transfer rather than deleted, so the bytes survive the quota change and the access does not. The docs warn 请勿将阿里云盘进行公开分享，禁止帐号被多IP访问, which is the exact pattern a bridge uses
- notes: Historical quota trajectory reflects repeated downward adjustments: an initial display bug in 2022 showing 100 GB across accounts was followed in 2024 by restriction of over-capacity storage, leading into the current paid tier ladder.
- extras:
  - access_mode: registration-gated
  - anonymous_read: routes resolve, shares refused
  - free_capacity_changes: 2022 bug showed 100 GB on every account; 2024 over-capacity accounts restricted
- evidence:
  - [1] 2026-10-21: table row '阿里云盘, 100G, 无, 有, 0.5M/s, 是, 是'
  - [5] 2026-10-21: the navigation exposes 开放平台 (/developer), 开通会员 and desktop clients
  - probe:POST https://api.aliyundrive.com/adrive/v2/share_link/get_share_by_anonymous 2026-10-21: 404 with {"code":"NotFound.ShareLink"} for a share_id that does not exist, so the route exists
  - probe:POST https://api.aliyundrive.com/v2/share_link/get_share_token 2026-10-21: 404 NotFound.ShareLink; /adrive/v3/... answered 'uri(...) not exist', so the working prefix has no /adrive
  - https://raw.githubusercontent.com/liupan1890/aliyunpan/main/adrive sdk/share.md 2026-10-21: documents get_share_token returning a JWT whose payload contains "user_id":"anonymous"
- sources:
  - [1] https://zh.wikipedia.org/wiki/中国大陆网盘列表
  - [2] https://www.alipan.com
  - [3] https://github.com/liupan1890/aliyunpan
  - [4] https://www.alipan.com/developer
  - [5] https://www.alipan.com/
