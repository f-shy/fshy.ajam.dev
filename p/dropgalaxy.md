# DropGalaxy

> dropgalaxy.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dropgalaxy/ | JSON https://fshy.ajam.dev/api/v1/entity/dropgalaxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DropGalaxy

- `debrid/dropgalaxy` | fails-quota | evidence documented | binding retention-clamped | category premium file host (one-click hoster), retrieval target | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:57.800Z (live) | stale on 2026-12-04
- url https://dropgalaxy.com/?op=payments
- price USD 30.54 per TiB at 30 days (USD 50 for 60 GB/day x 30 days = 1.64 TiB); USD 15.06 per TiB at 365 days (USD 300 for 60 GB/day x 365 days = 19.92 TiB)
- free tier: Free: files deleted '1 days after last download', 1024 Kbytes/sec, 20 GB/day download volume. Registered: 20 days, 1024 Kbytes/sec, 30 GB/day, 300 GB storage. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: 'Max upload file size 68610 Mb' on premium (68.6 GB); 5120 Mb registered, 0.00001 Mb free as listed | bytes: 68610000000 | source: [1] | note: The terms page states 5 GB as the maximum downloadable file size for registered and anonymous users.
- retention: free files deleted 1 day after the last download; registered 20 days; premium 60 days | days: 1 | source: [1] | note: The terms page states that files of a free account must be downloaded once in 90 days or are deleted, against '1 days after last download' on the payment page.
- egress: Premium raises the daily download volume to 60 GB and the speed to 50480 Kbytes/sec (48.1 MiB/s). Free and registered share the same 1024 Kbytes/sec cap. | metered: yes | free allowance: 20 GB/day free, 30 GB/day registered, 60 GB/day premium | price per TB: none published | source: [1]
- identity: email | detail: E-mail signup; card and crypto through the host checkout.
- interface: webdav
- limits:
  - volume-quota: 60 GB/day on premium [1]
  - per-ip-shaping: 1024 Kbytes/sec = 0.98 MiB/s on free and registered [1]
  - retention-clamped (binding): free files deleted one day after the last download [1]
  - volume-quota: 60 GB/day on premium; 30 GB/day registered free; 20 GB/day anonymous [1]
  - per-ip-shaping: 1024 Kbytes/sec = 0.98 MiB/s on free and registered; 48.1 MiB/s claimed on premium [1]
- limits note: The free column's 'max upload file size 0.00001 Mb' is the vendor's own placeholder and should be read as 'no free upload', not as a number. The terms page states a different limit for registered and anonymous users: 300 kilobits per second, no more than 3 files per day and no more than 2 files per hour.
- binding note: At 1 TiB/month the 60 GB/day premium allowance is fine; what fails first is the one-day free retention, which makes the free tier unusable for a multi-part archive even before speed.
- interface detail: WebDAV support is stated on the home page; the payment page is a plain comparison grid, and no API page was found.
- tooling: download accelerators supported; torrent leech and remote URL upload listed as premium features
- composes with: The worst value in the sector per TiB and the shortest free retention (one day), so it is a host to treat as a last resort for monthly retrieval rather than a key to buy.
- reliability: Sharing a premium account blocks access immediately, per the payment page warning.
- notes: Two vendor surfaces disagree on the free numbers by a factor of four, which is why the verdict does not rest on them: the premium price per TiB is USD 30, five times the best host compared. At 365 days, the vendor's own 60 GB/day is 21,900 GB = 19.92 TiB, so the annual plan costs USD 15.06 per TiB-month; a figure of USD 20.6 per TiB-month implies 300 / 20.6 = 14.6 TiB. The difference is 27%, and it moves DropGalaxy from worst-in-class on the annual plan to mid-table.
- evidence note: The vendor's payment page was read directly on 2026-11-03: the comparison table and the plan prices are the page's own text. The terms page gives different free-user limits (see limits_note).
- extras:
  - free_speed_mib_s: 0.9766
  - free_daily_cap_gib: 18.63
  - premium_parallel: not published
  - max_file_premium: 68.6 GB
  - api: no
  - price_30d_usd: 50.0
  - price_ladder_reported: USD 50 / 30 days; USD 5 / 1 day; USD 20 / 7 days; USD 100 / 90 days; USD 200 / 180 days; USD 300 / 365 days
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: indexed render: free 1024 Kbytes/sec, 20 GB in 1 days, '1 days after last download'; registered 30 GB, 5120 Mb; premium 50480 Kbytes/sec, 60 GB in 1 days, 68610 Mb; 1 days $5, 7 days $20, 30 days $50, 90 days $100, 180 days $200, 365 days $300
  - [2] 2026-10-23: an older vendor table with different numbers (free 5 GB in 3 days), showing how fast these fields move
  - [1] 2026-10-23: Premium 60 GB/day at 50480 Kbytes/sec (48.1 MiB/s); free and registered 1024 Kbytes/sec; plan ladder USD 50 / 30 d, USD 5 / 1 d, USD 20 / 7 d, USD 100 / 90 d, USD 200 / 180 d, USD 300 / 365 d.
  - [1] 2026-11-03: the payment page text is read directly: the comparison table and plan prices are on the vendor page | capture: sha256:3ede819df217d4ebbbfa86c58067f278c18ba925e146b8aed673ffc57b3c40d5 | quote: 60 GB in 1 days
  - [1] 2026-11-03: the comparison table is read directly | capture: sha256:3ede819df217d4ebbbfa86c58067f278c18ba925e146b8aed673ffc57b3c40d5 | quote: 60 GB in 1 days
  - [3] 2026-11-03: the home page states WebDAV support | capture: sha256:d79167b3fdeb08acd3ff99ab6f99f5c8d1aa7b74110ddf8743e66b5615298015 | quote: We also provide support via WebDav protocol for Windows, Linux, MacOS, and Blackberry.
  - [4] 2026-11-03: the terms page gives a 5 GB downloadable file cap for registered and anonymous users | capture: sha256:8e36f1eb31393193f19a10833954cf11db6a1c9f9633c808591fa0ca11040071 | quote: The maximum size of downloadable files for registered users and users with no account is 5 GB.
  - [4] 2026-11-03: the terms page gives 90 days for a free account | capture: sha256:8e36f1eb31393193f19a10833954cf11db6a1c9f9633c808591fa0ca11040071 | quote: YOUR FILES FROM YOUR FREE ACCOUNT HAVE TO BE DOWNLOADED ONCE IN 90 DAYS.
  - [4] 2026-11-03: the terms page gives 300 kilobits per second, 3 files per day and 2 files per hour for registered and anonymous users | capture: sha256:8e36f1eb31393193f19a10833954cf11db6a1c9f9633c808591fa0ca11040071 | quote: You do agree with the fact that registered users and users with no account have the ability to download files at speeds not exceeding 300 kilobits per second, no more than 3 files per day and no more than 2 files per hour.
  - [1] 2026-11-03: premium allows 60 GB per day; the plan prices USD 50 for 30 days and USD 300 for 365 days are on the same page | capture: sha256:3ede819df217d4ebbbfa86c58067f278c18ba925e146b8aed673ffc57b3c40d5 | quote: 60 GB in 1 days
  - [1] 2026-11-03: premium storage is 5000 GB on the payment page, against 300 GB registered | capture: sha256:3ede819df217d4ebbbfa86c58067f278c18ba925e146b8aed673ffc57b3c40d5 | quote: 5000 GB (+more on request)
  - [1] 2026-11-03: the free column is unchanged: 1 day retention, 1024 Kbytes/sec, 20 GB per day; the registered and premium columns and the plan ladder are also unchanged | capture: sha256:3ede819df217d4ebbbfa86c58067f278c18ba925e146b8aed673ffc57b3c40d5 | quote: 1 days after last download 1024 Kbytes/sec 20 GB in 1 days
- sources:
  - [1] https://dropgalaxy.com/?op=payments
  - [2] https://forum.z-o-o-m.eu/index.php?topic=6200.0
  - [3] https://dropgalaxy.com/
  - [4] https://dropgalaxy.com/tos.html
