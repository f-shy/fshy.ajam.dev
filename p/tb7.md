# tb7.pl

> tb7.pl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tb7/ | JSON https://fshy.ajam.dev/api/v1/entity/tb7.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tb7.pl

- `debrid/tb7-pl` | paid-only | evidence documented | binding volume-quota | category multi-hoster (Polish; daily transfer limit on a time account) | tier 10GB/24H
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:13.292Z (live) | stale on 2026-12-04
- url https://tb7.pl/premium
- free tier: unverified: the pricing page ties the daily Premium Limit to a purchase; no free allowance is stated on it | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The registration page of the same operator lists the daily limit among the advantages of registering, which does not say whether it applies before a purchase.
- per-object cap: unverified: no per-file cap is stated on the pricing page | source: [1]
- retention: unverified: not stated | source: [1]
- egress: 10GB / 24H Premium Limit credited daily at midnight; unused transfer accumulates up to 40GB. Extra transfer packs are sold separately. | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: A registration page and a login exist; payment by BLIK, e-transfer or card is listed. The form fields were not rendered, so the email requirement is unverified.
- interface: unknown
- limits:
  - volume-quota (binding): 10GB / 24H, accumulating to 40GB [1]
- binding note: The daily Premium Limit in bytes is the stated cap; accumulation raises the ceiling on a single day.
- interface detail: Web account panel; the same operator's family of sites uses one template.
- tooling: Browser; JDownloader and pyLoad support is claimed only by third-party lists.
- composes with: Sibling sites of one operator at different daily limits: tb7.pl (10GB), xt7.pl (20GB), gb7.pl (50GB).
- reliability: No outage observed on the day read.
- notes: Cheapest plans: 24 H at 4.99 zl, 30 days at 14.99 zl; two prices are listed per plan and the column labels were not captured. Extra transfer 10GB at 2.99 zl.
- evidence note: First-party pricing page read once; prices in zloty.
- evidence:
  - [1] 2026-11-03: 10 GB Premium Limit credited daily at midnight on purchase | capture: sha256:793ee9e15f251a032bd8b2cfce9c2c5f8e979bfbf646da5a6585e20c2f2a0f00 | quote: Po zakupie oraz codziennie o północy na Twoje konto wpływa 10GB Limitu Premium do wykorzystania na pobieranie.
  - [1] 2026-11-03: unused transfer accumulates up to 40 GB | capture: sha256:793ee9e15f251a032bd8b2cfce9c2c5f8e979bfbf646da5a6585e20c2f2a0f00 | quote: Niewykorzystany transfer przechodzi na kolejny dzień i kumuluje się do maksymalnie 40GB!
  - [1] 2026-11-03: the 24-hour plan is listed at 4.99 zl | capture: sha256:793ee9e15f251a032bd8b2cfce9c2c5f8e979bfbf646da5a6585e20c2f2a0f00 | quote: 24 H 4.99 zł
  - [1] 2026-11-03: the 30-day plan is listed at 14.99 zl | capture: sha256:793ee9e15f251a032bd8b2cfce9c2c5f8e979bfbf646da5a6585e20c2f2a0f00 | quote: 30 DNI 14.99 zł
  - [1] 2026-11-03: an extra 10 GB of transfer is listed at 2.99 zl | capture: sha256:793ee9e15f251a032bd8b2cfce9c2c5f8e979bfbf646da5a6585e20c2f2a0f00 | quote: 10GB 2.99 zł
  - [2] 2026-11-03: payment by BLIK, e-transfer or card | capture: sha256:6b06cf6fea9c204551332f350a029b3469ca249defdf45691169952f8cfdb248 | quote: - płatność BLIK-iem, e-przelewem lub kartą
  - [2] 2026-11-03: the registration page lists the 10GB daily limit as an advantage of registering | capture: sha256:6b06cf6fea9c204551332f350a029b3469ca249defdf45691169952f8cfdb248 | quote: - 10GB / 24H + Kumulacja do 40GB
- sources:
  - [1] https://tb7.pl/premium
  - [2] https://tb7.pl/rejestracja
