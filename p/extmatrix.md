# ExtMatrix

> extmatrix.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/extmatrix/ | JSON https://fshy.ajam.dev/api/v1/entity/extmatrix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ExtMatrix

- `debrid/extmatrix` | qualifies-with-caveat | evidence documented | binding per-object-cap | category file host (Japanese-market, premium one-time) | tier premium
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T09:46:38.367Z (live) | stale on 2026-12-26
- url https://www.extmatrix.com/premium.php
- price USD 12.95 per month, no TB figure published | parsed USD 12.95/mo
- free tier: Free account: 100.00 GB file space, 250.00 MB upload cap, 100 KB/s download, inactive files deleted after 30 days. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: Registration is required to hold the space; anonymous upload is capped at 250 MB per file.
- per-object cap: Free 250.00 MB; Premium 100.00 GB | bytes: 107374182400 | source: [1] | note: The 100 GB figure is the premium upload cap, quoted as 'Upload file size 100.00 GB'.
- retention: Free: 'Inactive files will be deleted: 30 Day(s)'. Premium: 'never'. | days: 30 | source: [1] | note: The 30 days is the free tier; premium files are not deleted for inactivity.
- egress: Free accounts are shaped to 100KB/s. Premium is 'Unlimited' download speed with 'Simultaneous downloads', 'Direct downloads', 'Download resuming' and accelerator support. No byte allowance is published for either tier. | metered: no | free allowance: no byte allowance published; the free throttle is 100 KB/s | source: [1]
- identity: card | detail: Free registration needs only a signup form; premium is bought by card through the site or its resellers, with billing explicitly one-off rather than recurring.
- interface: browser
- limits:
  - per-object-cap (binding): 250 MB free, 100 GB premium [1]
  - per-ip-shaping: 100 KB/s on free accounts [1]
  - retention-clamped: free files deleted after 30 days of inactivity [1]
- limits note: Premium allows 50 simultaneous uploads against 1 on free. Credit-card billing is explicitly not a subscription ('we won't charge you automatically').
- binding note: On the free tier the 250 MB upload cap fails before anything else: 1 TiB of monthly transfer cannot even be expressed in 250 MB objects without 4,000 uploads. At premium the cap rises to 100 GB and the absence of a published byte allowance becomes the unknown that binds instead.
- interface detail: Web upload and download with a 'Download Manager' and accelerator support; the vendor documents an HTTP upload API endpoint at www.extmatrix.com/api/upload.php that takes an api_key.
- tooling: The vendor publishes an HTTP upload endpoint at www.extmatrix.com/api/upload.php that takes an api_key. No rclone backend was found. Leechall and PrimeLeech both carry an extmatrix generator.
- composes with: A host the paid debrids mostly do not cover, so it is reached through a free leecher (leechall caps it at 6 GB/day, the highest cap on that list) or by buying a $12.95 month. It holds Japanese-market releases that do not appear on Rapidgator or Katfile.
- reliability: Free files vanish 30 days after the last touch, and the free tier's 100 KB/s makes a multi-gigabyte pull an overnight job.
- notes: The monthly price is flat, not per byte, so price_per_tb_month cannot be computed without a measured download. Web upload and download use a 'Download Manager' and accelerator support; the vendor documents an HTTP upload endpoint at www.extmatrix.com/api/upload.php.
- evidence note: Feature table and price table read on the vendor's premium page. A completed premium download would raise egress to measured.
- extras:
  - plans: 1 month $12.95; 3 months $34.95; 6 months $55.95; 1 year $89.95
  - annual_effective_monthly: USD 7.50
  - resellers: https://www.extmatrix.com/reseller.php
- evidence:
  - [1] 2026-10-23: the Free/Premium comparison (250 MB vs 100 GB upload, 100 GB vs unlimited space, 30-day vs never deletion, 100KB/s vs unlimited) and the price table $12.95 / $34.95 / $55.95 / $89.95
  - [2] 2026-10-23: a third-party leecher's daily cap for the host: 'extmatrix.com 0 B / 6 GB /d'
  - [3] 2026-11-25: the vendor documents an HTTP upload API endpoint | capture: sha256:bb728f9bd1291d63147eaac921cfce80c0cbc8324d33384e342c47260c0ff576 | quote: $upload_server = "https://www.extmatrix.com/api/upload.php";
  - [1] 2026-11-25: the free plan is shaped to 100KB/s while premium is unlimited | capture: sha256:f1320ac893c359dfc2459bd314fc03668f30a2204a0c9aca75ccc817259366e2 | quote: Download speed | Unlimited | 100KB/s
  - [1] 2026-11-25: free files are deleted after 30 days of inactivity and premium files are not | capture: sha256:f1320ac893c359dfc2459bd314fc03668f30a2204a0c9aca75ccc817259366e2 | quote: Inactive files will be deleted | never | 30 Day(s)
  - [1] 2026-11-25: the four premium prices are $12.95, $34.95, $55.95 and $89.95 | capture: sha256:f1320ac893c359dfc2459bd314fc03668f30a2204a0c9aca75ccc817259366e2 | quote: ** Price** | $12.95 | $34.95 | $55.95 | $89.95
  - [1] 2026-11-25: credit-card billing is one-off rather than auto-renewing | capture: sha256:f1320ac893c359dfc2459bd314fc03668f30a2204a0c9aca75ccc817259366e2 | quote: * Please note that credit card billing is not an automatic subscription; we won't charge you automatically.
  - [4] 2026-11-25: the vendor states limits may be revised at any time | capture: sha256:ae698846465fab2cfcb3e98f1b42c01e679ac06b830d61b7467ac665c275a505 | quote: ExtMatrix retains the right to create and revise limits on use, storage, upload and download speeds, sharing, maximum number and duration of look-ups or downloads and any other aspect of the Service, at its sole discretion and at any time, with or without notice.
  - [5] 2026-11-25: the anonymous upload page states a 250.00 MB per-file maximum | capture: sha256:8e0f335a95181d93a71d6754abe8eafebb25b7d4e3ac67b16ba0e5647c393c51 | quote: Choose a File: (max. 250.00 MB)
  - [2] 2026-11-25: a third-party leecher lists 6 GB per day for the host | capture: sha256:d8bf63f755d814642dc9a8e0b3c6a5e73d73009145cafcb9b09340ebcd64cf2f | quote: extmatrix.com extmatrix.com 0 B / 6 GB /d
- sources:
  - [1] https://www.extmatrix.com/premium.php
  - [2] https://leechall.com/
  - [3] https://www.extmatrix.com/api/docs.php
  - [4] https://www.extmatrix.com/help/terms.php
  - [5] https://www.extmatrix.com/
