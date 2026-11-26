# Replicas

> replicas.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/replicas/ | JSON https://fshy.ajam.dev/api/v1/entity/replicas.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Replicas

- `compute/replicas` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-24T13:21:02.388Z (live) | stale on 2026-12-25
- url https://replicas.dev
- free tier: $100 of free usage with no card required | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Workspaces normally egress from changing sandbox addresses; the Team plan adds a static egress IP. Traffic through a dedicated static IP is billed at USD 0.15 per GB and counts toward included usage. | metered: yes | price per TB: USD 150 | source: [1]
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
  - session_cap.note: no session clock published; workspaces sleep when idle with no published interval
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
  - [1] 2026-11-18:  | capture: sha256:554c5d1bdb7d3f3a18d7c48d5c3e2fc50b627fb049a7cbca8a9a8f472e92c917 | quote: Run Claude Code, Codex and other coding agents in the cloud, and get pull requests back.
  - [5] 2026-11-24: egress over a dedicated static IP is metered at USD 0.15 per GB | capture: sha256:1bf36dd2d35806926a09eecdc2d9a60218477729cfe74343e684f7b55105914a | quote: Traffic through a [dedicated static IP](https://docs.replicas.dev/features/static-egress-ip.md#dedicated-ip) is billed at \$0.15 / GB and counts toward included usage.
  - [5] 2026-11-24: egress is metered and priced on the dedicated static-IP path | capture: sha256:1bf36dd2d35806926a09eecdc2d9a60218477729cfe74343e684f7b55105914a | quote: Traffic through a [dedicated static IP](https://docs.replicas.dev/features/static-egress-ip.md#dedicated-ip) is billed at \$0.15 / GB and counts toward included usage.
  - [5] 2026-11-24: the dedicated-IP egress rate is USD 0.15 per GB | capture: sha256:1bf36dd2d35806926a09eecdc2d9a60218477729cfe74343e684f7b55105914a | quote: Traffic through a [dedicated static IP](https://docs.replicas.dev/features/static-egress-ip.md#dedicated-ip) is billed at \$0.15 / GB and counts toward included usage.
  - [1] 2026-11-24: the one-time free usage grant and no-card condition are unchanged | capture: sha256:554c5d1bdb7d3f3a18d7c48d5c3e2fc50b627fb049a7cbca8a9a8f472e92c917 | quote: $100 of free usage, no card required.
  - [4] 2026-11-24: the small workspace is 2 vCPU and 8 GB memory at USD 0.004 a minute within the allowance and USD 0.006 after | capture: sha256:d438dfcf3976ee799b294176e58ee3de3e4a2231091e4fc82d55d262cfc496dd | quote: 2 vCPU, 8 GB memory · $0.004/min included, $0.006/min after
  - [6] 2026-11-24: ordinary workspace egress comes from changing addresses; a static IP is an optional paid feature | capture: sha256:4d62d9199a604acf40ffcdd67e1be815884fb47ef515526c6cf4b0f01573a8b8 | quote: Workspaces normally reach the Internet from changing sandbox addresses.
- sources:
  - [1] https://replicas.dev
  - [2] https://docs.replicas.dev/features/cli.md
  - [3] https://docs.replicas.dev/features/api.md
  - [4] https://replicas.dev/pricing
  - [5] https://docs.replicas.dev/admin/billing
  - [6] https://docs.replicas.dev/features/static-egress-ip.md
