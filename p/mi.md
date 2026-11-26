# Xiaomi Token

> mi.com | Inference, Coding subscriptions, Netdisk and pan; 5 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mi/ | JSON https://fshy.ajam.dev/api/v1/entity/mi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Xiaomi

- `inference/xiaomi` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://mimo.mi.com/docs/price/pay-as-you-go
- free tier: MiMo-V2.5-TTS Series is 'PriceFree (limited time)'; other models bill per million tokens (e.g. MiMo-V2.5 input cache-miss USD 0.14, output USD 0.28). | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key from the MiMo platform; signup fields not detailed
- interface: rest
- limits:
  - volume-quota (binding): TTS free for a limited time; text models per-token priced [1]
- endpoint: https://api.xiaomimimo.com/v1
- tooling: OpenAI- and Anthropic-compatible clients against the MiMo endpoint
- composes with: only TTS is free and only for a limited time; text models are paid
- reliability: model IDs MiMo-V2.5-Pro and MiMo-V2.5 are marked deprecated in the model catalogue; use V2.6
- notes: The free text-model allowance is absent; only a limited-time TTS free price is documented. A MiMo Claw promo extends 'free usage' from 1h to 4h/day for that product, not the API.
- evidence:
  - [1] 2026-11-18: the TTS series is free for a limited time | capture: sha256:f064cf5ab38d60fbdc8be0627e254d7fc9d8db971aa5ed316d07b00d4eec9570 | quote: PriceFree (limited time)
- sources:
  - [1] https://mimo.mi.com/docs/price/pay-as-you-go

## Xiaomi Token Plan (China)

- `coding-subs/xiaomi-token-plan-cn` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://mimo.mi.com/docs/price/token-plan
- free tier: No free tier for text inference. Individual Lite USD 6/month (CNY 39) for 4.1 billion Credits; Standard USD 16, Pro USD 50, Max USD 100. TTS models are free for a limited time and do not consume Credits. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: a Xiaomi MiMo account and a purchased Token Plan; exact signup identity fields not verified
- interface: rest, cli
- limits:
  - volume-quota (binding): 4.1 billion to 82 billion Credits per month by tier [1]
  - retention-clamped: monthly quota does not roll over; service suspends on exhaustion [1]
- endpoint: https://token-plan-cn.xiaomimimo.com/v1
- tooling: an API key against OpenAI-compatible endpoints; OpenCode, OpenClaw and Claude Code are named
- composes with: monthly Credits are the scarce link; when exhausted the service suspends until an upgrade or a switch to pay-as-you-go
- reliability: MiMo-V2.5-Pro and V2.5 were retired on 2026-10-21; the plan suspends when the monthly quota is exhausted and cannot draw the account balance
- notes: Paid-only. The three regional ids share the same first-party Token Plan price page; they differ only in API endpoint region.
- evidence:
  - [1] 2026-11-18: the Lite individual plan is USD 6 per month with no free text tier | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: $6/month, ¥39/month
  - [1] 2026-11-18: the fixed monthly Credits are stated for each tier | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: Fixed Monthly Quota
  - [1] 2026-11-18: the service suspends when the monthly quota is used up | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: When the monthly total quota of the package is used up, the system will suspend the service and will not continue to deduct from your bonus or account balance.
- sources:
  - [1] https://mimo.mi.com/docs/price/token-plan

## Xiaomi Token Plan (Europe)

- `coding-subs/xiaomi-token-plan-ams` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://mimo.mi.com/docs/price/token-plan
- free tier: No free tier for text inference. Individual Lite USD 6/month (CNY 39) for 4.1 billion Credits; Standard USD 16, Pro USD 50, Max USD 100. TTS models are free for a limited time and do not consume Credits. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: a Xiaomi MiMo account and a purchased Token Plan; exact signup identity fields not verified
- interface: rest, cli
- limits:
  - volume-quota (binding): 4.1 billion to 82 billion Credits per month by tier [1]
  - retention-clamped: monthly quota does not roll over; service suspends on exhaustion [1]
- endpoint: https://token-plan-ams.xiaomimimo.com/v1
- tooling: an API key against OpenAI-compatible endpoints; OpenCode, OpenClaw and Claude Code are named
- composes with: monthly Credits are the scarce link; when exhausted the service suspends until an upgrade or a switch to pay-as-you-go
- reliability: MiMo-V2.5-Pro and V2.5 were retired on 2026-10-21; the plan suspends when the monthly quota is exhausted and cannot draw the account balance
- notes: Paid-only. The three regional ids share the same first-party Token Plan price page; they differ only in API endpoint region.
- evidence:
  - [1] 2026-11-18: the Lite individual plan is USD 6 per month with no free text tier | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: $6/month, ¥39/month
  - [1] 2026-11-18: the fixed monthly Credits are stated for each tier | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: Fixed Monthly Quota
  - [1] 2026-11-18: the service suspends when the monthly quota is used up | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: When the monthly total quota of the package is used up, the system will suspend the service and will not continue to deduct from your bonus or account balance.
- sources:
  - [1] https://mimo.mi.com/docs/price/token-plan

## Xiaomi Token Plan (Singapore)

- `coding-subs/xiaomi-token-plan-sgp` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://mimo.mi.com/docs/price/token-plan
- free tier: No free tier for text inference. Individual Lite USD 6/month (CNY 39) for 4.1 billion Credits; Standard USD 16, Pro USD 50, Max USD 100. TTS models are free for a limited time and do not consume Credits. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: a Xiaomi MiMo account and a purchased Token Plan; exact signup identity fields not verified
- interface: rest, cli
- limits:
  - volume-quota (binding): 4.1 billion to 82 billion Credits per month by tier [1]
  - retention-clamped: monthly quota does not roll over; service suspends on exhaustion [1]
- endpoint: https://token-plan-sgp.xiaomimimo.com/v1
- tooling: an API key against OpenAI-compatible endpoints; OpenCode, OpenClaw and Claude Code are named
- composes with: monthly Credits are the scarce link; when exhausted the service suspends until an upgrade or a switch to pay-as-you-go
- reliability: MiMo-V2.5-Pro and V2.5 were retired on 2026-10-21; the plan suspends when the monthly quota is exhausted and cannot draw the account balance
- notes: Paid-only. The three regional ids share the same first-party Token Plan price page; they differ only in API endpoint region.
- evidence:
  - [1] 2026-11-18: the Lite individual plan is USD 6 per month with no free text tier | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: $6/month, ¥39/month
  - [1] 2026-11-18: the fixed monthly Credits are stated for each tier | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: Fixed Monthly Quota
  - [1] 2026-11-18: the service suspends when the monthly quota is used up | capture: sha256:8c60cfb714cf93bcfe265e4857d779bad7a439d4fa0f3f10942650f44f57eb77 | quote: When the monthly total quota of the package is used up, the system will suspend the service and will not continue to deduct from your bonus or account balance.
- sources:
  - [1] https://mimo.mi.com/docs/price/token-plan

## 小米云服务 / Xiaomi Cloud (Mi Cloud Drive)

- `netdisk-pan/xiaomi-cloud` | fails-quota | evidence reported | binding per-object-cap | category phone-vendor cloud, China mainland
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T14:57:25.809Z (inherited) | stale on 2026-12-10
- url https://i.mi.com/
- price unverified: the manual publishes CNY annual prices only
- free tier: 5G free, with 50G, 200G and 2048G paid tiers at 72, 252 and 816 yuan a year | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published; the drive is sync-oriented and does not expose a single-file ceiling | source: [1]
- retention: Gallery sync and membership termination is staged by region: before December 1, 2022, before January 1, 2023 and before February 1, 2023; transfer windows close by May 31, 2023, June 30, 2023 and July 31, 2023; these services are not terminated on the Chinese mainland at this time | source: [2]
- egress: No published cap, and the drive is deliberately not share-oriented: the community notes 不能对外分享. Third-party clients download at full speed with concurrency 20 | metered: no | source: [3]
- identity: email | detail: A Xiaomi account outside the Chinese mainland can only be created through email; a +86 phone binding identifies a Chinese mainland account | country: 86
- interface: rest, cli
- limits:
  - per-object-cap (binding): 5 GB is the free tier total, which is the cap in practice [1]
  - write-gated: family sharing is capped at 8 members and shares quota and not data [1]
- binding note: Free storage is limited to 5 GB. Global email registration routes accounts to international regions where consumer drive sync features have been phased out. Total account quota is the binding constraint.
- tooling: a reverse-engineered REST interface at i.mi.com with a Go CLI, wangbjun/go-micloud, doing login, list, upload, download, share and tree at concurrency 5 up and 20 down; an unmerged OpenList driver pull request 1391 implements list, link, put and mkdir but its body says 还没写完
- composes with: The API is real and a wrapper exists, so it would be the cleanest phone-vendor target. 5 GB free means about 410 accounts per 2 TB and the 2 TB tier is CNY 239 to 408 a year, which is not a stacking play
- reliability: Global-region Gallery sync and all memberships were terminated outside mainland China in three regional waves by 2023-02-01, with Gallery data deleted by mid-2023. An email signup works and lands in the region where the product no longer exists, which is a worse outcome than a closed gate because it looks open
- notes: Email registration succeeds internationally but maps accounts to global regions lacking active drive storage sync. Unofficial client tooling includes experimental Go wrapper scripts and community OpenList driver integrations.
- extras:
  - access_mode: registration-gated
  - region_gate_inverted: yes
  - terminated_outside_mainland: 2022-10-25 onwards
  - aliases: 小米云服务 / Xiaomi Cloud (Mi Cloud Drive); 小米云服务 Xiaomi Cloud
- evidence:
  - [1] 2026-10-21: the tier table 免费 5G, 50G, 200G, 2048G at CNY 72, 252 and 816 a year
  - [2] 2026-10-21: 'Syncing of Gallery items to Xiaomi Cloud and Xiaomi Cloud membership services will be terminated' outside the Chinese mainland, and 'These services will not be terminated on the Chinese mainland at this time'
  - [4] 2026-10-21: 'The Xiaomi account outside the Chinese mainland can only be created through email'
  - [5] 2026-10-21: a full CLI, '登录采用模拟小米云服务Web端的登录逻辑', upload concurrency 5 and download 20
  - [6] 2026-10-21: 'Xiaomi Cloud Dirve', list, link, put and mkdir implemented, body says 还没写完
  - probe:https://i.mi.com/file/full?type=note_ 2026-10-21: HTTP 200, 102 bytes, {"result":"error","reason":"fileid参数不能为空","code":10016}, which is a 200 that carries an error
  - probe:https://i.mi.com/storage/web/v2/storage 2026-10-21: HTTP 404, 211 bytes, a Resin/4.0.61 MicloudWeb HTML error page
  - [2] 2026-11-03: the notice still says the Gallery sync and membership termination does not apply on the mainland | capture: sha256:fc31d226b1398d7ddec129c34360319c0d72eea8173cdf0f242c0cf922322c3f | quote: These services will not be terminated on the Chinese mainland at this time.
  - [2] 2026-11-03: the notice gives the three regional termination dates | capture: sha256:fc31d226b1398d7ddec129c34360319c0d72eea8173cdf0f242c0cf922322c3f | quote: | Before December 1, 2022 | Before January 1, 2023 | Before February 1, 2023 |
  - [3] 2026-11-03: the portal answers 200 and asks for a Xiaomi Account sign-in | capture: sha256:76ea69cb1bdbde2e6f2ef4a8272f6bbf1ed649877122b0c82fe8cb965d79f999 | quote: Sign in with Xiaomi Account
  - [5] 2026-11-03: the Go client still documents upload concurrency 5 and download concurrency 20 | capture: sha256:263ed9529b009a871c34ff2fa130e0540d726e9e1a38a1937a89ea338ac430b6 | quote: 上传和下载采用异步方式，默认上传并发5，下载并发20
  - probe:https://i.mi.com/file/full?type=note_ 2026-11-03: the file endpoint answers 200 with a JSON error body (102 bytes), a 200 that carries an error | capture: sha256:a81eb88f28b3b65bb54245632c88edb1561b358a08a9f528bee2a6b737753e52 | quote: "reason":"fileid参数不能为空"
  - probe:https://i.mi.com/storage/web/v2/storage 2026-11-03: the storage path answers 404 from a Resin/4.0.61 server | capture: sha256:875df53cc2022138b5de87de28d4fa32ed88a1e195d1138a909f37d3b1015550 | quote: Resin/4.0.61
  - [1] 2026-11-25: the manual lists 5G free and 50G, 200G and 2048G paid tiers at 72, 252 and 816 yuan a year | capture: sha256:57bb30b45cf1f73ef278d1fa9f4a8a999f394c48bcce23a3bfd0f194b1ad6f61 | quote: | 云存储空间 | 5G | 50G | 200G | 2048G | ... | 会员价格 | 免费 | 72元/年 | 252元/年 | 816元/年 |
  - [1] 2026-11-25: the manual prices membership in yuan per year, with no monthly or dollar figure | capture: sha256:57bb30b45cf1f73ef278d1fa9f4a8a999f394c48bcce23a3bfd0f194b1ad6f61 | quote: | 会员价格 | 免费 | 72元/年 | 252元/年 | 816元/年 |
  - [4] 2026-11-25: the FAQ distinguishes mainland accounts by a +86 phone binding and says non-mainland accounts are created by email | capture: sha256:9587f282635c57473aebb17c6076d47a71d87f034fcaf9971db6dfc355c8fe73 | quote: +86 is the beginning of the Chinese mobile phone number. If you can only bind a mobile phone number beginning with +86 when registering a Xiaomi account, it means that the Xiaomi account you created is a Chinese mainland account. ... The Xiaomi account outside the Chinese mainland can only be created through email.
  - [2] 2026-11-25: the notice gives three regional termination dates, three transfer deadlines and a mainland exclusion | capture: sha256:fc31d226b1398d7ddec129c34360319c0d72eea8173cdf0f242c0cf922322c3f | quote: | Before December 1, 2022 | Before January 1, 2023 | Before February 1, 2023 | ... | May 31, 2023 | June 30, 2023 | July 31, 2023 | ... These services will not be terminated on the Chinese mainland at this time.
  - [1] 2026-11-25: the ordinary tier is given as 5G, the paid tiers as 50G, 200G and 2048G | capture: sha256:57bb30b45cf1f73ef278d1fa9f4a8a999f394c48bcce23a3bfd0f194b1ad6f61 | quote: | 云存储空间 | 5G | 50G | 200G | 2048G |
  - [4] 2026-11-25: binding only a +86 mobile number marks the account as a Chinese mainland account | capture: sha256:9587f282635c57473aebb17c6076d47a71d87f034fcaf9971db6dfc355c8fe73 | quote: +86 is the beginning of the Chinese mobile phone number. If you can only bind a mobile phone number beginning with +86 when registering a Xiaomi account, it means that the Xiaomi account you created is a Chinese mainland account.
  - [4] 2026-11-25: an account outside the Chinese mainland can only be created through email | capture: sha256:9587f282635c57473aebb17c6076d47a71d87f034fcaf9971db6dfc355c8fe73 | quote: 2. The Xiaomi account outside the Chinese mainland can only be created through email.
- sources:
  - [1] https://i.mi.com/guide/zh-CN/membership/overview
  - [2] https://i.mi.com/announcement/stop_service
  - [3] https://i.mi.com/
  - [4] https://www.mi.com/global/support/faq/details/KA-547873/
  - [5] https://github.com/wangbjun/go-micloud
  - [6] https://github.com/OpenListTeam/OpenList/pull/1391
