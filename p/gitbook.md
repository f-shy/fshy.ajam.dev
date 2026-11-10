# GitBook

> gitbook.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gitbook/ | JSON https://fshy.ajam.dev/api/v1/entity/gitbook.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## GitBook (Free plan file library)

- `storage/gitbook` | qualifies-with-caveat | evidence reported | binding per-object-cap | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.gitbook.com
- disagrees on identity_kind: `storage/gitbook` says institution, `storage/gitbook-2` says email
- disagrees on verdict: `storage/gitbook` says qualifies-with-caveat, `storage/gitbook-2` says fails-quota
- free tier: No published total storage quota. Per-file cap is explicit: 'GitBook allows you to upload files up to 100MB per file.' GitBook's own docs ask-API, queried live, answered: 'I cannot find a documented storage quota or total storage limit per organization on the Free plan.' | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 100MB per file | bytes: 100000000 | source: [1] | note: not stated
- retention: Access token in the download URL is NOT enforced. A deliberately bogus `token=0000` returned the identical 838-byte file (same sha256), so file URLs are effectively public and permanent. | source: [1] | note: not stated
- egress: Free and CDN-served. Files land on `*-files.gitbook.io` (backed by `gitbook-x-prod.appspot.com`), fronted by Cloudflare with `Cache-Control: public, max-age=31536000`, `Accept-Ranges: bytes`, `Access-Control-Allow-Origin: *`. | metered: no
- identity: institution
- interface: rest, git, rclone
- limits:
  - per-object-cap (binding): 100MB per file [1]
- limits note: Per-object-cap: 100 MB per file. The only hard published number. Total org storage: undocumented (searched the docs ask-API, no figure). Retention: files persist while the org exists; no TTL clause.
- interface detail: rest
- tooling: GitBook Platform API `POST /v1/orgs/{org}/storage` + a `?ask=` query interface on the docs. No rclone backend. Git sync (GitHub/GitLab) is a second, separate route.
- composes with: Unlimited free GitBook accounts/orgs x 100 MB per file x unbounded file count (undocumented total). If the total really is unbounded this is per-record-unlimited; if it is soft-limited, the multiplier is free orgs.
- reliability: Access token in the download URL is NOT enforced. A deliberately bogus `token=0000` returned the identical 838-byte file (same sha256), so file URLs are effectively public and permanent. That cuts both ways: stable hotlinks, but no way to keep a file private.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'GitBook allows you to upload files up to 100MB per file.'
  - [2] 2026-10-21: probe: GET -> 200, 838 bytes, sha256 2d47fd8e...7356 — byte-identical to the correct-token fetch; the token is decorative
  - withheld 2026-10-21: probe: same URL with `Range: bytes=0-99` -> 206, 100 bytes (ranging works, so parallel ranged GETs are available)
  - [3] 2026-10-21: ... — 'I cannot find a documented storage quota or total storage limit per organization on the Free plan'
- sources:
  - [1] https://gitbook.com/docs/create-content/blocks/insert-files
  - [2] https://1050631731-files.gitbook.io/~/files/v0/gitbook-x-prod.appspot.com/o/spaces%2F...%2Factions.svg?alt=media&token=0000
  - [3] https://gitbook.com/docs/developers/gitbook-api/api-reference/storage.md?ask=

## gitbook (free site plan)

- `storage/gitbook-2` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:23.415Z (live) | stale on 2026-11-18
- url https://www.gitbook.com/pricing
- disagrees on identity_kind: `storage/gitbook` says institution, `storage/gitbook-2` says email
- disagrees on verdict: `storage/gitbook` says qualifies-with-caveat, `storage/gitbook-2` says fails-quota
- free tier: None reachable: Free plan exists but publishes zero storage, bandwidth or file-size figures. It is positioned as a docs editor, not a host. No quota to verify means no basis to qualify it; hosting terms ar. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: uploaded files up to 100MB per file | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: Traffic to published sites is not limited: page views are unlimited on the Free plan; no bandwidth or storage figure is published for Free. | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: the 2026-11-03 read covered https://www.gitbook.com/pricing (unlimited page views, no traffic limit) and https://gitbook.com/docs/create-content/blocks/insert-files (100MB per uploaded file); neither page states a storage quota, so the no-quota basis of the verdict is not re-proved by a quote
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: Free plan exists but publishes zero storage, bandwidth or file-size figures — it is positioned as a docs editor, not a host. No quota to verify means no basis to qualify it; hosting terms…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free plan exists but publishes zero storage, bandwidth or file-size figures — it is positioned as a docs editor, not a host. No quota to verify means no basis to qualify it; hosting terms…
  - [2] 2026-10-21: cited as the basis of the rejection: Free plan exists but publishes zero storage, bandwidth or file-size figures — it is positioned as a docs editor, not a host. No quota to verify means no basis to qualify it; hosting terms ar
  - [1] 2026-11-03: traffic to published sites is not limited | capture: sha256:12b97b45225fc0d151c22fcaf3ed523925a28d71e632064fead806c44b7a333a | quote: We never limit the amount of traffic to your published documentation.
  - [1] 2026-11-03: Free plan page views are unlimited | capture: sha256:12b97b45225fc0d151c22fcaf3ed523925a28d71e632064fead806c44b7a333a | quote: Page views: Free, Essential, Ultimate, and Enterprise plans: Unlimited.
  - [3] 2026-11-03: uploaded files are capped at 100MB each | capture: sha256:a75f93ea8ad3c2a716543890b985f5394a3f3483be0d528acc0a6240f96e7332 | quote: GitBook allows you to upload files up to 100MB per file.
- sources:
  - [1] https://www.gitbook.com/pricing
  - [2] https://gitbook.com/docs/account-and-billing/plans.md
  - [3] https://gitbook.com/docs/create-content/blocks/insert-files
