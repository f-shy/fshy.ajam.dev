# Parasail

> parasail.io | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/parasail/ | JSON https://fshy.ajam.dev/api/v1/entity/parasail.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Parasail

- `inference/parasail` | paid-only | evidence documented | binding request-rate | category inference endpoint, pay-per-token, card required
- needs card yes, phone no, ID no, institution no | verified 2026-10-28T04:36:19.314Z (live) | stale on 2026-11-28
- url https://www.parasail.io/
- free tier: No usable free allowance: 'To use models, create API keys, and access paid platform services, add a credit card. Without a card, you can still view the platform but can't use models or API keys.' A 'Serverless - Free' class limited to 5 requests per minute appears in the rate-limit table, and the pages read do not say how an account reaches it. | unit: none | metered on: unstated | read on: 2026-10-28 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: the billing documentation states a credit card must be added before models or API keys can be used; card data is processed by Stripe
- interface: rest
- limits:
  - request-rate (binding): Serverless - Free 5 requests per minute; Serverless - User 500 requests per minute; Enterprise unlimited; token limit not currently enforced on any of them [2]
  - volume-quota: usage is billed in arrears: the card is charged when accrued usage reaches USD 25, then the remainder at the end of the billing cycle [1]
- binding note: the card requirement is the gate (see identity); past it, the Free class allows 5 requests per minute and the User class 500
- endpoint: https://api.parasail.io/v1/chat/completions
- tooling: OpenAI-compatible REST at https://api.parasail.io/v1; any OpenAI SDK with a bearer key created at the dashboard
- composes with: pay-per-token open-model catalogue behind one OpenAI-compatible base URL; the card on file is the gate before any key works
- reliability: no reliability event recorded
- notes: The 'Serverless - Free' rate-limit row has no matching free-credit statement on the pages read.
- evidence note: documentation pages only; the 5 requests per minute class is a documented figure and not measured
- evidence:
  - [1] 2026-10-28: a credit card is required before any model or API key can be used | capture: sha256:65fe893d32634926cceb8605b554601422dff652a6c11cc6cc05b4765211149d | quote: To use models, create API keys, and access paid platform services, add a credit card. Without a card, you can still view the platform but can't use models or API keys.
  - [1] 2026-10-28: usage is billed in arrears with a charge at USD 25 accrued | capture: sha256:65fe893d32634926cceb8605b554601422dff652a6c11cc6cc05b4765211149d | quote: Parasail automatically charges your card after your organization's accrued usage reaches $25, then reconciles any remaining balance at the end of the billing cycle.
  - [2] 2026-10-28: the Free serverless class is limited to 5 requests per minute with no enforced token limit | capture: sha256:106da8f423d29e00bbc6a89ad3b7bb81942aa8f2cbc12f1ef0166c404889a88f | quote: | Serverless - Free | 5 | Not currently enforced |
  - [2] 2026-10-28: the User serverless class is limited to 500 requests per minute | capture: sha256:106da8f423d29e00bbc6a89ad3b7bb81942aa8f2cbc12f1ef0166c404889a88f | quote: | Serverless - User | 500 | Not currently enforced |
  - [3] 2026-10-28: the pricing table lists per-1M-token rates; gpt-oss-20b is USD 0.04 input, USD 0.20 output and USD 0.02 cache read | capture: sha256:1d258cbb6b716c29d0f436bbde0efe8f0655937cfc2ced772f16f3dbf314faa3 | quote: | gpt-oss-20b | $0.04 | $0.20 | $0.02 |
- sources:
  - [1] https://docs.parasail.io/parasail-docs/billing/pricing
  - [2] https://docs.parasail.io/parasail-docs/operate-in-production/limits-and-quotas
  - [3] https://parasail.io/pricing
