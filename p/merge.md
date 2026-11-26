# Merge Gateway

> merge.dev | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/merge/ | JSON https://fshy.ajam.dev/api/v1/entity/merge.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Merge Gateway

- `inference/merge-gateway` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference gateway with a free plan
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.merge.dev/merge-gateway/cost/pricing
- free tier: Free plan: nothing to pay, signup credit covers requests to the free model list up to a daily request cap; no card required. Pro is vendor cost plus a 5% Merge fee. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: signup needs no card; an email signup at gateway.merge.dev is enough for the Free plan
- interface: rest
- limits:
  - volume-quota (binding): Free plan signup credit covers free-model-list requests up to a daily request cap (resets at midnight UTC); card adds Pro and the full catalog [1]
- endpoint: https://api-gateway.merge.dev/v1/ai-sdk
- tooling: OpenAI/Anthropic-compatible endpoints plus the Merge Gateway SDK
- composes with: the daily request cap on the free model list is the scarce link
- reliability: a daily cap returns 429 free_tier_daily_limit; models outside the free list return 403 free_tier_model_not_allowed
- notes: Free plan has a real daily request cap and a model allowlist; numeric cap value is not published on the captured page (unverified).
- evidence:
  - [1] 2026-11-18: the Free plan covers free-model-list requests up to a daily cap with no payment method | capture: sha256:412259e3838565c7e60ebd1a5024a19bb7536d7b9611458de95a589e1969ece2 | quote: Nothing. Signup credit covers requests to the free model list, up to a daily request cap
  - [2] 2026-11-18: signup needs no card and the Free plan has a daily request cap | capture: sha256:ab0c4d2160a9ec15c9c4b2a658e65c815a16fe8eae4e22d655ceec915db83a01 | quote: Signup needs no card. The Free plan covers a list of free models up to a daily request cap, and adding a card moves you to Pro and the full catalog.
- sources:
  - [1] https://docs.merge.dev/merge-gateway/cost/pricing
  - [2] https://docs.merge.dev/merge-gateway
