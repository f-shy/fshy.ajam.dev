# Poe bot knowledge bases

> poe-developers.gitbook.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/poe-developers/ | JSON https://fshy.ajam.dev/api/v1/entity/poe-developers.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Poe bot knowledge bases

- `storage/poe-bot-knowledge-bases` | fails-quota | evidence reported | binding retention-clamped | category AI bot platform / knowledge base
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://poe-developers.gitbook.io/documentation/prompt-bots/how-to-create-a-prompt-bot
- free tier: 5 GB or 30 million characters per knowledge base, combined across all sources of one bot. One knowledge base per bot. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Uploads to temporary chats are 'retained for up to 15 days for safety review before being permanently deleted'; regular chats' files are 'permanently deleted within 24 hours of creation'. | days: 1 | source: [1] | note: not stated
- egress: No egress concept; bot answers are served by Poe. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - retention-clamped (binding): deleted within 24 hours [1]
  - write-gated: review before being permanently deleted' [1]
- limits note: per-knowledge-base-cap 5 GB / 30M chars. Uploads to temporary chats are 'retained for up to 15 days for safety review before being permanently deleted'; regular chats' files are 'permanently deleted within 24 hours of creation'.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: Creator UI + `poe-api-wrapper` (unofficial); server bots can accept attachments via `allow_attachments`
- tooling: poe-api-wrapper (unofficial Python), fastapi_poe for server bots
- composes with: 5 GB per bot, and bot creation is free and effectively unbounded, so each bot holds the same 5 GB allowance. That is the only axis on which the total grows, and it is a manual, per-bot upload loop.
- reliability: Knowledge base uploads allow 5 GB per bot with unlimited bot creation. Read access is restricted to model retrieval prompts without documented bulk export endpoints. Rate limits vary by underlying model.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 5 GB or 30 million characters per knowledge base, combined across all sources of one bot. One knowledge base per bot.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'The size of each knowledge base is limited to 5GB or 30 million characters combined across all knowledge sources.'
  - [2] 2026-10-21: 'permanently deleted within 24 hours of creation. Files you upload to a temporary chat are retained for up to 15 days'
  - [3] 2026-10-21: `allow_attachments` default False
- sources:
  - [1] https://poe-developers.gitbook.io/documentation/prompt-bots/how-to-create-a-prompt-bot
  - [2] https://help.poe.com/hc/en-us/articles/19944206309524-Poe-FAQs
  - [3] https://creator.poe.com/docs/server-bots/enabling-file-upload-for-your-bot
