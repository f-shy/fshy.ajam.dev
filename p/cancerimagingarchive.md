# TCIA

> cancerimagingarchive.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cancerimagingarchive/ | JSON https://fshy.ajam.dev/api/v1/entity/cancerimagingarchive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TCIA (The Cancer Imaging Archive)

- `storage/tcia` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.cancerimagingarchive.net
- free tier: Free. 'We do not charge a fee for sharing your data through TCIA except in rare circumstances where proposals are extremely large.' | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Per-object-cap: one zip per DICOM series (tens of MB each). The archive is sharded by series, not by dataset. Retention: permanent, DOI per collection. | source: [1] | note: not stated
- egress: Free and anonymous. NBIA REST API serves DICOM series zips with no key; CORS open. | metered: no
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): review, signed non-negotiable Data Submission Agreement, 'a few months' to complete [1]
- limits note: Per-object-cap: one zip per DICOM series (tens of MB each). The archive is sharded by series, not by dataset. Retention: permanent, DOI per collection. Deposit is NOT self-serve: quarterly Advisory Group review, signed non-negotiable Data Submission Agreement, 'a few months' to complete.
- interface detail: rest
- tooling: NBIA Data Retriever + documented REST API (`services.cancerimagingarchive.net/nbia-api/services/v1/`), plus the `tcia-utils` Python package. Deposit side has no API. It is a quarterly-reviewed proposal form.
- composes with: Read side is effectively unlimited and needs no account, so the fetch workload scales independently of any deposit relationship. Deposits: one collection per approval, unlimited collections per institution in principle.
- reliability: Deposit is a months-long institutional process; read path is fast and stable. Not a drop-box by any reading.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'We do not charge a fee', quarterly review, 'a few months', signed agreement required
  - [2] 2026-10-21: probe: GET -> 200, JSON array of collections
  - withheld 2026-10-21: probe: GET .../v1/getImage?SeriesInstanceUID=1.3.6.1.4.1.14519.5.2.1.6279.6001.109002525524522225658609808059 -> 200, 49,111,902 bytes, body starts 504b0304 (real ZIP of DICOM)
- sources:
  - [1] https://www.cancerimagingarchive.net/primary-data/
  - [2] https://services.cancerimagingarchive.net/nbia-api/services/v1/getCollectionValues
