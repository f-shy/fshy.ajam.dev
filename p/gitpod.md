# gitpod

> gitpod.io | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitpod/ | JSON https://fshy.ajam.dev/api/v1/entity/gitpod.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gitpod (now Ona), Compute

- `compute/gitpod` | paid-only | evidence documented | binding write-gated | category dev environment
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.gitpod.io/pricing
- duplicate of `compute/ona`
- free tier: no self-serve free tier is reachable: the pricing URL resolves to a sales contact form | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: Catalogue documentation prices this as a development environment with a free tier.
- per-object cap: not applicable
- retention: not established
- egress: not published | metered: no | source: [2]
- identity: card | detail: a sales conversation; no self-serve signup was reachable
- interface: unknown
- limits:
  - write-gated (binding): the pricing URL resolves to a sales form asking for company website, headcount and cloud provider [2]
- limits note: Gitpod and Ona are one provider under two names; the catalogue carries both
- binding note: the pricing URL resolves to a sales contact form, so the gate is a sales call and not a quota
- interface detail: not established
- tooling: the same as interface detail
- composes with: not established: the route is a sales conversation
- reliability: no reliability event recorded
- notes: Classified as its own slug because the catalogue carries both names and a reader may look up either. The record for the product is `ona`; this one exists so a search for Gitpod lands on the fact rather than a dead link.
- extras:
  - billing_model: flat-pool
  - free_tier_kind: none
  - duplicate_of: ona
  - slug_note: gitpod and ona are one provider
- evidence:
  - [1] 2026-10-22: redirects to ona.com/contact/sales, so no self-serve price is published at the URL the catalogue cites
  - [2] 2026-10-22: a sales contact form asking for full name, work email, company website, headcount and cloud provider
- sources:
  - [1] https://www.gitpod.io/pricing
  - [2] https://ona.com/contact/sales

## gitpod (now ona), Storage

- `storage/gitpod` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.gitpod.io/pricing
- disagrees on verdict: `storage/gitpod` says fails-quota, `storage/gitpod-ona` says dead
- free tier: None reachable: gitpod.io no longer resolves to a pricing page. It redirects to ona.com, which routes /pricing to a sales contact form. There is no self-serve free tier to evaluate; the product pivoted to. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: Gitpod.io no longer resolves to a pricing page. It redirects to ona.com, which routes /pricing to a sales contact form. There is no self-serve free tier to evaluate; the product pivoted to.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: gitpod.io no longer resolves to a pricing page — it redirects to ona.com, which routes /pricing to a sales contact form. There is no self-serve free tier to evaluate; the product pivoted to
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: gitpod.io no longer resolves to a pricing page — it redirects to ona.com, which routes /pricing to a sales contact form. There is no self-serve free tier to evaluate; the product pivoted to
  - [2] 2026-10-21: cited as the basis of the rejection: gitpod.io no longer resolves to a pricing page — it redirects to ona.com, which routes /pricing to a sales contact form. There is no self-serve free tier to evaluate; the product pivoted to
- sources:
  - [1] https://www.gitpod.io/pricing
  - [2] https://ona.com/contact/sales

## gitpod / ona

- `storage/gitpod-ona` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.gitpod.io/pricing
- disagrees on verdict: `storage/gitpod` says fails-quota, `storage/gitpod-ona` says dead
- free tier: none reachable: gitpod.io now redirects to ona.com, which routes to 'Contact sales' with no public pricing and no free tier. The free-tier Gitpod that people remember is gone. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: gitpod.io now redirects to ona.com, which routes to 'Contact sales' with no public pricing and no free tier. The free-tier Gitpod that people remember is gone.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: gitpod.io now redirects to ona.com, which routes to 'Contact sales' with no public pricing and no free tier. The free-tier Gitpod that people remember is gone.
  - [2] 2026-10-21: cited as the basis of the rejection: gitpod.io now redirects to ona.com, which routes to 'Contact sales' with no public pricing and no free tier. The free-tier Gitpod that people remember is gone.
- sources:
  - [1] https://www.gitpod.io/pricing
  - [2] https://ona.com/contact/sales
