# Epic Online Services Player Data Storage

> epicgames.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/epicgames/ | JSON https://fshy.ajam.dev/api/v1/entity/epicgames.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Epic Online Services Player Data Storage

- `storage/epic-online-services-player-data-storage` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:14.805Z (live) | stale on 2026-11-25
- url https://dev.epicgames.com/docs/epic-online-services/player-and-game-data/player-data-storage-interface/player-data-storage-overview
- free tier: 400 MB total storage space per user, 200 MB maximum individual file size, 1000 files per user | unit: MB | metered on: stored-bytes | read on: 2026-11-09 | source: [1]
- per-object cap: 200 MB maximum per file | bytes: 200000000 | source: [1] | note: not stated
- retention: Files that exceed the auto-delete file size are deleted following the upload. | source: [1] | note: the auto-delete file size is 400 MB
- egress: No per-GB egress meter documented for Player Data Storage; access is metered as API requests. EOS itself is free for all developers. | metered: yes
- identity: anonymous
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 200 MB per file [1]
- limits note: per-object-cap: 200 MB maximum individual file size; request-rate: 1000 read or write requests per minute; per-object-cap: 1000 files per user
- interface detail: rest
- tooling: EOS SDK (C/C++), C# and Unreal plugins (PlayEveryWare/eos_plugin_for_unity). File ops are chunked read/write callbacks: EOS_PlayerDataStorage_WriteFile / ReadFile / QueryFileList. No rclone backend.
- composes with: 400 MB per ProductUserId x unlimited free player identities. EOS supports anonymous/device auth, so identities are mintable at will; each new ProductUserId is a fresh 400 MB bucket. 2,500 identities = 1 TB.
- reliability: Throttles writes (not errors) once the 400 MB per-user total is reached until files are deleted; quota is per-deployment so a busy title can hit service-level allocation failures.
- notes: the same as the free tier
- evidence note: the cited page was read on 2026-11-09
- evidence:
  - [1] 2026-10-21: filename format, 64-char limit, encryption-key requirement, 'Data that you store through this interface is accessible to players (users) on any device'
  - [2] 2026-10-21: quotas table 'Maximum individual file size 200 MB / Total storage space per user 400 MB / Maximum files per user 1000' (secondary source, corroborates the SDK error codes EOS_Result_PlayerDataStorageFileSizeTooLarge and _UserThrottled)
  - [3] 2026-10-21: 'Each service applies usage quotas on a per-deployment basis'
  - [1] 2026-11-09: the Usage Limitations table gives the per-file cap, the auto-delete size, the per-user total, the file-count cap and the request rate | capture: sha256:5db07007d00e6efcf9b23fb4d63b95dcb88ecea52d3577f0632ee16c081e95ab | quote: | Usage Type | Limitation | | --- | --- | | Read or write | 1000 requests per minute | | Maximum individual file size (see note below) | 200 MB | | Auto-delete file size | 400 MB | | Total storage space per user | 400 MB | | Maximum files per user | 1000 |
  - [1] 2026-11-09: a file above the auto-delete size is deleted after upload | capture: sha256:5db07007d00e6efcf9b23fb4d63b95dcb88ecea52d3577f0632ee16c081e95ab | quote: Files that exceed the auto-delete file size are deleted following the upload.
- sources:
  - [1] https://dev.epicgames.com/docs/epic-online-services/player-and-game-data/player-data-storage-interface/player-data-storage-overview
  - [2] https://grokipedia.com/page/Player_Data_Storage_Epic_Online_Services
  - [3] https://dev.epicgames.com/docs/epic-online-services/working-with-the-eos-sdk/conventions-and-limitations
