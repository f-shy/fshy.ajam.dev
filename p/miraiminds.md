# Frequency

> miraiminds.co | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/miraiminds/ | JSON https://fshy.ajam.dev/api/v1/entity/miraiminds.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Frequency

- `inference/frequency` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:30:00.000Z (live) | stale on 2026-12-19
- url https://docs.miraiminds.co/v2/llm
- free tier: No free allowance is stated. The mira-llm model is priced at INR 15 input, INR 9.30 cached input and INR 55 output per million tokens, charged to a workspace wallet. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: create a key in the sandbox console Developers page with a first-time email check; production requires going live
- interface: rest
- limits:
  - volume-quota (binding): INR 15 input, INR 9.30 cached input, INR 55 output per million tokens [1]
  - request-rate: 16 requests running at once per workspace; 100 messages and 16,000 characters per request [1]
- endpoint: https://llm.scalefrequency.com/v2
- tooling: an OpenAI-compatible POST /v2/chat/completions (and /v1) with an sk_live_ key, plus SDK examples
- composes with: the per-token INR charge and workspace wallet top-up are the scarce links; no free tier is published
- reliability: a workspace that has not gone live gets 403 on the production address; an empty wallet returns 402 until funds are added
- notes: no standing free inference allowance is published; usage is charged per million tokens to the workspace wallet
- evidence:
  - [1] 2026-11-18: the mira-llm language model is billed per million tokens in INR with wallet charging; no free allowance is stated | capture: sha256:14e2c4cb5f6a62603e1558c162652ae055743a62db7be873392965eb8405a2b3 | quote: ₹15 input, ₹9.30 cached input, ₹55 output per 1,000,000 tokens
- sources:
  - [1] https://docs.miraiminds.co/v2/llm
