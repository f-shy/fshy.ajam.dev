# Runtime

> withruntime.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/withruntime/ | JSON https://fshy.ajam.dev/api/v1/entity/withruntime.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Runtime (withruntime.com)

- `compute/withruntime` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category container and VM sandbox | tier 1 GiB machine at the idle CPU floor
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:24:09.969Z (live) | stale on 2026-12-05
- url https://withruntime.com/pricing
- price parsed USD 6.39/mo
- free tier: 100 free hours of a 1 GB machine in the first 30 days, with no card. | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: hours, not credit
- per-object cap: free tier caps a sandbox at 2 vCPU / 4 GiB / 10 GiB disk; a paid account goes to 16 vCPU / 64 GiB / 400 GiB
- retention: A paused sandbox keeps files and memory at USD 0.08 per decimal GB per 30-day month; a snapshot or a custom image costs the same. | source: [1]
- egress: 100 GiB a month of outbound traffic is free, then USD 0.02/GB; inbound traffic is free. | metered: yes | free allowance: 100 GiB | source: [1]
- identity: email | detail: 100 free hours with no card; a paid account needs a payment method whose type and hold were not stated on the pricing page. Unverified for the paid path.
- interface: rest, cli, ssh
- limits:
  - volume-quota: outbound traffic 100 GiB a month free, then USD 0.02/GB [1]
  - per-ip-shaping (binding): a dedicated IPv4 address is USD 5 per 30-day month and a WireGuard tunnel is USD 5 per 30-day month, so there is no free public port [1]
- binding note: The first thing that fails for this use is ingress: a public address is a USD 5/month add-on, which alone equals the whole budget.
- interface detail: HTTP API at api.withruntime.com, JavaScript, Python, Go, Ruby and Java clients, the runtime CLI (npm package withruntime), an MCP server, and SSH to a sandbox
- tooling: not stated
- composes with: not established
- reliability: Compute has no one-minute minimum and memory bills only while compute runs; waiting is charged at a 50-millicore CPU floor.
- notes: The arithmetic at 24/7 for 1 GiB sitting idle: 0.05 vCPU x 0.025 + 1 GiB x 0.0075 = USD 0.00875/hour x 730 = USD 6.39. Busy at 1 vCPU: 0.025 + 0.0075 = USD 0.0325/hour x 730 = USD 23.73. Either way over USD 5, and the free tier is 100 hours, not a month. Egress: USD 0.02/GB x 1000 = USD 20 per TB beyond the 100 GiB allowance. Note the vendor's own framing (42% to 88% cheaper) is measured against agents that wait on a model, not against an always-on box, which is why the 730-hour figure is the one that decides.
- evidence note: Both usage rates, the idle floor, the free allowance, the add-on prices and the paused-sandbox rate are quoted from the pricing page read. What would raise it: the exact bill for a machine kept running with no work, which the vendor models but does not publish.
- extras:
  - keep_rate: 1.0
  - billing_model: per-second
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.note: 1 GiB with the 50-millicore default CPU floor while waiting
  - session_cap.restart_required: no
  - session_cap.note: no wall-clock cap published; a paused sandbox bills storage only
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: no public address by default; a dedicated IPv4 is USD 5/month and a managed WireGuard tunnel (16 peers) is USD 5/month
  - network_out.static_ip: no
  - free_tier_kind: hours
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - net.out: yes
  - net.in: yes
  - net.allowance: 100 GiB a month free, then $0.02 a GB
  - term: usage, no commitment
  - m10h_usd: 2.63
  - m24h_usd: 6.39
  - price_arithmetic: Idle 1 GiB: (0.05 x 0.025 + 1 x 0.0075) = USD 0.00875/hour x 730 = USD 6.39; x 300 = USD 2.63. Busy at 1 vCPU: (0.025 + 0.0075) x 730 = USD 23.73. Add USD 5/month for a dedicated IPv4 or a WireGuard tunnel.
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free usage: 100 free hours of a 1 GB machine in your first 30 days, no card' with '$0.025 per active vCPU-hour', '$0.0075 per reserved GiB-hour', 'Outbound traffic: 100 GiB a month free, then $0.02 per GB', 'Compute has no one-minute minimum, and memory is billed while compute runs', and the measured comparison '1,000 one-minute runs of 2 vCPU, 4 GiB: Runtime $0.64 against Fly Machines $1.53', quoted
  - [1] 2026-10-24: quoted: 'Active CPU | $0.025 per active vCPU-hour'; 'Memory | $0.0075 per reserved GiB-hour'; '100 free hours of a 1 GB machine in your first 30 days, no card'
  - [1] 2026-10-24: quoted: 'Waiting means memory plus the default CPU floor of 50 millicores, a twentieth of a vCPU.'
  - [1] 2026-10-24: quoted: 'Dedicated IPv4 address | $5 per 30-day month'; 'WireGuard tunnel, up to 16 peers | $5 per 30-day month'
  - [1] 2026-11-03: the first 100 GiB out a month is free per account | capture: sha256:199df88f30189af6c4c0060d99c86039d0a6b8df1daf260b28ab4e5812e9b506 | quote: | Outbound traffic, first 100 GiB a month per account | Free |
  - [1] 2026-11-03: outbound traffic past 100 GiB a month costs USD 0.02 per decimal GB | capture: sha256:199df88f30189af6c4c0060d99c86039d0a6b8df1daf260b28ab4e5812e9b506 | quote: | Outbound traffic past that | $0.02 per decimal GB |
  - [2] 2026-11-03: an HTTP API exists | capture: sha256:83d9b647cfa7acb60e1a54f962c1cfe0db3d28854e0c05740a80a644d17d6e4a | quote: One API for every Runtime Cloud product, at https://api.withruntime.com.
  - [3] 2026-11-03: a CLI exists | capture: sha256:b021ceb59c82216e9dbafb8d170b148810b7c9da66ce5a51b6917a28872c7427 | quote: The CLI runs every Runtime Cloud product from a terminal or a script.
  - [2] 2026-11-03: SSH login to a sandbox exists | capture: sha256:83d9b647cfa7acb60e1a54f962c1cfe0db3d28854e0c05740a80a644d17d6e4a | quote: Log in to a sandbox over SSH, open it in VS Code or a JetBrains IDE
- sources:
  - [1] https://withruntime.com/pricing
  - [2] https://withruntime.com/docs
  - [3] https://withruntime.com/docs/cli
