# 77File 云盘

> 77file.com | Debrid; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/77file/ | JSON https://fshy.ajam.dev/api/v1/entity/77file.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 77File 云盘 (77file.com), paid tiers

- `debrid/77file-vip` | qualifies-with-caveat | evidence documented | binding volume-quota | category paid-download file host (网赚网盘), VIP | tier 高级会员 / 尊享会员
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:57:23.978Z (live) | stale on 2026-11-23
- url https://www.77file.com/vip.php
- price CNY 16.4 per TB of 流量额度 (尊享, ¥197 for 12 months and 12 TB)
- disagrees on identity_kind: `debrid/77file-free` says email, `debrid/77file-vip` says any-phone
- disagrees on verdict: `debrid/77file-free` says fails-quota, `debrid/77file-vip` says qualifies-with-caveat
- free tier: Free registration gives 100 GB per third-party documentation; the free download path is throttled to tens of KB/s with ads and a wait, which is what the VIP tiers remove. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: 单文件最大 10GB, stated on the vendor's VIP page. | source: [2]
- retention: '文件永不删除' on the VIP page: files are not deleted for inactivity. | source: [2]
- egress: The paid tiers meter traffic, not time: 高级会员 is 存储空间 1T with 流量额度 1T at ¥39.7/month (list ¥40), 尊享会员 is 存储空间 1T with 流量额度 12T at ¥197 per 12 months (list ¥480), which the page renders as ¥16.41/month. | metered: yes | free allowance: 1 TB (高级) or 12 TB (尊享) of 流量额度 | source: [2]
- identity: any-phone | detail: Purchase is by card through a reseller (PayPal) or in-page; the account itself was not read. The vendor page promises '购买后稍等几分钟即开通' and no refunds.
- interface: rest
- limits:
  - volume-quota (binding): 1 TB 流量额度 (高级) or 12 TB (尊享); 存储空间 1 TB both [2]
  - pull-count: 25 次高速传输请求/天 (高级) or 100 次/天 (尊享); a counter of fast pulls, not of bytes [2]
  - per-object-cap: single file 10 GB [2]
  - volume-quota (binding): 1 TB trafii allowance (gaoji) or 12 TB (zunxiang); 1 TB storage on both [2]
  - pull-count: 25 fast-transfer requests per day (gaoji) or 100 per day (zunxiang); a counter of fast pulls, not of bytes [2]
- binding note: The 流量额度 is what binds: 12 TB for ¥197 is ¥16.4/TB, the cheapest paid traffic measured among debrid providers, but it can only be spent on files this host already holds - it is not a route to an arbitrary link.
- interface detail: Browser plus any multi-threaded downloader; the vendor advertises '支持下载加速工具' and '多线程 / 断点续传'.
- tooling: Browser, IDM, aria2. No WebDAV and no documented API.
- composes with: The cheapest paid file host among debrid providers per unit of traffic: ¥197 buys 12 TB, ¥16.4/TB, provided the files are already published by someone else on this host.
- reliability: A 网赚 host: it pays uploaders per download, so the catalogue is monetised links and the domain has changed hands historically. Files are advertised as never deleted, which is unusual and unverified.
- notes: The 25/100 次高速传输请求/天 is a true pull-count in the vocabulary's sense and is rare enough to record: the vendor sells a number of fast pulls per day on top of a byte allowance. The two page variants disagree on the 尊享 price (¥197/12mo vs ¥297/24mo), both promotions, and the conservative per-month figure is recorded. The page does not say whether 流量额度 12T is per month or per term; the arithmetic says per term, because a monthly 12 TB at ¥16.41/month would undercut the 1 TB/month tier at ¥39.7 by a factor no seller would offer. The 高级 per-TB figure therefore stays unstated rather than assumed. The term reading is the record's inference, not a vendor statement, so the row is ranked with the flag rather than used to decide anything.
- evidence note: Both tiers, the traffic allowances, the per-file cap and the never-delete claim were read off the vendor's VIP page. The 100 GB free figure is third-party.
- extras:
  - per_tb_cny: 16.4
  - pull_count_per_day: 100
  - single_file_gb: 10
- evidence:
  - [2] 2026-10-23: '高级会员 / 存储空间 1T · 流量额度 1T 39.7 元/月 原价 40元'; '尊享会员 / 存储空间 1T · 流量额度 12T 16.41 元/月 原价 480元 现价 197元'; '单文件最大 10GB'; '文件永不删除'; '支持下载加速工具'; '多线程 / 断点续传'
  - [3] 2026-10-23: an earlier landing variant of the same page: '高级會員 / 25次高速传输请求/天 1000G儲存 39.7 元/月', '尊享會員 / 100次高速传输请求/天 1000G儲存 12.37 元/月 原价 960元 现价 297元' - a 24-month promo, which is why the per-month figure differs
  - [1] 2026-10-23: third party: free registration '100G 网盘', download rewards '高额的现金下载奖励'
  - [2] 2026-10-23: gaoji: 1 TB storage with 1 TB of traffic at CNY 39.7/month (list CNY 40). zunxiang: 1 TB storage with 12 TB of traffic at CNY 197 per 12 months (list CNY 480), rendered as CNY 16.41/month. Both: 10 GB single file; 25 / 100 fast pulls per day.
- sources:
  - [1] http://www.58xuexi.com/app/v203089.html
  - [2] https://www.77file.com/vip.php
  - [3] https://www.77file.com/vip.php?uid=366925

## 77File 云盘 (77file.com), free account

- `debrid/77file-free` | fails-quota | evidence reported | binding per-ip-shaping | category paid-download file host (网赚网盘), free path | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T11:28:57.799Z (live) | stale on 2026-11-18
- url https://www.77file.com/
- price CNY 0
- disagrees on identity_kind: `debrid/77file-free` says email, `debrid/77file-vip` says any-phone
- disagrees on verdict: `debrid/77file-free` says fails-quota, `debrid/77file-vip` says qualifies-with-caveat
- free tier: 100 GB on registration, per third-party documentation of the vendor's own signup copy: '免费注册即可得到：100G 网盘'. Downloads on the free path are the throttled, ad-bearing path the VIP tiers exist to bypass. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: Not published for the free path; the paid page's 单文件最大 10GB is the only cap the vendor states. | source: [2]
- retention: '文件永不删除' is claimed on the paid page for the service as a whole. | source: [2]
- egress: Free downloads are throttled to tens of KB/s with ads and a wait. Third-party write-ups describe '几十KB/s，甚至几KB/s', which is the same order as 百度网盘's free path. | metered: no | source: [3]
- identity: email | detail: The registration form read shows email, password, password confirmation and captcha fields; a phone option is not shown on it. Whether a downloader needs an account is unverified.
- interface: rest
- limits:
  - per-ip-shaping (binding): free download '几十KB/s' per third-party reporting [4]
  - volume-quota: 100 GB storage on registration [1]
- binding note: A free pull at tens of KB/s cannot deliver a TiB in any month; the shaping is the wall and no byte counter exists to hit instead.
- interface detail: Browser; the returned URL is fetchable by a multi-threaded client.
- tooling: Browser, IDM, aria2.
- composes with: Not a retrieval route here at any volume; recorded because the free path is what most links on this host actually resolve to.
- reliability: Same operator, same monetisation: the free path is deliberately slow because uploaders are paid per download.
- notes: Split from the VIP record because the two tiers differ in the thing that matters: one is the cheapest paid traffic in the sector, the other is unusable.
- evidence note: Neither the 100 GB nor the throttle figure is on a page on 2026-11-03 read from the vendor. Both are third-party. The vendor landing page publishes features only.
- extras:
  - free_gb: 100
- evidence:
  - [3] 2026-10-23: landing page: '77File 云盘：稳定存储、极速下载、加密传输' - features only, no quota, no price
  - [1] 2026-10-23: third party: '免费注册即可得到：100G 网盘', '通过下载量您将获得丰厚的回报'
  - [4] 2026-10-23: third party: '下载速度只有几十KB/s，甚至几KB/s' on the free path
  - [5] 2026-11-03: the registration form asks for an email address, not a phone number | capture: sha256:03fff6a8675962c309ce94e502a331a272eae1a91e08be9e6225c72dbc885795 | quote: 请填写信息创建账号，邮箱务必正确，以便找回密码。
  - [5] 2026-11-03: the form fields are email, password, password confirmation and captcha | capture: sha256:03fff6a8675962c309ce94e502a331a272eae1a91e08be9e6225c72dbc885795 | quote: 邮箱 密码 确认密码 验证码
  - [2] 2026-11-03: the 10 GB per-file maximum is on the VIP page, not the landing page | capture: sha256:a1ef5ac6377bf6febcba9cf0d33aa1e9f4adbdca0877db346e099498f2314a41 | quote: 单文件最大 10GB
  - [2] 2026-11-03: the never-deleted claim is on the VIP page, not the landing page | capture: sha256:a1ef5ac6377bf6febcba9cf0d33aa1e9f4adbdca0877db346e099498f2314a41 | quote: 文件永不删除
  - [3] 2026-11-03: the landing page title advertises free large-capacity storage; no quota figure is on the page | capture: sha256:0e31a3aa20bf122d1d5ce0c048e6bcc3029b80b2e7814d4fd7082cdd8f288b40 | quote: <title>77File 云盘 - 免费超大容量在线云存储</title>
  - [4] 2026-11-03: third party: free download speed of tens of KB/s, sometimes a few KB/s | capture: sha256:e14525f5e4672b52d90add27f41f8d54b5635dd85314605333f95f8c5f2f4204 | quote: 下载速度只有几十KB/s，甚至几KB/s
  - [1] 2026-11-03: third party: the signup copy still lists a 100G disk on registration | capture: sha256:dd2341318472ff6d804f84c02b97a9f960ab3646f807ab240e7a98e16f221bca | quote: 100G 网盘: 与全球用户分享您的文件，无限存储空间，通过下载量您将获得丰厚的回报。
- sources:
  - [1] http://www.58xuexi.com/app/v203089.html
  - [2] https://www.77file.com/vip.php
  - [3] https://www.77file.com/
  - [4] https://www.chimaozy.com/77file%e7%a0%b4%e8%a7%a3%e9%99%90%e9%80%9f/
  - [5] https://www.77file.com/account?action=register
