# ScitiX Agent Sandbox

> scitix.github.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/scitix-github-io/ | JSON https://fshy.ajam.dev/api/v1/entity/scitix-github-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ScitiX Agent Sandbox

- `compute/scitix-agent-sandbox` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:18.814Z (live) | stale on 2026-12-05
- url https://scitix.github.io/Agent-Sandbox/
- free tier: free tier published without a credit amount | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: open-source software with no hosted plan, price or transfer allowance on the project site or docs introduction; egress is whatever the cluster's provider charges | metered: no | source: [1]
- identity: email
- interface: rest, cli
- limits:
  - write-gated (binding): no plan and no price: the project is software users run, compatible with the E2B API [1]
- interface detail: HTTP API served by the controller, the `abx` CLI, and E2B-compatible agent SDKs; the user installs the platform with Helm on a Kubernetes cluster and the CLI on a machine
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the project site was read on 2026-10-22. It is an open-source sandbox for evaluation harnesses with no plan or price, which confirms paid-only and explains it: the software runs on the user's cluster
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: environments are created per evaluation run on a user's own infrastructure
  - free_tier_kind: none
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Drop-in compatibility with E2B and popular RL frameworks' and 'designed for coding agents, evaluation harnesses, and RL pipelines needing fast, repeatable environments', with references to SWE-Bench Verified, SWE-Gym and Terminal-Bench, quoted; no plan and no price
  - [2] 2026-11-03: open-source engine with no plan, price or transfer allowance in the docs introduction | capture: sha256:c2e547546d13963740c6833f3495d05eac541a9d1f8b581219ac4b8b3fdbe5ec | quote: Agent Sandbox is an open-source sandbox engine for AI agents.
  - [3] 2026-11-03: an API served by the controller, driven by the abx CLI | capture: sha256:9ee19fd1f28088b13fe147f91144f13df31aa6a4e064b8b93fabb7426ccdb535 | quote: the operator that renders environments and pools, and the API `abx` talks to
- sources:
  - [1] https://scitix.github.io/Agent-Sandbox/
  - [2] https://scitix.github.io/Agent-Sandbox/docs/
  - [3] https://scitix.github.io/Agent-Sandbox/docs/installation/
