# ギガワタス

> giga-watasu.jp | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/giga-watasu/ | JSON https://fshy.ajam.dev/api/v1/entity/giga-watasu.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ギガワタス / GigaWatasu (giga-watasu.jp)

- `storage/gigawatasu` | qualifies-with-caveat | evidence reported | binding per-object-cap | category anonymous-dump
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://giga-watasu.jp
- free tier: 333 GB per file, no registration. Registered free members additionally get 111-day retention, send history and a receive folder. All free. No total-storage figure because there is no account-level bucket. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 333 GB per file | bytes: 333000000000 | source: [1] | note: not stated
- retention: Registered free members additionally get 111-day retention, send history and a receive folder. All free. | days: 111 | source: [1] | note: not stated
- egress: No bandwidth meter on the free tier; the paid product is a business plan, not storage or transfer. | metered: no
- identity: anonymous
- interface: rest, rclone
- limits:
  - per-object-cap (binding): 333 GB per file [1]
  - retention-clamped: Retention 3-111 days [1]
- limits note: per-object-cap 333 GB. Retention 3-111 days (free registration unlocks the 111-day end). Optional password, optional download-count cap, optional one-time download.
- interface detail: rest
- tooling: Web form at /upload (drag-and-drop, folder upload, password, download-count limit, one-time download). No API, no rclone backend.
- composes with: Account-less uploads so 333 GB x unlimited objects; retention 3-111 days chosen per drop means the chain is a re-upload cron rather than an accumulating archive.
- reliability: Newer entrant (the operator runs a comparison blog and scores itself #1, which is a caveat on the ranking but not on the numbers). Operator holds a Japanese PrivacyMark. Ad-supported rather than paid-tier-supported, so the free tier is the business model.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '広告最小で最大333GBを登録不要で。会員になれば最大111日保存・送信履歴・受取フォルダまで、ぜんぶ無料'
  - [2] 2026-10-21: 'ドラッグ&ドロップで、最大333GBまで', '最大333GB複数ファイル・フォルダ対応'
  - [3] 2026-09-14: third-party-style comparison by the same operator: '1位 ギガワタス 1ファイル333GB 3〜111日', verified 2026-09-14
- sources:
  - [1] https://giga-watasu.jp/
  - [2] https://giga-watasu.jp/upload
  - [3] https://giga-watasu.jp/blog/15hikaku
