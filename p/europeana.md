# europeana

> europeana.eu | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/europeana/ | JSON https://fshy.ajam.dev/api/v1/entity/europeana.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Europeana (EU cultural heritage aggregator)

- `storage/europeana` | fails-identity | evidence reported | binding none | category gov-cultural-aggregator
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:13:31.791Z (live) | stale on 2026-12-04
- url https://www.europeana.eu/
- disagrees on identity_kind: `storage/europeana` says institution, `storage/europeana-2` says email
- disagrees on verdict: `storage/europeana` says fails-identity, `storage/europeana-2` says fails-quota
- disagrees on identity_kind: `storage/europeana` says institution, `storage/europeana-3` says email
- disagrees on verdict: `storage/europeana` says fails-identity, `storage/europeana-3` says fails-quota
- free tier: No direct deposit at all. Europeana ingests metadata through accredited national aggregators; the media object stays on the provider's own server and is only linked. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [2] | note: not stated
- retention: source: [2] | note: not stated
- egress: N/a. Link-only. | metered: no
- identity: institution | detail: institution
- interface: unknown
- limits note: Scope test is the gate: 'Your collection is about Europe; made by a European or a European community; or owned by a European institution.' Plus aggregator intermediation, so an individual cannot submit even in-scope material directly.
- interface detail: OAI-PMH / EDM metadata submission through an aggregator. Not an object store.
- tooling: none for individuals.
- composes with: n/a.
- reliability: metadata-only even for accredited institutions, so it can never hold bytes.
- notes: No direct deposit at all. Europeana ingests metadata via accredited national aggregators; the media object stays on the provider's own server and is only linked.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No direct deposit at all — Europeana ingests metadata via accredited national aggregators; the media object stays on the provider's own server and is only linked.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: Step 2 Requirements: 'The scope of your collection aligns with the Europeana Content Strategy. Your collection is about Europe; made by a European or a European community; or owned by a European institution.'
  - [3] 2026-10-21: the framework is written for data partners/aggregators supplying 'your online collection', i.e. objects remain on the partner's host
  - [1] 2026-11-19: current share-your-collections page addresses institutions only | capture: sha256:757bd3266493e84a9c9e5497154298ab3787d73b093a911081486d9d8612b9cb | quote: Do you work for an institution that has digitised European cultural heritage collections? Get in touch with us to share them on Europeana.eu.
  - [1] 2026-11-19: current share page states aggregators assist institutions at every step | capture: sha256:757bd3266493e84a9c9e5497154298ab3787d73b093a911081486d9d8612b9cb | quote: We offer easy-to-use resources and training to support you, and our network of aggregators will assist you at every step of the process.
  - [1] 2026-11-19: share page addresses institutions with digitised cultural heritage collections | capture: sha256:757bd3266493e84a9c9e5497154298ab3787d73b093a911081486d9d8612b9cb | quote: Do you work for an institution that has digitised European cultural heritage collections? Get in touch with us to share them on Europeana.eu.
  - [2] 2026-11-19: the old process URL now resolves to the Europeana Knowledge Base | capture: sha256:84defe449e37ee0a0f4b4201da81a00c5bcea838676b5934e90af9261500999e | quote: Europeana Knowledge Base
- sources:
  - [1] https://www.europeana.eu/en/share-your-collections
  - [2] https://pro.europeana.eu/share-your-data/process
  - [3] https://pro.europeana.eu/post/publishing-framework

## europeana

- `storage/europeana-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:36.464Z (inherited) | stale on 2026-12-04
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
- reliability: unverified: https://www.europeana.eu/en/contribute answered HTTP 403 on 2026-11-19 (challenge); the aggregator claim could not be re-read from its first-party page; alternate retrieval routes failed and a probe confirmed HTTP 403
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Aggregator, not a store. Europeana ingests metadata from accredited national aggregators and domain aggregators; an individual cannot deposit bytes, and the media stays on the provider's…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Aggregator, not a store. Europeana ingests metadata from accredited national aggregators and domain aggregators; an individual cannot deposit bytes, and the media stays on the provider's…
  - probe:https://www.europeana.eu/en/contribute 2026-11-19: the contribute page answered HTTP 403 with a Cloudflare challenge, so its contents could not be re-read | capture: sha256:113e5b632e5d6fe4db9a16f3753506da49028fe863f8ed5d2b9fa76849440a0e | quote: "status": 403
  - probe:https://www.europeana.eu/en/contribute 2026-11-19: the contribute page answered HTTP 403, so its contents could not be re-read | capture: sha256:113e5b632e5d6fe4db9a16f3753506da49028fe863f8ed5d2b9fa76849440a0e | quote: "status": 403
- sources:
  - [1] https://www.europeana.eu/en/contribute

## europeana (incl. europeana 3d)

- `storage/europeana-3` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:36.465Z (inherited) | stale on 2026-12-04
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
- reliability: unverified: https://api.europeana.eu/record/v2/json answered HTTP 404 on 2026-11-19; the aggregator claim could not be re-read from its first-party endpoint; the contribute and pro.europeana.eu pages answered HTTP 403 with a challenge on all tried routes
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: An aggregator, not a host. Content arrives by harvesting institutional metadata; there is no self-serve deposit and no byte storage. /share-your-collections returns nothing usable and…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: An aggregator, not a host. Content arrives by harvesting institutional metadata; there is no self-serve deposit and no byte storage. /share-your-collections returns nothing usable and…
  - [2] 2026-10-21: cited as the basis of the rejection: An aggregator, not a host. Content arrives by harvesting institutional metadata; there is no self-serve deposit and no byte storage. /share-your-collections returns nothing usable and api.eu
  - probe:https://api.europeana.eu/record/v2/json 2026-11-19: the api.europeana.eu record endpoint answered HTTP 404, so its contents could not be re-read | capture: sha256:3b0320cbeb124bb5cd58849fb5eb7ba24095bf56a403ec025f1f48f4f62d4ae2 | quote: "status": 404
  - probe:https://api.europeana.eu/record/v2/json 2026-11-19: the record endpoint answered HTTP 404, so its contents could not be re-read | capture: sha256:3b0320cbeb124bb5cd58849fb5eb7ba24095bf56a403ec025f1f48f4f62d4ae2 | quote: "status": 404
- sources:
  - [1] https://api.europeana.eu/record/v2/json
  - [2] https://pro.europeana.eu/post/contribute-your-collections-on-europe-s-migration-heritage
