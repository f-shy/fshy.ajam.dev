# europeana

> europeana.eu | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/europeana/ | JSON https://fshy.ajam.dev/api/v1/entity/europeana.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Europeana (EU cultural heritage aggregator)

- `storage/europeana` | fails-identity | evidence reported | binding none | category gov-cultural-aggregator
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.europeana.eu/
- disagrees on identity_kind: `storage/europeana` says institution, `storage/europeana-2` says email
- disagrees on verdict: `storage/europeana` says fails-identity, `storage/europeana-2` says fails-quota
- disagrees on identity_kind: `storage/europeana` says institution, `storage/europeana-3` says email
- disagrees on verdict: `storage/europeana` says fails-identity, `storage/europeana-3` says fails-quota
- free tier: No direct deposit at all. Europeana ingests metadata via accredited national aggregators; the media object stays on the provider's own server and is only linked. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/a. Link-only. | metered: no
- identity: institution | detail: institution
- interface: unknown
- limits note: Scope test is the gate: 'Your collection is about Europe; made by a European or a European community; or owned by a European institution.' Plus aggregator intermediation, so an individual cannot submit even in-scope material directly.
- interface detail: OAI-PMH / EDM metadata submission through an aggregator. Not an object store.
- tooling: none for individuals.
- composes with: n/a.
- reliability: metadata-only even for accredited institutions, so it can never hold bytes.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No direct deposit at all — Europeana ingests metadata via accredited national aggregators; the media object stays on the provider's own server and is only linked.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Step 2 Requirements: 'The scope of your collection aligns with the Europeana Content Strategy. Your collection is about Europe; made by a European or a European community; or owned by a European institution.'
  - [2] 2026-10-21: the framework is written for data partners/aggregators supplying 'your online collection', i.e. objects remain on the partner's host
- sources:
  - [1] https://pro.europeana.eu/share-your-data/process
  - [2] https://pro.europeana.eu/post/publishing-framework

## europeana

- `storage/europeana-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.europeana.eu/en/contribute
- disagrees on identity_kind: `storage/europeana` says institution, `storage/europeana-2` says email
- disagrees on verdict: `storage/europeana` says fails-identity, `storage/europeana-2` says fails-quota
- free tier: none reachable: Aggregator, not a store. Europeana ingests metadata from accredited national aggregators and domain aggregators; an individual cannot deposit bytes, and the media stays on the provider's… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: Aggregator, not a store. Europeana ingests metadata from accredited national aggregators and domain aggregators; an individual cannot deposit bytes, and the media stays on the provider's…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Aggregator, not a store. Europeana ingests metadata from accredited national aggregators and domain aggregators; an individual cannot deposit bytes, and the media stays on the provider's…
- sources:
  - [1] https://www.europeana.eu/en/contribute

## europeana (incl. europeana 3d)

- `storage/europeana-3` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://api.europeana.eu/record/v2/json
- disagrees on identity_kind: `storage/europeana` says institution, `storage/europeana-3` says email
- disagrees on verdict: `storage/europeana` says fails-identity, `storage/europeana-3` says fails-quota
- free tier: none reachable: An aggregator, not a host. Content arrives by harvesting institutional metadata; there is no self-serve deposit and no byte storage. /share-your-collections returns nothing usable and… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: quota
  - dead_end.why: An aggregator, not a host. Content arrives by harvesting institutional metadata; there is no self-serve deposit and no byte storage. /share-your-collections returns nothing usable and…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: An aggregator, not a host. Content arrives by harvesting institutional metadata; there is no self-serve deposit and no byte storage. /share-your-collections returns nothing usable and…
  - [2] 2026-10-21: cited as the basis of the rejection: An aggregator, not a host. Content arrives by harvesting institutional metadata; there is no self-serve deposit and no byte storage. /share-your-collections returns nothing usable and api.eu
- sources:
  - [1] https://api.europeana.eu/record/v2/json
  - [2] https://pro.europeana.eu/post/contribute-your-collections-on-europe-s-migration-heritage
