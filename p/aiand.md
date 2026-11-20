# ai&

> aiand.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aiand/ | JSON https://fshy.ajam.dev/api/v1/entity/aiand.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ai&

- `inference/aiand` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://docs.aiand.com/
- free tier: No standing free tier is stated. Inference is prepaid per token; redemption codes handed out at events grant credits with no card or checkout. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an organization account and prepaid credits; event redemption codes add credit without a card
- interface: rest
- limits:
  - volume-quota (binding): prepaid per-token credit; credits do not expire [1]
- endpoint: https://api.aiand.com/v1
- tooling: OpenAI- and Anthropic-compatible APIs, the official SDKs, and an ai& CLI
- composes with: the prepaid credit balance is the scarce link; a redemption code is the only card-free way to get credit
- reliability: a zero balance returns 402 and new requests stop; failed requests are not billed
- notes: no standing free inference allowance is published; a self-serve card-free route exists only through event redemption codes
- evidence:
  - [1] 2026-11-18: billing is prepaid per token; a free inference allowance is not stated, but redemption codes grant credit without a card | capture: sha256:355828a37eda57f0294651d2bc55e92d03320d4f4b85d41676840653e7c2cdea | quote: Pay-per-token with automatic credit deduction. Per-model pricing
- sources:
  - [1] https://docs.aiand.com/
