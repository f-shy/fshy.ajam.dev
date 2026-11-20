# Catbox

> catbox.moe | Storage; 6 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/catbox/ | JSON https://fshy.ajam.dev/api/v1/entity/catbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Catbox (catbox.moe + Litterbox)

- `storage/catbox` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:12:58.757Z (live) | stale on 2026-12-04
- url https://catbox.moe
- free tier: 200 MB per file on catbox.moe, no total quota. Anonymous or free account. Anonymous files live until 2 years of inactivity; files tied to an account are permanent. Litterbox (sister service) takes 1 GB but expires in 1h-3d by choice. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 200 MB per file | bytes: 200000000 | source: [1] | note: not stated
- retention: Anonymous files live until 2 years of inactivity; files tied to an account are permanent | days: 730 | source: [1] | note: not stated
- egress: free direct GET from files.catbox.moe, no metering, range requests supported. | metered: no
- identity: anonymous | detail: unverified: the pages read describe anonymous uploads and an optional free account but do not state a sign-up credential; no sign-up was performed
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 200 MB per file [1]
  - per-object-cap (binding): 200 MB/file [1]
- limits note: 200 MB/file (GIF 20 MB); anonymous retention is inactivity-based; albums 500 files; .exe/.scr/.cpl/.doc*/.jar blocked; single-operator service.
- interface detail: rest
- tooling: https://catbox.moe/user/api.php multipart (reqtype=fileupload, fileToUpload=@f) returns a bare URL. Official ShareX config, Chrome and Firefox extensions; many community Python/Node/Go/Rust libs. No rclone backend, no account API for listing.
- composes with: Allows unlimited anonymous uploads at 200 MB per file. Free registered accounts provide permanent retention rather than 2-year idle expiration.
- reliability: Uploads return a valid files.catbox.moe URL, but download testing on 2026-10-21 returned HTTP 200 with Content-Length: 0 and empty bodies across multiple files, despite Accept-Ranges headers.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Uploads up to 200 MB are allowed'
  - [2] 2026-10-21: 'Anonymously uploaded files are kept until they have 2 years of inactivity ... Uploads associated with user accounts are permanent'
  - [3] 2026-10-21: probe: curl -F reqtype=fileupload -F fileToUpload=@ct.txt -> https://files.catbox.moe/affeka.txt; then GET -> HTTP 200, bytes=0 (repeated 3x, incl. 1.2 MB binary and 5 MB binary)
  - [1] 2026-11-19: the upload page offers login and registration links but states no sign-up credential | capture: sha256:9f1a8a957417e5a880e1b84929b832077c5e68bc3696eadea48ed646f05c9775 | quote: [Login] | [Register]
  - [1] 2026-11-19: the upload page states the 200 MB per-file limit | capture: sha256:9f1a8a957417e5a880e1b84929b832077c5e68bc3696eadea48ed646f05c9775 | quote: Uploads up to 200 MB are allowed.
  - [2] 2026-11-19: the FAQ states anonymous retention and permanent account files | capture: sha256:91c52e81d8e069bf0cec75ff4824da63eda2f19804afc554df89966aae02342b | quote: Anonymously uploaded files are kept until they have 2 years of inactivity (no access/hits), after which they are removed. Uploads associated with user accounts are permanent.
- sources:
  - [1] https://catbox.moe/nojs/
  - [2] https://catbox.moe/faq.php
  - [3] https://catbox.moe/user/api.php

## catbox.moe (permanent)

- `storage/catbox-moe` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category rejected-provider
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:45:00.000Z (inherited) | stale on 2026-11-23
- url https://catbox.moe/
- free tier: No account required. The origin answered HTTP 200 on 2026-10-23; a 6,585,929-byte object was read back twice with a matching digest at 0.315 MiB/s sustained. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: unverified: the record carries no verified number as of 2026-10-23 | source: [1] | note: a cap exists and was recorded elsewhere as 200 MiB; it is not restated here without a read
- retention: loli.la and catbox differ and the difference was not checked here | source: [1]
- egress: Unmetered; the measured sustained rate was 0.315 MiB/s, which is per-ip-shaping rather than a byte cap. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: no account for an upload or a download
- interface: rest, cli
- limits:
  - per-ip-shaping (binding): 0.315 MiB/s sustained on one connection; 32 connections moved less than one probe:https://catbox.moe/
- binding note: the sustained rate, not a byte counter, is what a large retrieval meets first
- interface detail: not documented
- tooling: plain HTTPS GET; the upload endpoint takes a multipart form
- composes with: a free anonymous object host that needs no account; it composes as a relay or a small-object store, not as an archive
- reliability: the origin answered 521 on 2026-10-21 and 200 on 2026-10-23; an earlier verdict treated the outage as a failed quota
- notes: The cap and retention fields were left unread rather than restated.
- evidence note: the origin and the read path were checked; the cap and the retention were not
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Origin is DOWN/behind Cloudflare 521. Direct connection to its resolved IP 108.181.20.35 times out on:443 from…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-23: HTTP 200 with Cloudflare headers; the site serves
  - probe:https://catbox.moe/ 2026-10-23: 6,585,929 bytes read back twice with a matching digest; 0.315 MiB/s sustained
- sources:
  - [1] https://catbox.moe/

## grey-market residential proxies / donated bandwidth as an egress source

- `storage/grey-market-residential-proxies-donated-bandwidth-as-an` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:42.832Z (live) | stale on 2026-12-04
- url https://blog.catbox.moe/post/813932072453455872/happy-11th-birthday-catbox
- free tier: none reachable: Looked for it and did not find it. What exists instead is the reverse case: hosts lose capacity to consumer-connection and datacentre proxy fleets (catbox stopped accepting datacenter+proxy anonymous uploads in | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Looked for it and did not find it. What exists instead is the reverse case: hosts lose capacity to consumer-connection and datacentre proxy fleets (catbox stopped accepting datacenter+proxy anonymous uploads in
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Looked for it and did not find it. What exists instead is the reverse case: hosts lose capacity to consumer-connection and datacentre proxy fleets catbox stopped accepting datacenter+proxy anonymous uploads in
  - [2] 2026-10-21: cited as the basis of the rejection: Looked for it and did not find it. What exists instead is the reverse case: hosts lose capacity to consumer-connection and datacentre proxy fleets catbox stopped accepting datacenter+proxy anonymous uploads in
  - [1] 2026-11-19: the catbox operator post confirms hosts restrict proxy/datacenter egress, not donate it as a free storage offer | capture: sha256:bbf736d043075465982e3f55cec0339faf900c5f0047a703c0adc43c8b3a6c4f | quote: Effective immediately, anonymous uploads from datacenter and public proxy IP addresses has been restricted.
  - [2] 2026-11-19: 1fichier's first-party network page restricts datacenter/proxy connections rather than offering donated bandwidth as a free storage tier | capture: sha256:b978b56e61b5d2ea4fcff8247ef8219ff1eb13827ceb81d1376033ab105182e6 | quote: Professional or abusive equipment detected. Use of the service is heavily restricted from this connection.
- sources:
  - [1] https://blog.catbox.moe/post/813932072453455872/happy-11th-birthday-catbox
  - [2] https://1fichier.com/network.html

## litterbox (catbox temporary)

- `storage/litterbox` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:08.541Z (live) | stale on 2026-12-04
- url https://litterbox.catbox.moe/resources/internals/api.php
- free tier: None reachable: Explicitly temporary. Expiry is chosen at upload (1h/12h/1d/3d/7d max). Not storage by construction; only useful as an ephemeral hand-off. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: not-storage
  - dead_end.why: Explicitly temporary — expiry is chosen at upload (1h/12h/1d/3d/7d max). Not storage by construction; only useful as an ephemeral hand-off.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Explicitly temporary — expiry is chosen at upload (1h/12h/1d/3d/7d max). Not storage by construction; only useful as an ephemeral hand-off.
  - [2] 2026-11-19: litterbox is explicitly a temporary upload service, not persistent storage | capture: sha256:158b395e3fee824a1d14141858ccf7818777a91c8d1aa094f7221f4aa40e9c90 | quote: Temporary uploads up to 1 GB are allowed.
- sources:
  - [1] https://litterbox.catbox.moe/resources/internals/api.php
  - [2] https://litterbox.catbox.moe/

## litterbox.catbox.moe (temporary)

- `storage/litterbox-catbox-moe` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:49.635Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/catbox.md
- free tier: none reachable: Upload API is broken: POST to /resources/internals/api.php returns HTTP 500 (a full 69 KB HTML error page) for every time= value, with or without browser UA/Referer. The GET page renders… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: Temporary uploads up to 1 GB are allowed. | note: not applicable
- retention: Temporary uploads expire after a chosen 1 hour, 12 hours, 1 day or 3 days.
- egress: No ads and no throttling on downloads. | metered: no
- identity: email
- interface: rest, cli
- interface detail: HTTP multipart file-upload API at https://catbox.moe/user/api.php (reqtype=fileupload), driven by curl or CLI clients
- tooling: not documented
- composes with: stated-absent: the first-party page states no a way to chain uploads into other storage services; it is a standalone temporary host with browser extensions and API clients
- reliability: unverified: https://litterbox.catbox.moe/resources/internals/api.php answered HTTP 403 on 2026-11-19; routes tried: direct capture, every listed pinned page reader, a raw fetch with headers (HTTP 412 from the origin), and the Wayback Machine (403); the upload API could not be re-read
- notes: unverified: the upload API page could not be re-read on 2026-11-19; https://litterbox.catbox.moe/resources/internals/api.php answered HTTP 403 to a direct probe after every pinned reader, a raw fetch (HTTP 412) and the Wayback Machine (403) failed
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Upload API is broken: POST to /resources/internals/api.php returns HTTP 500 (a full 69 KB HTML error page) for every time= value, with or without browser UA/Referer. The GET page renders…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Upload API is broken: POST to /resources/internals/api.php returns HTTP 500 (a full 69 KB HTML error page) for every time= value, with or without browser UA/Referer. The GET page renders 'T
  - probe:https://litterbox.catbox.moe/resources/internals/api.php 2026-11-19: the first-party API page answered HTTP 403 to a direct request on 2026-11-19 | capture: sha256:0713a9df440cc17c02470b1e22285a7f2544e6e078a05b3f482b1a5b76a82f3f | quote: "status": 403
  - [1] 2026-11-19: the first-party tools page documents an HTTP file-upload API | capture: sha256:416b245f9f072953aee73591deb0cce373c06cfa498e6d1bfe67ec5eb8a29c17 | quote: The API is located at https://catbox.moe/user/api.php
  - [2] 2026-11-19: the Litterbox homepage lists the selectable expiry periods 1 hour, 12 hours, 1 day and 3 days | capture: sha256:24511fe1519f052ac685917e77ae7b868682789ffc92d3d6d9877c41ebb9c29f | quote: Expire after: 1 Hour 12 Hours 1 Day 3 Days
  - [2] 2026-11-19: the Litterbox homepage states a 1 GB maximum per temporary upload | capture: sha256:24511fe1519f052ac685917e77ae7b868682789ffc92d3d6d9877c41ebb9c29f | quote: Temporary uploads up to 1 GB are allowed.
  - [3] 2026-11-19: the operator first-party page states Litterbox 1 GB cap, 1/12/24/72-hour expiry and no throttling | capture: sha256:d3a402ef0a74958ff02d971c3cd2e4155c24d8dc89db4a430b5366e2a62fc6f6 | quote: Litterbox is a temporary file upload service that allows you to upload files up to 1GB. Choose whether to have your files expire in 1, 12, 24, or 72 hours. Similar to Catbox - 100% free, no ads, and no throttling.
  - [4] 2026-11-19: the FAQ describes temporary anonymous file storage with later deletion | capture: sha256:8961f743719f3321b4f29ddc2e791d2b1261962f1c33d813d4603d959662a203 | quote: Temporary file storage, so you don't have to waste my disk space, or if you just want to upload something anonymously but have it deleted after a while.
- sources:
  - [1] https://catbox.moe/tools.php
  - [2] https://litterbox.catbox.moe/
  - [3] https://catbox.llc/
  - [4] https://litterbox.catbox.moe/faq.php

## oversubscription as a stable strategy (sell 10 tb, provision 1 tb)

- `storage/oversubscription-as-a-stable-strategy` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:55.865Z (live) | stale on 2026-12-04
- url https://catbox.moe/support.php
- free tier: none reachable: It exists but it is not the lever people think, because the hosts already limit the thing that would break it. gofile caps free accounts at 10,000 contents and 10 days' inactivity rather… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: It exists but it is not the lever people think, because the hosts already limit the thing that would break it. gofile caps free accounts at 10,000 contents and 10 days' inactivity rather…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: It exists but it is not the lever people think, because the hosts already limit the thing that would break it. gofile caps free accounts at 10,000 contents and 10 days' inactivity rather…
  - [2] 2026-10-21: cited as the basis of the rejection: It exists but it is not the lever people think, because the hosts already limit the thing that would break it. gofile caps free accounts at 10,000 contents and 10 days' inactivity rather tha
  - [3] 2026-11-19: gofile's first-party FAQ confirms the 10-day inactivity retention that the record cites as the lever hosts already limit | capture: sha256:bcf53f25fbf9b540c33a6a6b133fc9831b6360ad119451ab35288808059f379d | quote: Content is kept for 10 days of inactivity, and stays longer as long as it keeps being downloaded.
  - [4] 2026-11-19: gofile's first-party API docs confirm the 10,000-content cap that the record cites | capture: sha256:42ca50ec0fbc772c7065f2b62d9c2f2e241c037e84e37bb6f87648115b68c824 | quote: Free accounts are capped at 10,000 stored contents — uploads past the cap fail with `error-limits`.
- sources:
  - [1] https://catbox.moe/support.php
  - [2] https://www.patreon.com/pixeldrain/posts/2025-cycle-never-147074953
  - [3] https://gofile.io/faq
  - [4] https://gofile.io/api
