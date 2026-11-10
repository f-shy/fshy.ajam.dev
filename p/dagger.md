# Dagger

> dagger.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dagger/ | JSON https://fshy.ajam.dev/api/v1/entity/dagger.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

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
