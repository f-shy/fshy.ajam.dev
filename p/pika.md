# Pika

> pika.art | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pika/ | JSON https://fshy.ajam.dev/api/v1/entity/pika.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Pika

- `compute/pika` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://pika.art/pricing
- free tier: A USD 0 plan exists but carries no credit: the comparison table prints 'Monthly credits | 0 - packs only' for the free column against 900 for the USD 10 plan and 3,150 for USD 35. The free column does include 'No watermark: Yes' and 'Parallel video generations 2', and excludes 'Commercial license' and 'Priority queue'. Credit packs are sold separately and 'can't be used with the API, iOS app, or old.pika.art'. Published generation costs: 'Seedance 2.5 Video - 720p - 5s 122' credits, 'Wan 3.0 Video - 720p - 5s 33', 'Nano Banana 2 Images - 1 image - 1K 8', 'GPT Image 2.5 Images - 1 image - 1K 2'. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none-published
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): zero monthly credits: a free account generates nothing until it buys a pack, so the binding constraint is the first purchase rather than any rate or cap, and the cheapest image at 2 credits means even a pack is spent in hundreds of images rather than thousands. [1]
- limits note: zero monthly credits: a free account generates nothing until it buys a pack, so the binding constraint is the first purchase rather than any rate or cap, and the cheapest image at 2 credits means even a pack is spent in hundreds of images rather than thousands.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: the free account is a shell for buying packs, so it composes with nothing: no API access on packs, no commercial licence, and no recurring grant. What breaks: the absence of any allowance, which makes Pika the clearest paid-only entry among documented hosts.
- reliability: no reliability event recorded
- notes: These are inference credits, not general compute. Pika is widely listed in 'free credits' round-ups; on 2026-10-22 its own comparison table gives the free column zero monthly credits. The record exists as a refutation of that listing. Not established: whether a new account receives a one-time promotional grant that the table does not show; nothing on the page states one.
- extras:
  - facets.class: paid-only
  - facets.free_tier_kind: none-published
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: the comparison table prints 'Monthly credits | 0 - packs only | 900 | 3,150 | 8,550 and up' across the four plan columns, quoted
  - [1] 2026-10-22: 'Price / mo | $0 | $10 | $35 | $95-$880' with 'No watermark | Yes | Yes | Yes | Yes' and 'Commercial license | No | No | Yes | Yes', quoted
  - [1] 2026-10-22: generation costs 'Seedance 2.5 Video - 720p - 5s 122' credits and 'GPT Image 2.5 Images - 1 image - 1K 2' credits, quoted
  - [1] 2026-10-22: 'Top-up credits are only for Pika Create on pika.art and MCP on pika.art/mcp. They can't be used with the API, iOS app, or old.pika.art', quoted
- sources:
  - [1] https://pika.art/pricing
