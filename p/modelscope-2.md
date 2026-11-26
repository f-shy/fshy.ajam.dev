# ModelScope API-Inference

> modelscope.ai | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/modelscope-2/ | JSON https://fshy.ajam.dev/api/v1/entity/modelscope-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ModelScope API-Inference

- `inference/modelscope-api-inference` | fails-identity | evidence documented | binding request-rate | category inference API, free
- needs card no, phone yes, ID yes, institution no | verified 2026-11-03T11:30:33.178Z (live) | stale on 2026-12-04
- url https://www.modelscope.ai/docs/model-service/API-Inference/limits
- free tier: Free API access to selected open-source LLM, multimodal and text-to-image models, described as a non-commercial, non-profit product. Quota and concurrency are adjusted dynamically with platform load. Calls can be redeemed with Magicubes: about 0.5 per call for lightweight models, about 1 for standard and about 2 for flagship. A per-day call count is not stated on the page read | unit: requests | metered on: request-count | read on: 2026-10-28 | source: [1] | note: perpetual-free-allowance
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: national-id | detail: the ModelScope account must first bind to an Alibaba Cloud account that has completed real-name verification before API-Inference works normally. A ModelScope maintainer stated the binding is open only to Alibaba Cloud China-site accounts, not international-site accounts; a China-site account registers with a mainland China mobile number and individual verification needs an identity-verified personal Alipay account. The international site verifies by passport or driver's license, but its accounts are a separate system and are not accepted for the binding. unverified: whether the China-site Alipay verification accepts a non-mainland document
- interface: rest
- limits:
  - request-rate (binding): concurrency per model is limited dynamically by platform load, with normal single-concurrency use as the guiding principle; not for high-concurrency or SLA workloads [1]
  - volume-quota: 2000 API-Inference calls per day per registered user, as announced by the operator; the current limits page gives no daily figure and says quotas adjust dynamically with platform load [1]
  - volume-quota: per-model cap reported as 200 calls per day (100 for the largest DeepSeek models), within the daily total; the operator's current limits page gives no per-model figure and says limits adjust dynamically [2]
- binding note: dynamic per-model concurrency limits; a daily total of 2000 calls is announced but absent from the current limits page
- tooling: part of the free tier
- composes with: free open-model inference for experiments; the per-call Magicube cost is shown next to the provider in each model's code example
- reliability: older models are removed from API-Inference as new models are released
- evidence:
  - [1] 2026-10-28: API-Inference is offered free of charge to developers | capture: sha256:9b81bf0c672324cc38dfa6450b81b748282eb22b0de9f8d6c2b24215fc465047 | quote: offering them free of charge for developers to experience
  - [1] 2026-10-28: the Alibaba Cloud account bound to ModelScope must be real-name verified | capture: sha256:9b81bf0c672324cc38dfa6450b81b748282eb22b0de9f8d6c2b24215fc465047 | quote: Your ModelScope account must first bind to an Alibaba Cloud account. Additionally, to prevent abuse, the corresponding cloud account must have completed real-name verification before you can use API-Inference normally.
  - [1] 2026-10-28: not suitable for high-concurrency or SLA-bound workloads | capture: sha256:9b81bf0c672324cc38dfa6450b81b748282eb22b0de9f8d6c2b24215fc465047 | quote: Do not use it for online tasks requiring high concurrency and SLA guarantees.
  - [1] 2026-10-28: Magicube cost tiers per call | capture: sha256:9b81bf0c672324cc38dfa6450b81b748282eb22b0de9f8d6c2b24215fc465047 | quote: - Lightweight models: ~0.5 Magicubes per call
  - [1] 2026-10-28: older models are removed over time | capture: sha256:9b81bf0c672324cc38dfa6450b81b748282eb22b0de9f8d6c2b24215fc465047 | quote: As new models are released, older models may gradually be removed from API Inference.
  - [3] 2026-11-03: the operator announced free model inference with 2000 calls per day for registered users | capture: sha256:a3ac659346bfdf7da403e8477597c429a5ce7f60602ac917b3d773e35b969319 | quote: 开发者福利，魔搭推出免费模型推理API，注册就送每日2000次调用！
  - [2] 2026-11-03: a third party reports the operator's limits page, rendered in July 2026, giving 2,000 calls per day and 200 per model | capture: sha256:c513dc233cda2857815cbb6e4b30837ca55f71dacbdfa727d0d7c414e794cd9c | quote: Each registered ModelScope user is currently allowed a total of 2,000 API Inference calls per day, with a maximum of 200 calls per individual model.
  - [4] 2026-11-03: a ModelScope maintainer stated on 2025-10-14 that the Alibaba Cloud binding page accepts China-site accounts only, not international accounts | capture: sha256:757cfa52c726afa419d85c2c30239287eaec87370e7bb61eebca5185c5c7cce0 | quote: you would need to view the page in Chinese though, and it is currently only open to Alibaba Cloud cn-site's account, not the international account.
  - [5] 2026-11-03: a China-site account registers with a mainland China mobile number; an international-site account registers with an email and a non-mainland phone | capture: sha256:3c8b6f416f4fe9547579673ba0b70cf63182d7c917daf9d40eb90e6ea45f49e2 | quote: | **账号注册 ** | 需使用中国内地手机号注册。 | 需使用邮箱注册，并且需要中国内地以外（包含中国香港、中国澳门和中国台湾）的手机号进行安全验证。 |
  - [6] 2026-11-03: China-site individual identity verification requires a personal Alipay account that is itself identity-verified | capture: sha256:d9f27e357395c6d374e58c001f447197dd3b472faeedf0582a99c189aadc302e | quote: An active personal Alipay account that has completed identity verification.
  - [7] 2026-11-03: the international site verifies an individual by passport or driver's license, but that is a separate account system from the China site | capture: sha256:02c9fc9361501c7bd6484959eee9ed8eef776bd6f5e755b4b0ec4d6d004ba061 | quote: | Verification method | Passport or driver's license | Valid business document from the registration country/region |
  - [1] 2026-11-03: the bound Alibaba Cloud account must be real-name verified; page re-read unchanged | capture: sha256:9b81bf0c672324cc38dfa6450b81b748282eb22b0de9f8d6c2b24215fc465047 | quote: the corresponding cloud account must have completed real-name verification before you can use API-Inference normally.
- sources:
  - [1] https://www.modelscope.ai/docs/model-service/API-Inference/limits
  - [2] https://www.modelhubby.com/providers/modelscope/
  - [3] https://www.modelscope.cn/headlines/article/795
  - [4] https://github.com/modelscope/modelscope/issues/1524
  - [5] https://help.aliyun.com/zh/account/aliyun-vs-alibaba-cloud
  - [6] https://help.aliyun.com/en/account/verify-your-identity-individual-account
  - [7] https://www.alibabacloud.com/help/en/account/real-name-authentication/
