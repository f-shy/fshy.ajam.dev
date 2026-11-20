# UsenetDeal

> usenetdeal.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/usenetdeal/ | JSON https://fshy.ajam.dev/api/v1/entity/usenetdeal.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## UsenetDeal

- `debrid/usenetdeal` | paid-only | evidence documented | binding per-ip-shaping | category usenet provider (Dutch, speed-tiered flats and non-expiring blocks) | tier Starter
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://usenetdeal.com/
- price EUR 15.99 for a 1000 GB block, one-time
- free tier: No free tier and no trial; a 7-day money-back guarantee is the only risk reversal on the plans. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: 3800 days of binary retention on every plan and block | days: 3800 | source: [1]
- egress: Unlimited download on the three flat plans; blocks of 500, 1000 and 2500 GB that never expire | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: unverified: the checkout was not opened, so the fields it asks for are behind a sign-up.
- interface: nntp
- limits:
  - per-ip-shaping (binding): 20 Mbit/s on Starter, 100 Mbit/s on Fast, 1000 Mbit/s on Lightspeed [1]
  - request-rate: 10 connections on Starter, 40 on Fast, 60 on Lightspeed [1]
  - volume-quota: blocks of 500, 1000 and 2500 GB with no expiry [1]
- limits note: Flats per month: Starter EUR 1.69, Fast EUR 2.89, Lightspeed EUR 3.39. Blocks one-time: 500 GB EUR 9.99, 1000 GB EUR 15.99, 2500 GB EUR 35.99. The page does not say which billing period the monthly prices assume.
- binding note: The flats are unlimited in volume, so speed and connection count bound a month; the blocks are bounded by GB.
- interface detail: NNTP with free 256-bit SSL
- composes with: Blocks of 500, 1000 and 2500 GB at 1000 Mbit/s never expire, so a one-time block is the bulk route; the flats are speed-tiered.
- reliability: Backbone is not stated on the page read; a third-party index lists Abavia.
- notes: Flats are priced per month and speed tier; blocks one-time.
- evidence note: Prices, retention and connections are from the vendor plans page read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: monthly prices of three flats with a 7-day money-back guarantee | capture: sha256:1a4e0b40abd752859eb3a57666d01e88d5ebda3c21ddc9b3456f0e98da8649c2 | quote: | | STARTER € 1,69 per month 7-day money-back guarantee | FAST € 2,89 per month 7-day money-back guarantee | LIGHTSPEED € 3,39 per month 7-day money-back guarantee |
  - [1] 2026-11-03: one-time prices of three blocks | capture: sha256:1a4e0b40abd752859eb3a57666d01e88d5ebda3c21ddc9b3456f0e98da8649c2 | quote: | | BLOCK 500 € 9,99 One-time 1000Mbit speed | BLOCK 1000 € 15,99 One-time 1000Mbit speed | BLOCK 2500 € 35,99 One-time 1000Mbit speed |
  - [1] 2026-11-03: binary retention is 3800 days | capture: sha256:1a4e0b40abd752859eb3a57666d01e88d5ebda3c21ddc9b3456f0e98da8649c2 | quote: | Binary retention | 3800 days | 3800 days | 3800 days |
  - [1] 2026-11-03: connections per flat | capture: sha256:1a4e0b40abd752859eb3a57666d01e88d5ebda3c21ddc9b3456f0e98da8649c2 | quote: | Connections | 10 connections | 40 connections | 60 connections |
  - [1] 2026-11-03: speed per flat | capture: sha256:1a4e0b40abd752859eb3a57666d01e88d5ebda3c21ddc9b3456f0e98da8649c2 | quote: | Usenet speed | 20 Mbit/s | 100 Mbit/s | 1000 Mbit/s |
- sources:
  - [1] https://usenetdeal.com/usenet/
