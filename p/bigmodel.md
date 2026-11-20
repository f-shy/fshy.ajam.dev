# Zhipu AI

> bigmodel.cn | Inference, Coding subscriptions, Compute; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bigmodel/ | JSON https://fshy.ajam.dev/api/v1/entity/bigmodel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Zhipu AI

- `inference/zhipuai` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://docs.bigmodel.cn/cn/guide/start/pricing
- free tier: Several models are priced 免费 (free) in the CNY pricing table, e.g. 'GLM-4.7-Flash | 200K | 免费 | 免费 | 限时免费 | 免费' and 'GLM-4-Flash-250414 | 128K | 免费 | 免费 | 限时免费 | 不支持'. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: an account and API key from BigModel; no card or phone gate stated on this page
- interface: rest
- limits:
  - volume-quota (binding): GLM-4.7-Flash, GLM-4-Flash-250414 etc priced 免费 per 1M tokens [1]
  - volume-quota (binding): cache storage 限时免费 (limited-time free) [1]
- endpoint: https://open.bigmodel.cn/api/paas/v4
- tooling: OpenAI-compatible client against open.bigmodel.cn/api/paas/v4
- composes with: the free Flash models are the scarce link; quotas for them are not stated on this page
- reliability: free status is a listed price, not a quota; cache storage is only limited-time free
- notes: Free-priced models are documented but no numeric quota is published; this is the China platform.
- evidence:
  - [1] 2026-11-18: several models have free (免费) input/output prices per 1M tokens | capture: sha256:10ecdd8a20cc14b2563bd3b20cdc3abf0c7e1f62f4bed4df694dad9f612072e5 | quote: GLM-4.7-Flash | 200K | 免费 | 免费 | 限时免费 | 免费
- sources:
  - [1] https://docs.bigmodel.cn/cn/guide/start/pricing

## Zhipu BigModel Open Platform (bigmodel.cn)

- `inference/zhipu-bigmodel-open-platform` | qualifies-with-caveat | evidence documented | binding request-rate | category inference API, free models
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T05:36:15.599Z (live) | stale on 2026-12-19
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
- interface detail: OpenAI Chat Completions compatible. The platform is served by the first-party Zhipu inference API, with chat at POST https://open.bigmodel.cn/api/paas/v4/chat/completions and models at GET https://open.bigmodel.cn/api/paas/v4/models; auth is a bearer key in Authorization: Bearer YOUR_API_KEY, created on the API Keys page after sign-in, with a JWT Token scheme also documented. GLM Coding Plan uses separate base URLs and separate keys.
- endpoint: https://open.bigmodel.cn/api/paas/v4/
- tooling: any OpenAI SDK with base URL https://open.bigmodel.cn/api/paas/v4/; curl against POST https://open.bigmodel.cn/api/paas/v4/chat/completions with Authorization: Bearer YOUR_API_KEY.
- composes with: a free 200K-context text model and a free vision model are a zero-cost first pass in a two-stage pipeline; only the survivors go to a metered model
- reliability: not assessed: no request was sent to the endpoint
- notes: a keyless GET or POST to the chat route returns HTTP 401 with body {"error":{"code":"1001","message":"Header中未收到Authorization参数，无法进行身份验证。"}}, and a POST with an invalid bearer token returns HTTP 401 with body {"error":{"code":"401","message":"令牌已过期或验证不正确"}}. On 2026-11-18 two keyless POSTs returned HTTP 401 code 1001, so the route is live and needs a key.
- evidence note: the endpoint, routes and bearer scheme come from first-party docs pages and first-party OpenAPI specs; a keyless request returned HTTP 401 as expected. The key, account quota and per-model concurrency remain unverified behind a sign-up.
- probe:
  - records[0].probe_id: zhipu-bigmodel-open-platform-20261118
  - records[0].target: https://open.bigmodel.cn/api/paas/v4/chat/completions
  - records[0].runs[0].label: run1
  - records[0].runs[0].probed_at: 2026-11-18T05:26:29.953Z
  - records[0].runs[0].status: 401
  - records[0].runs[0].completion: no
  - records[0].runs[0].capture: sha256:16c5a0c733d623908ccbb303b3b335700aa191e50ec3bb362bf5fdb65712d540
  - records[0].runs[1].label: run2
  - records[0].runs[1].probed_at: 2026-11-18T05:36:15.599Z
  - records[0].runs[1].status: 401
  - records[0].runs[1].completion: no
  - records[0].runs[1].capture: sha256:4047936b16dcdfc8f1d0d929127c56da92c17320635afd48a64a8030ec2e4dc8
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
  - [7] 2026-11-18: first-party general API base endpoint for bigmodel.cn | capture: sha256:754e47a07859e1235caabcadf7912f6cdc96c7c99e662baa6ad4b1e636840660 | quote: https://open.bigmodel.cn/api/paas/v4/
  - [8] 2026-11-18: first-party OpenAPI server URL and bearer security in the chat-completion API reference | capture: sha256:2f7e2b795c218899ff08cbd06dbbead757e15600464ebb4e6e9b1bafbe595ef4 | quote: servers: - url: https://open.bigmodel.cn/api/ description: 开放平台服务 security: - bearerAuth: []
  - [9] 2026-11-18: first-party POST chat URL, method and bearer auth header | capture: sha256:59c1c2a3980b19ae51f80a298c01a3cd81d04babb9ff88d0313fe20563ecdc6a | quote: curl -X POST "https://open.bigmodel.cn/api/paas/v4/chat/completions" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer YOUR_API_KEY" \
  - [10] 2026-11-18: server URL in the first-party English OpenAPI spec, which also defines POST /paas/v4/chat/completions and bearerAuth | capture: sha256:51f627346bcf5d68fed3be6a85582a79ddff123357ca3cbdfc84c2fb5c9f015f | quote: "servers": [{"url": "https://open.bigmodel.cn/api/", "description": "Open Platform Service"}]
  - [11] 2026-11-18: first-party table separates the GLM Coding Plan base URLs from the general inference endpoint | capture: sha256:b3aa7e2bacca16a6e748fc8ae658d12b9ff09738d759743a57a5004f01740afa | quote: | Anthropic Message 协议 | `https://open.bigmodel.cn/api/anthropic` | | OpenAI Chat Completion 协议 | `https://open.bigmodel.cn/api/coding/paas/v4` | | OpenAI Response 协议 | `https://open.bigmodel.cn/api/v1` |
  - probe:https://open.bigmodel.cn/api/paas/v4/chat/completions 2026-11-18: a keyless POST to https://open.bigmodel.cn/api/paas/v4/chat/completions for GLM-4.7-Flash returned HTTP 401 with body {'error':{'code':'1001','message':'Header中未收到Authorization参数，无法进行身份验证。'}} and no completion in 1480 ms Probe start 2026-11-18T05:26:29.953Z. | capture: sha256:16c5a0c733d623908ccbb303b3b335700aa191e50ec3bb362bf5fdb65712d540 | quote: a keyless POST to https://open.bigmodel.cn/api/paas/v4/chat/completions for GLM-4.7-Flash returned HTTP 401 with body {'error':{'code':'1001','message':'Header中未收到Authorization参数，无法进行身份验证。'}} and no completion in 1480 ms
  - probe:https://open.bigmodel.cn/api/paas/v4/chat/completions 2026-11-18: a keyless POST to https://open.bigmodel.cn/api/paas/v4/chat/completions for GLM-4.7-Flash returned HTTP 401 with body {'error':{'code':'1001','message':'Header中未收到Authorization参数，无法进行身份验证。'}} and no completion in 508 ms Probe start 2026-11-18T05:36:15.599Z. | capture: sha256:4047936b16dcdfc8f1d0d929127c56da92c17320635afd48a64a8030ec2e4dc8 | quote: a keyless POST to https://open.bigmodel.cn/api/paas/v4/chat/completions for GLM-4.7-Flash returned HTTP 401 with body {'error':{'code':'1001','message':'Header中未收到Authorization参数，无法进行身份验证。'}} and no completion in 508 ms
- sources:
  - [1] https://bigmodel.cn/pricing
  - [2] https://docs.bigmodel.cn/cn/api/rate-limit
  - [3] https://docs.bigmodel.cn/cn/faq/registration-login
  - [4] https://docs.bigmodel.cn/cn/faq/authentication-issues.md
  - [5] https://bigmodel.cn/login
  - [6] https://docs.bigmodel.cn/cn/guide/platform/equity-explain.md
  - [7] https://docs.bigmodel.cn/cn/guide/develop/http/introduction
  - [8] https://docs.bigmodel.cn/api-reference/%E6%A8%A1%E5%9E%8B-api/%E5%AF%B9%E8%AF%9D%E8%A1%A5%E5%85%A8.md
  - [9] https://docs.bigmodel.cn/cn/guide/start/quick-start
  - [10] https://docs.bigmodel.cn/openapi/openapi-en.json
  - [11] https://docs.bigmodel.cn/cn/coding-plan/quick-start.md

## Zhipu AI Coding Plan

- `coding-subs/zhipuai-coding-plan` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.bigmodel.cn/cn/coding-plan/overview
- free tier: No standing free tier. The GLM Coding Plan has paid Lite/Pro/Max tiers with 2,000/12,000/28,000 credits per 5 hours and 10,000/60,000/140,000 per week. An occasional 2,000-credit experience card (体验卡) ends when its credits are used. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: a BigModel/Zhipu account and a paid subscription; exact signup fields not enumerated on these pages
- interface: rest, cli
- limits:
  - volume-quota (binding): 2,000 to 28,000 credits per 5 hours by tier [1]
  - volume-quota (binding): 10,000 to 140,000 credits per week by tier [1]
  - request-rate: OpenClaw is served at lower priority with dynamic queuing under load [1]
- endpoint: https://open.bigmodel.cn/api/coding/paas/v4
- tooling: ZCode, AutoClaw, Claude Code, Codex, OpenCode and WorkBuddy are named
- composes with: the 5-hour and weekly credit caps are the scarce link; the plan key is separate from the standard API key and only works in approved tools
- reliability: plan credits cannot be used through the standard API, and account sharing can restrict the subscription
- notes: Paid-only. The '体验卡' experience card is a limited promotional grant, not a standing free tier; no price is invented.
- evidence:
  - [1] 2026-11-18: all tiers support GLM-5.3 and GLM-5.3-Flash and the plan is subscription-only | capture: sha256:65877ea7900a83164403722abe4543e6f45c2e59e012437a51e3f66498f77470 | quote: - 所有套餐均支持 GLM-5.3、GLM-5.3-Flash。
  - [2] 2026-11-18: an experience card is a limited 2,000-credit grant that ends when consumed | capture: sha256:07b8c223ec63dde4b027da13e4f87686b776310c256c46342c2239c5fef1f12b | quote: 每张体验卡包含 2,000 积分
- sources:
  - [1] https://docs.bigmodel.cn/cn/coding-plan/overview
  - [2] https://docs.bigmodel.cn/cn/coding-plan/faq

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
