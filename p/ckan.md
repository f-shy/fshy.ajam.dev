# ckan's own default per-file cap

> ckan.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ckan/ | JSON https://fshy.ajam.dev/api/v1/entity/ckan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ckan's own default per-file cap

- `storage/ckan-s-own-default-per-file-cap-structural-applies-to-ev` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.060Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/ckan.md
- free tier: none reachable: The default deployment is hostile to bulk storage before any policy gate applies: ckan.max_resource_size defaults to 10 MB and ckan.max_image_size to 2 MB. Any portal that merely 'allows… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: CKAN default: "Also there are 10MiB limits on resource size and 2MiB limit on group/organization/user image size." | note: not applicable
- retention: stated-absent: the CKAN FileStore page describes resource and image uploads and states no retention period for stored files
- egress: stated-absent: the CKAN FileStore page describes uploads and storage backends but states no egress terms for stored bytes | metered: no
- identity: email
- interface: rest
- interface detail: CKAN FileStore uploads use the resource_create() and resource_update() action API functions with multipart/form-data and an extra upload key.
- tooling: not documented
- composes with: CKAN: "Resource files linked-to from CKAN or uploaded to CKAN’s FileStore can also be pushed into CKAN’s DataStore, which then enables data previews and a data API for the resources."
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The default deployment is hostile to bulk storage before any policy gate applies: ckan.max_resource_size defaults to 10 MB and ckan.max_image_size to 2 MB. Any portal that merely 'allows…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: The default deployment is hostile to bulk storage before any policy gate applies: ckan.max_resource_size defaults to 10 MB and ckan.max_image_size to 2 MB. Any portal that merely 'allows…
  - [1] 2026-11-19: the current CKAN configuration docs state the default per-file upload cap is 10 MB | capture: sha256:91f9b79969a6338626c2a3d24b9edb56a5bea7a4967cc93d8a0315570ff42df4 | quote: ckan.max_resource_size = 100 Default value: `10` The maximum in megabytes a resources upload can be.
  - [1] 2026-11-19: the current CKAN configuration docs state the default image upload cap is 2 MB | capture: sha256:91f9b79969a6338626c2a3d24b9edb56a5bea7a4967cc93d8a0315570ff42df4 | quote: ckan.max_image_size = 10 Default value: `2` The maximum in megabytes an image upload can be.
  - [2] 2026-11-19: CKAN FileStore uploads use the resource_create and resource_update action API functions over HTTP | capture: sha256:e810585ad7235c621f8cf38c6997ff006d0c08b97c58fcc4c1e5518928e3eb62 | quote: Files can be uploaded to the FileStore using the
  - [2] 2026-11-19: the page documents upload size settings but states no retention term | capture: sha256:e810585ad7235c621f8cf38c6997ff006d0c08b97c58fcc4c1e5518928e3eb62 | quote: ckan.max_resource_size = 10
  - [2] 2026-11-19: the default CKAN FileStore limits a resource upload to 10 MiB and an image to 2 MiB | capture: sha256:e810585ad7235c621f8cf38c6997ff006d0c08b97c58fcc4c1e5518928e3eb62 | quote: Also there are 10MiB limits on resource size and 2MiB limit on group/organization/user image size.
  - [2] 2026-11-19: CKAN FileStore files feed CKAN DataStore, enabling previews and a data API | capture: sha256:e810585ad7235c621f8cf38c6997ff006d0c08b97c58fcc4c1e5518928e3eb62 | quote: Resource files linked-to from CKAN or uploaded to CKAN’s FileStore can also be pushed into CKAN’s DataStore, which then enables data previews and a data API for the resources.
- sources:
  - [1] https://docs.ckan.org/en/latest/maintaining/configuration.html
  - [2] https://docs.ckan.org/en/2.12/maintaining/filestore.html
