# DataONE Hosted

> dataone.org | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dataone/ | JSON https://fshy.ajam.dev/api/v1/entity/dataone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataONE Hosted Repository (TACC / UC Santa Barbara)

- `storage/dataone-hosted-repository-the-price-anchor-for-managed-1` | paid-only | evidence documented | binding volume-quota | category academic
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T15:04:37.250Z (live) | stale on 2026-12-04
- url https://www.dataone.org/hosted-repo/
- price ~$1285.14 per month, billed annually, for one Hosted Repository; the price of each further 1 TB increment is unverified: not published. | parsed USD 1285/mo
- free tier: none: the only tier with storage, the Hosted Repository, is priced at ~$1285.14 /mo, billed annually. DataONE Member and DataONE Plus are listed as Free with no stated byte allowance. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not separately metered; included in the subscription. | metered: yes
- identity: email | detail: The Hosted Repository request form requires an e-mail address and DataONE follows up to set the repository up; the payment method for the annual billing is not published.
- interface: rest
- limits:
  - volume-quota (binding): 1 TB repository capacity, expandable in 1 TB increments [1]
- limits note: Paid: ~$1,285.14/month billed annually. DataONE Member and DataONE Plus tiers are free but provide no storage of your own - Member is for repositories you already run, Plus is a portal/FAIR-reporting layer ('upload any file format' refers to portal ingestion, not a byte grant).
- binding note: capacity is sold per repository in 1 TB increments at a fixed monthly price, so the bill rises with stored volume
- interface detail: rest
- tooling: Metacat + MetacatUI (open source, self-hostable); DataONE Member Node REST API for programmatic deposit and read.
- composes with: Per repository, so multiple repositories = multiple subscriptions at the same list price. Useful mainly as the market price for what the free programmes give away.
- reliability: All data and metadata are replicated to two geographically independent data centers in California and Tennessee.
- notes: 1 TB repository capacity, 'Grow your 1 TB repository capacity based on your storage needs in 1 TB increments', replicated to two geographic regions (California and Tennessee), custom DOI prefix and custom domain.
- evidence note: the vendor pages of the 2026-11-03 evidence rows were read and captured (https://www.dataone.org/services/, https://www.dataone.org/hosted-repo/, https://www.dataone.org/jointhenetwork/); every field that decides the verdict cites one of those captures
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 TB repository capacity, 'Grow your 1 TB repository capacity based on your storage needs in 1 TB increments', replicated to two geographic regions (California and Tennessee), custom DOI prefix and custom domain.
  - dead_end.first_recorded: 2026-10-21
  - price_verbatim: $1,285.14 per TB per month (~$15,421/TB/year) - the ceiling of this market
- evidence:
  - [1] 2026-10-21: 'Hosted Repository ... ~$1285.14 /mo, billed annually'
  - [2] 2026-10-21: 'Grow your 1 TB repository capacity based on your storage needs in 1 TB increments'; replicas in California and Tennessee
  - [3] 2026-10-21: 'Joining our network as a member repository is free' (free = catalogue membership, not bytes)
  - [1] 2026-11-03: the Hosted Repository is priced at about $1285.14 per month billed annually | capture: sha256:e5b0d3bd10b31293a04d6cb9c68907271adb370f8dd752c9ae0387c93d149e76 | quote: ~$1285.14 /mo, billed annually
  - [1] 2026-11-03: storage is only in the priced tier | capture: sha256:e5b0d3bd10b31293a04d6cb9c68907271adb370f8dd752c9ae0387c93d149e76 | quote: ~$1285.14 /mo, billed annually
  - [1] 2026-11-03: no free byte allowance | capture: sha256:e5b0d3bd10b31293a04d6cb9c68907271adb370f8dd752c9ae0387c93d149e76 | quote: ~$1285.14 /mo, billed annually
  - [1] 2026-11-03: price of the Hosted Repository tier | capture: sha256:e5b0d3bd10b31293a04d6cb9c68907271adb370f8dd752c9ae0387c93d149e76 | quote: ~$1285.14 /mo, billed annually
  - [2] 2026-11-03: capacity is a repository volume, not a per-object cap | capture: sha256:c7e19394709c0a0aa354998ed02c13032478f180cb9db7e35e9b5111583df27a | quote: Grow your 1 TB repository capacity based on your storage needs in 1 TB increments
  - [2] 2026-11-03: capacity unit | capture: sha256:c7e19394709c0a0aa354998ed02c13032478f180cb9db7e35e9b5111583df27a | quote: Grow your 1 TB repository capacity based on your storage needs in 1 TB increments
  - [2] 2026-11-03: the limit row is a volume quota | capture: sha256:c7e19394709c0a0aa354998ed02c13032478f180cb9db7e35e9b5111583df27a | quote: Grow your 1 TB repository capacity based on your storage needs in 1 TB increments
  - [2] 2026-11-03: volume-priced capacity | capture: sha256:c7e19394709c0a0aa354998ed02c13032478f180cb9db7e35e9b5111583df27a | quote: Grow your 1 TB repository capacity based on your storage needs in 1 TB increments
  - [1] 2026-11-03: the offer is a priced subscription with no free byte allowance | capture: sha256:e5b0d3bd10b31293a04d6cb9c68907271adb370f8dd752c9ae0387c93d149e76 | quote: ~$1285.14 /mo, billed annually
  - [2] 2026-11-03: the Hosted Repository request form requires an e-mail address | capture: sha256:c7e19394709c0a0aa354998ed02c13032478f180cb9db7e35e9b5111583df27a | quote: E-mail address (required)
  - [1] 2026-11-03: a contact form leads to set-up | capture: sha256:e5b0d3bd10b31293a04d6cb9c68907271adb370f8dd752c9ae0387c93d149e76 | quote: If you’re ready to set up a hosted repository or want to learn more, please provide your information below and we’ll get in touch to get started.
  - [2] 2026-11-03: two-region replication | capture: sha256:c7e19394709c0a0aa354998ed02c13032478f180cb9db7e35e9b5111583df27a | quote: All data and metadata are replicated to two geographically independent data centers in California and Tennessee
  - [3] 2026-11-03: membership is free and carries no storage | capture: sha256:05b3c109784116d5521be396ca36f38e02b0a3da9edf94ca1940960b6b244ef2 | quote: Joining our network as a member repository is free, and just one of several ways to participate in DataONE
  - [1] 2026-11-03: the free portal needs no card; storage is only in the Hosted Repository tier | capture: sha256:e5b0d3bd10b31293a04d6cb9c68907271adb370f8dd752c9ae0387c93d149e76 | quote: Create a portal for free during the preview period. No credit card required.
- sources:
  - [1] https://www.dataone.org/services/
  - [2] https://www.dataone.org/hosted-repo/
  - [3] https://www.dataone.org/jointhenetwork/

## dataone

- `storage/dataone` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cn.dataone.org/cn/v2/node
- free tier: none reachable: It is a federation of member nodes, not a depositor. The Coordinating Node answers (cn.dataone.org/cn/v2/node -> 200 XML) but there is no general deposit endpoint; you must go through a… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: It is a federation of member nodes, not a depositor. The Coordinating Node answers (cn.dataone.org/cn/v2/node -> 200 XML) but there is no general deposit endpoint; you must go through a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It is a federation of member nodes, not a depositor. The Coordinating Node answers (cn.dataone.org/cn/v2/node -> 200 XML) but there is no general deposit endpoint; you must go through a…
  - [2] 2026-10-21: cited as the basis of the rejection: It is a federation of member nodes, not a depositor. The Coordinating Node answers (cn.dataone.org/cn/v2/node -> 200 XML) but there is no general deposit endpoint; you must go through a memb
- sources:
  - [1] https://cn.dataone.org/cn/v2/node
  - [2] https://www.dataone.org/use-data/
