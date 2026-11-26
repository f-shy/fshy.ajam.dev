# file.io

> file.io | Storage; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/file/ | JSON https://fshy.ajam.dev/api/v1/entity/file.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## File.io

- `storage/file-io` | fails-quota | evidence reported | binding per-ip-shaping | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:37.015Z (live) | stale on 2026-12-04
- url https://file.io
- disagrees on identity_kind: `storage/file-io` says anonymous, `storage/file-io-2` says email
- disagrees on verdict: `storage/file-io` says fails-quota, `storage/file-io-2` says dead
- disagrees on identity_kind: `storage/file-io` says anonymous, `storage/file-io-3` says email
- free tier: no account; 4 GB per transfer ('file transfers are limited to a total of 4 GB') | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: 3-day expiry: 'The file is deleted automatically after 3 days, even if it was never downloaded'; 'The link works for 3 days. Each file can be downloaded up to 10 times a day.' The old expires= syntax and one-download deletion are no longer described. | days: 3 | source: [1] | note: not stated
- egress: unmetered direct link, but files self-destruct on first download | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-ip-shaping (binding): transfer ('file transfers are limited to a total of 4 GB') 4 GB/transfer [1]
- limits note: 4 GB per transfer; files expire after 3 days with up to 10 downloads per file per day; the old expires= syntax is no longer described.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: rest
- tooling: The old file.io API was retired in 2025; the about page directs scripted uploads to the LimeWire MCP server (https://www.file.io/developers).
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
  - [1] 2026-11-19: the first-party about page states a 3-day link life with up to 10 downloads per file per day | capture: sha256:e9e0141b38cbe95c7f11a3a46e250de5105c08a48da3df0e577bb941361b54cc | quote: The link works for 3 days. Each file can be downloaded up to 10 times a day.
  - [1] 2026-11-19: the stated file lifetime is 3 days | capture: sha256:e9e0141b38cbe95c7f11a3a46e250de5105c08a48da3df0e577bb941361b54cc | quote: The file is deleted automatically after 3 days, even if it was never downloaded, so nothing is left hanging around in the cloud.
  - [1] 2026-11-19: the 4 GB transfer cap is unchanged and the page states 3-day expiry with 10 downloads per day | capture: sha256:e9e0141b38cbe95c7f11a3a46e250de5105c08a48da3df0e577bb941361b54cc | quote: Yes, file transfers are limited to a total of 4 GB.
  - [1] 2026-11-19: upload and download are anonymous with no identity information required | capture: sha256:e9e0141b38cbe95c7f11a3a46e250de5105c08a48da3df0e577bb941361b54cc | quote: Users are not required to create an account or provide any personal information in order to upload or download files.
  - [1] 2026-11-19: the documented curl REST upload endpoint is retired | capture: sha256:e9e0141b38cbe95c7f11a3a46e250de5105c08a48da3df0e577bb941361b54cc | quote: The old file.io API was retired in 2025.
  - [1] 2026-11-19: the 4 GB no-account transfer offer is unchanged | capture: sha256:e9e0141b38cbe95c7f11a3a46e250de5105c08a48da3df0e577bb941361b54cc | quote: Share any type of file you like, with anyone, anywhere in the world. Files up to 4 GB can be shared without an account.
- sources:
  - [1] https://www.file.io/about
  - [2] https://file.io/

## file.io (now limewire)

- `storage/file-io-3` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:37.015Z (live) | stale on 2026-12-04
- url https://www.file.io/plans
- disagrees on identity_kind: `storage/file-io` says anonymous, `storage/file-io-3` says email
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
  - [2] 2026-11-19: the LimeWire free plan still expires files after 3 days, matching the rejection | capture: sha256:8c58b3fd40408b1294b8b39961e7cc0115c7c7f9941cbd1d0a50178b377d354f | quote: Files expire after 3 days
- sources:
  - [1] https://www.file.io/plans
  - [2] https://limewire.com/pricing
  - [3] https://www.file.io/developers

## file.io (documented api path)

- `storage/file-io-2` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:44.551Z (live) | stale on 2026-12-04
- url https://www.file.io/
- disagrees on identity_kind: `storage/file-io` says anonymous, `storage/file-io-2` says email
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
- reliability: The file-sharing service is live and files are deleted after 3 days; the old REST upload API was retired in 2025 in favour of the LimeWire MCP server.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: The REST flow printed in its own /about page no longer works: POST to both file.io and www.file.io returns 405 MethodNotAllowed from an S3-style object store.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The REST flow printed in its own /about page no longer works: POST to both file.io and www.file.io returns 405 MethodNotAllowed from an S3-style object store.
  - [1] 2026-11-19: the documented file.io upload API was retired; uploads now go through the LimeWire MCP server | capture: sha256:fc10a8150432a82de583be477b936f87c9a3475cd9f25d582697e4e061cea112 | quote: The old file.io API was retired in 2025. To upload files from an AI agent or an automation, use the LimeWire MCP server: [how to connect it](https://www.file.io/developers).
  - [1] 2026-11-19: the hosted file-sharing service deletes files after 3 days and is not a general storage offer | capture: sha256:fc10a8150432a82de583be477b936f87c9a3475cd9f25d582697e4e061cea112 | quote: The file is deleted automatically after 3 days, even if it was never downloaded, so nothing is left hanging around in the cloud.
- sources:
  - [1] https://www.file.io/
