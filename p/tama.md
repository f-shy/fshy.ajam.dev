# tama

> tama.computer | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tama/ | JSON https://fshy.ajam.dev/api/v1/entity/tama.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tama

- `compute/tama` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-25T15:03:52.090Z (live) | stale on 2026-12-26
- url https://tama.computer/
- free tier: No charge for snapshots or stopped machines. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email | detail: unverified: no signup gate is stated on the page read; the CLI installer and machine commands are published, but the identity kind is not established
- interface: cli
- limits:
  - request-rate (binding): billed by the second; the metered CPU-only rate is $0.0117 per vCPU-hour plus $0.0055 per GiB-hour and a dedicated instance reserved for a month is $4.82/hr × 730 h [1]
  - retention-clamped: a persistent kernel bills at 1.08 times its running rate while stopped, so a stop is a surcharge rather than a saving [1]
  - per-object-cap: machines run from 1 to 32 vCPU and 1 to 128 GB of RAM, with a GPU attached per machine [1]
- interface detail: CLI installed by a shell installer and driven with tama commands such as `tama new base --gpu H100`; no other interface is documented on the page
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and states per-second billing, the shape range and the persistent-kernel behaviour. There is no free tier, so the verdict moves to paid-only, and the stopped-machine multiplier is the keeper cost
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 6
  - shape.ram: 17
  - shape.gpu_class: NVIDIA H100
  - shape.gpu_count: 1
  - shape.note: the H100 shape is 24 GB of VRAM, 6 vCPU and 17 GB of RAM; CPU machines go to 32 vCPU and 128 GB
  - session_cap.restart_required: no
  - session_cap.note: a persistent kernel keeps state and bills at 1.08 times the running rate while stopped
  - free_tier_kind: none
  - burst_x: 1.0
  - ps.price: state is kept by a persistent kernel at 1.08 times the running rate
  - ps.durability: persistent kernel
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the kernel is kept
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Give your agent a machine to hack on and pay by the second' with 'tama new base --gpu H100', '1-32 vCPU · 1-128 GB RAM', 'Reserving a dedicated instance for a month $4.82/hr × 730 h', and 'persistent-kernel 1.08× stopped', quoted
  - [1] 2026-11-25: stopped machines and snapshots carry no charge; the 1.08x row is an optimisation speedup in a fork demo | capture: sha256:52a2d48956fb688a54ff84667c7ceb35811a19c1230c67e500651fc3f9beb74e | quote: No charge for snapshots or stopped machines.
  - [1] 2026-11-24: the machine is reached by an installed CLI | capture: sha256:52a2d48956fb688a54ff84667c7ceb35811a19c1230c67e500651fc3f9beb74e | quote: `curl -fsSL https://tama.computer/install | sh`
  - [1] 2026-11-24: a tama CLI provisions machines | capture: sha256:52a2d48956fb688a54ff84667c7ceb35811a19c1230c67e500651fc3f9beb74e | quote: `tama new base --gpu H100`
  - [1] 2026-11-24: the current metered CPU-only rate | capture: sha256:52a2d48956fb688a54ff84667c7ceb35811a19c1230c67e500651fc3f9beb74e | quote: $0.0117 per vCPU-hour + $0.0055 per GiB-hour
  - [1] 2026-11-24: per-second billing and no charge for snapshots or stopped machines | capture: sha256:52a2d48956fb688a54ff84667c7ceb35811a19c1230c67e500651fc3f9beb74e | quote: ## You only pay for the seconds a machine is running. No charge for snapshots or stopped machines.
- sources:
  - [1] https://tama.computer/
