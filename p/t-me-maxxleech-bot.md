# Leech Pro

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-maxxleech-bot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-maxxleech-bot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leech Pro (@MaxxLeech_Bot)

- `debrid/telegram-maxx-leech-bot` | qualifies-with-caveat | evidence reported | binding per-object-cap | category hosted bot (torrent or magnet to Telegram file) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-07
- url https://t.me/MaxxLeech_Bot
- free tier: Free to use: 'A powerful Torrent Leech Bot! With Permanent Thumbnail Support'. The operator's channel advertises 'Free to use: Support for files up to 4GB in size.' | unit: none | metered on: unstated | read on: 2026-10-23 | source: [1] | note: 4 GB exceeds the 2 GB free-account object ceiling, which implies the operator uploads through Premium or a user session; that is inference
- per-object cap: 'Support for files up to 4GB in size' on the operator's channel; Telegram's free-account ceiling is 2 GB. | source: [2] | note: 4 GB is the operator's claim; no byte-exact figure and no per-day quota
- retention: The leeched file is delivered into the requesting chat and follows cloud-chat retention; the operator states no storage window. | source: [3]
- egress: Free; the operator pulls the torrent and uploads the result to Telegram, so the local bandwidth is only the download. | metered: no | free allowance: not published | source: [1]
- identity: any-phone | detail: A Telegram account; the bot asks for no key.
- interface: rest
- limits:
  - per-object-cap (binding): 'up to 4GB in size' claimed by the operator [2]
  - request-rate: no daily count published [1]
- binding note: If the 4 GB claim holds it is the loosest object cap found on a free hosted bot. No volume figure is published, so no other kind can be named.
- interface detail: A Telegram chat: send a magnet or .torrent, pick files, receive them as Telegram documents.
- tooling: Any Telegram client. Two handles exist for the same bot (@maxxleech_bot and @MaxxLeech_Bot) and both resolve.
- composes with: Turns a magnet into a Telegram object without running a BitTorrent client or a seedbox; the 4 GB claim is the only public statement that a hosted bot beats Telegram's free 2 GB ceiling.
- reliability: A single-operator leech service; the channel already announces that 'Search result files will now be automatically deleted after 1 day', so delivered files can be transient.
- notes: Abandon if the 4 GB line disappears from the channel. The 4 GB claim is the single most interesting number in this class and the one most worth measuring.
- evidence note: The 4 GB figure is the vendor's own channel post, not a vendor limits page, and no file was leeched. A measured 3-4 GB leech would move it to measured.
- evidence:
  - [1] 2026-10-23: 'A powerful Torrent Leech Bot! With Permanent Thumbnail Support' and 'Bot By: @MaxxBots'
  - [2] 2026-10-23: channel post: 'Free to use: Support for files up to 4GB in size.' and 'Search result files will now be automatically deleted after 1 day.'
- sources:
  - [1] https://t.me/MaxxLeech_Bot
  - [2] https://t.me/MaxxBots
  - [3] https://telegram.org/faq
