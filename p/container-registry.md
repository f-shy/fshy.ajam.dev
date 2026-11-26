# 8gears container registry

> container-registry.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/container-registry/ | JSON https://fshy.ajam.dev/api/v1/entity/container-registry.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 8gears container registry (container-registry.com)

- `storage/8gears-container-registry` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.936Z (live) | stale on 2026-12-04
- url https://container-registry.com/pricing/
- free tier: No standing free tier: the first-party documentation lists an individual plan with 1 GB of storage, and the signup page offers only a 14-day free trial, after which a paid subscription applies. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: No per-object size cap stated; storage is a project quota (individual 1 GB, dedicated 100 GB), not a per-object limit. | source: [1] | note: not applicable
- retention: No fixed retention period; artifacts are kept until removed by tag-retention rules or garbage collection, which the administrator schedules. | source: [1]
- egress: stated-absent: the first-party pages state no price or quota for traffic out of the registry | metered: no
- identity: email
- interface: oci, cli
- interface detail: An OCI container registry: push and pull images with Docker by tag or digest; a repository holds images, Helm charts and OCI indexes.
- tooling: not documented
- composes with: Chains with OCI tooling (Docker, Helm) and replicates to or from other registries; a proxy-cache project pulls through Docker Hub and other registries.
- reliability: Per-user dedicated Harbor instances with project-level storage quotas; the pricing markdown twin renders empty (JS-gated) and signup provisions a paid subscription instance rather than a…
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Per-user dedicated Harbor instances with project-level storage quotas; the pricing markdown twin renders empty (JS-gated) and signup provisions a paid subscription instance rather than a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Per-user dedicated Harbor instances with project-level storage quotas; the pricing markdown twin renders empty (JS-gated) and signup provisions a paid subscription instance rather than a…
  - [2] 2026-10-21: cited as the basis of the rejection: Per-user dedicated Harbor instances with project-level storage quotas; the pricing markdown twin renders empty (JS-gated) and signup provisions a paid subscription instance rather than a fre
  - [3] 2026-10-21: cited as the basis of the rejection: Per-user dedicated Harbor instances with project-level storage quotas; the pricing markdown twin renders empty (JS-gated) and signup provisions a paid subscription instance rather than a fre
  - [4] 2026-11-19: the first-party documentation now states 1 GB of storage on the individual plan | capture: sha256:dbde229ec4fddc22d190f5fad8ac62c93030bededc65d6641c61064382296bc2 | quote: | Storage | 1 GB | 100 GB | Custom |
  - [5] 2026-11-19: the first-party signup page offers only a 14-day free trial, not a standing free tier | capture: sha256:4cff1cd87e3cdaa4fd2a1611eb2a8bf60f3db49bac3228cf310bb938f5e5ba3e | quote: 14 days of free trial at no cost. Subscription can be canceled any time, no artificial barriers
  - [6] 2026-11-19: Container Registry is reached with Docker push and pull by tag or digest | capture: sha256:1262389f3772e12711dab54222ea69d951a2c320b8031b75a12f866753dfa722 | quote: Log in with Docker, tag an image for your Container Registry project, push it, and pull it back by tag or digest.
  - [7] 2026-11-19: the first-party artifact-types page documents images, Helm charts and OCI indexes | capture: sha256:6f5f69c9399687a594da319cb43007bf028714976f10c9b1d5de2f063210d56a | quote: A repository can hold images, Helm charts and OCI indexes side by side.
  - [8] 2026-11-19: retention is governed by administrator-defined tag-retention rules rather than a fixed vendor period | capture: sha256:29c2dde9c45ec93c655ef906209e156133bc8c85179bc72dc38fa6fa4c2af14b | quote: As a project administrator, you can save storage capacity by defining rules to govern the number and retention period of artifacts stored in a repository.
  - [9] 2026-11-19: the first-party quota page states project storage quotas and no per-object cap | capture: sha256:ac8ae10f8068a28edfe45cee44109b6d8ccdd4aa3e1edde16eba67e08c7c61b2 | quote: Individual accounts have 1 GB of storage included. Dedicated accounts have 100 GB.
  - [10] 2026-11-19: a proxy-cache project composes Container Registry with upstream registries | capture: sha256:560d0500b5f1bd2a8b5520f76df1c7c84c644733719fcbf588af19d39c03d9d5 | quote: Set up a proxy cache project and point your clients at it. They pull through Container Registry, which keeps a copy of each image and serves it from there next time.
  - [4] 2026-11-19: the first-party plan page states account pricing but no egress terms | capture: sha256:dbde229ec4fddc22d190f5fad8ac62c93030bededc65d6641c61064382296bc2 | quote: Individual accounts are completely free of charge.
  - [11] 2026-11-19: the first-party replication page documents moving artifacts between registries | capture: sha256:6587af78ccbd38f4396896cf6bf58c43c6e1aa82cb39acd7fb2ba932b5c42d4d | quote: Replication rules specify which artifacts will be moved between registries and how they should be moved.
- sources:
  - [1] https://container-registry.com/pricing/
  - [2] https://container-registry.com/pricing/index.md
  - [3] https://container-registry.com/llms.txt
  - [4] https://container-registry.com/docs/2.15/introduction/dedicated-vs-individual-account/index.md
  - [5] https://container-registry.com/signup/index.md
  - [6] https://container-registry.com/docs/2.15/getting-started-guide/push-and-pull-images/index.md
  - [7] https://container-registry.com/docs/2.15/user-manual/images/artifact-types/index.md
  - [8] https://container-registry.com/docs/2.15/user-manual/images/tags/tag-retention/index.md
  - [9] https://container-registry.com/docs/2.15/administration-manual/storage-management/project-quotas/index.md
  - [10] https://container-registry.com/docs/2.15/administration-manual/replication/proxy-cache-projects/index.md
  - [11] https://container-registry.com/docs/2.15/administration-manual/replication/replication-rules/index.md
