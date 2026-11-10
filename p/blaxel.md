# Blaxel

> blaxel.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blaxel/ | JSON https://fshy.ajam.dev/api/v1/entity/blaxel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blaxel

- `compute/blaxel` | qualifies-with-caveat | evidence documented | binding retention-clamped | category container and VM sandbox | tier Pay-as-you-go, Tier 0
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:20:45.331Z (live) | stale on 2026-12-05
- url https://blaxel.ai/pricing
- price parsed USD 30.22/mo
- free tier: 'Up to $200 in free credits' on the pay-as-you-go plan, with 'Tier 0 | Free | 10' concurrent sandboxes. The page does not say what 'up to' depends on, and no expiry is stated. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: Credits are topped up to raise the tier; the free grant is bounded by a qualifier the page never explains.
- per-object cap: No per-sandbox vCPU or memory cap is published on the pricing page; the Custom plan advertises 'Up to 256 GB RAM per sandbox or job' as an upgrade over pay-as-you-go. | source: [1] | note: The binding cap is lifetime, not shape.
- retention: Sandboxes sit 'on automatic standby' with memory and filesystem snapshotted; Tier 0 and Tier 1 'enforce expiration dates (Tier 0 and 1, with respectively up to 7 and 30 days)'. In higher tiers unlimited persistence is permitted. | days: 7 | source: [2] | note: Seven days at Tier 0 is the hard ceiling on how long one sandbox can exist.
- egress: Internet egress traffic is listed as Included on https://blaxel.ai/pricing; no byte allowance and no overage price are published. Outbound traffic can be constrained by a per-domain firewall and a proxy, which is a policy control rather than a meter. | metered: no | source: [1]
- identity: email | detail: Signup is 'Start for free' with no card shown on the pricing page; no hold is mentioned. Raising the tier requires a top-up, which introduces a card at that point.
- interface: rest, cli
- limits:
  - volume-quota: 'Up to $200 in free credits', qualifier unexplained [1]
  - retention-clamped (binding): sandbox expiry at Tier 0 is at most 7 days [2]
  - per-ip-shaping: outbound can be restricted to a domain allowlist through the proxy [3]
- limits note: Every sandbox scales to zero after inactivity whether or not an expiry policy is set, so 'running' is not a state Blaxel holds by default.
- binding note: A 7-day maximum existence beats the credit: USD 200 cannot buy a month because no single sandbox is allowed to live that long at Tier 0.
- interface detail: REST API, TypeScript, Python and Go SDKs, a CLI and an MCP server; no SSH endpoint is documented on the platform: SSH into a sandbox is reached by running Tailscale SSH inside it, and 'bl connect sandbox' opens an interactive terminal similar to SSH
- tooling: not stated
- composes with: not established
- reliability: 'Automatic scale-to-zero after 5s inactivity' means a process with no client connection is suspended unless keep-alive is arranged; the docs offer process keep-alive as the workaround.
- notes: Blaxel prices CPU inside the RAM rate: USD 0.0000115 per GB of RAM per second is USD 0.0414 per GB-hour, so a 1 GB sandbox is USD 0.0414 an hour and USD 200 would be 4,831 hours, or a 4 GB sandbox USD 0.1656 an hour and 1,208 hours. Neither number is reachable as a month of uptime because of the 7-day Tier 0 expiry and the 5-second standby. The borrow against it: it is the cheapest per GB-hour of the sandbox providers here, and the right tool for bursty agent work.
- evidence note: The credit, the rates and the tier-0 expiry are first-party. What is not established: whether a keep-alive process suspends the 5-second standby timer in practice, and whether Tier 0 counts the 7-day limit from creation or from last wake.
- extras:
  - keep_rate: 1.0
  - billing_model: per-second on active CPU, keyed to RAM
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - session_cap.wall_clock_min: 10080
  - session_cap.idle_reap_s: 5
  - session_cap.restart_required: no
  - session_cap.note: 7-day maximum sandbox existence at Tier 0; standby after 5 s without a connection
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: exposed TCP ports and preview URLs
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.price: on standby the compute is $0; disk is not priced on this page
  - ps.durability: full memory state is preserved across the suspend
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: the page states no retention limit on a suspended sandbox
  - term: one-time credit
  - m10h_usd: 12.42
  - m24h_usd: 30.22
  - price_arithmetic: 0.0000115 x 3600 = 0.0414 per GB-hour; 1 GB x 730 = 30.22; 200 / 0.0414 = 4831 h theoretical, capped by the 7-day expiry
  - credit_usd: 200
  - credit_hours_at_shape: 168
  - credit_expiry: not stated
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Up to $200 in free credits. Spin up your first sandbox in under a second.' and 'Because Blaxel scales sandboxes to zero the second they're idle and resumes the full memory state in just 25 milliseconds' and '$0 compute costs on standby' and 'Up to 256 GB RAM per sandbox', quoted
  - [1] 2026-10-23: 'Every account starts with free-tier quotas. As you top up credits, your tier automatically increases.', quoted; the page lists no dollar credit
  - [1] 2026-10-24: quoted: 'Up to $200 in free credits', 'Access to all Blaxel products', 'Tier 0 | Free | 10' sandbox limit, and the rate 'Active CPU ... $0.0000115 / GB RAM · second' with '$0 compute costs on standby'.
  - [2] 2026-10-24: quoted: 'Some quota tiers enforce expiration dates (Tier 0 and 1, with respectively up to 7 and 30 days). In higher tiers, unlimited persistence is permitted.'; 'the automatic standby (scale-to-zero) which happens to all sandboxes when inactive'.
  - [4] 2026-10-24: quoted: 'Automatic scale-to-zero after 5s inactivity, resume from standby under 25ms even after weeks.'
  - [5] 2026-10-24: quoted: 'Sandboxes stay active as long as there's an active connection to them'; 'You can also use process keep-alive to keep the sandbox running when you launch a process, even if there isn't an active connection to it.'
  - [1] 2026-11-03: internet egress is listed as included; no byte allowance and no overage price are published | capture: sha256:ff54101630619bc5aa61c89c96b4af0aa9d9931c60c590f8d8132118ceb0d169 | quote: | Internet egress traffic | Outbound traffic from your workloads to the internet. | Included |
  - [6] 2026-11-03: sandboxes are reached by SDK, MCP server or REST API | capture: sha256:a447da4aafe812818234b41124636f8d14cdb4ab9ae21baa6fc3f306d67eb2dd | quote: using a simple file system interface from the SDK, MCP server, or REST API
  - [7] 2026-11-04: SSH access to a sandbox is documented through Tailscale run inside the sandbox | capture: sha256:96ec6b3793a54ba300ebc7b3e067e9a351b4d79aeaf58033876969ea3586a7c8 | quote: Once authenticated, the sandbox is reachable via SSH from any device on your Tailscale network:
  - [8] 2026-11-04: the CLI offers an interactive terminal described as similar to SSH | capture: sha256:b83612a281a30ff0d5fdd4183214525505b93ee2e01c84c8e95eaa1a72251262 | quote: This command opens a direct terminal connection to your sandbox, similar to SSH.
  - [6] 2026-11-04: TypeScript, Python and Go SDKs exist | capture: sha256:a447da4aafe812818234b41124636f8d14cdb4ab9ae21baa6fc3f306d67eb2dd | quote: Use the Blaxel SDKs for TypeScript, Python, and Go to programmatically manage sandboxes, agents, MCP servers, jobs, and other resources.
- sources:
  - [1] https://blaxel.ai/pricing
  - [2] https://docs.blaxel.ai/Sandboxes/Expiration.md
  - [3] https://docs.blaxel.ai/Sandboxes/Proxy-domains.md
  - [4] https://docs.blaxel.ai/
  - [5] https://docs.blaxel.ai/Sandboxes/Standby-control.md
  - [6] https://docs.blaxel.ai/llms.txt
  - [7] https://docs.blaxel.ai/Tutorials/Tailscale.md
  - [8] https://docs.blaxel.ai/cli-reference/commands/bl_connect_sandbox.md
