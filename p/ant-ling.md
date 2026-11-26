# Bailing

> ant-ling.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ant-ling/ | JSON https://fshy.ajam.dev/api/v1/entity/ant-ling.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bailing

- `inference/bailing` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://developer.ant-ling.com/zh-CN/docs
- free tier: No self-serve free API allowance stated on the captured docs; an OpenAI-compatible API exists and the docs point to a separate model-and-pricing page. | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: register an account and obtain a token before the first call; account fields not detailed
- interface: rest, browser
- limits:
  - volume-quota (binding): free API quota not stated in the captured docs [1]
- endpoint: https://api.ant-ling.com/v1
- tooling: OpenAI SDK or HTTP against api.ant-ling.com/v1/chat/completions
- composes with: no documented free API quota; the online chat experience is a separate product
- reliability: pricing and rate limits are on a separate page that returned no content
- notes: No published self-serve text free allowance found via the docs or pricing route; pricing page captured no data.
- evidence:
  - [1] 2026-11-18: the platform offers an OpenAI-compatible API after registration | capture: sha256:62fd5415f7c4dc1009a6e0862549fd6612024972ee7687608fca681a339d9645 | quote: 注册账号并获取令牌，完成首次调用前的环境配置。
  - [2] 2026-11-18: the API is OpenAI-compatible at the given base URL | capture: sha256:2f8529c27c35b85dd6f9664c85310d2c2e38e8e9eaa36f1e92eb27cd4cb01c39 | quote: 你可以直接使用 OpenAI SDK 接入蚂蚁百灵 API，或通过 HTTP 请求进行标准调用，实现无缝迁移。
- sources:
  - [1] https://developer.ant-ling.com/zh-CN/docs
  - [2] https://developer.ant-ling.com/zh-CN/docs/getting-started/quickstart/
