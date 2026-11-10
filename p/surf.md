# SURF

> surf.nl | Storage, Compute; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/surf/ | JSON https://fshy.ajam.dev/api/v1/entity/surf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SURF Research Drive (Netherlands) — up to 5 TB free via NWO-funded Small Compute applications

- `storage/surf-research-drive-up-to-5-tb-free-via-nwo-funded-small` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.surf.nl/en/services/storage-data-management/research-drive
- free tier: Community Edition: 'Are you working at an institution without its own Research Drive environment? Then apply for access to Research Drive Community Edition here. You will receive up to 5 TB of storage space.' Institutional instances have their own (much larger) quotas set per institution. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered. SURF is the Dutch national e-infrastructure, no egress product exists. | metered: no
- identity: institution
- interface: s3, webdav, rclone
- limits note: Per-object-cap: not published for Research Drive; the SURF bundle page caps 'max. 10TB project space storage' on Snellius and 'up to 200TB disk storage' on Grid/Spider. request-rate: not published. Retention: tied to the project; SURF states data is retained for the project duration. Gate: 'researchers must have either a tenured appointment .. or a tenure track appointment at one of the research organisations listed'. A genuinely institution-gated, NWO-funded scheme.
- interface detail: webdav
- tooling: Research Drive is ownCloud/Nextcloud-based, so the standard desktop sync client and WebDAV endpoints work; rclone's webdav backend applies. Not S3.
- composes with: Grants 5 TB per project via Small Compute. The same application also provides up to 10 TB project storage on Snellius, up to 200 TB disk storage and 300 TB tape storage on Grid/Spider for data processing, and up to 50 TB offline tape storage.
- reliability: servicedesk.surf.nl returns 401 to the reader and www.surf.nl intermittently 504s; the numbers here come from the live NWO page and a 2026-03-11 Wayback capture of the Research Drive page.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Research Drive - via SURF max. 5TB or via institution', 'max. 50TB offline tape storage, if required max. 10TB project space storage', 'up to 200TB disk storage, 300TB tape storage', 'tenured appointment ... or a tenure track appointment'
  - [2] 2026-10-21: captured 2026-03-11: 'Then apply for access to Research Drive Community Edition here. You will receive up to 5 TB of storage space.'
  - [3] 2026-10-21: probe: read on -> 401 (authenticated wiki)
- sources:
  - [1] https://www.surf.nl/en/small-compute-applications-nwo
  - [2] https://www.surf.nl/en/services/storage-data-management/research-drive
  - [3] https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/117178927/RD+Getting+started

## SURF

- `compute/surf` | fails-identity | evidence documented | binding write-gated | category national HPC allocation
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.surf.nl/en/small-compute-applications-nwo
- free tier: A Small Compute application can request "up to and including 1,000,000 CPU or GPU SBU (standard billing units) of cluster computing on Snellius Supercomputer", "Up to and including 500,000 CPU core-hours and/or 14,000 GPU hours of cluster computing on the LUMI pre-exascale supercomputer", "up to and including 1,000,000 CPU core hours or 10,000 GPU hours of Data Processing on Grid and/or Spider", and "up to and including 50,000 CPU core hours or 5,000 GPU hours of cloud computing on HPC Cloud via SURF Research Cloud", with a maximum duration of one year. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: continuous-small-allocation
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): Eligibility is a tenured or tenure-track appointment at a Dutch university, university of applied sciences, university medical centre, KNAW or NWO institute, and a temporary appointment qualifies only if the employer guarantees the project's completion, so the 14,000 LUMI GPU-hours are unreachable without a Dutch contract. [1]
- limits note: Eligibility is a tenured or tenure-track appointment at a Dutch university, university of applied sciences, university medical centre, KNAW or NWO institute, and a temporary appointment qualifies only if the employer guarantees the project's completion, so the 14,000 LUMI GPU-hours are unreachable without a Dutch contract.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the largest set of numbers in the file reachable without a competitive review: 14,000 LUMI GPU-hours plus 500,000 LUMI core-hours plus a million SBU on Snellius, decided on technical feasibility in about two weeks. It composes badly with nothing except the Dutch contract, which is the whole gate.
- reliability: no reliability event recorded
- notes: SURF and NWO Small Compute allocations provide scientific computing and Snellius cluster core-hours for Netherlands-affiliated academic researchers via feasibility review.
- extras:
  - facets.class: national-hpc
  - facets.free_tier_kind: continuous-small-allocation
  - facets.shape.gpu_class: AMD MI250X (LUMI-G)
- evidence:
  - [1] 2026-10-22: up to 1,000,000 CPU or GPU SBU on Snellius; up to 500,000 CPU core-hours and/or 14,000 GPU hours on LUMI; up to 1,000,000 CPU core hours or 10,000 GPU hours of data processing; up to 50,000 CPU core hours or 5,000 GPU hours of HPC Cloud, quoted
  - [1] 2026-10-22: "researchers must have either a tenured appointment [...] or a tenure track appointment at one of the research organisations listed below"; for small applications a temporary appointment qualifies only if the organisation "guarantees the computing time project's duration and completion", quoted
  - [2] 2026-10-22: "Affiliates of one of the Dutch Universities or Grand Technology Institutes can submit an application for compute resources through NWO", quoted
  - [3] 2026-10-22: "A researcher may submit a maximum of one computing time application per compute facility per calendar year directly to SURF"; maximum duration one year, quoted
  - [4] 2026-10-22: "These requests will only be assessed on technical feasibility by SURF and are usually handled within 2 weeks", quoted
- sources:
  - [1] https://www.surf.nl/en/small-compute-applications-nwo
  - [2] https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660190/Obtaining+an+account+on+Snellius
  - [3] https://www.nwo.nl/en/calls/computing-time-on-national-computing-facilities-0
  - [4] https://servicedesk.surf.nl/wiki/display/WIKI/Small+Compute+applications

## surf spider / data archive as a free self-service tier

- `storage/surf-spider-data-archive-as-a-free-self-service-tier` | fails-identity | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:43.357Z (live) | stale on 2026-11-19
- url https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/117178927/RD+Getting+started
- free tier: NWO Small Compute application (funded by NWO, applied for through SURF): a Grid/Spider data-processing allocation includes up to 200TB disk and 300TB tape; Snellius and HPC Cloud allocations include up to 50TB offline tape; Research Drive up to 5TB. Eligibility is limited to researchers with a tenured or tenure-track appointment at listed Dutch research organisations. | unit: TB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: institution
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Applications are made through SURF, funded by NWO, one application per applicant per type of service per calendar year; access follows within 1 to 2 weeks of an application.
- notes: Tape archive access is requested through SURF's servicedesk and is institution- and application-gated (the free route is the NWO Small Compute application, which caps at 300 TB tape but…
- evidence note: re-read on 2026-11-03: the vendor page https://www.surf.nl/en/small-compute-applications-nwo; it states the 200TB disk and 300TB tape allocation, the tenured or tenure-track eligibility and the one application per year rule; identity_cost.detail is not read from a page, so confidence stays reported
- extras:
  - dead_end.failure_class: not-storage
  - dead_end.why: Tape archive access is requested through SURF's servicedesk and is institution- and application-gated (the free route is the NWO Small Compute application, which caps at 300 TB tape but…
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Tape archive access is requested through SURF's servicedesk and is institution- and application-gated the free route is the NWO Small Compute application, which caps at 300 TB tape but requ
  - [2] 2026-10-21: cited as the basis of the rejection: Tape archive access is requested through SURF's servicedesk and is institution- and application-gated the free route is the NWO Small Compute application, which caps at 300 TB tape but requ
  - [2] 2026-11-03: the Grid/Spider allocation includes up to 200TB disk and 300TB tape | capture: sha256:db503af509d3506d2f65338fc79749a7b566a1288dd253363cc557588e84cd8d | quote: Up to and including 1,000,000 CPU core hours or 10,000 GPU hours of Data Processing on Grid and/or Spider (including up to 200TB disk storage, 300TB tape storage
  - [2] 2026-11-03: the allocation is stated in TB | capture: sha256:db503af509d3506d2f65338fc79749a7b566a1288dd253363cc557588e84cd8d | quote: Up to and including 1,000,000 CPU core hours or 10,000 GPU hours of Data Processing on Grid and/or Spider (including up to 200TB disk storage, 300TB tape storage
  - [2] 2026-11-03: the storage allocation is a stored-bytes amount | capture: sha256:db503af509d3506d2f65338fc79749a7b566a1288dd253363cc557588e84cd8d | quote: Up to and including 1,000,000 CPU core hours or 10,000 GPU hours of Data Processing on Grid and/or Spider (including up to 200TB disk storage, 300TB tape storage
  - [2] 2026-11-03: applicants must hold a tenured or tenure-track appointment at a listed organisation | capture: sha256:db503af509d3506d2f65338fc79749a7b566a1288dd253363cc557588e84cd8d | quote: researchers must have either a tenured appointment (and therefore hold a paid position for an indefinite period) or a tenure track appointment at one of the research organisations listed below.
  - [2] 2026-11-03:  | capture: sha256:db503af509d3506d2f65338fc79749a7b566a1288dd253363cc557588e84cd8d | quote: Up to and including 1,000,000 CPU core hours or 10,000 GPU hours of Data Processing on Grid and/or Spider (including up to 200TB disk storage, 300TB tape storage
  - [2] 2026-11-03: one application per type of service per calendar year | capture: sha256:db503af509d3506d2f65338fc79749a7b566a1288dd253363cc557588e84cd8d | quote: Each applicant may submit one application per type of service, per calendar year.
  - [2] 2026-11-03: the allocation is applied for through SURF and funded by NWO | capture: sha256:db503af509d3506d2f65338fc79749a7b566a1288dd253363cc557588e84cd8d | quote: Applications are done through SURF, but funded by NWO.
  - [2] 2026-11-04: one application per type of service per calendar year | capture: sha256:ffa3959b23e23963004be2495fd5dfebf04b4a0bc9439ac5d2aba5d26764ac90 | quote: Each applicant may submit one application per type of service, per calendar year.
- sources:
  - [1] https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/117178927/RD+Getting+started
  - [2] https://www.surf.nl/en/small-compute-applications-nwo
