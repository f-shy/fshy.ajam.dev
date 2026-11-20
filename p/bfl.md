# Black Forest Labs

> bfl.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bfl/ | JSON https://fshy.ajam.dev/api/v1/entity/bfl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Black Forest Labs

- `compute/black-forest-labs` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://bfl.ai/pricing
- free tier: Pay-as-you-go credits with a published calculator showing 'Rate: $0.048 / image' and 'Total Price: $0.048' for one image, and no free credit stated anywhere on the page. The page also sells open-weights licences, from a 'Builder' tier at '10K images / month' for developers to an enterprise tier. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none-published
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): no free allowance is published, so the first image is a card charge of USD 0.048; nothing here can be reached without a payment instrument. [1]
- limits note: no free allowance is published, so the first image is a card charge of USD 0.048; nothing here can be reached without a payment instrument.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The open-weights license does not meter per image, composing with external rented GPU capacity.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. The USD 0.048 rate is whatever model the calculator defaults to; the page does not name it in the extracted text, so the rate is quoted as the calculator's default and not as the price of a named model. Whether a new dashboard account receives promotional credits is not stated on the pricing page; the page was the only route read.
- extras:
  - facets.class: paid-only
  - facets.free_tier_kind: none-published
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the calculator prints 'Rate:$0.048 / image' and 'Total Price:$0.048', quoted; the page description reads 'Pay-as-you-go credits for FLUX 3 video and image, FLUX.2 image models and FLUX Tools'
  - [1] 2026-10-22: the licensing block lists 'Builder ... 10K images / month' and 'Platform ... 100K images / month', quoted; no free credits appear in the document
- sources:
  - [1] https://bfl.ai/pricing
