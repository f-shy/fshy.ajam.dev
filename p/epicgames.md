# Epic Online Services Player Data Storage

> epicgames.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/epicgames/ | JSON https://fshy.ajam.dev/api/v1/entity/epicgames.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Epic Online Services Player Data Storage

- `storage/epic-online-services-player-data-storage` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://dev.epicgames.com/docs/epic-online-services/player-and-game-data/player-data-storage-interface/player-data-storage-overview
- free tier: 400 MB total storage per user, 200 MB maximum per file, 1,000 files per user. No published product-level or title-level byte cap. | unit: MB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 200 MB maximum per file | bytes: 200000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No per-GB egress meter documented for Player Data Storage; access is metered as API requests. EOS itself is free for all developers. | metered: yes
- identity: anonymous
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 200 MB per file [1]
- limits note: Per-object-cap: 200 MB per file and 64-character filename limit; request-rate: ~1,000 read or write requests per minute per user, then EOS_PlayerDataStorage_UserThrottled; per-object-cap: 1,000 files per user. Retention: none stated. Files persist until explicitly deleted; no expiry found. Data is encrypted at rest with a client-side key EOS never stores, so losing the key loses the bytes.
- interface detail: part of limits note
- tooling: EOS SDK (C/C++), C# and Unreal plugins (PlayEveryWare/eos_plugin_for_unity). File ops are chunked read/write callbacks: EOS_PlayerDataStorage_WriteFile / ReadFile / QueryFileList. No rclone backend.
- composes with: 400 MB per ProductUserId x unlimited free player identities. EOS supports anonymous/device auth, so identities are mintable at will; each new ProductUserId is a fresh 400 MB bucket. 2,500 identities = 1 TB.
- reliability: Throttles writes (not errors) once the 400 MB per-user total is reached until files are deleted; quota is per-deployment so a busy title can hit service-level allocation failures.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: filename format, 64-char limit, encryption-key requirement, 'Data that you store through this interface is accessible to players (users) on any device'
  - [2] 2026-10-21: quotas table 'Maximum individual file size 200 MB / Total storage space per user 400 MB / Maximum files per user 1000' (secondary source, corroborates the SDK error codes EOS_Result_PlayerDataStorageFileSizeTooLarge and _UserThrottled)
  - [3] 2026-10-21: 'Each service applies usage quotas on a per-deployment basis'
- sources:
  - [1] https://dev.epicgames.com/docs/epic-online-services/player-and-game-data/player-data-storage-interface/player-data-storage-overview
  - [2] https://grokipedia.com/page/Player_Data_Storage_Epic_Online_Services
  - [3] https://dev.epicgames.com/docs/epic-online-services/working-with-the-eos-sdk/conventions-and-limitations
