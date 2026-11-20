# dataverse

> dataverse.org | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## dataverse installations on 5.5–6.0 (cuhk, icrisat, cidacs, jpl, fz jülich,

- `storage/dataverse-installations-on-5-5-6-0-cuhk-icrisat-cidacs-j` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.061Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/dataverse.md
- free tier: None reachable: 19 of 149 installs predate the collection-quota feature (Dataverse 6.1+) and return 404 on the quota endpoint. They cannot be scored on this axis at all. The absence of the endpoint is not. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party Dataverse pages leave the per-installation maximum upload size to a setting (:MaxFileUploadSizeInBytes) and state no single numeric cap | note: not applicable
- retention: stated-absent: the Dataverse collection-quota page states no retention period for stored files
- egress: stated-absent: the Dataverse guide pages describe upload and download APIs but state no egress price or transfer terms | metered: no
- identity: email
- interface: rest, s3
- interface detail: Dataverse exposes a REST-based native API and, on installations with direct upload enabled, pre-signed S3 URLs for file transfer.
- tooling: not documented
- composes with: Dataverse chains through DvUploader and through web applications such as OJS, OSF and RSpace that use the file upload API.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: 19 of 149 installs predate the collection-quota feature (Dataverse 6.1+) and return 404 on the quota endpoint. They cannot be scored on this axis at all — the absence of the endpoint is not
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: 19 of 149 installs predate the collection-quota feature (Dataverse 6.1+) and return 404 on the quota endpoint. They cannot be scored on this axis at all — the absence of the endpoint is not
  - [1] 2026-11-19: the collection-quota feature the record depends on was introduced only in Dataverse 6.1, so pre-6.1 installs cannot expose it | capture: sha256:8388e89e6de65072a1f41039ddcf9fcf12a7dcbb757d3c635e779a083a4dd9dc | quote: Please note that this is a new and still experimental feature (as of Dataverse v6.1 release).
  - [2] 2026-11-19: Dataverse exposes an S3 direct-upload path alongside its REST-based native API | capture: sha256:e90c303165b7f43f750a8f34e9c373e72c31f1794c073985ab5b365cbfc970ba | quote: To initiate a transfer of a file to S3, make a call to the Dataverse installation indicating the size of the file to upload.
  - [3] 2026-11-19: the Dataverse native API is REST-based | capture: sha256:ad5423b4b982223d0152bc7e275721ff1cb0e648637376cb5070bce8423aec14 | quote: The Dataverse Software exposes most of its GUI functionality via a REST-based API.
  - [4] 2026-11-19: the page documents collection storage quotas introduced in v6.1 and states no retention term | capture: sha256:b4889df14b989834eed350206b2f05d6b9667f72755ebcacd01915a1b6860a06 | quote: Please note that this is a new and still experimental feature (as of Dataverse v6.1 release).
  - [2] 2026-11-19: the upload cap is installation-configured through MaxFileUploadSizeInBytes, not stated as a fixed number | capture: sha256:e90c303165b7f43f750a8f34e9c373e72c31f1794c073985ab5b365cbfc970ba | quote: The call will return a 400 (BAD REQUEST) response if the file is larger than what is allowed by the
  - [5] 2026-11-19: the API guide describes integration paths but states no egress terms | capture: sha256:9452a7f1fff755c391d106a3624d5e19a52413748663d0ca9ade668255605086 | quote: APIs open the door for integrations between the Dataverse Software and other software.
  - [5] 2026-11-19: the file upload API lets external web applications deposit files into a Dataverse installation | capture: sha256:9452a7f1fff755c391d106a3624d5e19a52413748663d0ca9ade668255605086 | quote: OJS, OSF, and RSpace are all web applications that can integrate with a Dataverse installation
  - [5] 2026-11-19: the first-party API guide documents a file upload API for integrations | capture: sha256:9452a7f1fff755c391d106a3624d5e19a52413748663d0ca9ade668255605086 | quote: API stands for “Application Programming Interface” and an example is the Dataverse Software’s “file upload” API.
- sources:
  - [1] https://guides.dataverse.org/en/6.1/admin/collectionquotas.html
  - [2] https://guides.dataverse.org/en/6.11/developers/s3-direct-upload-api.html
  - [3] https://guides.dataverse.org/en/latest/api/native-api.html
  - [4] https://guides.dataverse.org/en/latest/admin/collectionquotas.html
  - [5] https://guides.dataverse.org/en/latest/api/intro.html

## dataverse upload api (post /api/users, post /api/datasets, post /api/builti

- `storage/dataverse-upload-api-post-api-users-post-api-datasets-po` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.061Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/dataverse.md
- free tier: none reachable: Not usable as a write path in this research frame. POST /api/users is 404 on 6.10+ (endpoint removed); POST /api/builtin-users requires :BuiltinUsersKey (403/404 without it). Writes… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the Dataverse native API guide states no fixed per-object size cap | note: not applicable
- retention: stated-absent: the Dataverse native API guide states no retention period for stored files
- egress: stated-absent: the Dataverse API guides describe upload and download endpoints but state no egress price or transfer terms | metered: no
- identity: email
- interface: rest
- interface detail: The Dataverse native API is REST-based; the builtin-user creation endpoint requires a server-side BuiltinUsersKey known only to the installation team.
- tooling: not documented
- composes with: Dataverse's file upload API chains with DvUploader and with web applications such as OJS, OSF and RSpace.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Not usable as a write path in this research frame. POST /api/users is 404 on 6.10+ (endpoint removed); POST /api/builtin-users requires :BuiltinUsersKey (403/404 without it). Writes…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Not usable as a write path in this research frame. POST /api/users is 404 on 6.10+ (endpoint removed); POST /api/builtin-users requires:BuiltinUsersKey (403/404 without it). Writes therefor
  - probe:https://dataverse.harvard.edu/api/users 2026-11-19: POST's /api/users endpoint is removed and returns 404 on a current Dataverse install | capture: sha256:a61b4b2353b3c5f66ca467d812f91f358fb7e68e57abab3392054af4bd3482e4 | quote: "status": 404
  - probe:https://dataverse.harvard.edu/api/builtin-users 2026-11-19: the builtin-users route is gated and returns 403 without the builtin-users key | capture: sha256:7e40676cb3e554abb2aeb3be381b034a231e40a73e532b1fd5d41169a80f5a46 | quote: "status": 403
  - [1] 2026-11-19: the Dataverse native API, including the user and builtin-user endpoints, is REST-based | capture: sha256:ad5423b4b982223d0152bc7e275721ff1cb0e648637376cb5070bce8423aec14 | quote: The Dataverse Software exposes most of its GUI functionality via a REST-based API.
  - [1] 2026-11-19: the builtin-user creation API needs a secret server-side key, so it is not an anonymous signup path | capture: sha256:ad5423b4b982223d0152bc7e275721ff1cb0e648637376cb5070bce8423aec14 | quote: For security reasons, builtin users cannot be created via API unless the team who runs the Dataverse installation has populated a database setting called `:BuiltinUsersKey`
  - [2] 2026-11-19: the per-file cap is a per-installation setting, not a fixed documented number | capture: sha256:e90c303165b7f43f750a8f34e9c373e72c31f1794c073985ab5b365cbfc970ba | quote: The call will return a 400 (BAD REQUEST) response if the file is larger than what is allowed by the
  - [3] 2026-11-19: the file upload API lets external applications deposit files into Dataverse | capture: sha256:9452a7f1fff755c391d106a3624d5e19a52413748663d0ca9ade668255605086 | quote: OJS, OSF, and RSpace are all web applications that can integrate with a Dataverse installation
  - [3] 2026-11-19: the API guide describes integration paths but states no egress terms | capture: sha256:9452a7f1fff755c391d106a3624d5e19a52413748663d0ca9ade668255605086 | quote: APIs open the door for integrations between the Dataverse Software and other software.
- sources:
  - [1] https://guides.dataverse.org/en/latest/api/native-api.html
  - [2] https://guides.dataverse.org/en/6.11/developers/s3-direct-upload-api.html
  - [3] https://guides.dataverse.org/en/latest/api/intro.html

## dataverse's own installations json (services.dataverse.harvard.edu/minivers

- `storage/dataverse-s-own-installations-json-services-dataverse-ha` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.061Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/dataverse.md
- free tier: None reachable: DNS dead. Cloudflare error 1016. Origin hostname does not resolve. The working substitute is the GitHub data file that powers the same map. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party Dataverse site states no per-object size cap for the installations-list endpoint | note: not applicable
- retention: stated-absent: the first-party Dataverse site states no retention period for stored bytes
- egress: stated-absent: the first-party Dataverse site states no egress terms for the installations-list endpoint | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the first-party Dataverse site describes a hosted repository and self-installed software; it states no byte-storage interface for the installations-list endpoint
- tooling: not documented
- composes with: stated-absent: the first-party Dataverse site states no way to chain the installations-list endpoint as byte storage into other services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: DNS dead. Cloudflare error 1016 — origin hostname does not resolve. The working substitute is the GitHub data file that powers the same map.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: DNS dead. Cloudflare error 1016 — origin hostname does not resolve. The working substitute is the GitHub data file that powers the same map.
  - probe:https://services.dataverse.harvard.edu/miniverse 2026-11-19: the origin hostname does not resolve, so the installations-JSON endpoint is unreachable today | capture: sha256:d01394102a53fc724f796d2f52302de447434f03a620c19b0c19911bfa811ef9 | quote: "status": null
  - [1] 2026-11-19: the first-party Dataverse site describes a hosted repository option and self-installed software but no installations-list JSON storage interface | capture: sha256:f9065a74ac71074bb4416c3d6b5d9d3e516ec64b204e460b310b448a05352af9 | quote: Does your institution need a place to host research data but doesn't need to install the Dataverse Project software?
- sources:
  - [1] https://dataverse.org/institutions
