# Hailo Developer Zone

> hailo.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hailo/ | JSON https://fshy.ajam.dev/api/v1/entity/hailo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hailo Developer Zone

- `compute/hailo-developer-zone` | self-hosted, last resort | verdict paid-only | evidence reported | binding none | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://hailo.ai/developer-zone/
- free tier: The Hailo AI Software Suite, the Dataflow Compiler, HailoRT and the Model Zoo are free to a registered developer, and registration is a plain account signup. What is neither free nor rentable is the silicon: a Hailo-8, Hailo-8L, Hailo-10H or Hailo-15 device is a module or card the developer owns. Hailo publishes no hosted device pool, and the third-party free hub that used to execute Hailo models in the cloud, DeGirum AI Hub, ceased operations on 2026-08-01. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-software-only
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: What that form asks for is unknown, because the request-access page returned 403 and the gate could not be read past it. No card, phone or ID document is stated, and no hold exists because nothing is sold to the developer
- interface: unknown
- limits note: no quota binds because no accelerator time is offered: the compiler emits a binary that only a Hailo device can execute.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The compile step chains with any cheap Linux CPU box, because the Dataflow Compiler runs there; the execute step chains with nothing, and the one free cloud executor closed 22 days ago.
- reliability: no reliability event recorded
- notes: Classified as paid-only, not dead, because Hailo sells and supports the product. The finding is that the free part is a compiler whose output cannot be run. No price for the module is recorded: Hailo publishes none on the pages read, so the cost is null rather than a guessed figure. What would change the verdict: a partner cloud renting Hailo silicon by the minute at a published rate, or Hailo restarting a hosted pool.
- self hosted: yes
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: free-software-only
  - facets.shape.gpu_class: Hailo-8 / Hailo-8L / Hailo-10H NPU, purchased module
  - facets.shape.gpu_count: 1
- evidence:
  - [2] 2026-10-22: 
  - [1] 2026-10-22: the Developer Zone is a sign-in and sign-up form gating the AI Software Suite; no hosted device is offered on the page
  - [3] 2026-10-22: the access form returned 403, so the gate could not be read past the form
  - [4] 2026-10-22: the free cloud route that executed Hailo models, DeGirum AI Hub, states it 'will no longer be available publicly' after 2026-09-30
- sources:
  - [1] https://hailo.ai/developer-zone/
  - [2] https://community.hailo.ai/t/dataflow-compiler-license-requirement/18491
  - [3] https://hailo.ai/developer-zone/request-access/
  - [4] https://degirum.com/
