# firestorage.jp

> firestorage.jp | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/firestorage/ | JSON https://fshy.ajam.dev/api/v1/entity/firestorage.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## firestorage.jp (ファイヤーストレージ)

- `storage/firestorage-jp` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://firestorage.jp
- free tier: Unregistered and free-member tiers: per-file max 300 GiB, unlimited number of uploads. The free member storage drive is only 2 GiB (25 GiB light, 100 GiB regular). The 'capacity unlimited' claim applies to the transfer service, not the drive. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 300 GiB per file | bytes: 322122547200 | source: [1] | note: not stated
- retention: Retention: user-selectable, '最長で14日間' on オクル, default 3 days; if unset the operator deletes on its own algorithm | days: 3 | source: [1] | note: not stated
- egress: No bandwidth metering on the free tiers; paid tiers sell storage GB and ad removal, not transfer. | metered: no
- identity: anonymous
- interface: rest, webdav
- limits:
  - per-object-cap (binding): 300 GiB per file [1]
  - retention-clamped: Retention: user-selectable, '最長で14日間' on オクル, default 3 days [1]
- limits note: 300 GiB per file. Retention: user-selectable, '最長で14日間' on オクル, default 3 days; if unset the operator deletes on its own algorithm. TOP-page anonymous upload is separately capped at 2 GiB. The 300 GiB path requires the オクル flow.
- interface detail: rest
- tooling: Web upload form (オクル) only; no documented public API for the free tier. Member drive has no WebDAV.
- composes with: Account-less uploads so 300 GiB per object x unlimited objects, but each object has a hard expiry, so chaining is a re-upload loop rather than accumulation.
- reliability: Two different caps on the same site (2 GiB from the front page, 300 GiB via オクル) is a real trap for any wrapper: the naive POST silently hits the 2 GiB ceiling. Deleted files are unrecoverable by policy.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '1ファイルの最大アップロードサイズ300GiB(オクル)' on 未登録会員 and 無料会員; 'ストレージ保存 保存容量2GiB' for free members
  - [2] 2026-10-21: '1ファイル最大300GiBまで対応', '最長で14日間アップロード可能です', default 3 days
  - [3] 2026-10-21: 'TOP画面からのアップロードは未登録の方の利用を主としている為、最大アップロードサイズは2GiBに制限'
- sources:
  - [1] https://firestorage.jp/doc/plan
  - [2] https://firestorage.jp/doc/okuru_m1
  - [3] https://firestorage.jp/doc/faq-all
