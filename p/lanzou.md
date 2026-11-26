# Lanzou Cloud

> lanzou.com | Storage, Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lanzou/ | JSON https://fshy.ajam.dev/api/v1/entity/lanzou.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lanzou (蓝奏云)

- `storage/lanzou` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T13:25:55.253Z (live) | stale on 2026-12-10
- url https://www.lanzou.com
- free tier: Unlimited total storage on the free 普通版: '无限制的总存储空间，分享免登录，不限制下载流量，不限速，不限制下载次数'. Per-file cap is the binding constraint, and it is tier-set in 个人中心 → 文件升级. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: no per-file cap stated by the provider | source: [1] | note: unverified: the help page states download speed; no per-file size is stated
- retention: unverified: no retention clause stated by the provider | source: [1] | note: unverified: the help page states download speed, not retention
- egress: Explicitly unmetered: no download traffic limit, no speed limit, no download-count limit, and shares download without login. | metered: no
- identity: any-phone | detail: 手机号 / 获取短信验证码 (mobile phone number and SMS code)
- interface: unknown
- limits:
  - per-object-cap (binding): unverified: no per-file cap stated by the provider [1]
- limits note: Per-file cap is reported at 100 MB for free accounts with account-level adjustments available in settings. Share links are public by design. Registration requires a mobile phone number and SMS verification code.
- interface detail: unverified: no interface stated by the provider
- tooling: unverified: no API stated by the provider; the page shows a web login
- composes with: unverified: object count cannot be derived from a stated per-object cap
- reliability: Registration requires a mainland Chinese phone number for SMS verification. Service provides web upload forms without an official public API.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '无限制的总存储空间，分享免登录，不限制下载流量，不限速，不限制下载次数'
  - [2] 2026-10-21: form fields 手机号 / 获取短信验证码 (phone + SMS required)
  - [1] 2026-11-19: the first-party page confirms unlimited total storage and unmetered downloads | capture: sha256:ddc0f2e6c32a2cdc8a1440273ebcfb8f342b8c373af6f373739f7f6ffbed50b0 | quote: 无限制的总存储空间，分享免登录，不限制下载流量，不限速，不限制下载次数
  - [2] 2026-11-25: the registration form asks for a mobile phone number and an SMS code | capture: sha256:392416d0d364934533ee37ce79a1d509337ab3a498b29033449939cf440c8818 | quote: 手机号 获取短信验证码
  - [1] 2026-11-25: the first-party page shows a web login link | capture: sha256:ddc0f2e6c32a2cdc8a1440273ebcfb8f342b8c373af6f373739f7f6ffbed50b0 | quote: 登录网盘
  - [1] 2026-11-25: the first-party page names the 普通版 tier only | capture: sha256:ddc0f2e6c32a2cdc8a1440273ebcfb8f342b8c373af6f373739f7f6ffbed50b0 | quote: 欢迎体验蓝奏云（普通版）网盘！
  - [3] 2026-11-25: the help fragment states that download speed is unrestricted | capture: sha256:7e8a90a2f237da17ff49a17e0c044cd5018e88a2b8103daf8b8a6ab0f4281d02 | quote: 我们对下载速度不做任何限制。
  - [1] 2026-11-25: the 普通版 page states unlimited storage and unmetered downloads | capture: sha256:ddc0f2e6c32a2cdc8a1440273ebcfb8f342b8c373af6f373739f7f6ffbed50b0 | quote: 无限制的总存储空间，分享免登录，不限制下载流量，不限速，不限制下载次数。
- sources:
  - [1] https://www.lanzou.com/u
  - [2] https://pc.woozooo.com/account.php?action=register
  - [3] https://www.lanzou.com/q/zh/wt.htm

## Lanzou Cloud (蓝奏云)

- `netdisk-pan/lanzou-cloud` | fails-quota | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T15:23:48.018Z (inherited) | stale on 2026-12-10
- url https://www.lanzou.com
- free tier: Unlimited total storage: '拥有无限制的总存储空间' | unit: unlimited | metered on: stored-bytes | read on: 2026-11-25 | source: [1]
- per-object cap: 100 MB per file on the free tier: '不限空间大小，不限下载速度，只是限制文件大小，最大不超过100M/个文件' | bytes: 100000000 | source: [2]
- retention: unverified: the vendor home page as read states no share-link lifetime; account retention is not published | source: [1]
- egress: Free and explicitly unmetered: '下载不限速度，不限流量，不限次数，免登录下载' | metered: no | free allowance: unlimited | source: [1]
- identity: country-phone | detail: the register form (pc.woozooo.com, terms on accounts.woozooo.com) asks for 手机号 plus an SMS code, then a username and password; it shows no email field and no country selector. A foreign-number path is unverified: behind a sign-up | country: 86
- interface: rest
- limits:
  - per-object-cap (binding): 100 MB per file on the free tier [2]
  - request-rate: no WebDAV on a free account; access is only through direct-link extraction [3]
- binding note: The total is genuinely unlimited and the egress is genuinely free, so nothing about capacity or traffic binds. 100 MB per object over a 10 TiB working set is 105,000 objects, which makes the file count the problem before the bytes.
- tooling: no official API. Reverse-engineered clients mount it: the OpenList Lanzou driver in account, cookie or link mode, and a mature unofficial Python wrapper, zaxtyson/LanZouCloud-API, which does login, list, upload, download, delete, move, folder operations and direct-link extraction, and whose README claims it works around both the file-type and the per-file size limits by splitting
- composes with: Unlimited total times 100 MB per object is the pure per-record-unlimited shape: 20 TiB is about 210,000 objects, all inside one free account's allowance. The gate is that registration is SMS-only on a mainland number
- reliability: Domains rotate across lanzou.com, lanzoue, lanzouj, lanzoux, and lanzoul. Share links valid on one domain frequently return HTTP 404 on others, requiring automated tools to maintain a multi-domain fallback list. CDN delivery exhibits geographical routing instability.
- notes: Exemplifies the per-item unlimited storage model where the 100 MiB per-file upload cap is the primary operational constraint. Vendor documentation confirms unlimited overall account capacity with per-file restrictions.
- extras:
  - access_mode: registration-gated
  - aliases: Lanzou Cloud / 蓝奏云; Lanzou (蓝奏云)
  - cross_topic_record: storage/lanzou
  - cross_topic_note: the storage topic carries the same provider; this record is scoped to its role as a direct-link target
- evidence:
  - [1] 2026-10-21: '拥有无限制的总存储空间'; '下载不限速度，不限流量，不限次数，免登录下载！'; '分享文件地址永久有效'
  - [2] 2026-10-21: '免费空间：无限制，只是限制文件大小，最大不超过100M/个文件'
  - [4] 2026-10-21: 811 stars, PyPI lanzou-api; the README claims it works around both the file-type and the per-file size limits
  - probe:https://abskoop.lanzoue.com/iyobY0jnhpdi 2026-10-21: 200, 1,976 B, title '数码小站 V0.4.2.zip - 蓝奏云', body contains src="/fn?AmQFb1o_bVDU..."
  - probe:POST https://apifile.woozooo.com/ajaxfile.php?file=95202518 2026-10-21: 200, 643 B, {"zt":1,"dom":"https://developer4.lanrar.com","url":"?AmRaZF1s..."} for action=downprocess
  - probe:GET https://developer4.lanrar.com/file/<token> 2026-10-21: 200 but 2,714 B of gzipped JavaScript from an automated-traffic filter, so the raw CDN needs the token chain; the parser path is reliable
  - [5] 2026-10-21: '新用户注册, 手机号, 获取短信验证码, 我已同意服务协议并注册', so signup is SMS-only
  - [3] 2026-10-21: '链接：只能显示链接里面的内容（不需要提供cookie就可以挂载）'
  - [5] 2026-11-03: the register form asks for a phone number, used for SMS verification and recovery, and a username and password | capture: sha256:392416d0d364934533ee37ce79a1d509337ab3a498b29033449939cf440c8818 | quote: 请使用用户名登录，手机号仅用于找回短信验证。
  - [3] 2026-11-03: the OpenList Lanzou driver mounts an account from a username and password | capture: sha256:ea97382be4ddfd770e37a0a1258a89fce5bef892ff485d54dbe66a90ba305ca2 | quote: 可以显示自己网盘所有文件，只需要填写帐号密码，会自动帮你刷新cookie
  - [1] 2026-11-25: the vendor page states unlimited total storage | capture: sha256:5b05f639888fc838d484db8cbd6c9eab5b1697c8de56482ddb0f69de4e20a18d | quote: 拥有无限制的总存储空间，支持个性化定制。
  - [1] 2026-11-25: the vendor page states downloads are unthrottled, unmetered, uncounted and login-free | capture: sha256:5b05f639888fc838d484db8cbd6c9eab5b1697c8de56482ddb0f69de4e20a18d | quote: 下载不限速度，不限流量，不限次数，免登录下载！
  - [6] 2026-11-25: the FAQ states there is no download speed limit | capture: sha256:7e8a90a2f237da17ff49a17e0c044cd5018e88a2b8103daf8b8a6ab0f4281d02 | quote: 我们对下载速度不做任何限制。
  - [2] 2026-11-25: the free tier has unlimited total space but caps each file at 100M | capture: sha256:a26fab2e5047b59b72b1dba236fe74e58fd7330dd4d1dca07bdeb155efda18f5 | quote: 不限空间大小，不限下载速度，只是限制文件大小，最大不超过100M/个文件
- sources:
  - [1] https://www.lanzou.com/
  - [2] https://www.cnblogs.com/Dongmy/p/18143085
  - [3] https://openlistteam.github.io/docs/zh/guide/drivers/lanzou.html
  - [4] https://github.com/zaxtyson/LanZouCloud-API
  - [5] https://pc.woozooo.com/account.php?action=register
  - [6] https://www.lanzou.com/q/zh/wt.htm
