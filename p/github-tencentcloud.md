# Tencent Cloud CubeSandbox

> github.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-tencentcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/github-tencentcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tencent Cloud CubeSandbox

- `compute/tencent-cubesandbox` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:09.894Z (live) | stale on 2026-11-22
- url https://github.com/TencentCloud/CubeSandbox
- free tier: no hosted tier: the project is self-hosted software for x86_64 Linux with KVM, so there is no capacity to buy; it ships a compatible API gateway and an egress filter | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): self-hosted software: users must supply x86_64 Linux with KVM, so there is no hosted capacity [1]
  - per-ip-shaping: CubeEgress filters egress by L7 domain and audits it, with kernel policies so traffic cannot skip inspection [1]
  - request-rate: cold start is 60 ms at single concurrency and the P99 is 137 ms under 50 concurrent creations [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the repository was read on 2026-10-22 and states the KVM requirement, the benchmarked cold start and the egress gateway. There is no hosted product, so the verdict stays paid-only with a better reason: it is software users run
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a sandbox starts in 60 ms and pause/resume is supported across nodes; a user's own host sets the clocks
  - free_tier_kind: none
  - reclassified_from: dead
  - ps.price: a user's own host and S3
  - ps.durability: snapshots to S3, resumable across nodes
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.max_retention: as long as a user keeps the snapshot
  - net.out: yes
  - net.in: no
  - net.ports: egress through CubeEgress with L7 domain filtering
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Cube Sandbox requires an x86_64 Linux environment with KVM support' and 'Cold start benchmarked on bare-metal. 60ms at single concurrency; under 50 concurrent creations, avg 67ms, P95 90ms, P99 137ms' with 'CubeEgress - OpenResty-based egress security gateway: L7 domain filtering, credential injection, and access auditing', quoted
- sources:
  - [1] https://github.com/TencentCloud/CubeSandbox
