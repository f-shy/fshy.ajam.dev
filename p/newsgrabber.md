# NewsGrabber

> newsgrabber.nl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/newsgrabber/ | JSON https://fshy.ajam.dev/api/v1/entity/newsgrabber.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NewsGrabber

- `debrid/newsgrabber` | paid-only | evidence documented | binding per-ip-shaping | category usenet provider (Dutch, prepaid speed-tiered packages) | tier 10 Mbit/s
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://www.newsgrabber.nl/
- free tier: No free tier and no trial on the packages page read; a 1-week package starts at EUR 1.75. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: unverified: the packages page defers retention to an announcements page that was not read | source: [1]
- egress: Packages are tiered by maximum speed (10 to 200 Mbit/s and unlimited); no download volume cap is listed | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: Payment is handled by MultiSafePay and PayPal and the account is active on successful payment. Further signup fields are unverified: behind a sign-up.
- interface: nntp
- limits:
  - per-ip-shaping (binding): speed tiers from 10 Mbit/s to unlimited [1]
  - request-rate: 20 to 50 connections at the same time [1]
- limits note: The 10 Mbit/s package is EUR 1.75 for 1 week, EUR 5.00 for 1 month, EUR 14.25 for 3 months, EUR 27.00 for 6 months and EUR 48.00 for 1 year; the unlimited-speed package is EUR 4.25 a week and EUR 15.00 a month.
- binding note: No volume cap is listed; the speed tier decides the monthly volume.
- interface detail: NNTP with a free anonymous SSL port
- composes with: Prepaid with no automatic renewal: an account stops at the end of its period, which makes a one-week package a cheap short-term fill.
- reliability: Retention and backbone were not read on the pages captured.
- notes: Priced per period and speed tier, not per terabyte.
- evidence note: Prices and connection counts are from the vendor packages page read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: the 10 Mbit/s package costs 1.75 a week, 5.00 a month and 48.00 a year in EUR | capture: sha256:61f99d12a6e2e0e10cde0e11e680dbe1dadd0d7b78c21ee24c7d5b9be9784e4b | quote: 1,75 | 5.00 | 14,25.00 | 27,00 | 48,00 |
  - [1] 2026-11-03: packages are prepaid and end without renewal | capture: sha256:61f99d12a6e2e0e10cde0e11e680dbe1dadd0d7b78c21ee24c7d5b9be9784e4b | quote: **Prepaid, so no notice required. After the expiry of your subscription period your usenet account stops.**
  - [1] 2026-11-03: 20 to 50 connections depending on the package | capture: sha256:61f99d12a6e2e0e10cde0e11e680dbe1dadd0d7b78c21ee24c7d5b9be9784e4b | quote: Access with 20 to 50 connections at the same time.
- sources:
  - [1] https://www.newsgrabber.nl/en/usenet-packages/
