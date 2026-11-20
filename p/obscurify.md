# Obscurify.ai

> obscurify.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/obscurify/ | JSON https://fshy.ajam.dev/api/v1/entity/obscurify.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Obscurify.ai

- `inference/obscurify` | trial-only | evidence documented | binding volume-quota | category inference gateway (privacy-first)
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://obscurify.ai/api-docs
- free tier: New accounts may get $1 of starter credit while this month's promo budget lasts. | unit: credits | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: anonymous | detail: account creation needs only a random account number, with no email, username or password
- interface: rest
- limits:
  - volume-quota (binding): USD 1 starter credit while the monthly promo budget lasts; free models limited to 1M tokens on Pay As You Go [1]
- endpoint: https://obscurify.ai/v1
- composes with: The starter credit is conditional on a promo budget, so it is not a standing free tier.
- reliability: an account with no balance and no plan gets 402; accounts never funded are deleted after 30 days
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: Obscurify may grant USD 1 of starter credit from a limited promo budget; free models carry a 1M token limit | capture: sha256:1052df0d547fb775966866d9ca2df7bf8d7423d56380ac6c0726b79d57c5e7ad | quote: New accounts may get $1 of starter credit while this month's promo budget lasts.
- sources:
  - [1] https://obscurify.ai/api-docs
