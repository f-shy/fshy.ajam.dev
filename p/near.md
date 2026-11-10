# NEAR AI Cloud

> near.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/near/ | JSON https://fshy.ajam.dev/api/v1/entity/near.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NEAR AI Cloud

- `compute/near-ai-cloud` | paid-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
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
- sources:
  - [1] https://near.ai/pricing
  - [2] https://near.ai/
