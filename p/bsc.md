# BSC Dataverse

> bsc.es | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bsc/ | JSON https://fshy.ajam.dev/api/v1/entity/bsc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BSC Dataverse (Barcelona Supercomputing Center)

- `storage/bsc-dataverse` | qualifies-with-caveat | evidence reported | binding per-object-cap | category academic repository / Dataverse 6.10.1
- needs card no, phone no, ID no, institution no | verified 2026-11-19T21:12:58.116Z (live) | stale on 2026-12-04
- url https://dataverse.bsc.es
- free tier: No quota defined for this collection | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 2.5 GB per file | source: [2]
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted. | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - per-object-cap (binding): 2.5 GB per file [2]
  - per-object-cap (binding): 1000 files per upload [2]
- limits note: the same as the free tier
- binding note: Maximum file size: 2.5 GB per file.
- interface detail: REST (native Dataverse API v1)
- tooling: curl / DVUploader
- composes with: Open local signup at a supercomputing centre — the operator demographic most likely to have real disk behind the instance.
- reliability: Also offers ORCID login; no published storage policy page found.
- notes: The quota endpoint states "No quota defined for this collection".
- evidence:
  - [3] 2026-10-21: https://dataverse.bsc.es/api/info/version — 6.10.1
  - [1] 2026-10-21: 'No quota defined for this collection'
  - [4] 2026-10-21: HTTP 200; loginpage also advertises ORCID
  - [1] 2026-11-09: the quota endpoint states no quota is defined, so no total quota is published | capture: sha256:22affb5fc8da9e9012666b9b18d2d9d0137210c9fed16c06e8fb34e0e1e07c7c
  - [2] 2026-11-09: the user guide still states a maximum file size of 2.5 GB per file | capture: sha256:3fdf8fa2b6d9ae893ad5f60d441c359f3c26cd52f1fe558a8860f4e7b7340d36 | quote: Maximum file size: 2.5 GB per file.
  - [2] 2026-11-09: the BSC user guide states a maximum of 1000 files per upload | capture: sha256:3fdf8fa2b6d9ae893ad5f60d441c359f3c26cd52f1fe558a8860f4e7b7340d36 | quote: Maximum number of files per upload: 1000 files.
  - [1] 2026-11-09: the repository's quota endpoint states that no quota is defined for the collection | capture: sha256:4b1b0cd4de8b7a8e5b25cf3b91bad279cc8d6022cea673ad64ceda6db2a37289
  - [2] 2026-11-19: the per-file limit remains 2.5 GB | capture: sha256:3fdf8fa2b6d9ae893ad5f60d441c359f3c26cd52f1fe558a8860f4e7b7340d36 | quote: Maximum file size: 2.5 GB per file.
- sources:
  - [1] https://dataverse.bsc.es/api/dataverses/:root/storage/quota?showInherited=true
  - [2] https://guides.bsc.es/dataverse/user-guide/data-preparation/file-number-size
  - [3] https://dataverse.bsc.es/api/info/version
  - [4] https://dataverse.bsc.es/dataverseuser.xhtml?editMode=CREATE
