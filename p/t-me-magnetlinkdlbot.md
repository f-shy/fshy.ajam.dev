# Magnet Link Downloader

> t.me | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/t-me-magnetlinkdlbot/ | JSON https://fshy.ajam.dev/api/v1/entity/t-me-magnetlinkdlbot.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Magnet Link Downloader (@MagnetLinkDLBot)

- `debrid/magnetlinkdl` | qualifies-with-caveat | evidence reported | binding none | category Telegram torrent-to-link bot: magnet or torrent in, direct download link out | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-03T11:28:50.404Z (live) | stale on 2026-11-18
- url https://t.me/MagnetLinkDLBot
- price USD 0
- free tier: The bot's own profile is its whole offer: "Magnet Link Downloader" and "If not working then Try @MagnetLinkDL2Bot". No price, byte allowance or daily count is published anywhere on the preview page. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Free by default: no payment surface is reachable from the bot's page, and a paid tier that is not advertised is not a tier a client can buy.
- per-object cap: Not stated. | source: [1]
- retention: Not stated. The output is a link to a file held on the operator's seedbox; how long it survives is unpublished. | source: [1]
- egress: The bot resolves a torrent and serves the result as an HTTP link. No bandwidth terms, allowance or price is published. | metered: no | source: [1]
- identity: any-phone | detail: A Telegram account, so any phone number that can receive a code. No email, payment or document is asked for.
- interface: unknown
- limits:
  - request-rate: unstated; one concurrent job per chat is the usual Telegram-bot shape but is not published [1]
- limits note: Nothing is published. A fallback line ('If not working then Try @MagnetLinkDL2Bot') provides an alternate bot handle.
- binding note: No counter is published, so none can be named; what a client meets is a queue on a shared bot, and that is an availability limit rather than a quota. Recording 'none' here is a statement about the published record, not a claim that the bot is unlimited.
- interface detail: A Telegram bot only. There is no HTTP endpoint: the interface is a chat with @MagnetLinkDLBot, and the operator publishes a fallback bot (@MagnetLinkDL2Bot) rather than an API.
- tooling: Telegram client. Automating it means a Telegram user session against a third-party bot, which is the opposite of the programmatic access these records prefers.
- composes with: The cheapest known conversion from a torrent to an HTTP link with no client, no disk and no seeding: a magnet goes in, a link comes out, and the download happens elsewhere. It is the debrid function reduced to one chat, with no published capacity behind it.
- reliability: The operator runs a spare bot for when the main one breaks, which is an honest statement about uptime. A third-party bot sees every magnet a user submits, and the resulting link is served from infrastructure nobody in these records controls.
- notes: Documented as a service because it resolves and fetches: a magnet is supplied and a link to bytes comes back. The ledger's account-mirror bots (for example anything that clones into a user's own Drive) are excluded by that same test and listed in findings.md instead.
- evidence note: The service's existence and function come from its own Telegram profile, which is its operator's claim. No magnet was submitted, so neither the conversion nor any speed is measured. Moving up needs one torrent run end to end.
- extras:
  - fallback_bot: @MagnetLinkDL2Bot
- evidence:
  - [1] 2026-10-23: the bot is live and self-described as 'Magnet Link Downloader', with a named fallback @MagnetLinkDL2Bot and a support channel @TheNiceBots
  - [2] 2026-11-03: the support channel lists the operator's other bots and has 140,678 subscribers | capture: sha256:8a065f0d2756f2a61a46fc5bf0fc4a98349f099f122b570dd57552f052258858 | quote: 140 678 subscribers
  - [1] 2026-11-03: the bot page is live as 'Magnet Link Downloader', names the fallback bot @MagnetLinkDL2Bot and a help channel, and states no price, allowance or daily count | capture: sha256:174a15f0ec85185aa09a17ac8f2455b104c2ccc53079125c1547c8a2ca2ec965 | quote: If not working then Try
- sources:
  - [1] https://t.me/MagnetLinkDLBot
  - [2] https://t.me/TheNiceBots
