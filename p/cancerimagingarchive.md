# TCIA

> cancerimagingarchive.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cancerimagingarchive/ | JSON https://fshy.ajam.dev/api/v1/entity/cancerimagingarchive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TCIA (The Cancer Imaging Archive)

- `storage/tcia` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:23.965Z (live) | stale on 2026-12-10
- url https://www.cancerimagingarchive.net
- free tier: We do not charge a fee for sharing your data through TCIA except in rare circumstances where proposals are extremely large. | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: | getImage | Set of images in a zip file | ZIP | SeriesInstanceUID (R) | NA | NA | NA | | | source: [1] | note: | getImage | Set of images in a zip file | ZIP | SeriesInstanceUID (R) | NA | NA | NA | |
- retention: Every TCIA dataset is published with a Data Citation which includes a persistent Digital Object Identifier (DOI) that must be cited or attributed any time the data are used as shown below. | source: [1] | note: Every TCIA dataset is published with a Data Citation which includes a persistent Digital Object Identifier (DOI) that must be cited or attributed any time the data are used as shown below.
- egress: Free and anonymous. NBIA REST API serves DICOM series zips with no key; CORS open. | metered: no
- identity: institution
- interface: rest
- limits:
  - write-gated (binding): Applications are reviewed quarterly by the TCIA Advisory Group to assess their utility to the TCIA user community. [1]
- limits note: Per-object-cap: one zip per DICOM series (tens of MB each). The archive is sharded by series, not by dataset. Retention: permanent, DOI per collection. Deposit is NOT self-serve: quarterly Advisory Group review, signed non-negotiable Data Submission Agreement, 'a few months' to complete.
- interface detail: rest
- tooling: NBIA Data Retriever + documented REST API (`services.cancerimagingarchive.net/nbia-api/services/v1/`), plus the `tcia-utils` Python package. Deposit side has no API. It is a quarterly-reviewed proposal form.
- composes with: Read side is effectively unlimited and needs no account, so the fetch workload scales independently of any deposit relationship. Deposits: one collection per approval, unlimited collections per institution in principle.
- reliability: Deposit is a months-long institutional process; read path is fast and stable. Not a drop-box by any reading.
- notes: Free. 'We do not charge a fee for sharing your data through TCIA except in rare circumstances where proposals are extremely large.'
- evidence:
  - [1] 2026-10-21: 'We do not charge a fee', quarterly review, 'a few months', signed agreement required
  - [2] 2026-10-21: probe: GET -> 200, JSON array of collections
  - withheld 2026-10-21: probe: GET .../v1/getImage?SeriesInstanceUID=1.3.6.1.4.1.14519.5.2.1.6279.6001.109002525524522225658609808059 -> 200, 49,111,902 bytes, body starts 504b0304 (real ZIP of DICOM)
  - [1] 2026-11-09: the primary-data page states the no-fee position for sharing data through TCIA | capture: sha256:4e0210320b8894682a945d7f06aa0315d4e31ceb6ef44c13aa96808dd1fc1096 | quote: We do not charge a fee for sharing your data through TCIA except in rare circumstances where proposals are extremely large.
  - [1] 2026-11-09: the primary-data page states applications are reviewed quarterly by the TCIA Advisory Group | capture: sha256:4e0210320b8894682a945d7f06aa0315d4e31ceb6ef44c13aa96808dd1fc1096 | quote: Applications are reviewed quarterly by the TCIA Advisory Group to assess their utility to the TCIA user community.
  - [3] 2026-11-25: getImage returns a ZIP keyed by SeriesInstanceUID | capture: sha256:1c109ca02551552e83b0626f600c18e8d34eb569443b1e4d13c137d2ac20579d | quote: | getImage | Set of images in a zip file | ZIP | SeriesInstanceUID (R) | NA | NA | NA | |
  - [4] 2026-11-25: the usage page states a persistent DOI for every dataset | capture: sha256:8dc182c5d0a2be953fea880bf87cb68ca907ba38689d4edace54e611b431ea83 | quote: Every TCIA dataset is published with a Data Citation which includes a persistent Digital Object Identifier (DOI) that must be cited or attributed any time the data are used as shown below.
  - [1] 2026-11-25: the primary-data page states quarterly advisory review | capture: sha256:4317031f4b8caaa4ffa05403fd636c03b8bb3cdc4c4ea6835adeb0977f05ad1a | quote: Applications are reviewed quarterly by the TCIA Advisory Group to assess their utility to the TCIA user community.
  - [1] 2026-11-25: the primary-data page states the no-fee position | capture: sha256:4317031f4b8caaa4ffa05403fd636c03b8bb3cdc4c4ea6835adeb0977f05ad1a | quote: We do not charge a fee for sharing your data through TCIA except in rare circumstances where proposals are extremely large.
- sources:
  - [1] https://www.cancerimagingarchive.net/primary-data/
  - [2] https://services.cancerimagingarchive.net/nbia-api/services/v1/getCollectionValues
  - [3] https://wiki.cancerimagingarchive.net/display/Public/TCIA+Programmatic+Interface+(REST+API)+Usage+Guide+v1
  - [4] https://www.cancerimagingarchive.net/data-usage-policies-and-restrictions/
