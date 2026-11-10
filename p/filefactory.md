# FileFactory

> filefactory.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filefactory/ | JSON https://fshy.ajam.dev/api/v1/entity/filefactory.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FileFactory

- `debrid/filefactory` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category premium file host (one-click hoster), retrieval target | tier premium
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:46.169Z (live) | stale on 2026-12-04
- url https://www.filefactory.com/premium
- price USD 19 per 30 days on the vendor pricing page; no per-TiB figure because the vendor publishes no byte allowance | parsed USD 19/mo
- free tier: Free account: a 45-60 sec wait timer before a download, a maximum transfer size of 2 GB, 20 transfers per day and 5 recipients per transfer; guest downloads have a device daily cap of 10/day. Premium removes the countdown: 30 days USD 19, 90 days USD 39, 180 days USD 59, 365 days USD 99. | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: Maximum transfer size (combined size of all files in one transfer): 5 GB Premium, 2 GB Free, 1 GB Guest. | source: [1]
- retention: Transfer expiry range 1-90 days Premium, 1-30 days Free, 1-7 days Guest; transfer history kept 1 year Premium and 30 days Free; account file cleanup depends on account status and activity. | source: [1]
- egress: The vendor pricing page lists 'No public countdown', 'Direct downloads' and 'Larger transfer allowances' for Premium, a 45-60 sec wait timer for Free and Guest downloads, and a device daily cap of 10/day for Guest downloads; it publishes no byte allowance and no TrafficShare figure. | metered: no | free allowance: not published: the pricing page shows the Premium and Free account allowances without a number and Guest downloads at 10/day | price per TB: none published | source: [1]
- identity: email | detail: Sign-up offers 'Sign up with Google' or 'Sign up with email'; the About page says 'No credit card required'; payments are settled via Odeonpay ALE S.R.L. (Paysagi) as Merchant of Record.
- interface: unknown
- limits:
  - per-ip-shaping (binding): 45-60 sec wait timer before Free and Guest downloads; Guest downloads capped at 10/day per device [1]
  - volume-quota: daily transfer limit 100 Premium, 20 Free, 3 Guest; maximum transfer size 5 GB Premium, 2 GB Free, 1 GB Guest; Premium download allowance stated as 'Larger transfer allowances' with no number [1]
- limits note: The vendor pricing page no longer claims unlimited bandwidth: Premium is 'Larger transfer allowances' with no number, and the account download allowances are shown without a figure.
- binding note: The vendor publishes a 45-60 sec wait timer for free downloads and no byte allowance for Premium downloads ('Larger transfer allowances'), so an unpublished allowance is what can fail at 1 TiB/month.
- interface detail: No API documentation reachable; the site presents FileFactory Transfer (send files by email or link) and serves its Premium pricing at /premium.
- tooling: browser; download managers supported per the premium feature list
- composes with: Only useful if the links are FileFactory links; its 2025-era share of link-site posts is small next to Rapidgator and 1fichier.
- reliability: Account file cleanup depends on account status and activity (vendor pricing page). An unauthenticated read of /premium from a datacenter address was answered with an 'Access Restricted' page, while two other provider routes were served the pricing page.
- notes: The vendor pricing page now prices Premium at USD 19 for 30 days and lists no TrafficShare or unlimited-bandwidth claim; the earlier reseller figures for the 30-day price and for TrafficShare are not on it. The per-TiB column stays empty because no byte allowance is published. Not worth a key at 1 TiB/month unless the link is here.
- evidence note: The vendor pricing page read on 2026-11-03 states the four Premium prices, the wait timer, the transfer limits and the transfer expiry ranges. The per-file download cap and the Premium byte allowance are not published there.
- extras:
  - premium_parallel: not published
  - max_file_premium: 5 GB maximum transfer size (Premium)
  - api: no
  - price_30d_usd: 19.0
  - price_ladder_reported: USD 19 / 30 days; USD 39 / 90 days; USD 59 / 180 days; USD 99 / 365 days (vendor pricing page)
  - volume_tib_month: 1.0
- evidence:
  - [2] 2026-10-23: reseller table: 30 days $13, 90 $35, 180 $59, 365 $94; TrafficShare 100 GB/month on one page and 1 TB elsewhere
  - [3] 2026-10-23: 365 days $99 and '1TB monthly TrafficShare'
  - [1] 2026-11-03: the vendor pricing page sells Premium on no public countdown, direct downloads and larger transfer allowances, with a Free and a Guest column and four priced plans | capture: sha256:d04379ddd7d6b1c2de850594ca559327629c43210c32a08d05474e8d09ad1122 | quote: Skip the public countdown, unlock direct downloads, and get larger transfer allowances with FileFactory Premium.
  - [4] 2026-11-03: the pricing page row for maximum transfer size lists 5 GB, 2 GB and 1 GB for Premium, Free and Guest | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Maximum combined size for all files in one transfer.
  - [4] 2026-11-03: the pricing page says account file cleanup depends on account status and activity, and lists the transfer expiry ranges and history periods per account type | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Signed-in accounts can store and manage files; cleanup depends on account status and activity.
  - [4] 2026-11-03: guest downloads have a device daily cap (10/day in the table) and account downloads use signed-in allowances with no number | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Guest downloads have a device daily cap; account downloads use signed-in allowances.
  - [4] 2026-11-03: account allowances are named without a number and the guest cap is 10/day | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Guest downloads have a device daily cap; account downloads use signed-in allowances.
  - [4] 2026-11-03: the download wait timer row lists None for Premium and 45-60 sec for Free and Guest | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Premium downloads start without the public countdown.
  - [4] 2026-11-03: the pricing page publishes numeric transfer limits per account type | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Maximum combined size for all files in one transfer.
  - [4] 2026-11-03: the transfer features table lists the daily transfer limit and the maximum transfer size per account type | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Maximum combined size for all files in one transfer.
  - [1] 2026-11-03: Premium is sold on larger transfer allowances, not on unlimited bandwidth | capture: sha256:d04379ddd7d6b1c2de850594ca559327629c43210c32a08d05474e8d09ad1122 | quote: Skip the public countdown, unlock direct downloads, and get larger transfer allowances with FileFactory Premium.
  - [1] 2026-11-03: Premium allowances are described without a number | capture: sha256:d04379ddd7d6b1c2de850594ca559327629c43210c32a08d05474e8d09ad1122 | quote: Skip the public countdown, unlock direct downloads, and get larger transfer allowances with FileFactory Premium.
  - [5] 2026-11-03: the vendor sign-up page offers sign-up with email (and with Google) | capture: sha256:44f85af7fc875389bcd8870883ff0583657eb560a146512083d77d0bc85d0e13 | quote: Sign up with email
  - [1] 2026-11-03: a read of /premium through one route was answered with an Access Restricted page | capture: sha256:78067777baf5a866f725b406ec87e9d5b05d80271ca9091ad96cd1033fefa21b | quote: Your access to FileFactory has been restricted.
  - [6] 2026-11-03: the vendor home page presents a file transfer service | capture: sha256:6a3ba34ec63c94f06255c918eda49828315f151d99cd4525615453be64c97bf7 | quote: Drag, drop, and send to get those large files moving.
  - [1] 2026-11-03: the vendor pricing page is readable and describes the Premium plan | capture: sha256:d04379ddd7d6b1c2de850594ca559327629c43210c32a08d05474e8d09ad1122 | quote: Skip the public countdown, unlock direct downloads, and get larger transfer allowances with FileFactory Premium.
  - [4] 2026-11-03: the vendor pricing page lists the plans, prices and limits | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Premium downloads start without the public countdown.
  - [4] 2026-11-03: the 30-day Premium plan is $19 USD | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: $19 USD
  - [4] 2026-11-03: the vendor price ladder starts at $19 USD for 30 days; the 90, 180 and 365 day plans are $39, $59 and $99 | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: $19 USD
  - [4] 2026-11-03: the maximum transfer size row lists 5 GB for Premium | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Maximum combined size for all files in one transfer.
  - [4] 2026-11-03: the 30-day Premium plan is $19 USD on the vendor pricing page | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: $19 USD
  - [1] 2026-11-03: the vendor pricing page lists 365 days as the recommended plan at $99 USD, with 180 days at $59, 90 days at $39 and 30 days at $19 | capture: sha256:d04379ddd7d6b1c2de850594ca559327629c43210c32a08d05474e8d09ad1122 | quote: 365 DaysRecommended
  - [4] 2026-11-03: the wait timer row lists None for Premium and 45-60 sec for Free and Guest; the transfer features list 5 GB, 2 GB and 1 GB maximum transfer size for Premium, Free and Guest | capture: sha256:d6f5775b8e72f1f52027bb307e6d38c83a6186cb84c1d98a2d0527ab883b95ce | quote: Premium downloads start without the public countdown.
  - [5] 2026-11-03: the sign-up page offers sign-up with Google or with email | capture: sha256:44f85af7fc875389bcd8870883ff0583657eb560a146512083d77d0bc85d0e13 | quote: Sign up with email
  - [7] 2026-11-03: the About page states that no credit card is required | capture: sha256:65f7f1191eae2c812586c49213f2e79983b2b4dd66c12d9cca4b450e6bcd64d1 | quote: No credit card required
  - [1] 2026-11-03: one read route for /premium was answered with an Access Restricted page | capture: sha256:78067777baf5a866f725b406ec87e9d5b05d80271ca9091ad96cd1033fefa21b | quote: Your access to FileFactory has been restricted.
  - [1] 2026-11-03: the vendor pricing page describes the Premium plan and lists four priced plans | capture: sha256:d04379ddd7d6b1c2de850594ca559327629c43210c32a08d05474e8d09ad1122 | quote: Skip the public countdown, unlock direct downloads, and get larger transfer allowances with FileFactory Premium.
- sources:
  - [1] https://www.filefactory.com/premium
  - [2] https://multihoster.org/filefactory-2/
  - [3] https://www.tenorshare.com/knowledge/filefactory-downloader.html
  - [4] https://www.filefactory.com/pricing
  - [5] https://www.filefactory.com/signup
  - [6] https://www.filefactory.com/
  - [7] https://www.filefactory.com/about
