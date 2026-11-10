# Torrent Bot

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-torrentobot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-torrentobot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Torrent Bot (@torrentobot)

- `debrid/telegram-torrentobot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (torrent leech to Telegram) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T15:25:57.139Z (live) | stale on 2026-12-04
- url https://t.me/torrentobot
- free tier: unverified: the bot's page states only its function ('I can leech torrent for you.') and a 'Start Bot' button; no price, quota, rate limit or file-size limit is stated, and whether use is free needs a started bot, behind a Telegram sign-up. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1]
- per-object cap: Not published. Telegram's 2 GB per file is the only documented ceiling. | source: [2]
- retention: Not stated; the leeched file stays in the chat that received it. | source: [1]
- egress: Telegram's own file delivery; no allowance stated. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account, which Telegram ties to a phone number; the bot asks for nothing more on its page.
- interface: unknown
- limits:
  - per-object-cap (binding): 2 GB per file, Telegram's own ceiling; the bot states none [2]
- binding note: No quota is published, so the platform's 2 GB object ceiling is the only documented wall.
- interface detail: A Telegram chat; the profile credits the operator handle @pelupabots.
- tooling: Any Telegram client. Nothing to install.
- composes with: A magnet or torrent goes in and the bot leeches it for the user and delivers it in Telegram, so the retrieval path rides on Telegram's 2 GB object ceiling.
- reliability: One operator; the page warns 'No porn or you will be banned', so a ban is a documented enforcement. Capacity, queueing and uptime are unmeasured.
- notes: Same class as debrid/telegram-torget-bot and debrid/telegram-maxx-leech-bot. Abandon if the handle stops resolving to a bot.
- evidence note: Only the bot's own description was read. No torrent was sent, so speed, size handling and queueing were not observed.
- evidence:
  - [1] 2026-11-03: the bot's description: it leeches a torrent for the user | capture: sha256:26521e8cd79d71ceda50e053d8540b966059c6f3fb45574f23be01e3bd760bca | quote: I can leech torrent for you.
  - [1] 2026-11-03: the bot states a ban rule for adult content | capture: sha256:26521e8cd79d71ceda50e053d8540b966059c6f3fb45574f23be01e3bd760bca | quote: Strong warning: ❌ No porn or you will be banned
  - [2] 2026-11-03: Telegram's per-file ceiling is 2 GB, 4 GB with Premium | quote: Send and receive files of any type, up to 2 GB in size each (or 4 GB with [Premium](https://telegram.org/faq_premium)), access them instantly on your other devices.
  - [1] 2026-11-03: the page states the bot's function and nothing about price or allowance | capture: sha256:4f49f597ba86b205904e46bccfe7dc849f7624379147a40e1996186008ad5bd4 | quote: I can leech torrent for you.
  - [1] 2026-11-03: the profile credits the operator handle @pelupabots | capture: sha256:4f49f597ba86b205904e46bccfe7dc849f7624379147a40e1996186008ad5bd4 | quote: [@pelupabots](https://t.me/pelupabots)
- sources:
  - [1] https://t.me/torrentobot
  - [2] https://telegram.org/faq
