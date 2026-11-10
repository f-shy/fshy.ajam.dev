# Emload

> emload.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/emload/ | JSON https://fshy.ajam.dev/api/v1/entity/emload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Emload

- `debrid/emload` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (Korean-market, premium subscription) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://www.emload.com/v2/
- price EUR 17.95 per month for 1 TB stored and 35 GB/day | parsed USD 20.09/TB-mo
- free tier: No free plan is listed in the plan block; the page opens directly at '1 Month €17.95 - 1 TB Storage - 35GB/Daily Bandwidth'. | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: An account is free to create ('Create Account'), but every listed plan is paid and the daily bandwidth figure is part of the paid plan.
- per-object cap: not stated on the page read | source: [1]
- retention: not stated on the page read | source: [1]
- egress: Each plan carries the same '35GB/Daily Bandwidth', which is a download allowance rather than a throttle. 35 GB/day is about 1.05 TB per 30 days. | metered: yes | free allowance: none | source: [1]
- identity: card | detail: Account creation is free; premium is bought at checkout. The page does not state which card processors are used, and the signup form fields were not read.
- interface: unknown
- limits:
  - volume-quota (binding): 35 GB per day of download bandwidth on every plan [1]
  - volume-quota (binding): 1 TB of storage on every plan [1]
- limits note: The daily bandwidth is identical across 1-month, 3-month, 6-month and 1-year plans; only the price per day changes. Nothing on the page suggests the allowance scales with price.
- binding note: 35 GB/day is the hard wall: 1 TiB of monthly transfer needs 34.1 GB/day sustained, which leaves 0.9 GB/day of headroom and no room for a retry. The 1 TB storage figure is the same number as the monthly transfer, so both walls arrive together.
- interface detail: Web upload and share. The page lists no API, FTP or remote-upload path.
- tooling: Browser only as read. Leechall lists emload with a 250 MB/day cap, the smallest on that list, so a leecher is not a practical substitute.
- composes with: One of the Korean-market hosts ('Webhard') that hold releases which never appear on the Western hosts. 35 GB/day covers 1 TiB of monthly transfer only if the month is exactly 30 days of full use, so it is a top-up rather than a bulk path.
- reliability: A bandwidth counter that resets daily means an unused day is lost, and a plan that runs at 35 GB/day exactly has no margin for a re-download.
- notes: Kshared publishes the identical plan at the identical price ('1 Month €17.95, 1 TB Storage, 35GB/Daily Bandwidth', 'Choose Your CloudFLA Plan'), which is one operator or one white-label script. The annual plan is €107.95, or €8.99 a month.
- evidence note: Price and plan terms read on the vendor page. The Korea-specific host list and the real per-file cap are not in this record.
- extras:
  - plans: 1 month €17.95; 3 months €43.95; 6 months €70.95; 1 year €107.95
  - annual_effective_monthly: EUR 8.99
  - twin_site: kshared.com
- evidence:
  - [1] 2026-10-23: the plan block: 1 Month €17.95, 3 Months €43.95, 6 Months €70.95, 1 Year €107.95, each with '1 TB Storage' and '35GB/Daily Bandwidth'
  - [2] 2026-10-23: a third-party leecher's cap for the host: 'emload.com 0 B / 250 MB /d'
- sources:
  - [1] https://www.emload.com/v2/
  - [2] https://leechall.com/
