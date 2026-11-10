# Upstore

> upstore.net | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/upstore/ | JSON https://fshy.ajam.dev/api/v1/entity/upstore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Upstore

- `debrid/upstore` | qualifies-with-caveat | evidence documented | binding per-object-cap | category premium file host (one-click hoster), retrieval target | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://upstore.net/premium/
- price EUR 14.55 per TiB-month at the monthly rate (EUR 16 / 33 days) with no byte cap published | parsed USD 14.81/TB-mo
- free tier: 'Slow speed', 'One file, one thread', 'Wait to download again', 'Captcha', 'Wait your turn', 'Download link will expire soon', 'Download files up to 2 GB', 'Upload files up to 2 GB', 'Limited lifetime storage'. | unit: mixed | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: free downloads are capped at 2 GB per file; premium raises the download and upload cap to 5 GB per file | bytes: 2000000000 | source: [1]
- retention: 'Files kept on server forever' is listed as a premium benefit; the free column says 'Limited lifetime storage' without a number | source: [1]
- egress: No byte allowance is published anywhere on the premium page. Speed is sold as 'Download speed - up to 1000 Mbps' with 'Download accelerators support'; the free tier is 'Slow speed, one file, one thread'. | metered: no | free allowance: none published | price per TB: none | source: [1]
- identity: card | detail: Account is e-mail based, but the payment page adds 'Age confirmed during the payment' and a Paymer check option; the card is the identity step.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB per file on free, 5 GB on premium [1]
  - per-ip-shaping: free is 'one file, one thread' with a wait; premium is 'up to 1000 Mbps' [1]
- limits note: Age confirmation is required during payment; the page states it as a payment step, not a document upload.
- binding note: With no byte cap published, the only hard number that can stop 1 TiB of monthly transfer is the 5 GB per-file ceiling, which forces an archive into at least 220 parts.
- interface detail: No API page found; the account is a web login.
- tooling: browser; download accelerators explicitly supported on premium (the vendor names them as a benefit)
- composes with: A flat monthly price with no byte counter is the cleanest fit for a client whose volume is unknown month to month, at roughly three times 1fichier's annual-equivalent price.
- reliability: Files are kept 'forever' only on premium; the free tier deletes on a clock the vendor does not publish.
- notes: Second-cheapest flat-rate key after 1fichier Premium, and the only one whose free tier the 2026 test called 'clean' rather than a paywall. The 5 GB per-file cap is the real cost: a 60 GB archive is twelve parts before deduplication.
- evidence note: Every number is from the vendor premium page read. The absence of a byte cap is the vendor's silence, not a measured fact, so the verdict keeps a caveat.
- extras:
  - premium_parallel: yes ('Parallel downloads')
  - max_file_free: 2 GB
  - max_file_premium: 5 GB
  - api: no
  - price_30d_eur: 14.55
  - price_ladder_reported: EUR 16 for 1 month + 3 bonus days (EUR 0.48/day); EUR 33 for 3 months; EUR 59 for 6 months; EUR 99 for 1 year
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: premium: 'High speed downloads', 'Parallel downloads', 'Download without delay', 'No captcha', 'Upload files up to 5 GB', 'Files kept on server forever', 'Download speed - up to 1000 Mbps'; free: 'Slow speed', 'One file, one thread', 'Download files up to 2 GB', 'Limited lifetime storage'; prices 16/33/59/99 EUR
- sources:
  - [1] https://upstore.net/premium/
