# Cirun

> cirun.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cirun/ | JSON https://fshy.ajam.dev/api/v1/entity/cirun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cirun

- `compute/cirun` | paid-only | evidence documented | binding request-rate | category CI runner
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://cirun.io/pricing/
- free tier: Quoted from the Open Source plan: 'Always free for open source', USD 0 forever, with 'Install cirun on unlimited public repositories', 'Unlimited runners', 'ARM-based runners', 'GPU runners' and 'All supported cloud providers'. Quoted from the docs introduction: 'Run jobs on your own cloud - bring AWS, GCP, Azure, Hetzner, DigitalOcean, Oracle, OpenStack, or Vast.ai credentials' and 'Pay your cloud, not the runner provider'. | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-orchestration-only
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card | detail: no payment instrument to Cirun: the Open Source plan is 'Always free for open source' at USD 0. The card sits one layer down, because the runners execute in a cloud account the caller already holds: the setup docs require 'a Service Account with Compute Engine Admin Permissions' and a downloaded JSON key pair, i.e. an existing billed AWS, GCP, Azure, Hetzner, DigitalOcean, Oracle, OpenStack or Vast.ai identity. The authorisation amount is not stated, and whether those clouds accept debit or prepaid is not stated
- interface: unknown
- limits:
  - request-rate (binding): The cloud account fails first: Cirun gives away the scheduler and the runner definition, and every vCPU-hour it orchestrates is billed by AWS, GCP, Hetzner or Vast.ai to the caller, so what the free plan removes is a management fee and not a compute cost. [1]
- limits note: The cloud account fails first: Cirun gives away the scheduler and the runner definition, and every vCPU-hour it orchestrates is billed by AWS, GCP, Hetzner or Vast.ai to the caller, so what the free plan removes is a management fee and not a compute cost.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The composition it enables is real and is the reason to keep the row: Cirun plus an Oracle Always Free Ampere instance would put that instance's cores behind a GitHub Actions label, so a free cloud can be addressed as a CI runner. The constraint is that the free tier it composes with must already exist.
- reliability: no reliability event recorded
- notes: Verdict is paid-only rather than qualifies, and the distinction matters: 'free for open source' here means free to schedule, and a reader who takes it for free GPU capacity will find a Vast.ai invoice. It is a strong chain member and a zero on its own. The docs FAQ and getting-started paths both 404, so the pricing page and the docs index are the evidence; docs.cirun.io returned 200 for both.
- extras:
  - facets.class: ci-runner-capacity
  - facets.free_tier_kind: free-orchestration-only
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Always free for open source', USD 0 forever, unlimited public repositories, unlimited runners, ARM-based runners, GPU runners, all supported cloud providers
  - [2] 2026-10-22: 'Run jobs on your own cloud - bring AWS, GCP, Azure, Hetzner, DigitalOcean, Oracle, OpenStack, or Vast.ai credentials'; 'Pay your cloud, not the runner provider'; 'runners are cheaper than GitHub-hosted'
  - [3] 2026-10-22: the setup requires 'a Service Account with Compute Engine Admin Permissions' and a downloaded JSON key pair, i.e. an existing billed cloud identity
- sources:
  - [1] https://cirun.io/pricing/
  - [2] https://docs.cirun.io/
  - [3] https://docs.cirun.io/cloud/gcp
