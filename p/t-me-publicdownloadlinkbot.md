# Public Download Link Bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-publicdownloadlinkbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-publicdownloadlinkbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Public Download Link Bot (@publicdownloadlinkbot)

- `debrid/telegram-publicdownloadlinkbot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link and stream) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:45.851Z (live) | stale on 2026-12-26
- url https://t.me/publicdownloadlinkbot
- free tier: The page offers 'a streaming link of any file on Telegram'; no price, quota or daily count is stated. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
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
- composes with: A streaming link to a stored Telegram file, read over HTTP without the Bot API's 20 MB getFile cap.
- reliability: Single-operator bot with an updates channel that carries no limits.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action. No programmatic path found: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: gives you a streaming link of any file on Telegram. | capture: sha256:f30be5f6d14d37a651ac4896b724c7b52ffead99e9f0ac3275e95da0813d43f4 | quote: gives you a streaming link of any file on Telegram.
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4 | quote: up to 2 GB in size each (or 4 GB with
  - [1] 2026-11-25: the bot's own page still offers a streaming link for any Telegram file | capture: sha256:d28628c0dfdebb3ae405239d5e74b2189cbc83e9e034a24db6dd8adc0a94a7f6 | quote: gives you a streaming link of any file on Telegram.
  - [1] 2026-11-25: the bot is still a Telegram chat with a Start action and no published HTTP API | capture: sha256:d28628c0dfdebb3ae405239d5e74b2189cbc83e9e034a24db6dd8adc0a94a7f6 | quote: [Start Bot](tg://resolve?domain=publicdownloadlinkbot)
  - [2] 2026-11-25:  | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63
  - [2] 2026-11-25:  | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63 | quote: send and receive files of any type, up to 2 GB in size each (or 4 GB with
- sources:
  - [1] https://t.me/publicdownloadlinkbot
  - [2] https://telegram.org/faq
