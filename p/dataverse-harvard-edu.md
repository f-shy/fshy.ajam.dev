# Harvard Dataverse

> dataverse.harvard.edu | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse-harvard-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse-harvard-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Harvard Dataverse Repository - per-collection quota

- `storage/harvard-dataverse-repository-per-collection-quota` | qualifies | evidence reported | binding per-object-cap | category academic
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dataverse.harvard.edu/
- free tier: 1 TB per Dataverse Collection allocation (2.5 TB for Harvard affiliates). Per-file 2.5 GB through UI/API; larger via the S3 direct-upload path. The 1 TB is enforced as a collection allocation, not a per-person cap: GET /api/dataverses/<alias>/storage/quota?showInherited=true returns {"Total quota allocation for this collection": 1099511627776} for ordinary collections, and one live collection returns 2748779069440 (2.5 TB). | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file 2.5 GB | bytes: 2500000000 | source: [1] | note: not stated
- retention: | write-once: publishing is irreversible, no delete without support intervention, no embargo; 'Submit for Review' spam screen before publication; per-file 2.5 GB in the browser path; 1,000 files/dataset is the observed effectiveDatasetFileCountLimit; S3 direct upload is admin-enabled per install and is the only route past the 2.5 GB file cap. | source: [1] | note: not stated
- egress: Free anonymous access without login. Endpoint GET /api/access/datafile/<id> returns HTTP 303 to a signed S3 URL with 1-hour expiration, supporting Range requests. | metered: no
- identity: email | detail: email
- interface: s3, rest, rclone, cli
- limits:
  - write-gated: Review' spam screen before publication [1]
  - per-object-cap (binding): Per-file 2.5 GB [1]
- limits note: write-once: publishing is irreversible, no delete without support intervention, no embargo; 'Submit for Review' spam screen before publication; per-file 2.5 GB in the browser path; 1,000 files/dataset is the observed effectiveDatasetFileCountLimit; S3 direct upload is admin-enabled per install and is the only route past the 2.5 GB file cap.
- interface detail: rest
- tooling: REST native API (create dataset, add files, direct S3 upload), plus the official Python/CLI clients. dataset count 306,027 live. rclone has no native backend but the S3 direct-upload path accepts any S3 client.
- composes with: Storage quota attaches to collections, which logged-in users can create as of June 2024. Each collection receives a 1 TiB allocation, and collections can be nested into hierarchical trees for sharding.
- reliability: Anonymous downloads return signed S3 URLs with 1-hour expiration, requiring URL resolution per request. Quota API endpoints rate-limit rapid successive requests with HTTP 403.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'All researchers from any discipline, both inside and out of the Harvard University community, can deposit files of up to 2.5GB, and store up to 1TB of data on the Harvard Dataverse Repository.'
  - [2] 2026-10-21: hosting restriction stated as '1TB per dataset (2.5GB per file) Any file types'
  - [3] 2026-10-21: probe returned 1099511627776 bytes
  - [4] 2026-10-21: probe returned 2748779069440 bytes (2.5 TB), proving allocations are set per collection and can exceed 1 TB
  - [5] 2026-10-21: 303 then 200, Content-Length 16393, file written and SHA-256 fed450c5dfa423d6a51168611bbb9f4179e862a9c831ee41c37b23b128cc24fa (16,393 bytes, exact)
  - [5] 2026-10-21: with Range: bytes=0-1048575 - HTTP 206, Content-Range: bytes 0-16392/16393
  - [6] 2026-10-21: and #207 - collection creation was disabled for :authenticated-users in Nov 2022, reopened June 2024
- sources:
  - [1] https://support.dataverse.harvard.edu/researchers
  - [2] https://neurips.cc/Conferences/2025/DataHostingGuidelines
  - [3] https://dataverse.harvard.edu/api/dataverses/SEE_Precursors/storage/quota?showInherited=true
  - [4] https://dataverse.harvard.edu/api/dataverses/kgwas/storage/quota?showInherited=true
  - [5] https://dataverse.harvard.edu/api/access/datafile/13913528
  - [6] https://github.com/IQSS/dataverse.harvard.edu/issues/199

## Harvard Dataverse

- `storage/harvard-dataverse` | qualifies-with-caveat | evidence documented | binding per-object-cap | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-22, checked 2026-10-21 (inherited) | stale on 2026-11-21
- url https://dataverse.harvard.edu
- free tier: 2.5 GB per file; 1 TB per Dataverse Collection for non-Harvard researchers (2.5 TB for Harvard affiliates). The 1 TB is real and stated by Harvard, but it is a service/support threshold, not a hard enforced cap. See limits. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 2.5 GB per file | bytes: 2500000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and unmetered. Public file access returns 303 -> a presigned S3 URL (dvn-cloud-iqss.s3.amazonaws.com) valid 3600s; S3 honours Range requests. No egress pricing exists anywhere in the product. Probe: GET /api/access/datafile/11685194 -L -H 'Range: bytes=0-1023' -> 303 then HTTP 206, Content-Range: bytes 0-1023/21269528, Server: AmazonS3. | metered: no
- identity: institution
- interface: s3, rest, rclone
- limits:
  - per-object-cap (binding): 2.5 GB per file [1]
  - write-gated: Review' spam-check gate, not peer review [1]
  - write-gated: curator rejecting a deposit at the review gate, and the storage-quota feature is flagge [1]
- limits note: Per-file 2.5 GB through the Harvard UI/API; larger files require the S3 direct-upload path, which Harvard has enabled (downloads already redirect to S3, so upload-redirect is configured). Dataset file-count cap observed live: effectiveDatasetFileCountLimit=1000 (12 used on the sampled dataset). No enforced collection quota: GET /api/dataverses/harvard/storage/quota?showInherited=true -> {"message":"No quota defined for this collection"}. Publishing is a 'Submit for Review' spam-check gate, not peer review.
- interface detail: rest
- tooling: Native REST API v6.10.1 (live: GET /api/info/version -> {"version":"6.10.1"}); SWORD v2 deposit; OAI-PMH harvest; S3 direct-upload API for files >2.5 GB (docs: 'This option can handle files >300GB'). Python client pyDataverse; R package dataverse. No rclone backend, but a REST loop is trivial (~15 lines) and the platform is a well-documented Invenio-free Java stack.
- composes with: Unlimited Dataverse Collections per account (Harvard: 9,755 collections / 306,011 datasets exist, anyone may create one). x 1 TB per collection. 20 collections = 20 TB in one account; 20 accounts = 400 TB. Also multiplies per dataset rather than per collection if the 1 TB is read as a guidance number, since no per-dataset quota is enforced on the root collection.
- reliability: Mature, 15+ year old service with DOI permanence and S3-backed bytes; the only soft failure mode is a curator rejecting a deposit at the review gate, and the storage-quota feature is flagged 'new and still experimental' upstream.
- notes: the same as the free tier
- evidence note: The quota endpoint answers were read on 2026-10-21. The record keeps reported because the per-file cap and the identity field were not measured. Was reported, now documented.
- extras:
  - verified[0].url: https://dataverse.harvard.edu/
  - verified[0].date: 2026-10-22
  - verified[0].via: none
  - verified[0].http_status: 0
  - verified[0].bytes: 0
  - verified[0].pattern_found: no
  - verified[0].what_changed: not read
  - unconfirmed[0].url: https://dataverse.harvard.edu/
  - unconfirmed[0].status: 0
  - unconfirmed[0].bytes: 0
  - unconfirmed[0].why: not read
- evidence:
  - [1] 2026-10-21: 'can deposit files of up to 2.5GB, and store up to 1TB of data on the Harvard Dataverse Repository'
  - [2] 2026-10-21: (updated Dec 3 2024) — 'free support for research data collections up to 1.0TB for non-Harvard researchers and groups and 2.5TB for Harvard affiliates'; paid Large Data Services only above 2.5TB
  - withheld 2026-10-21: probe: GET /api/dataverses/harvard/storage/quota?showInherited=true -> 'No quota defined for this collection'; GET /api/access/datafile/11685194 -> 303 to presigned S3 -> 206 Partial…
  - [3] 2026-10-22: the instance answers.
  - probe:https://dataverse.harvard.edu/api/dataverses/harvard/storage/quota?showInherited=true 2026-10-22: GET 2026-10-22: harvard 200/73 B 'No quota defined for this collection'; SEE_Precursors 200/104 B 'Total quota allocation for this collection: 1,099,511,627,776 bytes'; kgwas 200/104 B 2,748,779,069,440 bytes
- sources:
  - [1] https://support.dataverse.harvard.edu/researchers
  - [2] https://support.dataverse.harvard.edu/sites/g/files/omnuum821/files/2024-12/Harvard%20Dataverse%20Repository%20Large%20Data%20Services.pdf
  - [3] https://dataverse.harvard.edu/
