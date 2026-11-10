# Containarium

> containarium.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/containarium/ | JSON https://fshy.ajam.dev/api/v1/entity/containarium.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Containarium

- `compute/containarium` | paid-only | evidence documented | binding per-ip-shaping | category cloud VM
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://containarium.dev/pricing
- free tier: One price of USD 20 per seat per month for 2 vCPU (1 guaranteed, the second when the host has spare capacity), 4 GiB RAM, a 20 GB disk, 100 GB of egress and a public IPv4, with no per-second meter and no overage. Each seat is one box with SSH, an MCP server inside the box and a dashboard. Idle boxes sleep, which is how the flat price is possible. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Containarium seat | 2 vCPU (1 guaranteed) 4 GiB | included | included | included | included | $20.00 / mo', with 20 GB disk, 100 GB egress and a public IPv4 included and no overage | metered: no | source: [1]
- identity: card
- interface: ssh
- limits:
  - per-ip-shaping (binding): The 100 GB monthly egress and the single guaranteed vCPU are the terms that bind: the second vCPU is best-effort on host spare capacity, and the box sleeps when idle so a background job that needs a warm box has to keep it awake. [1]
- limits note: The 100 GB monthly egress and the single guaranteed vCPU are the terms that bind: the second vCPU is best-effort on host spare capacity, and the box sleeps when idle so a background job that needs a warm box has to keep it awake.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A box that keeps its filesystem and runs an MCP server is the piece a stateless sandbox lacks: an agent reconnects over SSH or HTTPS by hostname and finds its tools and caches still installed, so the setup cost is paid once a month rather than once a run.
- reliability: no reliability event recorded
- notes: The core is Apache 2.0 and self-hostable, which is not a price but does mean the same box can run on any rented VM. At USD 20 for 1 guaranteed vCPU and 4 GiB this is the cheapest flat-rate agent box found after RemoteHost's per-hour arithmetic.
- extras:
  - facets.class: flat-seat-box
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 4
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: 'Containarium seat | 2 vCPU (1 guaranteed) · 4 GiB | included | included | included | included | $20.00 / mo', with 20 GB disk, 100 GB egress and a public IPv4 included and no overage
  - [1] 2026-10-22: the vendor's own comparison at 730 hours per month: AWS t3.medium totals USD 35.62, Google Cloud e2-medium USD 41.15, Azure B2s USD 36.42, list prices read 2026-10-18
  - [2] 2026-10-22: one LXC container per agent with real root, a built-in MCP server over stdio, a routable hostname with TLS, and state that survives between runs until the box is deleted
  - [1] 2026-10-22: 'the box sleeps when idle' and the seat is a share of an instance rather than a dedicated machine
- sources:
  - [1] https://containarium.dev/pricing
  - [2] https://containarium.dev/sandbox-for-ai-agents
