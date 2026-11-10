# ddrive

> github.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-forscht/ | JSON https://fshy.ajam.dev/api/v1/entity/github-forscht.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ddrive (Discord as a filesystem)

- `storage/ddrive` | self-hosted, last resort | verdict qualifies-with-caveat | evidence reported | binding per-object-cap | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/forscht/ddrive
- free tier: Unlimited logical file size and unlimited total: 'Tested with storing 4000 GB of data on single discord channel'. Splits files into 24 MB chunks and fans them across webhooks. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: file size and unlimited total: 'Tested with storing 4000 GB | bytes: 4000000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Downloads are proxied by ddrive, which pulls refreshed signed URLs from Discord on demand. On the read path the only cost is your own egress. | metered: no
- identity: email
- interface: rest, ftp
- limits:
  - per-object-cap (binding): file size and unlimited total: 'Tested with storing 4000 GB [1]
- limits note: 24 MB chunk size; ~5 messages/5 s per channel even via webhook (~30 msg/min per webhook reported); metadata lives in Postgres. Lose the DB and 3 TB of chunks become unreachable in a channel (author notes a 3 TB cold start takes 30+ min).
- interface detail: rest
- tooling: github.com/forscht/ddrive, 533 stars, MIT, Node 16+ / Docker, REST API with OpenAPI 3.1 spec, Postgres for metadata, web UI. Companion: `tris203/disftp` (FTP front-end for Disbox).
- composes with: 1 Discord account x N webhook/channel pairs. Webhooks are used because 'Webhooks are not bound to a user's global rate limit' (Discord docs), so throughput scales with channel count rather than with the 50 req/s token budget.
- reliability: Viable and battle-tested at multi-TB scale, but every download depends on re-deriving a 24 h signed URL, so the front-end must be alive. Two major rewrites (v2 -> v4) invalidated old layouts.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: 'Tested with storing 4000 GB of data on single discord channel (With max file size of 16GB)'
  - [1] 2026-10-21: the project's own note, quoted: 'Now uses webhooks instead of bot/user tokens to bypass the discord rate limit', which is to say it routes around the per-token limit by using webhooks; 'I was able to upload file with 5GB of size in just 85 seconds'
  - [2] 2026-10-21: 'Webhooks are not bound to a user's global rate limit.'
- sources:
  - [1] https://github.com/forscht/ddrive
  - [2] https://docs.discord.food/topics/rate-limits
