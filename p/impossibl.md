# Impossibl

> impossibl.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/impossibl/ | JSON https://fshy.ajam.dev/api/v1/entity/impossibl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Impossibl

- `inference/impossibl` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://impossibl.com/docs/models
- free tier: No free allowance is stated on the docs read 2026-11-18: usage comes from workspace credits (1 credit = $0.000001) and the minimum purchase is $5 with a 5% platform fee. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a completed credit purchase of at least $5 is needed before calls to paid models
- interface: rest
- limits:
  - volume-quota (binding): 1 credit = $0.000001; minimum $5 purchase plus 5% platform fee and tax [1]
- endpoint: https://api.impossibl.com/v1
- tooling: an OpenAI-compatible key whose usage is drawn from workspace credits
- composes with: the $5 minimum credit purchase is the scarce link; no free text tier is published
- reliability: some models require a completed credit purchase even to appear as enabled
- evidence:
  - [1] 2026-11-18: the minimum credit purchase is $5 with a 5% fee | capture: sha256:00894afc03e28249b124e90f83f98ad23b83d5acbfe6ce552589c906ae6d78d5 | quote: The minimum purchase is \$5; the 5% platform fee and applicable tax are added to the credit amount.
- sources:
  - [1] https://impossibl.com/docs/models
