# KTH Data

> kth.se | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kth/ | JSON https://fshy.ajam.dev/api/v1/entity/kth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KTH Data Repository (launched 2025-01-29)

- `storage/kth-data-repository` | qualifies-with-caveat | evidence documented | binding per-object-cap | category newly launched institutional repository (InvenioRDM 14, KTH Royal Institute of Technology)
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T21:21:12.715Z (live) | stale on 2026-12-26
- url https://datarepository.kth.se
- free tier: By default, up to 100 files with a total size of 30 GB (30,000,000,000 bytes) per record; each file up to 30 GB. Quota increase is granted on request to researchdata@kth.se. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 30 GB per file | bytes: 30000000000 | source: [1] | note: Each file can be up to 30 GB, within the record's total quota.
- retention: You can only delete an unpublished record. Published records cannot be deleted except under special circumstances. If necessary, please submit a request via our support line. | source: [1] | note: A one-month grace period allows file modifications if errors are found.
- egress: Free and anonymous access. Download links return HTTP 302 redirecting to presigned S3 URLs with 60-second expiration, requiring per-request URL resolution. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits:
  - per-object-cap (binding): 30 GB per file [1]
- limits note: 100 files per record by default. 'For data governance reasons ... all data must belong to at least one community.' Files immutable after publication; one-month grace period.
- interface detail: The REST API calls for KTH Datarepository require authentication. The currently supported authentication method is through the use of Bearer tokens, which can be generated in the "Applications" section of your user account's settings in the KTH Datarepository.
- tooling: curl; the InvenioRDM python client.
- composes with: In the Files section of the deposit form, click the Import files button to import files from a previous version. Using this feature saves storage space as we don't duplicate the previous files.
- reliability: Login is ORCID / GitHub / KTH SSO. Genuinely open. But deposit requires membership of a KTH community, and the quota-increase email asks which 'organisation, project, or grant' the data belongs to.
- notes: 50 GB and 100 files per record by default; 10 GB per file. Quota increase is granted on email request to researchdata@kth.se. Not a hard wall. A record with a 70.4 GB single object exists in the public API, i.e. increases are real and granted.
- evidence:
  - [2] 2026-10-21: 58 records; largest file 70,402,901,125 bytes (sensor_data.zip), then 11.86 GB and 10.89 GB
  - [3] 2026-10-21: 302 to presigned.s3.cloud.kth.se, X-Amz-Expires=60
  - [1] 2026-10-21: 'up to 100 files with a total volume of 50GB'; 'file uploads up to 10GB'; 'contact support to request an increase at researchdata@kth.se'
  - [4] 2026-10-21: KTH SSO, ORCID, GitHub
  - [5] 2026-10-21: launched 29 January 2025; 'we needed to customize InvenioRDM so that all data must belong to at least one community'
  - [6] 2026-10-21: offers GitHub, ORCID, SSO, email
  - [1] 2026-11-19: the default per-record quota is 30 GB across up to 100 files | capture: sha256:286b54baf79476959494df8d5e63d3defc3ccd9e281f745749f8716a195fa853 | quote: By default, you can upload up to 100 files with a total size of 30 GB (30,000,000,000 bytes) per record.
  - [1] 2026-11-19: the per-file cap is now 30 GB | capture: sha256:286b54baf79476959494df8d5e63d3defc3ccd9e281f745749f8716a195fa853 | quote: Each file can be up to 30 GB, within the record's total quota.
  - [1] 2026-11-19: quota increases above 30 GB or 100 files are granted on request | capture: sha256:286b54baf79476959494df8d5e63d3defc3ccd9e281f745749f8716a195fa853 | quote: If you need more than 30 GB per record or 100 files, contact support to request an increase at
  - [1] 2026-11-25: each file is capped at 30 GB within the record quota | capture: sha256:286b54baf79476959494df8d5e63d3defc3ccd9e281f745749f8716a195fa853 | quote: Each file can be up to 30 GB, within the record's total quota.
  - [7] 2026-11-25: only unpublished records can be deleted; published records need special circumstances | capture: sha256:a205528643bcd72895898273c053c84c84e96416321dc01760e281a3bc0fc61d | quote: You can only delete an unpublished record. Published records cannot be deleted except under special circumstances. If necessary, please submit a request via our support line.
  - [1] 2026-11-25: a one-month grace period permits file changes, then only justified cases | capture: sha256:286b54baf79476959494df8d5e63d3defc3ccd9e281f745749f8716a195fa853 | quote: A one-month grace period allows file modifications if errors are found.
  - [8] 2026-11-25: the REST API requires a bearer token generated in account settings | capture: sha256:29c3d0fe80e8a75940036d16509fcc3dce94fb1f633f0556e11538723d5dfe1f | quote: The REST API calls for KTH Datarepository require authentication. The currently supported authentication method is through the use of Bearer tokens, which can be generated in the "Applications" section of your user account's settings in the KTH Datarepository.
  - [9] 2026-11-25: files can be imported from a previous version without duplicating storage | capture: sha256:0b4c3fc25f11602d921424dc63ffd727d39eb73a5d930c7ced4bd099e0a7bd59 | quote: In the Files section of the deposit form, click the Import files button to import files from a previous version. Using this feature saves storage space as we don't duplicate the previous files.
  - probe:https://datarepository.kth.se/api/records/xme8h-jc618/files/sensor_data.zip/content 2026-11-25: the URL parameter X-Amz-Expires is 60 | capture: sha256:66485b56a05432ac1ee464c6f0af26781494eb046c5c386da231a6a34d0508bf | quote: X-Amz-Expires=60
- sources:
  - [1] https://docs.datarepository.kth.se/deposit/manage_files/
  - [2] https://datarepository.kth.se/api/records?size=50
  - [3] https://datarepository.kth.se/api/records/xme8h-jc618/files/sensor_data.zip/content
  - [4] https://docs.datarepository.kth.se/get_started/create_account/
  - [5] https://inveniosoftware.org/blog/2025-03-11-march-KTH-data-repository/
  - [6] https://datarepository.kth.se/login/
  - [7] https://docs.datarepository.kth.se/deposit/manage_records/
  - [8] https://docs.datarepository.kth.se/deposit/rest_api/
  - [9] https://docs.datarepository.kth.se/deposit/manage_versions/

## NAISS / PDC

- `compute/naiss-pdc` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-11-25T11:17:31.401Z (live) | stale on 2026-12-26
- url https://www.pdc.kth.se/for-academic-researchers/doing-your-research-at-pdc-1.737528
- free tier: Small test allocations on the NAISS Dardel system can be applied for at any time, are handled locally within one to two weeks, and are free of charge to academic researchers at postdoctoral level or above. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: exploratory / test allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The free test allocation is for academic researchers at postdoctoral level or above, and the documented exception for people based outside Sweden requires membership of a Swedish research group with a Swedish supervisor. [1]
- limits note: The free test allocation is for academic researchers at postdoctoral level or above, and the documented exception for people based outside Sweden requires membership of a Swedish research group with a Swedish supervisor.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The out-of-Sweden exception is the only explicit statement found anywhere in documented allocations that a person based abroad can hold a Swedish allocation, and it still requires a Swedish group.
- reliability: no reliability event recorded
- notes: Documentation specifies that researchers based outside Sweden can receive compute allocations when affiliated with a Swedish research group or supervisor. Small test allocation sizes are not published.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: exploratory / test allocation
  - facets.shape.gpu_class: AMD MI250X (Dardel GPU partition)
- evidence:
  - [1] 2026-10-22: 'Academic researchers at postdoctoral level or above can use Dardel, free of charge, once they have been awarded an allocation of time'; 'Applications for smaller allocations can be put in at any time and are handled locally and quickly (within a week or two)', quoted
  - [1] 2026-10-22: 'Postgraduate (Ph.D.) students at Swedish universities (or who are based outside of Sweden, but are part of a Swedish research group or have a supervisor in Swedish academia) can be awarded time allocations', quoted
  - [1] 2026-11-25: postdoctoral-level academic researchers can use Dardel free of charge once awarded an allocation of time | capture: sha256:bf8241c14ec89f4c6de960af0b18a9645102b6d80a77eb83a5272a001da1e438 | quote: - Academic researchers at postdoctoral level or above can use Dardel, free of charge, once they have been awarded an allocation of time on the systems.
- sources:
  - [1] https://www.pdc.kth.se/for-academic-researchers/doing-your-research-at-pdc-1.737528
