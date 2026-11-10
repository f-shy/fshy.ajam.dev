# ModDB

> moddb.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/moddb/ | JSON https://fshy.ajam.dev/api/v1/entity/moddb.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ModDB (free member file hosting)

- `storage/moddb` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.moddb.com/features/overview-about-using-moddb
- disagrees on identity_kind: `storage/moddb` says anonymous, `storage/moddb-indiedb-file-downloads` says country-phone
- free tier: 4 GB per file via URL upload, ~2,800 MB via browser upload. No documented total storage cap per account; Files / Addons / Mods tabs are all upload surfaces on a free account. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB per file | bytes: 4000000000 | source: [1] | note: not stated
- retention: per-object-cap: 4,000 MB per file (URL upload) / ~2,800 MB (browser upload); uploads cannot be resumed and time out after 12 hours; no total-account cap documented. Retention: indefinite while the page exists; a page can be deleted by staff. | days: 0 | source: [1] | note: not stated
- egress: Free public downloads from media.moddb.com; no metered egress documented and no speed cap published. | metered: no
- identity: anonymous
- interface: unknown
- limits:
  - per-object-cap (binding): 4 GB per file [1]
  - per-object-cap (binding): 4,000 MB per file [1]
- limits note: per-object-cap: 4,000 MB per file (URL upload) / ~2,800 MB (browser upload); uploads cannot be resumed and time out after 12 hours; no total-account cap documented. Retention: indefinite while the page exists; a page can be deleted by staff.
- interface detail: wrapper-only
- tooling: Web upload form (requires member login); no public write API. Read path is plain HTTP GET on media.moddb.com. 'Click to connect via Steam' means account creation chains off an existing Steam identity.
- composes with: 4 GB per file x unlimited files x unlimited addon pages x free accounts. Also: URL-upload means the source file can live on another free host, so ModDB acts as a free second copy / re-distribution mirror rather than primary storage.
- reliability: Browser-upload path is fragile above ~2.8 GB and there is no resume, so a failed 12-hour upload wastes the slot. media.moddb.com answered 200 with real bytes (238,600) on probe, but the site root returns 503 to datacenter egress. Expect intermittent blocking.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: staff (TKAzA): 'we support files up to 4GB'; founder (INtense!): 'uploading a file from your computer currently supports only 2800mb, if you upload from a url you can do 4000mb+'
  - [2] 2026-10-21: 'Files' tab for tools, 'Addons' for mods, 'Mods' for total conversions
  - [3] 2026-10-21: probe: GET -> 200, 238600 bytes — CDN serves originals anonymously
  - [4] 2026-10-21: probe: GET -> 503 (this egress); GET /addons/add -> 200 with 'Members only' gate — upload requires a logged-in member account
- sources:
  - [1] https://www.moddb.com/forum/thread/how-to-upload-a-bigger-file-to-moddbcom
  - [2] https://www.moddb.com/features/overview-about-using-moddb
  - [3] https://media.moddb.com/images/members/5/4690/4689942/profile/cover.png
  - [4] https://www.moddb.com/

## ModDB / IndieDB (dbolical) file downloads

- `storage/moddb-indiedb-file-downloads` | qualifies-with-caveat | evidence reported | binding per-object-cap | category media
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.moddb.com
- disagrees on identity_kind: `storage/moddb` says anonymous, `storage/moddb-indiedb-file-downloads` says country-phone
- free tier: No published total quota, but a large installed base with published aggregate stats: the downloads index reports 149,920 files totalling 43,307.57 GB and 387,395,913 downloads. Mean file size is therefore ~296 MB, and the tail is much larger - a live listing for `objects3` shows '7.86gb (8,442,728,905 bytes)' on a single file. So 8 GB-class single objects are published and served today. | unit: objects | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: file size is therefore ~296 MB | bytes: 296000000 | source: [1] | note: not stated
- retention: per-object-cap: verified at least 8,442,728,905 bytes on a live file listing; the widely-cited 8192 MB figure is third-party (TWC wiki, marked TBC by its own author) and is contradicted by the 7.86 GB file, so treat ~8 GB as observed-not-documented. retention: indefinite; files stay downloadable for years | source: [1] | note: not stated
- egress: Free, no billing, and the site is Cloudflare-fronted (Server: cloudflare on the live origin). Files are served from the site itself rather than a separate CDN hostname; the mirror endpoint (/downloads/mirror/<id>/<n>/<hash>) is the byte path and is behind the same edge. | metered: no
- identity: country-phone
- interface: rest, sftp
- limits:
  - per-object-cap (binding): file size is therefore ~296 MB [1]
- limits note: Per-object cap is verified at 8,442,728,905 bytes on published files, with approximately 8 GB observed in practice. Retention is indefinite for hosted files. Uploads require web forms and endpoints enforce browser verification headers.
- interface detail: rest
- tooling: No upload API and no SFTP: the write path is the web 'Add File' form at /downloads/add, gated to logged-in members. There is a 'URL upload' field (fetch-from-URL) which is the closest thing to automation. Read side is plain anonymous HTTP GET from /downloads/mirror/..., plus an MD5 hash published on each file page.
- composes with: One account x unlimited game/mod profiles x unlimited files per profile. Because the unit is a mod page, not a repo, cardinality is bounded only by how many plausible mod entries you create. 8.44 GB verified per file x N files.
- reliability: Also note the add-file page itself says 'Members only / You do not have permission to add the requested downloads content' when unauthenticated.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: (archived capture 20261006020841) - aggregate '149,920 Files / 43307.57gb Size / 387,395,913 Downloads'
  - [2] 2026-10-21: (search index excerpt) - 'Size 7.86gb (8,442,728,905 bytes)', uploaded Aug 22 2025, MD5 published
  - withheld 2026-10-21: 'Members only. You do not have permission to add the requested downloads content.'
  - [1] 2026-10-21: probe: GET -> HTTP 503 (origin refuses proxy); direct GET /downloads/start/222436 -> 403 behind cloudflare
  - [3] 2026-10-21: third-party 'Moddb File Size Limit: 8192MB (TBC)' - flagged TBC by its own author and contradicted by the 7.86 GB file above
- sources:
  - [1] https://www.moddb.com/downloads
  - [2] https://www.moddb.com/downloads/objects3
  - [3] https://wiki.twcenter.net/index.php?title=Upload_Sites
