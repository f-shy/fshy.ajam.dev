# Tencent CNB

> cnb.cool | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cnb/ | JSON https://fshy.ajam.dev/api/v1/entity/cnb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CNB 云原生构建 (cnb.cool, Tencent Cloud Native Build, community edition)

- `storage/cnb` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- needs card no, phone no, ID yes, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cnb.cool
- free tier: Per top-level org, free tier per month: '仓库存储 100 GiB' + '对象存储 100 GiB' (object storage covers '制品、LFS 对象、图片及附件'), plus 160 build-CPU core-hours and 1600 dev-CPU core-hours. Over-quota is metered at ¥1/GiB/month, and storage is billed on daily average minus the free allowance. So staying under 100+100 GiB per org is genuinely free. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 256 MB per file | bytes: 256000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Pricing table specifies 仓库存储 and 对象存储 by GiB-month without a separate egress traffic row. Public release-attachment downloads run through the cnb.cool CDN. | metered: no
- identity: national-id | detail: national-id (WeChat login / 腾讯云 account; the docs' usage-management flow binds a Tencent Cloud budget). Not anonymous.
- interface: rest, webdav, webdav-proxy, cli
- limits:
  - per-object-cap (binding): 256 MB per file [1]
- limits note: Per-object-cap: 64 GB per release/commit attachment (provider's own plugin README: '目前暂支持 64GB 以内的文件上传'). repo-blob cap: 256 MB per file in the git tree, with the maintainers explicitly steering large files to release attachments ('此256M之限制..当以附件方式为之'). request-rate: none documented. Billing: over the free 100 GiB the org is charged ¥1/GiB/month at month start. Silent overage, not a hard stop.
- interface detail: rest
- tooling: OpenList ships a first-class `cnb_releases` driver (github.com/OpenListTeam/OpenList, drivers/cnb_releases. Fields: repo, token, use_tag_name, default_branch), i.e. a maintained WebDAV/HTTP front end over CNB release attachments. Also the official `cnbcool/attachments` plugin ('支持 commit 和 release 上传或下载附件，目前暂支持 64GB 以内的文件上传') and a Rust CLI (`cnb release download/--share`).
- composes with: Free allowance is per top-level organization ('每个顶级组织独立计费') providing 200 GiB each. Repositories support releases with attachments up to 64 GB per file.
- reliability: Community edition launched public beta 2025-08; beta-free extras expired 2025-08-31, so the 100+100 GiB figures are the steady state. No ban/wipe reports found; overage is billed rather than blocked, which is the real hazard.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '仓库存储 | 100 GiB | ¥1/GiB/月 | Git 对象' and '对象存储 | 100 GiB | ¥1/GiB/月 | 制品、LFS 对象等'; '每个顶级组织独立结算'
  - [2] 2026-10-21: '支持 commit 和 release 上传或下载附件，目前暂支持 64GB 以内的文件上传'
  - [3] 2026-10-21: maintained driver with release-attachment upload/download, proving a working non-web client
- sources:
  - [1] https://docs.cnb.cool/zh/pricing.html
  - [2] https://cnb.cool/wmde/attachments
  - [3] https://github.com/OpenListTeam/OpenList/tree/main/drivers/cnb_releases

## Tencent CNB

- `compute/tencent-cnb` | qualifies-with-caveat | evidence documented | binding volume-quota | category dev environment
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T16:54:12.670Z (live) | stale on 2026-10-25
- url https://docs.cnb.cool/zh/pricing.html
- free tier: translated from the CNB pricing table: cloud-native build CPU free quota 160 core-hours a month; cloud-native development CPU free quota 1,600 core-hours a month; both GPU lines 0 core-hours a month; GPU overage at CNY 0.5 per core-hour; repository storage 100 GiB; object storage 100 GiB; 500 AI credits a month. A core-hour is cores multiplied by hours, so 1,600 core-hours is 200 hours on an 8-core node and 1,600 hours on a 1-core node. | unit: core-hours | metered on: wall-clock | read on: 2026-11-04 | source: [1] | note: allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not published: the billing table on the pricing page lists repository storage, object storage, build and dev CPU and GPU core-hours and AI Credits, and no egress or traffic item | metered: no | source: [1]
- identity: any-phone | detail: a WeChat account and a phone number. The help centre says the real-name step authorises CNB to read the phone number bound to that WeChat account, and that an account without real-name verification may not write, by creating an issue for example. No page read states a country for the number, and whether a WeChat account with no mainland number passes is unverified.
- interface: rest, git
- limits:
  - volume-quota (binding): 160 core-hours a month of build CPU and 1,600 core-hours a month of development CPU, both reset at month end and never carried over; both GPU lanes are 0 core-hours a month, so a job that needs a card bills at CNY 0.5 per core-hour from the first one. [1]
- limits note: the build CPU allowance of 160 core-hours a month binds first, at 20 hours on an 8-core node; the development allowance of 1,600 core-hours is the larger lane, at 200 hours on the same node; both GPU lanes are 0 core-hours a month.
- binding note: the same as limits note
- interface detail: REST (OpenAPI at api.cnb.cool), Git over HTTPS with an access token, and the browser cloud IDE; Git over SSH is documented as unsupported
- tooling: a Git client over HTTPS (username cnb, an access token as the password); the REST OpenAPI at api.cnb.cool; the CNB CLI (command cnb, npm package @cnbcool/cnb-cli or Docker image cnbcool/cnb-cli, login by OAuth2 device flow or the CNB_TOKEN variable)
- composes with: 1,600 CPU core-hours a month runs a continuous build and test loop for a single developer, and it holds the build step of any chain whose GPU step has moved elsewhere.
- reliability: no reliability event recorded
- notes: the GPU lanes now bill by the core-hour: the announcement cancels the free quota for both GPU lines from 2026-08-01 and moves them to pay-as-you-go, and the pricing table lists both at zero core-hours a month. A forum post dated 2026-04-27 had made a shared L40 with more than 40 GB of VRAM look like free capacity. The account is a WeChat login tied to a phone number.
- extras:
  - facets.class: ci-gpu-runner
  - facets.free_tier_kind: allowance
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 16
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the pricing table: build CPU 160 core-hours a month free, development CPU 1,600 core-hours a month free, both GPU lines 0 core-hours a month free, storage 100 GiB for repositories and 100 GiB for objects
  - [2] 2026-07-01: quoted announcement, translated: from 2026-08-01 CNB cancels the free quota for cloud-native build GPU and cloud-native development GPU; GPU moves to pay-as-you-go; organizations without a bound Tencent Cloud budget cannot use GPU at all until they bind one
  - [3] 2026-04-27: the pre-withdrawal state, translated: a .cnb.yaml can request the cnb amd64 GPU L40 tag, giving a shared L40 with more than 40 GB of VRAM, with a single session of at most 4 hours
  - [4] 2026-07-26: an account's own quota panel showing a development GPU monthly quota of 1,600 core-hours, then a reply noting the announcement cancels it, then an answer on 2026-08-01 saying the GPU still works, which is a rollout lag and not a revocation
  - [1] 2026-11-03: the billing table ends with AI Credits and has no egress or traffic row | capture: sha256:a9f02eb070a0a636baab9c5ca987f0a723bc8700c5b8e7420b165bb19f2434c6 | quote: | AI Credits | 500 credits/月 | ¥0.05/credit | NPC 等 AI Token |
  - [5] 2026-11-03: the provider publishes an OpenAPI reference at api.cnb.cool | capture: sha256:45919295a138f3c0b6f4f4e2353056b3f4da5ca92de6a1cd0c3463254bd16cdb | quote: CNB OPENAPI
  - [6] 2026-11-03: Git access is over HTTPS with an access token; SSH is not supported for Git | capture: sha256:2138e9967ce85e13c0951bb1817cdf012901a3d664b88a5c59ddee12533168d7 | quote: 平台不支持 SSH 协议访问，原因如下：
  - [6] 2026-11-04: Git access uses the fixed username cnb with an access token | capture: sha256:2138e9967ce85e13c0951bb1817cdf012901a3d664b88a5c59ddee12533168d7 | quote: 用户名：固定填写 `cnb`
  - [7] 2026-11-04: CNB publishes a command-line tool, CNB CLI, installed as the npm package @cnbcool/cnb-cli or run as the Docker image cnbcool/cnb-cli, covering the OpenAPI | capture: sha256:0e30d0e54949089bc6a3c00a5224f52c91a4c3eb48817ea11a84c798791b0876 | quote: CNB CLI 是 CNB 平台 OpenAPI 的命令行工具， 一条 `cnb` 命令即可访问全部 OpenAPI 能力
  - [6] 2026-11-04: Git over HTTPS uses the fixed username cnb with an access token as the password | capture: sha256:2138e9967ce85e13c0951bb1817cdf012901a3d664b88a5c59ddee12533168d7 | quote: 用户名：固定填写 `cnb`
  - [1] 2026-11-04: the table's unit is the core-hour, cores multiplied by hours, not the clock hour | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: - `8核` 使用 `1小时` = `8核 × 1小时` = `8核时`
  - [1] 2026-11-04: the development CPU allowance is 1,600 core-hours a month, and the table prices overage per core-hour | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: | 云原生开发-CPU | 1600 核时/月 | ¥0.125/核时 | 云原生开发 CPU |
  - [1] 2026-11-04: the development CPU allowance is a monthly core-hour quota that resets at month end, which is a volume quota and not a request rate | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: 云原生开发-CPU 免费额度 `1600核时/月`，月底清零，不叠加至次月。
  - [1] 2026-11-04: the build CPU lane keeps a 160 core-hour monthly allowance alongside the 1,600 development allowance | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: 云原生构建-CPU 免费额度 `160核时/月`，月底清零，不叠加至次月。
  - [1] 2026-11-04: a monthly core-hour allowance per lane, with overage billed per core-hour | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: | 云原生构建-CPU | 160 核时/月 | ¥0.125/核时 | 云原生构建 CPU |
  - [1] 2026-11-04: the 160 core-hour build allowance is 20 hours on the 8-core node, against 200 hours for the 1,600 core-hour development allowance | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: | 8 | 16 | 20小时 |
  - [1] 2026-11-04: the 1,600 core-hour development allowance is 200 hours on the 8-core node | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: | 8 | 16 | 200小时 | 1人、8h/天、25天 |
  - [8] 2026-11-04: the real-name step reads the phone number bound to the WeChat account that signed in, so no phone number is typed into CNB | capture: sha256:919b100876ce7f7e1dee2b15a173f3991666d40fd0f2ceea143f41b29ec23d8e | quote: 在**个人设置 **> 实名认证中，微信扫码授权云原生构建获取您微信关联的手机号码，即可完成实名认证。
  - [3] 2026-11-04: the post reports a shared L40 with more than 40 GB of VRAM as the GPU a build could request | capture: sha256:68ae5d4a48075014c1b1919306907e7a9ada70d666f3378ce8602e8c9e6b6dd1 | quote: 可以用L40，40多G显存（共享）
  - [1] 2026-11-04: the pricing table was read again and still lists zero core-hours a month for the build GPU lane | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: | 云原生构建-GPU | 0 核时/月 | ¥0.5/核时 | 云原生构建 GPU |
  - [1] 2026-11-04: the build GPU lane is zero core-hours a month and overage bills per core-hour | capture: sha256:b99d2bb60fa5744f2c4267651d73e0b00e0279d93cb86fe538884a8a2f2e1865 | quote: | 云原生构建-GPU | 0 核时/月 | ¥0.5/核时 | 云原生构建 GPU |
- sources:
  - [1] https://docs.cnb.cool/zh/pricing.html
  - [2] https://cloud.tencent.com/announce/detail/2349
  - [3] https://linux.do/t/topic/2068176
  - [4] https://linux.do/t/topic/2635751
  - [5] https://api.cnb.cool/
  - [6] https://docs.cnb.cool/zh/guide/git-access.html
  - [7] https://docs.cnb.cool/zh/develops/cnb-cli.html
  - [8] https://cloud.tencent.com/document/product/1785/116269
