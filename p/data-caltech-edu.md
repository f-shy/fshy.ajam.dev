# InvenioRDM platform

> data.caltech.edu | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-caltech-edu/ | JSON https://fshy.ajam.dev/api/v1/entity/data-caltech-edu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CaltechDATA (InvenioRDM, California Institute of Technology)

- `storage/caltechdata` | fails-identity | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.caltech.edu
- free tier: 1 TB of free storage per user, announced 2026-06-26, 'made possible through a National Science Foundation Campus Cyberinfrastructure grant' and backed by the Open Storage Network. Additional storage $200/TB one-time. 550 files max per record. | unit: objects | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unmetered egress. Downloads stream directly from data.caltech.edu. Storage resides on the Open Storage Network, an NSF-funded academic infrastructure fabric. | metered: no
- identity: institution
- interface: rest
- limits note: 550 files per record; deposit requires a Caltech (access.caltech) identity, which is the real gate. The API reads are fully anonymous but writes are not open to the public.
- interface detail: rest
- tooling: InvenioRDM REST API (/api/records, files under /api/records/<id>/files/<key>/content); purpose-built client caltechlibrary/caltechdata_api (github.com/caltechlibrary/caltechdata_api, 13 stars); the whole instance's source is public at caltechlibrary/caltechdata (11 stars) so the quota config is auditable
- composes with: Default allocation is 1 TB free per registered institutional user. Deposited records are not individually account-capped, providing higher baseline capacity than general repositories.
- reliability: Anonymous API reads work and are generous (X-RateLimit-Limit: 500 observed on /api/records). The 1 TB allocation is explicitly funded by a time-bounded NSF grant, so the number has a funding horizon attached.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB of free storage per user, announced 2026-06-26, 'made possible through a National Science Foundation Campus Cyberinfrastructure grant' and backed by the Open Storage Network. Additional storage $200/TB one-time. 550 files max per record.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: read live (Last Updated Jun 29, 2026): 'All users with an access.caltech account get 1 TB of free storage through CaltechDATA. Additional storage requires a one-time charge of $200 / TB ... Individual records can include a maximum of 550 files.'
  - [2] 2026-10-21: read live, dated 06/26/2026: 'All researchers at Caltech can now upload up to 1 TB of data for free ... possible due to the Open Storage Network'
  - [3] 2026-10-21: probe: GET -> 200 with X-RateLimit-Limit: 500; GET /api/records/mhmjd-4pr39/files/... content endpoint -> 200, files.enabled: true, per-file links resolve
- sources:
  - [1] https://libanswers.caltech.edu/faq/163212
  - [2] https://library.caltech.edu/blogs/news/caltechdata-expanded-storage
  - [3] https://data.caltech.edu/api/records?size=1

## InvenioRDM platform class — CaltechDATA, TU Graz, TU Wien, TalTech, KTH, Bamberg, MSD-Live

- `storage/inveniordm-platform-class-caltechdata-tu-graz-tu-wien-ta` | fails-identity | evidence reported | binding none | category academic repository / InvenioRDM 14.0–15.0
- needs card no, phone no, ID no, institution yes | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://data.caltech.edu
- free tier: Per-record, NOT per-account: RDM_FILES_DEFAULT_QUOTA_SIZE = 10 GB and RDM_FILES_DEFAULT_MAX_FILE_SIZE = 10 GB, with APP_RDM_DEPOSIT_FORM_QUOTA maxFiles = 100. Records are unlimited. This is the structural inverse of Dataverse: InvenioRDM ships a real quota and it is per-object, so total space is unbounded while each record is capped at 10 GB. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 GB/file | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Cloudflare-fronted on every instance checked. | metered: no
- identity: institution | detail: institution
- interface: rest, rclone, cli
- limits:
  - per-object-cap: 10 GB/file [1]
- limits note: per-object-cap 10 GB/record and 10 GB/file, 100 files/record. No per-account cap exists in the platform, so no instance can report one.
- interface detail: REST (/api/records), InvenioRDM REST API v1
- tooling: curl / invenio-cli / rclone via REST
- composes with: Excellent for the archive workload if registration were open, because 10 GB x unlimited records is unbounded in aggregate. It is not open on any instance tested.
- reliability: All seven instances 404 on /signup/, which in InvenioRDM means SECURITY_REGISTERABLE is off; only Zenodo (already counted elsewhere) and the CERN demo return anything other than 404.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Per-record, NOT per-account: RDM_FILES_DEFAULT_QUOTA_SIZE = 10 GB and RDM_FILES_DEFAULT_MAX_FILE_SIZE = 10 GB, with APP_RDM_DEPOSIT_FORM_QUOTA maxFiles = 100. Records are unlimited. This is the structural inverse of Dataverse: InvenioRDM ships a real quota and it is per-object, so total space is unbounded while each record is capped at 10 GB.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: RDM_FILES_DEFAULT_QUOTA_SIZE = 10 * (10**9); RDM_FILES_DEFAULT_MAX_FILE_SIZE = 10 * (10**9); RDM_FILES_DEFAULT_MAX_ADDITIONAL_QUOTA_SIZE = 0
  - [1] 2026-10-21: APP_RDM_DEPOSIT_FORM_QUOTA = {'maxFiles': 100, 'maxStorage': RDM_FILES_DEFAULT_QUOTA_SIZE}
  - [3] 2026-10-21: 200, records served; /signup/ — 404
  - [4] 2026-10-21: 200; /signup/ — 404
  - [5] 2026-10-21: 200; /signup/ — 404
  - [6] 2026-10-21: 200; /signup/ — 404
  - [7] 2026-10-21: 200; /signup/ — 404
  - [8] 2026-10-21: 200; /signup/ — 404
  - [9] 2026-10-21: 200; /signup/ — 502
  - [10] 2026-10-21: 308 (registration enabled on the demo); https://zenodo.org/signup — 308
- sources:
  - [1] https://github.com/inveniosoftware/invenio-app-rdm/blob/master/invenio_app_rdm/config.py
  - [2] https://github.com/inveniosoftware/invenio-rdm-records/blob/master/invenio_rdm_records/config.py
  - [3] https://data.caltech.edu/api/records?size=1
  - [4] https://repository.tugraz.at/api/records?size=1
  - [5] https://researchdata.tuwien.ac.at/api/records?size=1
  - [6] https://data.taltech.ee/api/records?size=1
  - [7] https://datarepository.kth.se/api/records?size=1
  - [8] https://fd-repo.uni-bamberg.de/api/records?size=1
  - [9] https://data.msdlive.org/api/records?size=1
  - [10] https://inveniordm.web.cern.ch/signup
