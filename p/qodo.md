# Qodo

> qodo.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/qodo/ | JSON https://fshy.ajam.dev/api/v1/entity/qodo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Qodo

- `compute/qodo` | trial-only | evidence documented | binding retention-clamped | category cloud VM
- needs card no, phone unknown, ID no, institution no | verified 2026-11-04T06:40:26.616Z (live) | stale on 2026-12-05
- url https://www.qodo.ai/pricing/
- free tier: no permanent free tier: "We don't offer a permanent free tier. After your trial, pick a paid plan to keep reviewing." quoted, and the docs say "Every workspace begins with a 14-day free trial starting at signup" | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: 14 days then zero, so the review capacity vanishes rather than shrinking. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card: the pricing FAQ describes the 14-day Pro Team trial as 'unlimited reviews and no credit card', so no payment method is taken and no hold exists. The trial starts at signup - 'Every workspace begins with a 14-day free trial starting at signup' - and 'When the trial ends, usage stops unless a paid billing setup is active'. The signup form's own fields are not described, so whether an email, phone number or ID document is required is unknown; kind kept as email without an evidence row stating it.
- interface: git
- limits:
  - retention-clamped (binding): 14 days then zero, so the review capacity vanishes rather than shrinking. [1]
- limits note: 14 days then zero, so the review capacity vanishes rather than shrinking.
- binding note: the same as limits note
- interface detail: Git: Qodo is installed in the user's Git provider and reviews pull requests (docs.qodo.ai, Git code review and Install Qodo in your Git provider); the pricing page also lists IDE integrations.
- tooling: the Qodo app installed in a Git provider, and the Qodo Agentic Toolbox, a CLI documented at docs.qodo.ai/agentic-toolbox.
- composes with: the trial is a 14-day instrument for measuring a review pipeline on real pull request volume, and it pairs with a free repository host; nothing survives past day 14.
- reliability: no reliability event recorded
- notes: The free Developer tier with 250 credits and 30 PR reviews a month is still repeated by review sites; the vendor page and its docs both say it does not exist. That claim is false. One free route remains and it is gated: the pricing FAQ says "Qualified open source projects can apply to the Qodo for Open Source program for free access", which is an application that must be approved, not a signup.
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: trial
- evidence:
  - [1] 2026-10-22: "We don't offer a permanent free tier. After your trial, pick a paid plan to keep reviewing." quoted from the pricing FAQ; Pro Team is a 14-day trial with unlimited reviews and no credit card
  - [2] 2026-10-22: "Every workspace begins with a 14-day free trial starting at signup. This is the universal entry point into Qodo." and "When the trial ends, usage stops unless a paid billing setup is active." quoted
  - [1] 2026-10-22: the paid unit is a credit at "$.012/credit, pooled across the team" in 2,500 / 5,000 / 20,000 packs, advertised as about 18 / 36 / 144 reviews a month
  - [1] 2026-11-03: Pro Team includes git and IDE integrations | capture: sha256:dc31d98fc17e2bb8158c6c513c366072e7d86f4a145f61d0fe590cfa3b39000d | quote: Git + IDE integrations
  - [3] 2026-11-04: the provider documents Git code review on pull requests | capture: sha256:440811532095fb5768901ea9b98b28d7c33989775581abe44d6dfd26125f4bcd | quote: Automated AI review on every pull request, with bugs, standards, and context-aware feedback.
  - [3] 2026-11-04: the provider documents a CLI-powered Agentic Toolbox | capture: sha256:440811532095fb5768901ea9b98b28d7c33989775581abe44d6dfd26125f4bcd | quote: A CLI-powered quality counterpart for coding agents.
- sources:
  - [1] https://www.qodo.ai/pricing/
  - [2] https://docs.qodo.ai/pricing-and-usage
  - [3] https://docs.qodo.ai/
