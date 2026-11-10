# DataverseNL

> dataverse.nl | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse-3/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataverseNL

- `storage/dataversenl` | fails-identity | evidence reported | binding none | category national Dataverse consortium (DANS)
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dataverse.nl
- free tier: No quota defined (API); effectiveDatasetFileCountLimit=10000. The highest file-count ceiling seen in the sweep. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free | metered: no
- identity: institution | detail: Institution. 'The institutions using DataverseNL are responsible for assigning permissions to user accounts'; users 'log in with their institutional account'. Prospective depositors without a partner institution are told to 'contact your institution' or find another repository.
- interface: rest
- limits note: no storage quota, 10,000 files/dataset, no files required to publish
- interface detail: REST (works even though the HTML front end is behind Anubis proof-of-work)
- tooling: REST; note the HTML UI returns an Anubis 'Making sure you're not a bot' PoW page to non-browser clients
- composes with: None. Account provisioning is manual per institution.
- reliability: API fully usable anonymously for read; the wall is account provisioning, not transport.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no quota defined (API); effectiveDatasetFileCountLimit=10000 — the highest file-count ceiling seen in the sweep
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: {"message":"No quota defined for this collection"}
  - [2] 2026-10-21: 'effectiveDatasetFileCountLimit':10000
  - [2] 2026-10-21: (description) — 'contact your institution directly ... If your institution is not in this list, and you are looking for a repository to publish research data, please contact [DANS]'
  - [3] 2026-10-21: (search snippet) — 'The institutions using DataverseNL are responsible for assigning permissions to user accounts'
  - [4] 2026-10-21: Anubis proof-of-work interstitial to non-browser clients
- sources:
  - [1] https://dataverse.nl/api/dataverses/1/storage/quota?showInherited=true
  - [2] https://dataverse.nl/api/dataverses/1
  - [3] https://dans.knaw.nl/en/data-services/dataversenl/user-guide/
  - [4] https://dataverse.nl/
