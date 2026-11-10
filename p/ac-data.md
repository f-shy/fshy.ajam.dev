# ACdata

> ac-data.info | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ac-data/ | JSON https://fshy.ajam.dev/api/v1/entity/ac-data.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ACdata (ac-data.info)

- `storage/acdata` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ac-data.info
- free tier: Two products on one site. Transfer: 'ファイル容量を無制限（1ファイル 250ギガ）、ファイル保存期限最大65日、完全無料'. Unlimited total, 250 GB per file, up to 65 days. Separate cloud-drive product: 10 GB free, 30 GB if you hold premium on IllustratorAC/PhotoAC/SilhouetteAC. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 250 GB per file | bytes: 250000000000 | source: [1] | note: not stated
- retention: per-object-cap 250 GB; retention max 65 days; anonymous (browser-cache) uploads are deleted after 14 days | days: 65 | source: [1] | note: not stated
- egress: No metered bandwidth; funded by the AC illustration-marketplace family. | metered: yes
- identity: anonymous
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 250 GB per file [1]
  - retention-clamped: retention max 65 days [1]
  - retention-clamped: deleted after 14 days [1]
- limits note: per-object-cap 250 GB; retention max 65 days; anonymous (browser-cache) uploads are deleted after 14 days. The 10 GB drive is separate from the transfer allowance and does not stack with it.
- interface detail: rest
- tooling: Web upload form only; no API and no rclone backend.
- composes with: Account-less transfer allows 250 GB across unlimited objects with 65 days maximum retention in a re-upload cycle. The separate 10 GB cloud drive provides persistent storage.
- reliability: Run by the AC illustration-workspace group, so it is a marketing surface for their paid art subscriptions rather than a storage business. Historically stable, and the '10 GB free cloud' add-on is recent.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'ACデータでは、ファイル容量を無制限（1ファイル 250ギガ）、ファイル保存期限最大65日、完全無料'
  - [1] 2026-10-21: '無料で10GB！クラウドストレージ機能で長期間ファイル保存が可能になりました'
  - [1] 2026-10-21: browser-cache-only uploads 'アップロードしてから14日後にファイルが削除されます'
- sources:
  - [1] https://ac-data.info/
