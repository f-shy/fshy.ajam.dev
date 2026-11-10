# Tenki Sandbox

> tenki.cloud | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tenki/ | JSON https://fshy.ajam.dev/api/v1/entity/tenki.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tenki Sandbox

- `compute/tenki` | qualifies-with-caveat | evidence documented | binding volume-quota | category container and VM sandbox | tier Sandbox, Starter plan, 1 vCPU / 1 GiB / 5 GiB disk
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:18.818Z (live) | stale on 2026-12-05
- url https://tenki.cloud/pricing
- price parsed USD 48.62/mo
- free tier: USD 100 in free credits on a new account: USD 50 at signup and USD 50 the first time a payment method is added. Starter itself is a free plan. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: credit
- per-object cap: Starter caps a machine at 4 cores / 8 GB with 5 concurrent sessions; Team (USD 250/month, or USD 200 billed yearly) raises it to 16 cores / 64 GB and 100 sessions
- retention: A paused sandbox stops charging and keeps its files and memory; first 5 GiB of disk is free, storage beyond it is metered. | source: [1]
- egress: not published: the pricing page's sandbox rate table lists vCPU, memory and disk only, with no transfer allowance or per-GB price; the docs index puts its egress page under Runners, not Sandbox | metered: no | free allowance: not stated | source: [1]
- identity: card | detail: USD 50 of the USD 100 credit is released only when a payment method is added; top-up minimum USD 20. Card type and hold are not stated.
- interface: cli, ssh
- limits:
  - volume-quota (binding): Starter machines cap at 4 cores / 8 GB; 5 GiB of sandbox disk free [1]
- limits note: A sticky session has no duration cap, which is unusual among documented hosts: 'A sticky session runs until you terminate it.'
- binding note: The hourly rate is the wall: USD 0.0504 per vCPU-hour is 45x Krova's per-vCPU rate, so a month of 24/7 costs what a year of Krova costs.
- interface detail: `tenki` CLI, TypeScript, Python and Go SDKs, and SSH into a session with authorized keys; no REST reference read
- tooling: not stated
- composes with: not established
- reliability: Usage is metered by the second with no minimums; when the balance runs out Tenki stops starting new jobs and sessions until a top-up or auto-reload.
- notes: Arithmetic: 0.000014 x 3600 = USD 0.0504/vCPU-hour and 0.0000045 x 3600 = USD 0.0162/GiB-hour; 1 vCPU + 1 GiB = USD 0.0666/hour, x 730 = USD 48.62. At a 2 vCPU / 4 GiB shape the same rate gives (2 x 0.0504 + 4 x 0.0162) x 730 = USD 120.89 a month. Modelled at 200 hours a month instead of 730, the same shape would be USD 13.32.
- evidence note: All four sandbox rates, the credit split, the plan ceilings and the per-second metering are quoted from the vendor's pricing page read.
- extras:
  - keep_rate: 1.0
  - billing_model: per-second
  - shape.vcpu: 1
  - shape.ram_gib: 1
  - shape.disk_gib: 5
  - session_cap.restart_required: no
  - session_cap.note: no wall-clock cap stated; pausing stops the meter
  - network_out.allow_outbound: yes
  - network_out.ports: not stated on the pricing page
  - free_tier_kind: credit
  - granularity.min_billed_s: 0
  - burst_x: 1.0
  - shape_max.vcpu: 4
  - shape_max.ram_gib: 8
  - shape_max.disk_gib: 100
  - term: monthly plan plus usage
  - m10h_usd: 19.98
  - m24h_usd: 48.62
  - price_arithmetic: (0.0504 + 0.0162) = USD 0.0666/hour x 730 h = USD 48.62; x 300 h (10 h/day) = USD 19.98. Disk beyond the free 5 GiB adds 0.000108/GiB-hour.
  - credit_usd: 50
  - credit_usd_with_card: 100
  - credit_months_at_shape: 0.41
  - credit_hours_at_shape: 302
  - credit_expiry: not stated for free credits; purchased credits never expire
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Every plan includes free credits and limits. Go beyond them and you only pay for what you run.' with '\+ Usage beyond free credits', '$100 one-time credit', 'Up to 5 concurrent sessions' and '$100 monthly credits' on the paid tier, quoted
  - [1] 2026-10-24: quoted: '$100 one-time credit', 'Up to 5 concurrent sessions', 'Up to 4 cores and 8 GB RAM', and from the FAQ: 'New accounts get $100 in free credits: $50 when you sign up, applied to your first workspace, and $50 the first time you add a payment method.'
  - [1] 2026-10-24: quoted rate table: 'Sandbox vCPU $0.000014 per second', 'Sandbox Memory $0.0000045 per GiB/second', 'Sandbox Disk $0.00000003 per GiB/second Free 5 GiB'.
  - [2] 2026-10-24: quoted: 'A sticky session runs until you terminate it.'; 'Unset options fall back to service defaults of 2 vCPU, 4096 MB, and a 5 GiB root disk.'; 'Pause and resume preserve the VM's memory and durable filesystem state'.
  - [1] 2026-10-24: quoted: 'Sandbox vCPU | $0.000014per second'; 'Sandbox Memory | $0.0000045per GiB/second'; 'Sandbox Disk | $0.00000003per GiB/second Free 5 GiB'
  - [1] 2026-10-24: quoted FAQ: 'New accounts get $100 in free credits: $50 when you sign up ... and $50 the first time you add a payment method' and 'Starter is free ... up to 5 concurrent sessions and machines up to 4 cores / 8 GB'
  - [1] 2026-11-03: the sandbox rate table lists vCPU, memory and disk and no transfer line | capture: sha256:c72e4ae713d97dadf763eba128fde49de5d7de3495b6a0037546c488cccd70a1 | quote: | Sandbox Disk | $0.00000003per GiB/second Free 5 GiB |
  - [3] 2026-11-03: a CLI with SSH support exists | capture: sha256:36ddf3c1097471b61e8e79c621c8b40eea8cdca4f3cf72a0fc3e4db051309805 | quote: Command reference for the `tenki` CLI covering authentication, session lifecycle, command execution, file transfer, port exposure, SSH, persistent volumes, and snapshots.
  - [2] 2026-11-03: SSH keys are set at session creation in the SDKs and CLI | capture: sha256:6947920edd85ac294f839230b01eedc95436a88012db23d9ed917c9436a3b18c | quote: | SSH keys | `sshAuthorizedKeys` | `ssh_authorized_keys` | `WithSSHKeys` | `--authorized-key`, `--authorized-keys-file` |
- sources:
  - [1] https://tenki.cloud/pricing
  - [2] https://tenki.cloud/docs/sandbox/sessions.md
  - [3] https://tenki.cloud/llms.txt
