# Livepeer Studio

> livepeer.studio | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/livepeer/ | JSON https://fshy.ajam.dev/api/v1/entity/livepeer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Livepeer Studio

- `compute/livepeer-studio` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://livepeer.studio/pricing
- free tier: Sandbox plan, free: 1,000 transcoding minutes per month, 60 storage minutes per month, 5,000 delivery minutes per month, up to 30 concurrent viewers, 'Minimum Spend: None'. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: No card required, as reported: the vendor pricing page states "Minimum Spend: None" for the Sandbox plan, and an independent plan listing adds "No credit card required". A third-party restatement, so the rung is reported rather than documented. No hold exists because no payment method is stated, and the record does not state whether signup asks for an email address or anything else, nor whether debit or prepaid cards are accepted on the paid plans.
- interface: unknown
- limits:
  - volume-quota (binding): 1,000 transcoding minutes and 30 concurrent viewers are the first two walls; the free plan also excludes the paid AI endpoints. [1]
- limits note: 1,000 transcoding minutes and 30 concurrent viewers are the first two walls; the free plan also excludes the paid AI endpoints.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 1,000 free transcoding minutes covers about 16.6 hours of single-rendition video per month, which composes with a free object store for source and output; delivery at 5,000 minutes caps distribution, not production.
- reliability: no reliability event recorded
- notes: Livepeer's own 2026-05 product update is reported to deprioritise Studio transcoding, so evaluated providers may shrink; the pricing page was still live on 2026-10-22. Whether the minutes are free of charge or free of minimum spend only was not measured with a live render.
- extras:
  - facets.class: decentralized-media
  - facets.free_tier_kind: perpetual
- evidence:
  - [1] 2026-10-22: Sandbox free plan: 1,000 minutes/month transcoding, 60 minutes/month storage, 5,000 minutes/month delivery, 30 concurrent viewers, minimum spend none
  - [2] 2026-10-22: independent plan listing repeats the allowances and adds 'No credit card required' plus access to AI generate beta endpoints
- sources:
  - [1] https://livepeer.studio/pricing
  - [2] https://apis.io/plans/livepeer-com/livepeer-com-plans-pricing/
