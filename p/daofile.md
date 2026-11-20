# DaoFile

> daofile.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/daofile/ | JSON https://fshy.ajam.dev/api/v1/entity/daofile.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DaoFile

- `debrid/daofile` | fails-quota | evidence documented | binding volume-quota | category premium file host (one-click hoster), retrieval target | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://daofile.com/?op=payments
- price USD 43.87 per TiB-month if the allowance is 50 GB per 3 days; USD 14.7 if it is 50 GB per day. The page is ambiguous and the worse reading is recorded. | parsed USD 39.9/TB-mo
- free tier: Free downloads run through a capped 'free download flow' with speed caps and waiting; the vendor names no free allowance in bytes. | unit: mixed | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not published on the payment page | source: [1]
- retention: not published on the payment page | source: [1]
- egress: '50 GB traffic - Premium traffic refreshes every 3 days' is the whole premium allowance; speed is 'Unlimited speed - No speed caps from the free download flow'. | metered: yes | free allowance: 50 GB per 3 days (16.7 GB/day, 500 GB/30d = 0.46 TiB) on the conservative reading | price per TB: no overage price; the only lever is a longer plan | source: [1]
- identity: email | detail: E-mail signup; card, crypto and a Japan-facing reseller are the payment routes named on the page.
- interface: unknown
- limits:
  - volume-quota (binding): 50 GB of premium traffic, refreshed every 3 days [1]
  - per-ip-shaping: free flow is speed-capped; no number published [1]
- limits note: The refresh interval is stated as 3 days, not 1. Read literally that is 500 GB a month, less than half the requirement.
- binding note: Even on the generous reading of 50 GB/day the plan clears 1 TiB; on the literal 3-day reading it needs a second purchase inside the month, which is what fails first.
- interface detail: Payment page is an XFileSharing-style grid; no API page found.
- tooling: browser; no download-manager documentation found
- composes with: Cannot carry one TiB a month on the conservative reading of its allowance, so it is a spot purchase for a specific file, not a monthly key.
- reliability: A 3-day traffic refresh means a burst is lost, not queued: unused allowance does not roll over.
- notes: The verdict is taken on the literal reading. A dashboard reading after one purchase confirms the threshold; until then the conservative number stands.
- evidence note: Prices and the 50 GB / 3 days sentence are from the vendor payment page read. Whether the refresh is per day or per three days is unresolved and is the single fact that decides the verdict.
- extras:
  - free_daily_cap_gib: 16.67
  - premium_parallel: not published
  - max_file_premium: not published
  - api: no
  - price_30d_usd: 19.95
  - price_ladder_reported: USD 19.95 / 30 days; USD 39.95 / 90 days; USD 89.95 / 365 days; USD 129.95 / 999 days
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: USD 19.95/30d, 39.95/90d, 89.95/365d, 129.95/999d; '50 GB traffic - Premium traffic refreshes every 3 days'; 'Unlimited speed'
- sources:
  - [1] https://daofile.com/?op=payments
