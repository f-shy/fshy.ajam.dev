# Alibaba

> aliyun.com | Inference, Storage, Compute, Coding subscriptions; 8 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/aliyun/ | JSON https://fshy.ajam.dev/api/v1/entity/aliyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Alibaba

- `inference/alibaba` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://help.aliyun.com/zh/model-studio/new-free-quota
- free tier: New-user free quota: each eligible model typically gets 1,000,000 tokens, valid for 90 days, only in the China (Beijing) region; real-name verification is required. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: real-name verification required before the free quota is issued | country: CN
- interface: rest
- limits:
  - volume-quota (binding): typically 1,000,000 tokens per model, 90-day validity [1]
  - write-gated: real-name verification required; only China (Beijing) region eligible [1]
- endpoint: https://dashscope-intl.aliyuncs.com/compatible-mode/v1
- tooling: OpenAI-compatible SDK against the Model Studio compatible-mode endpoint
- composes with: the 90-day expiry and the Beijing-region-only rule bound the allowance
- reliability: free quota expires in 90 days, cannot be reissued, and is not valid outside the Beijing region
- notes: The global/international endpoint is not covered by the Beijing-only free quota; the China record shares the same source.
- evidence:
  - [1] 2026-11-18: each model gets a typical 1,000,000 token free quota with 90-day validity | capture: sha256:2b7f47e566f8d0eb8a12033a5d62bf2372856f7ba55e067eff1e06002c540632 | quote: 每个模型均有独立的免费额度（通常为 100 万 Token），不能跨模型合并或转移使用。
  - [1] 2026-11-18: free quota is valid for 90 days | capture: sha256:2b7f47e566f8d0eb8a12033a5d62bf2372856f7ba55e067eff1e06002c540632 | quote: 免费额度的有效期为 90 天，从开通阿里云百炼、模型发布或模型申请通过之日起计算（以较晚者为准）。
- sources:
  - [1] https://help.aliyun.com/zh/model-studio/new-free-quota

## Alibaba (China)

- `inference/alibaba-cn` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API
- needs card no, phone no, ID no, institution yes | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://help.aliyun.com/zh/model-studio/new-free-quota
- free tier: New-user free quota: each eligible model typically gets 1,000,000 tokens, valid for 90 days, only in the China (Beijing) region; real-name verification is required. | unit: tokens | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: institution | detail: real-name verification required before the free quota is issued | country: CN
- interface: rest
- limits:
  - volume-quota (binding): typically 1,000,000 tokens per model, 90-day validity [1]
  - write-gated: real-name verification required [1]
- endpoint: https://dashscope.aliyuncs.com/compatible-mode/v1
- tooling: OpenAI-compatible SDK against the DashScope compatible-mode endpoint
- composes with: the 90-day expiry and the Beijing-region-only rule bound the allowance
- reliability: free quota expires in 90 days and cannot be reissued after re-registration under the same real-name identity
- notes: record for the Alibaba (China) offer; verdict qualifies-with-caveat, confidence documented
- evidence:
  - [1] 2026-11-18: each model gets a typical 1,000,000 token free quota | capture: sha256:2b7f47e566f8d0eb8a12033a5d62bf2372856f7ba55e067eff1e06002c540632 | quote: 每个模型均有独立的免费额度（通常为 100 万 Token），不能跨模型合并或转移使用。
- sources:
  - [1] https://help.aliyun.com/zh/model-studio/new-free-quota

## Alibaba Bailian / DashScope File API (QwenCloud SG)

- `storage/alibaba-bailian-dashscope-file-api` | qualifies-with-caveat | evidence reported | binding per-object-cap | category Chinese LLM platform /v1/files
- needs card unknown, phone yes, ID no, institution no | verified 2026-11-19T21:12:57.317Z (live) | stale on 2026-12-04
- url https://help.aliyun.com/zh/model-studio/openai-file-interface
- free tier: 100 GB total per workspace and 10,000 files, with no stated expiry: '百炼存储空间支持的最大文件数为10000个，总大小不超过100 GB，暂时没有有效期限制。' Per file: 150 MB for purpose=file-extract and 500 MB for purpose=batch. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Per-file: 150 MB | bytes: 150000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No metered egress on file retrieval. The legacy get-file endpoint returns a pre-signed aliyuncs.com OSS URL, i.e. served from Alibaba OSS rather than a billed gateway. | metered: yes
- identity: any-phone | detail: an email address plus a mobile number from outside the Chinese mainland, for security verification, on the international site; real-name verification is required only to use Chinese-mainland resources or to apply for a credit line, and whether a card is asked for was not read.
- interface: unknown
- limits:
  - write-gated: review status (`checking` -> `available`/`rejected`) before they can be referenced [1]
  - per-object-cap (binding): Per-file: 150 MB [1]
- limits note: per-object-cap 150 MB (file-extract) / 500 MB (batch). 100 GB workspace byte cap and 10,000-file count cap, whichever hits first. Files enter a safety-review status (`checking` -> `available`/`rejected`) before they can be referenced.
- interface detail: OpenAI-compatible: base_url https://dashscope.aliyuncs.com/compatible-mode/v1 with the openai SDK; also https://dashscope-intl.aliyuncs.com for international, and https://maas.qwencloudapi.com/compatible-mode/v1 for the Singapore QwenCloud brand
- tooling: openai-python with a swapped base_url; curl multipart; documented endpoints upload/retrieve/list/delete plus GET /files/{file_id}/content
- composes with: 100 GB per workspace, and workspaces are a creatable dimension. 'Never expire' is the whole point: this is the only major /v1/files endpoint found that gives permanent retention on the free tier. At 500 MB/batch file, 10,000 files = 5 TB of nominal slots against a 100 GB byte wall. The byte wall binds.
- reliability: TWO CONTRADICTORY READ PATHS depending on which generation of the API you use. The NEW Agent Studio `GET /files/{file_id}/content` documents 'only files with downloadable=true can be downloaded; files uploaded directly or copied into a session sandbox are downloadable=false and return 400'. A read gate. The file-list example on the same doc set literally shows `"downloadable": false` on a directly uploaded CSV. But the LEGACY `GET /api/v1/files/{file_id}` returns a signed OSS `url` in the metadata, which is a real read path. The docs say the legacy interface is 'mainly for compatibility with historical scenarios', so its survival is not guaranteed. Probe the legacy path before relying on it. Alibaba Cloud international registration is email + mobile (any-phone); Chinese-mainland identity verification (passport/driver's licence) is only required for products deployed in mainland China.
- notes: 100 GB total per workspace; 10,000 files; NO expiry ('暂时没有有效期限制'. No validity-period limit for now). Per-file: 150 MB for purpose=file-extract, 500 MB for purpose=batch, 300 MB for fine-tune, 50 MB for the newer Agent Studio endpoint.
- evidence:
  - [1] 2026-10-21: '百炼存储空间支持的最大文件数为10000个，总大小不超过100 GB，暂时没有有效期限制' (10,000 files, 100 GB, no expiry); '单个文件最大为 150 MB' for file-extract; batch 500 MB
  - [2] 2026-10-21: 'You can store up to 10,000 files and 100 GB total. Files never expire.' — the Singapore/international wording of the same product
  - [3] 2026-10-21: '仅 downloadable 为 true 的文件可下载；当前接口直传与会话沙箱拷贝的文件 downloadable 均为 false，调用会返回 400'
  - [4] 2026-10-21: response example shows `"downloadable": false`
  - [5] 2026-10-21: legacy GET returns `"url": "http://xxxxx.oss-cn-hangzhou.aliyuncs.com/oss%3A//dashscope-pre/...&Signature=..."` (signed OSS URL)
  - [6] 2026-10-21: international site 'Requires an email address for registration, plus a mobile'
  - [7] 2026-10-21: PROBE: curl -D - -> 401, content-length 228; https://dashscope-intl.aliyuncs.com/api/v1/files/abc/content -> 401, 109 bytes; https://maas.qwencloudapi.com/compatible-mode/v1/files -> 401, 228 — all three live
  - [6] 2026-11-01: the international site registers with an email address and a mobile number from outside the Chinese mainland | capture: sha256:93a46222b5dfbd4250e93409aab9ab71046f8e0b31170aa6f9ce604ef62add4f | quote: Requires an email address for registration, plus a mobile number from outside the Chinese mainland (including Hong Kong (China), Macao (China), and Taiwan (China)) for security verification.
  - [1] 2026-11-01: the workspace holds 10,000 files totalling 100 GB with no stated validity period | capture: sha256:d2595b6e67a40546a868709c806860f060eea661eb13e06d3c2dcb483ee54391 | quote: 百炼存储空间支持的最大文件数为10000个，总大小不超过100 GB，暂时没有有效期限制。当文件数量或总大小达到任一上限时，新的文件上传请求将会失败。
  - [1] 2026-11-01: the 150 MB per-file ceiling for file-extract is unchanged | capture: sha256:d2595b6e67a40546a868709c806860f060eea661eb13e06d3c2dcb483ee54391 | quote: 将purpose指定为`file-extract`，文件格式支持文本文件（ TXT、DOCX、PDF、XLSX、EPUB、MOBI、MD、CSV、JSON），图片文件（BMP、PNG、JPG/JPEG、GIF和PDF扫描件），单个文件最大为 150 MB。
  - [1] 2026-11-19: the workspace holds 10000 files up to 100 GB with no stated validity period | capture: sha256:a3ab34a1c79a5d1ab98308c8875a03bad4bed1838b27a2fe8edc1e91e3c5325d | quote: 百炼存储空间支持的最大文件数为10000个，总大小不超过100 GB，暂时没有有效期限制。当文件数量或总大小达到任一上限时，新的文件上传请求将会失败。
  - [1] 2026-11-19: the 500 MB batch per-file ceiling is unchanged | capture: sha256:a3ab34a1c79a5d1ab98308c8875a03bad4bed1838b27a2fe8edc1e91e3c5325d | quote: 上传Batch任务的单个文件最大为500 MB。
  - [6] 2026-11-19: international registration needs an email address plus a non-mainland mobile number | capture: sha256:bded6d9f81950de6aa0675b87657f42e4431c58d01ae748489595414b170230e | quote: Requires an email address for registration, plus a mobile number from outside the Chinese mainland (including Hong Kong (China), Macao (China), and Taiwan (China)) for security verification.
- sources:
  - [1] https://help.aliyun.com/zh/model-studio/openai-file-interface
  - [2] https://docs.qwencloud.com/api-reference/platform-api/file
  - [3] https://help.aliyun.com/zh/model-studio/file-download
  - [4] https://help.aliyun.com/zh/model-studio/file-list
  - [5] https://help.aliyun.com/zh/model-studio/get-file-api
  - [6] https://www.alibabacloud.com/help/en/account/aliyun-vs-alibaba-cloud
  - [7] https://dashscope.aliyuncs.com/compatible-mode/v1/files

## Alibaba Cloud Agent Sandbox / FC / AgentRun

- `compute/alibaba-agentrun` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone yes, ID yes, institution no | verified 2026-11-18T04:45:13.519Z (live) | stale on 2026-12-19
- url https://help.aliyun.com/zh/agent-sandbox/product-overview/billing-overview
- free tier: no credit and no free compute; the only free allowance is 15 GiB of sandbox disk, and it is withdrawn while an instance is deep-asleep or snapshot-saved | unit: GiB | metered on: stored-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: national-id | detail: a China-site Alibaba Cloud account: registration needs a mobile number that can receive an SMS code, '注册前只需要准备一个...可以接收短信验证码的手机号码...即可，注册账号流程相同。', and '注册完成后，在充值和购买云产品之前需要完成账号的实名认证'. Individual verification takes '输入个人认证的姓名和身份证号码，开始认证，个人身份校验成功后进行扫脸', that is a name, an identity-card number and a face scan. The sandbox bills per second from the account balance ('账户余额不足导致欠费时，系统将发送欠费通知'), so the real-name check comes before use. | country: CN
- interface: rest
- limits:
  - request-rate (binding): vCPU, memory and disk are billed per second by QoS tier; the page's own example is '不足 1 秒按 1 秒计算' [1]
  - per-object-cap: 15 GiB of free rootfs disk while active or shallow-asleep; deep sleep and snapshots lose it [1]
  - retention-clamped: shallow sleep is entered automatically below 0.01 core of CPU, below 1,000 bytes a second of network, or with no request; deep sleep keeps memory in a snapshot and bills the storage [1]
- interface detail: an API, per the billing overview page: "自定义模板可通过 API 主动预热（Template Cache），减少沙箱首次启动耗时。"
- tooling: no client is named on https://help.aliyun.com/zh/agent-sandbox/product-overview/billing-overview
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the billing overview was read on 2026-10-22 (help.aliyun.com, Chinese). It prices three lifecycle states separately and states a 15 GiB free disk allowance. There is no free compute allowance, so the free tier is the disk and the record says so
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: no fixed wall clock; caps are user-set and a sandbox enters shallow sleep when idle by an activity test
  - free_tier_kind: allowance
  - granularity.min_billed_s: 1
  - burst_x: 1.0
  - ps.gib: 15
  - ps.price: billed per GiB-second past the 15 GiB allowance
  - ps.durability: rootfs; a deep-sleep snapshot holds memory as well as disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until destroyed; a snapshot persists while it is billed
  - net.out: yes
  - net.in: yes
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: three states priced separately: '活跃' bills vCPU, memory and disk; '深休眠' snapshots the whole instance including memory to persistent storage and bills disk only; '浅休眠' bills memory and disk and is entered automatically when 'CPU 消耗 < 0.01 core', '网络流量 < 1,000 Bytes/s' or '无请求触发'; and '磁盘享受 15 GiB 免费额度'. Deep sleep loses the 15 GiB free disk…
  - [1] 2026-11-03: an API operation exists | capture: sha256:0ba5638e5ac8343e0d93f7a027f9cdf5c3f9fd73d9fa905606ae8d8d8a5b64f7 | quote: 自定义模板可通过 API 主动预热（Template Cache），减少沙箱首次启动耗时。
  - [1] 2026-11-04: the page names an API and no other access interface | capture: sha256:0ba5638e5ac8343e0d93f7a027f9cdf5c3f9fd73d9fa905606ae8d8d8a5b64f7 | quote: 自定义模板可通过 API 主动预热（Template Cache），减少沙箱首次启动耗时。
  - [2] 2026-11-04: a China-site account must pass real-name verification before any recharge or purchase, and the sandbox bills from the account balance | capture: sha256:b159830a3ef0c3e1f58629d5641376bea1bc6a65c433aa1ec7e15573252a9b98 | quote: 注册完成后，在充值和购买云产品之前需要完成账号的实名认证
  - [2] 2026-11-04: a mobile number able to receive an SMS code is all that registration requires | capture: sha256:b159830a3ef0c3e1f58629d5641376bea1bc6a65c433aa1ec7e15573252a9b98 | quote: 注册前只需要准备一个...可以接收短信验证码的手机号码...即可，注册账号流程相同。
  - [3] 2026-11-04: individual verification is a Chinese identity-card number plus a face scan, on the China site | capture: sha256:fa61514d3943af491990bf35a4447df5567f1c43d925df8f1ddc438a9d689e2b | quote: 输入个人认证的姓名和身份证号码，开始认证，个人身份校验成功后进行扫脸。
  - [1] 2026-11-04: the sandbox bills against an account balance, so the account and its verification precede use | capture: sha256:0ba5638e5ac8343e0d93f7a027f9cdf5c3f9fd73d9fa905606ae8d8d8a5b64f7 | quote: 账户余额不足导致欠费时，系统将发送欠费通知。
  - [1] 2026-11-18:  | capture: sha256:0ba5638e5ac8343e0d93f7a027f9cdf5c3f9fd73d9fa905606ae8d8d8a5b64f7 | quote: 浅休眠 | 仅极速版支持 | 基于请求感知与内存快照技术，当沙箱实例空闲时自动进入浅休眠状态以降低成本。
- sources:
  - [1] https://help.aliyun.com/zh/agent-sandbox/product-overview/billing-overview
  - [2] https://help.aliyun.com/zh/account/ali-cloud-account-registration-process
  - [3] https://help.aliyun.com/zh/account/verify-your-identity-individual-account

## Alibaba Coding Plan (China)

- `coding-subs/alibaba-coding-plan-cn` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://help.aliyun.com/zh/model-studio/coding-plan
- free tier: No free plan. Pro at CNY 200/month (first month CNY 39.90 for first-time subscribers) with 6,000 requests per 5 hours, 45,000 per week and 90,000 per month. Lite stopped new subscriptions 2026-03-20. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: an Alibaba Cloud (Aliyun) account; real-name verification for Chinese cloud accounts is common but not stated on this page, so a national-ID gate is unverified here
- interface: rest, cli
- limits:
  - volume-quota (binding): 6,000 requests/5h; 45,000/week; 90,000/month on Pro [1]
  - request-rate: unpublished concurrency caps and throttling under load [1]
- endpoint: https://coding.dashscope.aliyuncs.com/v1
- tooling: OpenAI-compatible and Anthropic-compatible keys; Claude Code, OpenCode, Cursor, Cline and OpenClaw are named
- composes with: one monthly plan key through the coding base URL
- reliability: limited daily slots; undisclosed concurrency and rate technical limits
- notes: Paid-only. Separate slug from the existing alibaba-cloud-model-studio-coding-plan-china record, which cites an /en/ mirror of the same plan.
- evidence:
  - [1] 2026-11-18: the Lite plan is closed to new subscriptions on the China site | capture: sha256:8711bee2e0c920bb1d2481e64f8f7db735c9582b383a13a0acec8f46f2adec83 | quote: 1. Lite 套餐自 2026 年 3 月 20 日 00:00:00（UTC+08:00）起停止新购
  - [1] 2026-11-18: the 5-hour, weekly and monthly request caps are stated | capture: sha256:8711bee2e0c920bb1d2481e64f8f7db735c9582b383a13a0acec8f46f2adec83 | quote: | 用量限制 | 每 5 小时6,000 次请求 每周45,000 次请求 每月90,000 次请求 |
- sources:
  - [1] https://help.aliyun.com/zh/model-studio/coding-plan

## Alibaba Token Plan (China)

- `coding-subs/alibaba-token-plan-cn` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://help.aliyun.com/zh/model-studio/token-plan-overview
- free tier: No free tier stated. Token Plan is a Credits-billed subscription for interactive use in compatible AI tools; the overview page gives no price and no free allowance. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: an Aliyun account and a purchased Token Plan; real-name verification for Chinese cloud accounts is common but not stated on this page
- interface: rest, cli
- limits:
  - volume-quota (binding): monthly Credits allowance; amount and price not stated on the overview page [1]
- endpoint: https://token-plan.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
- tooling: a Token Plan API key (sk-sp-) plus the Bailian CLI; Claude Code, Codex, Qwen Code, OpenClaw and Hermes Agent are named
- composes with: monthly Credits spent through the China-region base URL; Standard and Pro plans add Harness MCP benefits
- reliability: no free allowance to throttle; the plan requires purchase
- evidence:
  - [1] 2026-11-18: Token Plan is a paid Credits-based subscription with no free allowance stated | capture: sha256:ebdc18f3f6b1d75ab26a52d4ab2b7396b17c46ee426d3695ab5559462b003d0c | quote: Token Plan 是阿里云百炼的 AI 模型订阅服务，以 Credits 统一计量，支持在兼容的 AI 工具中交互式使用。
  - [1] 2026-11-18: the page directs the user to select a plan and obtain a key | capture: sha256:ebdc18f3f6b1d75ab26a52d4ab2b7396b17c46ee426d3695ab5559462b003d0c | quote: 选择套餐并获取 API Key，按使用的工具复制命令完成接入。
- sources:
  - [1] https://help.aliyun.com/zh/model-studio/token-plan-overview

## Alibaba Cloud Model Studio Coding Plan (China site)

- `coding-subs/alibaba-cloud-model-studio-coding-plan-china` | fails-identity | evidence documented | binding request-rate | category coding subscription | tier Pro
- needs card no, phone yes, ID yes, institution no | verified 2026-11-02T15:23:25.619Z (live) | stale on 2026-12-03
- url https://help.aliyun.com/en/model-studio/coding-plan
- free tier: no free plan is listed. The plan page lists one paid plan: Pro at CNY 200 a month, with the first month at CNY 39.90 for first-time subscribers, for up to 6,000 requests per 5 hours, 45,000 requests per week and 90,000 requests per month | unit: requests | metered on: request-count | read on: 2026-11-02 | source: [1] | note: one request is one model call; new slots are restocked daily at 09:30:00 UTC+08:00
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: national-id | detail: The China site registers accounts with a mobile number from the Chinese mainland and requires individual or enterprise real-name verification before any purchase or use of cloud resources. Individual verification uses a real-name verified personal Alipay account, or a name and an identity card number with a face scan. The international site is a separate account system that does not share accounts | country: CN
- interface: rest, cli
- limits:
  - request-rate (binding): up to 6,000 requests per 5 hours, as a rolling window [1]
  - request-rate (binding): up to 45,000 requests per week, reset every Monday at 00:00:00 UTC+08:00 [1]
  - request-rate (binding): up to 90,000 requests per month, reset at 00:00:00 UTC+08:00 on the subscription renewal date [1]
- limits note: the same three request caps as the international edition; the first one reached pauses calls
- binding note: the identity gate fails before any quota binds and is not a term of the constraint vocabulary; the three request caps apply at once once an account exists
- interface detail: OpenAI-compatible base URL https://coding.dashscope.aliyuncs.com/v1 and Anthropic-compatible base URL https://coding.dashscope.aliyuncs.com/apps/anthropic, with a plan key that starts with sk-sp-. Supported models: qwen3.7-plus, qwen3.6-plus, kimi-k2.5, glm-5 and MiniMax-M2.5, and also qwen3.5-plus
- endpoint: part of interface detail
- tooling: the clients that the vendor lists on the plan page, among them Claude Code, Qwen Code, Cursor and OpenClaw; the user sets the plan key and the plan base URL in the client
- composes with: the Qwen Code auth menu offers this plan for the Beijing region with the endpoint https://coding.dashscope.aliyuncs.com/v1; the international edition of the same plan has its own record and needs a different account
- reliability: Pro slots sell first come, first served with a daily restock at 09:30:00 UTC+08:00, so a plan can be sold out; a key used by scripts or application backends can be suspended or revoked
- notes: The China site edition sells the same Pro quota as the international edition at CNY 200 a month, with a first month at CNY 39.90. A user outside the Chinese mainland cannot register: the site needs a mainland mobile number and real-name verification by identity card or a verified Alipay account. The page states that model inputs and generated content are used to improve the service
- evidence note: price, quota, base URLs and the identity requirements are quoted from the vendor pages read on 2026-11-02. The quota is the vendor's published number and is not a measurement
- evidence:
  - [1] 2026-11-02: the China site sells the Pro plan at 200 yuan a month | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: | Price | ¥ 200/month |
  - [1] 2026-11-02: the first month costs 39.90 yuan for first-time subscribers and renewals cost 200 yuan | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: First-time subscribers to the Pro plan can get the first month for ¥39.90 (list price: ¥200/month). Renewals are billed at ¥200/month.
  - [1] 2026-11-02: the Pro quota is 6,000 requests per 5 hours, 45,000 per week and 90,000 per month | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: | Quota | Up to 6,000 requests per 5 hours Up to 45,000 requests per week Up to 90,000 requests per month |
  - [1] 2026-11-02: plan slots are limited and sold first come first served | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: Slots are limited and available on a first-come, first-served basis.
  - [1] 2026-11-02: the daily restock is at 09:30 UTC+08:00 | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: New slots are restocked daily at 09:30:00 (UTC+08:00).
  - [1] 2026-11-02: the OpenAI-compatible China plan base URL | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: OpenAI-compatible protocol: `https://coding.dashscope.aliyuncs.com/v1`
  - [1] 2026-11-02: the Anthropic-compatible China plan base URL | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: Anthropic-compatible protocol: `https://coding.dashscope.aliyuncs.com/apps/anthropic`
  - [1] 2026-11-02: the supported model list | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: | Supported models | Only the following exact model versions are supported: Recommended models: qwen3.7-plus (vision), qwen3.6-plus (vision), kimi-k2.5 (vision), glm-5, and MiniMax-M2.5 More models: qwen3.5-plus (vision) |
  - [1] 2026-11-02: a key used outside interactive coding tools can be suspended or revoked | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8
  - [1] 2026-11-02: the China plan page states that inputs and generated content are used to improve the service | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: By using the Coding Plan, you authorize use of your model inputs and generated content to improve the service and optimize models.
  - [1] 2026-11-02: the plan is bought with an Alibaba Cloud account | capture: sha256:da63f67d7b1e7992a7e71ed32fad6ea852ba0d25a68f956df340e5c68ca88ce8 | quote: Subscribe directly with your Alibaba Cloud account.
  - [2] 2026-11-02: China site account registration needs a mobile number from the Chinese mainland | capture: sha256:bded6d9f81950de6aa0675b87657f42e4431c58d01ae748489595414b170230e | quote: Requires a mobile number from the Chinese mainland.
  - [2] 2026-11-02: China site purchase and use need real-name verification | capture: sha256:bded6d9f81950de6aa0675b87657f42e4431c58d01ae748489595414b170230e | quote: Required. You must complete individual or enterprise real-name verification before you purchase or use any cloud resources.
  - [2] 2026-11-02: an international site account does not work on the China site | capture: sha256:bded6d9f81950de6aa0675b87657f42e4431c58d01ae748489595414b170230e | quote: The account data of the two sites is completely isolated and cannot be shared.
  - [3] 2026-11-02: individual verification by Alipay needs a personal Alipay account that is itself real-name verified | capture: sha256:fa61514d3943af491990bf35a4447df5567f1c43d925df8f1ddc438a9d689e2b | quote: 一个可以正常使用的、已经完成实名认证的个人支付宝账号。
  - [3] 2026-11-02: the face-scan route takes a name and an identity card number | capture: sha256:fa61514d3943af491990bf35a4447df5567f1c43d925df8f1ddc438a9d689e2b | quote: 输入个人认证的姓名和身份证号码，开始认证，个人身份校验成功后进行扫脸。
- sources:
  - [1] https://help.aliyun.com/en/model-studio/coding-plan
  - [2] https://www.alibabacloud.com/help/en/account/aliyun-vs-alibaba-cloud
  - [3] https://help.aliyun.com/zh/account/verify-your-identity-individual-account

## student voucher

- `compute/student-voucher` | fails-identity | evidence documented | binding none | category dev environment
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://university.aliyun.com/buycenter/
- free tier: A CNY 300 no-threshold voucher quoted as 通过学生认证的高校学生，可领取300元云工开物学生专属优惠券, plus access to a student compute package across thirteen instance shapes. The credit is real and large for this market; the door is the finding. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: one-time-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: Verification requires full-time enrolment at a mainland Chinese higher-education institution, checked against the national student register, on an account that has already passed Alipay real-name certification. One account per identity card, and the student status expires every 30 days and must be re-verified. The vendor states that students in Hong Kong, Macau and Taiwan go through manual review instead, so the general route is closed to anyone not enrolled in a Chinese institution.
- interface: unknown
- limits note: Nothing throttles the voucher itself, but the status lapses after 30 days and the account cannot be re-verified after graduation, so the credit is a one-shot that cannot be renewed by waiting.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: With an enrolled affiliate, this is the single largest no-card cloud credit found in the Chinese market and it stacks with the student priced instances, which are sold separately from the voucher.
- reliability: no reliability event recorded
- extras:
  - facets.class: refutation
  - facets.free_tier_kind: one-time-credit
- evidence:
  - [1] 2026-10-22: page states 通过学生认证的高校学生，可领取300元云工开物学生专属优惠券, quoted
  - [2] 2026-10-22: page states the offer is for 中国内地高校的在校大学生 and requires 普通全日制 enrolment verified against 学信网 plus Alipay real-name certification, quoted
  - [2] 2026-10-22: page states 学生身份的有效期为30天 and that a verified account cannot be moved to another account, quoted
  - [3] 2026-10-22: the FAQ limits the general student benefit to students of Chinese institutions including the mainland, Hong Kong, Macau and Taiwan
- sources:
  - [1] https://university.aliyun.com/buycenter/
  - [2] https://help.aliyun.com/zh/account/student-identity-verification
  - [3] https://help.aliyun.com/zh/document_detail/2593343.html
