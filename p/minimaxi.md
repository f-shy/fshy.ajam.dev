# MiniMax Token

> minimaxi.com | Inference, Coding subscriptions; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/minimaxi/ | JSON https://fshy.ajam.dev/api/v1/entity/minimaxi.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## MiniMax (minimax.cn)

- `inference/minimax-cn` | paid-only | evidence documented | binding volume-quota | category inference API
- needs card no, phone yes, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://platform.minimaxi.com/docs/guides/quickstart
- free tier: No free text allowance stated; the quickstart requires account registration and an API Key, with pay-as-you-go or M Plan billing. Enterprise registration uses a main account with the registrant's name and phone number as administrator. | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: any-phone | detail: enterprise registration records the registrant's name and phone number as administrator | country: CN
- interface: rest
- limits:
  - volume-quota (binding): per-usage billing; no free text tier stated [1]
- endpoint: https://api.minimax.cn/anthropic/v1
- tooling: Anthropic SDK or OpenAI SDK by overriding the base URL
- composes with: no free tier published; usage requires a pay-as-you-go key or an M Plan seat or credits
- reliability: sub-accounts share the main account's usage rights and rate limits and are billed together
- notes: No self-serve free text allowance documented on the quickstart page.
- evidence:
  - [1] 2026-11-18: the China API requires registration and a key with pay-as-you-go or M Plan billing | capture: sha256:6e536e3a5ffc72249011298d988ab6be32fbb196fe5c4708e4d4470239d224bc | quote: 在开始使用 MiniMax API 之前，需要完成账户注册和 API Key 获取。
- sources:
  - [1] https://platform.minimaxi.com/docs/guides/quickstart

## MiniMax Token Plan (minimax.cn)

- `coding-subs/minimax-cn-coding-plan` | paid-only | evidence documented | binding volume-quota | category coding subscription
- needs card no, phone no, ID no, institution no | verified 2026-11-18T06:20:00.000Z (live) | stale on 2026-12-19
- url https://platform.minimaxi.com/docs/token-plan/intro
- free tier: No free tier for text or coding. M Plan has three paid tiers: Go, Explore and Build; Build is 12x the Go allowance on the China site. | unit: none | metered on: none | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable: the vendor serves the inference; no caller-stored bytes
- egress: not applicable | metered: no
- identity: email | detail: an M Plan account; no card gate or free signup allowance is stated on this page
- interface: rest, cli
- limits:
  - volume-quota (binding): monthly allowance by tier (Go 1x, Explore 3x, Build 12x); no free text allowance [1]
- endpoint: https://api.minimax.cn/anthropic/v1
- tooling: MiniMax Code agent app plus an M Plan API key for Claude Code, Codex, Cursor, OpenCode and other tools
- composes with: the monthly paid allowance is the scarce link; video generation consumes quota much faster than text
- reliability: MiniMax-M3.1-Flash-Preview was retired and redirected to MiniMax-M3.1-Flash
- evidence:
  - [1] 2026-11-18: M Plan has three paid tiers and no free text allowance | capture: sha256:95b089500d8fa4854e03ee2621548845f7552c03104e46bcf9a96ca79cb846c8 | quote: 订阅分为 Go、Explore 和 Build 三个档位
- sources:
  - [1] https://platform.minimaxi.com/docs/token-plan/intro
