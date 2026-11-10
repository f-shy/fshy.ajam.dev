# xt7.pl

> xt7.pl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/xt7/ | JSON https://fshy.ajam.dev/api/v1/entity/xt7.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## xt7.pl

- `debrid/xt7-pl` | paid-only | evidence documented | binding volume-quota | category multi-hoster (Polish; daily transfer limit on a time account) | tier 20GB/24H
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://xt7.pl/premium
- free tier: unverified: the pricing page ties the daily Premium Limit to a purchase; no free allowance is stated on it | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The registration page of the same operator lists the daily limit among the advantages of registering, which does not say whether it applies before a purchase.
- per-object cap: unverified: no per-file cap is stated on the pricing page | source: [1]
- retention: unverified: not stated | source: [1]
- egress: 20GB / 24H Premium Limit credited daily at midnight; unused transfer accumulates up to 80GB. Extra transfer packs are sold separately. | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: A registration page and a login exist; payment by BLIK, e-transfer or card is listed. The form fields were not rendered, so the email requirement is unverified.
- interface: unknown
- limits:
  - volume-quota (binding): 20GB / 24H, accumulating to 80GB [1]
- binding note: The daily Premium Limit in bytes is the stated cap; accumulation raises the ceiling on a single day.
- interface detail: Web account panel; the same operator's family of sites uses one template.
- tooling: Browser; JDownloader and pyLoad support is claimed only by third-party lists.
- composes with: Sibling sites of one operator at different daily limits: tb7.pl (10GB), xt7.pl (20GB), gb7.pl (50GB).
- reliability: No outage observed on the day read.
- notes: Cheapest plan: 30 days at 29.99 zl; longer plans 100 days 54.99, 180 days 74.99, 300 days 99.99.
- evidence note: First-party pricing page read once; prices in zloty.
- evidence:
  - [1] 2026-11-03: 20 GB Premium Limit credited daily at midnight on purchase | capture: sha256:6561ed08b2bb832e8b7b965ba99aa8a018fd9a330496e17500205509dcfd5f16 | quote: Po zakupie oraz codziennie o północy na Twoje konto wpływa 20GB Limitu Premium do wykorzystania na pobieranie.
  - [1] 2026-11-03: unused transfer accumulates up to 80 GB | capture: sha256:6561ed08b2bb832e8b7b965ba99aa8a018fd9a330496e17500205509dcfd5f16 | quote: Niewykorzystany transfer przechodzi na kolejny dzień i kumuluje się do maksymalnie 80GB!
  - [1] 2026-11-03: the 30-day plan is listed at 29.99 zl | capture: sha256:6561ed08b2bb832e8b7b965ba99aa8a018fd9a330496e17500205509dcfd5f16 | quote: 30 DNI 29.99 zł
  - [1] 2026-11-03: the 300-day plan is listed at 99.99 zl | capture: sha256:6561ed08b2bb832e8b7b965ba99aa8a018fd9a330496e17500205509dcfd5f16 | quote: 300 DNI 99.99 zł
- sources:
  - [1] https://xt7.pl/premium
