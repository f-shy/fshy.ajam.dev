# RADAR

> radar-service.eu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/radar-service/ | JSON https://fshy.ajam.dev/api/v1/entity/radar-service.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RADAR (FIZ Karlsruhe)

- `storage/radar` | fails-quota | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:58.036Z (live) | stale on 2026-12-04
- url https://www.radar-service.eu
- free tier: Paid institutional service, no free self-serve tier. Targeted at institutions and research groups buying a data-publication contract, not at individuals storing bulk data. | unit: none | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free downloads for published records; delivery via the RADAR web/API. | metered: no
- identity: institution
- interface: rest
- limits note: Volume is set by contract; no published free allowance.
- interface detail: rest
- tooling: REST API, OAI-PMH; institutional SSO.
- composes with: None free. Contracts are per-institution with a defined volume.
- reliability: Sound archival service, but irrelevant without a purchasing institution behind it.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: paid
  - dead_end.why: Paid institutional service, no free self-serve tier. Targeted at institutions and research groups buying a data-publication contract, not at individuals storing bulk data.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: variants page exists but body extraction returned empty; no free tier visible
  - [2] 2026-10-21: public search UI only, no self-registration for deposit
  - [1] 2026-11-19: RADAR is sold only to institutions under a paid annual service agreement, with no free self-serve tier | capture: sha256:a28ca2726a756b3d1977c6e589eacd8c64da4842809e02639f76624c9e02e429 | quote: RADAR Cloud is subject to a service agreement between your institution and FIZ Karlsruhe. Billing is done annually and includes a basic fee and a volume-based fee component.
- sources:
  - [1] https://radar.products.fiz-karlsruhe.de/en/radarvariants/betriebsvarianten
  - [2] https://www.radar-service.eu/radar/en/home
