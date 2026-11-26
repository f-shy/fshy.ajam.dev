# cern open data portal

> cern.ch | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cern/ | JSON https://fshy.ajam.dev/api/v1/entity/cern.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## cern open data portal

- `storage/cern-open-data-portal` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:06.547Z (live) | stale on 2026-12-04
- url https://opendata.cern.ch/docs/terms-of-use
- free tier: none reachable: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity…
  - [2] 2026-10-21: cited as the basis of the rejection: Read-only for outsiders. It disseminates LHC experiment data under experiment data policies; there is no deposit path for a member of the public. Excellent free reads, zero write capacity, s
  - [1] 2026-11-19: it is a read source | capture: sha256:ad9d7d7e25c9df5cb4054ef36a2d1c8281a948e759f46fadd98247bcee98f559
- sources:
  - [1] https://opendata.cern.ch/docs/terms-of-use
  - [2] https://opendata.cern.ch/docs/about

## cern open data portal / cern document server as writable storage

- `storage/cern-open-data-portal-cern-document-server-as-writable-s` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:46.272Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/cern.md
- free tier: none reachable: Read-only dissemination platform for external users. Submissions require internal CERN accounts, with no public deposit path. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the CERN Open Data pages describe published datasets and cold storage but state no per-object size cap for deposit | note: not applicable
- retention: CERN Open Data states a preservation goal: "Long-term preservation: Suitability for archival retention policies."
- egress: CERN Open Data serves published datasets; cold-tier files must be staged before access: "Users may need to “stage” data (retrieve from cold to warm/hot storage) before access; this introduces delays." | metered: no
- identity: email
- interface: browser, rest
- interface detail: stated-absent: CERN Open Data is a web portal providing access to published datasets, with no programmatic deposit interface documented for external users
- tooling: not documented
- composes with: stated-absent: CERN Open Data is a read-only dissemination portal and states no way to chain it as writable storage into other services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Read-only dissemination for outsiders; CDS submissions are internal. No deposit path for a non-CERN account.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Read-only dissemination for outsiders; CDS submissions are internal. No deposit path for a non-CERN account.
  - [1] 2026-11-19: the portal still disseminates data outward and provides no public deposit path | capture: sha256:2ba89d979ea7c1905898e72336db59099226776ef7199c96f25f9188000558f7 | quote: The CERN Open Data portal is the access point to a growing range of data produced through the research performed at CERN. It disseminates the preserved output from various research activities and includes accompanying software and documentation needed to understand and analyse the data.
  - [2] 2026-11-19: CERN Open Data is a web portal that provides access to published datasets, not a writable byte store | capture: sha256:905f51687e293c5bc7b24b8da0f3ca474b40b321d1b147f702beba41e7c3ae14 | quote: We provide access to data and resources from the four big LHC collaborations
  - [3] 2026-11-19: CERN describes long-term preservation of its published datasets in cold storage | capture: sha256:d52fd6e2ae1f997f77a18991b35fe98ad474ca3bacf944298ea47956c26fbceb | quote: Long-term preservation: Suitability for archival retention policies.
  - [3] 2026-11-19: cold-tier datasets require staging before they can be retrieved | capture: sha256:d52fd6e2ae1f997f77a18991b35fe98ad474ca3bacf944298ea47956c26fbceb | quote: Users may need to “stage” data (retrieve from cold to warm/hot storage) before access; this introduces delays.
- sources:
  - [1] https://opendata.cern.ch/docs/about
  - [2] https://opendata.cern.ch/docs/welcome
  - [3] https://opendata.cern.ch/docs/colddata
