# Steam

> steamgames.com | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/steamgames/ | JSON https://fshy.ajam.dev/api/v1/entity/steamgames.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Steam Cloud (developer-set per-app quota)

- `storage/steam-cloud` | qualifies-with-caveat | evidence documented | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:32.477Z (live) | stale on 2026-12-11
- url https://partner.steamgames.com/doc/features/cloud
- free tier: To set up Steam Cloud you must set the `Byte quota per user` and `Number of files allowed per user` options on the [Steam Cloud Settings](https://partner.steamgames.com/apps/cloud/) page in the Steamworks App Admin panel. | unit: objects | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: 100MB maximum size for a call to ISteamRemoteStorage::FileWrite or ISteamRemoteStorage::FileWriteStreamWriteChunk | bytes: 100000000 | source: [1] | note: not stated
- retention: Per-object-cap: 100 MB per FileWrite call (256 MB 'may result in a non-optimal storage endpoint'); per-object-cap: ~10,000 files per cloud save; the game must be launchable/owned for the user, and impersonating it blocks normal play during sync. Retention: indefinite. No expiry documented, but a developer can change quota or delist and the data can be evicted. | source: [1] | note: not stated
- egress: Unmetered and anonymous on the download path via the Steam client / Steamworks SDK. No published per-GB charge. | metered: no
- identity: email
- interface: rest
- limits:
  - per-object-cap (binding): 100MB maximum size for a call to ISteamRemoteStorage::FileWrite or ISteamRemoteStorage::FileWriteStreamWriteChunk [1]
- limits note: Per-object-cap: 100 MB per FileWrite call (256 MB 'may result in a non-optimal storage endpoint'); per-object-cap: ~10,000 files per cloud save; the game must be launchable/owned for the user, and impersonating it blocks normal play during sync. Retention: indefinite. No expiry documented, but a developer can change quota or delist and the data can be evicted.
- interface detail: rest
- tooling: Steamworks SDK `ISteamRemoteStorage` (FileWrite, FileWriteStreamWriteChunk, FileReadAsync). Working wrapper exists: github.com/Fldicoahkiin/SteamCloudFileManager. 237 stars, Rust, Windows/macOS/Linux, '支持任意文件的上传、下载与删除' (arbitrary file upload/download/delete against any owned game's cloud). Design writeup: krutonium.ca/posts/using-steam-as-cloud-storage/.
- composes with: One Steam account x every owned Cloud-enabled game with a large quota. At 93 GB/game, 12 games = ~1.1 TB; 100 games = ~9 TB. Multiply again by accounts. The lever is picking titles whose developers set 93 GB, not buying storage.
- reliability: Entirely undocumented by Valve; a developer lowering their quota can strand data, and files are re-downloaded into the local save folder on game launch. No public bans recorded.
- notes: Quota is set by each game's developer as 'Byte quota per user' and 'Number of files allowed per user', 'enforced on each Cloud-enabled game, on a per-user-per-game basis'. No Valve-imposed total. Community-observed ceilings: 93 GB per game, ~10,000 files. Defaults are frequently tiny (a few MB to 1 GB).
- evidence note: the Steamworks Steam Cloud page states the per-user byte quota and file-count options set in the App Admin panel
- evidence:
  - [1] 2026-10-21: 'you must set the Byte quota per user and Number of files allowed per user options ... This quota is enforced on each Cloud-enabled game, on a per-user-per-game basis'; file-size table '100MB Maximum size for a call to ISteamRemoteStorage::FileWrite'
  - [2] 2026-10-21: (published 2026-05-09) — '93GB Cloud Save Storage per Game, Maximum'; '100MB per File is an Ideal Limit, but above 250MB the back end for the API will start to hate you'; 'Possible Limit of 10,000 Files per Cloud Save'
  - [3] 2026-10-21: probe: GET (POST, no key) -> 200, returns file_size 4997533 for item 450814997 — Steam's public storage APIs answer anonymously
  - [4] 2026-10-21: (Sep 2025) — 'poly bridge 3 has 93GB available', user reports 23GB used in Factorio
  - [1] 2026-11-09: the Steamworks page states that the developer sets a per-user byte quota and a per-user file-count allowance | capture: sha256:f13b0e9e5cd9acacba3cdd0ae19f8c84f7510fd3b158c35a324c43a5fc55b22b | quote: To set up Steam Cloud you must set the `Byte quota per user` and `Number of files allowed per user` options on the [Steam Cloud Settings](https://partner.steamgames.com/apps/cloud/) page in the Steamworks App Admin panel.
  - [1] 2026-11-09: the page limits one FileWrite or FileWriteStreamWriteChunk call to 100MB | capture: sha256:f13b0e9e5cd9acacba3cdd0ae19f8c84f7510fd3b158c35a324c43a5fc55b22b | quote: | 100MB | Maximum size for a call to ISteamRemoteStorage::FileWrite or ISteamRemoteStorage::FileWriteStreamWriteChunk |
- sources:
  - [1] https://partner.steamgames.com/doc/features/cloud
  - [2] https://krutonium.ca/posts/using-steam-as-cloud-storage/
  - [3] https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/
  - [4] https://forums.factorio.com/viewtopic.php?t=130969

## Steam Workshop (per-app item storage)

- `storage/steam-workshop` | qualifies-with-caveat | evidence reported | binding write-gated | category media
- identity a placeholder: card and phone unknown | verified 2026-11-10T00:50:32.477Z (live) | stale on 2026-11-25
- url https://partner.steamgames.com/doc/features/workshop
- disagrees on identity_kind: `storage/steam-workshop` says anonymous, `storage/steam-workshop-2` says email
- disagrees on verdict: `storage/steam-workshop` says qualifies-with-caveat, `storage/steam-workshop-2` says fails-quota
- free tier: Arma 3 Workshop now support items of unlimited size. | unit: unlimited | metered on: unstated | read on: 2026-11-09 | source: [1]
- per-object cap: The maximum size varies depending on what the developers set it as. | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free and CDN-served by Valve's content network. Same infrastructure as game downloads, genuinely unmetered. | metered: no
- identity: anonymous
- interface: rest
- limits:
  - write-gated (binding): review images go through a separate Steam Cloud quota [1]
- limits note: Requires ownership of the game and a Steam client to upload. There is no headless upload path, which is the practical blocker. Per-item caps range from 20 MB to unlimited depending on app; preview images go through a separate Steam Cloud quota.
- interface detail: rest
- tooling: `ISteamUGC` (CreateItem + SetItemContent + SubmitItemUpdate) via the Steamworks SDK, so uploads need a Steam client with the game installed. Downloads are scriptable anonymously: `steamcmd +login anonymous +workshop_download_item <appid> <publishedfileid>`. Third-party downloaders (polocaz/ws-downloader, workshopfetch.com) exist for the read path.
- composes with: One Steam account x every Workshop-enabled game it owns x unlimited items per game. This is the multiplier: 'unlimited items per published file ID' inside an app whose developer set no cap.
- reliability: Very durable. Workshop items have survived a decade, links do not expire, and downloads are anonymous. Enforcement risk is real but technical: items can be delisted by the app's developer.
- notes: Per-item size is set by the game developer, not by Valve, and some games are explicitly unlimited. Arma 3: 'Arma 3 Workshop now support items of unlimited size.' Others are tiny: House Flipper raised its cap from 12 MB to 20 MB in a patch. So the quota is per-app, and the number of published items per account is not documented as capped.
- evidence note: the Arma 3 workshop page states that Workshop items may be of unlimited size
- evidence:
  - [1] 2026-10-21: 'What is the maximum size of a mod? Arma 3 Workshop now support items of unlimited size.'
  - [2] 2026-10-21: 'Increased the maximum Steam Workshop item size limit from 12 MB to 20 MB. Increased the default Workshop item size from 10 MB to 12 MB.'
  - [3] 2026-10-21: 'The maximum size varies depending on what the developers set it as.'
  - [4] 2026-10-21: 'Steam Workshop is a system of back-end storage and front-end web pages that make it easy to store, organize, sort, rate, and download content'
  - [1] 2026-11-09: the Arma 3 workshop page states that Workshop items may be of unlimited size | capture: sha256:8e8bf0b1f1496d4fc0e083aca7087dd85d5d4be1fe949086034d5cc390bd1c3c | quote: Arma 3 Workshop now support items of unlimited size.
  - [3] 2026-11-09: a Steam community answer states that the maximum item size is set by each game's developer | capture: sha256:646bcf275017d83f285e42a7e46913dd0d1df62b7ac99fdd07e5a4e2393c1af9 | quote: The maximum size varies depending on what the developers set it as.
- sources:
  - [1] https://arma3.com/workshop101
  - [2] https://steamcommunity.com/app/3710840/announcements/
  - [3] https://steamcommunity.com/discussions/forum/1/1744480966997034452/
  - [4] https://partner.steamgames.com/doc/features/workshop

## steam workshop

- `storage/steam-workshop-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:27.947Z (live) | stale on 2026-12-04
- url https://partner.steamgames.com/steamdirect
- disagrees on identity_kind: `storage/steam-workshop` says anonymous, `storage/steam-workshop-2` says email
- disagrees on verdict: `storage/steam-workshop` says qualifies-with-caveat, `storage/steam-workshop-2` says fails-quota
- free tier: none reachable: Hard ceiling far below the unit size, plus a paid gate: uploads need a Steamworks partner app ($100 Steam Direct fee per product) and the ISteamUGC API is a C++ SDK, not HTTP. Pract | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Hard ceiling far below the unit size, plus a paid gate: uploads need a Steamworks partner app ($100 Steam Direct fee per product) and the ISteamUGC API is a C++ SDK, not HTTP. Pract
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Hard ceiling far below the unit size, plus a paid gate: uploads need a Steamworks partner app ($100 Steam Direct fee per product) and the ISteamUGC API is a C++ SDK, not HTTP. Pract
  - [2] 2026-10-21: cited as the basis of the rejection: Hard ceiling far below the unit size, plus a paid gate: uploads need a Steamworks partner app ($100 Steam Direct fee per product) and the ISteamUGC API is a C++ SDK, not HTTP. Pract
  - [3] 2026-10-21: cited as the basis of the rejection: Hard ceiling far below the unit size, plus a paid gate: uploads need a Steamworks partner app ($100 Steam Direct fee per product) and the ISteamUGC API is a C++ SDK, not HTTP. Pract
  - [1] 2026-11-19: Steam Direct charges a non-refundable USD 100 fee per product, a paid gate to publishing an app | capture: sha256:29614f8c847e1ffd7254d0cc985f783114dc3011c2ca62914794d22f74a64930 | quote: In order to get fully set up, you will need to pay a $100.00 USD fee for each product you wish to distribute on Steam (the "Steam Direct Fee").
- sources:
  - [1] https://partner.steamgames.com/steamdirect
  - [2] https://steamcommunity.com/discussions/forum/10/4202490864588145731/
  - [3] https://steamcommunity.com/app/4000/discussions/5/1734343065615467703/
