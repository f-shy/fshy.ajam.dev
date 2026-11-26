# gitpod

> gitpod.io | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitpod/ | JSON https://fshy.ajam.dev/api/v1/entity/gitpod.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gitpod (now Ona), Compute

- `compute/gitpod` | paid-only | evidence documented | binding write-gated | category dev environment
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T11:17:26.441Z (live) | stale on 2026-12-26
- url https://www.gitpod.io/pricing
- duplicate of `compute/ona`
- free tier: no self-serve free tier is published at the cited URL: the page reached is a 'Talk to us' sales contact form requiring full name, work e-mail, company website, total numbers of engineers, phone number and cloud infrastructure. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: Catalogue documentation prices this as a development environment with a free tier.
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
  - [1] 2026-11-25: the cited pricing URL resolves to a sales contact page rather than a published price or free tier | capture: sha256:d6b08305da3d3348910d38c67768b45636aeead25a3a75d5f175a305780f2800 | quote: # Talk to us
  - [2] 2026-11-25: the page reached from the cited pricing URL is a sales contact form, with no self-serve free tier stated | capture: sha256:681201cd7be00092eb66770627a5100f262d25bdc40817b4baac431100446ad8 | quote: Fill out the form below and our team will get in touch.
- sources:
  - [1] https://www.gitpod.io/pricing
  - [2] https://ona.com/contact/sales

## gitpod (now ona), Storage

- `storage/gitpod` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:41.045Z (inherited) | stale on 2026-12-04
- url https://www.gitpod.io/pricing
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
  - death.on: 2026-11-19
  - death.cause: free-tier-removed
- evidence:
  - [1] 2026-10-21: gitpod.io no longer resolves to a pricing page — it redirects to ona.com, which routes /pricing to a sales contact form. There is no self-serve free tier to evaluate; the product pivoted to
  - [2] 2026-10-21: cited as the basis of the rejection: gitpod.io no longer resolves to a pricing page — it redirects to ona.com, which routes /pricing to a sales contact form. There is no self-serve free tier to evaluate; the product pivoted to
  - probe:https://www.gitpod.io/pricing 2026-11-19: the gitpod.io pricing URL redirects through ona.com/pricing to a sales contact page, with no self-serve pricing page reachable | capture: sha256:5c21a1262aeea27eeb2cc781ac8e02e6b00e71ee676c627a8d41a6267507134e | quote: "final_url": "https://ona.com/contact/sales"
  - probe:https://www.gitpod.io/pricing 2026-11-19: the gitpod.io pricing URL now redirects to an Ona sales contact page; the old self-serve free tier is no longer offered | capture: sha256:5c21a1262aeea27eeb2cc781ac8e02e6b00e71ee676c627a8d41a6267507134e | quote: "final_url": "https://ona.com/contact/sales"
- sources:
  - [1] https://www.gitpod.io/pricing
  - [2] https://ona.com/contact/sales

## gitpod / ona

- `storage/gitpod-ona` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:45.425Z (inherited) | stale on 2026-12-04
- url https://www.gitpod.io/pricing
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
  - probe:https://www.gitpod.io/pricing 2026-11-19: gitpod.io/pricing redirects to ona.com contact/sales, so the former free-tier Gitpod pricing is gone | capture: sha256:095cbb76881c4fdfca1db203e4c64b12e8e99d2d25d3bb50cb2b5bd35a07ac90 | quote: "final_url": "https://ona.com/contact/sales"
- sources:
  - [1] https://www.gitpod.io/pricing
  - [2] https://ona.com/contact/sales
