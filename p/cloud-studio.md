# Cloud Studio

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cloud-studio/ | JSON https://fshy.ajam.dev/api/v1/entity/cloud-studio.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cloud Studio

- `compute/cloud-studio` | trial-only | evidence reported | binding retention-clamped | category dev environment
- needs card no, phone yes, ID yes, institution no | verified 2026-11-03T08:51:16.011Z (live) | stale on 2026-11-18
- url https://linux.do/t/topic/2902157
- free tier: documented standing grant: a 20 machine-hour resource pack after binding a Tencent Cloud account, plus 2 machine hours claimable once a day and valid for 7 days; machine hours are deducted at a factor per machine shape, and when the pack is used up the application keeps running and bills pay-as-you-go to the account balance | unit: credits | metered on: wall-clock | read on: 2026-09-14 | source: [1] | note: machine hours are credits deducted per hour of use at a factor per shape: GPU T4 1.2, GPU V100 3.6, GPU A10 3.3, GPU L40 8, GPU A800 14; the 20 machine-hour pack is about 16.7 hours of T4 or 2.5 hours of L40
- per-object cap: not applicable | source: [2]
- retention: the 2,000 hours came from a defect and not from the offer, so it is unreproducible by design, and the same thread's earlier reports show the standing grant falling from 50,000 minutes a month in 2024 to 20 to 50 hours in 2026. | source: [2]
- egress: not stated | metered: no | source: [2]
- identity: national-id | detail: a Tencent Cloud account must be bound for the first-binding machine-hour grant, and the vendor guide says using compute resources usually needs that account with personal real-name verification; accepted documents are a mainland China resident ID card or a mainland travel permit for Hong Kong, Macau and Taiwan users, and other international documents are sent to the international site; registration also includes phone verification
- interface: unknown
- limits:
  - retention-clamped (binding): the 2,000 hours came from a defect and not from the offer, so it is unreproducible by design, and the same thread's earlier reports show the standing grant falling from 50,000 minutes a month in 2024 to 20 to 50 hours in 2026. [2]
  - volume-quota: a 20 machine-hour pack on first binding of a Tencent Cloud account and 2 machine hours per daily claim valid for 7 days; when the pack is exhausted the application keeps running and bills pay-as-you-go from the account balance; compute is released about 10 minutes after the IDE tab closes [1]
- limits note: the 2,000 hours came from a defect and not from the offer, so it is unreproducible by design, and the same thread's earlier reports show the standing grant falling from 50,000 minutes a month in 2024 to 20 to 50 hours in 2026.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 2,000 L40 hours is about 200 hours of a 10-GPU job, which would be the largest free GPU allowance in earlier readings if it were an offer rather than a defect; as a chain element it is a windfall and not a resource.
- reliability: no reliability event recorded
- notes: Recorded to stop subsequent evaluation chasing it: the number is real and the route is not. ⚠ A defect grant is not a free tier and must not be counted as one, which is why this is `trial-only` with the defect named in the offer. The useful signal is the trend it sits in: Tencent's standing grant fell by roughly two orders of magnitude between 2024 and 2026 while users kept finding temporary surplus.
- extras:
  - facets.class: cloud-ide
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_class: L40
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 48
- evidence:
  - [2] 2026-09-14: the post, translated: 'earlier Cloud Studio had a bug and I got 2,000-plus machine-hours free, I do not know what to do with them'
  - [3] 2026-07-22: 
  - [1] 2026-10-22: quoted, translated from the vendor's machine-hour FAQ: 'first binding grant: after binding a Tencent Cloud account, a 20 machine-hour resource pack is granted' and 'daily login: after logging in each day, 2 machine hours can be claimed from the profile card (valid for 7 days)'. A new account therefore starts with tens of hours and accumulates at 2 a day, which supports the trial-only verdict and the top of the stored 20-to-50-hour range; it does not support the 2,000-hour windfall, which stays a forum report and is not repeated by any vendor page
  - [1] 2026-11-03: binding a Tencent Cloud account grants a 20 machine-hour resource pack; the same FAQ gives 2 machine hours a day valid 7 days | capture: sha256:59758a367fac9120ea4e97fe3837f6cb12d3a5e47ddd70128504eea31d85af38 | quote: 首次绑定赠送：完成腾讯云账号绑定后，赠送 20 机时资源包（自动发放到资源管理）。
  - [1] 2026-11-03: the grant is a resource pack of machine hours, a credit deducted at a per-shape factor | capture: sha256:59758a367fac9120ea4e97fe3837f6cb12d3a5e47ddd70128504eea31d85af38 | quote: 首次绑定赠送：完成腾讯云账号绑定后，赠送 20 机时资源包（自动发放到资源管理）。
  - [4] 2026-11-03: a T4 with 16G of video memory deducts 1.2 machine hours per hour; the same table lists V100 3.6, A10 3.3, L40 8 and A800 14 | capture: sha256:c77eeff6deb8970d2de7a255320fd69b5ff1af252139645104deea7a8c3f1452 | quote: | GPU T4 | T4，8核，32G内存，16G显存 | 1.2 |
  - [1] 2026-11-03: the vendor FAQ is the source of the standing grant | capture: sha256:59758a367fac9120ea4e97fe3837f6cb12d3a5e47ddd70128504eea31d85af38 | quote: 首次绑定赠送：完成腾讯云账号绑定后，赠送 20 机时资源包（自动发放到资源管理）。
  - [5] 2026-11-03: personal real-name verification on the Tencent Cloud account accepts a mainland China ID card, or a mainland travel permit for Hong Kong, Macau and Taiwan users | capture: sha256:acd20bee44956630fa7e8d57e1243fd0964df7c9a76944b8a9dcc821e7352dcc | quote: 支持中国大陆居民使用身份证实名认证，支持中国香港和中国澳门用户使用来往内地通行证认证，支持中国台湾用户使用来往大陆通行证认证。
  - [5] 2026-11-03: using compute resources usually needs a Tencent Cloud account with real-name verification | capture: sha256:acd20bee44956630fa7e8d57e1243fd0964df7c9a76944b8a9dcc821e7352dcc | quote: 如果您需要使用腾讯云相关能力（如算力资源等），通常需要先拥有腾讯云账号并完成实名认证。
  - [1] 2026-11-03: after the resource pack is used up the application is not stopped and switches to pay-as-you-go billing against the account balance | capture: sha256:59758a367fac9120ea4e97fe3837f6cb12d3a5e47ddd70128504eea31d85af38 | quote: 资源包机时耗尽：资源包用完后，系统不会自动停止应用，而是自动切换为按量付费模式，按规格单价从腾讯云账号余额扣除；
  - [1] 2026-11-03: the 20 machine-hour first-binding pack is stated by the vendor FAQ | capture: sha256:59758a367fac9120ea4e97fe3837f6cb12d3a5e47ddd70128504eea31d85af38 | quote: 首次绑定赠送：完成腾讯云账号绑定后，赠送 20 机时资源包（自动发放到资源管理）。
  - [6] 2026-11-03: 2 machine hours can be claimed free each day and are valid for 7 days | capture: sha256:4caa499c7a426cbd71d5763ec7b29cd32a7cbb1181f53c337ae6371599146e0a | quote: 每天可免费领取 2 个机时。领取的机时 7 日内有效。
  - [4] 2026-11-03: an L40 with 48G of video memory deducts 8 machine hours per hour | capture: sha256:c77eeff6deb8970d2de7a255320fd69b5ff1af252139645104deea7a8c3f1452 | quote: | GPU L40 | L40，48核，192G内存，48G显存 | 8 |
  - [7] 2026-11-03: machine hours are consumed while an IDE tab is open and compute is released about 10 minutes after the last IDE tab closes | capture: sha256:8463af3f20e7413ec49f3fb9febe3ed58a0c62b407675eee5991254304be7e51 | quote: 关闭该应用的所有 IDE 模式相关标签页（包括 `edit` / `learn`），系统会在 10 分钟左右自动释放算力并停止消耗（释放期间可能产生少量费用）。
  - [8] 2026-11-03: the 20 machine-hour first-binding grant can usually be claimed once | capture: sha256:da8aec66ede480defc8f5477b26ec9ff8c5462d102af928fbe2dd53299c8d7c8 | quote: 福利通常仅一次**：首次绑定 20 机时福利一般只能领取一次。
- sources:
  - [1] https://cloud.tencent.com/document/product/1039/131773
  - [2] https://linux.do/t/topic/2902157
  - [3] https://linux.do/t/topic/2635751
  - [4] https://cloud.tencent.com/document/product/1039/131894
  - [5] https://cloud.tencent.com/document/product/1039/131801
  - [6] https://cloud.tencent.com/document/product/1039/131775
  - [7] https://cloud.tencent.com/document/product/1039/131770
  - [8] https://cloud.tencent.com/document/product/1039/131802
