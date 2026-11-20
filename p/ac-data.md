# ACdata

> ac-data.info | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ac-data/ | JSON https://fshy.ajam.dev/api/v1/entity/ac-data.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ACdata (ac-data.info)

- `storage/acdata` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:12:57.315Z, checked 2026-10-21 (inherited) | stale on 2026-11-05
- url https://ac-data.info
- free tier: Two products on one site. Transfer: 'ファイル容量を無制限（1ファイル 250ギガ）、ファイル保存期限最大65日、完全無料'. Unlimited total, 250 GB per file, up to 65 days. Separate cloud-drive product: 10 GB free, 30 GB if you hold premium on IllustratorAC/PhotoAC/SilhouetteAC. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 250 GB per file | bytes: 250000000000 | source: [1] | note: not stated
- retention: per-object-cap 250 GB; retention max 65 days; anonymous (browser-cache) uploads are deleted after 14 days | days: 65 | source: [1] | note: not stated
- egress: No metered bandwidth; funded by the AC illustration-marketplace family. | metered: yes
- identity: anonymous | detail: unverified: the live page answered HTTP 405 with an AWS WAF captcha on 2026-11-09, so no signup form was seen
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
- notes: unverified: https://ac-data.info/ answered HTTP 405 on 2026-11-11 and served a human-verification page; the offer pages were not readable
- evidence:
  - [1] 2026-10-21: 'ACデータでは、ファイル容量を無制限（1ファイル 250ギガ）、ファイル保存期限最大65日、完全無料'
  - [1] 2026-10-21: '無料で10GB！クラウドストレージ機能で長期間ファイル保存が可能になりました'
  - [1] 2026-10-21: browser-cache-only uploads 'アップロードしてから14日後にファイルが削除されます'
  - [1] 2026-11-09: the live page is a WAF captcha, so no signup form could be read | capture: sha256:44c579219e47ad6483a0062562286ca3d9b8ccf50ef80441be534b02c3cfc1e7 | quote: x-amzn-waf-action: captcha
  - [2] 2026-11-09: the archived 2026-10-08 copy states a 250 GB per-file cap | capture: sha256:998e0b421f5d8d0f846261cccfafbf251f2661c0c4e118e7a3e36aa5cdc5c934 | quote: ACデータでは、ファイル容量を無制限（1ファイル 250ギガ）、ファイル保存期限最大65日、完全無料でテレワークを応援します。
  - probe:https://ac-data.info/ 2026-11-11: the page answered HTTP 405 | capture: sha256:f8b8961be2f1e35421151eace5a721c8797edb4c3d03394ffd187b4c8d6d1ede | quote: "status": 405
  - probe:https://ac-data.info/ 2026-11-19: the page still answers HTTP 405 with a human-verification challenge | capture: sha256:ba9eda15759405a60d404b2398b3b2e55625e2f9298219958b6f41c03138537b | quote: "status": 405
- sources:
  - [1] https://ac-data.info/
  - [2] https://web.archive.org/web/20261008230046/https://ac-data.info/
