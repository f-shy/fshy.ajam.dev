# activeloop deep lake

> deeplake.ai | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deeplake/ | JSON https://fshy.ajam.dev/api/v1/entity/deeplake.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## activeloop deep lake / hivemind

- `storage/activeloop-deep-lake-hivemind` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:53.937Z (live) | stale on 2026-12-04
- url https://deeplake.ai/pricing
- free tier: none reachable: The product pivoted away from storage. deeplake.ai/pricing now sells 'Hivemind' agent traces and queries ($15 credits, 150k traces, 1.5M queries) with no storage allowance at all, and the… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: stated-absent: the first-party page states no per-object size cap | source: [1] | note: not applicable
- retention: stated-absent: the first-party page states no retention period for stored bytes | source: [1]
- egress: stated-absent: the first-party page states no egress terms for stored bytes | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the first-party pricing page is for agent traces and queries and states no storage client interface
- tooling: not documented
- composes with: stated-absent: the first-party page states no way to chain byte storage with other services
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: The product pivoted away from storage. deeplake.ai/pricing now sells 'Hivemind' agent traces and queries ($15 credits, 150k traces, 1.5M queries) with no storage allowance at all, and the…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The product pivoted away from storage. deeplake.ai/pricing now sells 'Hivemind' agent traces and queries ($15 credits, 150k traces, 1.5M queries) with no storage allowance at all, and the…
  - [1] 2026-11-19: the pricing page sells agent traces and queries, not a storage allowance | capture: sha256:3b9338c4d0b65f4f82ec13a00f2ee31c3606b96af70b1015e4fa7ecffccb8c8f | quote: Clear pricing for agent traces, queries, and team collaboration.
  - [1] 2026-11-19: the first-party pricing page is for agent traces and queries, not storage | capture: sha256:5a9acae1acf3ad18fa421df5d368458353a1be54f3921f9c8dfcab5cb4715012 | quote: Clear pricing for agent traces, queries, and team collaboration.
- sources:
  - [1] https://deeplake.ai/pricing
