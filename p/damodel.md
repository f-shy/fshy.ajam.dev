# DAMODEL

> damodel.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/damodel/ | JSON https://fshy.ajam.dev/api/v1/entity/damodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DAMODEL

- `compute/damodel` | trial-only | evidence documented | binding none | category GPU cloud
- needs card no, phone yes, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://www.damodel.com/
- free tier: RTX 4090 rental quoted at CNY 20 of credit to every new registration (新人注册), with 4090, A800 and H800 cards cut permanently in price. A price aggregator that polls vendor pages daily records the 4090 at USD 0.267 per card-hour on demand, USD 0.18 preemptible and USD 0.224 on a monthly rate for a cn-north-b instance. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: The signup form was not read. The provider is a mainland company selling in CNY, and every comparable mainland host requires a mobile number plus real-name certification, but this record does not establish it.
- interface: unknown
- limits note: The CNY 20 credit is the first thing to run out: at USD 0.267 an hour for a 4090 it buys about 11 hours at the CNY 6.67 rate the aggregator applies, and the account then needs a deposit.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A CNY 20 registration credit is one evening of 4090 time, which is enough to benchmark a model against a rented 3090 elsewhere before committing a deposit.
- reliability: no reliability event recorded
- notes: DAMODEL provides GPU instances in China with pay-as-you-go pricing.
- extras:
  - facets.class: regional-trial
  - facets.free_tier_kind: one-time-credit
  - facets.shape.gpu_class: RTX 4090
  - facets.shape.gpu_count: 1
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: front page states ¥20 新人注册丹摩 (CNY 20 for a new registration at Damodel) and 4090、A800、H800等卡型永久降价, quoted
  - [2] 2026-10-22: aggregator lists 丹摩 DAMODEL RTX 4090 at USD 0.267 on demand, USD 0.18 spot and USD 0.224 monthly for cn-north-b, refreshed within 24 hours
- sources:
  - [1] https://www.damodel.com/
  - [2] https://www.suanli.ai/gpus/RTX-4090
