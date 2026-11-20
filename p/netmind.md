# NetMind

> netmind.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netmind/ | JSON https://fshy.ajam.dev/api/v1/entity/netmind.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NetMind

- `compute/netmind` | paid-only | evidence documented | binding volume-quota | category GPU cloud
- needs card no, phone no, ID no, institution no | verified 2026-11-03T08:50:29.744Z (live) | stale on 2026-12-04
- url https://www.netmind.ai/event/freeCredit
- free tier: No amount is stated on the live page: https://www.netmind.ai/event/freeCredit resolves to the general homepage, whose body carries no credit figure. The only archive capture (2025-04-22) reads 'you immediately unlock $ of credit' with the figure blank. | unit: mixed | metered on: wall-clock | read on: 2026-10-23 | source: [1] | note: the home page names H100, A100 and RTX 4090 as on-demand or reserved compute and lists no hourly price, tier, billing granularity or minimum bill. It names no L40S or L4.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): no USD 100 credit is published; the Elevate programme offers 'up to $100,000 in free inference credits' by application [1]
- limits note: the $100 claim does not survive the page it is attributed to
- binding note: with no published balance there is nothing to spend; the account is pay-as-you-go
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 100 at H100 list rates is a few hours of a single card or a few thousand small inference calls, which is enough to benchmark against free lanes; it does not sustain a job.
- reliability: no reliability event recorded
- notes: The Elevate programme is an application for startups, not a signup credit. Corrected on 2026-10-23 from USD 100 on a new account, which no first-party page supports.
- evidence note: the event URL and the archive capture were read on 2026-10-23 and neither carries a $100 figure; the record's earlier value came from a third-party card
- extras:
  - facets.class: decentralized-credit
  - facets.free_tier_kind: recurring-credit
  - facets.shape.gpu_class: H100/A100/RTX 4090
- evidence:
  - [1] 2026-10-23: 200 but resolves to the homepage; no credit amount in the body
  - [1] 2026-10-23: the 2025-04-22 archive reads 'you immediately unlock $ of credit' with the amount missing
  - [2] 2026-11-03: the page names H100, A100 and RTX 4090 compute and carries no rate | capture: sha256:1908c370df5830ce6c965c8226b5c5d6f19721b184d06cf2eabe3859aa9e365b | quote: H100, A100, RTX 4090 - on-demand or reserved
- sources:
  - [1] https://www.netmind.ai/event/freeCredit
  - [2] https://www.netmind.ai/
