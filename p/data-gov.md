# data.gov

> data.gov | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/data-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/data-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## data.gov (us federal catalog)

- `storage/data-gov` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:32.920Z (live) | stale on 2026-12-04
- url https://data.gov/contact/
- free tier: none reachable: Metadata-only harvester. It does not host data files and has no self-service publisher path at all: sources are federal agency data.json inventories. The contact page states plainly that it | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Metadata-only harvester. It does not host data files and has no self-service publisher path at all: sources are federal agency data.json inventories. The contact page states plainly that it
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Metadata-only harvester. It does not host data files and has no self-service publisher path at all: sources are federal agency data.json inventories. The contact page states plainly that it
  - [2] 2026-10-21: cited as the basis of the rejection: Metadata-only harvester. It does not host data files and has no self-service publisher path at all: sources are federal agency data.json inventories. The contact page states plainly that it
  - [1] 2026-11-19: the first-party contact page says the catalog does not hold data files | capture: sha256:f11396b9e2fd6655d5ea77a2f20ac2ec758b615cb828d003a5640df541f36467 | quote: Data.gov is a metadata catalog. We provide information about federal datasets and links to where data is published. We do not own or manage the underlying data.
  - [2] 2026-11-19: the first-party how-to says Data.gov does not host data files directly | capture: sha256:3c3f01e5a98955511109bb05e559cc9102c624c557971755dabbe1c25331d2e1 | quote: Data.gov is the federal government’s central open data catalog. It does not host data files directly.
- sources:
  - [1] https://data.gov/contact/
  - [2] https://resources.data.gov/resources/data-gov-open-data-howto/
