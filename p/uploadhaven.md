# UploadHaven

> uploadhaven.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uploadhaven/ | JSON https://fshy.ajam.dev/api/v1/entity/uploadhaven.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UploadHaven

- `debrid/uploadhaven` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category premium file host (one-click hoster), retrieval target | tier pro
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:58.091Z (live) | stale on 2026-12-26
- url https://uploadhaven.com/
- price USD 8.99 per TiB-month on the stated 'Unlimited bandwidth', which no fair-use number contradicts that was reachable | parsed USD 8.18/TB-mo
- free tier: Free downloads for everyone, with no published byte cap: 'Free downloads for everyone. Unlock uncapped speeds with Pro.' | unit: mixed | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: 'Up to 100 GB per file' with a registered account | bytes: 100000000000 | source: [1]
- retention: not stated on the landing page | source: [1]
- egress: 'Unlimited bandwidth' on the landing page; Pro adds 'Max speed', 'No wait', 'No ads'. Free is 'uncapped speeds' only after paying, so free is speed-shaped. | metered: no | free allowance: unlimited claimed | price per TB: none | source: [1]
- identity: email | detail: E-mail signup for Pro; card payment.
- interface: browser
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
  - price_ladder_reported: USD 8.99 / month, or USD 2.99 / 3 days, or USD 69.99 / year
  - volume_tib_month: 1.0
  - interface_check: No programmatic path found: No API documentation found; the site is a single-page uploader with a Pro checkout.
- evidence:
  - [1] 2026-10-23: 'Up to 100 GB per file', 'Unlimited bandwidth', 'Free downloads for everyone. Unlock uncapped speeds with Pro.', 'Pro Plan ... Max speed, No wait, No ads', '$2.99 / 3 days or $8.99/month'
  - [1] 2026-10-23: Pro is USD 8.99/month or USD 2.99/3 days, sold on 'Unlimited bandwidth', 'Max speed', 'No wait' and 'No ads'; no monthly byte allowance and no fair-use clause appear on the page.
  - [1] 2026-11-25: the landing page claims a 100 GB per-file limit and unlimited bandwidth | capture: sha256:0116796df46cc929e30f4d957fe3109b51850dd0265c9b7b54361107e4c6621b | quote: Up to 100 GB per file Unlimited bandwidth Free to use
  - [1] 2026-11-25: free downloads exist and uncapped speeds are a Pro feature | capture: sha256:0116796df46cc929e30f4d957fe3109b51850dd0265c9b7b54361107e4c6621b | quote: Free downloads for everyone. Unlock uncapped speeds with Pro. Your bandwidth, unleashed.
  - [2] 2026-11-25: the signup page lists a yearly Pro plan at USD 69.99 | capture: sha256:92f7b071b35d03b5c436833cac7a7fdc4f58c926b486381775f2cc0e2376bdf6 | quote: 69.99
  - [2] 2026-11-25: the signup form asks for an email address | capture: sha256:92f7b071b35d03b5c436833cac7a7fdc4f58c926b486381775f2cc0e2376bdf6 | quote: Email address
  - [2] 2026-11-25: payment on signup is handled by Stripe | capture: sha256:92f7b071b35d03b5c436833cac7a7fdc4f58c926b486381775f2cc0e2376bdf6 | quote: Secure payment via Stripe
- sources:
  - [1] https://uploadhaven.com/
  - [2] https://uploadhaven.com/account/register
