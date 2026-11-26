# Shardflux

> shardflux.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shardflux/ | JSON https://fshy.ajam.dev/api/v1/entity/shardflux.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shardflux

- `compute/shardflux` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-24T13:21:04.001Z (live) | stale on 2026-12-25
- url https://shardflux.dev/#pricing
- free tier: a 7-day trial at Pro limits for a new account after an established GitHub account or work domain is verified and a $0 non-prepaid Stripe card check passes; compute pauses at the cap or after 7 days and up to 10 GiB of retained workspace storage is kept with nothing deleted; a parked workspace uses no compute and keeps its memory and processes | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Outbound transfer is a monthly allowance by plan: 100 GB Developer (USD 9), 250 GB Pro (USD 29), 1 TB Startup, 5 TB Scale, and 250 GB during the 7-day signup trial. There is no overage price: at 100 % of the allowance outbound internet traffic is blocked until the next period or an upgrade | metered: yes | free allowance: 250 GB during the 7-day trial; 100 GB a month on Developer, 250 GB Pro, 1 TB Startup, 5 TB Scale | source: [1]
- identity: email | detail: unverified: the signup form fields were not read. Registration is automatic via the console, CLI or HTTP API with Google, GitHub or a permanent email address (disposable addresses refused); compute requires an active trial, which adds an established GitHub account or work domain plus a non-prepaid Stripe card check approved by the bank
- interface: rest, cli
- limits:
  - retention-clamped (binding): the trial runs at Pro limits for 7 days or until the RAM GiB-hour or CPU-hour cap, then compute pauses until a paid plan is chosen; nothing is deleted [1]
  - request-rate: a workspace parks seconds after its last call and uses no compute while suspended [1]
- interface detail: HTTP API, the `shard` CLI, and TypeScript and Python SDKs (`npm i @shardflux/sdk`); an E2B SDK compatibility mode; no SSH access found in the docs read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the trial's 30-day life, the parked-state behaviour and that nothing is deleted when it ends. The 30-day clock is the fact, and the parked state preserving memory is the state answer
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 2
  - shape.note: the free shape is 1 vCPU and 2 GiB; Pro reaches 4 vCPU and 8 GiB per workspace, up to 8 vCPU and 16 GiB each on larger plans
  - session_cap.idle_reap_s: 600
  - session_cap.restart_required: no
  - session_cap.note: no maximum session published; the session idle timeout defaults to 10 minutes
  - free_tier_kind: trial
  - burst_x: 1.0
  - ps.price: retained storage is part of the monthly plan
  - ps.durability: microVM disk plus retained memory and processes on suspend
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: nothing is deleted when the trial ends
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Each workspace is a Linux microVM with its own kernel, disk and memory. Shardflux creates it, parks it, wakes it and keeps its state' and 'A workspace parks seconds after its last call, and the next call wakes it. Suspended, it uses no compute.' and 'Suspend and resume keep its memory and running processes, so the dev server is still on its port.' and 'At the cap or after 30 days the account is on Free, with nothing deleted.', quoted
  - [2] 2026-11-03: no overage price; outbound is blocked at the allowance | capture: sha256:cd82a34150bd502733e30faa4bdd0ca1393f6692767c29f073052068e59e96ad | quote: Storage and outbound transfer have no overage. Retained state and shared volumes are never charged, and outbound traffic is still blocked at 100 % of the transfer allowance.
  - [2] 2026-11-03: trial outbound allowance 250 GB | capture: sha256:cd82a34150bd502733e30faa4bdd0ca1393f6692767c29f073052068e59e96ad | quote: | Outbound transfer | 250 GB |
  - [2] 2026-11-03: outbound allowance per plan | capture: sha256:cd82a34150bd502733e30faa4bdd0ca1393f6692767c29f073052068e59e96ad | quote: | Outbound transfer | 100 GB | 250 GB | 1 TB | 5 TB |
  - [2] 2026-11-03: an HTTP API and the shard CLI exist | capture: sha256:cd82a34150bd502733e30faa4bdd0ca1393f6692767c29f073052068e59e96ad | quote: New accounts can register automatically via the console, CLI (`shard signup`) or HTTP API
  - [2] 2026-11-18:  | capture: sha256:73fa7d00e62212a2cf3f5802db05e05dc1017d603c5bf12d5d15bf7fbeaf8373 | quote: Session idle timeout | 10 minutes unless the template sets one (60 to 86,400 seconds)
  - [1] 2026-11-24: the trial lasts 7 days and keeps up to 10 GiB at the end | capture: sha256:de3241a32553b2012c1022726d6cc490c18922d2788150b566a48369b1a5efff | quote: At the cap or after 7 days a paid plan is required to open or resume workspaces; 10 GiB of retained workspace storage is kept.
  - [2] 2026-11-24: the trial end condition and the 7-day clock | capture: sha256:73fa7d00e62212a2cf3f5802db05e05dc1017d603c5bf12d5d15bf7fbeaf8373 | quote: When the RAM GiB-hours or CPU hours are used up, or after 7 days, workspace compute pauses until you choose a paid plan ($9/mo Developer and up).
  - [2] 2026-11-24: registration is automatic and needs no card before workspaces open | capture: sha256:73fa7d00e62212a2cf3f5802db05e05dc1017d603c5bf12d5d15bf7fbeaf8373 | quote: New accounts can register automatically via the console, CLI (`shard signup`) or HTTP API, and create organizations, projects and API keys right away.
  - [3] 2026-11-24: the signup methods and the refusal of disposable addresses | capture: sha256:064f8cb659280826791ef672f0e4fae865b92205d414b247cdd588b84c39651c | quote: Sign up at https://app.shardflux.dev/signup with Google, GitHub or a permanent email address (disposable addresses can't sign up).
  - [2] 2026-11-24: the per-plan outbound allowances | capture: sha256:73fa7d00e62212a2cf3f5802db05e05dc1017d603c5bf12d5d15bf7fbeaf8373 | quote: | Outbound transfer | 100 GB | 250 GB | 1 TB | 5 TB |
  - [1] 2026-11-24: the trial identity and card gate | capture: sha256:de3241a32553b2012c1022726d6cc490c18922d2788150b566a48369b1a5efff | quote: New accounts start the trial after a non-prepaid Stripe card check and a verified work domain or established GitHub account (nothing is charged).
  - [2] 2026-11-24: the trial length and Pro-level limits | capture: sha256:73fa7d00e62212a2cf3f5802db05e05dc1017d603c5bf12d5d15bf7fbeaf8373 | quote: This starts 7 days of Pro’s allowances and limits.
  - [2] 2026-11-24: the trial requires an established GitHub account or work domain and a card check | capture: sha256:73fa7d00e62212a2cf3f5802db05e05dc1017d603c5bf12d5d15bf7fbeaf8373 | quote: Before starting workspace compute, verify an established GitHub account (at least 30 days old) or non-disposable work domain (registered at least 30 days ago with active MX records), and complete the $0 Stripe card check
- sources:
  - [1] https://shardflux.dev/#pricing
  - [2] https://docs.shardflux.dev/limits
  - [3] https://docs.shardflux.dev/quickstart
