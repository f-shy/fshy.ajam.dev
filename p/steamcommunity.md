# steam friends chat file transfer

> steamcommunity.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/steamcommunity/ | JSON https://fshy.ajam.dev/api/v1/entity/steamcommunity.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## steam friends chat file transfer

- `storage/steam-friends-chat-file-transfer` | fails-quota | evidence reported | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-04T01:24:43.354Z (live) | stale on 2026-11-19
- url https://steamcommunity.com/groups/SteamClientBeta/discussions/3/1760230157504631620/
- free tier: chat uploads are capped at 2048 MB (2GB) of temporary cloud storage over a rolling period of 60 days (user-reported) | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: about 30 MB per file (reported by one forum user on 2 Nov 2024) | source: [1] | note: not applicable
- retention: chat uploads count against the cap for about 60 days and then drop off (user-reported) | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- limits:
  - volume-quota (binding): 2048 MB (2GB) of chat uploads over a rolling period of 60 days (user-reported) [2]
- binding note: a user-reported rolling 60-day cap of 2048 MB on chat uploads; no first-party statement was found
- interface detail: not documented
- tooling: files are pasted or uploaded in the Steam client chat window; a public link and an API: unverified: not stated in the captured threads
- composes with: not recorded
- reliability: chat uploads are capped at 2048 MB (2GB) over a rolling period of 60 days (user-reported)
- notes: user-reported limit: 2048 MB (2GB) of chat uploads over a rolling period of 60 days; the per-file cap is in per_object_cap; no first-party statement was found
- evidence note: re-read on 2026-11-03: two Steam Client Beta forum threads on steamcommunity.com (the URLs of its 2026-11-03 evidence rows); both are user posts, so the 2048 MB rolling 60-day cap and the 30 MB per-file figure are user-reported and no first-party page states them
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: ~30 MB per file ceiling reported in the Steam Client Beta forum; P2P-ish, no public link, no API. Useless as storage.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: ~30 MB per file ceiling reported in the Steam Client Beta forum; P2P-ish, no public link, no API. Useless as storage.
  - [2] 2026-11-03: a forum user reports a 2048 MB cap on chat uploads over a rolling 60 days | capture: sha256:ea8d49305d99201f433c9c802a23fc00a606d92038b97882abe18579415c1eca | quote: But basically you have a rolling period of 60 days where you can have up to 2048 MB (2GB) of temporarily cloud storage which contains all your chat uploads from the previous 60 days.
  - [1] 2026-11-03: a forum user reports 30 MB as the maximum file size in Steam chat | capture: sha256:0d2a96382aa9a549c6eacba7e737b0a8dbdbc6ae7cc0337eee20da4027e386cb | quote: think 30mb is max
  - [1] 2026-11-03: files are pasted into the Steam chat window | capture: sha256:0d2a96382aa9a549c6eacba7e737b0a8dbdbc6ae7cc0337eee20da4027e386cb | quote: Of course i mean Ctrl + V.. Pictures.. thats more then 100MB? just curious..
  - [2] 2026-11-04: a forum user reports a 2048 MB cap on chat uploads over a rolling 60 days | capture: sha256:ea8d49305d99201f433c9c802a23fc00a606d92038b97882abe18579415c1eca | quote: But basically you have a rolling period of 60 days where you can have up to 2048 MB (2GB) of temporarily cloud storage which contains all your chat uploads from the previous 60 days.
- sources:
  - [1] https://steamcommunity.com/groups/SteamClientBeta/discussions/3/1760230157504631620/
  - [2] https://steamcommunity.com/groups/SteamClientBeta/discussions/3/4416425392685449291/?ctp=2&l=polish
