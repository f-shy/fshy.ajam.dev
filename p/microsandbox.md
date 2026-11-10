# microsandbox

> microsandbox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/microsandbox/ | JSON https://fshy.ajam.dev/api/v1/entity/microsandbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## microsandbox

- `compute/microsandbox` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:14.177Z (live) | stale on 2026-12-05
- url https://microsandbox.dev/pricing
- free tier: a monthly pool of 5 vCPU-hours, 20 GiB-hours of memory and 20 GiB-hours of disk with a 1 GiB durable-storage cap, and a hard cap of 3 sandboxes at 1 vCPU, 512 MiB and 8 GiB of disk with no overage | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: the pricing page meters vCPU, memory, disk and durable storage and states no egress allowance or price; public internet access is on by default and can be cut to an allowlist or disabled | metered: no | source: [1]
- identity: email
- interface: cli
- limits:
  - request-rate (binding): 5 vCPU-hours a month on the free pool, hard-capped with no overage [1]
  - per-object-cap: 1 GiB of durable storage and 3 sandboxes at 1 vCPU, 512 MiB and 8 GiB of disk [1]
- interface detail: CLI (msb), and SDKs for Rust, TypeScript, Python and Go; with an API key the same SDK runs on microsandbox cloud; an MCP server exists
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free pool in computer-hours with a hard cap and no overage. The pool is what makes the duty cycle computable: 5 vCPU-hours a month is about 10 minutes a day
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 0.5
  - shape.disk: 8
  - shape.note: the free shape: 1 vCPU, 512 MiB and 8 GiB of disk, three at a time
  - session_cap.restart_required: no
  - session_cap.note: billed for the time a sandbox actually runs; the monthly pool is the bound and the page states no reap
  - free_tier_kind: allowance
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - ps.gib: 1
  - ps.price: a 1 GiB durable-storage cap on the free pool
  - ps.durability: durable storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the plan's cap
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'every sandbox is a small computer, billed for the time it actually runs. plans bundle a monthly pool of compute' with a free pool of '5 vcpu-hours, 20 memory gib-hours, 20 disk gib-hours, 1 gib durable storage cap' described as 'hard cap. no overage. 3 sandboxes, each 1 vcpu, 512 mib, 8 gib disk', quoted
  - [2] 2026-11-03: egress is open by default and no allowance or price is stated | capture: sha256:c46b6546d63b06dc3f49db6afa523c85e128840023941a35cd0257caae1550e6 | quote: by default, sandboxes can reach the public internet.
  - [3] 2026-11-03: the cloud is reached through the SDK with an API key | capture: sha256:0eada3da3086a8277a215a45b2e6ec1dc36967da0d609b36ec2fee683b70a903 | quote: With an API key set, the same SDK runs sandboxes on [microsandbox cloud](https://docs.microsandbox.dev/cloud/overview.md) instead.
- sources:
  - [1] https://microsandbox.dev/pricing
  - [2] https://microsandbox.dev
  - [3] https://docs.microsandbox.dev/sdk/overview
