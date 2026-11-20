# ParsGet

> parsget.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/parsget/ | JSON https://fshy.ajam.dev/api/v1/entity/parsget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ParsGet (پارس‌گت)

- `debrid/parsget` | qualifies-with-caveat | evidence documented | binding volume-quota | category premium-link generator / multi-hoster (Iran; file hosts, torrent and usenet, Iranian download server) | tier basic
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:17:21.000Z (live) | stale on 2026-11-23
- url https://parsget.com/
- price Toman 3,480,000 per TB-month equivalent (Basic: 348,000 Toman for 100 GB/month)
- free tier: Free plan: 3 GB per day, 3 links per day, 1.5 GB maximum file size, one day of file retention, Netherlands download server, limited site list. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The pricing table is in Persian numerals and Toman. Paid plans are 348,000 / 748,000 / 1,398,000 Toman per month for 100 / 300 / 600 GB.
- per-object cap: 1.5 GB on the free plan; 'unlimited' (نامحدود) on Basic, Pro and Ultra. | bytes: 1500000000 | source: [1] | note: The vendor writes ۱٫۵ گیگابایت; decimal GB is assumed, not probed.
- retention: Free 1 day, Basic 5 days, Pro 15 days, Ultra 30 days (row 'نگهداری فایل'). | days: 1 | source: [1]
- egress: Traffic is the billed unit: 3 GB/day on the free plan and 100/300/600 GB per month on Basic/Pro/Ultra, counted when the file is downloaded. The pricing footnote says a premium site can draw more than one unit per GB ('ضریب مصرف از سایت‌های پریمیوم ممکنه متفاوت باشه'). | metered: yes | free allowance: 3 GB/day | source: [1]
- identity: email | detail: Registration is an account on panel.parsget.com/auth/register. The form itself was not opened in on 2026-10-23, so email as the minimum is inferred from the existence of a password panel, not observed.
- interface: webdav
- limits:
  - volume-quota (binding): 100 GB/month on Basic, 300 GB on Pro, 600 GB on Ultra [1]
  - request-rate: 3 links/day free, 50 on Basic, 100 on Pro, 300 on Ultra [1]
  - per-object-cap: 1.5 GB per file on the free plan only [1]
  - retention-clamped: 1 day on the free plan, 5/15/30 days on Basic/Pro/Ultra [1]
- limits note: The table's footnote attaches a per-host multiplier to premium sites, so a nominal 100 GB can be consumed by fewer than 100 GB of download.
- binding note: At 1 TiB/month the top plan is exhausted at 600 GB, and the premium-site multiplier makes the effective ceiling lower than the printed number.
- interface detail: WebDAV is listed as active from Basic upward ('WebDAV: فعال'); Ultra adds 'همه اتصال‌های ابری'. Download links are plain HTTPS from dl.parsget.com. No public API page was found.
- tooling: WebDAV mount through rclone or any WebDAV client on paid plans; a browser extension ('افزونه مرورگر'). No vendor CLI, SDK or rclone backend documented.
- composes with: Replaces a shelf of file-host premium accounts for an Iranian client: the file is pulled once into the vendor's Iranian server and then downloaded on domestic half-price traffic.
- reliability: Everything is drawn against a traffic balance; the per-host multiplier changes the burn rate, and the service is Iranian-hosted, so its international links are the first thing to degrade under filtering or cross-border restrictions.
- notes: The strongest native multi-hoster found in the region: torrent, usenet and hosted file hosts behind one Persian-language account, priced only in Toman. The checkout gateway was not read, so the payment rail is inferred from the market (Iranian shops bill through Shaparak) rather than observed here. Absence of a public API is a tooling note, not a verdict: WebDAV is the programmatic path.
- evidence note: The plan table and the footnote were read on parsget.com/pricing today. What would raise it: a signed-in panel reading that names the checkout gateway and prints the multiplier per host.
- evidence:
  - [2] 2026-10-23: The service converts links from 50+ sites, includes torrent and usenet, and bills on 'ترافیک داخلی (نیم‌بها)' with a dl.parsget.com direct link
  - [1] 2026-10-23: All four plan columns: 3 GB/day free; 100/300/600 GB/month at 348,000/748,000/1,398,000 Toman; 1.5 GB file cap on free; 1/5/15/30 day retention; WebDAV from Basic
- sources:
  - [1] https://parsget.com/pricing
  - [2] https://parsget.com/
