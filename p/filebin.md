# Filebin

> filebin.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filebin/ | JSON https://fshy.ajam.dev/api/v1/entity/filebin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filebin

- `storage/filebin` | fails-quota | evidence reported | binding retention-clamped | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:37.562Z (live) | stale on 2026-12-04
- url https://filebin.net
- free tier: no account; per-bin, no published byte cap; bins expire 6 days after creation | unit: mixed | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: no account; per-bin, no published byte cap; bins expire 6 days after creation | days: 6 | source: [1] | note: not stated
- egress: unmetered; downloads redirect to a signed S3 URL (Backblaze-style hel1-dc4) | metered: no
- identity: anonymous
- interface: rest
- limits:
  - retention-clamped (binding): expire 6 days [1]
  - retention-clamped (binding): retention from bin creation ('deleted automatically 6 days [1]
- limits note: 6-day retention from bin creation ('deleted automatically 6 days from now' on the create page). Bin is created implicitly by the first PUT.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: rest
- tooling: Plain HTTP PUT to a bin URL (curl -X PUT --data-binary @file -H 'filename: probe.bin' https://filebin.net/<bin>/probe.bin); the hosted service gates downloads behind bin approval. The Filebin server is also open source (github.com/espebra/filebin2, BSD-3) and can be self-hosted as a last resort.
- composes with: Unlimited distinct bin IDs, each with its own 6-day clock. 'N bins x 6 days' is the only multiplication, and nothing survives week 2.
- reliability: Bins are gated: the first-party FAQ shows a newly created bin as 'pending approval' with 'Downloads are not allowed as the bin is pending approval.' The self-hosted Filebin server source is published, but the hosted service at filebin.net applies the approval gate and 6-day expiry.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: no account; per-bin, no published byte cap; bins expire 6 days after creation
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: PUT https://filebin.net/e1probe1792600137/probe.bin -> 201, JSON echoes bytes:32768 + md5. GET same URL with curl's default UA -> 200, 32768 B, sha256 MATCH, 302 through to storage.filebin.net signed URL (X-Amz-Expires=900).
- evidence:
  - [1] 2026-10-21: 'deleted automatically 6 days from now', no-registration flow
  - withheld 2026-10-21: probe: PUT /<bin>/probe.bin -> 201 (32768 B, md5 echoed); GET with curl UA -> 200 / 32768 B / sha256 match; GET with Mozilla UA -> 200 / 5399 B HTML
  - [2] 2026-10-21: version v1.3.1, source github.com/espebra/filebin2
  - [1] 2026-11-19: the first-party page still states a 6-day automatic deletion from bin creation | capture: sha256:e6a70b6121252eed6052f13f436828d2272d97ebe61f4ffd6246854487cd075c | quote: will in any case be deleted automatically 6 days from now
  - [3] 2026-11-19: a bin is gated behind administrator approval before downloads are allowed | capture: sha256:851f8059e2050f51e91e8f9bf2791049eb3a9a3c65713333853e61c828362466 | quote: Downloads are not allowed as the bin is pending approval.
  - [3] 2026-11-19: downloads on the hosted service are blocked until a bin is approved | capture: sha256:851f8059e2050f51e91e8f9bf2791049eb3a9a3c65713333853e61c828362466 | quote: Downloads are not allowed as the bin is pending approval.
  - [2] 2026-11-19: the first-party about page states the server source is published and self-hostable | capture: sha256:c2354dc288f45491cafe2f3ee282ffdef71da5c829e879df6b50fbd1e2fe0e5c | quote: The source code is licensed under the BSD 3-clause license and it can be self hosted.
- sources:
  - [1] https://filebin.net/
  - [2] https://filebin.net/about
  - [3] https://filebin.net/faq

## filebin.net

- `storage/filebin-net` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:13:37.562Z (live) | stale on 2026-12-04
- url https://filebin.net/
- free tier: none reachable: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: Bins are automatically deleted 6 days from creation. | source: [1]
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
  - dead_end.failure_class: write-gated
  - dead_end.why: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price.
  - [2] 2026-10-21: cited as the basis of the rejection: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price.
  - [2] 2026-11-19: the first-party FAQ still shows the approval gate on downloads that underlies the rejection | capture: sha256:851f8059e2050f51e91e8f9bf2791049eb3a9a3c65713333853e61c828362466 | quote: Downloads are not allowed as the bin is pending approval.
  - [1] 2026-11-19: the first-party page states automatic deletion 6 days from bin creation | capture: sha256:e6a70b6121252eed6052f13f436828d2272d97ebe61f4ffd6246854487cd075c | quote: will in any case be deleted automatically 6 days from now
- sources:
  - [1] https://filebin.net/
  - [2] https://filebin.net/faq
