# Orgo

> orgo.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/orgo/ | JSON https://fshy.ajam.dev/api/v1/entity/orgo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Orgo

- `compute/orgo` | qualifies-with-caveat | evidence reported | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:14.184Z (live) | stale on 2026-11-19
- url https://www.orgo.ai/pricing
- free tier: free tier published without a credit amount | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published as a volume allowance or price: only a bandwidth rate limit, up to 100 Mbps on a Free account's hourly computer and up to 1,000 Mbps on a paid plan | metered: no | source: [1]
- identity: email
- interface: rest, cli, ssh
- limits:
  - write-gated (binding): access is an API, SDK or MCP server; no plan or price appears on the extracted page [1]
- interface detail: HTTP API with Python and TypeScript SDKs, CLI (orgo), MCP server, and key-based SSH on paid plans (Linux only)
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and describes the product and its snapshot and clone verbs but publishes no plan or price in the extracted body, so the free-tier claim still rests on documented records card
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a running computer can be shared, cloned or snapshotted; the page states no clock
  - persistent_storage.price: not stated
  - persistent_storage.durability: snapshot of a running computer
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: the snapshot
  - free_tier_kind: allowance
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Orgo provides cloud computers (virtual desktops) for AI agents. Provision a Linux desktop in seconds, drive it over the API/SDK or the hosted MCP server, and share, clone, or snapshot running computers.' quoted; the extracted body carries no plan and no price
  - [2] 2026-11-03: only a bandwidth rate is published for network, no volume allowance or price | capture: sha256:c9f1f936b7081e08c785b356f7be0888f7b9402ab6af7b82a7abe9fd25209bf8 | quote: A Free account's hourly computer runs at up to 100 Mbps.
  - [3] 2026-11-03: a REST HTTP API exists | capture: sha256:c34c764e50182aa017ad705666931988115f7c73b075592243d7356018d8c217 | quote: [API](https://docs.orgo.ai/api-reference/introduction.md). A plain HTTP API.
  - [4] 2026-11-03: SSH access exists, paid plans | capture: sha256:4ded39c609713c02f441d1a846e69a7834ec8c2584be2ad813682e7559ce908f | quote: Direct SSH (key access) - real key-based `sshd` access to Linux computers via your own keypair
- sources:
  - [1] https://www.orgo.ai/pricing
  - [2] https://docs.orgo.ai/guides/account-limits.md
  - [3] https://docs.orgo.ai/
  - [4] https://www.orgo.ai/pricing.md
