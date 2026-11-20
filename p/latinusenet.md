# LatinUsenet

> latinusenet.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/latinusenet/ | JSON https://fshy.ajam.dev/api/v1/entity/latinusenet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LatinUsenet

- `debrid/latinusenet` | paid-only | evidence documented | binding per-ip-shaping | category usenet provider (Spanish-language, unlimited flats and volume plans) | tier Unlimited 10 mbps
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:37:14.439Z (live) | stale on 2026-12-04
- url https://latinusenet.com/
- free tier: No free tier and no trial on the plans page read; four unlimited plans from USD 5 a month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: source: [1]
- retention: unverified: the plans page read does not state retention | source: [1]
- egress: Unlimited downloads on the four flat plans; speed tiers 10, 25, 50 and 100 mbps | metered: no | free allowance: unlimited | source: [1]
- identity: card | detail: unverified: the checkout was not opened, so the fields it asks for are behind a sign-up.
- interface: nntp
- limits:
  - per-ip-shaping (binding): speed tiers of 10, 25, 50 and 100 mbps [1]
  - request-rate: 10 simultaneous connections on the 10 mbps plan, up to 100 on the 100 mbps plan [1]
- limits note: Monthly: USD 5, 7, 9 and 12 for 10, 25, 50 and 100 mbps. Billed yearly: USD 4.17, 5.83, 7.50 and 10.00 a month (USD 50, 70, 90 and 120 a year).
- binding note: Downloads are unlimited; the speed tier and its connection count decide what a month retrieves.
- interface detail: NNTP with 256-bit SSL/TLS protection
- composes with: The cheapest flat is speed-capped at 10 mbps with 10 connections; a volume-based plan with no expiry date also exists on a separate page.
- reliability: Backbone and retention are not stated on the plans page read.
- notes: Unlimited volume, priced per month and speed tier.
- evidence note: Prices, speeds and connection counts are from the vendor plans page read on 2026-11-03.
- evidence:
  - [1] 2026-11-03: the cheapest monthly plan is USD 5.00 | capture: sha256:896c3be1ab9503b676c1e483a30f6b27050e6ee2aca19ebca2ccb962bb8b1b1c | quote: ## $5.00/mes
  - [1] 2026-11-03: the cheapest yearly-billed plan is USD 4.17 a month | capture: sha256:896c3be1ab9503b676c1e483a30f6b27050e6ee2aca19ebca2ccb962bb8b1b1c | quote: ## $4.17/mes
  - [1] 2026-11-03: 10 connections on the cheapest plan | capture: sha256:896c3be1ab9503b676c1e483a30f6b27050e6ee2aca19ebca2ccb962bb8b1b1c | quote: - 10 conexiones simultáneas
  - [1] 2026-11-03: downloads are unlimited on the flat plans | capture: sha256:896c3be1ab9503b676c1e483a30f6b27050e6ee2aca19ebca2ccb962bb8b1b1c | quote: - Descargas ilimitadas
  - [1] 2026-11-03: the cheapest plan is capped at 10 mbps | capture: sha256:896c3be1ab9503b676c1e483a30f6b27050e6ee2aca19ebca2ccb962bb8b1b1c | quote: - Conexión a 10 mbps
- sources:
  - [1] https://latinusenet.com/planes/
