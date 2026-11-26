# Thunderstore

> thunderstore.io | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/thunderstore/ | JSON https://fshy.ajam.dev/api/v1/entity/thunderstore.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Thunderstore

- `storage/thunderstore` | qualifies-with-caveat | evidence reported | binding none | category registry
- identity a placeholder: card and phone unknown | verified 2026-11-25T19:55:24.770Z (live) | stale on 2026-12-10
- url https://thunderstore.io
- free tier: Maximum package size limit of 10 GB, a soft-limit that can be increased if needed. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: Maximum package size limit of 10 GB, a soft-limit that can be increased if needed. | source: [1] | note: 10 GB package size limit; a soft-limit that can be increased if needed.
- retention: Deprecated mods can still be found on the website and mod manager by checking a box in the search options. | source: [1] | note: Deprecated mods can still be found on the website and mod manager by checking a box in the search options.
- egress: Free and CDN-fronted: download URLs 302 to ccdn.thunderstore.io with `Cache-Control: max-age=2678400`, `Server: cloudflare`, no auth. | metered: no
- identity: email
- interface: rest, rclone, cli
- limits note: 10 GB package size soft limit that can be increased if needed.
- interface detail: rest
- tooling: Package upload via multipart POST to /api/experimental/submission/upload/ (thunderstore-cli, tcli); metadata read via /api/experimental/package/. No rclone backend, CLI wrapper exists: github.com/thunderstore-io/thunderstore-cli.
- composes with: Unlimited packages x 5 GB each. Team is the ownership unit, one user can create many teams; nothing in the source caps packages per team. 20 packages = 100 GB, 200 = 1 TB, all on a free account.
- reliability: Packages surviving as 'mods' for a real game community; orphaned/garbage packages are routinely delisted, which deletes files.
- notes: 10 GB package size limit, a soft-limit that can be increased if needed.
- evidence:
  - [1] 2026-10-21: 'Currently there's a maximum package size limit of 5 242 880 000 bytes (or roughly 5 GB), but this is a soft-limit and can be increased if needed'
  - [2] 2026-10-21: REPOSITORY_MAX_PACKAGE_SIZE_MB=(int, 500), REPOSITORY_MAX_PACKAGE_TOTAL_SIZE_GB=(int, 1000)
  - [3] 2026-10-21: MAX_PACKAGE_SIZE / MAX_TOTAL_SIZE enforcement
  - [4] 2026-10-21: upload form states '10GB max'
  - withheld 2026-10-21: probe: GET thunderstore.io/package/download/BepInEx/BepInExPack/5.4.2305/ -> 302 to ccdn.thunderstore.io/...zip
  - withheld 2026-10-21: probe: GET ccdn.thunderstore.io/...zip Range 0-10 -> 206, Content-Range bytes 0-10/669238, Cache-Control max-age=2678400
  - [1] 2026-11-19: the package-creation wiki now states a 10 GB soft package-size limit | capture: sha256:64f35b0d8a2537bcdd5a589f160b8e15a1e5e7a1f514ad157b156dc2387b9cf3 | quote: Currently there's a maximum package size limit of 10 GB, but this is a soft-limit and can be increased if needed.
  - [1] 2026-11-19: the package-creation wiki now states a 10 GB soft package-size limit, replacing the earlier 5 GB figure | capture: sha256:64f35b0d8a2537bcdd5a589f160b8e15a1e5e7a1f514ad157b156dc2387b9cf3 | quote: Currently there's a maximum package size limit of 10 GB, but this is a soft-limit and can be increased if needed.
  - [1] 2026-11-25: the package size limit is 10 GB and is a soft limit | capture: sha256:3f4c2f00a706311307b348362418d55d5d0df027fbc321c51ee67b309a580a13 | quote: Currently there's a maximum package size limit of 10 GB, but this is a soft-limit and can be increased if needed.
  - [5] 2026-11-25: deprecation keeps packages findable through a search option | capture: sha256:93b0703be7fad64d0fdfc2f510872b621141c315ca3d9995c687fa041bca8a62 | quote: Deprecated mods can still be found on the website and mod manager by checking a box in the search options.
- sources:
  - [1] https://wiki.thunderstore.io/mods/creating-a-package
  - [2] https://raw.githubusercontent.com/thunderstore-io/Thunderstore/master/django/thunderstore/core/settings.py
  - [3] https://raw.githubusercontent.com/thunderstore-io/Thunderstore/master/django/thunderstore/repository/package_upload.py
  - [4] https://thunderstore.dev/package/create/
  - [5] https://wiki.thunderstore.io/moderation/removing-a-package.md
