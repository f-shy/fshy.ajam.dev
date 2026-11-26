# FileJoker

> filejoker.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filejoker/ | JSON https://fshy.ajam.dev/api/v1/entity/filejoker.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileJoker

- `debrid/filejoker` | qualifies-with-caveat | evidence documented | binding volume-quota | category premium file host (one-click hoster), retrieval target | tier premium-vip
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:58.091Z (live) | stale on 2026-12-26
- url https://filejoker.net/premium
- price USD 20.74 per TiB-month on VIP (USD 33.95 for 1.64 TiB of allowance); USD 22.95 buys only 0.33 TiB on the base plan | parsed USD 18.86/TB-mo
- free tier: Free tier is measured, not published: 125-130 KB/s in Chrome in the July 2026 test, which the tester called the slowest usable free tier in the set. | unit: mixed | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: 'Unlimited File Size' is a VIP-only benefit; the base premium column does not list it | source: [1]
- retention: not published on the premium page | source: [1]
- egress: Traffic is sold in 5-day windows, not per day: 60 GB or 300 GB 'of traffic in any 5 days'. Speed is 'Unlimited Speed' on both paid tiers. | metered: yes | free allowance: 60 GB / 5 days on Premium (12 GB/day, 0.33 TiB/30d); 300 GB / 5 days on VIP (60 GB/day, 1.64 TiB/30d) | price per TB: no overage price; the only lever is VIP | source: [1]
- identity: email | detail: E-mail signup; card and crypto payment.
- interface: browser
- limits:
  - volume-quota (binding): 60 GB per 5 days on Premium, 300 GB per 5 days on VIP [1]
  - per-ip-shaping: free tier measured at 125-130 KB/s = 0.119-0.124 MiB/s [2]
- limits note: The 5-day window is not a daily counter; an unused part of a window cannot be carried into the next.
- binding note: The base premium plan clears only a third of 1 TiB a month, so the choice is VIP or nothing, and VIP's counter is what decides the month.
- interface detail: No API page found. The K2S-family sites publish a separate API, but FileJoker's own premium page does not reference one.
- tooling: JDownloader 2 (12.62 MB/s combined in the July 2026 test); iOS and Android apps
- composes with: Only worth a key when the archive is FileJoker-hosted; VIP is the tier that reaches one TiB a month, at roughly four times 1fichier's rate.
- reliability: Free downloads are 0.12 MiB/s, which is a 102-day transfer for one TiB; the paid tiers are the only usable path.
- notes: The 5-day window is the unusual part: a client that pulls 200 GB in one weekend and nothing for three weeks is inside VIP's allowance, while a steady 40 GB/day is not. No programmatic path found: No API page found. The K2S-family sites publish a separate API, but FileJoker's own premium page does not reference one.
- evidence note: Price, tier structure and the 5-day traffic windows are from the vendor premium page read. The free-tier speed is third-party.
- extras:
  - free_speed_mib_s: 0.1216
  - premium_parallel: not published
  - max_file_premium: unlimited on VIP only
  - api: no
  - price_30d_usd: 33.95
  - price_ladder_reported: Premium USD 22.95 / month with 60 GB of traffic in any 5 days; Premium VIP USD 33.95 / month with 300 GB in any 5 days
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: Premium $22.95/mo '60.000 MB of traffic in any 5 days'; Premium VIP $33.95/mo '300.000 MB of traffic in any 5 days'; 'Unlimited File Size' listed under VIP
  - [2] 2026-10-23: JD2 12.62 MB/s combined, browser 11.8 MB/s, free 125-130 KB/s
  - [1] 2026-11-25: Premium includes 60.000 MB of traffic in any 5 days | capture: sha256:da1d7fd63d5d375d66495af0bfe301d87745185d944594220acdf172879cb56e | quote: 60.000 MB of traffic in any 5 days
  - [1] 2026-11-25: Premium VIP includes 300.000 MB of traffic in any 5 days | capture: sha256:da1d7fd63d5d375d66495af0bfe301d87745185d944594220acdf172879cb56e | quote: 300.000 MB of traffic in any 5 days
  - [1] 2026-11-25: Unlimited File Size is listed as a VIP benefit | capture: sha256:da1d7fd63d5d375d66495af0bfe301d87745185d944594220acdf172879cb56e | quote: Unlimited File Size
  - [3] 2026-11-25: the signup form asks for an email address | capture: sha256:200f5198df3e000ba4f5e75847973ec36e552d59e9188730b74384084716588b | quote: <label for="inputEmail">Email:</label>
- sources:
  - [1] https://filejoker.net/premium
  - [2] https://filehostreviews.com/best-file-hosting-services/
  - [3] https://filejoker.net/
