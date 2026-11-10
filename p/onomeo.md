# onomeo

> onomeo.com | Inference; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onomeo/ | JSON https://fshy.ajam.dev/api/v1/entity/onomeo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## onomeo

- `inference/onomeo` | paid-only | evidence documented | binding request-rate | category inference gateway, public beta, balance-billed models; free models removed
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:15:50.267Z (live) | stale on 2026-12-05
- url https://onomeo.com/models
- free tier: none for API calls on the catalogue read: all 17 listed models are paid and the free-chat, free-code and free-vision models are listed as removed this week; invite trials and earned rewards cover selected answers in browser chat only and do not cover API calls | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: a third-party listing reports 30 free-model calls every 5 hours per account; that offer is not on the first-party pages read
- per-object cap: not applicable
- retention: not applicable
- egress: metered: no
- identity: email | detail: sign in with an email code, Google, GitHub or Discord; no password and no card needed; new accounts per network are capped at 3 a day
- interface: rest
- limits:
  - request-rate (binding): up to 12 requests a minute per key [1]
  - volume-quota: balance in dollars; accounts without a balance get API answers that end with a '- via onomeo.com' line [2]
- binding note: 12 requests a minute per key
- endpoint: https://onomeo.com/v1/chat/completions
- tooling: OpenAI-compatible client with one key; also Anthropic and Gemini request formats for paid models
- composes with: top-up from $5, balance never expires
- reliability: public beta with no uptime promise; the models table lists availability between 50% and 100% over 7 days
- notes: the third-party figure of 30 calls every 5 hours predates the removal of the free models
- evidence:
  - [1] 2026-11-04: the Removed list of this week's changes names free-chat, free-code and free-vision | capture: sha256:559b882770530e60b878faccb5aa12bf3c5c5b44451bc47958758786ef8b30b4 | quote: codestral-latestfree-chatfree-codefree-visionglyph-clusterhy4-previewminimax-m2.7qwen-flash-character
  - [1] 2026-11-04: sign-in methods and no card | capture: sha256:559b882770530e60b878faccb5aa12bf3c5c5b44451bc47958758786ef8b30b4 | quote: - Sign in with an email code, Google, GitHub or Discord. No password and no card needed.
  - [1] 2026-11-04: the per-key request rate | capture: sha256:559b882770530e60b878faccb5aa12bf3c5c5b44451bc47958758786ef8b30b4 | quote: - Up to 12 requests a minute per key.
  - [3] 2026-11-04: rewards do not cover API calls | capture: sha256:7a07235e992fe87b931cc0c8dc488422d0367ebfba67c5eff1d3d23663e9028e | quote: Earned rewards can cover eligible answers in browser chat; they do not cover image generation or API calls.
  - [4] 2026-11-04: the sign-up cap per network | capture: sha256:f87797fd3f3b1b0b86e1e3d0f6a4b1ffd2a9aea9ce66587823855b5fc52de268 | quote: New accounts per network are capped at 3 a day.
  - [5] 2026-11-04: a third-party listing reports 30 free-model calls every 5 hours | capture: sha256:faea35e8a1d9320370a2e0251bc7177a58a804deb6f3afc12535d5daf06a3d73 | quote: Its free tier gives 30 free-model calls every 5 hours per account (12 requests per minute per key)
- sources:
  - [1] https://onomeo.com/models
  - [2] https://onomeo.com/integrations
  - [3] https://onomeo.com/help
  - [4] https://onomeo.com/terms
  - [5] https://free-llm.com/provider/onomeo
