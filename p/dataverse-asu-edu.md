# asu dataverse

> dataverse.asu.edu | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataverse-asu-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/dataverse-asu-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## asu dataverse / unc dataverse / uva dataverse (unverified openness)

- `storage/asu-dataverse-unc-dataverse-uva-dataverse` | fails-identity | evidence reported | binding none | category rejected-provider
- needs card no, phone no, ID no, institution yes | verified 2026-10-30T18:09:47.043Z (inherited) | stale on 2026-11-14
- url https://dataverse.asu.edu/api/info/version
- free tier: not stated at https://dataverse.asu.edu/api/info/version: the endpoint returns only the Dataverse software version, no free allowance | unit: none | metered on: none | read on: 2026-10-30 | source: [1] | note: the root-collection quota endpoint /api/dataverses/:root/storage/quota of the ASU, UNC and UVA installations answers 'No quota defined for this collection'
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: institution | detail: deposit is limited to institution affiliates: ASU-affiliated projects and people at ASU; UNC faculty, students, staff and affiliates at UNC, with external collaborators admitted only inside a UNC project dataverse; UVA employees and students at UVA
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: the three installations answer their version and root-collection quota endpoints with HTTP 200
- notes: ASU, UNC and UVA Dataverse installations: deposit is limited to institution affiliates, and the root collections define no storage quota
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: identity
  - dead_end.why: deposit at the ASU, UNC and UVA Dataverse installations is limited to institution affiliates
  - dead_end.retry_when: if an installation opens deposit to depositors with no affiliation
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 
  - [2] 2026-10-21: 
  - [3] 2026-10-21: 
  - [1] 2026-10-30: the cited endpoint answers HTTP 200 with a software version string and prints no free allowance | capture: sha256:d9ee4b3af76b7d1ccd01da256cec28038457fc362e159c72548612898bdf7fd2 | quote: {"status":"OK","data":{"version":"6.11 asu-6.11-oai-rights","build":null}}
  - [4] 2026-10-30: the ASU root collection defines no storage quota | capture: sha256:ca4a3e90fe2974286ac6bfbaed216f17cbc1c0f4ff266dd377ebf59530fc6d9f | quote: {"status":"OK","data":{"message":"No quota defined for this collection"}}
  - [5] 2026-10-30: the UNC root collection defines no storage quota | capture: sha256:04024c52a70b352765b9b0fc6c08244a11d685616965d2062c4de2b18e82c5ac | quote: {"status":"OK","data":{"message":"No quota defined for this collection"}}
  - [6] 2026-10-30: the UVA root collection defines no storage quota | capture: sha256:6e341fb8a16453bb8b3935a9c8273a4a77cb374a8a61f4d10a9f7a7a94adbc82 | quote: {"status":"OK","data":{"message":"No quota defined for this collection"}}
  - [2] 2026-10-30: the UNC installation answers its version endpoint with HTTP 200 | capture: sha256:706ceff6cfda83fec31fd77233c3fa5c56658d811834d86248e4006d825fcd4b | quote: {"status":"OK","data":{"version":"6.8","build":"with-mdq-bugfix"}}
  - [3] 2026-10-30: the UVA installation answers its version endpoint with HTTP 200 | capture: sha256:9a1efdccc84d0e888c91d2d957933a06863235a72d8fd74f4adce4b79fd9c245 | quote: {"status":"OK","data":{"version":"6.9","build":"2027-e2021d3"}}
  - [7] 2026-10-30: account creation at the UNC installation is limited to UNC faculty, students, staff and affiliates | capture: sha256:a4deaae241236d3012271edc17436fd529ebfc8da9fad4e88a62559be740e671 | quote: The UNC Dataverse user policy has recently been updated to limit account creation within UNC Dataverse to UNC faculty, students, staff, and affiliates.
  - [8] 2026-10-30: deposit to the ASU installation is limited to ASU-affiliated projects and people | capture: sha256:0574fa4e7e7e5877a75d339b28b3f03b6e8aec4be25fbadd9331736eaf6f41e6 | quote: Submission of datasets is limited to ASU-affiliated projects and people.
  - [9] 2026-10-30: deposit to the UVA installation is open to UVA employees and students | capture: sha256:c058b63fb6f8c39a2acabe4114292c3465a2984726410d23989a9250350ccf1b | quote: Any employee (faculty/staff) or student of the University may submit datasets to LibraData.
  - [7] 2026-10-30: the UNC installation accepts up to 2TB per project from eligible depositors | capture: sha256:a4deaae241236d3012271edc17436fd529ebfc8da9fad4e88a62559be740e671 | quote: UNC Dataverse accepts deposits of up to 2TB for a project.
- sources:
  - [1] https://dataverse.asu.edu/api/info/version
  - [2] https://dataverse.unc.edu/api/info/version
  - [3] https://dataverse.lib.virginia.edu/api/info/version
  - [4] https://dataverse.asu.edu/api/dataverses/:root/storage/quota
  - [5] https://dataverse.unc.edu/api/dataverses/:root/storage/quota
  - [6] https://dataverse.lib.virginia.edu/api/dataverses/:root/storage/quota
  - [7] https://tdx.unc.edu/TDClient/33/Portal/KB/Article/405/RDMC-UNC-Dataverse-Frequently-Asked-Questions
  - [8] https://asulibrary.atlassian.net/wiki/spaces/ARDRUD/pages/456949846
  - [9] https://library.virginia.edu/libra/datasets/libradata-faq
