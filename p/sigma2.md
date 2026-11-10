# nird data

> sigma2.no | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sigma2/ | JSON https://fshy.ajam.dev/api/v1/entity/sigma2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NIRD Data Lake (Sigma2, Norway) — S3 object storage, 10 TB single-object support, 100M objects/bucket

- `storage/nird-data-lake-s3-object-storage-10-tb-single-object-sup` | paid-only | evidence documented | binding per-object-cap | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-04T01:24:31.183Z (live) | stale on 2026-12-05
- url https://documentation.sigma2.no/files_storage/nird/s3.html
- disagrees on identity_kind: `storage/nird-data-lake-data-peak-as-a-free-tier` says email, `storage/nird-data-lake-s3-object-storage-10-tb-single-object-sup` says institution
- disagrees on verdict: `storage/nird-data-lake-data-peak-as-a-free-tier` says fails-quota, `storage/nird-data-lake-s3-object-storage-10-tb-single-object-sup` says paid-only
- free tier: No fixed per-project byte number published. Quota is set per project by the Resource Allocation Committee (RFK) in TiB on NIRD Data Peak and/or Data Lake separately. What IS fixed and unusually generous: 'NIRD S3 supports 10TB single object sizes and up to 100 million objects per bucket', total NIRD capacity 75 PB (24 PB DP + 51 PB DL), and measured throughput '27GB/s'. | unit: TiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 TB per single object | bytes: 10000000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered; S3 and HTTPS serve directly, and NIRD S3 is explicitly for 'data sharing with external collaborators' and 'data streaming'. | metered: no
- identity: institution | detail: Applicants belong to a listed Norwegian organisation (universities and university colleges, governmental research centres, hospitals, industrial parties); the project leader holds a permanent, postdoctoral or temporary position; master and PhD students and guest researchers apply through a colleague.
- interface: s3, nfs, rclone, cli
- limits:
  - per-object-cap (binding): 10 TB per single object [1]
- limits note: Per-object-cap: 10 TB per single object, 100M objects per bucket. The most permissive object caps in this niche. Retention: 'long-term storage of non-persistent data'; Data Lake has NO on-demand backup ('On-demand backup | Yes | No'), only erasure coding and snapshots. request-rate: not published (27 GB/s aggregate is the claim). Gate: Norwegian university/research affiliation plus RFK allocation.
- interface detail: s3
- tooling: Rclone (provider = Other, endpoint https://s3.nird.sigma2.no), AWS CLI, s3cmd, MinIO client, Cyberduck. The same data is simultaneously available over POSIX, NFS and S3. 'the same data can be accessed simultaneously through multiple protocols'.
- composes with: Quota is per project and RFK-allocated, so the multiplier is project count and the DP/DL split (two resources, 'The two resources have separate quota based on the project allocation'). NIRD Data Lake is pitched at 'structured or unstructured data of any volume larger than 1 TiB'. I.e. the intended workload IS tens of TB.
- reliability: CRITICAL COST CAVEAT most agents will miss: NIRD is NOT free. The User Contribution Model (v2.2, valid from 1 Oct 2025) prices it at 'NIRD Data Lake 470 NOK per TB/year' and 'NIRD Data Peak 800 NOK per TB/year' for Category A, invoiced yearly to the institution. 20 TiB of Data Lake ≈ 9,400 NOK/yr. The bytes are unmetered but the TB-years are not. This fails the 'free' filter unless an EU-programme exemption applies ('Projects participating in EU programmes are exempted from contribution').
- notes: Priced per TB per year for an allocated project: Category A NIRD Data Lake 470 NOK per TB/year and NIRD Data Peak 800 NOK per TB/year (valid from 1 October 2025); projects participating in EU programmes are exempted from contribution.
- evidence note: documented: the 10 TB single-object size was read on 2026-11-03 at https://documentation.sigma2.no/files_storage/nird/s3.html, the Data Lake yearly price per TB at https://www.sigma2.no/user-contribution-model, the backup difference at https://documentation.sigma2.no/files_storage/nird/dp_dl.html and the applicant eligibility at https://www.sigma2.no/apply-e-infrastructure-resources.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No fixed per-project byte number published — quota is set per project by the Resource Allocation Committee (RFK) in TiB on NIRD Data Peak and/or Data Lake separately. What IS fixed and unusually generous: 'NIRD S3 supports 10TB single object sizes and up to 100 million objects per bucket', total NIRD capacity 75 PB (24 PB DP + 51 PB DL), and measured throughput '27GB/s'.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'NIRD S3 supports 10TB single object sizes and up to 100 million objects per bucket', rclone config with endpoint s3.nird.sigma2.no, 'measured throughput of 27GB/s'
  - [2] 2026-10-21: DP vs DL table: DL protocols 'POSIX, GPFS and NFS', 'S3'; 'On-demand backup | No'; 'storage for structured or unstructured data of any volume larger than 1 TiB'
  - [3] 2026-10-21: 'The total capacity of NIRD is 75 PB (24 PB on DP and 51 PB on DL)'
  - [4] 2026-10-21: captured 2025-12-06: 'NIRD Data Lake | 470 NOK per TB/year', 'NIRD Data Peak | 800 NOK per TB/year', 'All prices below are valid from 1 October 2025. The current version of the User Contribution model is V2.2.'
  - [5] 2026-10-21: probe: curl -D - -> HTTP/1.1 200 OK, Server: NooBaa/5.21.4, ListAllMyBucketsResult Owner NooBaa. Live and answering; NooBaa (not Ceph), which means S3-over-object-store namespace rather than RGW.
  - [6] 2026-10-21: probe: curl -X PUT --data x -> 404 (write correctly closed)
  - [4] 2026-11-03: Category A NIRD Data Lake costs 470 NOK per TB per year | capture: sha256:2b918a79cd28fd378cae2b0801eeecef350a74136be6856bc9341c6a761444a3 | quote: | NIRD Data Lake | 470 NOK per TB/year |
  - [7] 2026-11-03: students and guest researchers cannot apply directly; an eligible organisation and project leader are required | capture: sha256:020485bc1f33e9711a7011536422b23a3c725c0b5a6708e6b06baea7d84922b2 | quote: Note that master and PhD students and guest researchers cannot apply directly.
  - [4] 2026-11-03: EU-programme projects are exempt from the contribution | capture: sha256:2b918a79cd28fd378cae2b0801eeecef350a74136be6856bc9341c6a761444a3 | quote: Projects participating in EU programmes are exempted from contribution
  - [4] 2026-11-03: Category A NIRD Data Peak costs 800 NOK per TB per year | capture: sha256:2b918a79cd28fd378cae2b0801eeecef350a74136be6856bc9341c6a761444a3 | quote: | NIRD Data Peak | 800 NOK per TB/year |
  - [2] 2026-11-03: Data Peak has on-demand backup, Data Lake has none | capture: sha256:188ccd71a4200dc02c8023a49e314e34beb948a762228ad9b9f884cf48764aa2 | quote: | On-demand backup | Yes | No |
  - [1] 2026-11-03: the single-object size is 10TB | capture: sha256:c9286c7c84fa0f8bf3f6bf4b62016474cc64e88cdba933b5f2ab259fd097ee09 | quote: NIRD S3 supports 10TB single object sizes and up to 100 million objects per bucket.
  - [1] 2026-11-04: NIRD S3 supports 10 TB single objects | capture: sha256:d33cb1497c5e9376ee7574b7d4153f11e63024b51c315ffaaef4d07553040a98 | quote: NIRD S3 supports 10TB single object sizes and up to 100 million objects per bucket.
- sources:
  - [1] https://documentation.sigma2.no/files_storage/nird/s3.html
  - [2] https://documentation.sigma2.no/files_storage/nird/dp_dl.html
  - [3] https://documentation.sigma2.no/files_storage/nird_lmd.html
  - [4] https://www.sigma2.no/user-contribution-model
  - [5] https://s3.nird.sigma2.no/
  - [6] https://s3.nird.sigma2.no/probe-xyz/probe.txt
  - [7] https://www.sigma2.no/apply-e-infrastructure-resources

## nird data lake / data peak as a free tier (sigma2, norway)

- `storage/nird-data-lake-data-peak-as-a-free-tier` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.sigma2.no/user-contribution-model
- disagrees on identity_kind: `storage/nird-data-lake-data-peak-as-a-free-tier` says email, `storage/nird-data-lake-s3-object-storage-10-tb-single-object-sup` says institution
- disagrees on verdict: `storage/nird-data-lake-data-peak-as-a-free-tier` says fails-quota, `storage/nird-data-lake-s3-object-storage-10-tb-single-object-sup` says paid-only
- free tier: none reachable: Not free. The User Contribution Model v2.2 charges 470 NOK per TB/year for NIRD Data Lake and 800 NOK per TB/year for NIRD Data Peak. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The User Contribution Model v2.2 charges 470 NOK per TB/year for NIRD Data Lake and 800 NOK per TB/year for NIRD…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The User Contribution Model v2.2 charges 470 NOK per TB/year for NIRD Data Lake and 800 NOK per TB/year for NIRD Data
- sources:
  - [1] https://www.sigma2.no/user-contribution-model
