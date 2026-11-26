# Caution

> caution.co | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/caution/ | JSON https://fshy.ajam.dev/api/v1/entity/caution.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Caution

- `compute/caution` | paid-only | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-25T05:18:26.644Z (live) | stale on 2026-12-26
- url https://caution.co/pricing.html
- free tier: 2 vCPU · 14 GiB`m5.xlarge`$210/mo | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no self-serve signup: deployments are arranged with an engineer, and the compute is the user's own AWS Nitro enclave. [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22. It sells confidential-compute deployment into the user's own AWS account, with no plan and no self-serve signup, which confirms paid-only and explains why: there is no capacity to rent.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - network_out.out: yes
  - network_out.in: yes
  - network_out.ports: a user's own AWS account
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Caution supports reproducible enclave deployments on AWS Nitro, including verified deployments and a CLI-first workflow for Linux and macOS' and 'Book 20 minutes with one of our engineers'; the page publishes no self-serve plan and no price
  - [1] 2026-11-25: the fully managed price list offers the 2 vCPU, 14 GiB m5.xlarge enclave at USD 210 per month, its cheapest paid plan | capture: sha256:86d486dfa6f53aa336341a83341c810282afa4968f79ed04af28f55b8d359537 | quote: 2 vCPU · 14 GiB`m5.xlarge`$210/mo
- sources:
  - [1] https://caution.co/pricing.html
