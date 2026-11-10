# Ona Cloud

> ona.com | Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ona/ | JSON https://fshy.ajam.dev/api/v1/entity/ona.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Ona (formerly Gitpod)

- `compute/ona` | paid-only | evidence documented | binding write-gated | category dev environment
- needs card yes, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ona.com/contact/sales
- free tier: no self-serve free tier is reachable: the Gitpod pricing URL now resolves to a sales contact form that asks for company, headcount and cloud provider | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: an earlier catalogue row records a free tier; no page that states one was reachable in verification
- per-object cap: not stated | source: [2]
- retention: not established
- egress: not published | metered: no | source: [1]
- identity: card | detail: a sales conversation; no self-serve signup was reachable
- interface: unknown
- limits:
  - write-gated (binding): the pricing URL resolves to a sales contact form with no self-serve signup [1]
- limits note: Product offers development environments via sales-led onboarding; self-serve pricing is not published.
- binding note: the pricing URL resolves to a sales contact form with no self-serve tier, so a sales call is the gate
- interface detail: not established: the pricing page is now a sales form
- tooling: part of interface detail
- composes with: not established; the route requires a sales conversation
- reliability: no reliability event recorded
- notes: Ona Cloud (formerly associated with Gitpod) provides developer workspace environments under sales-directed onboarding.
- evidence note: the redirect and the form are documented; the product's terms are not, because no page stating them was reached
- extras:
  - billing_model: flat-pool
  - free_tier_kind: none
  - slug_merge: gitpod and ona are one provider; the catalogue id is ona
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-22: the URL that carried pricing now serves a sales contact form asking for company website, headcount and cloud provider
  - [3] 2026-10-22: redirected to the Ona sales form, so no self-serve price is published at the URL the catalogue cites
- sources:
  - [1] https://ona.com/contact/sales
  - [2] https://ona.com/pricing
  - [3] https://www.gitpod.io/pricing

## Ona Cloud

- `compute/ona-cloud` | dead | evidence documented | binding retention-clamped | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ona.com/stories/ona-core-shutdown
- free tier: The vendor's own notice, published 2026-10-13, quoted: 'we will be winding down Ona Cloud on October 31, 2026. Please save any code and data you want to keep before then. Current subscribers will be receiving an email with more detail. New signups have already closed.' The company joined OpenAI and points users to Codex Cloud. | unit: none | metered on: wall-clock | read on: 2026-10-13 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: The product ends on a printed date nine days after this read and new signups are already closed, so the workspace cannot be entered now and anything held on it has to be exported before 2026-10-31. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no signup is possible: the vendor notice states 'New signups have already closed' and the product winds down on 2026-10-31, so the identity cost is moot for a new user and there is no hold to pay. What the closed signup form asked for is not stated in the evidence
- interface: unknown
- limits:
  - retention-clamped (binding): The product ends on a printed date nine days after this read and new signups are already closed, so the workspace cannot be entered now and anything held on it has to be exported before 2026-10-31. [1]
- limits note: The product ends on a printed date nine days after this read and new signups are already closed, so the workspace cannot be entered now and anything held on it has to be exported before 2026-10-31.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It chains with nothing from this point, and the replacement it names, Codex Cloud, is a ChatGPT-account product rather than a free compute lane.
- reliability: no reliability event recorded
- notes: A workspace product bought by a model lab and closed is the clearest death shape in among documented hosts: the notice is first-party, the date is printed, and the reason is an acquisition rather than a cost problem. Anyone who planned a chain on a Gitpod or Ona workspace in October 2026 loses it this month.
- extras:
  - facets.free_tier_kind: none
- evidence:
  - [1] 2026-10-22: 
  - [1] 2026-10-22: 
- sources:
  - [1] https://ona.com/stories/ona-core-shutdown
