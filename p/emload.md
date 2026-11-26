# Emload

> emload.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/emload/ | JSON https://fshy.ajam.dev/api/v1/entity/emload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Emload

- `debrid/emload` | qualifies-with-caveat | evidence documented | binding volume-quota | category file host (Korean-market, premium subscription) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:46:38.368Z (live) | stale on 2026-12-26
- url https://www.emload.com/v2/
- price EUR 17.95 per month for 1 TB stored and 35 GB/day | parsed USD 20.22/TB-mo
- free tier: No free plan is listed in the plan block; the page opens directly at '1 Month €17.95 - 1 TB Storage - 35GB/Daily Bandwidth'. | unit: TB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: An account is free to create ('Create Account'), but every listed plan is paid and the daily bandwidth figure is part of the paid plan.
- per-object cap: not stated on the page read | source: [1]
- retention: not stated on the page read | source: [1]
- egress: Each plan carries the same '35GB/Daily Bandwidth', which is a download allowance rather than a throttle. 35 GB/day is about 1.05 TB per 30 days. | metered: yes | free allowance: none | source: [1]
- identity: card | detail: Account creation is free through a 'Create Account' sign-up page; premium is bought at checkout. No card processor is named on the page read.
- interface: browser
- limits:
  - volume-quota (binding): 35 GB per day of download bandwidth on every plan [1]
  - volume-quota (binding): 1 TB of storage on every plan [1]
- limits note: The daily bandwidth is identical across 1-month, 3-month, 6-month and 1-year plans; only the price per day changes. Nothing on the page suggests the allowance scales with price.
- binding note: 35 GB/day is the hard wall: 1 TiB of monthly transfer needs 34.1 GB/day sustained, which leaves 0.9 GB/day of headroom and no room for a retry. The 1 TB storage figure is the same number as the monthly transfer, so both walls arrive together.
- interface detail: Web upload and share. The page lists no API, FTP or remote-upload path.
- tooling: Browser only as read. Leechall lists emload with a 250 MB/day cap, the smallest on that list, so a leecher is not a practical substitute.
- composes with: One of the Korean-market hosts ('Webhard') that hold releases which never appear on the Western hosts. 35 GB/day covers 1 TiB of monthly transfer only if the month is exactly 30 days of full use, so it is a top-up rather than a bulk path.
- reliability: A bandwidth counter that resets daily means an unused day is lost, and a plan that runs at 35 GB/day exactly has no margin for a re-download.
- notes: Kshared publishes the identical plan at the identical price ('1 Month €17.95, 1 TB Storage, 35GB/Daily Bandwidth', 'Choose Your CloudFLA Plan'), which is one operator or one white-label script. The annual plan is €107.95, or €8.99 a month. No programmatic path found: Web upload and share. The page lists no API, FTP or remote-upload path.
- evidence note: Price and plan terms read on the vendor page. The Korea-specific host list and the real per-file cap are not in this record.
- extras:
  - plans: 1 month €17.95; 3 months €43.95; 6 months €70.95; 1 year €107.95
  - annual_effective_monthly: EUR 8.99
  - twin_site: kshared.com
- evidence:
  - [1] 2026-10-23: the plan block: 1 Month €17.95, 3 Months €43.95, 6 Months €70.95, 1 Year €107.95, each with '1 TB Storage' and '35GB/Daily Bandwidth'
  - [2] 2026-10-23: a third-party leecher's cap for the host: 'emload.com 0 B / 250 MB /d'
  - [3] 2026-11-25: the sign-up page offers a Create Account action | capture: sha256:fe06cdaa01ee98c0af315f3820a0d98794c9ef541d83fe830e8539fb1e15e80b | quote: [Create Account](https://www.emload.com/v2/user/join?v=1795578141)
  - [1] 2026-11-25: every plan carries 35GB of daily download bandwidth | capture: sha256:c676793f968ad383e2e79ee9b8878435c0be048665c9ff4e7633ca8bdafcb810 | quote: ## 35GB/Daily Bandwidth
  - [1] 2026-11-25: every plan includes 1 TB of storage | capture: sha256:c676793f968ad383e2e79ee9b8878435c0be048665c9ff4e7633ca8bdafcb810 | quote: ## 1 TB Storage
  - [1] 2026-11-25: the 1-month plan is priced at EUR 17.95 | capture: sha256:c676793f968ad383e2e79ee9b8878435c0be048665c9ff4e7633ca8bdafcb810 | quote: ## €17.95
  - [2] 2026-11-25: a third-party leecher still lists emload as a supported host | capture: sha256:d8bf63f755d814642dc9a8e0b3c6a5e73d73009145cafcb9b09340ebcd64cf2f | quote: emload.com premium link generator
- sources:
  - [1] https://www.emload.com/v2/
  - [2] https://leechall.com/
  - [3] https://www.emload.com/v2/user/join
