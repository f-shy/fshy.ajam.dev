# Knowledge Network

> ecoinformatics.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ecoinformatics/ | JSON https://fshy.ajam.dev/api/v1/entity/ecoinformatics.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## knb (knowledge network for biocomplexity)

- `storage/knb` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://knb.ecoinformatics.org/
- free tier: none reachable: Free tier provides 5 GB storage per registered user. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: 5 GB free per user.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 5 GB free per user.
  - [2] 2026-10-21: cited as the basis of the rejection: 5 GB free per user.
- sources:
  - [1] https://knb.ecoinformatics.org/
  - [2] https://knb.ecoinformatics.org/knb/d1/mn/v2/node

## Knowledge Network for Biocomplexity (KNB, NCEAS / UC Santa Barbara)

- `storage/knowledge-network-for-biocomplexity` | fails-quota | evidence reported | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://knb.ecoinformatics.org
- free tier: 5 GB free per user ('Store up to 5GB of data for free'), with DOIs for permanent publication. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 5 GB free per user ('Store up to 5GB of data for free'), with DOIs for permanent publication | source: [1] | note: not stated
- egress: Free public downloads with no metering; metadata is harvestable. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest
- limits:
  - per-object-cap (binding): 5 GB account cap [1]
- limits note: Per-account 5 GB aggregate is the binding constraint; ecological/environmental scope; EML metadata required.
- interface detail: rest
- tooling: Web upload plus desktop metadata editors (Morpho), EML metadata standard, DOI minting; a Metacat REST API exists for reads.
- composes with: 5 GB x accounts; no published per-dataset unlimited tier, so it does not chain to 500 GB without account multiplication.
- reliability: Long-lived (NCEAS, since 2003) and stable, but the 5 GB account cap makes it a metadata/DOI service rather than a bulk store.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB free per user ('Store up to 5GB of data for free'), with DOIs for permanent publication.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Store up to 5GB of data for free. The KNB also supports DOIs to permanently publish your data sets.'
  - [2] 2026-10-21: live submit path
- sources:
  - [1] https://knb.ecoinformatics.org
  - [2] https://knb.ecoinformatics.org/submit
