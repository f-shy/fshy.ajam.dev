# Teldrive

> github.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-tgdrive/ | JSON https://fshy.ajam.dev/api/v1/entity/github-tgdrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Teldrive

- `debrid/teldrive` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding per-object-cap | category software (Telegram-backed drive, self-hosted) | tier self-hosted
- needs card no, phone yes, ID no, institution no | verified 2026-10-23T01:52:23.000Z (live) | stale on 2026-11-23
- url https://github.com/tgdrive/teldrive
- free tier: No fee. 'Teldrive requires PostgreSQL and a Telegram account.' The bytes go into the account's own Telegram channels; the software is MIT-licensed. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-23 | source: [1] | note: 'unlimited' is Telegram's own claim about the account, not Teldrive's about itself
- per-object cap: Inherits Telegram's per-object ceiling: 2 GB on a free account, 4 GB with Premium. | source: [2] | note: Teldrive states no cap of its own
- retention: As long as the Telegram account and the channel survive. The project warns: 'Accounts and stored files can become unavailable; keep independent backups.' | source: [1]
- egress: Telegram's own terms; downloads come from Telegram's media DCs, at the speed a free account is allowed. | metered: no | free allowance: no allowance published | source: [2]
- identity: any-phone | detail: A Telegram account plus api_id/api_hash, and a PostgreSQL instance that must be run. This is software, not a hosted service.
- interface: rest, rclone, cli
- limits:
  - per-object-cap (binding): 2 GB free / 4 GB Premium, governed by Telegram [2]
  - request-rate: Telegram flood control applies to the account Teldrive drives [3]
- binding note: Teldrive cannot change the object ceiling; it only hides it. At 1 TiB/month the 2 GB cap still splits every large object, and the account's upload flood limits (FLOOD_PREMIUM_WAIT_X on a non-Premium account) shape the rate.
- interface detail: 'Telegram-backed file storage with a web interface, an HTTP API, and rclone integration.' Login is by Telegram account, and channels are synced from the UI.
- tooling: Linux/Windows binaries, Nix, Docker or Podman; a maintained rclone fork (tgdrive/rclone) supplies the backend. PostgreSQL is mandatory.
- composes with: Turns a set of Telegram channels into one mounted filesystem, which is the only way to make the per-object cap stop being the unit of work: the user sees files, the backend shards them.
- reliability: The project ships its own warning: 'Follow Telegram's terms and API limits. Accounts and stored files can become unavailable; keep independent backups.' A ban takes the whole drive with it.
- notes: This is software that must be run locally, unlike every bot among debrid providers. It is included because it is the only maintained path that presents Telegram as a filesystem, and because the free compute tier can host it; abandon if the PostgreSQL requirement or the rclone fork stops being maintained.
- evidence note: Requirements and the data-safety sentence are from the repository read. No instance was deployed, so the effective throughput is unmeasured.
- self hosted: yes
- evidence:
  - [1] 2026-10-23: 'Teldrive requires PostgreSQL and a Telegram account.' and 'Telegram-backed file storage with a web interface, an HTTP API, and rclone integration.'
  - [1] 2026-10-23: 'Follow Telegram's terms and API limits. Accounts and stored files can become unavailable; keep independent backups.'
  - [4] 2026-10-23: 'organize your Telegram files and unlock their full potential as cloud storage' with an rclone mount and optional encryption
- sources:
  - [1] https://github.com/tgdrive/teldrive
  - [2] https://telegram.org/faq
  - [3] https://core.telegram.org/api/errors
  - [4] https://teldrive-docs.pages.dev/docs/
