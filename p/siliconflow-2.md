# SiliconFlow

> siliconflow.cn | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/siliconflow-2/ | JSON https://fshy.ajam.dev/api/v1/entity/siliconflow-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SiliconFlow (China)

- `inference/siliconflow-cn` | paid-only | evidence unverified | binding none | category inference endpoint, pay-as-you-go
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:45:48.000Z (live) | stale on 2026-12-03
- url https://www.siliconflow.cn/
- free tier: unverified: the first-party apex pages say Get Started for Free but the models page required a capture that was not obtainable; no free-token quota is verified on the pages read | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account at cloud.siliconflow.com and an API key are implied by the call to action; signup fields not stated on the apex pages
- interface: rest
- binding note: no quota could be verified on the captured pages
- endpoint: https://api.siliconflow.cn/v1
- tooling: an OpenAI-compatible key against the SiliconFlow API
- composes with: pairs with an OpenAI-compatible agent through a key; no free allowance is verified on the pages read
- reliability: no reliability event recorded
- notes: recorded to preserve the name; a free allowance is not established. The two ids share the same doc URL but different API bases (com vs cn).
- evidence note: the China apex is a hardware and solutions page that states no free inference offer, and the models page returned origin refusal, so no quota is verified
- evidence:
  - [1] 2026-11-18: the China apex is an enterprise hardware and solutions pitch with no free inference offer | capture: sha256:9eb0e00e18edf6cf5dfd77e85a5c29a24abbd43e87b004a90a6524b10891e148 | quote: ### AI 硬件
- sources:
  - [1] https://www.siliconflow.cn/
