# temp.sh

> temp.sh | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/temp/ | JSON https://fshy.ajam.dev/api/v1/entity/temp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## temp.sh

- `storage/temp-sh` | fails-quota | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:28.944Z (live) | stale on 2026-12-04
- url https://temp.sh
- disagrees on identity_kind: `storage/temp-sh` says anonymous, `storage/temp-sh-uguu-se-litterbox-tmpfiles-org` says email
- free tier: no account; 4 GB per file, 3-day retention | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 4 GB per file | bytes: 4000000000 | source: [1] | note: not stated
- retention: no account; 4 GB per file, 3-day retention | 4 GB/file, 'Files expire after 3 days' (page description: 'Temporary File Upload | days: 3 | source: [1] | note: not stated
- egress: unmetered but requires a POST to the file page (a form submit, not a GET) | metered: no
- identity: anonymous
- interface: rest
- limits:
  - per-object-cap (binding): 4 GB per file [1]
  - per-object-cap (binding): 4 GB/file [1]
  - retention-clamped: retention 4 GB/file, 'Files expire after 3 days [1]
- limits note: 4 GB/file, 'Files expire after 3 days' (page description: 'Temporary File Upload. 3 days. 4GB Size Limit.').
- interface detail: rest
- tooling: curl -F 'file=@x' https://temp.sh/upload ; ShareX supported per the page
- composes with: None. Per-file, 3-day expiry.
- reliability: Download links require submitting an HTML confirmation form rather than serving raw binary bytes on direct GET requests. Automated download tools and proxies receive an HTML landing page unless following the interactive form submission flow.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: no account; 4 GB per file, 3-day retention
  - dead_end.first_recorded: 2026-10-21
  - probe_reported: POST /upload -> 200 'https://temp.sh/VQJJo/probe.bin'. GET that URL -> 200 but 3165 B text/html (a page with a single <form method=POST> 'Click here to download'). POST to the same URL -> 200, 32768 B, sha256 MATCH.
- evidence:
  - [1] 2026-10-21: 'Files expire after 3 days', 4 GB, curl -F upload example
  - withheld 2026-10-21: probe: POST /upload -> 200 + URL; GET URL -> 200 / 3165 B HTML (form); POST URL -> 200 / 32768 B / sha256 match
  - [1] 2026-11-19: the homepage still states a 3-day file expiry | capture: sha256:60c15be8b8497dd542a649faa0a685c420c57db21e1986b2e29933fb68737048 | quote: Files expire after 3 days
  - [1] 2026-11-19: the homepage still states a 4GB file size limit | capture: sha256:60c15be8b8497dd542a649faa0a685c420c57db21e1986b2e29933fb68737048 | quote: Current file size limit is 4GB
- sources:
  - [1] https://temp.sh/

## temp.sh / uguu.se / litterbox / tmpfiles.org (transfer.sh lineage)

- `storage/temp-sh-uguu-se-litterbox-tmpfiles-org` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:28.944Z (live) | stale on 2026-12-04
- url https://temp.sh/
- disagrees on identity_kind: `storage/temp-sh` says anonymous, `storage/temp-sh-uguu-se-litterbox-tmpfiles-org` says email
- free tier: none reachable: All are short-TTL transfer services, not storage: temp.sh 4 GB but 3-day expiry; uguu.se 128 MiB and 3 hours; Litterbox 1 GB but 1 hour-3 days; tmpfiles.org 100 MB and 60 min-48 h. transfer. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: All are short-TTL transfer services, not storage: temp.sh 4 GB but 3-day expiry; uguu.se 128 MiB and 3 hours; Litterbox 1 GB but 1 hour-3 days; tmpfiles.org 100 MB and 60 min-48 h. transfer.
  - dead_end.retry_when: never; it is not storage
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: All are short-TTL transfer services, not storage: temp.sh 4 GB but 3-day expiry; uguu.se 128 MiB and 3 hours; Litterbox 1 GB but 1 hour-3 days; tmpfiles.org 100 MB and 60 min-48 h. transfer.
  - [2] 2026-10-21: cited as the basis of the rejection: All are short-TTL transfer services, not storage: temp.sh 4 GB but 3-day expiry; uguu.se 128 MiB and 3 hours; Litterbox 1 GB but 1 hour-3 days; tmpfiles.org 100 MB and 60 min-48 h. transfer.
  - [3] 2026-10-21: cited as the basis of the rejection: All are short-TTL transfer services, not storage: temp.sh 4 GB but 3-day expiry; uguu.se 128 MiB and 3 hours; Litterbox 1 GB but 1 hour-3 days; tmpfiles.org 100 MB and 60 min-48 h. transfer.
  - [2] 2026-11-19: uguu.se still caps uploads at 128 MiB and expires files after 3 hours | capture: sha256:ec186c91dd4bdfac1ab1b1cab97cd5fcfcf8d6f8073a4c52e569c880db067f47 | quote: Max upload size is 128 MiB & files expire after 3 hours.
  - [3] 2026-11-19: Litterbox still allows temporary uploads up to 1 GB | capture: sha256:158b395e3fee824a1d14141858ccf7818777a91c8d1aa094f7221f4aa40e9c90 | quote: Temporary uploads up to 1 GB are allowed.
- sources:
  - [1] https://temp.sh/
  - [2] https://uguu.se/
  - [3] https://litterbox.catbox.moe/
