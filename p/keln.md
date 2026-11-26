# Keln Sandboxes

> keln.ai | Inference, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/keln/ | JSON https://fshy.ajam.dev/api/v1/entity/keln.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Keln

- `inference/keln` | paid-only | evidence documented | binding volume-quota | category agent sandbox
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.keln.ai/models-pricing/
- free tier: No free allowance is stated on the pricing page read on 2026-11-18: sandbox time is USD 0.0001 a second on top of tokens, with a 30-second minimum (USD 0.003) for an answer that runs code. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a funded account is required before a sandbox runs
- interface: rest
- limits:
  - volume-quota (binding): USD 0.0001 per second of sandbox time with a 30-second minimum per code-running answer [1]
- endpoint: https://api.keln.ai/v1
- tooling: the vendor API with a code-execution sandbox
- composes with: the 30-second minimum is the scarce link, because a short run still bills the full half minute
- reliability: a per-second meter with a minimum means latency costs money independently of tokens
- evidence:
  - [1] 2026-11-18: sandbox time is USD 0.0001 a second on top of tokens with a 30-second minimum of USD 0.003 per code-running answer | capture: sha256:f5c13a7ea5a568b960ec1a73b86152df95d9016f795ebf9273054741e0d3ee03 | quote: - Code execution bills per second of sandbox time, on top of tokens. Details ↗
- sources:
  - [1] https://docs.keln.ai/models-pricing/

## Keln Sandboxes

- `compute/keln-sandboxes` | paid-only | evidence documented | binding volume-quota | category agent sandbox | tier prepaid sandbox compute
- needs card no, phone no, ID no, institution no | verified 2026-11-25T02:12:34.751Z (live) | stale on 2026-12-26
- url https://docs.keln.ai/sandboxes/
- free tier: No free sandbox allowance is stated. Workspaces are prepaid by card and requests return 402 at zero balance; the default is 3 running sandboxes before the first paid top-up. | unit: none | metered on: wall-clock | read on: 2026-11-25 | source: [1] | note: No free trial, free credits or recurring free sandbox hours are published on the sandbox, billing or FAQ pages read.
- per-object cap: not applicable: the unit is a sandbox, not an object | note: No per-object cap is published.
- retention: A running sandbox is stopped at a 24-hour lifetime from creation or last resume; a paused sandbox holds files, memory and processes until deletion or expiry after 30 days. | source: [2]
- egress: Outbound internet is enabled by default; port 25 is always blocked. Public preview-port URLs are available with an optional token. No data-out price or allowance is published. | metered: no | source: [3]
- identity: email | detail: Sign-in is with Google, GitHub, or email and password; creating an API key requires a verified email address. Sandbox top-ups are by card, USD 5 to USD 5,000, with a 2.9% plus USD 0.30 fee.
- interface: rest, cli
- limits:
  - volume-quota (binding): 100 running sandboxes per workspace, or 3 before the first paid top-up [4]
  - retention-clamped: 24-hour sandbox lifetime from creation or last resume; paused sandboxes kept at most 30 days [4]
  - request-rate: 500 requests per second, burst to 1,000, per key [4]
  - per-object-cap: 1 MB request body; file uploads stream and have no limit [4]
- limits note: A balance must cover the first 5 minutes of runtime at create or resume; images are limited to 20 per workspace and previews to 256 per sandbox.
- binding note: With no free credits, the prepaid balance and the 3-sandbox pre-top-up cap stop a user before any time limit does.
- interface detail: Sandbox API at https://sandbox.keln.ai/v1 with commands, streamed output, file I/O, preview ports and a network policy; an MCP server connects Claude Code, Cursor and Codex.
- endpoint: https://sandbox.keln.ai/v1/sandboxes
- tooling: The user calls the REST API or connects the hosted MCP server; no client install is needed beyond an API key.
- composes with: Sandboxes share the same prepaid balance and API key as Keln inference, so agent compute and model tokens are billed through one account.
- reliability: If the balance runs out while sandboxes are running, Keln stops them after 60 seconds; paused sandboxes remain paused because they incur no charges.
- notes: A paid-only hosted sandbox: USD 0.166 per hour for 2 vCPU/4 GiB, prepaid by card with no free allowance. Public preview URLs and an MCP server are offered.
- evidence note: Sandbox prices, limits and the prepaid card gate are quoted from the vendor's own docs read on 2026-11-25.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - shape.disk_gib: 10
  - shape.note: default template 2 vCPU, 2048 MiB memory, 10240 MiB disk; a 2 vCPU/4 GiB configuration is USD 0.166/h
  - billing_model: prepaid per-second metering
  - free_tier_kind: none
  - term: per-second, no monthly fee
  - price_arithmetic: 2 × $0.0504 + 4 × $0.0162 = $0.166 per hour
  - status: live
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: preview ports over HTTPS with an optional token
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: 24-hour maximum lifetime; paused sandboxes expire after 30 days
- evidence:
  - [4] 2026-11-25: the per-vCPU price | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | vCPU | $0.0504 per vCPU-hour |
  - [4] 2026-11-25: the default-comparable 2 vCPU/4 GiB hourly price | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | 2 vCPU, 4 GiB | $0.166 |
  - [4] 2026-11-25: the running-sandbox cap before a paid top-up | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | Running sandboxes | 100, or 3 before your first paid top-up | Per workspace | `429 concurrency_limit` |
  - [4] 2026-11-25: the sandbox lifetime | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | Lifetime | 24 hours from `created_at` or the last resume | Per sandbox | `400 invalid_parameter` |
  - [4] 2026-11-25: paused-sandbox retention | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | Paused sandboxes | 100, each kept 30 days at most | Per workspace | `429 paused_limit` |
  - [1] 2026-11-25: the prepaid card top-up and fee | capture: sha256:8d89a4404a00e32e6934ecdfaa1453069b60440b0021702513ab92e793c16830 | quote: Top-ups are by card, $5 to $5,000, with a processing fee of 2.9% + $0.30 itemized at checkout.
  - [5] 2026-11-25: the sign-in options | capture: sha256:b86eae10a4ec2316af351545ed3df568dd54eb24b951a6ce53e5afa8e6ad1d72 | quote: Sign in at [app.keln.ai](https://app.keln.ai/) with Google, GitHub, or email and password.
  - [2] 2026-11-25: paused sandbox data retention | capture: sha256:cc43edccc75b492f82cf84085c53553f4625c6329ac4e9289dac18331665690f | quote: | `paused` | A snapshot of files, memory, and processes | You delete the sandbox, or it expires after 30 days with `end_reason` set to `pause_expired`. |
  - [3] 2026-11-25: egress restriction | capture: sha256:c58cbd222c0b4afafb3304b6c3c0021001fd08732f1d4a18736eb6a83955752c | quote: Outbound traffic on port 25 is always blocked, even when internet access is enabled.
  - [4] 2026-11-24: vCPU time is USD 0.0504 per vCPU-hour | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | vCPU | $0.0504 per vCPU-hour |
  - [4] 2026-11-24: memory is USD 0.0162 per GiB-hour | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | Memory | $0.0162 per GiB-hour |
  - [4] 2026-11-24: the base 2 vCPU and 2 GiB sandbox is USD 0.133 per hour | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | 2 vCPU, 2 GiB (`base` default) | $0.133 |
  - [4] 2026-11-24: billing is per second while running with no monthly fee and a one-second minimum | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: A sandbox that starts running is billed for at least 1 second.
  - [4] 2026-11-24: the balance must cover the first five minutes before a sandbox starts | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: Your balance must cover the first 5 minutes of runtime when creating or resuming a sandbox. Otherwise, the API returns `402 insufficient_balance`.
  - [4] 2026-11-24: a sandbox runs at most 24 hours from creation or last resume | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: A sandbox can run for a maximum of 24 hours from `created_at` or its most recent resume.
  - [4] 2026-11-24: running sandboxes are capped at 100 per workspace, or 3 before the first paid top-up | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | Running sandboxes | 100, or 3 before your first paid top-up | Per workspace | `429 concurrency_limit` |
  - [4] 2026-11-24: requests are capped at 500 per second per key with a burst to 1000 | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: | Requests | 500 per second, burst to 1,000 | Per key | `429 rate_limited` |
  - [4] 2026-11-24: the Sandbox API is at sandbox.keln.ai and shares API keys and prepaid balance with inference | capture: sha256:041ad7c4b8e5399c874f628505ea5ecb93b77e9016daa2fa06bb96229d5c6445 | quote: The Sandbox API is available at `https://sandbox.keln.ai`. It uses the same [API keys](https://docs.keln.ai/platform/authentication/) and prepaid [balance](https://docs.keln.ai/platform/billing/) as the inference API.
  - [2] 2026-11-24: a stopped sandbox's contents are deleted and a paused snapshot expires after 30 days | capture: sha256:5be72abdf09a87edca517a0e49cab5ca30b9f942fb24b3fb5039b9934bc819a2 | quote: You delete the sandbox, or it expires after 30 days with `end_reason` set to `pause_expired`.
  - [3] 2026-11-24: outbound internet access is on by default and can be restricted; outbound port 25 is always blocked | capture: sha256:c19de5395696d210bb9791f42afd2462b93c508d98a23358d8027803c92cc0fd | quote: Outbound traffic on port 25 is always blocked, even when internet access is enabled.
  - [5] 2026-11-24: sign-in uses Google, GitHub or email and password, and a key requires a verified email | capture: sha256:8a9955bd4ab6371c912cbfe4d697364c36a3350415338ca683f1c115f19779dc | quote: Creating a key requires a verified email address.
  - [1] 2026-11-24: top-ups are by card from USD 5 to USD 5000 with a fee itemised at checkout | capture: sha256:8bc67934abd799d5414c40509ff3b815500a1a92d05e5a325377b25e755d59b9 | quote: Top-ups are by card, $5 to $5,000, with a processing fee of 2.9% + $0.30 itemized at checkout.
- sources:
  - [1] https://docs.keln.ai/platform/billing/
  - [2] https://docs.keln.ai/sandboxes/data-handling/
  - [3] https://docs.keln.ai/sandboxes/network/
  - [4] https://docs.keln.ai/sandboxes/
  - [5] https://docs.keln.ai/platform/authentication/
