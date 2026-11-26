# datahub.io

> datahub.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datahub/ | JSON https://fshy.ajam.dev/api/v1/entity/datahub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## datahub.io

- `storage/datahub-io` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:43.470Z (live) | stale on 2026-12-04
- url https://datahub.io/pricing
- free tier: none reachable: Pivoted from open-data publishing to a paid 'Data Solutions' shop. /pricing 301s to /solutions (enterprise reference datasets, CSV, S3 API for customers); /publish is a 404. No free storage | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: Pivoted from open-data publishing to a paid 'Data Solutions' shop. /pricing 301s to /solutions (enterprise reference datasets, CSV, S3 API for customers); /publish is a 404. No free storage
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-21: Pivoted from open-data publishing to a paid 'Data Solutions' shop. /pricing 301s to /solutions (enterprise reference datasets, CSV, S3 API for customers); /publish is a 404. No free storage
  - [2] 2026-10-21: cited as the basis of the rejection: Pivoted from open-data publishing to a paid 'Data Solutions' shop. /pricing 301s to /solutions (enterprise reference datasets, CSV, S3 API for customers); /publish is a 404. No free storage
  - [3] 2026-10-21: cited as the basis of the rejection: Pivoted from open-data publishing to a paid 'Data Solutions' shop. /pricing 301s to /solutions (enterprise reference datasets, CSV, S3 API for customers); /publish is a 404. No free storage
  - [1] 2026-11-19: datahub.io now sells a paid data-solutions product with an S3 API for customers, not free storage | capture: sha256:55dee53aa8c69602b817b65c8a37bc834aaaf852b6c642f8962dff0b1a830b40 | quote: Get instant access to our S3 bucket for frictionless data retrieval, ensuring fast and scalable performance.
  - probe:https://datahub.io/publish 2026-11-19: the former open-data publishing route returns 404 today | capture: sha256:b55f99d4f7b9c321ceb7e27cc265a1f646fefe0a111f923501d0101b59e634a6 | quote: "status": 404
  - [1] 2026-11-19: the free open-data publishing service has been replaced by a paid data-solutions offering | capture: sha256:55dee53aa8c69602b817b65c8a37bc834aaaf852b6c642f8962dff0b1a830b40 | quote: Empower Your Innovation with Global Data Solutions
- sources:
  - [1] https://datahub.io/pricing
  - [2] https://datahub.io/solutions
  - [3] https://docs.datahub.io/
