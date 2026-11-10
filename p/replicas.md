# Replicas

> replicas.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/replicas/ | JSON https://fshy.ajam.dev/api/v1/entity/replicas.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Replicas

- `compute/replicas` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:07.844Z (live) | stale on 2026-12-05
- url https://replicas.dev
- free tier: $100 of free usage with no card required | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Team plan adds access to a static egress IP; no egress data allowance or overage price is published on the pricing page. | metered: no | source: [1]
- identity: email | detail: '$100 of free usage, no card required.', quoted from replicas.dev read 2026-10-22
- interface: rest, cli
- limits:
  - request-rate (binding): $100 of free usage, one time [1]
- interface detail: REST API at https://api.replicas.dev with a bearer API key, and the replicas CLI
- tooling: the replicas CLI (npm package replicas-cli) and the REST API
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the $100 grant and the no-card condition, which corrects the record's USD 120
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a run is provisioned on a schedule, a webhook or an API call; the page states no session clock
  - free_tier_kind: one-time-credit
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$100 of free usage, no card required.' and 'Get started for free' with 'Every minute is attributable', quoted
  - [2] 2026-11-03: a CLI exists | capture: sha256:193f8907b037a900978e18c9d2b7935687cfd2c8d748dc7daddf8b99a195832c | quote: Control workspaces, chats, environments, and automations from your terminal.
  - [3] 2026-11-03: an API exists | capture: sha256:7e21470975567b23900e4f5428fa9de7d2db4526db5bb283d2497902ac404d23 | quote: The Replicas API covers what you can do in the app
  - [4] 2026-11-03: static egress IP is a Team-plan feature; no data allowance or price | capture: sha256:9287329ba639722f1765a0c62169afa321062dac70deda907ded3d89a7b8b77a | quote: Access to a static egress IP
  - [3] 2026-11-04: the REST API is at api.replicas.dev with a bearer API key | capture: sha256:7e21470975567b23900e4f5428fa9de7d2db4526db5bb283d2497902ac404d23 | quote: Send an API key as a bearer token to `https://api.replicas.dev`:
  - [2] 2026-11-04: the CLI is the replicas-cli npm package | capture: sha256:193f8907b037a900978e18c9d2b7935687cfd2c8d748dc7daddf8b99a195832c | quote: npm install -g replicas-cli
- sources:
  - [1] https://replicas.dev
  - [2] https://docs.replicas.dev/features/cli.md
  - [3] https://docs.replicas.dev/features/api.md
  - [4] https://replicas.dev/pricing
