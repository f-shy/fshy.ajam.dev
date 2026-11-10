# DARE

> uol.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uol/ | JSON https://fshy.ajam.dev/api/v1/entity/uol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DARE (Universität Oldenburg) — dare.uol.de

- `storage/dare-dare-uol-de` | qualifies | evidence reported | binding none | category academic repository / Dataverse 6.12.1
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dare.uol.de
- free tier: No quota defined at root. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted, 1.69 s to version API. | metered: no
- identity: email | detail: email
- interface: rest
- limits note: No published per-file cap; no quota number returned by the API.
- interface detail: REST (native Dataverse API v1), SWORD
- tooling: curl / DVUploader
- composes with: Useful precisely because it is small (78 datasets, 45 collections): an installation this lightly used has had no reason to set a quota, and every one of its collections returns the same 'No quota defined'.
- reliability: Very low dataset count. An untested production instance; do not assume operational maturity.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: https://dare.uol.de/api/info/version — 6.12.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [3] 2026-10-21: HTTP 200 (native signup form present)
  - [4] 2026-10-21: 78 datasets; type=dataverse — 45
- sources:
  - [1] https://dare.uol.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dare.uol.de/api/info/version
  - [3] https://dare.uol.de/dataverseuser.xhtml?editMode=CREATE
  - [4] https://dare.uol.de/api/search?q=*&type=dataset&per_page=1
