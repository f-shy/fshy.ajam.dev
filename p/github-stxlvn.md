# Torrs

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-stxlvn/ | JSON https://fshy.ajam.dev/api/v1/entity/github-stxlvn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Torrs (self-hosted torrent-to-Telegram bot)

- `debrid/torrs` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding per-object-cap | category software (torrent to Telegram file, self-hosted) | tier self-hosted
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://github.com/stxlvn/Torrs
- free tier: No fee. A self-run bot: magnet, hash or .torrent in, selected files out into the chat. Requires a Telegram bot token and, for the full path, a local Bot API server. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Files above 1.9 GB are split into 7-Zip volumes because 'the self-hosted Bot API server limit is 2 GB per file'. | source: [1] | note: 1.9 GB is the project's own safety margin under the 2 GB ceiling
- retention: Whatever the chat keeps; the project caches by Telegram file_id so a repeat request re-sends instead of re-downloading. | source: [1]
- egress: Telegram's; the bot's host carries the swarm traffic and the upload. | metered: no | free allowance: no allowance published | source: [2]
- identity: any-phone | detail: api_id/api_hash from my.telegram.org, hence a phone-registered Telegram account, plus a host to run TorrServer and the Bot API server.
- interface: rest, cli
- limits:
  - per-object-cap (binding): 1.9 GB split threshold under the 2 GB local Bot API limit [1]
  - per-object-cap (binding): 50 MB without a local Bot API server [1]
- binding note: The project documents the sequence exactly: 50 MB without a local server, 2 GB with one, and a 1.9 GB split above that. Nothing about flood control appears, because at these object counts it does not bind.
- interface detail: A Telegram chat in front of TorrServer, plus a CLI-style configuration; lossless FLAC needs a second, user-account (MTProto) session because the Bot API only accepts .mp3/.m4a audio.
- tooling: Docker or source, TorrServer, and the tdlib Bot API server for the >50 MB path; 7-Zip is mandatory for objects above 1.9 GB.
- composes with: The reference implementation of the whole lane: a torrent leeched on somebody else's VM, uploaded to Telegram through a local Bot API server, split at 1.9 GB, and re-sent by file_id on request.
- reliability: A ban risk the project acknowledges in its own README; a self-run stack also means the Bot API server must be moved with logOut or updates are lost.
- notes: Software, not hosted. It is the only source found that states the 50 MB -> 2 GB -> 1.9 GB-split chain in one place, which makes it the best independent confirmation of the platform caps among debrid providers. Abandon if the README's limit table changes.
- evidence note: The 50 MB / 2 GB / 1.9 GB progression is stated in the project's README read. Nothing was built.
- self hosted: yes
- evidence:
  - [1] 2026-10-23: 'files larger than 1.9 GB are automatically split into 7-Zip volumes (the self-hosted Bot API server limit is 2 GB per file)'
  - [1] 2026-10-23: 'without it Telegram cuts file uploads to 50 MB, with it the limit is 2 GB'
  - [1] 2026-10-23: for lossless FLAC a second Telegram account ('userbot', via MTProto) is used because the Bot API only accepts .mp3/.m4a for sendAudio
- sources:
  - [1] https://github.com/stxlvn/Torrs
  - [2] https://telegram.org/faq
