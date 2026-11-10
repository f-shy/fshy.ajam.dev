# Dockup

> getdockup.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/getdockup/ | JSON https://fshy.ajam.dev/api/v1/entity/getdockup.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dockup

- `compute/dockup` | qualifies-with-caveat | evidence documented | binding write-gated | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:29.905Z (live) | stale on 2026-12-05
- url https://getdockup.com/
- free tier: a Free-forever plan alongside $45 a month for unlimited users; the product deploys into the user's own AWS account. | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published: https://getdockup.com/ states no data-transfer allowance or price (it deploys into the user's own AWS account) | metered: no | source: [1]
- identity: email
- interface: git
- limits:
  - write-gated (binding): the free plan is a control plane over the user's own AWS account; there is no hosted compute to consume. [1]
- interface detail: Git push to GitHub deploys; the Dockup web UI handles manual deployments and rollbacks; no REST API or CLI is stated
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: The product deploys into an AWS account the user rents; the evidence describes a sign-up that connects GitHub and AWS, not an install.
- evidence note: the pricing page was read on 2026-10-22 and states both a free-forever row and a $45 tier. The compute is the user's own AWS account, so the free plan is a control plane rather than capacity.
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a user's own AWS account holds the machines, so the clocks are AWS's
  - network_out.out: yes
  - network_out.in: yes
  - network_out.ports: a user's own AWS account
  - free_tier_kind: allowance
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Free forever' beside '$45 monthly, unlimited users', and 'Sign up and connect your Github and AWS accounts', quoted
  - [1] 2026-11-03: deployment is driven by a Git push | capture: sha256:ac4c054145a8ec517df39a5c739efe4f75fa62394910de314887f40dff8d4049 | quote: Push to Github to deploy code.
  - [1] 2026-11-03: a web UI exists for manual actions | capture: sha256:ac4c054145a8ec517df39a5c739efe4f75fa62394910de314887f40dff8d4049 | quote: For deployment checklists, manual deployments or rollbacks, use Dockup UI.
- sources:
  - [1] https://getdockup.com/
