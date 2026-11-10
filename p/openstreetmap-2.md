# OpenStreetMap GPS traces

> openstreetmap.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/openstreetmap-2/ | JSON https://fshy.ajam.dev/api/v1/entity/openstreetmap-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OpenStreetMap GPS traces (openstreetmap.org/traces)

- `storage/openstreetmap-gps-traces` | fails-quota | evidence reported | binding none | category crowdsourced geodata
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:22:32.522Z (live) | stale on 2026-11-19
- url https://www.openstreetmap.org/trace/create
- free tier: No published per-user quota and no quota endpoint; storage is GPX-only and appended to the OSM rails DB + a trace store. Effectively unlimited in count, tiny per unit. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: free, no auth for public traces; individual points also exposed via the API 0.6 trace endpoints | metered: no
- identity: email | detail: Email. Verified the live form: fields are `user[display_name]`, `user[email]`, `user[pass_crypt]`, `user[pass_crypt_confirmation]`. Email confirm, no affiliation, no review.
- interface: rest
- limits note: GPX only (zip/tar/tar.gz accepted as a bundle). Visibility model changed in Aug 2026: 'Public' and 'Private' deprecated, leaving 'Identifiable' and 'Trackable'. Trackable = not listed publicly but still retrievable by id.
- interface detail: Web form + `POST /api/0.6/gpx/create` (401 Unauthorized without auth. Verified).
- tooling: any GPS app with OSM upload; `gpx_files` API; bulk via the rails API
- composes with: Not a blob store. .gpx (+ .zip/.tar.gz bundles) only. Useful as an append-only time-series archive, not for arbitrary objects.
- reliability: A trace is public-by-default unless you pick Trackable, so it is a poor fit for anything non-geographic.
- notes: the same as the free tier
- evidence note: reported: the pages read on 2026-11-03 are three OpenStreetMap wiki pages. https://wiki.openstreetmap.org/wiki/Upload states that only GPX traces can be uploaded, several in one zip, tar or tar.gz file. https://wiki.openstreetmap.org/wiki/API_v0.6 states that the GPX upload call requires authentication and that since August 2026 an upload must give the visibility trackable or identifiable (public and private now return an error). https://wiki.openstreetmap.org/wiki/Visibility_of_GPS_traces states that Public and Private were deprecated in August 2026 and that points are available via the API for every visibility level. These are community wiki pages, not a vendor quota page. The absence of a per-user quota, the sign-up form and the API authentication-failure answer are not covered by those pages, and the clause that a Trackable trace is retrievable by id is not stated on those pages, so the rung stays reported.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: No published per-user quota and no quota endpoint; storage is GPX-only and appended to the OSM rails DB + a trace store. Effectively unlimited in count, tiny per unit.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 401 'Couldn't authenticate you' (auth endpoint exists, read is gated per-user)
  - [3] 2026-10-21: form fields user[display_name], user[email], user[pass_crypt] (email-only signup)
  - [4] 2026-10-21: Aug 2026 deprecation of Public/Private; Identifiable vs Trackable matrix
  - [1] 2026-10-21: GPX-only, zip/tar bundles accepted
  - [5] 2026-11-03: POST /api/0.6/gpx uploads a GPX file or an archive of them | capture: sha256:0e5ba397cf16d6b7e872d4235ac20075d5409e5f2685554722c3ae0713de739d | quote: Use this to upload a GPX file or archive of GPX files. Requires authentication.
  - [4] 2026-11-03: points of every trace are available via the API, whatever the visibility | capture: sha256:b29ede398175cfb81cbceb7e1f09a194daecbdb233e386352bc642a93852477c | quote: This is currently always true, and there is no way to make a track completely private.
  - [4] 2026-11-03: the visibility levels in limits_note match the wiki | capture: sha256:b29ede398175cfb81cbceb7e1f09a194daecbdb233e386352bc642a93852477c | quote: The Public and Private levels were deprecated in August 2026.
  - [1] 2026-11-04: uploads are GPX only, several in one zip, tar or tar.gz | capture: sha256:92e9d1c1136d9146b707878322261709165880a4ea18c900fd6de915567d8e16 | quote: Only GPS traces in the GPX file format can be uploaded to OpenStreetMap; multiple GPX files can also be submited if using a single zip (or tar/tar.gz) file.
  - [5] 2026-11-04: the GPX upload is a REST call that requires authentication | capture: sha256:0e5ba397cf16d6b7e872d4235ac20075d5409e5f2685554722c3ae0713de739d | quote: Use this to upload a GPX file or archive of GPX files. Requires authentication.
- sources:
  - [1] https://wiki.openstreetmap.org/wiki/Upload
  - [2] https://api.openstreetmap.org/api/0.6/user/gpx_files
  - [3] https://www.openstreetmap.org/user/new
  - [4] https://wiki.openstreetmap.org/wiki/Visibility_of_GPS_traces
  - [5] https://wiki.openstreetmap.org/wiki/API_v0.6
