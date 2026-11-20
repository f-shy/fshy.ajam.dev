# FreeDiscussions

> freediscussions.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/freediscussions/ | JSON https://fshy.ajam.dev/api/v1/entity/freediscussions.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FreeDiscussions

- `debrid/freediscussions` | trial-only | evidence documented | binding volume-quota | category usenet provider (volume plans with a 14-day trial) | tier Starter
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://freediscussions.com/
- free tier: A free 14-day trial on every package; a third-party index states it carries 10 GB of high-speed data. | unit: GB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: The 10 GB allowance is from usenet.org, not the vendor page.
- per-object cap: source: [1]
- retention: unverified: the packages page read does not state retention | source: [1]
- egress: Metered by plan: 35, 70 or 140 GB of high-speed data a month, plus a 600 GB flat-rate volume at 2 Mbit/s | metered: yes | free allowance: 35 GB high-speed volume per month on the smallest plan | source: [1]
- identity: email | detail: unverified: the trial signup form was not opened, so what it asks for (email, phone or card) is behind a sign-up.
- interface: nntp
- limits:
  - volume-quota (binding): 35 GB high-speed volume on Starter and Flex, 70 GB on Expert, 140 GB on Master [1]
  - per-ip-shaping: 600 GB a month flat-rate volume at a maximum of 2 Mbit/s [1]
- limits note: Starter EUR 13.99 monthly debit, Flex EUR 8.33 one-time, Expert EUR 9.83 one-time, Master EUR 14.99 one-time.
- binding note: The high-speed volume is a fixed number of GB, after which the 2 Mbit/s flat volume applies.
- interface detail: NNTP with 256-bit SSL; the vendor ships a free newsreader
- composes with: Four plans: a monthly Starter at EUR 13.99 and one-time Flex, Expert and Master volumes; every plan adds a 600 GB flat-rate volume at 2 Mbit/s that keeps a slow background download running after the high-speed volume is used.
- reliability: Backbone and retention are not stated on the vendor page read.
- notes: Volume-metered, not unlimited.
- evidence note: Plan prices and the trial are from the vendor packages page read on 2026-11-03; the 10 GB allowance is third-party.
- evidence:
  - [1] 2026-11-03: every package carries a free 14-day trial | capture: sha256:78c5fac7f6fb28618889375416d28a32259790e310b6531f59a2a61590528762 | quote: All packages have a free 14-day trial period.
  - [1] 2026-11-03: every package includes a 600 GB monthly flat-rate volume | capture: sha256:78c5fac7f6fb28618889375416d28a32259790e310b6531f59a2a61590528762 | quote: 600 GB
  - [2] 2026-11-03: a third-party index gives the trial allowance as 10 GB | capture: sha256:21ad28e1a6ddecd602f2cf8af988ec0914021be2093f90cd885439e5a7f4be2d | quote: FreeDiscussions offers a 14-day free trial with 10 GB of high-speed data access.
  - [2] 2026-11-03: the cheapest paid tier is the one-time Flex volume at EUR 8.33 | capture: sha256:21ad28e1a6ddecd602f2cf8af988ec0914021be2093f90cd885439e5a7f4be2d | quote: Flex – €8.33 one-time
  - [2] 2026-11-03: the monthly Starter plan is EUR 13.99 | capture: sha256:21ad28e1a6ddecd602f2cf8af988ec0914021be2093f90cd885439e5a7f4be2d | quote: Starter – €13.99/month
- sources:
  - [1] https://freediscussions.com/packages
  - [2] https://www.usenet.org/providers/freediscussions
