# Isra.cloud

> isra.cloud | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/isra/ | JSON https://fshy.ajam.dev/api/v1/entity/isra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Isra.cloud

- `debrid/isra-cloud` | qualifies-with-caveat | evidence reported | binding volume-quota | category file host (Israeli-market, premium via resellers) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T11:28:46.170Z (live) | stale on 2026-11-18
- url https://isra.cloud/
- price USD 19.00 per 30 days for about 1,5 TB of bandwidth on the vendor premium page | parsed USD 19/mo
- free tier: 'Upload your personal files to a secure cloud storage system ... You get 1 TB of space'. | unit: TB | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: The 1 TB claim is on the landing page and on its premium subdomain, which serve the same text. The vendor terms state 'We provide Only premium subscription services.' and the landing text does not call the 1 TB free, so whether a free account keeps that space is unverified.
- per-object cap: 3 GB maximum size of an uploaded file (for a Premium user), per the vendor terms. | source: [2]
- retention: not stated on the pages read; the only related statement is that 'a premium user can restrict' access to their own files | source: [2]
- egress: Premium users are limited to 55GB of download per day (24 hours), changeable at the administration's discretion (vendor terms). The vendor publishes no free download volume; free_allowance holds the third-party figure. | metered: yes | free allowance: 650 MB/day (third-party figure, not the vendor's) | price per TB: USD 19.00 per 30 days for ~1,5 TB; USD 45.00 per 90 days for ~5 TB; USD 75.00 per 180 days for ~10 TB (vendor premium page) | source: [3]
- identity: email | detail: Sign-up page /register.html ('User Registration') with a captcha code; the form fields did not render in the capture. The premium page says 'To purchase a premium access you need to be a registered, verified and authorized user.' Premium is sold on the vendor premium page and through resellers labelled 'Official Reseller'.
- interface: unknown
- limits:
  - volume-quota (binding): 1 TB of storage on the free account [1]
  - volume-quota (binding): 650 MB per day of download (third-party figure from leechall.com) [3]
  - volume-quota (binding): premium users are limited to 55GB of download per day (24 hours), and the vendor's terms say it 'can be changed in any case if decided by our Administration' [2]
- limits note: The 1 TB is storage, not transfer. The only free-download figure is third-party, so if it holds the ratio between the two makes the free side unusable as a transfer path; the premium side is stated in the vendor terms.
- binding note: Premium plans are sold by bandwidth (about 1,5 TB for 30 days, about 5 TB for 90 days, about 10 TB for 180 days); the vendor publishes no free download volume.
- interface detail: Web upload and file manager on a subdomain (premium.isra.cloud). No API was found; the vendor publishes no endpoint.
- tooling: Browser only as read. Both Leechall and PrimeLeech carry an isra.cloud generator, so a leecher is the only scripted pull found.
- composes with: The 1 TB storage figure is the headline, but the vendor publishes no free download volume. The vendor sells premium plans on its own premium page (USD 19.00 for 30 days, USD 45.00 for 90 days, USD 75.00 for 180 days) and resellers list the same durations in EUR.
- reliability: The terms state the per-day allowance can be changed at the administration's discretion, and that a premium user's files may not be downloadable by another account even with premium.
- notes: The vendor publishes its premium plans at isra.cloud/premium.html: $19.00 for 30 days, $45.00 for 90 days and $75.00 for 180 days, one-time charge with no auto-renew; resellers list the same durations.
- evidence note: The 1 TB storage sentence is the vendor's own; its terms say 'We provide Only premium subscription services.', so whether a free account keeps that space is unverified. The premium plans, the 3 GB upload cap and the premium daily figure are vendor pages; the free daily transfer cap is a third-party statement.
- extras:
  - reseller_prices_30d: 24instant €20.00; safedeal.cc €40.00; apseller $20.00 voucher
  - premium_subdomain: premium.isra.cloud
  - daily_cap_source: third-party (leechall.com)
- evidence:
  - [1] 2026-10-23: 'You get 1 TB of space' and the cross-platform sharing claim
  - [3] 2026-10-23: third-party daily cap for the host: 'isra.cloud 0 B / 650 MB /d'
  - [4] 2026-10-23: reseller prices labelled 'Official Reseller': 'Isra Cloud 30 Days Premium 20,00 €', 'Isra Cloud 90 Days Premium 52,00 €'
  - [2] 2026-10-23: the daily allowance 'can be changed in any case if decided by our Administration' and the premium-file access restriction
  - [2] 2026-11-03: the vendor terms say the service provides only premium subscription services | capture: sha256:f7655caa8c9ed69fbbd4e80efd982cb7de7fbf9a40e011ab85236ffb3b958c05 | quote: We provide Only premium subscription services.
  - [2] 2026-11-03: the maximum size of an uploaded file is 3 GB for a Premium user | capture: sha256:f7655caa8c9ed69fbbd4e80efd982cb7de7fbf9a40e011ab85236ffb3b958c05 | quote: You agree that the maximum size of files uploaded to the service are 3 GB (for Premium User).
  - [2] 2026-11-03: the cap is stated on the terms page | capture: sha256:f7655caa8c9ed69fbbd4e80efd982cb7de7fbf9a40e011ab85236ffb3b958c05 | quote: You agree that the maximum size of files uploaded to the service are 3 GB (for Premium User).
  - [2] 2026-11-03: premium users are limited to 55GB of download per day, changeable by the administration | capture: sha256:f7655caa8c9ed69fbbd4e80efd982cb7de7fbf9a40e011ab85236ffb3b958c05 | quote: Premium users are limited to 55GB download per day (24 hours), and it can be changed in any case if decided by our Administration.
  - [5] 2026-11-03: the vendor premium page sells a 30-day plan at $19.00 with about 1,5 TB of bandwidth, a 90-day plan at $45.00 with about 5 TB and a 180-day plan at $75.00 with about 10 TB | capture: sha256:6d8f787bf88aa4ef0aa2c2ef74b56e688eb194b4f0a14fc84f3cf3dd6a2b5292 | quote: ~ 1,5 TB Bandwidth
  - [2] 2026-11-03: the row is a daily download volume figure | capture: sha256:f7655caa8c9ed69fbbd4e80efd982cb7de7fbf9a40e011ab85236ffb3b958c05 | quote: Premium users are limited to 55GB download per day (24 hours), and it can be changed in any case if decided by our Administration.
  - [2] 2026-11-03: the premium daily limit is 55GB per 24 hours and can be changed by the administration | capture: sha256:f7655caa8c9ed69fbbd4e80efd982cb7de7fbf9a40e011ab85236ffb3b958c05 | quote: Premium users are limited to 55GB download per day (24 hours), and it can be changed in any case if decided by our Administration.
  - [3] 2026-11-03: a third-party leecher still lists 650 MB/day for the host | capture: sha256:e84c300476217086e5c5520066523963a39329436dceab3c3019eaab8d16d271 | quote: isra.cloud 0 B / 650 MB /d
  - [5] 2026-11-03: the vendor premium page sells a 30-day plan with about 1,5 TB of bandwidth | capture: sha256:6d8f787bf88aa4ef0aa2c2ef74b56e688eb194b4f0a14fc84f3cf3dd6a2b5292 | quote: ~ 1,5 TB Bandwidth
  - [5] 2026-11-03: the vendor premium page lists a 30-day plan at $19.00 | capture: sha256:6d8f787bf88aa4ef0aa2c2ef74b56e688eb194b4f0a14fc84f3cf3dd6a2b5292 | quote: $19.00
  - [5] 2026-11-03: buying premium needs a registered, verified and authorized account | capture: sha256:6d8f787bf88aa4ef0aa2c2ef74b56e688eb194b4f0a14fc84f3cf3dd6a2b5292 | quote: To purchase a premium access you need to be a registered, verified and authorized user.
  - [5] 2026-11-03: the 30-day plan is $19.00 with about 1,5 TB of bandwidth | capture: sha256:6d8f787bf88aa4ef0aa2c2ef74b56e688eb194b4f0a14fc84f3cf3dd6a2b5292 | quote: ~ 1,5 TB Bandwidth
  - [5] 2026-11-03: the premium page lists three priced plans with a one-time charge and no auto-renew | capture: sha256:6d8f787bf88aa4ef0aa2c2ef74b56e688eb194b4f0a14fc84f3cf3dd6a2b5292 | quote: We don't have auto renews & subscription! Charge is one time only
  - [2] 2026-11-03: the terms describe a premium-only service | capture: sha256:f7655caa8c9ed69fbbd4e80efd982cb7de7fbf9a40e011ab85236ffb3b958c05 | quote: We provide Only premium subscription services.
  - [5] 2026-11-03: the vendor premium page lists 30 days at $19.00 (about 1,5 TB), 90 days at $45.00 (about 5 TB) and 180 days at $75.00 (about 10 TB) | capture: sha256:6d8f787bf88aa4ef0aa2c2ef74b56e688eb194b4f0a14fc84f3cf3dd6a2b5292 | quote: $19.00
  - [4] 2026-11-03: the reseller still lists 30 days at 20,00 EUR; 90 days at 52,00 EUR and 180 days at 85,00 EUR | capture: sha256:8688a325c775f145ee44fd4b3fa8d5fce1a182f2d67b368ce07fe7da5e6f3030 | quote: Isra Cloud 30 Days Premium 20,00 €
  - [6] 2026-11-03: the sign-up page is live and shows a captcha code; its form fields did not render in the capture | capture: sha256:894acbd378c2ac2fdabcfe51d1a90c726bb4b924df7f02b5b6c8cd9dbac9d06a | quote: User Registration
  - [1] 2026-11-03: the landing page still states 1 TB of space | capture: sha256:f60973d4c4954f6775ebb3c7703c10ac249d241d144b8be85b6322e800c3b54c | quote: You get 1 TB of space
- sources:
  - [1] https://isra.cloud/
  - [2] https://isra.cloud/tos.html
  - [3] https://leechall.com/
  - [4] https://www.24instant.com/en/139-isra-cloud
  - [5] https://isra.cloud/premium.html
  - [6] https://isra.cloud/register.html
