# File To Direct Link Bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-filetodirectlinkbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-filetodirectlinkbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File To Direct Link Bot (@FileToDirectLinkBot)

- `debrid/telegram-filetodirectlinkbot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T07:37:11.506Z (live) | stale on 2026-12-04
- url https://t.me/FileToDirectLinkBot
- free tier: The page offers a 'permanent download and stream link for Telegram files'; no price, quota or daily count is stated. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
- per-object cap: unverified: the bot's page states no per-file cap; Telegram's own file ceiling is 2 GB (4 GB with Premium). | source: [2]
- retention: The page calls the link 'permanent'; no number of days is stated. | source: [1]
- egress: No traffic allowance or price is stated on the bot's page. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account, which is logged in with a mobile phone number; no key or card is asked on the bot's page.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB per file on a free Telegram account (4 GB with Premium); the bot states no cap of its own [2]
- binding note: The only number that can be named from evidence is the per-file ceiling; the bot publishes no quota.
- interface detail: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- tooling: Any Telegram client; a Telegram account is required to start the bot.
- composes with: A permanent link to a stored Telegram file, read over HTTP without the Bot API's 20 MB getFile cap.
- reliability: Single-operator bot; the link's permanence is the operator's claim and is unmeasured.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: Bot to get permanent download and stream link for Telegram files | capture: sha256:1ddf1c577a9fa449ad62a92d1fd2735cc71022ba50132b2e88734584b3c06769 | quote: Bot to get permanent download and stream link for Telegram files
  - [2] 2026-11-03: a Telegram account is logged in with a mobile phone number | quote: Just use your main mobile phone number to log in everywhere, your cloud chats will sync instantly.
  - [2] 2026-11-03: Telegram's own per-file ceiling is 2 GB, or 4 GB with Premium | quote: up to 2 GB in size each (or 4 GB with
  - [1] 2026-11-03: the bot's description: a permanent download and stream link for Telegram files | capture: sha256:2c8b99f5e799b50a2ddf551ac85bc336954af3f8278a53c970d622a9d2f37673 | quote: Bot to get permanent download and stream link for Telegram files
  - [2] 2026-11-03: Telegram's per-file ceiling is 2 GB, 4 GB with Premium | quote: Send and receive files of any type, up to 2 GB in size each (or 4 GB with [Premium](https://telegram.org/faq_premium)), access them instantly on your other devices.
- sources:
  - [1] https://t.me/FileToDirectLinkBot
  - [2] https://telegram.org/faq
