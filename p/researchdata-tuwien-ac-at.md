# small institutional inveniordm instances

> researchdata.tuwien.ac.at | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/researchdata-tuwien-ac-at/ | JSON https://fshy.ajam.dev/api/v1/entity/researchdata-tuwien-ac-at.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## small institutional inveniordm instances (tu wien, kth, taltech, tu graz, b

- `storage/small-institutional-inveniordm-instances-tu-wien-kth-tal` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:50.378Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/researchdata-tuwien-ac-at.md
- free tier: none reachable: Published documentation states no numeric per-record quota. Instances host small document metadata rather than bulk data. Record counts remain low across instances. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: Each file can be up to 30 GB, within the record's total quota. | note: not applicable
- retention: Long-term preservation is stated; no automatic deletion period is stated on https://researchdata.tuwien.at/tuw/about
- egress: not stated on https://inveniordm.docs.cern.ch/reference/rest_api_quickstart | metered: no
- identity: email
- interface: rest
- interface detail: InvenioRDM REST API uploads file content into a record draft, then publishes the record.
- tooling: not documented
- composes with: Files are uploaded into an InvenioRDM record draft through the REST API and published as a citable record.
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Record counts are in the tens-to-hundreds KTH 58…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Record counts are in the tens-to-hundreds KTH 58, Tal
  - [1] 2026-11-19: TU Wien Research Data is an InvenioRDM platform for TU Wien members and partners, not an open deposit service | capture: sha256:c721c8f3f47dcfd11511c925ee6358ea0087a095b5925b0795100e1836931f8b | quote: The TU Wien Research Data Repository (powered by InvenioRDM 14.0) is an institutional platform that enables TU Wien members and partners to share and preserve research data and code.
  - [2] 2026-11-19: External users are not automatically granted upload permission on this InvenioRDM instance | capture: sha256:e334291d87d5b7b3578fc2021c30edf6d75e31cc588478636cbb00adb151563d | quote: Login is possible for members of TU Wien via their TU Wien account (single sign-on). Other users can log in with their identity provider if available but will not be automatically granted permission to upload content.
  - [3] 2026-11-19: InvenioRDM file content is uploaded over a REST API endpoint | capture: sha256:8491f526dab6da41380f72598706b5604164c8547cf9eb2f72e0d46d687a2ce7 | quote: curl -i -X PUT https://inveniordm.web.cern.ch/api/records/ha4g3-7x208/draft/files/data.csv/content
  - [4] 2026-11-19: the TU Wien repository states long-term preservation with no numeric expiry | capture: sha256:c721c8f3f47dcfd11511c925ee6358ea0087a095b5925b0795100e1836931f8b
  - [5] 2026-11-19: the KTH InvenioRDM instance states a 30 GB per-file cap | capture: sha256:286b54baf79476959494df8d5e63d3defc3ccd9e281f745749f8716a195fa853 | quote: Each file can be up to 30 GB, within the record's total quota.
- sources:
  - [1] https://researchdata.tuwien.ac.at/tuw/about
  - [2] https://www.tuwien.at/index.php?eID=dms&path=Documents%2FData%20Protection%20Declaration%20Other%2FData_Protection_Information_Research_Data.pdf&s=4
  - [3] https://inveniordm.docs.cern.ch/reference/rest_api_quickstart
  - [4] https://researchdata.tuwien.at/tuw/about
  - [5] https://docs.datarepository.kth.se/deposit/manage_files
