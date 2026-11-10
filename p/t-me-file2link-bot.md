# File to Link

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-file2link-bot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-file2link-bot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File to Link (@file2link_bot)

- `debrid/telegram-file2link-bot` | fails-quota | evidence documented | binding per-object-cap | category hosted bot (Telegram file to link, 20 MB) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T15:05:37.414Z (live) | stale on 2026-12-04
- url https://t.me/file2link_bot
- free tier: The page offers 'get download link for any telegram file'; no price or quota is stated. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
- per-object cap: 'size limit is 20MB' on the bot's own page; for larger files the page points to @getpubliclinkbot. | source: [1]
- retention: unverified: the bot's page states no storage window or link lifetime. | source: [1]
- egress: No traffic allowance or price is stated on the bot's page. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account, which is logged in with a mobile phone number; no key or card is asked on the bot's page.
- interface: unknown
- limits:
  - per-object-cap (binding): 'size limit is 20MB' on the bot's own page [1]
- binding note: The only number that can be named from evidence is the per-file ceiling; the bot publishes no quota.
- interface detail: A Telegram chat with the bot; the result is a link or a file delivered into the chat. No HTTP API is published.
- tooling: Any Telegram client; a Telegram account is required to start the bot.
- composes with: Not a path for large objects: the bot page states a 20 MB limit and names @getpubliclinkbot for bigger files, which is the record to use.
- reliability: Single-operator bot; 18 058 monthly users are shown on the page.
- notes: Abandon if the t.me page stops resolving to a bot with a Start action.
- evidence note: The description is the bot's own, read on its t.me page. Liveness of the backend needs a Telegram account and was not tested. Any paid tier of the bot is unverified: behind a sign-up (it is reached from inside the bot, with a Telegram account); the bot's page states no price.
- evidence:
  - [1] 2026-11-03: the bot's own page states its offer: size limit is 20MB | capture: sha256:8fc677a69381ab9ade8f856824825d6f16a4434ca7130cf747aa6890ec93823b | quote: size limit is 20MB
  - [2] 2026-11-03: a Telegram account is logged in with a mobile phone number | quote: Just use your main mobile phone number to log in everywhere, your cloud chats will sync instantly.
  - [2] 2026-11-03: Telegram's own per-file ceiling is 2 GB, or 4 GB with Premium | quote: up to 2 GB in size each (or 4 GB with
  - [1] 2026-11-03: the page shows 18 058 monthly users | capture: sha256:8fc677a69381ab9ade8f856824825d6f16a4434ca7130cf747aa6890ec93823b | quote: 18 058 monthly users
  - [1] 2026-11-03: the bot's page still states a 20MB size limit and points larger files to @getpubliclinkbot, with no price or quota | capture: sha256:9889af960df6751d4b4df144e193f173b0280f441c9d84aa77922d464c35ae2f | quote: get download link for any telegram file, size limit is 20MB, for large files use our
- sources:
  - [1] https://t.me/file2link_bot
  - [2] https://telegram.org/faq
