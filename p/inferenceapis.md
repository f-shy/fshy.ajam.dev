# Inference APIs

> inferenceapis.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/inferenceapis/ | JSON https://fshy.ajam.dev/api/v1/entity/inferenceapis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Inference APIs

- `inference/inferenceapis` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://inferenceapis.com/pricing
- free tier: No free allowance is stated on the pricing page read 2026-11-18: pay-as-you-go from prepaid credits with no subscription, no minimums and no daily request or token caps. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: a free account is created, then funds are added with a card before calls succeed
- interface: rest
- limits:
  - volume-quota (binding): prepaid credits billed per model; no free tier and no daily caps [1]
- endpoint: https://api.inferenceapis.com/v1
- tooling: an OpenAI-compatible key with per-model pay-as-you-go pricing
- composes with: the prepaid balance is the scarce link; no free tier exists to outgrow
- reliability: only abusive traffic is throttled; no documented free allowance
- evidence:
  - [1] 2026-11-18: pay-as-you-go from prepaid credits with no free tier | capture: sha256:89a6c0300df8de3dc6d0495ee268d6bbf8095dec0ad847cce869da8b4a7ac6ba | quote: Pay as you go from prepaid credits. No subscription, no minimums, no daily request or token caps — you pay for what you use, per model, at the rates below.
- sources:
  - [1] https://inferenceapis.com/pricing
