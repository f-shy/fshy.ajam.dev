# ParsGet

> parsget.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/parsget/ | JSON https://fshy.ajam.dev/api/v1/entity/parsget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ParsGet (پارس‌گت)

- `debrid/parsget` | qualifies-with-caveat | evidence documented | binding volume-quota | category premium-link generator / multi-hoster (Iran; file hosts, torrent and usenet, Iranian download server) | tier basic
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:47:00.044Z (live) | stale on 2026-12-26
- url https://parsget.com/
- price Toman 1,940,000 per TB-month equivalent (Basic: 194,000 Toman for 100 GB/month)
- free tier: Free plan: 3 GB per day, 3 links per day, 1.5 GB maximum file size, 1 day of file retention, Netherlands download server, limited site list. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The pricing table is in Persian numerals and Toman. Basic is 194,000 Toman per month for 100 GB, and Pro and Ultra carry 250 GB and 470 GB per month.
- per-object cap: 1.5 GB on the free plan; 'unlimited' (نامحدود) on Basic, Pro and Ultra. | bytes: 1500000000 | source: [1] | note: The vendor writes ۱٫۵ گیگابایت; decimal GB is assumed, not probed.
- retention: Free 1 day, Basic 5 days, Pro 15 days, Ultra 30 days (row 'نگهداری فایل'). | days: 1 | source: [1]
- egress: Traffic is the billed unit: 3 GB/day on the free plan and 100/250/470 GB per month on Basic/Pro/Ultra, counted when the file is downloaded. The pricing footnote says a premium site can draw more than one unit per GB ('ضریب مصرف از سایت‌های پریمیوم ممکنه متفاوت باشه'). | metered: yes | free allowance: 3 GB/day; 100/250/470 GB per month on Basic/Pro/Ultra | source: [1]
- identity: email | detail: Registration is an account on panel.parsget.com/auth/register; the form accepts a phone number or an email address, so email as the minimum is stated by the register page rather than inferred.
- interface: webdav
- limits:
  - volume-quota (binding): 100 GB/month on Basic, 250 GB on Pro, 470 GB on Ultra [1]
  - request-rate: 3 links/day free, 50 on Basic, 100 on Pro, 300 on Ultra [1]
  - per-object-cap: 1.5 GB per file on the free plan only [1]
  - retention-clamped: 1 day on the free plan, 5/15/30 days on Basic/Pro/Ultra [1]
- limits note: The table's footnote attaches a per-host multiplier to premium sites, so a nominal 100 GB can be consumed by fewer than 100 GB of download.
- binding note: At 1 TiB/month the top plan is exhausted at 470 GB, and the premium-site multiplier makes the effective ceiling lower than the printed number.
- interface detail: WebDAV is listed as active from Basic upward ('WebDAV: فعال'); Ultra adds 'همه اتصال‌های ابری'. Download links are plain HTTPS from dl.parsget.com. No public API page was found.
- tooling: WebDAV mount through rclone or any WebDAV client on paid plans; a browser extension ('افزونه مرورگر'). No vendor CLI, SDK or rclone backend documented.
- composes with: Replaces a shelf of file-host premium accounts for an Iranian client: the file is pulled once into the vendor's Iranian server and then downloaded on domestic half-price traffic.
- reliability: Everything is drawn against a traffic balance; the per-host multiplier changes the burn rate, and the service is Iranian-hosted, so its international links are the first thing to degrade under filtering or cross-border restrictions.
- notes: The strongest native multi-hoster found in the region: torrent, usenet and hosted file hosts behind one Persian-language account, priced only in Toman. The checkout gateway was not read, so the payment rail is inferred from the market (Iranian shops bill through Shaparak) rather than observed here. Absence of a public API is a tooling note, not a verdict: WebDAV is the programmatic path.
- evidence note: The plan table and the footnote were read on parsget.com/pricing today. What would raise it: a signed-in panel reading that names the checkout gateway and prints the multiplier per host.
- evidence:
  - [2] 2026-10-23: The service converts links from 50+ sites, includes torrent and usenet, and bills on 'ترافیک داخلی (نیم‌بها)' with a dl.parsget.com direct link
  - [1] 2026-10-23: All four plan columns: 3 GB/day free; 100/300/600 GB/month at 348,000/748,000/1,398,000 Toman; 1.5 GB file cap on free; 1/5/15/30 day retention; WebDAV from Basic
  - [1] 2026-11-25: free traffic is 3 GB/day; Basic, Pro and Ultra are 100/250/470 GB per month | capture: sha256:092aca2df4c3f5538ab77c8adebb160c0b1918fa6ccbe4e59f5ab36f24828d94 | quote: | ترافیک | روزانه ۳ گیگابایت | ۱۰۰ گیگابایت / ماه | ۲۵۰ گیگابایت / ماه | ۴۷۰ گیگابایت / ماه |
  - [1] 2026-11-25: daily link counts are 3 on free, 50 Basic, 100 Pro, 300 Ultra | capture: sha256:092aca2df4c3f5538ab77c8adebb160c0b1918fa6ccbe4e59f5ab36f24828d94 | quote: | لینک روزانه | ۳ | ۵۰ | ۱۰۰ | ۳۰۰ |
  - [1] 2026-11-25: the free per-file cap is 1.5 GB and paid plans are unlimited | capture: sha256:092aca2df4c3f5538ab77c8adebb160c0b1918fa6ccbe4e59f5ab36f24828d94 | quote: | حداکثر حجم هر فایل | ۱٫۵ گیگابایت | نامحدود | نامحدود | نامحدود |
  - [1] 2026-11-25: file retention is 1/5/15/30 days across free/Basic/Pro/Ultra | capture: sha256:092aca2df4c3f5538ab77c8adebb160c0b1918fa6ccbe4e59f5ab36f24828d94 | quote: | نگهداری فایل | ۱ روز | ۵ روز | ۱۵ روز | ۳۰ روز |
  - [1] 2026-11-25: WebDAV is active from Basic upward and absent on free | capture: sha256:092aca2df4c3f5538ab77c8adebb160c0b1918fa6ccbe4e59f5ab36f24828d94 | quote: | WebDAV | ندارد | فعال | فعال | فعال |
  - [1] 2026-11-25: premium-site traffic can be consumed at a different coefficient | capture: sha256:092aca2df4c3f5538ab77c8adebb160c0b1918fa6ccbe4e59f5ab36f24828d94 | quote: ترافیک نمایش‍اده‌شده معادل مصرف سایت‌های پایه هست؛ ضریب مصرف از سایت‌های پریمیوم ممکنه متفاوت باشه.
  - [2] 2026-11-25: the service converts links from 50+ services with half-price domestic traffic | capture: sha256:edbfe1177a889c5e2ffb45ab1e3760c6ed883e81c632954f1dd2b1013b046402 | quote: دانلود پرسرعت از ۵۰+ سرویس مختلف با ترافیک داخلی (نیم‌bها)؛
  - [3] 2026-11-25: registration accepts a phone number or an email address | capture: sha256:5cde5cbfaedb400839578d4dba5bb25ec41ce351154c189b6852467393d58687 | quote: شماره موبایل یا ایمیل
- sources:
  - [1] https://parsget.com/pricing
  - [2] https://parsget.com/
  - [3] https://panel.parsget.com/auth/register
