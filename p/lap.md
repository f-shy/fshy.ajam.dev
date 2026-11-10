# Lapdev

> lap.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lap/ | JSON https://fshy.ajam.dev/api/v1/entity/lap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Lapdev

- `compute/lapdev` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:16.614Z (live) | stale on 2026-12-05
- url https://lap.dev/pricing/
- free tier: free during public beta, with unlimited developers and catalogs, installed into the user's own Kubernetes clusters. | unit: unlimited | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: no egress allowance or overage price on https://lap.dev/pricing/ and https://docs.lap.dev | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - retention-clamped: free only during public beta; the page says so as a state rather than a term [1]
  - write-gated (binding): the user installs lapdev-kube-manager into their own cluster, so there is no hosted compute. [1]
- interface detail: lapdev CLI (Devbox) and the dashboard at app.lap.dev; no REST API or SSH documented on the pages read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states that the product is free during beta and runs in the user's own clusters. The free half is the software, and the end of beta is the clock.
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: environments are namespaces in a user's cluster; a user's cluster sets the clocks
  - free_tier_kind: allowance
  - ps.price: a user's own cluster storage
  - ps.durability: a user's own volumes
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: as long as a user keeps it
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Lapdev is currently in public beta and free to use. Install lapdev-kube-manager in your own clusters and keep using the manifests you already ship.' and 'Unlimited developers · Unlimited catalogs', quoted
  - [1] 2026-11-03: the pricing page prints no egress allowance or overage price; network cost is the user's own cluster cost | capture: sha256:e5c8355a97d252c23f4624afc70972d230991033fce58f6cf6198ca8607c9c60 | quote: No platform subscription fees during beta. Pay only your own Kubernetes infrastructure costs.
  - [2] 2026-11-03: a CLI (lapdev) is documented; the dashboard is at app.lap.dev | capture: sha256:f2b746f18a5cde7728ae2e23f6810cadc61944f424e78fea4cc30eaa85d613a2 | quote: Devbox is built into the `lapdev` command
- sources:
  - [1] https://lap.dev/pricing/
  - [2] https://docs.lap.dev/how-to-guides/local-development-with-devbox.md
