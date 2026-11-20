# Telegram Bot API server

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-tdlib/ | JSON https://fshy.ajam.dev/api/v1/entity/github-tdlib.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Telegram Bot API server (self-hosted, --local mode)

- `debrid/telegram-bot-api-local-server` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding per-object-cap | category bot API gateway (software, self-hosted) | tier self-hosted
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://github.com/tdlib/telegram-bot-api
- free tier: No fee to Telegram. The cost is a host: the server must run somewhere with outbound internet. 'The only mandatory options are --api-id and --api-hash.' | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: the account's own 2 GB free / 4 GB Premium per-file ceiling still applies to a user session; this record is about the bot gateway
- per-object cap: In local mode the server 'Upload[s] files up to 2000 MB' and 'Download[s] files without a size limit.' | source: [1] | note: '2000 MB' is the vendor's own wording; no byte-exact boundary is published
- retention: Not applicable: a gateway. Bytes live in the chat they were sent to, not on the server. | source: [1]
- egress: No separate charge from Telegram. The host's outbound bandwidth is the part that is metered, by whoever runs the host. | metered: no | free allowance: none published | source: [1]
- identity: any-phone | detail: my.telegram.org issues api_id/api_hash to a Telegram account, and a Telegram account is registered to a phone number. No card and no email are required for the app registration.
- interface: rest
- limits:
  - per-object-cap (binding): 2000 MB per upload in --local mode (50 MB on api.telegram.org) [1]
  - write-gated: requires api_id and api_hash from my.telegram.org [1]
- limits note: Download has no size limit in local mode; upload does. The asymmetry is the reason a mirror bot can pull a 2 GB file but still split anything above 2 GB.
- binding note: At 1 TiB/month this still fails first: no object above 2000 MB can be sent, so the month is 512+ objects at best. Flood control is nowhere near binding (see telegram-uploadbot).
- interface detail: HTTP JSON API. 'By default the Telegram Bot API server is launched on the port 8081, which can be changed using the option --http-port.' The server 'accepts only HTTP requests, so a TLS termination proxy needs to be used to handle remote HTTPS requests.'
- endpoint: http://127.0.0.1:8081 (default --http-port)
- tooling: Docker image or CMake build of tdlib/telegram-bot-api; any Bot API client library can be pointed at it. The state-of-the-art in-the-wild user is the Torrs bot, which runs the server to lift its own 50 MB ceiling.
- composes with: Raises a bot from 50 MB per upload and 20 MB per download to 2000 MB and unlimited, so a 2 GB file in a channel becomes retrievable by a script; needs a VM plus a TLS proxy, which a free compute tier supplies.
- reliability: One server per bot at a time: moving a bot requires logOut from api.telegram.org first, or updates are silently lost ('If the bot is logged in on more than one server simultaneously, there is no guarantee that it will receive all updates.').
- notes: Abandon this if Telegram ships the local-mode upload cap below 2 GB, or if the 2000 MB figure disappears from the README without a replacement. This is software that must be run locally, not a hosted service; it is recorded because it is the only documented way to make a bot a 2 GB path, and because hosted leech bots visibly depend on it.
- evidence note: The limit sentences are on the project README and the Bot API page, both read. A measured rung needs a 2 GB upload through a running instance; that was not done.
- self hosted: yes
- evidence:
  - [1] 2026-10-23: 'To enable Bot API features not available at https://api.telegram.org, specify the option --local. In the local mode the Bot API server allows to: Download files without a size limit. Upload files up to 2000 MB.' and the mandatory --api-id/--api-hash sentence
  - [1] 2026-10-23: 'If the bot is logged in on more than one server simultaneously, there is no guarantee that it will receive all updates.'
  - [2] 2026-10-23: 'If you switch to a local Bot API server, your bot will be able to: Download files without a size limit. Upload files up to 2000 MB.' plus 'The majority of bots will be OK with the default configuration, running on our servers.'
  - [3] 2026-10-23: 'Page not found' on 2026-10-23, and the Wayback capture 20250718224518 of the same URL is the same 'Page not found' - there is no limits page to cite, so flood numbers come from bots/faq and api/errors
- sources:
  - [1] https://github.com/tdlib/telegram-bot-api
  - [2] https://core.telegram.org/bots/api
  - [3] https://core.telegram.org/api/limits
