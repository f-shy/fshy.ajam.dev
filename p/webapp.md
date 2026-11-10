# webapp.io

> webapp.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/webapp/ | JSON https://fshy.ajam.dev/api/v1/entity/webapp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## webapp.io

- `compute/webapp-io` | qualifies-with-caveat | evidence documented | binding write-gated | category dev environment
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:24:18.389Z (live) | stale on 2026-12-05
- url https://webapp.io
- free tier: a free trial of hosted test environments that create ten or more copies of an app per branch | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Bandwidth allowance per plan: Starter (free) 10 GB, Pro 100 GB, Team 1 TB (the pricing page states a different Team figure), Scale custom; no overage price is published, limits beyond these go to sales | metered: yes | free allowance: 10 GB on the Starter plan | source: [1]
- identity: email
- interface: rest
- limits:
  - write-gated (binding): the free path is a signup; no quota or price is published on the page [1]
  - request-rate: each branch can have 10 or more environment copies [1]
- interface detail: HTTP API and webhooks (https://docs.webapp.io/api-docs/setup.md), GitHub, GitLab and BitBucket integrations, a Layerfile in the repository, and a debugging terminal
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the site was read on 2026-10-22 and offers a free start with no published quota. The product is per-branch environment copies rather than a machine, and the free tier's limits are not…
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: an environment per branch; the page states no clock
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: yes
  - net.ports: a preview per branch, reachable for acceptance tests
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'Webapp.io's hosted test environments build 10x faster than general CI/CD platforms. Build your webapps faster and try us for free today.' with 'You can create 10+ copies of your app for every branch instantly', quoted
  - [2] 2026-11-03: Starter 10 GB, Pro 100 GB, Team 1 TB bandwidth | capture: sha256:f63a65e6f930c061fe6fe602c4fc9aab434c70c092266d05c6af966491f345dd | quote: | Bandwidth | 10GB | 100GB | 1TB | Custom |
  - [2] 2026-11-03: an API and webhooks are included on every plan | capture: sha256:f63a65e6f930c061fe6fe602c4fc9aab434c70c092266d05c6af966491f345dd | quote: | API & Webhooks | ✔ | ✔ | ✔ | ✔ |
  - [3] 2026-11-03: the pricing page states 500GB for Team, conflicting with the docs table | capture: sha256:182c1388d3b11afdeec97c881cb6560a42739b27685ed19481793810142a1ab7 | quote: Previews: get 30 day retention guarantees for your previews for up to 500GB of bandwidth
  - [2] 2026-11-03: no overage price is published; limits beyond go to sales | capture: sha256:f63a65e6f930c061fe6fe602c4fc9aab434c70c092266d05c6af966491f345dd | quote: If your project is likely to exceed these limits, please [contact sales](https://webapp.io/contact/sales) to discuss solutions.
- sources:
  - [1] https://webapp.io
  - [2] https://docs.webapp.io/
  - [3] https://webapp.io/pricing
