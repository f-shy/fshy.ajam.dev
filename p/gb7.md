# gb7.pl

> gb7.pl | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gb7/ | JSON https://fshy.ajam.dev/api/v1/entity/gb7.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## gb7.pl

- `debrid/gb7-pl` | paid-only | evidence documented | binding volume-quota | category multi-hoster (Polish; daily transfer limit on a time account) | tier 50GB/24H
- needs card no, phone no, ID no, institution no | verified 2026-11-25T12:00:08.353Z (live) | stale on 2026-12-26
- url https://gb7.pl/premium
- free tier: unverified: the pricing page ties the daily Premium Limit to a purchase; no free allowance is stated on it | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The registration page of the same operator lists the daily limit among the advantages of registering, which does not say whether it applies before a purchase.
- per-object cap: unverified: no per-file cap is stated on the pricing page | source: [1]
- retention: unverified: not stated | source: [1]
- egress: 50GB / 24H Premium Limit credited daily at midnight; unused transfer accumulates up to 200GB. Extra transfer packs are sold separately. | metered: yes | free allowance: none stated | source: [1]
- identity: email | detail: A registration page and a login exist; payment by BLIK, e-transfer or card is listed. The form fields were not rendered, so the email requirement is unverified.
- interface: unknown
- limits:
  - volume-quota (binding): 50GB / 24H, accumulating to 200GB [1]
- binding note: The daily Premium Limit in bytes is the stated cap; accumulation raises the ceiling on a single day.
- interface detail: Web account panel; the same operator's family of sites uses one template.
- tooling: Browser; JDownloader and pyLoad support is claimed only by third-party lists.
- composes with: Sibling sites of one operator at different daily limits: tb7.pl (10GB), xt7.pl (20GB), gb7.pl (50GB).
- reliability: No outage observed on the day read.
- notes: Plans listed at 59.99, 109.99, 149.99 and 199.99 zloty; extra transfer 50GB at 8.99, 100GB at 15.99, 200GB at 29.99. A Black Week banner offers 20 percent extra days up to 27 November 2026.
- evidence note: First-party pricing page read once; prices in zloty.
- evidence:
  - [1] 2026-11-03: 50 GB Premium Limit credited daily at midnight on purchase | capture: sha256:be91e027a34f1c8c5938f0dc2e44d30625fc17a8fd46f203421356977d82a323 | quote: Po zakupie oraz codziennie o północy na Twoje konto wpływa 50GB Limitu Premium do wykorzystania na pobieranie.
  - [1] 2026-11-03: unused transfer accumulates up to 200 GB | capture: sha256:be91e027a34f1c8c5938f0dc2e44d30625fc17a8fd46f203421356977d82a323 | quote: Niewykorzystany transfer przechodzi na kolejny dzień i kumuluje się do maksymalnie 200GB!
  - [1] 2026-11-03: the 30-day plan is listed at 59.99 zl | capture: sha256:be91e027a34f1c8c5938f0dc2e44d30625fc17a8fd46f203421356977d82a323 | quote: 30 DNI 59.99 zł
  - [1] 2026-11-03: an extra 50 GB of transfer is listed at 8.99 zl | capture: sha256:be91e027a34f1c8c5938f0dc2e44d30625fc17a8fd46f203421356977d82a323 | quote: 50GB 8.99 zł
  - [1] 2026-11-25: 50 GB is credited daily at midnight, accumulates to 200 GB, and the four plan prices are unchanged | capture: sha256:0ba28ef6acb5ffab9f4e217cc41d1a06a7facd3120f23c45a21853f30fcff334 | quote: Po zakupie oraz codziennie o północy na Twoje konto wpływa 50GB Limitu Premium do wykorzystania na pobieranie. ... Niewykorzystany transfer przechodzi na kolejny dzień i kumuluje się do maksymalnie 200GB! ... 30 DNI ... 59.99 zł ... 100 DNI ... 109.99 zł ... 180 DNI ... 149.99 zł ... 300 DNI ... 199.99 zł
  - [1] 2026-11-25: a Black Week campaign adds 20 percent bonus days until 27 Nov 2026 | capture: sha256:0ba28ef6acb5ffab9f4e217cc41d1a06a7facd3120f23c45a21853f30fcff334 | quote: BLACK WEEK+20% dni GRATIS do każdego nowo zakupionego dostępu Premium!Promocja trwa do **piątku 27 listopada, godz. 23:59**. Przykład: 30 dni → 36 dni, 300 dni → 360 dni.
  - [2] 2026-11-25: the registration page lists BLIK, e-transfer or card as payment rails | capture: sha256:476391fe0f89dad6ca9dccdb21cc35dc0416e24f812bda449fa41b46a1037808 | quote: - płatność BLIK-iem, e-przelewem lub kartą
  - [1] 2026-11-25: a Black Week banner offers 20 percent bonus days on newly purchased Premium access until 27 November 2026 | capture: sha256:db8ba34e75a06d4f6b5c1ecb95c08b3727458386cb8c700d4c2b38fb1d7ac449 | quote: BLACK WEEK+20% dni GRATIS do każdego nowo zakupionego dostępu Premium!Promocja trwa do **piątku 27 listopada, godz. 23:59**. Przykład: 30 dni → 36 dni, 300 dni → 360 dni.
  - [1] 2026-11-25: the Black Week bonus-days banner is present on the pricing page | capture: sha256:db8ba34e75a06d4f6b5c1ecb95c08b3727458386cb8c700d4c2b38fb1d7ac449 | quote: BLACK WEEK+20% dni GRATIS do każdego nowo zakupionego dostępu Premium!Promocja trwa do **piątku 27 listopada, godz. 23:59**. Przykład: 30 dni → 36 dni, 300 dni → 360 dni.
- sources:
  - [1] https://gb7.pl/premium
  - [2] https://gb7.pl/rejestracja
