# Volcengine

> volcengine.com | Compute, Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/volcengine/ | JSON https://fshy.ajam.dev/api/v1/entity/volcengine.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Volcano Engine AgentKit / veFaaS sandbox

- `compute/volcengine-agentkit` | qualifies-with-caveat | evidence unverified | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:21.010Z (live) | stale on 2026-11-19
- url https://docs.volcengine.com/docs/agentkit/billing-items?lang=zh
- free tier: no free sandbox quota or trial credit is listed on the billing page; only the shared gateway is free, for 2 agent runtimes per account per region and for 2 MCP services plus MCP toolsets combined | unit: none | metered on: wall-clock | read on: 2026-10-02 | source: [1] | note: sandbox template usage is billed per second: CNY 0.0000405 per vCPU-second and CNY 0.0000102 per GB-second of memory, plus CNY 0.8 per GB of public downstream traffic; a new-account trial pack is unverified
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: sandbox template public downstream traffic is billed at CNY 0.8 per GB | metered: yes | source: [2]
- identity: email | detail: unverified: signup and real-name verification requirements are not stated on the AgentKit billing or limits pages; buying a gateway instance requires an available account balance above CNY 100; the email kind is assumed
- interface: unknown
- limits:
  - volume-quota: 100 sandbox instances and 50 sandbox templates per account per region, raisable through the quota center [3]
  - retention-clamped: maximum sandbox instance lifetime 24 hours, not adjustable [3]
  - per-object-cap: agent runtime: imported image up to 10 G, request payload up to 16 MB, synchronous request timeout 30 minutes, 20 runtimes per account per region and 20 instances per runtime [3]
- limits note: the quota center raises the runtime, template and instance counts; the 24 hour sandbox lifetime and the 20 instances per runtime cannot be raised
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- notes: Reached on 2026-10-22 by no route in the challenge protocol. The first read returned an empty body; the firecrawl route then returned 64,113 bytes of the AgentKit billing document, but the fetched body is the document shell and navigation with no per-item price table in the extracted text. The price table is rendered by script and the route that would execute it did not return it. Volcengine's Chinese billing document is therefore reached but its numbers are not.
- evidence note: documented for the per-second prices, free gateway counts and limits from the rendered first-party billing and limits pages; signup requirements and any new-account trial pack are…
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - free_tier_kind: allowance
  - burst_x: 1.0
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: unverified: no route returned the page on 2026-10-22. The first read returned an empty body; the firecrawl route then returned 64,113 bytes of the AgentKit billing document, but the fetched body is the document shell and navigation with no per-item price table in the extracted text. The price table is rendered by script and the route that would execute it did not return it. Volcengine's Chinese billing document is therefore reached but its numbers are not.
  - [1] 2026-10-28: the live billing page is the lowercase billing-items path | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: 本文介绍 AgentKit 各计费项的构成、单价及计算方式，帮助您在下单前预估费用。
  - [1] 2026-10-28: the free counts are stated on the billing page | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: 智能体运行时：每账号每地域 2 个免费；超出部分按共享网关实例费计费。
  - [1] 2026-10-28: the shared gateway is free for 2 agent runtimes per account per region | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: 智能体运行时：每账号每地域 2 个免费；超出部分按共享网关实例费计费。
  - [1] 2026-10-28: sandbox template vCPU is priced at CNY 0.0000405 per second | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: | 沙箱模板 CPU | toolvcpu | 沙箱模板运行消耗的计算资源。 | 元 / vCPU / 秒 | 0.0000405 |
  - [3] 2026-10-28: up to 100 sandbox instances per account per region | capture: sha256:0fb71d2cc7836fc99428ea9acb4829c6a58b1b15ce55971cb572ef24800995ca | quote: | 单个账号在单个地域可创建的沙箱实例数量 | 100 | 是，如需提升配额，请前往
  - [3] 2026-10-28: the sandbox instance lifetime cap is 24 hours and not adjustable | capture: sha256:0fb71d2cc7836fc99428ea9acb4829c6a58b1b15ce55971cb572ef24800995ca | quote: | 单个沙箱实例的最大生命周期时长 | 24 小时 | 否 |
  - [1] 2026-10-28: sandbox public downstream traffic is billed at CNY 0.8 per GB | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: | 沙箱模板公网流量 | tooltraffic | 沙箱模板产生的公网下行流量费用。 | 元 / GB | 0.8 |
  - [1] 2026-10-28: sandbox public downstream traffic is billed per GB | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: | 沙箱模板公网流量 | tooltraffic | 沙箱模板产生的公网下行流量费用。 | 元 / GB | 0.8 |
  - [1] 2026-10-28: a gateway instance purchase needs an available balance above CNY 100 | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: 购买网关实例时，请确保您的火山引擎账户可用余额大于 100 元。
  - [1] 2026-10-28: the free counts are stated on the rendered billing page | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: 智能体运行时：每账号每地域 2 个免费；超出部分按共享网关实例费计费。
  - [1] 2026-10-28: sandbox compute is billed per second of use, unchanged | capture: sha256:f51fcb10fd81a8d53e25d9932e3e608bd46c4206446146fa713c70c1a473daf0 | quote: | 沙箱模板 CPU | toolvcpu | 沙箱模板运行消耗的计算资源。 | 元 / vCPU / 秒 | 0.0000405 |
  - [1] 2026-11-03: sandbox public downstream traffic is billed at CNY 0.8 per GB; no free traffic allowance is listed | capture: sha256:36c58395c005456fd66b732f7c27d4ed07eed0c56105ef2ff5781a03dc170d7c | quote: | 沙箱模板公网流量 | tooltraffic | 沙箱模板产生的公网下行流量费用。 | 元 / GB | 0.8 |
- sources:
  - [1] https://docs.volcengine.com/docs/agentkit/billing-items?lang=zh
  - [2] https://docs.volcengine.com/docs/agentkit/Billing_items?lang=zh
  - [3] https://docs.volcengine.com/docs/agentkit/limits?lang=zh

## Volcengine (火山引擎)

- `compute/volcengine-free-trial` | fails-identity | evidence documented | binding write-gated | category VPS | tier Free trial quota
- needs card no, phone yes, ID yes, institution no | verified 2026-10-24T06:45:00.000Z (live) | stale on 2026-11-24
- url https://www.volcengine.com/article/2821160
- free tier: '免费试用额度仅对完成中国大陆实名认证的账号开放，未完成认证的账号无法触发额度发放逻辑'. the free trial quota is issued only to accounts that have completed mainland-China real-name verification; an unverified account never triggers the issuance. The article's stated precondition is '已完成中国大陆手机号+身份证双重实名认证的火山引擎账号'. a mainland mobile number plus a national identity card. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: one free trial quota per account, gated on real-name verification status rather than on quantity
- retention: Not stated on the article read: the trial quota's validity period and the instance lifetime are not given in the troubleshooting guide. The article names the trial as time-limited ('限时赠送') without a duration.
- egress: not published on the page read | metered: yes | source: [1]
- identity: national-id | detail: national ID required: a mainland-China mobile number plus an identity card (身份证), verified as 实名认证. No card is mentioned as the gate on the page read; the gate is the identity document and the mainland phone number behind it. | country: CN
- interface: ssh, rest
- limits:
  - write-gated (binding): mainland-China real-name verification: a mainland mobile number plus a national identity card [1]
  - per-ip-shaping: accounts verified outside mainland China are told to apply for regional trial entitlements instead [1]
  - volume-quota: the trial quota lapses automatically once a paid plan is opened on the account [1]
- binding note: The national ID is the first and only thing that matters: without a mainland identity card the quota logic is never triggered at all.
- interface detail: Volcengine ECS instances with SSH and a console; the trial page read is about the quota rather than the machine
- tooling: any SSH client; the vendor console
- composes with: Out of reach: the gate is a mainland national identity card, which no amount of card or phone solves.
- reliability: no reliability event recorded
- notes: Volcengine Cloud trial allocations are restricted to users with mainland China real-name identity verification (实名认证) and expire upon purchasing a commercial plan.
- evidence note: The real-name requirement and the phone-plus-ID pair are quoted from Volcengine's own developer article read. A second Volcengine documentation page on real-name verification returned a DNS failure, so the official verification page itself was not read.
- extras:
  - shape.note: not published on the page read
  - billing_model: free
  - term: not published
  - price_arithmetic: not computable: the trial's shape and duration are unpublished, so no rate exists to multiply
  - free_tier_kind: trial
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: not published on the page read
  - session_cap.restart_required: no
  - session_cap.note: not published
  - signup_url: https://www.volcengine.com/
  - payment_methods: not established: the gate on the page read is the identity document, not a card
- evidence:
  - [1] 2026-10-24: quoted: '免费试用额度仅对完成中国大陆实名认证的账号开放，未完成认证的账号无法触发额度发放逻辑' (the free trial quota is open only to accounts with completed mainland-China real-name verification; an unverified account cannot trigger the issuance logic)
  - [1] 2026-10-24: quoted: '已完成中国大陆手机号+身份证双重实名认证的火山引擎账号' (an account with completed dual real-name verification by mainland-China mobile number and identity card)
  - [1] 2026-10-24: quoted: '非中国大陆实名认证账号的场景，建议申请对应区域的产品试用权益' (for accounts not verified in mainland China, apply for the trial entitlement of the corresponding region)
  - [2] 2026-10-24: the ECS product page describes the service as '安全稳定、可弹性伸缩的云计算服务' with '99.995% SLA 可用性', but publishes no free tier on that page
- sources:
  - [1] https://www.volcengine.com/article/2821160
  - [2] https://www.volcengine.com/product/ecs

## volcengine ark files api (doubao)

- `storage/volcengine-ark-files-api` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ark.volcengine.com/region:cn-beijing/docs/upload-files-api
- free tier: none reachable: Server-side clamped retention: minimum 1 day, maximum 30 days, default 7 days. 512 MB per file on managed storage. Cannot hold anything. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Server-side clamped retention: minimum 1 day, maximum 30 days, default 7 days. 512 MB per file on managed storage. Cannot hold anything.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Server-side clamped retention: minimum 1 day, maximum 30 days, default 7 days. 512 MB per file on managed storage. Cannot hold anything.
- sources:
  - [1] https://ark.volcengine.com/region:cn-beijing/docs/upload-files-api
