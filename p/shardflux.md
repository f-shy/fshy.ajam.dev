# Shardflux

> shardflux.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shardflux/ | JSON https://fshy.ajam.dev/api/v1/entity/shardflux.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shardflux

- `compute/shardflux` | trial-only | evidence documented | binding retention-clamped | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:18.815Z (live) | stale on 2026-12-05
- url https://shardflux.dev/#pricing
- free tier: a trial at Pro limits that ends at the cap or after 30 days, then the account moves to Free with nothing deleted; a parked workspace uses no compute and keeps its memory and processes | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Outbound transfer is a monthly allowance by plan: 100 GB Developer (USD 9), 250 GB Pro (USD 29), 1 TB Startup, 5 TB Scale, and 250 GB during the 7-day signup trial. There is no overage price: at 100 % of the allowance outbound internet traffic is blocked until the next period or an upgrade | metered: yes | free allowance: 250 GB during the 7-day trial; 100 GB a month on Developer | source: [1]
- identity: email
- interface: rest, cli
- limits:
  - retention-clamped (binding): the trial runs at Pro limits for 30 days or until the cap, then the account drops to Free with nothing deleted [1]
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
  - session_cap.restart_required: no
  - session_cap.note: parks seconds after the last call; suspend keeps memory and running processes, so the dev server is still on its port when it wakes
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
- sources:
  - [1] https://shardflux.dev/#pricing
  - [2] https://docs.shardflux.dev/limits
