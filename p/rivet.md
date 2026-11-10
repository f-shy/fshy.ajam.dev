# Rivet

> rivet.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rivet/ | JSON https://fshy.ajam.dev/api/v1/entity/rivet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Rivet (Actors & agentOS)

- `compute/rivet` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:16.351Z (live) | stale on 2026-12-05
- url https://rivet.dev/pricing/
- free tier: 100,000 awake actor hours a month on the free tier, with state storage and active CPU billed per second beyond it | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): 100,000 awake actor hours a month on the free tier [1]
  - per-object-cap: 1 vCPU is half a physical core; configurations are 0.08 to 1 vCPU, or exactly 2, 4 or 8 [1]
  - request-rate (binding): active execution bills per vCPU-second plus $0.0000029 a GiB-second of state storage [1]
- interface detail: TypeScript SDK (rivetkit, rivetkit/client) and a web dashboard; no REST, CLI or SSH access read
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the free tier's awake-actor-hour cap and the metered rates. The vCPU definition is the shape fact: one vCPU is half a physical core
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.note: 1 vCPU is half a physical core; the free tier can run 0.08 to 1 vCPU
  - session_cap.restart_required: no
  - session_cap.note: an actor sleeps when idle and only awake hours are counted, so the meter is the state axis
  - free_tier_kind: allowance
  - burst_x: 1.0
  - ps.price: $0.0000029 a GiB-second of persisted actor state
  - ps.durability: FoundationDB persistence layer
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Awake Actor Hours · 100,000 /mo max' on the free tier, with 'per 1k Awake Actor Hours', 'State Storage', 'per vCPU-second + $0.0000029/GiB-s' and '1 vCPU = half a physical core. 0.08-1 vCPU, or exactly 2, 4, or 8', quoted
  - [2] 2026-11-03: a TypeScript SDK (rivetkit) is the documented way in | capture: sha256:a33e7b42f5cd6530a2507d618ce4859a931b55c0d3501a27896820add38b945f | quote: npm install rivetkit
  - [1] 2026-11-03: the page prices control plane and Actor Nodes per month; no egress allowance or egress price is listed | capture: sha256:bb41c9e377806440a6b33b63444353a356647fb39e2ff0e9ce1bda721d44143f | quote: Pay for coordination, state, and active execution on Rivet Cloud.
- sources:
  - [1] https://rivet.dev/pricing/
  - [2] https://rivet.dev/docs/
