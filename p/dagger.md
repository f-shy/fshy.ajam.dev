# Dagger Cloud

> dagger.io | CI runners, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dagger/ | JSON https://fshy.ajam.dev/api/v1/entity/dagger.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dagger Cloud

- `ci-cd-runners/dagger-cloud` | paid-only | evidence documented | binding volume-quota | category hosted CI pipeline engine with usage-based pricing and a monthly plan minimum | tier Starter USD 20 per month; Scale USD 200 per month
- needs card no, phone no, ID no, institution no | verified 2026-11-19T07:00:00.000Z (live) | stale on 2026-12-20
- url https://dagger.io/pricing/
- free tier: no free hosted tier: idle capacity is free, repeat cache work costs 5x less, and the Starter plan is USD 20 a month with a higher Scale plan at USD 200 a month | unit: mixed | metered on: none | read on: 2026-11-19 | source: [1]
- per-object cap: unverified: no per-object or build wall-clock cap stated in the first-party pages read | source: [1]
- retention: unverified: no number is stated in the first-party pages read | source: [1]
- egress: unverified: pipeline input and output data are billed by the GB, but the page states no free egress allowance | metered: no | source: [1]
- identity: email | detail: a Dagger Cloud account is needed for the hosted service; the exact form fields are unverified: behind a sign-up
- interface: cli, rest, git
- limits:
  - volume-quota (binding): pipeline CPU and memory are billed at USD 0.005 per CPU-minute and USD 0.005 per GB-minute for new work, and five times less for repeat work [1]
  - volume-quota (binding): pipeline inputs cost USD 0.025 per GB and outputs USD 0.10 per GB for new work, five times less for repeat work [1]
  - volume-quota (binding): the plan price or the usage bill is charged, whichever is higher; Starter is USD 20 a month and Scale USD 200 a month [1]
- binding note: there is no free hosted plan: the monthly minimum applies even when usage is below it, so the Starter price binds a reader with no budget
- interface detail: pipelines are written as code in an SDK and run as containers; the hosted cloud runs the same pipelines the open-source engine runs locally
- endpoint: unverified: no public API endpoint stated on the pages read
- tooling: pipelines as code in an SDK, executed as standard OCI containers with content-addressed caching
- composes with: a pipeline defined in code runs in containers on Dagger Cloud, with cache hits billed at a fifth of the rate of new work
- reliability: 
- notes: A hosted CI pipeline service with usage pricing and a monthly plan minimum. The open-source engine is a different offer already recorded under compute/dagger.
- evidence note: all values are quoted from the first-party pricing page read on 2026-11-19. The engine itself is open source and can run locally; this record is for the hosted Dagger Cloud service and its pricing. There is no standing free hosted tier on the page.
- evidence:
  - [1] 2026-11-19: idle capacity is free on the hosted service | capture: sha256:fa5ef1ca966dd9bea34f35487c68ac5c775682386f692df14b0b7c613424d852 | quote: ## Idle capacity is free
  - [1] 2026-11-19: repeat cache work is billed five times less | capture: sha256:fa5ef1ca966dd9bea34f35487c68ac5c775682386f692df14b0b7c613424d852 | quote: You pay 5× less for operations that could be served from cache, whether or not they actually are.
  - [1] 2026-11-19: the hosted Starter plan is USD 20 per month | capture: sha256:fa5ef1ca966dd9bea34f35487c68ac5c775682386f692df14b0b7c613424d852 | quote: Starter — $20/mo
  - [1] 2026-11-19: the monthly plan minimum applies | capture: sha256:fa5ef1ca966dd9bea34f35487c68ac5c775682386f692df14b0b7c613424d852 | quote: You pay the plan price or your usage, whichever is higher.
- sources:
  - [1] https://dagger.io/pricing/

## Dagger

- `compute/dagger` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:14.690Z (live) | stale on 2026-12-05
- url https://dagger.io
- free tier: the engine is open source and runs locally; the cloud runs the same pipelines, with no plan or price on this page | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Cloud usage pricing bills pipeline outputs (pushed container images and container egress) at 10 cents per GB for new work and 2 cents per GB for repeat work; no free allowance is stated; plans are Starter USD 20 a month and Scale USD 200 a month, billed at the higher of plan price or usage | metered: yes | price per TB: USD 100 per TB for new work, USD 20 per TB for repeat work | source: [2]
- identity: email
- interface: cli
- limits:
  - write-gated (binding): no plan or price is published; the local engine is free and the cloud path is priced elsewhere [1]
- interface detail: the dagger CLI, with modules and SDKs in Go, Python, TypeScript, Java, PHP, Elixir and Rust; engine selectable as cloud, local container, tcp, tls, ssh or kube-pod; no SDK term in the interface vocabulary
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes a portable pipeline engine that runs locally or in the vendor's cloud. It publishes no plan or price, so the free half is the software rather than capacity
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a pipeline is a DAG of cached steps; there is no machine to keep alive
  - free_tier_kind: allowance
  - ps.price: all cached automatically
  - ps.durability: content-addressed cache
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the cache is kept
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Dagger is the missing software stack for CI. It makes your pipelines faster and more repeatable, not by throwing bigger machines at them, but by replacing artisanal scripts with a clean API' and 'run it locally or let our cloud scale it out', quoted
  - [2] 2026-11-03: pipeline outputs (container egress) cost 10 cents per GB for new work and 2 cents per GB for repeat work | capture: sha256:fa5ef1ca966dd9bea34f35487c68ac5c775682386f692df14b0b7c613424d852 | quote: | Pipeline outputs | New work: 10¢ / GB | Repeat work: 2¢ / GB |
  - [3] 2026-11-03: the dagger CLI is the main interface | capture: sha256:f57943c6aef17b30e09bb7f56c79e0237a22a2f72ad5104b373e4c9f33df5e44 | quote: dagger [options] [subcommand | file...]
  - [1] 2026-11-03: modules are written against language SDKs | capture: sha256:fc1320878f77a7380a2672ba3bdd733f6cc80950d2eac0bad08b4dc44c451d4d | quote: Write your own Dagger modules in Go, Python, TypeScript, Java, PHP, Elixir, Rust or Dang
- sources:
  - [1] https://dagger.io
  - [2] https://dagger.io/pricing
  - [3] https://docs.dagger.io/reference/cli
