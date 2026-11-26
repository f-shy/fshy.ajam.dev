# Panoramax

> openstreetmap.fr | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openstreetmap/ | JSON https://fshy.ajam.dev/api/v1/entity/openstreetmap.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Panoramax — OSM-FR instance (panoramax.openstreetmap.fr) ⭐

- `storage/panoramax-osm-fr-instance` | qualifies | evidence reported | binding none | category federated crowdsourced street-level imagery (open-source, self-hostable)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T21:21:16.852Z (live) | stale on 2026-12-10
- url https://panoramax.openstreetmap.fr
- free tier: NO QUOTA ANYWHERE IN THE SERVER. There is no quota code, no quota column in the DB migrations, and no quota endpoint. Because the feature does not exist. A contributor filed Feature Request #334 '(Feature Request) Disable uploads when less than X GB of storage is available', still Open 5 months later, precisely because an admin cannot cap anything. Storage is whatever the instance's disks hold: OSM-FR alone reports 22.7M pictures = 48.5 TB of originals + 22.5 TB of derivates. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: No per-object cap stated in the cited Panoramax server issue or API/CLI docs.
- retention: source: [1] | note: No retention period stated; the API docs state useless pictures may be detected and deleted during processing.
- egress: Unmetered and CDN-friendly: no auth on any GET, plain nginx serving, Accept-Ranges honored. Verified 206 Partial Content with Content-Range: bytes 0-1023/3336348 on a live HD original. | metered: no
- identity: email | detail: Email. But indirectly. `/api/configuration` on OSM-FR literally returns `"registration_is_open": true` and `/api/auth/login` 302s to openstreetmap.org/oauth2/authorize; the OSM signup form (/user/new) accepts `user[email]` + `user[display_name]` + password, no affiliation, no .edu, no review, email-confirm only. IGN instance uses its own Keycloak (`panoramax.ign.fr/oauth/realms/geovisio`). Eithe….
- interface: rest, cli
- limits note: Two-object model, must be JP(E)G (HEIC unsupported. Issue #186), EXIF GPS + timestamp mandatory, images deduplicated by distance/rotation within an upload set. Approx 18 MB per 96 MP photo. Nothing enforces a byte ceiling.
- interface detail: REST + OGC API Features + STAC 1.0 + STAC item-search. POST /api/upload_sets → POST /api/upload_sets/{id}/files → POST /api/upload_sets/{id}/complete. Bearer token from POST /api/auth/tokens/generate.
- tooling: panoramax_cli (v1.4.1, Windows/Linux binaries + Python lib) with `upload`, `download`, `transfer`, `migration` subcommands; Docker `panoramax/api`; JOSM/iD plugins; the CLI can also transfer sequences between instances, so one file can be replicated across the whole federation.
- composes with: Upload once → replicate to N instances with `panoramax_cli transfer` → each instance serves its own /images/<2/2/2/2>/<uuid>.jpg path → front the whole federation with Cloudflare. Since every picture is addressed by a stable UUID and every asset URL is in the STAC item's `assets.hd.href`, a proxy can rewrite to whichever instance is alive.
- reliability: Volunteer hardware with ZFS RAIDZ2 + daily remote snapshots; no SLA and no capacity guard, so an instance can silently fill and start 500ing on upload. That is the whole reason #334 exists.
- notes: Feature request '(Feature Request) Disable uploads when less than X GB of storage is available': permit the server admin to set an amount of storage that must remain free.
- self hosted: no
- evidence:
  - [2] 2026-10-21: literal: {"auth":{"enabled":true,"registration_is_open":true,...},"geovisio_version":"2.15.1-22-gf754cc9"}
  - [3] 2026-10-21: live STAC catalog, 2.15.1, links to /api/upload_sets, /api/users/
  - [4] 2026-10-21: 200, Content-Length: 3336348, image/jpeg, no auth
  - withheld 2026-10-21: same URL with Range: bytes=0-1023 — HTTP/1.1 206 Partial Content, Content-Range: bytes 0-1023/3336348
  - [1] 2026-10-21: open feature request to add a storage floor; proves no quota mechanism exists
  - [5] 2026-10-21: 100M pictures across 10 instances, 1M 72MP pictures ≈ 9 TB originals, 360° tiling doubles it
  - [6] 2026-10-21: FS_PERMANENT_URL = 'definitive storage of original, high-definition ... pictures'; derivates are only thumb/sd/tiles, i.e. the hd asset IS the original
  - [7] 2026-10-21: `upload`, `download`, `transfer`, `migration` subcommands
  - [1] 2026-11-11: the open work item asks for an admin-set storage floor, so the server has no such cap | capture: sha256:4d3e63bfea1a2fd38b7627f1343e5a4d37203426a7c3b2e7dc8f8a4316493307 | quote: (Feature Request) Disable uploads when less than X GB of storage is available ... permit the server admin to set an amount of storage that must remain free
  - [1] 2026-11-19: the open feature request asks to add an admin-set storage floor, so the server has no quota cap today | capture: sha256:43f4eb56916543fc91500efcc5da7223d3478a7de49a921da4a4a762b92e552f | quote: permit the server admin to set an amount of storage that must remain free
  - [1] 2026-11-25: the open feature request discusses a missing storage floor, not a per-object cap; no per-object cap is stated | capture: sha256:43f4eb56916543fc91500efcc5da7223d3478a7de49a921da4a4a762b92e552f | quote: As new, small instances are created, I think a valuable feature for administrators would be to permit the server admin to set an amount of storage that must remain free.
  - [8] 2026-11-25: the API docs state useless pictures may be deleted during processing; no retention period is stated | capture: sha256:53b563a5bb7f421c073b21c24af8a45bcccaa9a8020ffd46cb33f3cfce39aa03 | quote: useless pictures like when stopped at a traffic light are detected and deleted.
  - [1] 2026-11-25: the cited issue discusses storage-floor controls and states no per-object cap | capture: sha256:43f4eb56916543fc91500efcc5da7223d3478a7de49a921da4a4a762b92e552f | quote: As new, small instances are created, I think a valuable feature for administrators would be to permit the server admin to set an amount of storage that must remain free.
  - [8] 2026-11-25: the API docs describe deletion of useless pictures during processing and state no retention period | capture: sha256:53b563a5bb7f421c073b21c24af8a45bcccaa9a8020ffd46cb33f3cfce39aa03 | quote: useless pictures like when stopped at a traffic light are detected and deleted.
- sources:
  - [1] https://gitlab.com/panoramax/server/api/-/work_items/334
  - [2] https://panoramax.openstreetmap.fr/api/configuration
  - [3] https://panoramax.openstreetmap.fr/api
  - [4] https://panoramax.openstreetmap.fr/images/20/1f/c2/ac/ddad-4381-b3eb-111519d2c7bb.jpg
  - [5] https://forum.geocommuns.fr/t/storage-needs-for-a-panoramax-instance/3205
  - [6] https://docs.panoramax.fr/backend/install/settings/
  - [7] https://docs.panoramax.fr/cli/COMMANDS/
  - [8] https://docs.panoramax.fr/backend/api/api/
