# Helix

> helix.imperial.ac.uk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/helix-imperial-ac-uk/ | JSON https://fshy.ajam.dev/api/v1/entity/helix-imperial-ac-uk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Helix (Imperial College London, launched 2025-26)

- `storage/helix` | fails-identity | evidence reported | binding none | category newly launched institutional repository (InvenioRDM, replaced Spiral's data function)
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:14:01.975Z (live) | stale on 2026-12-04
- url https://helix.imperial.ac.uk
- free tier: No published per-record or per-user quota; the live API on 2026-11-19 serves a 13,576,598,383-byte single object (timeavg.zip) and five objects over 6 GB, so per-object caps are at least that single object's size. 45 records total (40 open, 5 embargoed). | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: single object and four objects over 6 GB | bytes: 6000000000 | source: [1] | note: not stated
- retention: Retention minimum 10 years | days: 3650 | source: [1] | note: not stated
- egress: Free, anonymous. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits:
  - retention-clamped: Retention minimum 10 years [1]
  - per-object-cap: single object and four objects over 6 GB [1]
- limits note: No published byte cap. Retention minimum 10 years. Personal/sensitive data refused outright.
- interface detail: InvenioRDM REST, DOI minting, embargoes, restricted records.
- tooling: curl.
- composes with: InvenioRDM shim.
- reliability: Deposit is for 'research staff and students affiliated with' Imperial. Login page offers only email. The SSO is behind it.
- notes: No published per-record or per-user quota; the live API already serves a 13.58 GB single object and four objects over 6 GB, so per-object caps are at least ~14 GB. 40 records total. A very new instance.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published per-record or per-user quota; the live API already serves a 13.58 GB single object and four objects over 6 GB, so per-object caps are at least ~14 GB. 40 records total — a very new instance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 40 records; largest 13,576,598,383 bytes (timeavg.zip), then 6.37 GB and 6.23 GB
  - [2] 2026-10-21: live InvenioRDM response with pids, versions, files
  - [3] 2026-10-21: Helix is for data 'involving research staff and students affiliated with' Imperial
  - [4] 2026-10-21: ... — 'we're pleased to introduce Helix, https://helix.imperial.ac.uk/'
  - [3] 2026-11-19: deposit is restricted to people affiliated with Imperial College London | capture: sha256:b62e06ede29ca2761a5704ad6b477b176e26a512f991b35c4b17c327d54b6183 | quote: Helix is intended for data collected or generated during research involving research staff and students affiliated with Imperial College London. It is free to use and accepts data from across all disciplines.
  - [5] 2026-11-19: the repository states a minimum 10-year retention | capture: sha256:30aea2823324a25e10e62ade5914fc73cca28a5b2c706e44b35a5f9726f7a07c | quote: Data within this Repository will be retained for a minimum of 10 years or otherwise if required by a funder, sponsor, regulatory body, or ethical approval.
  - [1] 2026-11-19: the live InvenioRDM API reports 45 records on 2026-11-19 | capture: sha256:49f0b45b3635cb78fa2200e96c61b6db69b0de882c65621ab4421770ed36c784 | quote: "total": 45
  - [1] 2026-11-19: the live API carries a 13,576,598,383-byte single object on 2026-11-19 | capture: sha256:49f0b45b3635cb78fa2200e96c61b6db69b0de882c65621ab4421770ed36c784 | quote: "size": 13576598383
- sources:
  - [1] https://helix.imperial.ac.uk/api/records?size=50
  - [2] https://helix.imperial.ac.uk/api/records?size=1
  - [3] https://www.imperial.ac.uk/research-and-innovation/support-for-staff/scholarly-communication/research-data-management/archival-and-preservation/finding-a-research-data-repository--archive/
  - [4] https://spiral.imperial.ac.uk/collections/
  - [5] https://www.imperial.ac.uk/research-and-innovation/support-for-staff/scholarly-communication/research-data-management/archival-and-preservation/helix-preservation-policy
