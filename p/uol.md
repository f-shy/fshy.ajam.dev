# DARE

> uol.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uol/ | JSON https://fshy.ajam.dev/api/v1/entity/uol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DARE (Universität Oldenburg) — dare.uol.de

- `storage/dare-dare-uol-de` | qualifies-with-caveat | evidence reported | binding write-gated | category academic repository / Dataverse 6.12.1
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:13:26.680Z (live) | stale on 2026-12-04
- url https://dare.uol.de
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-11-09 | source: [1] | note: No quota defined for this collection
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted, 1.69 s to version API. | metered: no
- identity: email | detail: Contact the repository support address by email.
- interface: rest
- limits:
  - write-gated (binding): uploads are not possible with a default account [2]
- limits note: No published per-file cap; no quota number returned by the API.
- binding note: uploads are not possible with a default account
- interface detail: REST (native Dataverse API v1), SWORD
- tooling: curl / DVUploader
- composes with: Useful precisely because it is small (78 datasets, 45 collections): an installation this lightly used has had no reason to set a quota, and every one of its collections returns the same 'No quota defined'.
- reliability: Very low dataset count. An untested production instance; do not assume operational maturity.
- notes: the same as the free tier
- evidence:
  - [3] 2026-10-21: https://dare.uol.de/api/info/version — 6.12.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [4] 2026-10-21: HTTP 200 (native signup form present)
  - [5] 2026-10-21: 78 datasets; type=dataverse — 45
  - [1] 2026-11-09: the root collection's quota endpoint states that no quota is defined for this collection | capture: sha256:5aaf35e6516e74f75fa6d6248f93a923136e6259992b9ab51eb9d5e8e1b0325c | quote: No quota defined for this collection
  - [2] 2026-11-09: the homepage still states that it is not possible to upload data with a default account | capture: sha256:9bfce4a809f82ebf7bb28639a1beea1d1157d30db9e76f0d3438e904dcbe4d82 | quote: Please be advised that it is not possible to upload data with your default account.
  - [2] 2026-11-09: the homepage still directs users to contact the repository by email to learn how to use DARE | capture: sha256:9bfce4a809f82ebf7bb28639a1beea1d1157d30db9e76f0d3438e904dcbe4d82 | quote: Please feel free to contact us via email to [address removed] to learn more about how to use DARE.
  - [4] 2026-11-09:  | capture: sha256:0954b986135376884880940c49a310692979d27747830a8f78db67fb84527d6b
  - [1] 2026-11-19: the root collection's quota endpoint still reports no quota defined | capture: sha256:c41dc19f7de2f5e1298cf7d53096769dc5200dea0d5b703ee252289fe89c03d7 | quote: No quota defined for this collection
  - [2] 2026-11-19: the homepage still states that uploads are not possible with a default account | capture: sha256:6ee781d9bb9b68b365e049e586fdc6eb6a56af84adfb9c0fe7eec6680f1c580c | quote: it is not possible to upload data with your default account
- sources:
  - [1] https://dare.uol.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dare.uol.de
  - [3] https://dare.uol.de/api/info/version
  - [4] https://dare.uol.de/dataverseuser.xhtml?editMode=CREATE
  - [5] https://dare.uol.de/api/search?q=*&type=dataset&per_page=1
