# DirectURLBot Link Bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-directurlbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-directurlbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DirectURLBot Link Bot (@DirectURLBot)

- `debrid/telegram-directurlbot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T07:37:11.506Z (live) | stale on 2026-12-04
- url https://t.me/DirectURLBot
- free tier: The page describes a Telegram files-to-link bot; no price, quota or daily count is stated. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the bot's page states no per-file cap; Telegram's own file ceiling is 2 GB (4 GB with Premium). | source: [2]
- retention: unverified: the bot's page states no storage window or link lifetime. | source: [1]
- egress: No traffic allowance or price is stated on the bot's page. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account, which is logged in with a mobile phone number; no key or card is asked on the bot's page.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB per file on a free Telegram account (4 GB with Premium); the bot states no cap of its own [2]
- binding note: The only number that can be named from evidence is the per-file ceiling; the bot publishes no quota.
- interface detail: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- tooling: Any Telegram client; a Telegram account is required to start the bot.
- composes with: A link to a stored Telegram file, read over HTTP without the Bot API's 20 MB getFile cap.
- reliability: Support is by direct message to @FlixHelpBot; no status page or capacity is published.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: FILE TO LINK | capture: sha256:0828c273ed6f5b5a370829c22f9e299d19c4ec0059d2a7e2225e4036506f72eb | quote: FILE TO LINK
  - [2] 2026-11-03: a Telegram account is logged in with a mobile phone number | quote: Just use your main mobile phone number to log in everywhere, your cloud chats will sync instantly.
  - [2] 2026-11-03: Telegram's own per-file ceiling is 2 GB, or 4 GB with Premium | quote: up to 2 GB in size each (or 4 GB with
- sources:
  - [1] https://t.me/DirectURLBot
  - [2] https://telegram.org/faq
