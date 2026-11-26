# NEAR AI Cloud

> near.ai | Compute, Inference; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/near/ | JSON https://fshy.ajam.dev/api/v1/entity/near.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NEAR AI Cloud (Compute)

- `compute/near-ai-cloud` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:17:31.402Z (live) | stale on 2026-12-26
- url https://near.ai/pricing
- free tier: Attested TEE inference on open-weight models, 'pay per token, with no minimums or subscriptions', from USD 0.04 input and USD 1.35 output per 1M tokens on Qwen 3.8 27B, up to USD 3.30 input and USD 16.50 output on Kimi K3. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email
- interface: rest
- limits:
  - volume-quota (binding): No free allowance is published; every token is billed, so the first limit is the account balance. [1]
- limits note: No free allowance is published; every token is billed, so the first limit is the account balance.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At USD 0.04 per 1M input tokens NEAR undercuts most centralized hosts for bulk document work, so it composes with a pipeline that is input-heavy and output-light; output at USD 1.35 per 1M is the expensive half.
- reliability: no reliability event recorded
- notes: Whether a new account receives trial credit behind cloud.near.ai/signin was not established; the pricing page states no free allowance. Token rates come from the vendor's own catalog read on 2026-10-22.
- extras:
  - facets.class: paid-cloud
- evidence:
  - [1] 2026-10-22: per-model table of input and output USD per 1M tokens, 'No minimums, no subscriptions', rates 'Last updated 2026-10-22'
  - [2] 2026-10-22: TEE-hosted open-weight models, hardware-signed attestation on every response, OpenAI-compatible API
  - [1] 2026-11-25: the cheapest listed model is billed at USD 0.04 input and USD 1.35 output per 1M tokens | capture: sha256:e927a37e3c9078c4e0ca500147abf35488ecd8e5a1daba62d83737b54bc0ffca | quote: | Qwen 3.8 27B | Private TEE | Qwen/Qwen3.8-27B | 262K | $0.04 | $1.35 |
- sources:
  - [1] https://near.ai/pricing
  - [2] https://near.ai/

## NEAR AI Cloud (nearai)

- `inference/nearai` | paid-only | evidence documented | binding volume-quota | category private inference cloud, prepaid credits
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-19
- url https://docs.near.ai/cloud/quickstart
- free tier: no free tier stated: the quickstart instructs users to create an account, purchase credits, and generate an API key; models run in TEEs | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account at cloud.near.ai and an API key are required; credits must be purchased; signup fields not stated on the quickstart page
- interface: rest
- limits:
  - volume-quota (binding): credits must be purchased before use; no free allowance is stated on the quickstart page [1]
- binding note: no free allowance, so purchased credits bind first
- endpoint: https://cloud-api.near.ai/v1
- tooling: an OpenAI-compatible key at cloud-api.near.ai/v1
- composes with: pairs with an OpenAI-compatible agent through a purchased-credit key
- reliability: no reliability event recorded
- notes: TEE-hosted private inference with top-up or pay-as-you-go; no free offer appears on the captured pages.
- evidence:
  - [1] 2026-11-18: credits must be purchased before inference use | capture: sha256:35908eb81f2f4f70bfa24d280afe9408ba4d1442fabbb90e80db9852950e4ba0 | quote: 1. Create your account - Sign up at [cloud.near.ai](https://cloud.near.ai/) 2. Add Credits - Go to the "Credits" section and purchase credits based on your needs 3. Generate API Key - Go to the "API Keys" section and generate a new key
- sources:
  - [1] https://docs.near.ai/cloud/quickstart
