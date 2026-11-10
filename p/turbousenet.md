# TurboUsenet

> turbousenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/turbousenet/ | JSON https://fshy.ajam.dev/api/v1/entity/turbousenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TurboUsenet

- `debrid/turbousenet` | paid-only | evidence reported | binding request-rate | category usenet provider (Dutch, one unlimited plan with one-off payments) | tier TurboTurbo
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-11-18
- url https://turbousenet.com/
- free tier: No free tier and no trial on the order page read; the order summary shows TurboTurbo for 365 days at EUR 54.95. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: unverified: the order page read does not state retention; a third-party index says over 3,900 days | source: [1]
- egress: Unlimited speed and unlimited data on the single plan (third-party index) | metered: no | free allowance: unlimited | source: [2]
- identity: card | detail: The order page says payments are one-off and 'We do not store info'; the form fields were not read: unverified: behind a sign-up.
- interface: nntp
- limits:
  - request-rate (binding): 50 connections (third-party index) [2]
- limits note: TurboTurbo for 365 days is EUR 54.95; the shorter periods were not read.
- binding note: Speed and volume are unlimited per the third-party index, so the connection count is the stated bound.
- interface detail: NNTP
- composes with: One plan priced per day; the order page shows the 365-day price, and the vendor says payments are one-off, so there is no renewal to cancel.
- reliability: The order page names NectoFarm B.V. as the statement name; the backbone is not stated by the vendor.
- notes: Priced per period.
- evidence note: The 365-day price is on the vendor order page; plan limits are from a third-party index.
- evidence:
  - [1] 2026-11-03: the order summary prices the plan at EUR 54.95 | capture: sha256:cda2186bbcc79e300d03c665aa872f888793fefea716b7d7d611b128f8d87e44 | quote: Total cost: € 54,95
  - [1] 2026-11-03: the EUR 54.95 covers 365 days | capture: sha256:cda2186bbcc79e300d03c665aa872f888793fefea716b7d7d611b128f8d87e44 | quote: Duration: 365 days
  - [2] 2026-11-03: a third-party index states unlimited speed, 50 connections and over 3,900 days retention | capture: sha256:de22f4ce677b5c3b0ec355bcd0a1ff09f55e2a2cb228cb47edd25cc5921188fa | quote: TurboUsenet is a Dutch provider based in Arnhem, offering a single no-nonsense plan called TurboTurbo – unlimited speed, 50 connections, over 3,900 days retention, and transparent per-day pricing. Perfect for users who want Usenet without the frills.
- sources:
  - [1] https://turbousenet.com/en/order/
  - [2] https://www.usenet.org/providers/turbousenet
