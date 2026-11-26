# KUAE Cloud

> mthreads.com | Coding subscriptions, Compute; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mthreads/ | JSON https://fshy.ajam.dev/api/v1/entity/mthreads.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## KUAE Cloud Coding Plan

- `coding-subs/kuae-cloud-coding-plan` | trial-only | evidence documented | binding retention-clamped | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://docs.mthreads.com/kuaecloud/kuaecloud-doc-online/coding_plan/plan_overview
- free tier: Free Trial: about 40 prompts per 5 hours, valid 30 days from claim, one claim per account, limited daily slots. Paid: Lite about 120, Pro about 600, Max about 2400 prompts per 5 hours. Each prompt bundles roughly 15-20 model calls. | unit: requests | metered on: request-count | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: an account on the KUAE Cloud / Moore Threads coding platform; the guide shows a free claim button after registration, and does not state that a card is needed for the Free Trial
- interface: rest, cli
- limits:
  - request-rate: about 40 prompts per 5 hours on Free Trial [1]
  - retention-clamped (binding): 30-day validity from claim; one claim per account [1]
- endpoint: https://coding-plan-endpoint.kuaecloud.net/v1
- tooling: OpenAI-compatible /v1 and Anthropic-compatible endpoints; Claude Code, Cline, Cursor, Kilo Code, Roo Code and OpenCode are named
- composes with: the 30-day Free Trial with a 5-hour prompt window is the scarce link; it cannot be claimed twice on one account
- reliability: peak-hour requests may queue; free-trial slots are limited daily (code.mthreads.com shows 100 developers per day)
- notes: Trial-only. Earlier doc-url attempts returned a 16-word footer shell.
- evidence:
  - [1] 2026-11-18: a 30-day free trial is offered during the promotion | capture: sha256:6984bf84a23a34c4ce22b588117d89791f4f908b473486c262ba96663b3dbce2 | quote: 用户在推广活动期间可申请30天免费试用
  - [1] 2026-11-18: Free Trial is about 40 prompts per 5 hours and valid 30 days, once per account | capture: sha256:6984bf84a23a34c4ce22b588117d89791f4f908b473486c262ba96663b3dbce2 | quote: 每 5 小时最多约 40 次 prompts
- sources:
  - [1] https://docs.mthreads.com/kuaecloud/kuaecloud-doc-online/coding_plan/plan_overview

## Moore Threads AI

- `compute/moore-threads-ai` | trial-only | evidence reported | binding request-rate | category cloud VM
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T11:17:30.951Z (live) | stale on 2026-12-10
- url https://code.mthreads.com/
- free tier: Free Trial: CNY 0, limited to 100 developers a day, with usage equivalent to the Lite Plan, valid for 30 days from the day it is claimed; supports the latest GLM 4.7 open-source model and multiple mainstream coding tools. The page advertises this as a limited-time free trial. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-window
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: country-phone | country: CN
- interface: rest
- limits:
  - request-rate (binding): 100 signups a day is the first wall, then a 30-day clock; the page states no token allowance, so the daily quota is the constraint that visibly fails first. [1]
- limits note: 100 signups a day is the first wall, then a 30-day clock; the page states no token allowance, so the daily quota is the constraint that visibly fails first.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: It composes with any coding client that speaks an OpenAI-compatible or Anthropic-compatible endpoint, which is why the vendor lists Claude Code and Cline. It breaks at the identity step and at the daily cap, and the 30 days do not renew.
- reliability: no reliability event recorded
- notes: The vendor page states no signup gate at all, so the Chinese-mobile requirement is reported by a third party and not confirmed here; that is why the rung is reported and not documented. The prompt allowance inside the free window is not published; The Chinese source text is quoted here in translation to keep the file ASCII.
- extras:
  - facets.class: hardware-vendor-programme
  - facets.free_tier_kind: trial-window
  - facets.shape.gpu_class: Moore Threads MTT S5000
- evidence:
  - [1] 2026-10-22: 'domestic compute with a domestic model, a limited-time 30-day free trial' and 'Free Trial: CNY 0, limited to 100 developers a day', translated from the live page read
  - [1] 2026-10-22: the page states the service runs on MTT S5000 GPUs and serves GLM-4.7, translated, so the offer is accelerator-hosted inference rather than a resold third-party API
  - [2] 2026-10-22: a deal aggregator records the gate as a Chinese mobile number and reports the vendor page did not state one; the aggregator dates the offer at 2026-10-11
  - [1] 2026-11-25: the vendor page states a CNY 0 free trial for 100 developers a day, Lite-equivalent usage, 30 days from claim, GLM-4.7 and multiple coding tools | capture: sha256:7a906621919fe99ce165240ce7cdcf596c45b0539d974d6fedb3bfaa18397a2f | quote: 限时免费 #### Free Trial ¥ 0每日限量 100 名开发者 与 Lite Plan 套餐用量相当 面向轻量工作负载的开发者 支持最新 GLM 4.7 开源模型 适用于多款主流编程工具 领取成功之日起 30 天内有效
  - [2] 2026-11-25: a deal aggregator translates the vendor page: free trial at CNY 0 for 100 developers a day, Lite-equivalent usage, 30 days from claim, usable from Claude Code, Cursor, OpenCode and Cline | capture: sha256:24da4f8945a68618c454ef675f3f4dbd5d10e22a0f12ab615f3c31f6f680e1e1 | quote: Free Trial 档 0 元：每日限量 100 名开发者领取，用量与 Lite Plan 相当（官方称为 Claude Pro 套餐的 3 倍用量），领取成功之日起 30 天内有效，可接入 Claude Code、Cursor、OpenCode、Cline、Kilo Code、Roo Code
  - [1] 2026-11-25: the vendor page still states a CNY 0 free trial for 100 developers a day, Lite-equivalent usage, 30 days from claim, GLM-4.7 and multiple coding tools | capture: sha256:7a906621919fe99ce165240ce7cdcf596c45b0539d974d6fedb3bfaa18397a2f | quote: 限时免费 #### Free Trial ¥ 0每日限量 100 名开发者 与 Lite Plan 套餐用量相当 面向轻量工作负载的开发者 支持最新 GLM 4.7 开源模型 适用于多款主流编程工具 领取成功之日起 30 天内有效
- sources:
  - [1] https://code.mthreads.com/
  - [2] https://lanmao.ai/zh/o/mthreads-ai-coding-plan-free-trial/
