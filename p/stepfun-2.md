# StepFun

> stepfun.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stepfun-2/ | JSON https://fshy.ajam.dev/api/v1/entity/stepfun-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StepFun (China)

- `inference/stepfun` | paid-only | evidence documented | binding request-rate | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://platform.stepfun.com/docs/zh/overview/concept
- free tier: No free text allowance stated; the Chinese concept page documents RPM, TPM and concurrency rate limits but no free quota. | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key; signup fields not detailed on the concept page
- interface: rest
- limits:
  - request-rate (binding): RPM, TPM and concurrency limits [1]
- endpoint: https://api.stepfun.com/v1
- tooling: OpenAI-compatible client against the StepFun China API
- composes with: no documented free tier; rate limits apply once an account has quota
- reliability: any one of RPM, TPM or concurrency can trigger a limit first
- notes: No free tier on the captured concept page; the pricing route returned no content.
- evidence:
  - [1] 2026-11-18: rate limits are expressed as RPM, TPM and concurrency | capture: sha256:cbdc12179d9ff6d7fdebb56eac4a1a4d75cb444d0303af1f20fc418ba9cb4d0d | quote: RPM (每分钟请求数)**: RPM 限制是基于时间的，它规定了用户在一分钟内可以发起的请求数量。
- sources:
  - [1] https://platform.stepfun.com/docs/zh/overview/concept
