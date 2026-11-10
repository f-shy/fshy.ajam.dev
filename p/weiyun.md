# 腾讯微云 Tencent

> weiyun.com | Netdisk and pan, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/weiyun/ | JSON https://fshy.ajam.dev/api/v1/entity/weiyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Weiyun (腾讯微云)

- `netdisk-pan/weiyun` | fails-egress | evidence reported | binding per-object-cap | category consumer-pan
- needs card no, phone yes, ID no, institution no | verified 2026-11-04T00:21:07.067Z (inherited) | stale on 2026-11-19
- url https://share.weiyun.com
- free tier: 5 GB for a free account, per the vendor member-centre page | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Not published | source: [2]
- retention: When a membership lapses and usage exceeds the free quota, the account has 180 days to upgrade or clear the excess, after which it is frozen | days: 180 | source: [1]
- egress: Member-gated speed, with free downloads heavily throttled | metered: yes | source: [2]
- identity: country-phone | detail: login is by WeChat app QR scan or by QQ login ('微信登录', 'QQ登录'); the page shows no email or phone sign-in, and what a new WeChat or QQ account needs is unverified: behind a sign-up | country: 86
- interface: rest
- limits:
  - per-object-cap (binding): 5 GB is the free tier total, which is the cap in practice [1]
  - write-gated: need_pwd=1 shares require the password before any listing, and the CGI endpoint wants a signed request [2]
- binding note: The free account is 5 GB, and the share path is closed to an unauthenticated caller even for metadata. Either number closes it; the quota is the one a reader can check without an account.
- tooling: A reverse-engineered client mounts it: the OpenList weiyun driver takes a pasted login cookie and is unmaintained. A pull request to OpenList proposes a further driver on the vendor's MCP API with an MCPToken; its merge state is unverified. github.com/billzhong/weiyun scrapes the share page and then wgets. No rclone backend
- composes with: Nothing to chain. A QQ or WeChat account is required, which is +86-gated in practice, and the share endpoints answer with a null body to an unauthenticated caller
- reliability: The share page ships the share record in a JavaScript blob, so the metadata is embedded and public, and the CGI then answers ret 102027 with a null body. Tencent has left the product on minimal maintenance and the old scrapers work only where the markup has not changed
- notes: Demonstrates metadata embedded directly within page HTML markup while programmatic API access is restricted. The file directory hierarchy is visible publicly while download payloads require authenticated client sessions.
- extras:
  - access_mode: registration-gated
  - anonymous_read: metadata embedded in the page, API refused
- evidence:
  - probe:https://share.weiyun.com/5BPnTh7 2026-10-21: 200, 17,276 B, with inline JSON "share_name":"...rar", "store_cnt":1570, "need_pwd":1, "short_url":"https://share.weiyun.com/5BPnTh7"
  - probe:https://web.cgi.weiyun.com/wy_share.fcg?cmd=get_share_info&share_id=5BPnTh7 2026-10-21: 200, 55 B, {"rsp_body":null,"rsp_header":{"cmd":"","ret":102027}}, so metadata is refused
  - probe:POST https://share.weiyun.com/api/v4/weiyun/share/queryShareInfo 2026-10-21: returned HTML and not JSON, so the endpoint does not exist
  - [1] 2026-11-03: the free account has 5 GB of storage | capture: sha256:30e640ff39803b6d4dbfdee35f8590081b7b2f0ad04f06c037ba80a1aee94c48 | quote: 会员服务到期后，存储空间将恢复到免费账号的5GB存储空间。
  - [1] 2026-11-03: usage over the quota must be cleared or upgraded within 180 days | capture: sha256:30e640ff39803b6d4dbfdee35f8590081b7b2f0ad04f06c037ba80a1aee94c48 | quote: 若您的已用容量超出可用额度，需要在180天内升级存储空间或对容量超额部分进行清理。
  - [3] 2026-11-03: the OpenList Weiyun driver is a reverse-engineered interface that its team does not maintain | capture: sha256:947a1572e76f0c84452d0cac8c4318a5a801b77d1246a0af4b267cf28cd2b23e | quote: 本接口是基于历史产物的逆向接口，项目组不会主动进行维护
  - [3] 2026-11-03: a QQ-login cookie must be replaced after 48 hours | capture: sha256:947a1572e76f0c84452d0cac8c4318a5a801b77d1246a0af4b267cf28cd2b23e | quote: QQ：登录目前只能保活48小时就得更换cookie
  - [4] 2026-11-03: a pull request adds an OpenList driver on the vendor's official MCP API | capture: sha256:1e32a8e601b225649b4c02180f7ea54f10742369f2e515d5b4edbb2a0e5b23cc | quote: 新增微云开放平台（WeiYun Open，基于 MCP 官方 API）的存储驱动 `weiyun_open`，支持通过官方 MCP 接口访问微云网盘。
  - [5] 2026-11-03: the login panel offers a WeChat app QR scan, with QQ login as the other option | capture: sha256:0007e348281b815b87ee86a7579eb56f1992cd80308fdca1a9790a06f1fdedac | quote: 请使用微信App扫码登录
- sources:
  - [1] https://www.weiyun.com/vip
  - [2] https://share.weiyun.com
  - [3] https://openlistteam.github.io/docs/zh/guide/drivers/weiyun.html
  - [4] https://github.com/OpenListTeam/OpenList/pull/2305
  - [5] https://www.weiyun.com/

## 腾讯微云 Tencent Weiyun

- `storage/tencent-weiyun` | fails-quota | evidence reported | binding none | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.weiyun.com
- free tier: Free tier offers approximately 10 GB storage. Paid tiers start around 10 CNY per month. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Throttled for non-members. PanHunt: '非会员限速'. | metered: no
- identity: any-phone | detail: any-phone (QQ/WeChat)
- interface: rest, webdav-proxy
- limits note: quota 10 GB. no WebDAV, no direct link on the free tier ('WebDAV 不支持 / 直链 不支持').
- interface detail: rest
- tooling: OpenList driver `weiyun` (present in drivers/); qaiu netdisk-fast-download does NOT list it, so tooling is OpenList-only.
- composes with: 10 GB x QQ/WeChat accounts. QQ numbers are cheap but each is a real identity.
- reliability: Stable but deliberately shrunk.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: About 10 GB free; paid ~¥10/month.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: '腾讯微云 | 约 10GB | 约 ¥10/月 | 非会员限速 | 不支持 | 不支持'（核对 2026-10-19）
  - [2] 2026-10-21: driver exists
- sources:
  - [1] https://panhunt.com/compare
  - [2] https://github.com/OpenListTeam/OpenList/tree/main/drivers/weiyun
