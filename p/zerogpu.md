# ZeroGPU

> zerogpu.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zerogpu/ | JSON https://fshy.ajam.dev/api/v1/entity/zerogpu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZeroGPU

- `inference/zerogpu` | paid-only | evidence documented | binding volume-quota | category inference gateway
- needs card no, phone no, ID no, institution no | verified 2026-11-18T14:35:09.000Z (live) | stale on 2026-12-19
- url https://docs.zerogpu.ai/docs/model-catalog
- free tier: The Model Catalog lets you browse every available ZeroGPU model and compare pricing across the tasks you care about. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: log into the dashboard to obtain an API key; no free signup credit stated
- interface: rest
- limits:
  - volume-quota (binding): per-token prices, for example USD 0.02 input and USD 0.10 output per 1M tokens on gpt-oss-20b [1]
- endpoint: https://api.zerogpu.ai/v1
- composes with: No free text inference allowance is published in the captured model catalog or quickstart.
- reliability: 403 for an invalid or revoked key; 401 if no key is sent
- notes: the same as composes with
- evidence:
  - [1] 2026-11-18: ZeroGPU publishes per-token prices for its model catalog with no free inference tier stated | capture: sha256:dfd760fa9204b78f9d2eb83ee206761b8f374a78c07bf177597dc48ef6e8b157 | quote: The Model Catalog lets you browse every available ZeroGPU model and compare pricing across the tasks you care about.
- sources:
  - [1] https://docs.zerogpu.ai/docs/model-catalog
