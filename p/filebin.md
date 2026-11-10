# Filebin

> filebin.net | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filebin/ | JSON https://fshy.ajam.dev/api/v1/entity/filebin.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filebin

- `storage/filebin` | fails-quota | evidence reported | binding retention-clamped | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
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
- tooling: Plain HTTP PUT. 'curl -X PUT --data-binary @file -H "filename: probe.bin" https://filebin.net/<bin>/probe.bin'. Open source (github.com/espebra/filebin2, BSD-3) so it can be self-hosted.
- composes with: Unlimited distinct bin IDs, each with its own 6-day clock. 'N bins x 6 days' is the only multiplication, and nothing survives week 2.
- reliability: IMPORTANT INVERSION: a real browser UA (Mozilla/..) gets a 5399-byte 'are you sure / proceed to download' interstitial at HTTP 200; curl's default UA gets the real bytes. Automation works better than a browser here. The opposite of the usual trap. Any client that sets a browser UA (rclone, most HTTP libs, headless Chrome) will silently receive HTML instead of the file.
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
- sources:
  - [1] https://filebin.net/
  - [2] https://filebin.net/about

## filebin.net

- `storage/filebin-net` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filebin.net/
- free tier: none reachable: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.failure_class: write-gated
  - dead_end.why: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price.
  - [2] 2026-10-21: cited as the basis of the rejection: Hard 6-day automatic deletion of every bin, and bins require approval before downloads are allowed. No persistence path at any price.
- sources:
  - [1] https://filebin.net/
  - [2] https://filebin.net/faq
