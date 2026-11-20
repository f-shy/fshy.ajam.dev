# SnelNL

> snelnl.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/snelnl/ | JSON https://fshy.ajam.dev/api/v1/entity/snelnl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SnelNL

- `debrid/snelnl` | trial-only | evidence documented | binding per-ip-shaping | category usenet provider (Dutch, speed-tiered unlimited plans) | tier Slow
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:25:56.571Z (live) | stale on 2026-12-04
- url https://www.snelnl.com/
- free tier: Free trial of 3 days/10 GB on each plan (Slow, Basic, Fast); no ongoing free tier. | unit: mixed | metered on: none | read on: 2026-11-03 | source: [1] | note: Trial is 3 days/10 GB; which of the two limits ends it first, and the fields the trial order form asks for, are unverified: behind a sign-up. The unit is mixed because the trial is bounded in days and in GB.
- per-object cap: source: [1]
- retention: unverified: the vendor page read does not state retention; a third-party index says over 1,100 days | source: [1]
- egress: Unlimited downloads on all three plans; tiered by speed 5, 60 and 1000 Mbit | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: unverified: the order form was not opened, so the fields it asks for are behind a sign-up; a third-party index lists card, PayPal, iDEAL and Paysafe.
- interface: nntp
- limits:
  - per-ip-shaping (binding): 5 Mbit, 60 Mbit and 1000 Mbit download speed by plan [1]
- limits note: Starting at EUR 3.95 a month (Slow), EUR 6.95 (Basic) and EUR 8.95 (Fast), per the vendor page and a third-party index.
- binding note: No volume cap; the speed tier bounds a month.
- interface detail: NNTP; the vendor bundles its own downloading and streaming software
- composes with: The Slow plan is capped at 5 Mbit; Basic and Fast raise the cap, all at unlimited volume.
- reliability: Backbone and retention are not stated on the vendor page read.
- notes: Verdict is trial-only: the vendor offers a 3 days/10 GB free trial on each plan and no ongoing free tier.
- evidence note: Prices and speeds are from the vendor products page read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: the cheapest plan starts at EUR 3.95 a month | capture: sha256:2906f125970e8a6ea2c640f8e1e7572993b57879f07317e38bcb29b0606fd2c3 | quote: - Starting at € 3,95 p/month
  - [1] 2026-11-03: the cheapest plan is capped at 5 Mbit | capture: sha256:2906f125970e8a6ea2c640f8e1e7572993b57879f07317e38bcb29b0606fd2c3 | quote: - 5 Mbit downloadspeed
  - [1] 2026-11-03: downloads are unlimited | capture: sha256:2906f125970e8a6ea2c640f8e1e7572993b57879f07317e38bcb29b0606fd2c3 | quote: - Unlimited Downloads
  - [2] 2026-11-03: a third-party index states three plan prices, 1,100 days retention and a 3-day trial | capture: sha256:5f2b6ae389444f537297ae9ff1cc1c0518e7ac71afdf8c54c391002b88ae9ae7 | quote: SnelNL is a Dutch Usenet provider with three speed-tiered plans: Slow (5 Mbps, €3.95/month), Basic (60 Mbps, €6.95/month), and Fast (1,000 Mbps, €8.95/month). Over 1,100 days retention, 100,000+ newsgroups, SSL, free newsreader with streaming, 3-day trial. Credit card, PayPal, iDEAL, Paysafe.
  - [3] 2026-11-03: the vendor's test-accounts page offers a free trial period on its subscriptions (Free test! on Slow, Basic and Fast) | capture: sha256:ccda0bb306bf506d05dc163284224895bb61ce0376582f33e828f70ab992de77 | quote: # Start your free trial period
  - [4] 2026-11-03: the vendor's trial is 3 days or 10 GB | capture: sha256:88b3804aeef025cb40536227ab1e61b6efec49c8f1a5b8fa6e333deb1a6be12d | quote: a referred customer subscribes for a free trial period of 3 days/10 GB
- sources:
  - [1] https://www.snelnl.com/en/products
  - [2] https://www.usenet.org/providers/snelnl
  - [3] https://www.snelnl.com/en/test-accounts
  - [4] https://www.snelnl.com/en/affiliate
