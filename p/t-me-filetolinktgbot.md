# File Stream

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-filetolinktgbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-filetolinktgbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File Stream (@FileToLinkTGbot)

- `debrid/telegram-file-to-link-tg-bot` | qualifies-with-caveat | evidence documented | binding per-object-cap | category hosted bot (Telegram file to HTTP link) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://t.me/FileToLinkTGbot
- free tier: Free to use, no account: 'This bot generate direct download link of Telegram Files.' No quota, rate limit or file-size cap appears on the bot's page. | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: the absence is not a measurement of capacity
- per-object cap: Not published. The only documented ceiling is Telegram's 2 GB per object. | source: [2]
- retention: The file stays in the chat it was posted in; the bot's link lifetime is not stated on its page. | source: [1]
- egress: Free, and the point of the bot: it hands back an HTTP link, which sidesteps the Bot API's 20 MB getFile ceiling by streaming through the vendor's own Telegram session. | metered: no | free allowance: not published | price per TB: the mechanism is inferred from what the bot does, not from a statement about its account | source: [1]
- identity: any-phone | detail: A Telegram account to message the bot; no token, key or email is requested.
- interface: rest
- limits:
  - per-object-cap (binding): 2 GB, Telegram's own object ceiling; the bot states none [2]
- binding note: Nothing else is published. At 1 TiB/month the object ceiling is reachable and the vendor's own throttling is unknown, so the honest binding is the documented one.
- interface detail: A Telegram chat: send or forward a file, receive a URL.
- tooling: Any Telegram client; the returned URL works in a browser, VLC or a download manager with range requests.
- composes with: The cheapest way past the 20 MB getFile wall without running a server: a file already in Telegram becomes a plain HTTP URL, so a script never touches the Bot API's download path.
- reliability: A single-operator bot with no published capacity: its links can expire or disappear without notice, and nothing in the page says how long it keeps a session alive.
- notes: Abandon if the page stops resolving or loses the description. Its value is structural (an MTProto-backed URL) rather than quantitative, so do not quote a quota for it until one is measured.
- evidence note: The bot exists and describes itself this way today. Its cap is `unverified`: no file was sent, so the record rests on the platform ceiling, not on the operator's policy.
- evidence:
  - [1] 2026-10-23: 'This bot generate direct download link of Telegram Files.' - page resolves with a Start action, no monthly-user count shown
  - [3] 2026-10-23: 'Use the getFile method. Please note that this will only work with files of up to 20 MB in size.' - the limit this class of bot exists to bypass
- sources:
  - [1] https://t.me/FileToLinkTGbot
  - [2] https://telegram.org/faq
  - [3] https://core.telegram.org/bots/faq
