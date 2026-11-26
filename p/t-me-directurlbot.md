# DirectURLBot Link Bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-directurlbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-directurlbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DirectURLBot Link Bot (@DirectURLBot)

- `debrid/telegram-directurlbot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:45.852Z (live) | stale on 2026-12-26
- url https://t.me/DirectURLBot
- free tier: unverified: the first-party page now resolves to a bare Telegram contact page with no description, price, quota or daily count | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
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
- composes with: A link to a stored Telegram file, read over HTTP without the Bot API's 20 MB getFile cap.
- reliability: Support is by direct message to @FlixHelpBot; no status page or capacity is published.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action. No programmatic path found: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: FILE TO LINK | capture: sha256:0828c273ed6f5b5a370829c22f9e299d19c4ec0059d2a7e2225e4036506f72eb | quote: FILE TO LINK
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4 | quote: up to 2 GB in size each (or 4 GB with
  - [1] 2026-11-25: today's first-party t.me page is a bare contact page with no description, price or limit | capture: sha256:532c1d0bb5d27758d85d6d994a293305a8f6133ded1b3bef8ea6a9a489917802 | quote: Telegram: Contact @DirectURLBot
  - [1] 2026-11-25: the page offers only a Telegram Send Message link, not a Start Bot action or an HTTP API | capture: sha256:532c1d0bb5d27758d85d6d994a293305a8f6133ded1b3bef8ea6a9a489917802 | quote: Send Message
  - [2] 2026-11-25:  | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63
  - [2] 2026-11-25:  | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63 | quote: send and receive files of any type, up to 2 GB in size each (or 4 GB with
  - [3] 2026-11-25: the archived first-party page from 2026-04-25 was titled FILE TO LINK | capture: sha256:151be2922e3a1e451d7a77943766cf99047c4e970a85f2d0f8184f72edcf5f16 | quote: FILE TO LINK
  - [3] 2026-11-25: the archived page directed bug reports to @FlixHelpBot, matching the record's reliability note | capture: sha256:151be2922e3a1e451d7a77943766cf99047c4e970a85f2d0f8184f72edcf5f16 | quote: For Bugs Or Issues Message [@FlixHelpBot](https://t.me/FlixHelpBot)
- sources:
  - [1] https://t.me/DirectURLBot
  - [2] https://telegram.org/faq
  - [3] https://web.archive.org/web/20260425234356/https://t.me/DirectURLBot?provider=wayback
