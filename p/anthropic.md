# Anthropic API

> anthropic.com | Coding subscriptions; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/anthropic/ | JSON https://fshy.ajam.dev/api/v1/entity/anthropic.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Anthropic Claude

- `coding-subs/claude-code` | qualifies-with-caveat | evidence documented | binding request-rate | category coding subscription
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T17:29:12.672Z (live) | stale on 2026-12-04
- url https://www.anthropic.com/pricing
- free tier: Free: USD 0, 'Limited usage every 5 hours and every week' with no number; chat, web search, file creation and code execution, memory, connectors, Artifacts. Claude Code is not included | unit: mixed | metered on: unstated | read on: 2026-10-22 | source: [1] | note: the Free column states 'Limited' for the 5-hour limit and the weekly limit with no number; Pro, Max and Ultra are multiples of Pro (1x, 5x, and 10x weekly with no 5-hour limit), so no column states an absolute usage
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: card | detail: an account for Free; a credit card for Pro, Max and Ultra. Max carries USD 100 a month and Ultra USD 200 a month in API credits
- interface: cli, rest
- limits:
  - request-rate (binding): usage is a multiple of Pro with no absolute number: Free 'Limited' every 5 hours and every week; Max 5x Pro every 5 hours and every week; Ultra no 5-hour limit and 10x Pro every week [1]
- interface detail: Claude Code is a CLI and is marked 'Claude Code included' on the Pro, Max and Ultra cards; the Free card has none
- tooling: Claude Code CLI; the Anthropic API separately
- composes with: Pro at USD 20 is the cheapest plan that includes Claude Code; Max adds API credits that can be spent on the same account
- reliability: no reliability event recorded
- notes: The individual ladder is Free, Pro (USD 17 a month annual or USD 20 monthly), Max (USD 100 a month, 5x Pro) and Ultra (USD 200 a month, 10x Pro weekly, no 5-hour limit for verified accounts). The earlier Max 20x tier is no longer listed.
- evidence note: prices and usage multiples are quoted from the vendor page. Usage is stated only as a multiple of Pro, never as an absolute number. The Max 20x tier read earlier is no longer listed; Ultra is the 10x weekly tier.
- evidence:
  - [1] 2026-10-30: Claude Code is sold on the paid plans only; the Free plan still excludes it | capture: sha256:5760cd794f0005a568c71cd1c9a256fe14e10f870b5aaf335b4173aaccbe6649 | quote: Claude Code is included in all paid plans.
  - [1] 2026-11-03: Free is Limited with no number, Pro is the 1x baseline, Max is 5x per 5 hours and per week, Ultra has no 5-hour limit and 10x per week; no 20x column | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: | Limit every 5 hours | Limited | 1x | 5x | No 5-hour limit‡ | | Limit every week | Limited | 1x | 5x | 10x |
  - [1] 2026-11-03: the Free card states a limited usage allowance per 5 hours and per week, with no number | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: Limited usage every 5 hours and every week
  - [1] 2026-11-03: the Free weekly limit is 'Limited', so the unit is not unlimited | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: | Limit every week | Limited | 1x | 5x | 10x |
  - [1] 2026-11-03: the plan table marks Claude Code No on Free and Yes on Pro, Max and Ultra | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: | Claude Code | No | Yes | Yes | Yes |
  - [1] 2026-11-03: Max includes $100 and Ultra $200 a month in API credits; Free and Pro none | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: | New Monthly API credits† | No | No | $100/month | $200/month |
  - [1] 2026-11-03: Pro is USD 17 a month with annual billing ($200 up front) or USD 20 monthly | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: Per month with annual subscription discount ($200 billed up front). $20 if billed monthly.
  - [1] 2026-11-03: a credit card pays for Pro, Max and Ultra; Free takes no payment method | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: | Credit card | n/a | Yes | Yes | Yes |
  - [1] 2026-11-03: Claude Code is absent from Free and present on Pro, Max and Ultra | capture: sha256:e335b934081c577d159ba3f1d46e37a87d17102da2c7de3983158e6c1a9514eb | quote: | Claude Code | No | Yes | Yes | Yes |
- sources:
  - [1] https://www.anthropic.com/pricing

## Anthropic API

- `coding-subs/anthropic-api` | paid-only | evidence documented | binding none | category inference API
- needs card yes, phone no, ID no, institution no | verified 2026-11-10T01:56:01.641Z (live) | stale on 2026-12-11
- url https://www.anthropic.com/pricing
- free tier: no free API tier is stated on the pricing page | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: not applicable | metered: no
- identity: card | detail: a card on the platform account
- interface: rest
- limits note: no vendor quota binds: the vendor does not serve the usage this record prices
- interface detail: a REST API with per-token pricing
- tooling: any Anthropic-compatible client
- composes with: the pay-as-you-go reference that makes a subscription comparable: a plan is cheap only relative to the API price of the same model
- reliability: no reliability event recorded
- notes: Kept as a record because the plan comparison is meaningless without the API price it substitutes for. no monthly subscription: the page prices input and output per million tokens and names no plan charged by the month.
- evidence note: the pricing page was read. The per-model API rates were not extracted in full, so this record carries no rate.
- evidence:
  - [1] 2026-10-22: no free API tier is offered; the page prices the consumer plans and states that Max includes USD 100 to USD 200 a month of API credits
  - [1] 2026-11-10: the pricing page prices input and output per million tokens and names no plan charged by the month | capture: sha256:8488d4d023473ae3ea934a74c0df362fdce7e0191303528b858c9eb028c0a98b | quote: Input $8 / MTok Output $40 / MTok
- sources:
  - [1] https://www.anthropic.com/pricing
