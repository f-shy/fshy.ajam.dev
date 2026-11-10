# Maritime

> maritime.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/maritime/ | JSON https://fshy.ajam.dev/api/v1/entity/maritime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Maritime

- `compute/maritime` | qualifies-with-caveat | evidence documented | binding write-gated | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:07.843Z (live) | stale on 2026-12-05
- url https://maritime.sh/pricing
- free tier: Free at $0/mo, no card needed; the first paid tier is $20/mo | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: No egress allowance or overage price is published on the pricing page; usage is machine time and disk only. | metered: no | source: [1]
- identity: email | detail: 'Try it out, no card needed' on the pricing page, read 2026-10-22
- interface: rest, cli
- limits:
  - write-gated (binding): the free tier is a plan tier, not a metered allowance; capacity above it needs a paid plan from $20/mo [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: REST API and CLI, per maritime.sh/llms.txt: "one REST API" and "the maritime CLI"
- tooling: the provider documents TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime) and the maritime CLI (npm maritime-cli), per maritime.sh/llms.txt
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and lists the Free tier and three paid tiers. The page publishes no hour or credit allowance for Free, so the free tier is recorded as a plan with no metered allowance rather than a quota
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free · $0/mo · Try it out, no card needed.' with paid tiers at $20/mo, $100/mo and $500/mo, quoted
  - [2] 2026-11-03: REST API and CLI exist | capture: sha256:15ede80b02234716172021235d9ed4ee95eb00eb7c66d30ad73a5255ea226df1 | quote: Interfaces: one REST API (bearer mk_ key), TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime), the maritime CLI (npm maritime-cli), an MCP server for desktops and phones, and the dashboard.
  - [1] 2026-11-03: plan credit covers machine time and disk; no egress line | capture: sha256:4db5ed2e401eba55e14432fc58656cff99fa43cb4fc2cc98540857e0fe5ce135 | quote: The credit covers machine time and disk.
  - [2] 2026-11-04: the provider lists a REST API and the maritime CLI | capture: sha256:c6c087926fcf03c7e2def30d3be4513f5353ea46d5b12f52e238a68794ca49ab | quote: Interfaces: one REST API (bearer mk_ key), TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime), the maritime CLI (npm maritime-cli), an MCP server (https://mcp.maritime.sh/mcp) for desktops, phones, sandboxes, swarms and agents, and the dashboard.
  - [2] 2026-11-04: the provider lists its SDKs and CLI | capture: sha256:c6c087926fcf03c7e2def30d3be4513f5353ea46d5b12f52e238a68794ca49ab | quote: Interfaces: one REST API (bearer mk_ key), TypeScript SDK (npm maritime-sdk), Python SDK (pip maritime), the maritime CLI (npm maritime-cli), an MCP server (https://mcp.maritime.sh/mcp) for desktops, phones, sandboxes, swarms and agents, and the dashboard.
- sources:
  - [1] https://maritime.sh/pricing
  - [2] https://maritime.sh/llms.txt
