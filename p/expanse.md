# Expanse

> expanse.sh | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/expanse/ | JSON https://fshy.ajam.dev/api/v1/entity/expanse.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Expanse

- `compute/expanse` | self-hosted, last resort | verdict paid-only | evidence documented | binding write-gated | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-11-03T08:50:26.531Z (live) | stale on 2026-12-04
- url https://expanse.sh
- free tier: no free tier published | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - write-gated (binding): no plan and no price: the product analyses the user's own GPU queue and does not supply capacity. [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Paid-only rather than dead: the product is sold and reachable. Self-hosted: one command installs Expanse on the user's existing SLURM or Kubernetes cluster, beside its scheduler.
- evidence note: the site was read on 2026-10-22. It sells a prediction tool for infrastructure that is already running, with no free tier and no compute product, which confirms paid-only
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - free_tier_kind: none
  - reclassified_from: dead
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the site was read on 2026-10-22 and sells workload prediction for GPU scheduling: 'Run Analyse before execution to predict GPU allocation, memory usage, runtime, and completion probability', with a June 2026 benchmark claiming runtime within 10% and memory within 5%. No plan and no price
  - [1] 2026-10-29: Expanse is installed on a user's existing SLURM or Kubernetes cluster | capture: sha256:ac1b9b163baafbf1768e7b02aff49e8892c23c7e385cf3ccdcede371483ab855 | quote: One command installs Expanse on your existing SLURM or Kubernetes cluster.
  - [1] 2026-11-03: the 16 x H100 figure on the page is an illustrative workload example, not a rate; the page lists no hourly price for any card and sells analysis software for an existing cluster | capture: sha256:ac1b9b163baafbf1768e7b02aff49e8892c23c7e385cf3ccdcede371483ab855 | quote: Illustrative comparison values showing the same workload before and after Expanse analysis.
- sources:
  - [1] https://expanse.sh
