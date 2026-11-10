# Helix

> helix.imperial.ac.uk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/helix-imperial-ac-uk/ | JSON https://fshy.ajam.dev/api/v1/entity/helix-imperial-ac-uk.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Helix (Imperial College London, launched 2025-26)

- `storage/helix` | fails-identity | evidence reported | binding none | category newly launched institutional repository (InvenioRDM, replaced Spiral's data function)
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://helix.imperial.ac.uk
- free tier: No published per-record or per-user quota; the live API already serves a 13.58 GB single object and four objects over 6 GB, so per-object caps are at least ~14 GB. 40 records total. A very new instance. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
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
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published per-record or per-user quota; the live API already serves a 13.58 GB single object and four objects over 6 GB, so per-object caps are at least ~14 GB. 40 records total — a very new instance.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 40 records; largest 13,576,598,383 bytes (timeavg.zip), then 6.37 GB and 6.23 GB
  - [2] 2026-10-21: live InvenioRDM response with pids, versions, files
  - [3] 2026-10-21: Helix is for data 'involving research staff and students affiliated with' Imperial
  - [4] 2026-10-21: ... — 'we're pleased to introduce Helix, https://helix.imperial.ac.uk/'
- sources:
  - [1] https://helix.imperial.ac.uk/api/records?size=50
  - [2] https://helix.imperial.ac.uk/api/records?size=1
  - [3] https://www.imperial.ac.uk/research-and-innovation/support-for-staff/scholarly-communication/research-data-management/archival-and-preservation/finding-a-research-data-repository--archive/
  - [4] https://spiral.imperial.ac.uk/collections/
