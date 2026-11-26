# MG-RAST

> mg-rast.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mg-rast/ | JSON https://fshy.ajam.dev/api/v1/entity/mg-rast.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MG-RAST (metagenomics, Argonne National Laboratory)

- `storage/mg-rast` | qualifies-with-caveat | evidence reported | binding retention-clamped | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:26.264Z (live) | stale on 2026-12-10
- url https://www.mg-rast.org
- free tier: No published per-account byte or sequence-count quota; described as 'an open source, open submission web application server' and 'one of the biggest repositories for metagenomic data'. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: max. size per file: 10GB | source: [1] | note: max. size per file: 10GB; larger files were not tested
- retention: We reserve the right to delete non-public data sets after 120 days. | source: [1]
- egress: Data publicly available in MG-RAST is available without restrictions | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest, cli, browser
- limits:
  - retention-clamped (binding): delete non-public data sets after 120 days [1]
  - write-gated: application server' and 'one of the biggest repositories for metagenomic data' [1]
- limits note: Retention is the trap: 'We reserve the right to delete non-public data sets after 120 days'. Only PUBLIC deposits persist.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Documented REST API (api.mg-rast.org/api.html) for submission and retrieval; web upload; standard metagenome formats (FASTA/FASTQ) with automatic phylogenetic/functional annotation.
- composes with: max. project size: 200 metagenomes
- reliability: Best-effort service with an explicit no-guarantee clause ('we cannot guarantee correctness of results, integrity of data, or privacy') and a 120-day deletion right on private data; funded by NIH/NSF grants, so continuity tracks grant cycles.
- evidence:
  - [1] 2026-10-21: 'We reserve the right to delete non-public data sets after 120 days'; 'Data publicly available in MG-RAST is available without restrictions'
  - [2] 2026-10-21: 'open source, open submission web application server'; API at api.mg-rast.org
  - [1] 2026-11-09:  | capture: sha256:fff22b242347a7a40270699a647e04ea1ddccc0b789ebcba20af49c0d850e3f4 | quote: Data publicly available in MG-RAST is available without restrictions
  - [1] 2026-11-09:  | capture: sha256:fff22b242347a7a40270699a647e04ea1ddccc0b789ebcba20af49c0d850e3f4 | quote: We reserve the right to delete non-public data sets after 120 days.
  - [1] 2026-11-19: public data is available without restrictions | capture: sha256:fff22b242347a7a40270699a647e04ea1ddccc0b789ebcba20af49c0d850e3f4 | quote: Data publicly available in MG-RAST is available without restrictions
  - [1] 2026-11-19:  | capture: sha256:fff22b242347a7a40270699a647e04ea1ddccc0b789ebcba20af49c0d850e3f4 | quote: We reserve the right to delete non-public data sets after 120 days.
  - [3] 2026-11-25: the submission SOP states a tested per-file size of 10GB | capture: sha256:76f9435df4d66106ce41d39249da71d0125857fffdc4536cd3531157fd4864ac | quote: - max. size per file: 10GB
  - [3] 2026-11-25: the SOP gives a tested file size and says larger files were not tested | capture: sha256:76f9435df4d66106ce41d39249da71d0125857fffdc4536cd3531157fd4864ac | quote: - max. size per file: 10GB...While there is no reason to assume the software will not work with larger numbers of files or larger files, we did not test for that.
  - [3] 2026-11-25: the submission SOP states a tested project size of 200 metagenomes | capture: sha256:76f9435df4d66106ce41d39249da71d0125857fffdc4536cd3531157fd4864ac | quote: - max. project size: 200 metagenomes
  - [3] 2026-11-25: MG-RAST names web, command line and RESTful API interfaces | capture: sha256:76f9435df4d66106ce41d39249da71d0125857fffdc4536cd3531157fd4864ac | quote: There are three interfaces for uploading and publishing data, the Web interface, intended for most users, command line scripts, intended for programmers, and the native RESTful API, recommended for experienced programmers.
  - [1] 2026-11-25:  | capture: sha256:fff22b242347a7a40270699a647e04ea1ddccc0b789ebcba20af49c0d850e3f4 | quote: We reserve the right to delete non-public data sets after 120 days.
- sources:
  - [1] https://www.mg-rast.org/legal.html
  - [2] https://www.mg-rast.org/
  - [3] https://help.mg-rast.org/api.html
