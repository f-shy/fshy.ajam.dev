# rclone

> rclone.org | Storage, Debrid; 3 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/rclone/ | JSON https://fshy.ajam.dev/api/v1/entity/rclone.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## linkbox (linkbox.to)

- `storage/linkbox` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://rclone.org/linkbox/
- free tier: None reachable: Has a genuine merged rclone backend (PR #7055, read+write, API token from /admin/account) but the free allowance is tens of GB and the API takes the auth token as a query parameter. A crede. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: Has a genuine merged rclone backend (PR #7055, read+write, API token from /admin/account) but the free allowance is tens of GB and the API takes the auth token as a query parameter — a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Has a genuine merged rclone backend (PR #7055, read+write, API token from /admin/account) but the free allowance is tens of GB and the API takes the auth token as a query parameter — a…
  - [2] 2026-10-21: cited as the basis of the rejection: Has a genuine merged rclone backend (PR #7055, read+write, API token from /admin/account) but the free allowance is tens of GB and the API takes the auth token as a query parameter — a crede
  - [3] 2026-10-21: cited as the basis of the rejection: Has a genuine merged rclone backend (PR #7055, read+write, API token from /admin/account) but the free allowance is tens of GB and the API takes the auth token as a query parameter — a crede
- sources:
  - [1] https://rclone.org/linkbox/
  - [2] https://www.linkbox.to/admin/account
  - [3] https://github.com/rclone/rclone/issues/6629

## ulož.to free tier

- `storage/ulo-to-free-tier` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://forum.rclone.org/t/alternative-free-drive-to-uloz/53751
- free tier: none reachable: The rclone forum's canonical 'free drive' lost its appeal: free storage cut from 20 GB to ~1 GB (needs a bank card). Tracked as a live migration event by rclone users, not a provider. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
  - dead_end.why: The rclone forum's canonical 'free drive' lost its appeal: free storage cut from 20 GB to ~1 GB (needs a bank card). Tracked as a live migration event by rclone users, not a provider.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: The rclone forum's canonical 'free drive' lost its appeal: free storage cut from 20 GB to ~1 GB (needs a bank card). Tracked as a live migration event by rclone users, not a provider.
- sources:
  - [1] https://forum.rclone.org/t/alternative-free-drive-to-uloz/53751

## rclone - premiumizeme backend

- `debrid/rclone-premiumizeme` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding none | category client: mount and sync (rclone backend) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:51:00.000Z (live) | stale on 2026-11-23
- url https://rclone.org/premiumizeme/
- price USD 0 for the caller; the storage behind it is EUR 9.99/month | parsed USD 11.18/mo
- free tier: Free software with no account and no quota of its own; transfer is metered by the underlying debrid account. The backend was added in v1.49 and carries Tier 3 in rclone's support table. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable to the caller; the object cap is the debrid account's. | source: [1]
- retention: not applicable: a mount reflects the remote's contents live. | source: [1]
- egress: rclone does not meter or bill; it reads through the debrid account and therefore spends that account's fair-use budget. | metered: no | free allowance: none of its own | source: [1]
- identity: anonymous | detail: No registration with rclone; it inherits the debrid account's identity. Installing it needs no account at all. | country: None
- interface: rclone, webdav
- limits:
  - request-rate: none published by rclone; the upstream Premiumize rate limit is unpublished and surfaces as a 200-with-rate_limit_reached envelope the backend must interpret [1]
- limits note: Read-only: no upload path exists in this backend, so a workflow that writes into debrid cloud cannot use it.
- binding note: The client imposes nothing; at 1 TiB/month the binding constraint is the Premiumize fair-use meter, not the mount.
- interface detail: Configured with 'rclone config' -> 'premiumizeme'; authentication is an interactive OAuth token in a browser, not the raw API key, so a headless box needs the token copied in. The backend is read-only.
- endpoint: https://www.premiumize.me/api
- tooling: rclone itself, plus anything that speaks to an rclone mount: Plex, Jellyfin, Emby, restic, rsync over the mount.
- composes with: This is the only direct, first-party path from a plain Unix command to any of the eight services: 'rclone mount premiumizeme:' and published records has a filesystem, with no zurg, no shim and no container.
- reliability: A mount is only as stable as the upstream API; a Premiumize throttle comes back as a success-shaped JSON envelope and shows up as a stalled read rather than an error.
- notes: Named as a separate record because 'which debrid service has an rclone backend' is a question six of the eight answer 'none' and one answers 'yes'. Trigger condition: a real-debrid or torbox backend landing in rclone makes this record a comparison, not a singleton.
- evidence note: The backend page and the backend table were read. Nothing was mounted, so the throughput claim is absent rather than estimated.
- self hosted: yes
- extras:
  - backend_status: Tier 3 in rclone's own table, which is the lowest support tier for a backend
  - write_support: none: read-only backend
  - alternative_route: TorBox publishes a first-party WebDAV endpoint (https://webdav.torbox.app), which rclone can mount as a generic WebDAV remote with no backend at all
  - shim_route: Real-Debrid reaches rclone only through zurg's WebDAV, which is a separate binary and a separate record
- evidence:
  - [1] 2026-10-23: 'added in v1.49', Tier 3, and the browser OAuth configuration flow for the premiumizeme backend
  - [2] 2026-10-23: the full backend table lists premiumizeme as read-only ('R') and lists no other debrid service
- sources:
  - [1] https://rclone.org/premiumizeme/
  - [2] https://rclone.org/overview/
