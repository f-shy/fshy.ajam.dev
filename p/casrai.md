# datacite commons

> casrai.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/casrai/ | JSON https://fshy.ajam.dev/api/v1/entity/casrai.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## datacite commons, openalex, base, semantic scholar s2orc

- `storage/datacite-commons-openalex-base-semantic-scholar-s2orc` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.921Z (live) | stale on 2026-12-04
- url https://casrai.org/guides/datacite-commons-searching-pid-graph
- free tier: none reachable: All four are discovery/index layers with zero writable storage. DataCite Commons is the PID graph over DOIs; OpenAlex and BASE are harvesters; S2ORC bulk access is per-release S3 partitions | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: All four are discovery/index layers with zero writable storage. DataCite Commons is the PID graph over DOIs; OpenAlex and BASE are harvesters; S2ORC bulk access is per-release S3 partitions
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: All four are discovery/index layers with zero writable storage. DataCite Commons is the PID graph over DOIs; OpenAlex and BASE are harvesters; S2ORC bulk access is per-release S3 partitions
  - [2] 2026-10-21: cited as the basis of the rejection: All four are discovery/index layers with zero writable storage. DataCite Commons is the PID graph over DOIs; OpenAlex and BASE are harvesters; S2ORC bulk access is per-release S3 partitions
  - [1] 2026-11-19: the guide says Commons is a search and discovery layer, not a writable store | capture: sha256:f7e302913112e75d099ddd8bec75fd62fda6e6334cbfd505e38a3ffb8bb170ae | quote: Commons is the public-facing search tool built to browse the resulting graph of relationships, not to mint or edit identifiers. No account is required to search it.
  - [2] 2026-11-19: the first-party API docs offer bulk download of releases, not user uploads | capture: sha256:bda536398be2b089f14d039588f344c702e780aee0c8d91cdf66194f82db5b5a | quote: Download full-corpus datasets from the Semantic Scholar Academic Graph (S2AG)
- sources:
  - [1] https://casrai.org/guides/datacite-commons-searching-pid-graph
  - [2] https://api.semanticscholar.org/api-docs/datasets
