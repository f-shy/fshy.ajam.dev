# Turboget.net

> turboget.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/turboget/ | JSON https://fshy.ajam.dev/api/v1/entity/turboget.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Turboget.net

- `debrid/turboget-net` | paid-only | evidence documented | binding volume-quota | category Turbobit Turbo-access storefront (reseller domain on the Turbobit platform) | tier Turbo access
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:36.944Z (live) | stale on 2026-12-04
- url https://turboget.net/
- price USD 16.58 per TB of download traffic on the 1-month plan (USD 9.95 for 600 GB)
- free tier: Free mode (after a robot test and a time-out): about 5 Gb of downloads a day at a limited speed of about 55-60 KB/s, as written in the FAQ. The paid Turbo access plans are sold here. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1] | note: The free path is on turbobit.net, not on this domain.
- per-object cap: Premium account: 'Upload files up to 100 GB in size'; the cap for a free account is not published. | bytes: 100000000000 | source: [2] | note: The 100 GB figure is described as transfer volume, not a single-object cap; unverified as a hard number.
- retention: not stated on the pages that rendered; Turbobit's own FAQ says files are kept while the account is active and longer for premium | source: [1] | note: unstated
- egress: Turbo plans on the premium page: 5 days 100 GB USD 5.95 (trial), 1 month 600 GB USD 9.95, 6 months 3600 GB USD 34.95, 1 year 7200 GB USD 59.95, 2 years 14400 GB USD 89.95; the daily and monthly caps are in limits. | metered: yes | free allowance: about 5 Gb a day in free mode at 55-60 KB/s | price per TB: USD 16.58 | source: [3]
- identity: email | detail: Registration needs a real email address, a password and agreement to the rules. A guest purchase needs an email address; payment methods listed are plastic cards, Skrill, cryptocurrency via Freekassa and resellers. No phone number or ID document is asked on the pages read.
- interface: unknown
- limits:
  - volume-quota (binding): Premium: 25 GB per day and 600 GB per month (rules page); free mode: about 5 Gb per day (FAQ) [2]
- limits note: The rules page also caps Premium at 250 files per day and at 10 different IP ranges per day; the Plus+ option doubles the volume limits to 50 GB per day and 1200 GB per month. Whether a datacenter address is accepted: not published.
- binding note: Premium downloads are capped at 25 GB per day and 600 GB per month on the rules page; the monthly volume is the plan size and is reached before any object cap applies.
- interface detail: Single-page app (data-app="turbobit") whose tariff and checkout pages render entirely from JavaScript; the only readable surfaces are the marketing page and the FAQ.
- tooling: Browser only. Support channels named on the FAQ: help2.turboget.net, online chat, and support by email, Skype and ICQ.
- composes with: A second front door to the same Turbo codes sold by turbobitpremium.org and by the Russian forum resellers; useful only if its price or its payment rail differs, which could not be read.
- reliability: The FAQ is a copy of Turbobit's own FAQ (it opens 'What is Turbobit.net?') and support runs on turbobit.net addresses, so a buyer is dealing with the Turbobit operator through a second domain. The FAQ and the rules page state different daily Premium download volumes.
- notes: The cheapest paid plan is the 5-day 100 GB trial at USD 5.95; the cheapest per unit of traffic is the 2-year plan at 14400 GB for USD 89.95. The plain HTML of the tariff pages is an empty shell and the prices render only in a script-executing reader.
- evidence note: The plans, prices, traffic volumes, free-mode volume, upload cap and registration inputs are quoted from the premium, rules and FAQ pages as read through a rendering reader; the plain HTML of /premium is an empty single-page-app shell.
- evidence:
  - [1] 2026-10-23: the FAQ is Turbobit's own ('What is Turbobit.net?'), the guest Turbo-code purchase path, and the support addresses @Turbobit.net
  - [3] 2026-10-23: 'Turbo access allows you to download files with unlimited speed', 'The total volume and number of your files are unlimited', 'Up to 100GB file transfer volume'
  - probe:https://turboget.net/tariffs 2026-10-23: the response is an HTML shell with <div id="app"></div> and a JS bundle; no price is present in the bytes returned
  - [1] 2026-11-03: free users download about 5 Gb a day with limited speed | capture: sha256:2067508164c49956aaf9ac24bf60de7ebd88040651ca6cc3dd8b7438eb65f6bd | quote: If you are a free user, you may download about 5 Gb a day if downloading continually, but note that free account speed is limited.
  - [4] 2026-11-03: the 1-month Turbo plan is 600 GB for $9.95 | capture: sha256:568c37c6e3941152d6d736696e37cd10a5cd8d9fce3d46731c823ce05d62d2b2 | quote: 1 month 600 GB most popular $9.95
  - [2] 2026-11-03: Premium accounts upload files up to 100 GB | capture: sha256:fdcc09dd9ca599d33fe98596d313cbf47470609b1995ac8d07b7b7867c10ceac | quote: Upload files up to 100 GB in size
  - [2] 2026-11-03: rules page caps Premium at 25 GB per day and 600 GB per month | capture: sha256:fdcc09dd9ca599d33fe98596d313cbf47470609b1995ac8d07b7b7867c10ceac | quote: A user with a Premium Account can download files totalling up to 25 GB per day and up to 600 GB per month.
  - [2] 2026-11-03: Premium use is limited to 10 IP ranges a day | capture: sha256:fdcc09dd9ca599d33fe98596d313cbf47470609b1995ac8d07b7b7867c10ceac | quote: Premium Account can be used from 10 different IP ranges during the day.
  - [1] 2026-11-03: registration needs an email, a password and agreement to the rules | capture: sha256:2067508164c49956aaf9ac24bf60de7ebd88040651ca6cc3dd8b7438eb65f6bd | quote: you will need to enter a real email address, to make up a password for your account, and to agree to the rules of our service.
  - [1] 2026-11-03: a guest purchase needs an email address | capture: sha256:2067508164c49956aaf9ac24bf60de7ebd88040651ca6cc3dd8b7438eb65f6bd | quote: Enter your email if you are paying as a guest
  - [1] 2026-11-03: FAQ states 40 Gb per day and 600 Gb per month for Turbo | capture: sha256:2067508164c49956aaf9ac24bf60de7ebd88040651ca6cc3dd8b7438eb65f6bd | quote: All users who have Turbo Access may enjoy the maximum download speed possible and download up to 40 Gb a day, 600 Gb per month.
  - [4] 2026-11-03: the 5-day Turbo trial plan is 100 GB for $5.95 | capture: sha256:568c37c6e3941152d6d736696e37cd10a5cd8d9fce3d46731c823ce05d62d2b2 | quote: 5 days 100 GB trial $5.95
- sources:
  - [1] https://turboget.net/faq
  - [2] https://turboget.net/rules
  - [3] https://turboget.net/
  - [4] https://turboget.net/premium
