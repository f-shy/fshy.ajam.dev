# deic interactive hpc

> sdu.dk | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sdu/ | JSON https://fshy.ajam.dev/api/v1/entity/sdu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## deic interactive hpc / ucloud (denmark)

- `storage/deic-interactive-hpc-ucloud` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:34.056Z (live) | stale on 2026-12-04
- url https://docs.cloud.sdu.dk/guide/resources-products.html
- free tier: none reachable: Storage is a Weka filesystem product granted through a reviewed 'grant application' scored by an internal committee per provider, requested in GB with no published default. It is… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: write-gated
  - dead_end.why: Storage is a Weka filesystem product granted through a reviewed 'grant application' scored by an internal committee per provider, requested in GB with no published default. It is…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Storage is a Weka filesystem product granted through a reviewed 'grant application' scored by an internal committee per provider, requested in GB with no published default. It is…
  - [2] 2026-10-21: cited as the basis of the rejection: Storage is a Weka filesystem product granted through a reviewed 'grant application' scored by an internal committee per provider, requested in GB with no published default. It is POSIX-on-Ku
  - [1] 2026-11-19: storage is requested in GB through an allocation grant, with no published free allowance | capture: sha256:d1a0c29ba3da3c4df529db3555f960ae54c2f5218779f611e74d1ffa2aa43107 | quote: When applying for storage resources, users need to specify the total amount of resources for these products in GB. Data can be stored for a duration at least as long as the allocation grant period.
  - [2] 2026-11-19: the grant is reviewed by an internal committee per provider | capture: sha256:ac23937287ed62dcba09d636c7ce88a43f0d9d38dd2b5415187d69260ad4ab53 | quote: The grant application will be reviewed by an internal committee, one for each provider included in the application.
- sources:
  - [1] https://docs.cloud.sdu.dk/guide/resources-products.html
  - [2] https://docs.cloud.sdu.dk/guide/resources-grant.html
