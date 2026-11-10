# Mosaic Sandbox

> mosaicos.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mosaicos/ | JSON https://fshy.ajam.dev/api/v1/entity/mosaicos.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mosaic Sandbox

- `compute/mosaic` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:29.000Z (live) | stale on 2026-11-22
- url https://sandbox.mosaicos.com/
- free tier: no free tier: $0.05 an hour of active compute with RAM and storage included, and $0 while hibernated | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.05 an hour of active compute, with RAM and storage included in that rate [1]
  - retention-clamped: a hibernated sandbox costs $0, so stopping is a pause rather than a loss [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the flat hourly rate and the hibernation rule. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: first-party: ses Pricing Benchmarks Roadmap Security Get Key No walled gardens A real Linux sandbox for any agent. Start in
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: hibernation costs nothing and the page states no automatic reap; SSH is available when enabled at creation
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: included in the $0.05 hourly rate
  - ps.durability: sandbox disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.ports: SSH when enabled at creation, with a reachable endpoint issued
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '$0.05/hour active compute · Includes RAM and storage. $0 while hibernated' and 'Each sandbox runs on Firecracker/KVM. Agents can connect through the REST API, the mos CLI, Python, TypeScript, and Go SDKs, MCP, or native SSH.' quoted
- sources:
  - [1] https://sandbox.mosaicos.com/
