# Limrun

> lim.run | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/lim/ | JSON https://fshy.ajam.dev/api/v1/entity/lim.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Limrun

- `compute/limrun` | trial-only | evidence documented | binding volume-quota | category macOS host
- needs card no, phone no, ID no, institution no | verified 2026-11-24T13:20:55.904Z (live) | stale on 2026-12-25
- url https://lim.run
- free tier: Free trial with 120 one-time credits at USD 0.00 per month; overage USD 0.06 per credit; Xcode warm state 0.4 credits per minute. | unit: credits | metered on: wall-clock | read on: 2026-11-24 | source: [1] | note: The Trial grant is one-time and does not renew; overage is optional and requires a payment method.
- per-object cap: not stated | source: [2]
- retention: Disk snapshots restore build state across instances; no retention clock is published. | source: [2]
- egress: No egress volume allowance, price or network policy is published on the pages read. | metered: no | source: [2]
- identity: email | detail: Registration asks for an email address and name and a third-party sign-in provider, enterprise single sign-on or a passwordless email code.
- interface: rest, cli
- limits:
  - volume-quota (binding): 120 one-time Trial credits, then USD 0.06 per credit overage [1]
  - request-rate: Xcode active uses 2 credits per minute; Xcode warm uses 0.4 credits per minute [1]
  - volume-quota (binding): unlimited concurrency on every plan, subject to abuse-prevention quotas [1]
- limits note: Xcode active uses 2 credits per minute and warm 0.4 credits per minute; concurrency is unlimited on every plan; session and egress clocks are not published.
- interface detail: MCP server at https://mcp.limrun.com/mcp, REST API at https://api.limrun.com, and the lim CLI (npm install -g lim).
- tooling: the same as interface detail
- composes with: not established
- reliability: no reliability event recorded
- notes: A free trial with 120 one-time credits is the only grant; paid plans start at USD 20 per month.
- evidence note: Plans, credits, rates, identity and the interface are on first-party pages read 2026-11-24; egress volume terms are not published.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: pricing is explicitly split between idle and active, so an idle machine has its own rate
  - free_tier_kind: none
  - reclassified_from: dead
  - ps.price: an S3-backed cache keeps warm builds
  - ps.durability: S3-backed cache
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the cache is kept
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: 'keep warm builds with an S3-backed cache. Pricing is split between idle and' ... with an MCP server card and 'Sign up or log in' at console.limrun.com; the extracted body does not carry the price table
  - [1] 2026-11-24: the Trial plan gives 120 one-time credits at no monthly fee with a per-credit overage rate | capture: sha256:b51cd7cde0be4ced4d67f1ed7c53c86424c2aeb047ef5d5e09eb074065d1d127 | quote: Trial | $0.00/month | $0.00/year ($0.00/month equivalent) | 120 one-time | $0.06 | Try Limrun with your first builds and tests. |
  - [1] 2026-11-24: the Xcode warm rate in credits and dollar equivalents per plan | capture: sha256:b51cd7cde0be4ced4d67f1ed7c53c86424c2aeb047ef5d5e09eb074065d1d127 | quote: Xcode | warm | 0.4 | $0.024 | $0.016 | $0.0128 | $0.02 |
  - [1] 2026-11-24: the trial grant is one-time and overage does not renew it | capture: sha256:b51cd7cde0be4ced4d67f1ed7c53c86424c2aeb047ef5d5e09eb074065d1d127 | quote: Enabling overage does not renew the one-time signup grant.
  - [1] 2026-11-24: trial credits are free and the listed dollar rates apply only to overage | capture: sha256:b51cd7cde0be4ced4d67f1ed7c53c86424c2aeb047ef5d5e09eb074065d1d127 | quote: Trial credits are free; Trial dollar prices below apply only to overage.
  - [2] 2026-11-24: the homepage says builds use an S3-backed cache and pricing separates idle and build time | capture: sha256:3c9fe88f6af0ff4eddae819c0b8d2d748153633f9ce8527d892f80b0c41f4bc4 | quote: keep warm builds with an S3-backed cache. Pricing is split between idle and
  - [3] 2026-11-24: registration asks for an email address and name and a supported sign-in method | capture: sha256:86f4c6f60fb6d3c82f9ec8d9ecd2d16166d22484e0991882be628c174da8b825 | quote: As part of registration, you will be asked to provide certain information, such as your email address and name, and to authenticate through a supported third-party sign-in provider, enterprise single sign-on, or a passwordless email code.
  - [4] 2026-11-24: the MCP server is a Streamable HTTP OAuth endpoint | capture: sha256:e7bb337fbec26fd04e86bd97a3d38337c3f2fc6aca45f1eafde39e6214645c5a | quote: MCP server (Streamable HTTP, OAuth): https://mcp.limrun.com/mcp
  - [1] 2026-11-24: disk snapshots are retained across instances | capture: sha256:b51cd7cde0be4ced4d67f1ed7c53c86424c2aeb047ef5d5e09eb074065d1d127 | quote: Restore build state across instances to avoid starting from scratch.
- sources:
  - [1] https://limrun.com/pricing.md
  - [2] https://lim.run
  - [3] https://limrun.com/terms
  - [4] https://limrun.com/llms.txt
