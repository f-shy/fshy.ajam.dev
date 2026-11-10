# zoom team

> zoom.us | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zoom/ | JSON https://fshy.ajam.dev/api/v1/entity/zoom.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## zoom team chat files

- `storage/zoom-team-chat-files` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://developers.zoom.us/docs/team-chat/
- free tier: download_token scoping and plan-dependent retention make anonymous serving implausible. Left recorded so nobody re-runs the same failed fetches. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: the same as the free tier
- notes: the same as the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: download_token scoping and plan-dependent retention make anonymous serving implausible. Left recorded so nobody re-runs the same failed fetches.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: download_token scoping and plan-dependent retention make anonymous serving implausible. Left recorded so nobody re-runs the same failed fetches.
- sources:
  - [1] https://developers.zoom.us/docs/team-chat/

## Zoom Team Chat — files API

- `storage/zoom-team-chat-files-api` | fails-quota | evidence inferred | binding none | category messaging
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-21
- url https://developers.zoom.us/docs/team-chat/
- free tier: No storage quota obtained. Zoom's chat-files docs were not readable through any allowed path (empty reader output, no retention number). | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Unknown/unverified. Zoom file downloads are token-scoped (download_token), so anonymous serving is unlikely. | metered: no
- identity: email
- interface: rest, rclone
- limits note: Unverified. Documentation endpoint returned an empty response on 2026-10-21.
- interface detail: rest
- tooling: Zoom REST API v2 (/chat/users/{userId}/messages, /files). No rclone backend; no third-party bulk client found.
- composes with: Cannot be assessed without the retention number. Free Zoom accounts have historically capped chat file retention and total cloud storage, so assume no.
- reliability: Unresolved. Do not treat as available; the absence of a published retention figure is itself a warning that retention is plan-dependent.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: No storage quota obtained. Zoom's chat-files docs were not readable through any allowed path (empty reader output, no retention number).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: unverified: reader returned empty content; no quota or retention statement extracted
  - [2] 2026-10-21: unverified: returned an unrelated audio-settings article, wrong article id
- sources:
  - [1] https://developers.zoom.us/docs/team-chat/
  - [2] https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060612
