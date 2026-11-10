# KTH Data

> kth.se | Storage, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kth/ | JSON https://fshy.ajam.dev/api/v1/entity/kth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KTH Data Repository (launched 2025-01-29)

- `storage/kth-data-repository` | qualifies-with-caveat | evidence reported | binding per-object-cap | category newly launched institutional repository (InvenioRDM 14, KTH Royal Institute of Technology)
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://datarepository.kth.se
- free tier: 50 GB and 100 files per record by default; 10 GB per file. Quota increase is granted on email request to researchdata@kth.se. Not a hard wall. A record with a 70.4 GB single object exists in the public API, i.e. increases are real and granted. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 GB per file | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and anonymous access. Download links return HTTP 302 redirecting to presigned S3 URLs with 60-second expiration, requiring per-request URL resolution. | metered: no
- identity: institution | detail: institution
- interface: rest
- limits:
  - per-object-cap (binding): 10 GB per file [1]
- limits note: 100 files per record by default. 'For data governance reasons ... all data must belong to at least one community.' Files immutable after publication; one-month grace period.
- interface detail: InvenioRDM REST (/api/records), OAI-PMH, GitHub integration.
- tooling: curl; the InvenioRDM python client.
- composes with: Mountable via any InvenioRDM wrapper; the 60-second presign makes it a poor CDN origin unless fronted by Cloudflare with a re-resolving shim.
- reliability: Login is ORCID / GitHub / KTH SSO. Genuinely open. But deposit requires membership of a KTH community, and the quota-increase email asks which 'organisation, project, or grant' the data belongs to.
- notes: the same as the free tier
- evidence:
  - [2] 2026-10-21: 58 records; largest file 70,402,901,125 bytes (sensor_data.zip), then 11.86 GB and 10.89 GB
  - [3] 2026-10-21: 302 to presigned.s3.cloud.kth.se, X-Amz-Expires=60
  - [1] 2026-10-21: 'up to 100 files with a total volume of 50GB'; 'file uploads up to 10GB'; 'contact support to request an increase at researchdata@kth.se'
  - [4] 2026-10-21: KTH SSO, ORCID, GitHub
  - [5] 2026-10-21: launched 29 January 2025; 'we needed to customize InvenioRDM so that all data must belong to at least one community'
  - [6] 2026-10-21: offers GitHub, ORCID, SSO, email
- sources:
  - [1] https://docs.datarepository.kth.se/deposit/manage_files/
  - [2] https://datarepository.kth.se/api/records?size=50
  - [3] https://datarepository.kth.se/api/records/xme8h-jc618/files/sensor_data.zip/content
  - [4] https://docs.datarepository.kth.se/get_started/create_account/
  - [5] https://inveniosoftware.org/blog/2025-03-11-march-KTH-data-repository/
  - [6] https://datarepository.kth.se/login/

## NAISS / PDC

- `compute/naiss-pdc` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
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
- sources:
  - [1] https://www.pdc.kth.se/for-academic-researchers/doing-your-research-at-pdc-1.737528
