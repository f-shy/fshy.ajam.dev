# Verda

> verda.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/verda/ | JSON https://fshy.ajam.dev/api/v1/entity/verda.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Verda (formerly DataCrunch)

- `compute/verda` | paid-only | evidence documented | binding request-rate | category GPU cloud
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://verda.com/pricing
- free tier: no free tier: pay-as-you-go GPU capacity on multi-node clusters with no commitments and no minimums, priced per GPU | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): priced per GPU-hour on multi-node clusters, with no commitment and no minimum [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Confirmed 2026-10-22: paid-only stands. The incoming qualifies-with-caveat was built on a 50 per cent spot discount off a paid meter, which is cheaper capacity rather than free capacity, and the content-credit route publishes no amount so it cannot be counted as a lane.
- evidence note: the pricing page was read on 2026-10-22 and states the pay-as-you-go model per GPU. There is no free tier, so the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.note: priced per GPU with specs shown per row
  - session_cap.restart_required: no
  - session_cap.note: a cluster runs for an hour or months; the page states no reap
  - free_tier_kind: none
  - granularity.min_billed_s: 60
  - burst_x: 1.0
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'True pay-as-you-go pricing on multi-node clusters. Spin up for an hour or months - no commitments, no minimums. Specs and price are shown per GPU.' quoted
  - [1] 2026-10-22: the pricing page carries only 'Price' and 'Spot price' columns, for example '1x H100 SXM5 80GB ... $4.470/h | $2.235/h'; there is no free tier, trial or signup credit on the page; the only free route is content-creation credits at https://docs.verda.com/resources/obtaining-free-credits/how-to-receive-credits/ with no published amount
- sources:
  - [1] https://verda.com/pricing
