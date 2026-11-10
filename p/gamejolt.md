# Game Jolt game builds

> gamejolt.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gamejolt/ | JSON https://fshy.ajam.dev/api/v1/entity/gamejolt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Game Jolt game builds

- `storage/game-jolt-game-builds` | fails-quota | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://gamejolt.com
- free tier: 3 GB TOTAL PER GAME, not per file. The 3 GB number is corroborated by an official changelog post ('Max filesize for builds has now been bumped to 3GB instead of 2GB. Go upload big things!') and developer posts ('the upload limit for total game size on GameJolt has been extended to 3GB'). Earlier limits were 1 GB then 2 GB per build. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Max filesize for builds has now been bumped to 3GB | bytes: 3000000000 | source: [1] | note: not stated
- retention: per-object-cap: 3 GB total per game (all builds counted together, per the developer posts). retention: indefinite for published games | source: [1] | note: not stated
- egress: Free, Cloudflare-fronted (Server: cloudflare, cf-cache-status: HIT on the storefront). No billing. No separate CDN hostname was resolvable from here (mproxy./build./games.gamejolt.net all NXDOMAIN), so downloads are served through the main site edge. | metered: no
- identity: email
- interface: rest, sftp, cli
- limits:
  - per-object-cap (binding): Max filesize for builds has now been bumped to 3GB [1]
- limits note: per-object-cap: 3 GB total per game (all builds counted together, per the developer posts). retention: indefinite for published games. request-rate: not published. Upload is browser-based; several developers report having to leave the platform at exactly this cap.
- interface detail: rest
- tooling: Web dashboard only ('Add Your Game' at /dashboard/games/add) - no upload API, no SFTP, no CLI. Read side is ordinary HTTPS GET from game pages. The public Game Jolt API v1_2 is for auth/scores/trophies/data-store, not file transfer.
- composes with: Allows multiple game listings per account with 3 GB total storage per game. Scaling requires registering multiple distinct game entries.
- reliability: The cap is the finding and it is enforced at the game level, so splitting into multiple builds or platforms does not raise it. Multiple independent developers left Game Jolt for itch.io citing this limit, which is corroborating evidence that it is enforced rather than advisory. Some gamejolt.com pages return 403/422 to non-browser readers, so automated reads are partly blocked.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 3 GB TOTAL PER GAME, not per file. Earlier it was 1 GB, then 2 GB per build ('that's per build, meaning that if you have multiple builds for different platforms, each one is allowed to be up to 2GB').
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Max filesize for builds has now been bumped to 3GB instead of 2GB. Go upload big things!'
  - [2] 2026-10-21: 4 months ago: 'the upload limit for total game size on GameJolt has been extended to 3GB'
  - [3] 2026-10-21: 11 years ago: 1 GB -> 2 GB, 'per build ... if you have multiple builds for different platforms, each one is allowed to be up to 2GB'
  - [4] 2026-10-21: 11 months ago: developer leaves for itch.io citing the 3 GB cap
  - [5] 2026-10-21: probe: GET -> 200, Server: cloudflare, cf-cache-status: HIT; DNS for mproxy/build/games.gamejolt.net -> NXDOMAIN
- sources:
  - [1] https://gamejolt.com/p/max-filesize-for-builds-has-now-been-bumped-to-3gb-instead-of-2gb-yevwgtyp
  - [2] https://ssr.gamejolt.net/p/attention-fellow-devs-this-is-more-aimed-toward-the-ones-that-are-jsdnctmg
  - [3] https://gamejolt.com/p/now-supporting-larger-file-uploads-we-ve-bumped-the-maximum-file-f9tedkfu
  - [4] https://gamejolt.com/p/attention-due-to-gamejolt-s-limitation-on-the-game-file-size-of-max-sz6qxugj
  - [5] https://gamejolt.com/
