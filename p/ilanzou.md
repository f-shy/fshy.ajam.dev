# Lanzou Premium

> ilanzou.com | Storage, Netdisk and pan; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ilanzou/ | JSON https://fshy.ajam.dev/api/v1/entity/ilanzou.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 蓝奏云优享版 iLanzou (ilanzou.com)

- `storage/ilanzou` | qualifies-with-caveat | evidence reported | binding per-object-cap | category cloud-drive
- needs card no, phone yes, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.ilanzou.com
- free tier: Free account starts at 10 GB; after phone/email verification it becomes 2 TB but only for 1 year ('注册认证用户可以获得 2T 容量（1年）'). Paid 10 TB at ¥9/mo or ¥88/yr. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: no published per-file limit on 优享 (classic Lanzou is 100 MB | bytes: 100000000 | source: [1] | note: not stated
- retention: retention-clamped: the 2 TB grant is 1 year, not permanent | days: 365 | source: [1] | note: not stated
- egress: Unlimited speed, download without login: homepage '不限速 / 下载免登录'. Caveat from a secondary source: non-members need to log in to download shared files larger than 100 MB. | metered: no
- identity: country-phone | detail: country-phone or email (绑定手机或邮箱 unlocks the 2 TB).
- interface: rest, webdav-proxy
- limits:
  - retention-clamped: retention-clamped: the 2 TB grant is 1 year [1]
  - per-object-cap (binding): per-object-cap: no published per-file limit on 优享 (classic Lanzou is 100 MB [1]
- limits note: retention-clamped: the 2 TB grant is 1 year, not permanent. per-object-cap: no published per-file limit on 优享 (classic Lanzou is 100 MB). Sharing: >100 MB shared files require the downloader to log in.
- interface detail: rest
- tooling: OpenList driver `ilanzou` (reverse-engineered, explicitly unmaintained: '本接口是基于历史产物的逆向接口，项目组不会主动进行维护'); qaiu/netdisk-fast-download `iz` parser; HeriHeriCloud treats the Lanzou family as its storage substrate.
- composes with: 2 TB per verified account, expiring in 12 months. So treat as '2 TB renewable annually per identity', not a permanent tier. 10 GB/file is the classic-Lanzou escape (classic caps at 100 MB).
- reliability: Two-tier product (classic vs 优享) with repeated policy narrowing. IT之家 reported APK sharing moved behind the ¥9/mo paywall. Unmaintained OpenList driver means the API can rot.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: '下载免登录 / 不限速 / 无损存储'
  - [1] 2026-10-19: '免费 较小...适合稍大文件的无门槛分享' (table checked 2026-10-19)
  - [3] 2026-10-21: '免费用户初始容量为10GB，完成认证（绑定手机或邮箱）后可获得 2TB容量（有效期1年）'
  - [4] 2026-10-21: driver present but marked reverse-engineered/unmaintained
- sources:
  - [1] https://panhunt.com/pan-platforms/ilanzou
  - [2] https://www.ilanzou.com/
  - [3] https://www.11map.com/sites/506.html
  - [4] https://docs.oplist.org/guide/drivers/ilanzou

## Lanzou Premium (蓝奏云优享版, ilanzou)

- `netdisk-pan/lanzou-premium` | fails-quota | evidence reported | binding per-object-cap | category consumer-pan
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:21:07.070Z (inherited) | stale on 2026-11-19
- url https://www.ilanzou.com
- free tier: A free account has a free tier: the vendor page publishes no quota figure, and a third-party page reports 10 GB, or 2 TB for one year after registration and account authentication, against 10 TB for a member. Per-file cap is above the legacy 100 MB | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Above the legacy 100 MB and not published as one number; large-file resolution needs an account | source: [1]
- retention: Not published | source: [1]
- egress: Ordinary users upload and download with no speed limit ('普通用户上传下载永不限速'); files under 100 MB download from a share link without a login, larger files need a login unless the downloader is… | metered: no | source: [1]
- identity: email | detail: unverified: the vendor home page shows only a login control and no registration form. A third-party page says registration plus 'account authentication' (账号认证) unlocks the 2 TB year, and what that authentication asks for is not stated. Behind a sign-up
- interface: rest
- limits:
  - per-object-cap (binding): above 100 MB and unpublished; large-file resolution needs an account [2]
- binding note: The capacity is paid and no free figure is published, so the free tier cannot be shown to reach anything. The per-file cap is the number a buyer would need and the page does not publish it.
- tooling: Reverse-engineered clients mount it: the OpenList ilanzou driver takes an account and password and has no share mode, and the netdisk-fast-download iz parser needs authentication only for large files
- composes with: Nothing to multiply, because the capacity is paid. Its role in the topic is as the resolver's iz driver, which is what makes legacy Lanzou links reachable when the direct CDN refuses
- reliability: The same rotating-CDN problem as legacy Lanzou, plus one observed failure that matters: the resolver issued a direct URL anonymously and the connection then could not be made. A resolved link is not a delivered file
- notes: The one probe is a real finding: a share resolved anonymously and the CDN then refused the TCP connection, which is why the record says a resolved link is not a delivered file.
- extras:
  - access_mode: paid
  - resolver_driver: iz
  - aliases: Lanzou Premium / 蓝奏云优享版 (ilanzou)
  - registration_path_unverified: yes
- evidence:
  - probe:https://lz.qaiu.top/parser?url=https%3A%2F%2Fwww.ilanzou.com%2Fs%2FbyZ05Sh3&pwd=xbc6 2026-10-21: 302 to https://small5.bakstotre.com/...491744860608972.rar with a filename, so a direct URL was issued anonymously; the connection then failed after 23 seconds
  - [3] 2026-10-21: '在线预览, 下载免登录, 不限速, 无损存储'
  - [4] 2026-10-21: the driver needs 账户、密码 only
  - [2] 2026-10-21: the iz parser needs authentication for large files
  - [3] 2026-11-03: files under 100 MB download from a share link without login; above that a login is needed, except for VIP | capture: sha256:7de65de6f432b32f58a357e1b31778faf7776190dd2955dc8af3d5c33e52ea0f | quote: 小于100M的文件，普通用户可通过分享链接免登陆下载 VIP用户无分享链接文件大小上限下载限制
  - [5] 2026-11-03: a third-party comparison gives a free account 10 GB, and 2 TB for a year after registration and authentication | capture: sha256:5e029a309be1cc8c8d6b5621b6ba736ddf6923e562caf097c1fca322225f7e26 | quote: | 存储容量 | 10GB（注册认证后享2T/1年） | 10TB |
  - [5] 2026-11-03: registration and an account authentication step are named, with no detail on what it requires | capture: sha256:5e029a309be1cc8c8d6b5621b6ba736ddf6923e562caf097c1fca322225f7e26 | quote: 新用户注册并完成账号认证后，即可
  - [4] 2026-11-03: the OpenList ilanzou driver is configured with an ilanzou account and password | capture: sha256:f13c1d9c1502125c2cdf3c7681abdc2c6e5f34305f18c78e8f9831a716c0dd25 | quote: 填写自己的蓝奏云优享版帐号密码
  - [3] 2026-11-03: ordinary users upload and download with no speed limit | capture: sha256:7de65de6f432b32f58a357e1b31778faf7776190dd2955dc8af3d5c33e52ea0f | quote: 普通用户上传下载永不限速
- sources:
  - [1] https://www.ilanzou.com
  - [2] https://github.com/qaiu/netdisk-fast-download
  - [3] https://www.ilanzou.com/
  - [4] https://openlistteam.github.io/docs/zh/guide/drivers/ilanzou.html
  - [5] https://ai-321.com/AI/13827.html
