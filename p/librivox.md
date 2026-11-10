# LibriVox

> librivox.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/librivox/ | JSON https://fshy.ajam.dev/api/v1/entity/librivox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LibriVox

- `debrid/librivox` | qualifies | evidence documented | binding per-ip-shaping | category public-domain audiobook library (metadata API + Internet Archive files) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:24:34.450Z (live) | stale on 2026-11-23
- url https://librivox.org/api/info
- price USD 0
- free tier: Free public-domain audiobooks, read by volunteers, with a JSON/XML catalogue API. The API caps a single response at 500 records ('Can no longer be set above 500', added 2026-09-26) and pages with offset. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The catalogue size is not published; the highest project id returned by sort_order=desc was 23017, which bounds it near 23,000 projects.
- per-object cap: not applicable: one MP3 per section, one ZIP per book. The ZIP is served by archive.org, so the object size is the Internet Archive item's size. | source: [1]
- retention: permanent: public-domain recordings 'donated to the public domain', with the audio stored as Internet Archive items | source: [2]
- egress: Metadata is free and unmetered from the API. The audio is not served by librivox.org: each record's url_zip_file points at archive.org/compress/<item>/..., so audio bytes are Internet Archive egress and inherit its per-IP shaping. | metered: no | free allowance: no byte allowance published | source: [1]
- identity: anonymous | detail: No key and no account: the API answered an anonymous GET with 200 and 3,084 bytes for limit=2.
- interface: rest, cli
- limits:
  - request-rate: 500 records maximum per request; 'If you intend to access a large number of records this way, please be considerate, and add a delay between your requests.' [1]
  - per-ip-shaping (binding): audio is fetched from archive.org, which shapes the caller (measured 1.99-3.17 MiB/s on this machine) [1]
- binding note: The API is metadata and would take minutes to walk at 500 records a request; the bytes come from archive.org, so the Internet Archive's per-IP ceiling is what decides a TiB-scale pull.
- interface detail: GET https://librivox.org/api/feed/audiobooks with id, since, author, title, genre, fields, extended, coverart, limit, offset, format, sort_order. Parameters may be path segments instead of query strings.
- endpoint: https://librivox.org/api/feed/audiobooks?format=json&limit=500&offset=0
- tooling: curl/python-requests; any HTTP client. No SDK and no rclone backend is needed because the metadata is a plain JSON API and the audio is a plain archive.org URL.
- composes with: Harvest the catalogue through the API (a few hundred requests), then pull the MP3s from archive.org - the same egress path and the same shaping as any other Internet Archive item.
- reliability: The API changed in 2026-09-26 to cap limit at 500; older clients that asked for more are silently clamped rather than rejected.
- notes: The interesting part is where the bytes are not: librivox.org serves a small JSON catalogue and archive.org serves the audio. A plan that expects a fast audiobook mirror from this API alone will move metadata and no media.
- evidence note: The API contract is the vendor's own page and was exercised here for two records; the audio path is read from the record's url_zip_file field, not downloaded. Downloading one ZIP would raise it.
- extras:
  - max_limit: 500
  - highest_project_id: 23017
  - audio_host: archive.org
- evidence:
  - [1] 2026-10-23: 'limit - ... Defaults to 50. Can no longer be set above 500', added 2026-09-26, and the 'add a delay between your requests' guidance
  - [2] 2026-10-23: 'Librivox donates its recordings to the public domain' and the non-commercial, ad-free terms
  - probe:https://librivox.org/api/feed/audiobooks?limit=2&format=json&sort_order=desc 2026-10-23: 200, 3,084 bytes of JSON; highest project id 23017, which bounds the catalogue near 23,000 projects
  - probe:https://librivox.org/api/feed/audiobooks?limit=1&format=json 2026-10-23: anonymous access works and the record carries url_zip_file pointing at archive.org/compress/<item>/
- sources:
  - [1] https://librivox.org/api/info
  - [2] https://librivox.org/pages/about-librivox/
