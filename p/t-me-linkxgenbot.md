# LinkXGenBot 24-hour Link Bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-linkxgenbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-linkxgenbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LinkXGenBot 24-hour Link Bot (@LinkXGenBot)

- `debrid/telegram-linkxgenbot` | qualifies-with-caveat | evidence documented | binding retention-clamped | category hosted bot (Telegram file to link, 24-hour links) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:47.479Z (live) | stale on 2026-12-26
- url https://t.me/LinkXGenBot
- free tier: The page offers a file-to-link bot whose links expire after 24 hours; no price, quota or daily count is stated. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the bot's page states no per-file cap; Telegram's own file ceiling is 2 GB (4 GB with Premium). | source: [2]
- retention: 'The Generated Link will expire after 24 Hrs.' | days: 1 | source: [1]
- egress: No traffic allowance or price is stated on the bot's page. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account, which is logged in with a mobile phone number; no key or card is asked on the bot's page.
- interface: chat
- limits:
  - retention-clamped (binding): 1 day: the link expires after 24 hours [1]
- binding note: The only stated number is the 24-hour link life.
- interface detail: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- tooling: Any Telegram client; a Telegram account is required to start the bot.
- composes with: Links last one day, so it serves a same-day pull only; the stored Telegram file itself is not stated to expire.
- reliability: Support is through the group @HeimanSupport and the channel @HeimanSupports.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action. No programmatic path found: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: The Generated Link will expire after 24 Hrs. | capture: sha256:ccb83d02ad65388bf5ddabee88879ed841120b68b356d65daefcea612485b472 | quote: The Generated Link will expire after 24 Hrs.
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4
  - [2] 2026-11-03:  | capture: sha256:b2b47f4d10eef65f2241c8d0b8c905d5c40e0f31bcd2ba1962c5682609fd55b4 | quote: up to 2 GB in size each (or 4 GB with
  - [1] 2026-11-25: the bot's own page states a file-to-link service whose generated links expire after 24 hours | capture: sha256:c8d4c336659bc272d7f8da7b8a31dc7c2dcdbfaf5e1a2f6bbaf29b48e6b3c317 | quote: This is an File to Link Bot. The Generated Link will expire after 24 Hrs.
  - [1] 2026-11-25: the bot's own page names @HeimanSupport and @HeimanSupports for support | capture: sha256:c8d4c336659bc272d7f8da7b8a31dc7c2dcdbfaf5e1a2f6bbaf29b48e6b3c317 | quote: [@HeimanSupport](https://t.me/HeimanSupport) & [@HeimanSupports](https://t.me/HeimanSupports)
  - [2] 2026-11-25: Telegram login uses a mobile phone number | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63
  - [2] 2026-11-25:  | capture: sha256:db52c8ab9f1c97f8c3e07bd0bfdcad3b97224fa5ab080ee3807d1312a614ad63 | quote: Send and receive files of any type, up to 2 GB in size each (or 4 GB with
- sources:
  - [1] https://t.me/LinkXGenBot
  - [2] https://telegram.org/faq
