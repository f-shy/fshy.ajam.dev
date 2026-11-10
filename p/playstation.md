# playstation

> playstation.com | Storage, Netdisk and pan; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/playstation/ | JSON https://fshy.ajam.dev/api/v1/entity/playstation.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## playstation plus cloud storage

- `storage/playstation-plus-cloud-storage` | paid-only | evidence documented | binding volume-quota | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-03T15:03:51.459Z (live) | stale on 2026-12-04
- url https://www.playstation.com/en-us/support/subscriptions/ps5-ps-plus-cloud-storage/
- free tier: no free tier: cloud storage requires a PlayStation Plus membership; up to 100 GB of PS5 saved data and 100 GB of PS4 saved data, at most 1000 PS4 saved data files | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: a PlayStation Plus membership is required; what sign-up asks for: unverified: behind a sign-up
- interface: unknown
- limits:
  - volume-quota (binding): 100 GB of PS5 saved data and 100 GB of PS4 saved data [1]
  - volume-quota (binding): 1000 PS4 saved data files [1]
- binding note: cloud storage holds up to 100 GB of PS5 saved data and 100 GB of PS4 saved data, and at most 1000 PS4 saved data files
- interface detail: not documented
- tooling: the PlayStation console Saved Data settings (Upload to Cloud Storage and Download to console storage tabs); a public API is not documented on the vendor page
- composes with: not recorded
- reliability: part of the free tier
- notes: cloud storage for saved data: 100 GB for PS5 and 100 GB for PS4, at most 1000 PS4 saved data files; a PlayStation Plus membership is required
- evidence note: vendor pages captured 2026-11-03: https://www.playstation.com/en-us/support/subscriptions/ps5-ps-plus-cloud-storage/; every field that decides the verdict cites one of these captures
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 200 GB total (100 GB PS5 + 100 GB PS4, plus a 1,000-file cap on PS4 saves) and it is a paid subscription, not a free tier. No API — console UI only.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 200 GB total (100 GB PS5 + 100 GB PS4, plus a 1,000-file cap on PS4 saves) and it is a paid subscription, not a free tier. No API — console UI only.
  - [1] 2026-11-03: cloud storage requires a PlayStation Plus membership | capture: sha256:121f233668dde557ad1e4c5f847c952d049edc14840f7908abe8ac9c5618d938 | quote: Become a PlayStation Plus member to use cloud storage.
  - [1] 2026-11-03: cloud storage holds up to 100 GB of PS5 saved data and 100 GB of PS4 saved data, at most 1000 PS4 saved data files | capture: sha256:121f233668dde557ad1e4c5f847c952d049edc14840f7908abe8ac9c5618d938 | quote: You can save up to 100 GB of PS5 saved data and 100 GB of PS4 saved data. The number of PS4 saved data files you can store is limited to 1000.
  - [1] 2026-11-03: files move through the console Saved Data settings | capture: sha256:121f233668dde557ad1e4c5f847c952d049edc14840f7908abe8ac9c5618d938 | quote: 3. Select Download or Delete from Cloud Storage, and then go to the **Download to console storage **tab.
- sources:
  - [1] https://www.playstation.com/en-us/support/subscriptions/ps5-ps-plus-cloud-storage/

## PlayStation Plus cloud storage (Sony)

- `netdisk-pan/playstation-plus-cloud-storage` | fails-egress | evidence reported | binding write-gated | category console cloud saves
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:20:56.364Z (inherited) | stale on 2026-11-19
- url https://www.playstation.com/en-us/support/subscriptions/ps5-ps-plus-cloud-storage/
- price Bundled with PS Plus Essential at about USD 79.99/yr; 100 GB is not purchasable separately
- free tier: 100 GB for PS5 saves and 100 GB for PS4 saves, so 200 GB total, plus a hard limit of 1,000 PS4 save files. Requires an active PS Plus subscription | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 1,000 PS4 save files; no per-file byte cap published | source: [2]
- retention: While the subscription is active. No retention clock published | source: [1]
- egress: Console-mediated only. There is no HTTP API, so there is no egress path at all | metered: no | source: [2]
- identity: email | detail: a PSN account and a paid subscription
- interface: unknown
- limits:
  - per-object-cap: 1,000 PS4 save files [2]
  - write-gated (binding): uploads happen from the console UI and need a PSN-authenticated console [2]
- binding note: 200 GB on a paid subscription, but the gate that matters is that the only client is a console: there is no path to read the bytes from a server.
- tooling: none documented. PS4 save decryption is a separate jailbreak scene and not a storage API
- composes with: Not chainable. Even filled to 200 GB the bytes are opaque save blobs retrievable only by a PS5 or PS4, so there is no read path to build on
- reliability: The read path is console-only, which is the upload-open and read-gated failure in its purest form: a write quota with no programmatic read is not storage
- notes: PlayStation Plus cloud save storage provides 100 GB for PlayStation 5 and 100 GB for PlayStation 4, totalling 200 GB across both consoles. Access is confined strictly to console software without web or programmatic API support.
- extras:
  - access_mode: registration-gated
  - api: none, console only
  - quota_split: 100 GB PS5 plus 100 GB PS4
  - aliases: PlayStation Plus cloud storage (Sony)
  - cross_topic_record: storage/playstation-plus-cloud-storage
  - cross_topic_note: the storage topic carries the same provider from the game-save angle
- evidence:
  - [2] 2026-10-21: every step is console UI, 'Settings > Saved Data and Game/App Settings > Upload to Cloud Storage'
  - [1] 2026-10-21: '100 GB of online storage ... The number of PS4 saved data files you can store is limited to 1000'
  - [3] 2026-10-21: the 10 GB to 100 GB expansion
  - [2] 2026-11-03: 100 GB for PS5 saves, 100 GB for PS4 saves and 1000 PS4 save files, unchanged | capture: sha256:3fb6da72a3d334680ee4c9fe43929c80d254ed718b62fe735c203258f39b756e | quote: You can save up to 100 GB of PS5 saved data and 100 GB of PS4 saved data. The number of PS4 saved data files you can store is limited to 1000.
  - [2] 2026-11-03: cloud storage needs a PlayStation Plus membership | capture: sha256:3fb6da72a3d334680ee4c9fe43929c80d254ed718b62fe735c203258f39b756e | quote: Become a PlayStation Plus member to use cloud storage.
  - [1] 2026-11-03: 100 GB cloud storage is in the Essential, Extra and Premium plans | capture: sha256:c5dfcb4a339011dbc092b6930d425ab1a18a0e10aefd6d433f2b2a49c7809b46 | quote: | 100GB Cloud Storage | x | x | x |
- sources:
  - [1] https://www.playstation.com/en-us/support/subscriptions/playstation-plus-support/
  - [2] https://www.playstation.com/en-us/support/subscriptions/ps5-ps-plus-cloud-storage/
  - [3] https://blog.playstation.com/2019/01/30/playstation-plus-cloud-storage-expanding-to-100gb-free-games-for-february

## playstation app captures library

- `storage/playstation-app-captures-library` | fails-quota | evidence documented | binding retention-clamped | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:22:32.526Z (live) | stale on 2026-12-05
- url https://www.playstation.com/en-us/support/games/ps5-game-captures-ps-app/
- free tier: Captures are stored for 14 days on the vendor's cloud servers and are available in the PlayStation App; no PlayStation Plus subscription is needed | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: Gameplay videos under 3 minutes long that are non-4K; no byte cap stated on the page | source: [1] | note: not applicable
- retention: 14 days after the capture is created on the PS5 console | days: 14 | source: [1]
- egress: not recorded | metered: no
- identity: email | detail: a PS5 console linked to the PlayStation App is required for upload
- interface: unknown
- limits:
  - retention-clamped (binding): 14 days after creation on the PS5 console [1]
- binding note: captures expire after 14 days and only PS5 gameplay captures are accepted
- interface detail: not documented
- tooling: unverified: whether a developer API exists; the documented path is the PlayStation App on iOS and Android with a linked PS5 console
- composes with: not recorded
- reliability: Captures are available in the PlayStation App for 14 days after they are created on the PS5 console; only gameplay clips under 3 minutes (non-4K) and screenshots are uploaded
- notes: the same as reliability
- evidence note: documented: the page read on 2026-11-03 is https://www.playstation.com/en-us/support/games/ps5-game-captures-ps-app/, which states that once auto-upload is enabled captures are available in PlayStation App for 14 days after they are created on the PS5 console, that captures are stored for 14 days on cloud servers so as to be available via the app, that only gameplay videos under 3 minutes long that are non-4K and screenshots are uploaded (video clips in a higher resolution than 1920x1080 are not uploaded), that the PS5 console must be linked to PlayStation App, and that no PlayStation Plus subscription is needed. The 14-day retention and the clip limits that decide the verdict rest on that vendor page; the identity kind email is not stated on it.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: PS5 auto-upload goes to a private per-account library in the PS App with no public URL, no documented quota, no documented retention, and no API at all. Web-only, login-walled, unverified…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: PS5 auto-upload goes to a private per-account library in the PS App with no public URL, no documented quota, no documented retention, and no API at all. Web-only, login-walled, unverified…
  - [1] 2026-11-03: captures are kept 14 days and no PlayStation Plus subscription is needed | capture: sha256:dc546460ad3c0ca2ab7344010427010674bc847ffde988aaf5095bfd895d5fb4 | quote: No. Your captures are stored for 14 days on SIE's cloud servers in order to make them available to you via PlayStation App.
  - [1] 2026-11-03: retention is 14 days from creation | capture: sha256:dc546460ad3c0ca2ab7344010427010674bc847ffde988aaf5095bfd895d5fb4 | quote: Your captures of games will then be available in PlayStation App for 14 days after they are created on your PS5 console.
  - [1] 2026-11-03: clips over 3 minutes or in 4K are not uploaded | capture: sha256:dc546460ad3c0ca2ab7344010427010674bc847ffde988aaf5095bfd895d5fb4 | quote: Gameplay videos under 3 minutes long that are non-4K.
  - [1] 2026-11-03: uploaded clips are bounded by duration and resolution | capture: sha256:dc546460ad3c0ca2ab7344010427010674bc847ffde988aaf5095bfd895d5fb4 | quote: Gameplay videos under 3 minutes long that are non-4K.
  - [1] 2026-11-03: auto-upload requires a console linked to the app | capture: sha256:dc546460ad3c0ca2ab7344010427010674bc847ffde988aaf5095bfd895d5fb4 | quote: Your PS5 console needs to be linked to PlayStation App.
  - [1] 2026-11-03: the documented path goes through the PlayStation App | capture: sha256:dc546460ad3c0ca2ab7344010427010674bc847ffde988aaf5095bfd895d5fb4 | quote: Your PS5 console needs to be linked to PlayStation App.
  - [1] 2026-11-04: retention is 14 days from creation on the console | capture: sha256:dc546460ad3c0ca2ab7344010427010674bc847ffde988aaf5095bfd895d5fb4 | quote: Your captures of games will then be available in PlayStation App for 14 days after they are created on your PS5 console.
- sources:
  - [1] https://www.playstation.com/en-us/support/games/ps5-game-captures-ps-app/
