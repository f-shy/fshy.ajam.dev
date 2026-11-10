# file.io

> file.io | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file/ | JSON https://fshy.ajam.dev/api/v1/entity/file.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File.io

- `storage/file-io` | fails-quota | evidence reported | binding per-ip-shaping | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://file.io
- disagrees on identity_kind: `storage/file-io` says institution, `storage/file-io-2` says email
- disagrees on verdict: `storage/file-io` says fails-quota, `storage/file-io-2` says dead
- disagrees on identity_kind: `storage/file-io` says institution, `storage/file-io-3` says email
- free tier: no account; 4 GB per transfer ('file transfers are limited to a total of 4 GB') | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 4 GB/transfer; default 14-day expiry, override with ?expires=N[day|w|M|y]; file is DELETED after the first download ('after it is downloaded, the file is completely deleted'). | days: 14 | source: [1] | note: not stated
- egress: unmetered direct link, but files self-destruct on first download | metered: no
- identity: institution
- interface: rest
- limits:
  - per-ip-shaping (binding): transfer ('file transfers are limited to a total of 4 GB') 4 GB/transfer [1]
- limits note: 4 GB/transfer; default 14-day expiry, override with ?expires=N[day|w|M|y]; file is DELETED after the first download ('after it is downloaded, the file is completely deleted').
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: documented REST: curl -F 'file=@x' https://file.io/?expires=1w -> {"success":true,"link":...,"expiry":"7 days"}
- composes with: None. One-download-then-delete semantics make it anti-storage by design.
- reliability: Docs still describe a working API, but both the apex and www return 301/405 today. The 405 comes from an object-store front end, so the API has been re-plumbed and the documented POST is stale. Would need browser/session cookies to find the new path.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no account; 4 GB per transfer ('file transfers are limited to a total of 4 GB')
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: POST https://file.io/ -> 301 to https://www.file.io/; POST https://www.file.io/ -> 405 MethodNotAllowed from an S3-style backend ('ResourceType: OBJECT'). The documented endpoint no longer accepts uploads. Upload path FAILED.
- evidence:
  - [1] 2026-10-21: 'file transfers are limited to a total of 4 GB', expires syntax, sample JSON responses
  - [2] 2026-10-21: probe: POST -> 301; POST https://www.file.io/ -> 405 MethodNotAllowed (ResourceType: OBJECT)
- sources:
  - [1] https://www.file.io/about
  - [2] https://file.io/

## file.io (now limewire)

- `storage/file-io-3` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.file.io/plans
- disagrees on identity_kind: `storage/file-io` says institution, `storage/file-io-3` says email
- disagrees on verdict: `storage/file-io-2` says dead, `storage/file-io-3` says fails-quota
- free tier: none reachable: file.io redirects into LimeWire. Free plan is 40 GB storage with a 4 GB upload cap and files expire after 3 days; 20 downloads per file per day. Retention makes it unusable as storage, and… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: retention
  - dead_end.why: file.io redirects into LimeWire. Free plan is 40 GB storage with a 4 GB upload cap and files expire after 3 days; 20 downloads per file per day. Retention makes it unusable as storage, and…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: file.io redirects into LimeWire. Free plan is 40 GB storage with a 4 GB upload cap and files expire after 3 days; 20 downloads per file per day. Retention makes it unusable as storage, and…
  - [2] 2026-10-21: cited as the basis of the rejection: file.io redirects into LimeWire. Free plan is 40 GB storage with a 4 GB upload cap and files expire after 3 days; 20 downloads per file per day. Retention makes it unusable as storage, and t
  - [3] 2026-10-21: cited as the basis of the rejection: file.io redirects into LimeWire. Free plan is 40 GB storage with a 4 GB upload cap and files expire after 3 days; 20 downloads per file per day. Retention makes it unusable as storage, and t
- sources:
  - [1] https://www.file.io/plans
  - [2] https://limewire.com/pricing
  - [3] https://www.file.io/developers

## file.io (documented api path)

- `storage/file-io-2` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.file.io/
- disagrees on identity_kind: `storage/file-io` says institution, `storage/file-io-2` says email
- disagrees on verdict: `storage/file-io` says fails-quota, `storage/file-io-2` says dead
- disagrees on verdict: `storage/file-io-2` says dead, `storage/file-io-3` says fails-quota
- free tier: none reachable: The REST upload flow documented on /about returns HTTP 405 Method Not Allowed on POST to file.io and www.file.io. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: dead-service
  - dead_end.why: The REST flow printed in its own /about page no longer works: POST to both file.io and www.file.io returns 405 MethodNotAllowed from an S3-style object store.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The REST flow printed in its own /about page no longer works: POST to both file.io and www.file.io returns 405 MethodNotAllowed from an S3-style object store.
- sources:
  - [1] https://www.file.io/
