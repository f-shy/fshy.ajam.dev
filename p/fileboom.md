# FileBoom

> fileboom.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fileboom/ | JSON https://fshy.ajam.dev/api/v1/entity/fileboom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileBoom

- `debrid/fileboom` | qualifies-with-caveat | evidence reported | binding volume-quota | category premium file host (one-click hoster), retrieval target | tier premium-max
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:46.168Z (live) | stale on 2026-11-18
- url https://fileboom.me/
- price USD 17.20 per TiB-month on Premium Max (USD 46.94 for 2.73 TiB); USD 26.8 on Premium Pro; USD 52.5 on Premium | parsed USD 15.64/TB-mo
- free tier: Free accounts download 10 GB/day at slow speed with ads; the site sells three paid tiers by daily traffic: Premium 20 GB, Premium Pro 50 GB and Premium Max 100 GB per day. | unit: mixed | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: Premium: 'Uploading files up to 5Gb' (vendor terms); a reseller table lists 10 GB on Premium Pro. | source: [2]
- retention: Premium account: 'Storing files for 90 days' (vendor terms); free-account retention is not published. | source: [2]
- egress: Traffic is the product: 20, 50 or 100 GB per day depending on tier, with 'no speed limits' claimed for all three. | metered: yes | free allowance: 20/50/100 GB per day by tier | price per TB: no overage price; the tier is the lever | source: [1]
- identity: email | detail: Sign-up with a valid e-mail address, a user name and a password, or with a Google account; card and crypto via resellers or the vendor checkout.
- interface: unknown
- limits:
  - volume-quota (binding): 10 GB per day on a free account; 20/50/100 GB per day on Premium, Premium Pro and Premium Max [3]
  - per-object-cap: 5 GB on Premium, 10 GB on Premium Pro (reported) [4]
- limits note: The vendor premium page lists Free at 10 GB/day and Premium Max at 100 GB/day and shows 'From $1.22 /day'; the Premium and Premium Pro figures and every plan price are reseller-reported, and a reseller states that the Premium (20 GB) plan is marked 'New users only' on the vendor site.
- binding note: Only Premium Max clears 1 TiB a month with room; the two cheaper tiers cap at 0.55 and 1.36 TiB.
- interface detail: Part of the K2S family, which publishes an API at keep2share.cc/api/v2; FileBoom's own site did not confirm a separate endpoint on 2026-11-03.
- tooling: browser and download managers; JDownloader 2 support is reported for the family
- composes with: Only useful when the file is FileBoom-hosted; it is the most expensive per TiB of the K2S family for the same 100 GB/day.
- reliability: The family applies a hard daily counter; a missed day is not recoverable.
- notes: Included because the K2S family is one of the four host groups that actually appear on link sites in volume. Its per-TiB price is the worst of that group.
- evidence note: Four resellers agree on the 20/50/100 GB structure and within a few dollars on price, which is why the shape is recorded; the exact 30-day total needs the vendor checkout to become documented.
- extras:
  - premium_parallel: not published
  - max_file_premium: 10 GB (reported)
  - api: no
  - price_30d_usd: 46.94
  - price_ladder_reported: Premium USD 28.94 / 30 days (20 GB/day); Premium Pro USD 35.94 (50 GB/day); Premium Max USD 46.94 (100 GB/day), all reported by resellers because the vendor page is client-rendered
  - volume_tib_month: 1.0
- evidence:
  - [3] 2026-10-23: Premium 20 GB/day, 30 days $28.94, 90 days $71.94, 365 days $189.90
  - [5] 2026-10-23: table of Premium 20 GB, Pro 50 GB, Max 100 GB at $28.94/$35.94/$46.94 per month
  - [4] 2026-10-23: 'Daily traffic 50 GB / 20 GB'; 'Max file size 10 GB / 5 GB'
  - [6] 2026-11-03: the plan table of the vendor premium page, as read by a reseller in October 2026, lists the Free plan at 10 GB per day, slow, with ads | capture: sha256:a1e4b2c565ce28f408afed1bed1a7430ce6a8fb40c779f9f7690e6cfdc98ec53 | quote: | Free | 10 GB | Slow | Ads |
  - [2] 2026-11-03: the vendor terms list uploads up to 5Gb among the features of a Premium account | capture: sha256:0efefcfc8510d50986edad75a4b10d1212b9299c412636300af3fbf898fe7e04 | quote: Uploading files up to 5Gb
  - [2] 2026-11-03: the cap is stated on the vendor terms page | capture: sha256:0efefcfc8510d50986edad75a4b10d1212b9299c412636300af3fbf898fe7e04 | quote: Uploading files up to 5Gb
  - [2] 2026-11-03: the vendor terms list storing files for 90 days among the features of a Premium account | capture: sha256:0efefcfc8510d50986edad75a4b10d1212b9299c412636300af3fbf898fe7e04 | quote: Storing files for 90 days
  - [2] 2026-11-03: the retention is stated on the vendor terms page | capture: sha256:0efefcfc8510d50986edad75a4b10d1212b9299c412636300af3fbf898fe7e04 | quote: Storing files for 90 days
  - [6] 2026-11-03: the plan table lists a 10 GB daily limit for Free next to the paid tiers | capture: sha256:a1e4b2c565ce28f408afed1bed1a7430ce6a8fb40c779f9f7690e6cfdc98ec53 | quote: | Free | 10 GB | Slow | Ads |
  - [6] 2026-11-03: a reseller states that the Premium (Normal) 20 GB plan is for new users only on the vendor site | capture: sha256:a1e4b2c565ce28f408afed1bed1a7430ce6a8fb40c779f9f7690e6cfdc98ec53 | quote: | Premium (Normal) | 20 GB | Fast | New users only on the official site |
  - [2] 2026-11-03: registration needs a valid e-mail address, a user name and a password | capture: sha256:0efefcfc8510d50986edad75a4b10d1212b9299c412636300af3fbf898fe7e04 | quote: To register, you must submit a valid e-mail address and create a user name and password.
  - [7] 2026-11-03: the vendor premium page shows a Free column at 10 GB/day, slow, and a Premium Max column at 100 GB/day, with the lowest price from $1.22 /day | capture: sha256:79a025d78d16b027b2c7e651771e2df329e79efa33e73ab2bcac95fd630074f9 | quote: From $1.22 /day
  - [8] 2026-11-03: the vendor sign-up page offers social accounts (Google) or e-mail | capture: sha256:a08c78a37b6d4562c4daf7a0dab7a8a78959ea8f7c4438927436956e3c2ae692 | quote: Sign up with your social accounts or e-mail:
  - [5] 2026-11-03: a reseller price page updated October 19, 2026 still lists the 30-day prices at $28.94, $35.94 and $46.94 | capture: sha256:9bbd64623ca8d39d0f020e2042304c321d9aaf6dedef0e414b5cbaa73f928207 | quote: For 30 days: Premium $28.94, Premium Pro $35.94, Premium Max $46.94.
  - [6] 2026-11-03: the plan table lists the daily limits of the free and paid plans | capture: sha256:a1e4b2c565ce28f408afed1bed1a7430ce6a8fb40c779f9f7690e6cfdc98ec53 | quote: | Free | 10 GB | Slow | Ads |
- sources:
  - [1] https://fileboom.me/
  - [2] https://fboom.me/page/terms.html
  - [3] https://fileboom.link/fileboom-premium-account/
  - [4] https://plusinstant.com/fileboom-premium/fileboom-premium-30-days.html
  - [5] https://rapidquickjp.com/en/blog/fileboom-premium-price
  - [6] https://rapidquickjp.com/en/blog/fileboom-plans
  - [7] https://fboom.me/premium
  - [8] https://fboom.me/auth/register
