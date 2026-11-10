# XKey

> suanli.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/suanli/ | JSON https://fshy.ajam.dev/api/v1/entity/suanli.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## XKey

- `compute/xkey` | paid-only | evidence reported | binding none | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://www.suanli.ai/provider/148
- free tier: The lowest 24 GB GPU rate documented: RTX 3090 at USD 0.128 per card-hour on annual billing in a four-card instance, USD 0.133 in a two-card instance and USD 0.143 for one card, against USD 0.217 to USD 0.223 on demand. RTX 4090 runs at USD 0.144 per card-hour annual and USD 0.274 on demand. At the annual rate one card running continuously for a month costs about USD 93. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: Not established. The vendor sells in the mainland market through silengine.com and the aggregator does not record an account door.
- interface: unknown
- limits note: There is no quota to exhaust: the binding term is the annual commitment that produces the cheap rate, because the same card costs 74 percent more on demand, at USD 0.223 against USD 0.128 per card-hour.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: USD 93 a month for a dedicated 3090 changes what a no-budget client can do: three days of continuous GPU time costs about USD 9 here, against the USD 0.64 median hourly rate for a 4090 that the same aggregator reports for the market as a whole.
- reliability: no reliability event recorded
- notes: New to documented records. Everything about this record comes from the aggregator, whose cheapest tier is an annual commitment, so the number is the best case rather than the walk-up price; the on-demand figure is in the same evidence line for that reason. The vendor page at silengine.com was not read, and the aggregator's collection method is its own claim, so this is reported and not documented. Open question: whether the annual rate is payable by a foreign card or requires a mainland account.
- extras:
  - facets.class: regional-floor-price
  - facets.free_tier_kind: none
  - facets.shape.gpu_class: RTX 3090
  - facets.shape.gpu_count: 4
  - facets.shape.vram_gib: 24
- evidence:
  - [1] 2026-10-22: provider page lists RTX 3090 at $0.128 per card-hour for a four-card annual instance in 西南八区, $0.133 for two cards, $0.143 for one, and $0.217 to $0.223 on demand, refreshed within 24 hours
  - [2] 2026-10-22: the 4090 comparison page names 希氪智算 as the monthly-billing cheapest of 106 providers at $0.144 per card-hour, and gives the market median as $0.64
  - [1] 2026-10-22: the page states the vendor's own site is silengine.com, which is where the price would have to be confirmed
- sources:
  - [1] https://www.suanli.ai/provider/148
  - [2] https://www.suanli.ai/gpus/RTX-4090
