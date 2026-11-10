# Get Public Link Bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-getpubliclinkbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-getpubliclinkbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Get Public Link Bot (@getPublicLinkBot)

- `debrid/telegram-getpubliclinkbot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T07:37:11.506Z (live) | stale on 2026-12-04
- url https://t.me/getPublicLinkBot
- free tier: The page offers an external link for 'any Document File of any SIZE'; no price, quota or daily count is stated. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
- per-object cap: The bot states 'any SIZE'; no number is published. Telegram's own file ceiling is 2 GB (4 GB with Premium). | source: [1]
- retention: unverified: the bot's page states no storage window or link lifetime. | source: [1]
- egress: No traffic allowance or price is stated on the bot's page. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account, which is logged in with a mobile phone number; no key or card is asked on the bot's page.
- interface: unknown
- limits:
  - per-object-cap (binding): The bot states 'any SIZE' [1]
- binding note: The only number that can be named from evidence is the per-file ceiling; the bot publishes no quota.
- interface detail: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- tooling: Any Telegram client; a Telegram account is required to start the bot.
- composes with: The large-file companion of @file2link_bot, which sends files above its 20 MB limit here; the link is HTTP, so it is read without the Bot API's 20 MB getFile cap.
- reliability: Single-operator bot; the page directs problems to a FAQ inside the bot (behind a Telegram account), and shows 13 870 monthly users.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: Just Send Me any Document File of any SIZE i will Generate a External Link. | capture: sha256:ce95e5d287ce57fe0bba371a25a9c4414932b444208d4403a6951dacd442346d | quote: Just Send Me any Document File of any SIZE i will Generate a External Link.
  - [2] 2026-11-03: a Telegram account is logged in with a mobile phone number | quote: Just use your main mobile phone number to log in everywhere, your cloud chats will sync instantly.
  - [2] 2026-11-03: Telegram's own per-file ceiling is 2 GB, or 4 GB with Premium | quote: up to 2 GB in size each (or 4 GB with
  - [1] 2026-11-03: the page shows 13 870 monthly users | capture: sha256:ce95e5d287ce57fe0bba371a25a9c4414932b444208d4403a6951dacd442346d | quote: 13 870 monthly users
- sources:
  - [1] https://t.me/getPublicLinkBot
  - [2] https://telegram.org/faq
