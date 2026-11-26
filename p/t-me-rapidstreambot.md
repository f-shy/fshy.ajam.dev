# RapidStream

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-rapidstreambot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-rapidstreambot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RapidStream (@RapidStreamBot)

- `debrid/telegram-rapidstreambot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:47.478Z (live) | stale on 2026-12-26
- url https://t.me/RapidStreamBot
- free tier: The page offers a file-to-link bot that it calls 'fairly enough broken'; no price, quota or daily count is stated. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the bot's page states no per-file cap; Telegram's own file ceiling is 2 GB (4 GB with Premium). | source: [2]
- retention: unverified: the bot's page states no storage window or link lifetime. | source: [1]
- egress: No traffic allowance or price is stated on the bot's page. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account, which is logged in with a mobile phone number; no key or card is asked on the bot's page.
- interface: chat
- limits:
  - per-object-cap (binding): 2 GB per file on a free Telegram account (4 GB with Premium); the bot states no cap of its own [2]
- binding note: The only number that can be named from evidence is the per-file ceiling; the bot publishes no quota.
- interface detail: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- tooling: Any Telegram client; a Telegram account is required to start the bot.
- composes with: A link to a stored Telegram file; the bot page describes the feature set as broken, so it is a fallback only.
- reliability: The bot's page describes its feature set as partly broken.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action. No programmatic path found: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: A simple enough file to link bot with fairly enough broken features. | capture: sha256:b4bfd3a98c1b9ae72e2ef908c80b693092421d54fce56657e2ca12e1eec2e1ca | quote: A simple enough file to link bot with fairly enough broken features.
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4 | quote: up to 2 GB in size each (or 4 GB with
  - [1] 2026-11-25: the bot's own page still calls its feature set fairly enough broken | capture: sha256:5e857bd2ca9d431a016e545ce8c4499daff0096e0b1e62e887eed00571bee2cb | quote: A simple enough file to link bot with fairly enough broken features.
  - [2] 2026-11-25: Telegram login uses a mobile phone number | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63
  - [2] 2026-11-25:  | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63 | quote: Send and receive files of any type, up to 2 GB in size each (or 4 GB with
- sources:
  - [1] https://t.me/RapidStreamBot
  - [2] https://telegram.org/faq
