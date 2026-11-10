# URL Uploader

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-uploadbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-uploadbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## URL Uploader (@uploadbot)

- `debrid/telegram-uploadbot` | qualifies-with-caveat | evidence documented | binding volume-quota | category hosted bot (URL to Telegram file) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://t.me/uploadbot
- free tier: The bot's own description: 'Quick way to upload files to telegram by url. Maximum file size allowed 500MB Daily upload limit 1GB, /upgrade for more'. 18 717 monthly users on the same page. | unit: GB | metered on: uploaded-bytes | read on: 2026-10-23 | source: [1] | note: 1 GB/day is the published ceiling, not a measurement
- per-object cap: 'Maximum file size allowed 500MB' - a quarter of Telegram's own 2 GB object ceiling. | bytes: 500000000 | source: [1]
- retention: The fetched file is delivered into the chat that asked for it, so it follows cloud-chat retention; the bot's copy of the URL is not described. | source: [2] | note: no statement about the bot's own storage was found
- egress: No charge. Delivery is a normal Telegram file message, so a later scripted download is capped by the Bot API's 20 MB getFile limit unless the bot streams it over MTProto. | metered: no | free allowance: none published | source: [1]
- identity: any-phone | detail: A Telegram account is needed to message any bot. The bot asks for no API key, token or email of its own.
- interface: rest
- limits:
  - volume-quota (binding): 1 GB/day on the free tier [1]
  - per-object-cap: 500 MB per file [1]
- binding note: 1 GB/day is about 30 GB/month, so the day counter fails long before 1 TiB. The 500 MB object cap is the second wall and the 20 MB getFile cap only bites on retrieval.
- interface detail: A Telegram chat. Programmatic use means driving the Bot API or an MTProto client to send a URL to @uploadbot; there is no other endpoint.
- tooling: Any Telegram client; no API key, token or account with the operator.
- composes with: A free 500 MB-per-file URL fetch into Telegram, which is the cheapest way to park a public HTTP file in the cloud without running anything; the 1 GB/day ceiling makes it a per-object tool, not a store.
- reliability: An undocumented daily reset and an unpublished retrieval path: after the file lands, whether the bot can hand it back above 20 MB depends on machinery it does not describe.
- notes: Abandon if the description loses the 1 GB/day line or the monthly-user count falls to zero. The paid '/upgrade' tier's price was not read.
- evidence note: The quota sentences are the bot's own Telegram description, read, with its monthly-user count. What would raise it: one measured upload at the stated cap and one retrieval above 20 MB.
- evidence:
  - [1] 2026-10-23: 'Quick way to upload files to telegram by url. Maximum file size allowed 500MB Daily upload limit 1GB, /upgrade for more', with 18 717 monthly users
  - [3] 2026-10-23: 'Use the getFile method. Please note that this will only work with files of up to 20 MB in size.' - the ceiling on retrieving what this bot stores
- sources:
  - [1] https://t.me/uploadbot
  - [2] https://telegram.org/faq
  - [3] https://core.telegram.org/bots/faq
