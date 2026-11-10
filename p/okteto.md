# Okteto

> okteto.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/okteto/ | JSON https://fshy.ajam.dev/api/v1/entity/okteto.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Okteto

- `compute/okteto` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:16.615Z (live) | stale on 2026-12-05
- url https://okteto.com
- free tier: Starter, self-hosted on a Kubernetes cluster the user owns: free for up to 5 users, no credit card needed | unit: users | metered on: identity-count | read on: 2026-10-29 | source: [1] | note: read from the vendor pricing page; the licence is free, the cluster is not
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: not published: no egress allowance or overage price on https://www.okteto.com/pricing/ | metered: no | source: [2]
- identity: email
- interface: cli
- limits:
  - write-gated (binding): environments run on self-hosted Kubernetes infrastructure; the free plan does not supply compute [2]
  - request-rate: resource limits, governance and observability are the plan's levers [2]
- interface detail: Okteto CLI, a web dashboard, and an Okteto API (BETA, defined with OpenAPI) reached with an Admin Access Token
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Self-hosted: the pricing page says Okteto runs self-hosted on any Kubernetes cluster the user owns, and the free Starter plan is a self-hosted licence for up to 5 users.
- evidence note: the site was read on 2026-10-22 and describes environments spun up on self-hosted infrastructure, with a free signup. The compute is the user's cluster, so a free plan is a control plane rather than capacity
- self hosted: yes
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an environment is created per task and destroyed after; the page states no clock because a user's cluster sets it
  - free_tier_kind: allowance
  - ps.price: a user's own cluster storage
  - ps.durability: a user's own volumes
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: as long as a user keeps it
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: 'When an agent picks up work, Okteto spins up a full-stack, isolated environment on your infrastructure in seconds.' with 'Start for Free' and 'Resource limits, governance, and observability across the entire fleet', quoted
  - [1] 2026-10-29: Okteto runs self-hosted on a Kubernetes cluster a user owns; the Starter plan is free for up to 5 users | capture: sha256:d394ec3a73bb5e07a9f745b9f70a4e932b42e1e5dde6bd3680725f27ab1cc287 | quote: Okteto runs Self-Hosted on any Kubernetes cluster you own
  - [1] 2026-10-29: the Starter plan is free for up to 5 users with no credit card, and it is self-hosted | capture: sha256:d394ec3a73bb5e07a9f745b9f70a4e932b42e1e5dde6bd3680725f27ab1cc287 | quote: Free for up to 5 users, no credit card needed.
  - [1] 2026-11-03: the pricing page prints no egress allowance or overage price; only per-user pricing | capture: sha256:d394ec3a73bb5e07a9f745b9f70a4e932b42e1e5dde6bd3680725f27ab1cc287 | quote: Perfect for exploring Okteto with a small team. Free for up to 5 users, no credit card needed.
  - [3] 2026-11-03: the Okteto CLI is the documented access interface | capture: sha256:48569c40ad9d2f74f7042f45e35b08306775fe854e730c7989c63f77ca8f5e1d | quote: The Okteto CLI is our [open-source](https://github.com/okteto/okteto) tool that lets you develop your applications on Okteto.
  - [4] 2026-11-04: Okteto documents an OpenAPI-defined API in beta | capture: sha256:7ea25d5809714e65c0fbcdc3cbc2ebdf9bc22ae547e238f563bcbb05b1035349 | quote: The Okteto API `BETA` is defined using OpenAPI, providing access to resources managed by Okteto.
- sources:
  - [1] https://www.okteto.com/pricing/
  - [2] https://okteto.com
  - [3] https://www.okteto.com/docs/development/using-okteto-cli/
  - [4] https://www.okteto.com/docs/admin/okteto-api/
