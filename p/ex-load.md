# EX-LOAD

> ex-load.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ex-load/ | JSON https://fshy.ajam.dev/api/v1/entity/ex-load.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EX-LOAD

- `debrid/ex-load` | qualifies-with-caveat | evidence documented | binding volume-quota | category premium file host (one-click hoster) selling daily traffic | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:35:59.157Z (live) | stale on 2026-11-23
- url https://ex-load.com/
- price USD 23.30 per TB-month on a 30-day pass; USD 7.22 per TB-month at the annual rate | parsed USD 7.22/TB-mo
- free tier: Downloading is free and needs no account: 'Direct Links - Share a single link - no account required for whoever downloads it' and 'Unlimited Downloads - No caps on how many times a file can be downloaded'. The free path's speed and waiting time are not stated; only the premium page prints 'Waiting time 0 seconds'. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Free downloads exist and are uncounted by download count. What the free path costs is time, not bytes, and the site does not quantify it.
- per-object cap: Premium prints 'Max file size: Unlimited'; Premium Pro repeats 'Unlimited file size'. No free-tier per-file cap is stated. | source: [2] | note: 'Unlimited' is the vendor's word for the paid path; it is recorded as stated, not as measured.
- retention: Not stated on the pages read. | source: [1]
- egress: Paid traffic is counted per day: Premium carries '50 GB Traffic per day', Premium Pro '200 GB Traffic per day'. Within the allowance: 'High download speed', 'Unlimited parallel downloads', 'Download-Accelerators support'. | metered: yes | free allowance: 50 GB/day on Premium; 200 GB/day on Premium Pro | price per TB: USD 7.22 per TB at the 365-day rate (computed: USD 129.95 / 12 months over 1.5 TB per month) | source: [2]
- identity: card | detail: Buying premium needs a card: 'Card, crypto and more' on the checkout. Downloading needs nothing at all, and a prepaid premium key can be activated without a card ('If you already have a premium key, you can activate it on the My Profile page').
- interface: rest, unknown
- limits:
  - volume-quota (binding): 50 GB per day (Premium), 200 GB per day (Premium Pro), reset daily [2]
  - write-gated: uploading requires Partner status, 'granted after a review' [1]
- limits note: The traffic counter starts 'From 50 GB' and does not accumulate: a day unused is a day lost. The write gate is separate and only affects publishing, not retrieval.
- binding note: At 1 TiB a month (about 34 GB a day) the 50 GB daily bucket on Premium is enough, so the binding constraint becomes the monthly bill rather than a technical wall; at 1 TiB a day only Premium Pro's 200 GB would still fall short by a factor of five.
- interface detail: 'Download-Accelerators support' and 'Unlimited parallel downloads' on the paid tier; multi-thread clients are the intended path. No API is advertised.
- tooling: Download managers (IDM, JDownloader class) as named by 'Download-Accelerators support'. A premium key can be activated on the account page, which is the resale surface these records checks elsewhere.
- composes with: A host that a debrid broker resolves, priced here as the alternative to one: 50 GB a day for USD 34.95 a month is 45 times the traffic of a FilesMonster 30-day pass for twice the price, and both are far above a multi-host debrid subscription.
- reliability: Publishing is closed to new accounts: 'Not every account can upload files - Partner status is granted after a review'. That keeps the catalogue curated and also means a client cannot use this host as free storage, only as a retrieval target.
- notes: The record exists for the daily-bucket comparison: it is the only host in this set that sells traffic by the day with no rollover, which is the shape a downloader with bursty demand wants and a steady one does not.
- evidence note: Free-download terms, the two daily buckets and all four prices were read on the vendor's pages. The free path's actual speed and wait are unstated by the vendor and were not measured.
- extras:
  - bucket_math: 50 GB/day is 1.5 TB a 30-day month; 200 GB/day is 6 TB. The annual pass at USD 129.95 over 18.25 TB is the cheapest per byte here
- evidence:
  - [2] 2026-10-23: the prices (30 days USD 34.95, 60 days USD 49.95, 90 days USD 61.95, 365 days USD 129.95) and the buckets ('50 GB Traffic per day' Premium, '200 GB Traffic per day' Premium Pro)
  - [1] 2026-10-23: 'Unlimited Downloads - No caps on how many times a file can be downloaded', 'Direct Links ... no account required for whoever downloads it', and the Partner-only upload gate
  - [3] 2026-10-23: two sale models exist (purchase-only, and premium-or-purchase), which is how a single file can be priced above the subscription
- sources:
  - [1] https://ex-load.com/
  - [2] https://ex-load.com/premium/
  - [3] https://ex-load.com/make_money
