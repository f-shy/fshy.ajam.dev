# LibriVox

> librivox.org | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/librivox/ | JSON https://fshy.ajam.dev/api/v1/entity/librivox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LibriVox

- `debrid/librivox` | qualifies | evidence documented | binding per-ip-shaping | category public-domain audiobook library (metadata API + Internet Archive files) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:47:00.873Z (live) | stale on 2026-12-26
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
- reliability: unverified: HTTP 522 on 2026-11-25; no anonymous live GET to the feed was confirmed, and a probe recorded the status.
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
  - [1] 2026-11-25: The API still caps one response at 500 records | capture: sha256:9f8787c1abbef5288d3be98c4019c4431d1ab9b4515734415b0fbd9099c04c1b | quote: limit - will cap the number of results you receive. Defaults to 50. Can no longer be set above 500.
  - [1] 2026-11-25: The vendor still asks for a delay between large request runs | capture: sha256:9f8787c1abbef5288d3be98c4019c4431d1ab9b4515734415b0fbd9099c04c1b | quote: If you intend to access a large number of records this way, please be considerate, and add a delay between your requests.
  - [1] 2026-11-25: Audio ZIPs are hosted by Archive.org rather than by librivox.org | capture: sha256:9f8787c1abbef5288d3be98c4019c4431d1ab9b4515734415b0fbd9099c04c1b | quote: url\_zip\_file - the URL of a .zip file containing the all of the audio files. Hosted by Archive.org.
  - [2] 2026-11-25: Recordings are dedicated to the public domain | capture: sha256:db1728d9d982b2b8d9c6ef3546b9c10c2d630f85ede8445def0dd7ed47ac1419 | quote: Librivox donates its recordings to the public domain
  - probe:https://librivox.org/api/feed/audiobooks?limit=2&format=json&sort_order=desc 2026-11-25: The API feed answered HTTP 522 to an anonymous GET on 2026-11-25 | capture: sha256:a2e6d128da4385eafd9656b2ce8b87540acd6c3420210fd3464c76efabe66410 | quote: "status": 522
- sources:
  - [1] https://librivox.org/api/info
  - [2] https://librivox.org/pages/about-librivox/
