# Meituan LongCat API Platform

> longcat.chat | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/longcat/ | JSON https://fshy.ajam.dev/api/v1/entity/longcat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Meituan LongCat API Platform

- `inference/meituan-longcat-api` | paid-only | evidence documented | binding request-rate | category inference API, paid
- needs card no, phone yes, ID no, institution no | verified 2026-10-28T04:36:18.792Z (live) | stale on 2026-11-28
- url https://longcat.chat/platform
- free tier: no standing free allowance on the pages read: LongCat-2.0 and LongCat-2.5-Preview are pay-as-you-go from a prepaid balance at a limited-time discount of USD 0.30 per 1M uncached input and USD 1.20 per 1M output. Six LongCat-Flash models were retired effective May 29, 2026. LongCat-2.0-Preview was announced with an initial quota of 5,000,000 Tokens/day, and billing for LongCat-2.0 was announced on 2026-06-30. Promotional credits exist and are consumed before the paid balance, but how a new account obtains one is not stated | unit: none | metered on: none | read on: 2026-10-28 | source: [1] | note: no-standing-free-allowance
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: outside mainland China an account registers with a mobile phone number or an email. The international-site FAQ states no identity verification is required to recharge or use the service. Mainland China accounts must complete identity verification (real name and ID number) or enterprise verification before recharging or buying token packs
- interface: rest
- limits:
  - request-rate (binding): limits are enforced per API key and exceeding them returns HTTP 429; no requests-per-minute figure is published on the pages read [2]
- binding note: per-key request limit with a 429 response; the prepaid balance is the other gate
- endpoint: https://api.longcat.chat/openai
- tooling: OpenAI-compatible POST /v1/chat/completions on https://api.longcat.chat/openai and Anthropic-compatible POST /v1/messages on https://api.longcat.chat/anthropic
- composes with: pairs with an agent as a 1M-context pay-as-you-go model; the six LongCat-Flash models of the earlier API launch are retired
- reliability: six LongCat-Flash models were retired effective May 29, 2026 and the changelog announces LongCat-2.0 billing on 2026-06-30
- notes: a one-time free grant for new accounts is unverified; the first-party pages read state no free grant
- evidence note: pricing and retirement are read from the vendor docs; whether a new-account promotional credit is granted is unverified
- evidence:
  - [3] 2026-10-28: the platform exposes an OpenAI-compatible chat completions endpoint | capture: sha256:3e520f3655465af2b5379e55e6cee73f2e51578d7f53e5e999e9e2160cfe95e9 | quote: Fully compatible with the OpenAI API specification, supporting the following endpoints:
  - [2] 2026-10-28: registration outside mainland China is by phone or email | capture: sha256:b4bc67c2cf20921428adc79a027897e13fdc7f5a75d51efc26daadad53fd804e | quote: Users in Mainland China can register/login using their mobile phone number. Users outside Mainland China can register/login using either their mobile phone number or email.
  - [2] 2026-10-28: mainland accounts need identity or enterprise verification before recharging | capture: sha256:b4bc67c2cf20921428adc79a027897e13fdc7f5a75d51efc26daadad53fd804e | quote: Users in Mainland China are required to complete Identity Verification or Enterprise Verification before recharging or purchasing Token Packs.
  - [2] 2026-10-28: the international-site FAQ requires no identity verification to recharge or use the service | capture: sha256:b4bc67c2cf20921428adc79a027897e13fdc7f5a75d51efc26daadad53fd804e | quote: A: No Identity Verification is required — recharging and using the service do not mandate verification.
  - [2] 2026-10-28: rate limits are per API key and return 429 | capture: sha256:b4bc67c2cf20921428adc79a027897e13fdc7f5a75d51efc26daadad53fd804e | quote: Yes, rate limits are enforced per API Key. When exceeded, you'll receive a 429 status code.
  - [1] 2026-10-28: only two models are sold, both pay-as-you-go | capture: sha256:627907d8e085f81dd796ac0697c0a2756c303b3222d68b7a66dcc9f6f2d5351c | quote: Pay-As-You-Go currently supports LongCat-2.5-Preview and LongCat-2.0.
  - [1] 2026-10-28: limited-time discounted uncached input price per 1M tokens in USD | capture: sha256:627907d8e085f81dd796ac0697c0a2756c303b3222d68b7a66dcc9f6f2d5351c | quote: | Uncached Input | $0.30 |
  - [1] 2026-10-28: promotional credits exist and are consumed first; the paid balance does not expire | capture: sha256:627907d8e085f81dd796ac0697c0a2756c303b3222d68b7a66dcc9f6f2d5351c | quote: Your balance never expires. If you also have promotional credits, those are consumed before your paid balance.
  - [4] 2026-10-28: six LongCat-Flash models were retired effective May 29, 2026 | capture: sha256:b60dc7d7e7ab8a227dc5dbd7fc2b1f228cef0c6cf5b2436c8d62f96fa93f365f | quote: Effective May 29, 2026, the platform will retire the following 6 models:
  - [4] 2026-10-28: LongCat-2.0-Preview was announced with an initial daily token quota | capture: sha256:b60dc7d7e7ab8a227dc5dbd7fc2b1f228cef0c6cf5b2436c8d62f96fa93f365f | quote: With an initial quota of 5,000,000 Tokens/day, you can [submit model feedback](https://longcat.chat/platform/feedback).
  - [4] 2026-10-28: the changelog entry for 2026-06-30 announces LongCat-2.0 release and billing | capture: sha256:b60dc7d7e7ab8a227dc5dbd7fc2b1f228cef0c6cf5b2436c8d62f96fa93f365f | quote: ### LongCat-2.0 Release & Billing Now Available
- sources:
  - [1] https://longcat.chat/platform/docs/api-pay-as-you-go
  - [2] https://longcat.chat/platform/docs/faq
  - [3] https://longcat.chat/platform/docs/
  - [4] https://longcat.chat/platform/docs/change-log
