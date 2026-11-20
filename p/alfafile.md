# Alfafile

> alfafile.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alfafile/ | JSON https://fshy.ajam.dev/api/v1/entity/alfafile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Alfafile

- `debrid/alfafile` | qualifies | evidence documented | binding volume-quota | category premium file host (one-click hoster), retrieval target | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://alfafile.net/premium
- price USD 14.99 per TiB-month on the 30-day 1 TB plan; the 90-day 4 TB plan is USD 10.00 per TiB-month | parsed USD 9.09/TB-mo
- free tier: No free download allowance is published; the site sells '3.00 TB space as free user' of storage, which is a storage figure and not a download one. | unit: mixed | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: upload/download up to 50 GB per file on premium | bytes: 50000000000 | source: [1]
- retention: not stated on the premium page | source: [1]
- egress: Premium is sold as a bandwidth block with storage attached: '1 TB bandwidth / 1 TB storage' at each price point, plus 'Unlimited simultaneous downloads'. | metered: yes | free allowance: 1 TB per 30-day plan at the entry price (exactly 1 TiB of bytes: quota 1099511627776) | price per TB: no per-GB overage; buy the next bandwidth block | source: [1]
- identity: email | detail: E-mail signup for the account and token; payment by card.
- interface: rest
- limits:
  - volume-quota (binding): 1 TB of download bandwidth per 30-day plan [1]
  - per-object-cap: 50 GB per file on premium [1]
  - per-ip-shaping: free tier measured near 50 KB/s = 0.0477 MiB/s [2]
- limits note: Bandwidth is consumed by downloads only; storage is a separate figure on the same plan.
- binding note: One 30-day plan is exactly one TiB of bytes, so the counter lands at the monthly requirement with nothing spare.
- interface detail: 'To use Alfafile API you require ... an access token ... by using either of the Alfafile API user/login method'; client libraries are published at /api/doc/library.
- endpoint: https://alfafile.net/api
- tooling: documented JSON REST API with token login and client libraries; JDownloader 2 measured 60 MiB/s on a paid account
- composes with: The only one of the 30-day 1 TiB hosts with a documented public API, so it can be driven headlessly where Rapidgator would need the site.
- reliability: The API blocks an IP after repeated wrong passwords; the vendor asks callers to stop retrying after three failures.
- notes: Priced identically to Rapidgator's 1 TB / 30 day plan with a published API and the fastest measured throughput in the 2026 test. Its weakness is coverage: the same test calls its file availability narrower than Rapidgator.
- evidence note: Prices, plan shape and API are from the vendor pages read. The free-tier speed is third-party only.
- extras:
  - free_speed_mib_s: 0.0477
  - premium_parallel: unlimited
  - max_file_premium: 50 GB
  - api: yes
  - price_30d_usd: 14.99
  - price_ladder_reported: USD 14.99 / 30 days for 1 TB bandwidth; USD 19.99 / 30 days for 2 TB; USD 39.99 / 30 days for 4 TB; longer plans from USD 39.99 / 90 days for 4 TB
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: USD 14.99/30d 1 TB bandwidth + 1 TB storage; 19.99/2 TB; 39.99/4 TB; 'Unlimited simultaneous downloads'; 'Upload/Download files up to 50 GB'
  - [3] 2026-10-23: 'To use Alfafile API you require the following: A alfafile account ... Access Token ... by using either of the Alfafile API user/login method'
  - [2] 2026-10-23: fastest host in the July 2026 test at ~60 MiB/s in JD2; free tier ~50 KB/s
- sources:
  - [1] https://alfafile.net/premium
  - [2] https://filehostreviews.com/best-file-hosting-services/
  - [3] https://alfafile.net/api/doc
