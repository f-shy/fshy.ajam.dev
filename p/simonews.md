# simonews

> simonews.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/simonews/ | JSON https://fshy.ajam.dev/api/v1/entity/simonews.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## simonews

- `debrid/simonews` | qualifies-with-caveat | evidence documented | binding volume-quota | category usenet provider (German, volume subscriptions and 5-year prepaid accounts) | tier 25 Gigabyte monthly
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://www.simonews.com/
- free tier: Free demo account: 0.5 Gigabyte for 7 days at EUR 0.00, confirmed with a free SMS code to a mobile phone; one new demo per phone number and email address every 90 days. | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: The demo needs a mobile number; a landline works through a hang-up call to a stated number.
- per-object cap: source: [2]
- retention: 1600 days of Usenet retention ('1600 Tage Usenet Retention') | days: 1600 | source: [3]
- egress: Monthly volume of 25, 75 or 150 GB, or flat rates of 1, 4 or 16 Mbit/s; 5-year accounts of 25 to 500 GB | metered: yes | free allowance: 0.5 GB demo over 7 days | source: [2]
- identity: any-phone | detail: The demo sends 'a free SMS code to your mobile phone which you have to confirm on this page'; a landline is accepted by a hang-up call. The paid order form was not opened: unverified: behind a sign-up.
- interface: nntp
- limits:
  - volume-quota (binding): 25, 75 and 150 GB per month; 5-year accounts of 25, 100, 200 and 500 GB [2]
  - retention-clamped: 1600 days of retention [3]
- limits note: Monthly: 25 GB EUR 5.95, 75 GB EUR 13.95, 150 GB EUR 23.95; flat rates 1 Mbit/s EUR 11.95, 4 Mbit/s EUR 18.95, 16 Mbit/s EUR 29.95. EU prices include VAT.
- binding note: Every paid product is a fixed volume or a speed-capped flat; the demo is 0.5 GB.
- interface detail: NNTP; the vendor page names a Usenet server per account
- composes with: The 5-year accounts do not renew: 25 GB for EUR 10.00 up to 500 GB for EUR 100.00, so a bulk block can be held for years.
- reliability: Backbone is not stated on the vendor pages read.
- notes: The free demo is 0.5 GB, enough to test the service only; prices are in euro and volume-metered.
- evidence note: Demo terms, prices and retention are from the vendor pages read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: the demo is 0.5 GB for 7 days at no charge | capture: sha256:4c6c2222442fae2d2d6743b4971851b7eb9a5dbd5ab2c99265a377f33617ebc9 | quote: Free Demo Account 0.5 Gigabyte / 7 Tage = € 0.00
  - [1] 2026-11-03: the demo needs a phone that can receive an SMS code | capture: sha256:4c6c2222442fae2d2d6743b4971851b7eb9a5dbd5ab2c99265a377f33617ebc9 | quote: To avoid muliple demo accounts we are going to send a free SMS code to your mobile phone which you have to confirm on this page.
  - [1] 2026-11-03: the demo can be repeated every 90 days per phone number and email | capture: sha256:4c6c2222442fae2d2d6743b4971851b7eb9a5dbd5ab2c99265a377f33617ebc9 | quote: For every phone number and email address used, you may order a new demo account every 90 days.
  - [2] 2026-11-03: the smallest monthly subscription is 25 GB at EUR 5.95 | capture: sha256:e05eb0271228b2333d35ae5c51592ddfa98ea171f4838f1bf64da708ae347c6d | quote: | 25 Gigabyte | € 5.95 p.m. |
  - [2] 2026-11-03: the smallest 5-year account is 25 GB at EUR 10.00 | capture: sha256:e05eb0271228b2333d35ae5c51592ddfa98ea171f4838f1bf64da708ae347c6d | quote: | 25 Gigabyte | € 10.00 |
  - [3] 2026-11-03: retention is 1600 days | capture: sha256:a24f84e8a40d595eeafbcb024622baee61bd0937896195b505877345f78c119f | quote: # 1600 Tage Usenet Retention
- sources:
  - [1] https://www.simonews.com/usenet_server/english/test_zugang/
  - [2] https://www.simonews.com/usenet_server/english/preise/
  - [3] https://www.simonews.com/
