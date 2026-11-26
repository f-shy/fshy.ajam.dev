# aruba cloud object storage

> aruba.it | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aruba/ | JSON https://fshy.ajam.dev/api/v1/entity/aruba.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## aruba cloud object storage / infomaniak object storage landing page

- `storage/aruba-cloud-object-storage-infomaniak-object-storage-lan` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:10.639Z (live) | stale on 2026-12-04
- url https://www.aruba.it/en/cloud/cloud-object-storage.aspx
- free tier: unverified: no free object-storage offer was found today: probes of the Aruba and Infomaniak product URLs returned a not-found status; the vendor still lists paid object storage with egress free up to 10 TB per organisation per month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Product URLs returned HTTP 404 on 2026-10-21. Infomaniak pricing on the Public Cloud page is EUR 0.01/GB (EUR 10/TB), with egress free up to 10 TB/month per organisation and metered thereafter.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Both product URLs 404; Infomaniak's real numbers sit on a Public Cloud price page EUR 0.01/GB = EUR 10/TB, egress free only to 10 TB/month per organisation, metered
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Both product URLs 404; Infomaniak's real numbers sit on a Public Cloud price page EUR 0.01/GB = EUR 10/TB, egress free only to 10 TB/month per organisation, metered
  - [2] 2026-10-21: cited as the basis of the rejection: Both product URLs 404; Infomaniak's real numbers sit on a Public Cloud price page EUR 0.01/GB = EUR 10/TB, egress free only to 10 TB/month per organisation, metered
  - [3] 2026-10-21: cited as the basis of the rejection: Both product URLs 404; Infomaniak's real numbers sit on a Public Cloud price page EUR 0.01/GB = EUR 10/TB, egress free only to 10 TB/month per organisation, metered
  - probe:https://www.aruba.it/en/cloud/cloud-object-storage.aspx 2026-11-19: a probe today confirms the Aruba product URL still returns HTTP 404 | capture: sha256:9ae8ec63ae76a728f432650b504f40eb1377629ce413ef72b505e9ba10c907df | quote: "status": 404
  - [4] 2026-11-19: the first-party Infomanik pricing page states 10 TB of included monthly outgoing traffic per organisation | capture: sha256:c4f7476f13c73f749422728cd664ff9f503799b7d31a11fc300eb041b4933648 | quote: Generally speaking, the incoming and outgoing traffic is free. With regard to storage, 10 TB are included per month and per organisation for outgoing traffic (the rate indicated on this page then applies).
  - probe:https://www.aruba.it/en/cloud/cloud-object-storage.aspx 2026-11-19: a direct probe of the product page returned HTTP 404 on 2026-11-19, confirming the dead verdict | capture: sha256:d40b5ab58eb0251f7ac47dd78c502e2b87ca72a43b2ebb89d0fcb18b67f3d427 | quote: "status": 404
- sources:
  - [1] https://www.aruba.it/en/cloud/cloud-object-storage.aspx
  - [2] https://www.infomaniak.com/en/hosting/object-storage
  - [3] https://pcr.cloud-mercato.com/providers/infomaniak/object-storage/infomaniak-os/pricing
  - [4] https://www.infomaniak.com/en/hosting/public-cloud/prices
