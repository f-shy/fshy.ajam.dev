# Azion

> azion.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/azion/ | JSON https://fshy.ajam.dev/api/v1/entity/azion.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Azion

- `compute/azion` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:01:15.543Z (live) | stale on 2026-12-05
- url https://www.azion.com/en/pricing/
- free tier: The Hobby plan is free with all platform features: 8 hours of compute time a month, 3 million function requests a month, 1 TB a month of data transfer, 10 workloads and 1 workspace, with no card. Each invocation is capped at 512 MB of isolate memory, 2 s of CPU time, 5 minutes of wall clock, 50 sub-requests and a 100 MB body. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: monthly-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Hobby includes 1 TB a month of data transfer; Hobby has no overage price, and usage above the limits may need an upgrade or restrict the account. Pro and Enterprise bill beyond the included amount at on-demand prices. | metered: no | free allowance: 1 TB / month (Hobby) | price per TB: Hobby: no overage price published. Pro and Enterprise on-demand: USD 0.085 per GB in the United States for the next 9 TB after the first 1 TB, i.e. USD 85 per TB (USD 0.11 per GB in Brazil, USD 0.198 per GB in Latam and other regions) | source: [1]
- identity: email
- interface: cli, rest, graphql
- limits:
  - volume-quota (binding): 8 compute-hours a month is the wall, not the 3 million requests: at the 2 s per-invocation CPU ceiling that is 14,400 maximum-length invocations before the allowance is gone, while the request counter would still read 0.5 percent used. [1]
- limits note: 8 compute-hours a month is the wall, not the 3 million requests: at the 2 s per-invocation CPU ceiling that is 14,400 maximum-length invocations before the allowance is gone, while the request counter would still read 0.5 percent used.
- binding note: the same as limits note
- interface detail: CLI, API, GraphQL API and Terraform, per the Azion pricing page: "CLI, API, GraphQL API, Terraform"
- tooling: the azion CLI, per the Azion CLI page: "puts the Azion Platform behind one terminal command, `azion`"
- composes with: 8 compute-hours plus 1 TB of egress a month is the largest free egress allowance found among evaluated providers, so the shape that fits is a mostly-cached site with a thin function edge; the 2 s CPU ceiling per call forces the heavy work off the edge.
- reliability: no reliability event recorded
- notes: Possibilities: (a) compute time is wall clock rather than CPU, which would make 8 hours equal 8 hours of wall clock; not settled by the page, which defines it as total execution accumulated and separately caps CPU at 2 s and wall clock at 5 min per invocation. Both readings are stated in the record. (b) The 3M request allowance binds first for a high-request, low-CPU workload; that is true and it is the second wall, not the first for anything that computes. The 530-ms-class cold start was not measured.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: monthly-allowance
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: Hobby: Compute Time 8 hours/month included, Requests 3M/month included, Data Transfer 1 TB/month included, Workloads 10 included, quoted
  - [2] 2026-10-22: Memory per isolate 512 MB; max CPU execution time 2 s; max execution time 5 min; sub-requests 50; body 100 MB on Hobby; exceeding Hobby included usage may require an upgrade and the account may be restricted, quoted
  - [3] 2026-10-22: the Hobby plan is offered at no cost and Azion may modify, suspend or terminate it and disable accounts with or without prior notice, quoted
  - [1] 2026-11-03: Hobby has no overage price: usage above the limits may need an upgrade or restricts the account | capture: sha256:85b3dfba5b5c632de5064532c0e26857a91e5c683940d3d1cebad8441509c7a4 | quote: For the Hobby plan, if you exceed included usage or resource limits, you may need to upgrade or your account may be restricted.
  - [1] 2026-11-03: Hobby includes 1 TB a month of data transfer | capture: sha256:85b3dfba5b5c632de5064532c0e26857a91e5c683940d3d1cebad8441509c7a4 | quote: | Data Transfer | 1 TB / month included | 2 TB / month included | Custom |
  - [4] 2026-11-03: Pro and Enterprise on-demand data transfer after the first TB is USD 0.085 per GB in the United States | capture: sha256:524bd12e89286e8a42faa1af2bf5e8dbdaf64a3bfc2c1ffba8c25a433b972f35 | quote: | Next 9 TB / month | $0.085 | $0.085 | $0.085 | $0.11 | $0.198 | $0.198 |
  - [1] 2026-11-03: CLI, API, GraphQL API and Terraform are included in every plan | capture: sha256:85b3dfba5b5c632de5064532c0e26857a91e5c683940d3d1cebad8441509c7a4 | quote: | CLI, API, GraphQL API, Terraform | ✓ | ✓ | ✓ |
  - [5] 2026-11-03: the API is a REST API | capture: sha256:84fc938498774966a5d6d9a756d640e38db14e1047fde42f424ae99f1e46b37e | quote: Azion API exposes the resources of your Azion account as a REST API over HTTPS, at the base URL `https://api.azion.com/v4`.
  - [6] 2026-11-03: the CLI is the azion binary | capture: sha256:a5629af5071622c330cad1545b685bc01e16d276b220522402ea0cc2519c570d | quote: Azion CLI puts the Azion Platform behind one terminal command, `azion`, an [open-source](https://github.com/aziontech/azion-cli/) binary written in Go.
  - [1] 2026-11-04: the pricing page lists CLI, API, GraphQL API and Terraform | capture: sha256:85b3dfba5b5c632de5064532c0e26857a91e5c683940d3d1cebad8441509c7a4 | quote: CLI, API, GraphQL API, Terraform
  - [6] 2026-11-04: the CLI page names the azion command | capture: sha256:a5629af5071622c330cad1545b685bc01e16d276b220522402ea0cc2519c570d | quote: puts the Azion Platform behind one terminal command, `azion`
- sources:
  - [1] https://www.azion.com/en/pricing/
  - [2] https://www.azion.com/en/documentation/platform/functions/limits/
  - [3] https://www.azion.com/en/documentation/agreements/azion-plans-terms-and-conditions/
  - [4] https://www.azion.com/en/documentation/products/pricing/
  - [5] https://www.azion.com/en/documentation/devtools/api/
  - [6] https://www.azion.com/en/documentation/products/azion-cli/
