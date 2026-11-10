# iFlow API

> iflow.cn | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iflow/ | JSON https://fshy.ajam.dev/api/v1/entity/iflow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iFlow API (platform.iflow.cn)

- `inference/iflow-api` | dead | evidence documented | binding none | category inference API, closed
- identity a placeholder: card and phone unknown | verified 2026-10-28T04:36:18.792Z (live) | stale on 2026-11-28
- url https://platform.iflow.cn/
- free tier: none: the vendor notice dated March 20, 2026 says the iFlow API service and model library close on April 17, 2026 together with iFlow CLI | unit: none | metered on: none | read on: 2026-10-28 | source: [1] | note: service-closed
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: unverified: the service is closed and the sign-up requirement was not read
- interface: rest
- tooling: not stated
- composes with: closed; the vendor notice points users to Qoder
- reliability: closed on April 17, 2026 per the vendor notice; no request was sent after that date
- evidence note: the closure is the vendor's own announcement of the shutdown date; the closed state was not probed
- evidence:
  - [1] 2026-10-28: iFlow CLI closes on April 17 and the iFlow API service and model library close with it | capture: sha256:60b6ac7bf89bf0d189f8d4c0aa738300767cc359d14c2339dd857b19d598641e | quote: iFlow CLI 产品将于 2026 年 3 月 20 日 起停止维护，并于 4 月 17 日 正式关闭，iFlow API 服务、模型库 将同步关停
  - [1] 2026-10-28: the FAQ confirms the API service and model library close on April 17, 2026 | capture: sha256:60b6ac7bf89bf0d189f8d4c0aa738300767cc359d14c2339dd857b19d598641e | quote: 是的，iFlow API 服务和模型库将于 2026 年 4 月 17 日同步关闭，请您提前做好迁移工作。
  - [2] 2026-10-28: the README announces iFlow CLI shutting down on April 17, 2026 | capture: sha256:ca22d3fb75ca38b1ad4b2756c9e4a8a42a5b1f709f7a1ed261514a3ef72f20dc | quote: iFlow CLI will be shutting down on April 17, 2026 (UTC+8).
  - [1] 2026-10-28: the farewell post says iFlow CLI stops maintenance on 2026-03-20 and closes on 04-17, and the iFlow API service and model library shut down at the same time | capture: sha256:60b6ac7bf89bf0d189f8d4c0aa738300767cc359d14c2339dd857b19d598641e | quote: iFlow CLI 产品将于 2026 年 3 月 20 日 起停止维护，并于 4 月 17 日 正式关闭，iFlow API 服务、模型库 将同步关停
  - [2] 2026-10-28: the former offer was free access to Kimi K2, Qwen3 Coder and DeepSeek v3 through the iFlow open platform | capture: sha256:ca22d3fb75ca38b1ad4b2756c9e4a8a42a5b1f709f7a1ed261514a3ef72f20dc | quote: 1. Free AI Models: Access powerful and free AI models through the [iFlow open platform](https://platform.iflow.cn/docs/api-mode), including Kimi K2, Qwen3 Coder, DeepSeek v3, and more
  - [3] 2026-10-28: platform.iflow.cn now describes search results for models, returned as Markdown or JSON | capture: sha256:28c9a7f5bce74f987bfa2e9cf77f2686663ea799011c15ae44f3dfbf39bd716b | quote: 我们提供Markdown、Json格式，让模型能够更加准确理解搜索结果
  - [2] 2026-10-28: an API key came from an iFlow account | capture: sha256:ca22d3fb75ca38b1ad4b2756c9e4a8a42a5b1f709f7a1ed261514a3ef72f20dc | quote: To get your API key: 1. Register for an iFlow account
- sources:
  - [1] https://vibex.iflow.cn/t/topic/4819
  - [2] https://github.com/iflow-ai/iflow-cli
  - [3] https://platform.iflow.cn/
