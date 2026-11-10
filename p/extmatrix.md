# ExtMatrix

> extmatrix.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/extmatrix/ | JSON https://fshy.ajam.dev/api/v1/entity/extmatrix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ExtMatrix

- `debrid/extmatrix` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (Japanese-market, premium one-time) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T03:18:17.000Z (live) | stale on 2026-11-23
- url https://www.extmatrix.com/premium.php
- price USD 12.95 per month, no TB figure published | parsed USD 12.95/mo
- free tier: Free account: 100.00 GB file space, 250.00 MB upload cap, 100 KB/s download, inactive files deleted after 30 days. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: Registration is required to hold the space; anonymous upload is capped at 250 MB per file.
- per-object cap: Free 250.00 MB; Premium 100.00 GB | bytes: 107374182400 | source: [1] | note: The 100 GB figure is the premium upload cap, quoted as 'Upload file size 100.00 GB'.
- retention: Free: 'Inactive files will be deleted: 30 Day(s)'. Premium: 'never'. | days: 30 | source: [1] | note: The 30 days is the free tier; premium files are not deleted for inactivity.
- egress: Free accounts are shaped to 100KB/s. Premium is 'Unlimited' download speed with 'Simultaneous downloads', 'Direct downloads', 'Download resuming' and accelerator support. No byte allowance is published for either tier. | metered: no | free allowance: no byte allowance published; the free throttle is 100 KB/s | source: [1]
- identity: card | detail: Free registration needs only a signup form; premium is bought by card through the site or its resellers, with billing explicitly one-off rather than recurring.
- interface: unknown
- limits:
  - per-object-cap (binding): 250 MB free, 100 GB premium [1]
  - per-ip-shaping: 100 KB/s on free accounts [1]
  - retention-clamped: free files deleted after 30 days of inactivity [1]
- limits note: Premium allows 50 simultaneous uploads against 1 on free. Credit-card billing is explicitly not a subscription ('we won't charge you automatically').
- binding note: On the free tier the 250 MB upload cap fails before anything else: 1 TiB of monthly transfer cannot even be expressed in 250 MB objects without 4,000 uploads. At premium the cap rises to 100 GB and the absence of a published byte allowance becomes the unknown that binds instead.
- interface detail: Web upload and download with a 'Download Manager' and accelerator support; the site publishes no API or remote-upload endpoint on the pages read.
- tooling: No rclone backend, no published API. Leechall and PrimeLeech both carry an extmatrix generator, so the workable path today is a leecher rather than the host itself.
- composes with: A host the paid debrids mostly do not cover, so it is reached through a free leecher (leechall caps it at 6 GB/day, the highest cap on that list) or by buying a $12.95 month. It holds Japanese-market releases that do not appear on Rapidgator or Katfile.
- reliability: Free files vanish 30 days after the last touch, and the free tier's 100 KB/s makes a multi-gigabyte pull an overnight job.
- notes: The monthly price is flat, not per byte, so price_per_tb_month cannot be computed without a measured download. $89.95 a year is the cheapest per month at $7.50.
- evidence note: Feature table and price table read on the vendor's premium page. A completed premium download would raise egress to measured.
- extras:
  - plans: 1 month $12.95; 3 months $34.95; 6 months $55.95; 1 year $89.95
  - annual_effective_monthly: USD 7.50
  - resellers: https://www.extmatrix.com/reseller.php
- evidence:
  - [1] 2026-10-23: the Free/Premium comparison (250 MB vs 100 GB upload, 100 GB vs unlimited space, 30-day vs never deletion, 100KB/s vs unlimited) and the price table $12.95 / $34.95 / $55.95 / $89.95
  - [2] 2026-10-23: a third-party leecher's daily cap for the host: 'extmatrix.com 0 B / 6 GB /d'
- sources:
  - [1] https://www.extmatrix.com/premium.php
  - [2] https://leechall.com/
