# Skyhook

> skyhook.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/skyhook/ | JSON https://fshy.ajam.dev/api/v1/entity/skyhook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Skyhook

- `compute/skyhook` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:35.125Z (live) | stale on 2026-12-05
- url https://skyhook.io
- free tier: a Kubernetes PaaS with preview environments, canary deployments and monitoring, offered without a credit card | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://skyhook.io read 2026-11-04 prints no pricing, egress allowance or overage price | metered: no | source: [1]
- identity: email
- interface: cli, rest
- limits:
  - write-gated (binding): the site states no card is required but publishes no plan, quota or price [1]
- interface detail: a CLI, an API and a UI, stated on https://skyhook.io; the page names no endpoint, binary or SDK
- tooling: https://skyhook.io (read 2026-11-04) names a CLI, an API and a UI and names no client binary, library or SDK
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the no-card position and the product. It publishes no price and no quota, so the free tier's shape cannot be settled from it
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: preview environments are created per change; the page states no clock
  - network_out.out: yes
  - network_out.in: yes
  - network_out.ports: preview environments and canaries
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'We turned Kubernetes into the PaaS you always wanted. No lock-in, no limitations. Everything you need to ship faster - preview environments, canary deployments, monitoring' and 'No credit card required.', quoted
  - [1] 2026-11-04: deploys run from a CLI, an API or a UI | capture: sha256:8b0cc84930681b1a5fdec27b80e5fe4ec36f6177575f7b98dc3d90be701f833a | quote: Deploy from CLI, API, or UI - whatever fits your workflow.
  - [1] 2026-11-04: the platform runs in the user's own clusters; the page prints no egress terms | capture: sha256:8b0cc84930681b1a5fdec27b80e5fe4ec36f6177575f7b98dc3d90be701f833a | quote: Works on AWS, GCP, Azure, OCI, on-prem, or any Kubernetes cluster
  - [1] 2026-11-04: the page names a CLI, an API and a UI and no client by name | capture: sha256:8b0cc84930681b1a5fdec27b80e5fe4ec36f6177575f7b98dc3d90be701f833a | quote: Deploy from CLI, API, or UI - whatever fits your workflow.
- sources:
  - [1] https://skyhook.io
