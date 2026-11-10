# Catbox

> catbox.moe | Storage; 5 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/catbox/ | JSON https://fshy.ajam.dev/api/v1/entity/catbox.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Catbox (catbox.moe + Litterbox)

- `storage/catbox` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://catbox.moe
- free tier: 200 MB per file on catbox.moe, no total quota. Anonymous or free account. Anonymous files live until 2 years of inactivity; files tied to an account are permanent. Litterbox (sister service) takes 1 GB but expires in 1h-3d by choice. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 200 MB per file | bytes: 200000000 | source: [1] | note: not stated
- retention: Anonymous files live until 2 years of inactivity; files tied to an account are permanent | days: 730 | source: [1] | note: not stated
- egress: free direct GET from files.catbox.moe, no metering, range requests supported. | metered: no
- identity: anonymous
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
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://blog.catbox.moe/post/813932072453455872/happy-11th-birthday-catbox
  - [2] https://1fichier.com/network.html

## litterbox (catbox temporary)

- `storage/litterbox` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://litterbox.catbox.moe/resources/internals/api.php

## oversubscription as a stable strategy (sell 10 tb, provision 1 tb)

- `storage/oversubscription-as-a-stable-strategy` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- sources:
  - [1] https://catbox.moe/support.php
  - [2] https://www.patreon.com/pixeldrain/posts/2025-cycle-never-147074953
