# Bothub

> bothub.ru | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bothub/ | JSON https://fshy.ajam.dev/api/v1/entity/bothub.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bothub

- `inference/bothub` | paid-only | evidence documented | binding volume-quota | category inference gateway, chat and Telegram bot
- needs card no, phone no, ID no, institution no | verified 2026-11-18T13:00:00.000Z (live) | stale on 2026-12-19
- url https://bothub.ru/
- free tier: The site says 'Start for free. Pay as you grow. No upfront costs'; the API model pages are a catalog of paid models and the captured page states no standing free token allowance. | unit: none | metered on: unstated | read on: 2026-11-18 | source: [1]
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: registration gives access via web or Telegram; the captured page does not state a free API credit
- interface: rest
- limits:
  - volume-quota (binding): packages sold in RUB; token packs do not expire, no free API allowance stated [1]
- endpoint: https://openai.bothub.ru/v1
- tooling: a web interface or Telegram bot; the OpenAI-compatible endpoint requires a funded account
- composes with: the API route needs a balance, so the 'start free' claim is about the chat interface rather than a metered API allowance
- reliability: package validity is unlimited for individual plans and tokens do not burn
- evidence:
  - [1] 2026-11-18: the site advertises a free start with no upfront cost | capture: sha256:2d239b1199e5056147b93d8b4d9db21d2e669dfd76212d1d6e73523425d75895 | quote: Начните бесплатно. Платите по мере роста. Никаких предоплатных затрат
- sources:
  - [1] https://bothub.ru/
