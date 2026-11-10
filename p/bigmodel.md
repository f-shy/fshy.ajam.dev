# Zhipu Z

> bigmodel.cn | Inference, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bigmodel/ | JSON https://fshy.ajam.dev/api/v1/entity/bigmodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zhipu BigModel Open Platform (bigmodel.cn)

- `inference/zhipu-bigmodel-open-platform` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API, free models
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T11:30:44.393Z (live) | stale on 2026-12-04
- url https://bigmodel.cn/pricing
- free tier: Two models are free on input, output and cache, with no token cap or expiry stated: the text model GLM-4.7-Flash (200K context) and the vision model GLM-4.6V-Flash. Concurrency per model is the only published constraint and the per-model figure sits behind a login | unit: unlimited | metered on: none | read on: 2026-10-28 | source: [1] | note: perpetual free models; the login page advertises a new-user experience pack of 20 million tokens (2000万); its model scope, expiry and any real-name condition are unverified: behind a…
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: registration accepts a non-mainland phone number: choose the country code and verify by SMS code. The FAQ states API calls do not require real-name authentication (it is recommended for account security, and is the route to an enterprise account); whether the API-key page asks for it is unverified: behind a sign-up
- interface: rest
- limits:
  - request-rate (binding): concurrency, the number of requests in flight at one moment, is capped per model and per user-rights tier (levels V0 to V3, raised by points that only cash-balance spending earns); the per-model figure for the free text model is on a login-gated page and is unverified [2]
- binding note: concurrency per model and per user-rights tier; platform-level throttling can apply at peak load
- tooling: not stated
- composes with: a free 200K-context text model and a free vision model are a zero-cost first pass in a two-stage pipeline; only the survivors go to a metered model
- reliability: not assessed: no request was sent to the endpoint
- notes: the international Z.ai site publishes its own free Flash models under a separate account system; this is the bigmodel.cn side
- evidence note: the free-model list is the pricing page's own FAQ answer and the authentication FAQ says API calls do not require real-name authentication; the per-model concurrency figure and the terms of the new-user pack are unverified: behind a sign-up
- evidence:
  - [1] 2026-10-28: the pricing page FAQ lists GLM-4.7-Flash as free on input, output and cache | capture: sha256:c22b2e59d56c54571fda1695d0638adfcac945d95211b50f9065fcabfa512824 | quote: 文本模型 GLM-4.7-Flash（200K上下文）：输入免费、输出免费、缓存免费
  - [1] 2026-10-28: the pricing page FAQ lists the vision model GLM-4.6V-Flash as free on input, output and cache | capture: sha256:c22b2e59d56c54571fda1695d0638adfcac945d95211b50f9065fcabfa512824 | quote: 视觉模型 GLM-4.6V-Flash：输入免费、输出免费、缓存免费
  - [3] 2026-10-28: registration accepts an overseas phone number chosen by country code and verified by SMS code | capture: sha256:4ee36090f3d32b773fdf9be22b77a510bcb3e37f4fe4c59df9f1e4d8e4d2a516 | quote: 智谱开放平台是支持海外手机号注册的。在注册过程中，请您选择相应的国家区号，并通过短信验证码进行验证，即可完成注册。
  - [2] 2026-10-28: rate limits are concurrency limits set independently per model | capture: sha256:7a2f1ffeaab37f6ddb8b18805eb22ae7f9b38e283e3dc0ffe7ca25f02d35254c | quote: 不同模型设有独立的并发限制
  - [4] 2026-11-03: the platform FAQ states API calls do not require real-name authentication, which it only recommends | capture: sha256:b528b52026e8a853e693ae1d9496aae8dfba75f0ebc325f7404c4d958f78fe0c | quote: 目前调用 API 并不强制要求实名认证，但为确保您的账户安全，我们建议您进行
  - [5] 2026-11-03: the login and registration page advertises a new-user experience pack of 2000万 (20 million) tokens | capture: sha256:c82d922cdba1777c24c15af8e5c30e0ff21a9575846ac6a01b838fdfb7a13358 | quote: 新用户免费赠送专享 2000万 tokens体验包！
  - [6] 2026-11-03: model concurrency entitlement depends on the user-rights tier, raised by points | capture: sha256:0c4528fffbc31285d82839ceb37d954649ba3f5f92f50d595d9bd12a4342d6d7 | quote: 开发者通过获取积分来提升用户权益等级。凭用户权益等级享受模型并发权益、智谱新产品体验、智谱平台服务等多项平台权益内容。
  - [6] 2026-11-03: spending gift-account balance does not earn tier points | capture: sha256:0c4528fffbc31285d82839ceb37d954649ba3f5f92f50d595d9bd12a4342d6d7 | quote: 需注意，赠金账户的余额消耗不会换算到积分内。
  - [2] 2026-11-03: the per-model rates are shown per account in the console rate-limits page, not in the public docs | capture: sha256:7a2f1ffeaab37f6ddb8b18805eb22ae7f9b38e283e3dc0ffe7ca25f02d35254c | quote: 可通过 速率限制 查看您的账户目前各模型可调用的速率
  - [1] 2026-11-03: the pricing page FAQ still lists GLM-4.7-Flash as free on input, output and cache | capture: sha256:2bc19e1dad8a4e0757132c8ed6495c0ee23a1f886687ce00ff8872f78897d428 | quote: 文本模型 GLM-4.7-Flash（200K上下文）：输入免费、输出免费、缓存免费
- sources:
  - [1] https://bigmodel.cn/pricing
  - [2] https://docs.bigmodel.cn/cn/api/rate-limit
  - [3] https://docs.bigmodel.cn/cn/faq/registration-login
  - [4] https://docs.bigmodel.cn/cn/faq/authentication-issues.md
  - [5] https://bigmodel.cn/login
  - [6] https://docs.bigmodel.cn/cn/guide/platform/equity-explain.md

## Zhipu Z Managed Agents

- `compute/zhipu` | paid-only | evidence documented | binding retention-clamped | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:26.000Z (live) | stale on 2026-11-22
- url https://docs.bigmodel.cn/cn/managed-agents/overview.md
- free tier: no free tier published: a managed-agent platform whose sessions emit an idle status when a round ends, with memory mountable across several sessions and cron creating new ones | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - retention-clamped (binding): a session emits status_idle when a round ends, so the platform knows when to stop; cron creates a new session on schedule [1]
  - per-object-cap: Memory mounts into several sessions and its changes are audited [1]
  - write-gated: no plan or price appears on the overview; billing is on a page this record does not cite [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the managed-agents overview was read on 2026-10-22 (Chinese) and documents the session lifecycle and the shared memory, with no plan or price in it. The billing page is not cited by this record, so no figure is asserted
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the platform emits session.status_idle at the end of a round, which is the signal a client can bill or stop on
  - free_tier_kind: none
  - reclassified_from: dead
  - ps.price: not stated on the overview
  - ps.durability: Memory mountable across sessions with audited changes
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the memory is kept
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '平台驱动循环；一轮结束后发出 session.status_idle' - the platform drives the loop and emits session.status_idle when a round ends - and 'Memory 可挂载到多个会话并审计变更；定时任务按 cron 自动创建新会话', quoted
- sources:
  - [1] https://docs.bigmodel.cn/cn/managed-agents/overview.md
