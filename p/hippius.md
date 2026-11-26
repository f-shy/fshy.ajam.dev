# hippius hub

> hippius.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hippius/ | JSON https://fshy.ajam.dev/api/v1/entity/hippius.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## hippius hub (hub.hippius.com / registry.hippius.com)

- `storage/hippius-hub` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:03.731Z (live) | stale on 2026-12-04
- url https://registry.hippius.com/v2/_catalog?n=3
- free tier: Hippius Hub is a live hosted service. Its Free plan gives 25 GB of private and 100 GB of public storage, with about 100 GB of pulls a month; paid plans go from $5 to $99 a month. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Creating the first namespace requires an account balance of at least $10 as a spam check; the Free plan itself stays free.
- notes: The most interesting-looking find that fails on both counts. It indexes 11,452 public models and 1,741 containers and is pullable with docker/oras. Exactly the ORAS-as-storage shape this su.
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The most interesting-looking find that fails on both counts. It indexes 11,452 public models and 1,741 containers and is pullable with docker/oras — exactly the ORAS-as-storage shape this…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The most interesting-looking find that fails on both counts. It indexes 11,452 public models and 1,741 containers and is pullable with docker/oras — exactly the ORAS-as-storage shape this…
  - [2] 2026-10-21: cited as the basis of the rejection: The most interesting-looking find that fails on both counts. It indexes 11,452 public models and 1,741 containers and is pullable with docker/oras — exactly the ORAS-as-storage shape this su
  - [3] 2026-11-19: Hippius Hub now offers a Free plan with 25 GB private and 100 GB public storage | capture: sha256:4434167b7f8e6f53143017fe7daf7e106bf89d285e711ff3ddf4beefc7148b19 | quote: Yes. The Free plan gives you 25 GB of private and 100 GB of public storage, with about 100 GB of pulls a month, and paid plans go from $5 to $99 a month.
  - [3] 2026-11-19: creating the first Hippius Hub namespace requires at least $10 account balance as a spam check | capture: sha256:4434167b7f8e6f53143017fe7daf7e106bf89d285e711ff3ddf4beefc7148b19 | quote: To create your first namespace, your account needs a balance of at least $10 as a spam check, but the plan itself stays free.
  - [3] 2026-11-19: the first-party Hippius Hub page documents the live Free plan | capture: sha256:4434167b7f8e6f53143017fe7daf7e106bf89d285e711ff3ddf4beefc7148b19 | quote: Yes. The Free plan gives you 25 GB of private and 100 GB of public storage, with about 100 GB of pulls a month, and paid plans go from $5 to $99 a month.
- sources:
  - [1] https://registry.hippius.com/v2/_catalog?n=3
  - [2] https://hippius.com
  - [3] https://hippius.com/hippius-hub
