# Tencent Cloud

> tencent.com | Compute, Inference, Storage; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tencent/ | JSON https://fshy.ajam.dev/api/v1/entity/tencent.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tencent Cloud SCF

- `compute/tencent-scf` | qualifies-with-caveat | evidence documented | binding request-rate | category cloud VM
- needs card no, phone yes, ID yes, institution no | verified 2026-11-06T17:42:12.767Z (live) | stale on 2026-12-07
- url https://cloud.tencent.com/document/product/583/17299
- free tier: a free quota exists for 云函数 (SCF), listed in the billing overview's own contents; its size is on the linked pricing page, which this record does not cite | unit: mixed | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: Outbound internet traffic is a billed item of pay-as-you-go billing, and the free quota excludes Web function response traffic; the per-unit price is not on this page. | metered: no | source: [1]
- identity: national-id | detail: national-id: an account must pass real-name identity verification before it can buy or use a cloud product ('腾讯云账号需要完成账号实名认证才能购买和使用云产品'). On the mainland site an individual verifies with a Chinese resident identity card ('个人实名认证支持中国大陆居民使用身份证实名认证'); Phone: required on both routes: the international sign-up states 'Enter the mobile number of the registration location.' and 'Obtain and enter the verification code sent to your mobile number.', and the mainland form carries a mobile-number field with a China prefix ('获取验证码'). Card: required on the international route: 'Enter your card information correctly to complete the card binding.' Country: the registration location is fixed at sign-up: 'Once the account registration location is confirmed, it cannot be changed.' | country: CN on the mainland route, where an individual verifies with a Chinese resident identity card; the international station takes a government document issued in the account's registration country, which is fixed at sign-up
- interface: unknown
- limits:
  - request-rate (binding): SCF has a free quota, named in the billing overview's contents; its size is on the linked pricing page [1]
  - write-gated: log delivery to CLS is billed under CLS's own rules, and CLS grants new users a separate short-lived quota [1]
  - per-object-cap: other products reached from a function, such as CFS and COS, bill under their own rules [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the billing overview was read on 2026-10-22 and its contents carry a 免费额度 section, which contradicts the record's paid-only verdict. The amount is not in the extracted body, so the record states that a free quota exists and does not give a number
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: a function answers an invocation; there is no machine to keep alive
  - free_tier_kind: allowance
  - net.out: yes
  - net.in: yes
  - net.ports: invocation and an API gateway
  - net.static_ip: no
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: the billing overview was read on 2026-10-22 (Chinese) and its own table of contents lists '免费额度' - a free quota - alongside a pay-as-you-go mode; the amount itself is on the linked pricing page this record does not cite
  - [1] 2026-11-03: outbound internet traffic is a billed item | capture: sha256:03b7aaaaf37440fb03255f390a014066701a7926df0418a366a1bbdf9283eb2e | quote: 后付费计费项包括：资源使用费用、调用次数费用、外网出流量费用、预置并发闲置费用、Web 函数响应流量费用。
  - [2] 2026-11-04: an account must complete real-name identity verification before buying or using a cloud product | capture: sha256:f27142020863fac0aaaca4820b10fe2a7db93221cfd3609fd72f18c7c1bf42dc | quote: 腾讯云账号需要完成账号实名认证才能购买和使用云产品
  - [2] 2026-11-04: individual verification on the mainland site is done with a Chinese resident identity card | capture: sha256:f27142020863fac0aaaca4820b10fe2a7db93221cfd3609fd72f18c7c1bf42dc | quote: 个人实名认证支持中国大陆居民使用身份证实名认证
  - [3] 2026-11-04: the mainland registration page offers email sign-up and a +86 mobile field with a code sent to it | capture: sha256:e699b3323761db4d21764e31e0bd7eb795d778607fcda7a4a7279138fe437cd3 | quote: 邮箱注册
  - [4] 2026-11-04: registration starts with an email address, a Google account or WeChat, before the real-name step | capture: sha256:b6750a98148b75d7630a6584256c3e50cb9678ead369907e951075e72d65fba0 | quote: Tencent Cloud accounts can be registered using an email address, a Google account, or WeChat
  - [4] 2026-11-04: the international station binds a card at sign-up with a 1.00 USD pre-authorization | capture: sha256:b6750a98148b75d7630a6584256c3e50cb9678ead369907e951075e72d65fba0 | quote: Enter your card information correctly to complete the card binding.
  - [5] 2026-11-04:  | capture: sha256:abe56c8853601b6f30e696190d0de52a506973c3d27014d754c99e3a25e3e3d0 | quote: Tencent Cloud International supports individual users in applying for identity verification using a valid ID card, passport, driver's license, or work permit
  - [2] 2026-11-04: the real-name verification gate is unchanged | capture: sha256:f27142020863fac0aaaca4820b10fe2a7db93221cfd3609fd72f18c7c1bf42dc | quote: 腾讯云账号需要完成账号实名认证才能购买和使用云产品
  - [2] 2026-11-06: an account must pass real-name identity verification before it can buy or use a cloud product, and an individual on the mainland route verifies with a Chinese resident identity card | capture: sha256:f27142020863fac0aaaca4820b10fe2a7db93221cfd3609fd72f18c7c1bf42dc | quote: 腾讯云账号需要完成账号实名认证才能购买和使用云产品
  - [5] 2026-11-06: the identity document must come from the account's registration country, which is fixed at sign-up | capture: sha256:abe56c8853601b6f30e696190d0de52a506973c3d27014d754c99e3a25e3e3d0 | quote: This location is the country/region you selected when the account is registered. Once the account is registered, it cannot be changed
- sources:
  - [1] https://cloud.tencent.com/document/product/583/17299
  - [2] https://cloud.tencent.com/document/product/378/3629
  - [3] https://cloud.tencent.com/register
  - [4] https://intl.cloud.tencent.com/document/product/378/17985
  - [5] https://intl.cloud.tencent.com/document/product/378/10495

## Tencent Cloud Agent Runtime - Agent Sandbox

- `compute/tencent-agent-runtime` | paid-only | evidence documented | binding request-rate | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22T04:48:09.512Z (live) | stale on 2026-11-22
- url https://cloud.tencent.com/document/product/1814/133249
- free tier: no free tier: CPU bills at CNY 0.000081 a core-second from a successful start to a stop; a paused instance stops CPU and memory billing and pays only the storage its state needs | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: not published | metered: no | source: [1]
- identity: email
- interface: unknown
- limits:
  - request-rate (binding): CNY 0.000081 a core-second, billed from a successful start to a stop [1]
  - retention-clamped: a paused instance stops CPU and memory billing and continues to pay for the storage its state needs; waking resumes compute billing [1]
  - per-object-cap: the document's own 30-day example for 1 core always-on is CNY 69.98, and for 2 cores CNY 419.90 [1]
- interface detail: Access interface not documented in published terms.
- tooling: not stated
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the billing document was read on 2026-10-22 (Chinese, updated 2026-10-10) and states the per-second CPU rate, the pause semantics and a 30-day worked example. There is no free tier, so the claim is contradicted and the verdict moves to paid-only
- extras:
  - keep_rate: 1.0
  - billing_model: unclassified
  - shape.vcpu: 1
  - shape.note: the document's worked example bills 1 core for 28,800 seconds a day at CNY 69.98 a month
  - session_cap.restart_required: no
  - session_cap.note: no vendor reap: billing runs from start to stop, and pause keeps state for a storage charge
  - free_tier_kind: none
  - granularity.min_billed_s: 1
  - burst_x: 1.0
  - ps.price: state storage is billed while an instance is paused
  - ps.durability: paused state kept on storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the state is kept
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: '按 实际运行时长 及 资源规格 计费。实例 启动成功后开始计费，停止后停止计费' - billed on actual runtime and spec, from a successful start to a stop - with 'CPU 0.000081 元 / 核 / 秒' and '暂停期间 CPU、内存停止计费，保留状态所需存储继续计费，唤醒后计算资源重新计费', quoted
- sources:
  - [1] https://cloud.tencent.com/document/product/1814/133249

## Tencent Hunyuan text generation API (China site)

- `inference/tencent-hunyuan-api-cn` | fails-identity | evidence documented | binding volume-quota | category inference API, one-time free tokens
- needs card no, phone no, ID yes, institution no | verified 2026-11-03T11:30:41.454Z (live) | stale on 2026-12-04
- url https://cloud.tencent.com/document/product/1729/97731
- free tier: A one-time free resource package on first activation: 共100万 tokens shared across Hunyuan-a13b, Hunyuan-role-latest, the translation models and the vision models, and a separate 100万 tokens for Hunyuan-embedding, each valid for 1 year from activation. The page states the functions are migrating to TokenHub and the original platform no longer accepts new model purchases | unit: tokens | metered on: request-count | read on: 2026-10-28 | source: [1] | note: one-time-quota
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: national-id | detail: activation needs Tencent Cloud enterprise or personal real-name authentication, quoted from the billing page. The vendor's account overview scopes China-site accounts to mainland enterprises and to individuals in the mainland, Hong Kong, Macao and Taiwan; whether a non-mainland passport completes China-site authentication is unverified
- interface: rest
- limits:
  - volume-quota (binding): 100万 tokens shared across the listed text and vision models, one-time; a separate 100万 tokens for Hunyuan-embedding [1]
  - retention-clamped: the package expires 1 year after activation and unused tokens become invalid [1]
- binding note: real-name authentication gates activation before any quota applies
- tooling: not stated
- composes with: the page directs new model services to TokenHub; services already bought continue to work. TokenHub gives each main account a one-time free trial of 100 万 tokens for every language model, valid 1 year, in a campaign running to 2026-12-31, and its quick start also requires real-name authentication first. The international edition of TokenHub carries the same 100 万 tokens and is described in the chaining of the Tencent HY Text Generation Global record
- reliability: the page states the Hunyuan functions are migrating to TokenHub and the original platform stops supporting new model purchases
- notes: postpaid list price for Hunyuan-a13b after the package: CNY 0.5 input and CNY 2 output per million tokens; the free-model status of hunyuan-lite is not shown on this page
- evidence:
  - [1] 2026-10-28: activating Hunyuan requires Tencent Cloud enterprise or personal real-name authentication | capture: sha256:07837555e214b164169bc053e2404066aa2f4051838685e78195cb1ad6db8c30 | quote: 腾讯混元大模型的开通使用需要先通过 [腾讯云企业实名认证](https://cloud.tencent.com/document/product/378/56515) 或者 [腾讯云个人实名认证](https://cloud.tencent.com/document/product/378/56514)。
  - [1] 2026-10-28: the free resource package for Hunyuan-a13b is 100万 tokens shared, valid for 1 year | capture: sha256:07837555e214b164169bc053e2404066aa2f4051838685e78195cb1ad6db8c30 | quote: | Hunyuan-a13b | 共100万 tokens，共享消耗。资源包有效期为1年，自开通服务之日起1年内若免费资源包未使用完，则过期作废。 |
  - [1] 2026-10-28: postpaid list price for Hunyuan-a13b per million tokens after the free package | capture: sha256:07837555e214b164169bc053e2404066aa2f4051838685e78195cb1ad6db8c30 | quote: | Hunyuan-a13b | 输入：0.5元输出：2元 |
  - [2] 2026-11-03: China-site accounts are for mainland enterprises and for individuals in the mainland, Hong Kong, Macao and Taiwan | capture: sha256:3a09aa6c9dd50bceb033b07ab7795888d5cd749e242061cb414f476f0879120e | quote: Tencent Cloud China site accounts are applicable to enterprise users in the Chinese mainland (excluding Hong Kong (China), Macao (China), and Taiwan (China) regions), and individual users in the Chinese mainland, Hong Kong (China), Macao (China), and Taiwan (China).
  - [3] 2026-11-03: TokenHub China gives every language model a free trial of 1,000,000 tokens, valid 1 year | capture: sha256:3e6b2c337c56ffd9e526077430ce02ba6cd098413bca31ed74947cdf41e4c2e8 | quote: 所有语言模型均提供 100 万 Tokens 的免费体验额度，有效期 1 年。
  - [3] 2026-11-03: the TokenHub free trial campaign runs to 2026-12-31 | capture: sha256:3e6b2c337c56ffd9e526077430ce02ba6cd098413bca31ed74947cdf41e4c2e8 | quote: 本期活动时间截至 2026 年 12 月 31 日
  - [4] 2026-11-03: the TokenHub China quick start requires real-name authentication before use | capture: sha256:6e5e04ea903b42256fc24fa5b6c1ceffd38f549c311b82f76cf9ed32ed2a15ab | quote: 在使用腾讯云大模型服务平台 TokenHub 之前，您需要 并完成 。注册腾讯云 实名认证
  - [1] 2026-11-03: the page still lists the one-time 100万 token package for Hunyuan-a13b with 1 year validity; the page is unchanged since 2026-06-26 | capture: sha256:07837555e214b164169bc053e2404066aa2f4051838685e78195cb1ad6db8c30 | quote: | Hunyuan-a13b | 共100万 tokens，共享消耗。资源包有效期为1年，自开通服务之日起1年内若免费资源包未使用完，则过期作废。 |
- sources:
  - [1] https://cloud.tencent.com/document/product/1729/97731
  - [2] https://intl.cloud.tencent.com/document/product/378/80429
  - [3] https://cloud.tencent.com/document/product/1823/130053
  - [4] https://main.qcloudimg.com/raw/document/product/pdf/1823_130058_cn.pdf

## tencent cloud cos (腾讯云对象存储)

- `storage/tencent-cloud-cos` | fails-egress | evidence documented | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:45.960Z (live) | stale on 2026-12-05
- url https://cloud.tencent.com/document/product/436/50201
- free tier: None reachable: Storage is cheap, egress is the entire cost and it is the worst ratio in the set. Standard storage ¥0.118/GB/mo ($18.06/TB/mo) but outbound traffic ¥0.5/GB. That is ¥512/TB = $76.54 per TB. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Outbound internet traffic is billed at 0.5 yuan/GB in every storage class, settled daily; no free allowance is stated on the billing pages. | metered: yes
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: read 2026-11-03: https://cloud.tencent.com/document/product/436/50201 (outbound traffic 0.5 yuan/GB in every storage class) and https://cloud.tencent.com/document/product/436/53863 (1 TB = 1024 GB billing unit), both vendor pages; the egress meter that decides fails-egress cites those captures. The storage price and the free-tier absence carry the 2026-10-21 evidence rows only.
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Storage is cheap, egress is the entire cost and it is the worst ratio in the set. Standard storage ¥0.118/GB/mo ($18.06/TB/mo) but outbound traffic ¥0.5/GB — that is ¥512/TB = $76.54 per TB
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Storage is cheap, egress is the entire cost and it is the worst ratio in the set. Standard storage ¥0.118/GB/mo ($18.06/TB/mo) but outbound traffic ¥0.5/GB — that is ¥512/TB = $76.54 per TB
  - [2] 2026-10-21: cited as the basis of the rejection: Storage is cheap, egress is the entire cost and it is the worst ratio in the set. Standard storage ¥0.118/GB/mo ($18.06/TB/mo) but outbound traffic ¥0.5/GB — that is ¥512/TB = $76.54 per TB
  - [3] 2026-10-21: cited as the basis of the rejection: Storage is cheap, egress is the entire cost and it is the worst ratio in the set. Standard storage ¥0.118/GB/mo ($18.06/TB/mo) but outbound traffic ¥0.5/GB — that is ¥512/TB = $76.54 per TB
  - [1] 2026-11-03: outbound traffic is 0.5 yuan per GB in every storage class | capture: sha256:b0b0f266de1f7e32799b0c0e5dc6a6d77098681bb03b5c1b5f92de83f8dc731a | quote: | 流量单价（元/GB） | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
  - [4] 2026-11-03: the billing unit is GB with 1 TB = 1024 GB | capture: sha256:14a24c232ed16b24af3f7f7ae199f462076422ee0ebcd662d3367b47a5ab1897 | quote: 外网下行流量1TB = 1024GB
  - [1] 2026-11-04: outbound traffic is 0.5 yuan per GB in every storage class | capture: sha256:b0b0f266de1f7e32799b0c0e5dc6a6d77098681bb03b5c1b5f92de83f8dc731a | quote: | 流量单价（元/GB） | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 |
- sources:
  - [1] https://cloud.tencent.com/document/product/436/50201
  - [2] https://www.foreignserver.com/cos/txyshoufei.html
  - [3] https://buy.cloud.tencent.com/price/cos
  - [4] https://cloud.tencent.com/document/product/436/53863
