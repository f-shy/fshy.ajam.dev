# UploadHaven

> uploadhaven.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploadhaven/ | JSON https://fshy.ajam.dev/api/v1/entity/uploadhaven.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UploadHaven

- `debrid/uploadhaven` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category premium file host (one-click hoster), retrieval target | tier pro
- needs card no, phone no, ID no, institution no | verified 2026-10-23T02:20:00.000Z (live) | stale on 2026-11-23
- url https://uploadhaven.com/
- price USD 8.99 per TiB-month on the stated 'Unlimited bandwidth', which no fair-use number contradicts that was reachable | parsed USD 8.18/TB-mo
- free tier: Free downloads for everyone, with no published byte cap: 'Free downloads for everyone. Unlock uncapped speeds with Pro.' | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: 'Up to 100 GB per file' with a registered account | bytes: 100000000000 | source: [1]
- retention: not stated on the landing page | source: [1]
- egress: 'Unlimited bandwidth' on the landing page; Pro adds 'Max speed', 'No wait', 'No ads'. Free is 'uncapped speeds' only after paying, so free is speed-shaped. | metered: no | free allowance: unlimited claimed | price per TB: none | source: [1]
- identity: email | detail: E-mail signup for Pro; card payment.
- interface: unknown
- limits:
  - per-ip-shaping (binding): free tier is speed-capped; Pro is 'Max speed' with no number published [1]
  - per-object-cap: 100 GB per file, registered account required [1]
  - per-ip-shaping (binding): free downloads are shaped and gated; Pro removes the gate and the shaping, with no byte number published [1]
- limits note: 'Unlimited bandwidth' has no fair-use clause found; that is an absence of evidence, not evidence of absence.
- binding note: With no byte cap published and no API, the thing that fails at 1 TiB/month is throughput or coverage long before any counter.
- interface detail: No API documentation found; the site is a single-page uploader with a Pro checkout.
- tooling: browser drag-and-drop; no download-manager documentation found
- composes with: The cheapest flat-rate key found in the sector. It is worth nothing at 1 TiB/month unless the files are UploadHaven-hosted, and its file network is the smallest of any host here.
- reliability: Free downloads exist but are the tier the vendor is selling out of; no rate was measured on 2026-10-23.
- notes: A plan with no allowance goes in the flat-month group, where it is USD 8.99/month and out of contention.
- evidence note: Price and claim are from the vendor landing page read. The absence of a cap is unverified by measurement, so the record keeps no per-TiB confidence beyond the price.
- extras:
  - premium_parallel: not published
  - max_file_free: 100 GB (registered)
  - max_file_premium: 100 GB
  - api: no
  - price_30d_usd: 8.99
  - price_ladder_reported: USD 8.99 / month, or USD 2.99 / 3 days
  - volume_tib_month: 1.0
- evidence:
  - [1] 2026-10-23: 'Up to 100 GB per file', 'Unlimited bandwidth', 'Free downloads for everyone. Unlock uncapped speeds with Pro.', 'Pro Plan ... Max speed, No wait, No ads', '$2.99 / 3 days or $8.99/month'
  - [1] 2026-10-23: Pro is USD 8.99/month or USD 2.99/3 days, sold on 'Unlimited bandwidth', 'Max speed', 'No wait' and 'No ads'; no monthly byte allowance and no fair-use clause appear on the page.
- sources:
  - [1] https://uploadhaven.com/
