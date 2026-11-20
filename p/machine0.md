# machine0

> machine0.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/machine0/ | JSON https://fshy.ajam.dev/api/v1/entity/machine0.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## machine0

- `compute/machine0` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:47:20.744Z (live) | stale on 2026-11-22
- url https://machine0.io/
- free tier: no free tier: per-minute billing from $0.013 an hour for 1 vCPU, 1 GB and 25 GB, with suspend that freezes state and stops billing | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): $0.013 an hour for the smallest VM, up to $0.208 for xxl at 8 vCPU and 16 GB [1]
  - retention-clamped: a VM stays on unless stopped or suspended; suspend freezes state and stops billing [1]
  - per-object-cap: GPUs run from $0.836 an hour up to eight H200s on one VM [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states the VM ladder, per-minute billing and the suspend behaviour. There is no free tier, so the verdict moves to paid-only, and suspend-stops-billing is the keeper cost
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: first-party: very operation is a CLI command with --json . A remote MCP server lets agents drive everything programmaticall
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.ram: 1
  - shape.disk: 25
  - shape.note: small at $0.013 an hour; GPUs including H100, H200, L40S, MI300X and RTX Ada are optional per VM
  - session_cap.restart_required: no
  - session_cap.note: VMs remain on unless stopped or suspended: the default is no reap, and suspend is a user action
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.gib: 25
  - ps.price: included in the VM size
  - ps.durability: VM disk, frozen on suspend
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - net.ports: dedicated resources with static IPs
  - net.static_ip: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'VMs remain on unless stopped or suspended.' and 'Start, Suspend, Snapshot & Resume: Freeze a VM's state, stop billing, restore later. Create golden images from any VM and spin up clones.' with the ladder: 'small 1 vCPU 1 GB 25 GB $0.013/hr ~$9/month' to 'xxl 8 vCPU 16 GB 320 GB $0.208/hr', quoted
- sources:
  - [1] https://machine0.io/
