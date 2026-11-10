# Telegram Drive

> telegram-drive.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/telegram-drive/ | JSON https://fshy.ajam.dev/api/v1/entity/telegram-drive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Telegram Drive (desktop, caamer20)

- `debrid/telegram-drive-desktop-caamer20` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding per-object-cap | category software (Telegram-backed drive, local-first desktop app) | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://telegram-drive.com/
- free tier: 'Every feature is free. The optional $5 license only removes sponsor placements.' Files live in the account's Saved Messages and channels; there is no separate storage account. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: again, 'unlimited' is Telegram's account claim
- per-object cap: 'The application caps a Telegram object at exactly 2,000,000,000 bytes.' and 'Files over 2 GB are skipped and logged.' | bytes: 2000000000 | source: [2] | note: 2,000,000,000 is the app's own hard cap, below Telegram's stated 2 GB
- retention: Until deleted from the account. The site answers the storage question with 'No. Storage and file handling follow Telegram's account, service, and per-file limits.' | source: [1]
- egress: Telegram's; the app streams from Telegram's media DCs and keeps only caches locally. | metered: no | free allowance: no allowance published | source: [3]
- identity: any-phone | detail: The account's own Telegram credentials; no account with the project.
- interface: unknown
- limits:
  - per-object-cap (binding): 2,000,000,000 bytes per object in the app [2]
  - per-object-cap (binding): 2 GB per object at Telegram [3]
- binding note: The app's own 2e9-byte cap is marginally stricter than Telegram's and is the one a user meets; neither leaves 1 TiB of monthly transfer with fewer than ~550 objects.
- interface detail: A GUI application over MTProto (Rust/Tauri/Grammers per the repository); no public HTTP API or CLI is documented. Desktop folder sync is the automation surface.
- tooling: Windows, macOS (Intel and Apple Silicon), Linux, Android and Google TV builds, released on GitHub.
- composes with: A client-side drive over one Telegram account: no server, no database, and a hard 2e9-byte object cap, so it composes with a free compute tier only as a sync target.
- reliability: The vendor's own warning: 'Telegram Drive should not be treated as literally unlimited storage or as the only backup of important data.' Files above 2 GB are skipped, not split.
- notes: Software, not a hosted service. Abandon if the 2e9 cap or the free-everything claim changes; the $5 licence is cosmetic and does not gate a feature.
- evidence note: Both the 2e9 cap and the skip behaviour are stated on the vendor's site and repository, read. No install was run.
- self hosted: yes
- evidence:
  - [1] 2026-10-23: 'Every feature is free. The optional $5 license only removes sponsor placements.' and 'No. Storage and file handling follow Telegram's account, service, and per-file limits.'
  - [1] 2026-10-23: 'Files over 2 GB are skipped and logged.' and 'Telegram-Drive currently limits a Telegram object to roughly 2 GB'
  - [2] 2026-10-23: 'The application caps a Telegram object at exactly 2,000,000,000 bytes.' and 'Telegram Drive should not be treated as literally unlimited storage'
- sources:
  - [1] https://telegram-drive.com/
  - [2] https://github.com/caamer20/Telegram-Drive
  - [3] https://telegram.org/faq
