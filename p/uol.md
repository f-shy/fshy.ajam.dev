# DARE

> uol.de | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/uol/ | JSON https://fshy.ajam.dev/api/v1/entity/uol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DARE (Universität Oldenburg) — dare.uol.de

- `storage/dare-dare-uol-de` | qualifies-with-caveat | evidence reported | binding write-gated | category academic repository / Dataverse 6.12.1
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:54:58.643Z (live) | stale on 2026-12-10
- url https://dare.uol.de
- free tier: No quota defined for this collection | unit: none | metered on: unstated | read on: 2026-11-09 | source: [1] | note: The quota endpoint returns "No quota defined for this collection": no numeric quota, unit or metering basis is published.
- per-object cap: source: [1] | note: No per-object size cap is stated on the homepage, the signup form or the root quota endpoint; the quota endpoint reports no quota defined for the root collection.
- retention: source: [1] | note: No retention period is stated on the homepage, the signup form or the root quota endpoint; the homepage says the Dataverse serves teaching and demonstrations purposes only.
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
  - [1] 2026-11-25: the root collection quota endpoint reports no quota defined and publishes no per-object size cap | capture: sha256:efe1d6d0ca8d34e2bbe8dc6e91e89278c883c280bcb82383c6fd389ddd67136b
  - [2] 2026-11-25: the homepage states the teaching and demonstration purpose and no retention period | capture: sha256:2634eed47fb512b2cb3142d49f8dea690f6aea89057ae25319c521c416385e96 | quote: This Dataverse serves teaching and demonstrations purposes only. Please do not upload any real data!
  - [1] 2026-11-25: the quota endpoint reports no defined quota, so no unit is denominated; it does not claim unlimited storage | capture: sha256:efe1d6d0ca8d34e2bbe8dc6e91e89278c883c280bcb82383c6fd389ddd67136b
  - [1] 2026-11-25: the endpoint returns the exact message No quota defined for this collection | capture: sha256:efe1d6d0ca8d34e2bbe8dc6e91e89278c883c280bcb82383c6fd389ddd67136b
  - [1] 2026-11-25: the root collection quota endpoint still reports no quota defined | capture: sha256:efe1d6d0ca8d34e2bbe8dc6e91e89278c883c280bcb82383c6fd389ddd67136b
- sources:
  - [1] https://dare.uol.de/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://dare.uol.de
  - [3] https://dare.uol.de/api/info/version
  - [4] https://dare.uol.de/dataverseuser.xhtml?editMode=CREATE
  - [5] https://dare.uol.de/api/search?q=*&type=dataset&per_page=1
