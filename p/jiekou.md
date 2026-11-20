# Jiekou.AI

> jiekou.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jiekou/ | JSON https://fshy.ajam.dev/api/v1/entity/jiekou.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Jiekou.AI

- `inference/jiekou` | paid-only | evidence documented | binding write-gated | category inference gateway
- needs card yes, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.jiekou.ai/docs/support/quickstart
- free tier: No free allowance is stated on the quickstart read 2026-11-18: the account balance must be non-zero before the service can be used, and a top-up is recommended. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: card | detail: login via Google, GitHub or email, then a funded balance before API calls
- interface: rest
- limits:
  - volume-quota: account balance must be non-zero; top-up via the billing page [1]
  - write-gated (binding): the binding constraint named on the first-party page [1]
- endpoint: https://api.jiekou.ai/openai
- tooling: a Bearer API key created in the account after login via Google, GitHub or email
- composes with: the non-zero balance prerequisite is the scarce link; no free text tier is published
- reliability: auto top-up is recommended to avoid interruption when the balance runs out
- evidence:
  - [1] 2026-11-18: a non-zero account balance is required to use the service | capture: sha256:57c80729d3e5f2d210aae14577cdbe80f9fa4082b8161eabbfc6c3d75f7edd07 | quote: 使用接口AI的服务需要账户中余额不为0
- sources:
  - [1] https://docs.jiekou.ai/docs/support/quickstart
