# microsandbox

> microsandbox.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/microsandbox/ | JSON https://fshy.ajam.dev/api/v1/entity/microsandbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## microsandbox

- `compute/microsandbox` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-24T13:20:56.539Z (live) | stale on 2026-12-25
- url https://microsandbox.dev/pricing
- free tier: free trial: USD 10 one-time credit, 1 sandbox at a time, up to 2 vCPU and 1 GiB RAM, up to 32 GiB root disk, 100 services per org and 20 per sandbox; ephemeral with 1-hour sessions. Cloud access is by request (private beta) at USD 0 per trial. Builder is USD 20 a month with USD 20 of usage included | unit: credits | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: no egress allowance or price is published on the pricing page; the docs describe outbound network rules that can be restricted to allowed hosts. Persistent volumes are USD 0.15 per GiB-month and snapshots USD 0.08 per GiB-month | metered: no | source: [1]
- identity: email | detail: a name, an email and a password are required at signup; no card or phone number appears on the signup page. Cloud access is by request through a waitlist that asks for an email
- interface: cli, rest
- limits:
  - request-rate (binding): USD 10 one-time trial credit; 1 sandbox at a time, up to 2 vCPU and 1 GiB RAM; ephemeral 1-hour sessions [1]
  - per-object-cap: up to 32 GiB root disk per sandbox; 100 services per org and 20 per sandbox; 1 sandbox at a time on the free trial [1]
- interface detail: CLI (msb), SDKs for Rust, TypeScript, Python, Go and Ruby, and REST endpoints over HTTPS at api.microsandbox.dev with an MSB_API_KEY bearer token; an MCP server card is published
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
  - session_cap.note: no sandbox session clock; a separate SSH inactivity timeout defaults to 10 minutes and is independent of sandbox idle
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
  - [2] 2026-11-03: egress is open by default and no allowance or price is stated | capture: sha256:c46b6546d63b06dc3f49db6afa523c85e128840023941a35cd0257caae1550e6 | quote: by default, sandboxes can reach the public internet.
  - [3] 2026-11-18:  | capture: sha256:46ac6305bdc5728cc0454fe271c4d96487a7ec950c7d7c458215ce165d18803c | quote: SSH inactivity timeout keeps its 10-minute default, but you can now change it.
  - [1] 2026-11-24: the free offer is a USD 10 one-time trial credit, not a monthly compute pool | capture: sha256:108c642d87a113db477bdd3b5abda755b8fd0e55faf91500f89db6b224614236 | quote: free trial | $0/trial | $10 one-time credit
  - [1] 2026-11-24: the free allowance is denominated in USD credit, not compute hours | capture: sha256:108c642d87a113db477bdd3b5abda755b8fd0e55faf91500f89db6b224614236 | quote: $10 one-time credit
  - [1] 2026-11-24: the free allowance is a one-time credit with no stated metering basis | capture: sha256:108c642d87a113db477bdd3b5abda755b8fd0e55faf91500f89db6b224614236 | quote: free trial | $0/trial | $10 one-time credit
  - [1] 2026-11-24: the free trial caps sessions at one hour and runs one sandbox at a time | capture: sha256:108c642d87a113db477bdd3b5abda755b8fd0e55faf91500f89db6b224614236 | quote: ephemeral · 1-hour sessions
  - [1] 2026-11-24: the free trial root disk ceiling is 32 GiB, not 8 GiB | capture: sha256:108c642d87a113db477bdd3b5abda755b8fd0e55faf91500f89db6b224614236 | quote: up to 32 gib root disk
  - [4] 2026-11-24: the signup page asks for an email address | capture: sha256:af792fcbd6069289071812c98eea734dfb794c8c9b6271aaf332c4ba1bbbf2f7 | quote: email
  - [4] 2026-11-24: the signup form requires a password of 8 to 128 characters | capture: sha256:af792fcbd6069289071812c98eea734dfb794c8c9b6271aaf332c4ba1bbbf2f7 | quote: password8 to 128 characters
  - [1] 2026-11-24: the pricing page prices persistent volumes but publishes no egress line | capture: sha256:108c642d87a113db477bdd3b5abda755b8fd0e55faf91500f89db6b224614236 | quote: 1 gib persistent volumes | $0.15/month | $0.15/month
  - [5] 2026-11-24: the managed cloud exposes a documented API reference and a dashboard | capture: sha256:3c92bb83fec033552ec16db119fd8e22ea715e9c7410501fbf491e7c8c8344a8 | quote: [API reference](https://docs.microsandbox.dev/api-reference/overview.md)
  - [6] 2026-11-24: the managed cloud is driven through a documented REST API and CLI | capture: sha256:76743991579d8edcfba70db317df4d916b91d52d6af8e39dfbec5ac289f9680a | quote: See [context commands](https://docs.microsandbox.dev/cli/management.md#msb-context) for JSON output and troubleshooting.
  - [1] 2026-11-24: paid tiers convert their monthly fee to usage credit and unused credit does not roll over | capture: sha256:108c642d87a113db477bdd3b5abda755b8fd0e55faf91500f89db6b224614236 | quote: your monthly payment becomes usage credit. extra usage is billed at the rates below. monthly credit does not roll over.
- sources:
  - [1] https://microsandbox.dev/pricing
  - [2] https://microsandbox.dev
  - [3] https://docs.microsandbox.dev/changelog/2026-08-21.md
  - [4] https://microsandbox.dev/signup?plan=free
  - [5] https://docs.microsandbox.dev/cloud/overview.md
  - [6] https://docs.microsandbox.dev/cloud/connect.md
