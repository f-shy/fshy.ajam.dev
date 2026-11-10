# MG-RAST

> mg-rast.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mg-rast/ | JSON https://fshy.ajam.dev/api/v1/entity/mg-rast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MG-RAST (metagenomics, Argonne National Laboratory)

- `storage/mg-rast` | qualifies-with-caveat | evidence reported | binding retention-clamped | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.mg-rast.org
- free tier: No published per-account byte or sequence-count quota; described as 'an open source, open submission web application server' and 'one of the biggest repositories for metagenomic data'. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. 'Data publicly available in MG-RAST is available without restrictions', with an API site at api.mg-rast.org for programmatic access. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest
- limits:
  - retention-clamped (binding): delete non-public data sets after 120 days [1]
  - write-gated: application server' and 'one of the biggest repositories for metagenomic data' [1]
- limits note: Retention is the trap: 'We reserve the right to delete non-public data sets after 120 days'. Only PUBLIC deposits persist.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Documented REST API (api.mg-rast.org/api.html) for submission and retrieval; web upload; standard metagenome formats (FASTA/FASTQ) with automatic phylogenetic/functional annotation.
- composes with: Unlimited public datasets per account; no published aggregate cap, so the unit is the dataset.
- reliability: Best-effort service with an explicit no-guarantee clause ('we cannot guarantee correctness of results, integrity of data, or privacy') and a 120-day deletion right on private data; funded by NIH/NSF grants, so continuity tracks grant cycles.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'We reserve the right to delete non-public data sets after 120 days'; 'Data publicly available in MG-RAST is available without restrictions'
  - [2] 2026-10-21: 'open source, open submission web application server'; API at api.mg-rast.org
- sources:
  - [1] https://www.mg-rast.org/legal.html
  - [2] https://www.mg-rast.org/
