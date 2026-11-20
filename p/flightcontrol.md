# Flightcontrol

> flightcontrol.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/flightcontrol/ | JSON https://fshy.ajam.dev/api/v1/entity/flightcontrol.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Flightcontrol

- `compute/flightcontrol` | paid-only | evidence documented | binding volume-quota | category platform host
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.flightcontrol.dev/pricing
- free tier: The Single user plan is free with unlimited projects, unlimited environments and unlimited deployments for one user, but it deploys into the customer's own AWS account, so every instance is billed by AWS and the platform page states 'You're responsible for AWS costs'. Paid plans start at USD 97/month for 25 users. | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-control-plane
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: card
- interface: unknown
- limits:
  - volume-quota (binding): the free plan covers the control plane only; the first wall is the AWS bill for the instances, which begins with the first deployment. [1]
- limits note: the free plan covers the control plane only; the first wall is the AWS bill for the instances, which begins with the first deployment.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a free control plane on top of a paid AWS account is only worth it when the AWS account already exists for another reason; it composes with AWS credits, not with a zero-budget start.
- reliability: no reliability event recorded
- notes: Classified as a refusal of free capacity rather than a dead product: the product is live (status page operational in October 2026) and the platform fee really is zero, but the compute is an AWS invoice. Possibilities: (a) Flightcontrol had shut down; refuted by the churn of changelog entries through December 2025 and an operational status in October 2026. (b) The free plan needs a company; refuted, it is one user and personal repos. The gate is the AWS account and its card, which is a payment relationship that can be entered, but not for nothing.
- extras:
  - facets.class: bring-your-own-cloud
  - facets.free_tier_kind: free-control-plane
- evidence:
  - [1] 2026-10-22: Single user plan Free: 1 user, personal single-user repos, unlimited projects, unlimited environments, unlimited deployments, community support, 'You're responsible for AWS costs', quoted
  - [1] 2026-10-22: Starter USD 97/month including 5 services then +USD 20/service, 25 users, GitHub organizations; Business USD 397/month, quoted
  - [2] 2026-10-22: the service was reported operational on 2026-10-11, so it is not dead
- sources:
  - [1] https://www.flightcontrol.dev/pricing
  - [2] https://statusgator.com/services/flightcontrol
