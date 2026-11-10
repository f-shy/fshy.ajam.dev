# Datarade

> datarade.ai | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datarade/ | JSON https://fshy.ajam.dev/api/v1/entity/datarade.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Datarade (storage/datarade)

- `storage/datarade` | fails-quota | evidence reported | binding none | category data-marketplace
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datarade.ai
- free tier: Zero bytes hosted. Datarade is explicitly a discovery and brokerage layer: it 'doesn't host or deliver data, instead, it focuses on discovery, comparability, and transparency'. Providers list a data product with metadata and a link; the bytes stay wherever the provider already keeps them. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A. No delivery. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: fails-quota absolutely. Even the commercial model is commission-only ($0/year + 30%, or $6,000/yr + 20%), so listing is free but delivers nothing.
- interface detail: web
- tooling: Provider Studio for listings, no storage API. There is no upload endpoint because there is no object store.
- composes with: None. A listing is metadata; it consumes no quota and provides none.
- reliability: Data marketplace directory platform. Hosts dataset metadata, vendor descriptions, and external links rather than raw data files.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Zero bytes hosted. Datarade is explicitly a discovery and brokerage layer: it 'doesn't host or deliver data, instead, it focuses on discovery, comparability, and transparency'. Providers list a data product with metadata and a link; the bytes stay wherever the provider already keeps them.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: surfaced with the decisive line: 'doesn't host or deliver data, instead, it focuses on discovery, comparability, and transparency'.
  - [2] 2026-10-21: surfaced: 'Pricing that grows with you … Every tier puts your data products in front of them' — listing tiers, no storage tiers.
  - [3] 2026-10-21: surfaced: 'Commission-only Free $0/year; + 30% commission · 3 listings · 3 contact requ[ests]'.
- sources:
  - [1] https://datarade.ai/company/blog/ai-ready-data-marketplaces
  - [2] https://providers.datarade.ai/apply
  - [3] https://techyorker.com/products/datarade-marketplace/pricing/

## datarade (see candidate entry)

- `storage/datarade-see-candidate-entry` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datarade.ai/company/blog/ai-ready-data-marketplaces
- free tier: none reachable: A brokerage that stores no bytes on principle: 'doesn't host or deliver data'. The whole 'data marketplace' category (Datarade, data.world, AWS Data Exchange, Snowflake Marketplace listings) | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: A brokerage that stores no bytes on principle: 'doesn't host or deliver data'. The whole 'data marketplace' category (Datarade, data.world, AWS Data Exchange, Snowflake Marketplace listings)
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: A brokerage that stores no bytes on principle: 'doesn't host or deliver data'. The whole 'data marketplace' category (Datarade, data.world, AWS Data Exchange, Snowflake Marketplace listings)
- sources:
  - [1] https://datarade.ai/company/blog/ai-ready-data-marketplaces
