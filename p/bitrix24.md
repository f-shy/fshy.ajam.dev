# Bitrix24 Free

> bitrix24.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bitrix24/ | JSON https://fshy.ajam.dev/api/v1/entity/bitrix24.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Bitrix24 Free (Drive)

- `storage/bitrix24-free` | qualifies-with-caveat | evidence reported | binding retention-clamped | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.bitrix24.com
- free tier: Free plan: '5 GB storage' with 'Unlimited users - no team size limits'. Portals are free and self-service. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: Retention: 'inactive Free accounts may be deleted after 40 days'. This is a documented data-loss clause and the binding constraint. | days: 40 | source: [1] | note: not stated
- egress: No egress meter on any plan; Drive files served from the portal. Not part of the pricing table. | metered: no
- identity: email
- interface: rest, webdav, rclone
- limits:
  - retention-clamped (binding): Retention: 'inactive Free accounts may be deleted after 40 days [1]
  - retention-clamped (binding): deleted after 40 days [1]
- limits note: Per-object-cap: not published on the pricing page (Drive-specific cap unverified). Quota is per-portal, shared across Drive + CRM files + email attachments + call recordings. A mixed bucket. Retention: 'inactive Free accounts may be deleted after 40 days'. This is a documented data-loss clause and the binding constraint.
- binding note: a clock, not a quota: bytes leave whether or not transfer is completed
- interface detail: webdav
- tooling: Bitrix24 Drive mounts as a WebDAV network drive (documented for Windows/macOS); REST API also exposes disk.* methods. Third-party mounts exist (rclone via WebDAV, or OS-native WebDAV).
- composes with: 5 GB x unlimited free portals, each with unlimited users. 100 portals = 500 GB. WebDAV means a plain `rclone copy` per portal. The most scriptable of the free-workspace KBs.
- reliability: Inactive free portals are deleted after 40 days per Bitrix24's own blog, so an archive role requires periodic activity. Cannot attach external cloud storage to Drive.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: Free 'for 1–2 users', '5 GB storage'; Free 'unlimited users'
  - [2] 2026-10-21: '5 GB cloud storage – shared space for files' and 'inactive Free accounts may be deleted after 40 days'
  - [3] 2026-10-21: 'It is not possible to connect external cloud storage to Bitrix24'; Drive usage shared with CRM files and call recordings
- sources:
  - [1] https://www.bitrix24.com/prices/
  - [2] https://www.bitrix24.com/about/blogs/bitrix24-free-plan-everything-you-need-to-start-and-scale.php
  - [3] https://helpdesk.bitrix24.com/open/25769143/
