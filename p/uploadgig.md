# UploadGIG

> uploadgig.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploadgig/ | JSON https://fshy.ajam.dev/api/v1/entity/uploadgig.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UploadGIG

- `debrid/uploadgig` | qualifies-with-caveat | evidence documented | binding volume-quota | category premium file host (one-click hoster), retrieval target | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://uploadgig.com/premium
- price USD 7.33 per TiB-month at the 30-day plan (USD 20.00 for 2.73 TiB of allowance), USD 4.22 at 365 days | parsed USD 6.67/TB-mo
- free tier: No free allowance is published on the premium page; the page sells only the paid tier ('30Days 20.00 USD ... 100 GB daily traffic'). Free-mode behaviour is known only from a third-party measurement: 30.0 KB/s in Chrome. | unit: mixed | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not established for the free tier; the premium page sells speed, not size | source: [1]
- retention: not established; the premium page states no retention window | source: [1]
- egress: Premium is sold as '100 GB daily traffic' with 'Max download speed', 'Parallel downloads' and 'No waiting time'. Traffic is metered by design and the daily allowance is the product. | metered: yes | free allowance: 100 GB/day on every premium plan (93.13 GiB/day, 2.73 TiB/30d) | price per TB: no overage price published; the next plan up is the only way to buy more | source: [1]
- identity: email | detail: Account is an e-mail signup. Payment is by card or crypto through the vendor's payment page; no phone or identity document is asked for.
- interface: unknown
- limits:
  - volume-quota (binding): 100 GB/day of premium download traffic [1]
  - per-ip-shaping: free tier measured at 30.0 KB/s = 0.0286 MiB/s [2]
- limits note: The vendor publishes no free-tier number at all; the only free figure is a third-party browser measurement.
- binding note: At 1 TiB/month the 100 GB/day allowance is 2.7x the requirement, so the first thing to fail is the daily counter only if usage bursts; otherwise the price does.
- interface detail: No public API documentation was found on the site on 2026-10-23. JDownloader 2 works against it per the 2026 third-party test.
- tooling: JDownloader 2 (37.8 MB/s combined in the July 2026 test); browser premium 14.4 MB/s
- composes with: A 100 GB/day key covers one TiB a month with 2.7x headroom, so it composes as a paid fallback when a link is UploadGIG-only and no debrid covers it.
- reliability: Free mode is throttled to roughly 30 KB/s and carries waiting and ads; premium removes both. Upload fails are retried by JDownloader 2 without special handling.
- notes: Kept as the cheapest per-TiB host in the 30-day bracket that is not a video host. Its weakness is coverage, not price: the 2026 test ranks it 9th of 12 and calls it a budget pick.
- evidence note: Price and daily allowance are from the vendor premium page read. The free-tier speed is third-party. A paid download through the vendor API would raise it to measured.
- extras:
  - free_speed_mib_s: 0.0286
  - premium_parallel: unlimited ('Parallel downloads')
  - max_file_premium: not published
  - api: no
  - price_30d_usd: 20.0
  - price_ladder_reported: USD 20.00 / 30 days; USD 50.00 / 90 days; USD 80.00 / 180 days; USD 140.00 / 365 days
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: USD 20.00/30 days, 50.00/90, 80.00/180, 140.00/365, '100 GB daily traffic', 'Max download speed', 'Parallel downloads', 'No waiting time'
  - [2] 2026-10-23: third-party July 2026 test: JD2 37.8 MB/s combined, browser premium 14.4 MB/s, free 30.0 KB/s
- sources:
  - [1] https://uploadgig.com/premium
  - [2] https://filehostreviews.com/best-file-hosting-services/
