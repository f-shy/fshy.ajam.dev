# baidu pan

> ithome.com | Debrid, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ithome/ | JSON https://fshy.ajam.dev/api/v1/entity/ithome.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 迅雷超级会员 (Xunlei SVIP)

- `debrid/xunlei-super-member` | qualifies-with-caveat | evidence reported | binding volume-quota | category download accelerator + cloud drive membership | tier 超级会员 (SVIP)
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T11:28:53.665Z (live) | stale on 2026-11-18
- url https://www.ithome.com/1/012/491.htm
- price CNY 9.93/month at the 30-month price (¥298/30mo); CNY 22/month on 连续包年 | parsed USD 1.49/mo
- free tier: 超级会员 is sold by the month. The vendor's own table gives the non-member column (普通用户) a 10GB cloud drive, 10-day recycle bin, 5 GB per month of cloud-drive high-speed download ('非会员：5GB/月') and a speed table entry of 586 KB/s against 15.8 MB/s for 超级会员. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The vendor page vip.xunlei.com/vip_service/supervip_info/dist/ was read on 2026-11-03.
- per-object cap: Not published. 云添加 accepts up to 500 files per submission and the drive is 10 to 12 TB, so the practical unit is a task, not a byte. | source: [2]
- retention: 云盘回收站: the vendor table lists 保留60天 (年费超级会员), 保留30天 (超级会员), 保留15天 (白金会员) and 保留10天 (普通用户). Files not deleted are kept while the membership runs. | days: 60 | source: [3]
- egress: The vendor page states the cloud-drive high-speed download volume by member level: 超级会员等级1-3：2TB/月、超级会员等级4-6：6TB/月，超级会员等级7-10：12TB/月、白金会员：1TB/月、非会员：5GB/月. A third-party article quoting the vendor's promotion states 月度支持10TB云盘高速取回. When the volume is used up the task runs at normal speed. | metered: yes | free allowance: 5 GB/month of 云盘高速下载 for a non-member; 10 TB/month is the third-party figure for the annual membership | source: [3]
- identity: any-phone | detail: The login offers a phone number plus 微信/QQ QR login. No email-only path was found and the login page at i.xunlei.com returned an empty document to every reader tried, so whether a non-mainland number is accepted was not established. Phone is the gate; the country rule is unverified.
- interface: cli
- limits:
  - volume-quota (binding): 云盘高速下载 per month, vendor page: 超级会员等级1-3：2TB/月、超级会员等级4-6：6TB/月，超级会员等级7-10：12TB/月、白金会员：1TB/月、非会员：5GB/月; a third-party article states 月度支持10TB云盘高速取回 and 文件上传流量为240G/天、1T/月 [3]
  - request-rate: 1000 次云添加/天, 500 files per submission [3]
  - per-ip-shaping: 10 并行下载; the vendor speed table puts 超级会员 at 15.8 MB/s against 586 KB/s un-membered [1]
- binding note: 10 TB/month of high-speed retrieval is the first wall at 1 TiB/month only if uploads are also counted; the real constraint is that retrieval is inside a membership, not sold per byte, so the quota binds before any shaping does.
- interface detail: Vendor client only. 云添加 takes magnet, ed2k and http(s) links, and third-party tools drive it through the user's own endpoints rather than a published API. No public API was found on any page read.
- tooling: Official Windows, macOS, Android and iOS clients; the 云添加 queue accepts magnet/ed2k/http in batch. No rclone backend exists for 迅雷云盘.
- composes with: Retrieval is a monthly allowance inside the membership, set by the member level: 超级会员等级1-3：2TB/月、超级会员等级4-6：6TB/月，超级会员等级7-10：12TB/月、白金会员：1TB/月、非会员：5GB/月 on the vendor page (a third-party article states 月度支持10TB云盘高速取回). The card price is in price_per_tb_month.
- reliability: Offline downloading and acceleration features are consolidated under member acceleration, making cloud retrieval dependent on active subscription status.
- notes: Drive size by source: IT之家 and 新浪 say 12 TB, the 会员省 price index says 10 TB, and the vendor privilege table lists 12T (年费超级会员), 6T (超级会员), 3T (白金会员) and 10GB (普通用户). 迅雷's 离线 function no longer exists as a standalone product; the cloud-add queue is what replaced it.
- evidence note: Prices come from IT之家 and 新浪 quoting the vendor's promotion pages and from the 会员省 index (read 2026-11-03). The vendor's privilege page vip.xunlei.com/vip_service/supervip_info/dist/ was read on 2026-11-03 and gives the allowances by level. The login page was not readable; one purchase and one 云添加 would raise this to measured.
- extras:
  - cloud_add_per_day: 1000
  - retrieval_tb_month: 10
  - parallel_downloads: 10
- evidence:
  - [2] 2026-10-23: 30-month 券后 298 元 (9.93 元/月), 年卡 360 元, 连续包年 264 元; '12T 云盘空间、每天 1000 次云添加'; '下载超级加速'
  - [3] 2026-10-23: '云盘空间达12TB，云添加次数为1000次/天，单次可上传500个文件，月度支持10TB云盘高速取回，文件上传流量为240G/天、1T/月，还支持超级通道、10个并行下载，云盘回收站保留60天'
  - [1] 2026-10-23: vendor speed table 15.8 MB/s / 7.82 MB/s / 586 KB/s across 超级会员 / 会员 / 非会员; page returned 403, table seen through the search index only
  - [4] 2026-10-23: same 30-month deal at ¥298 and 15-month at ¥159 on 2026-10-23; this page calls the drive 10T rather than 12T
  - [1] 2026-11-03: the vendor page states the monthly cloud-drive high-speed download volume by member level, 5 GB for a non-member | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: 会员享更多云盘高速下载流量，根据不同的会员等级，可使用的下载流量也有所不同，超级会员等级最高12TB/月，超级会员等级1-3：2TB/月、超级会员等级4-6：6TB/月，超级会员等级7-10：12TB/月、白金会员：1TB/月、非会员：5GB/月
  - [1] 2026-11-03: the vendor speed table lists 15.8 MB/s, 7.82 MB/s and 586 KB/s | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: 15.8 MB/s 7.82 MB/s 586 KB/s
  - [1] 2026-11-03: the vendor privilege table lists recycle-bin retention of 60, 30, 15 and 10 days across the four columns | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: | [云盘回收站](https://vip.xunlei.com/vip_service/tqzy/index.html#icon-Recycle?referfrom=v_pc_hygw_ggong_privi_summary) | 保留60天 | 保留30天 | 保留15天 | 保留10天 |
  - [1] 2026-11-03: the vendor privilege table lists cloud space 12T, 6T, 3T and 10GB across the four columns | capture: sha256:0c2db2af81ddc82ead7718a99560296ab9e221b318a5472f7620fd3ce1bb59c8 | quote: | 云盘特权 | [云盘空间](https://vip.xunlei.com/vip_service/tqzy/index.html#icon-yuncloud?referfrom=v_pc_hygw_ggong_privi_summary) | 12T | 6T | 3T | 10GB |
  - [3] 2026-11-03: the third-party article lists 12TB drive, 1000 cloud-adds a day, 10TB monthly retrieval, 240G/day and 1T/month upload, 60-day recycle bin | capture: sha256:69d452c3d35360f6be5e1f26dd7a639c3a834a75cd5666927acb334ec8cf5306 | quote: 云盘空间达12TB，云添加次数为1000次/天，单次可上传500个文件，月度支持10TB云盘高速取回，文件上传流量为240G/天、1T/月，还支持超级通道、10个并行下载，云盘回收站保留60天
  - [4] 2026-11-03: a price index lists the 30-month card at 298 yuan | capture: sha256:eabfb39b3b42286751d19afa575d44f30b02a60a6afc39550e71245eb98bbf58 | quote: ¥298 / 30个月（合 ¥9.9/月） · 迅雷官方旗舰店 · 京东购买
  - [2] 2026-11-03: the article lists the 30-month card at 298 yuan after the coupon | capture: sha256:57025f72ae72146ce6c1828ef192735ea79c462b84a8ad83ac8ff11f11c91b2e | quote: 11.11 大促期间，30 个月券后直降至 298 元，单月约合 9.93 元官方好价：
- sources:
  - [1] https://vip.xunlei.com/vip_service/supervip_info/dist/
  - [2] https://www.ithome.com/1/012/491.htm
  - [3] https://finance.sina.com.cn/roll/2026-05-15/doc-inhxycci6175908.shtml
  - [4] https://vip.qust.me/deals

## baidu pan

- `storage/baidu-pan` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:34:56.914Z (live) | stale on 2026-11-18
- url https://www.ithome.com/0/511/746.htm
- free tier: New accounts get 5GB of base free storage; tasks and activities add more. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: country-phone
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: Paid SVIP membership gives 5T of space for the length of the subscription; the SVIP price is not on the captured first-party page.
- reliability: A legacy 2T free allowance was cut to 100G from 2020-10-15 for accounts not logged in between 2018-12-25 and 2020-10-15; accounts logged in at least once keep 2T, and paid accounts are unaffected.
- notes: historically 2 TB free, but the free allowance was cut to 100 GB for accounts not logged in for two years (2020 announcement). Endpoint and open-platform quota API exist but registration…
- evidence note: Re-read on 2026-11-03: https://eyun.baidu.com/content/120945/ (new accounts normally get 5GB base free storage; the same page's FAQ gives 2TB as the usual base space), https://pan.baidu.com/buy/memberCenter (SVIP includes 5T), https://eyun.baidu.com/knowledge/bb8114b593e34901b2f38926a60f8f0c.html and https://eyun.baidu.com/content/862622/ (a mainland China phone number is the main registration condition), https://passport.baidu.com/v2/?reg (registration form asks for a phone number) and, third party, https://www.ithome.com/0/511/746.htm (2020 cut of the 2T allowance to 100G for accounts not logged in between 2018-12-25 and 2020-10-15). Confidence stays reported: the 5GB figure is contradicted on its own page and the legacy-cut claim rests on the third-party page.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: historically 2 TB free, but the free allowance was cut to 100 GB for accounts not logged in for two years (2020 announcement). Endpoint and open-platform quota API exist but registration…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: historically 2 TB free, but the free allowance was cut to 100 GB for accounts not logged in for two years (2020 announcement). Endpoint and open-platform quota API exist but registration…
  - [2] 2026-10-21: cited as the basis of the rejection: historically 2 TB free, but the free allowance was cut to 100 GB for accounts not logged in for two years (2020 announcement). Endpoint and open-platform quota API exist but registration req
  - [3] 2026-11-03: a newly registered account normally gets 5GB of base free storage | capture: sha256:70d67a81e6d03648b71de6ae338189297890d3915c90297f03cec4c47b461516 | quote: 新用户注册百度云盘后，通常会获得5GB的基础免费存储空间。
  - [3] 2026-11-03: the base free allowance is stated in GB | capture: sha256:70d67a81e6d03648b71de6ae338189297890d3915c90297f03cec4c47b461516 | quote: 新用户注册百度云盘后，通常会获得5GB的基础免费存储空间。
  - [3] 2026-11-03: the free allowance is storage space | capture: sha256:70d67a81e6d03648b71de6ae338189297890d3915c90297f03cec4c47b461516 | quote: 新用户注册百度云盘后，通常会获得5GB的基础免费存储空间。
  - [4] 2026-11-03: the SVIP membership includes 5T of space | capture: sha256:b8ee6b0678bb98ddd04dff3ac8a0a3a673a1ac60037bc51b2e49d7553f39c130 | quote: 百度网盘为SVIP会员全面地提供极致的服务，包括5T超大空间
  - [1] 2026-11-03: the 2020 notice cut the 2T free space to 100G for accounts not logged in during the window | capture: sha256:5530ebd63ad9bded3f4e347e494cf65394af4a9d5a08fe5702b079c1bd52d9d4 | quote: 2018 年 12 月 25 日至 2020 年 10 月 15 日期间，未登录过百度网盘帐号的用户，2T 免费存储空间将从 2020 年 10 月 15 日开始调整为 100G
  - [5] 2026-11-03: registration mainly supports mainland China phone numbers | capture: sha256:cc9ed449726e7c85052e336d15db0f2af71bc41a0b445fd656644ab3e7e115d2 | quote: 目前百度网盘主要支持中国大陆手机号
  - [3] 2026-11-03: the base free allowance for new accounts is 5GB | capture: sha256:70d67a81e6d03648b71de6ae338189297890d3915c90297f03cec4c47b461516 | quote: 新用户注册百度云盘后，通常会获得5GB的基础免费存储空间。
  - [6] 2026-11-03: registration is conditioned mainly on a mainland China phone number | capture: sha256:03fd897ac38b9809811f3f911164d1b1d3741b60d7271d9717bc80a026f8f116 | quote: 百度企业网盘和百度网盘均以中国大陆手机号为主要注册条件
  - [7] 2026-11-03: the registration form asks for a phone number, with no email field | capture: sha256:cbd2f0650bf3512eba5bcddf6ebcaa7e1cdacb6e4b74379432ab9ff74e5790aa | quote: 手机号 可用于登录和找回密码
- sources:
  - [1] https://www.ithome.com/0/511/746.htm
  - [2] https://pan.baidu.com/
  - [3] https://eyun.baidu.com/content/120945/
  - [4] https://pan.baidu.com/buy/memberCenter
  - [5] https://eyun.baidu.com/knowledge/bb8114b593e34901b2f38926a60f8f0c.html
  - [6] https://eyun.baidu.com/content/862622/
  - [7] https://passport.baidu.com/v2/?reg
