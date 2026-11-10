# DLsite

> dlsite.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dlsite/ | JSON https://fshy.ajam.dev/api/v1/entity/dlsite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DLsite (circle / web upload)

- `storage/dlsite` | qualifies-with-caveat | evidence reported | binding per-object-cap | category Japanese doujin marketplace — GB-scale arbitrary archives
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.dlsite.com/circle/circle/webup
- free tier: 作品本体 10GBまで (10 GB per work) via web upload; 'ファイル容量が10GBを超えてもお取り扱いは可能です' (works over 10 GB can still be handled, by arrangement). Accepted formats zip/rar/7z, and files over 4 GB must be RAR or 7-Zip. | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap 10 GB | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Purchaser-authenticated download; no public egress figure. No CDN hot-link. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - write-gated: Review is write-gated (審査) [1]
  - per-object-cap (binding): per-object-cap 10 GB [1]
- limits note: per-object-cap 10 GB web / larger on request; formats zip/rar/7z; >4 GB must be RAR or 7z.
- interface detail: Web circle upload; no public write API. viviON ID login.
- tooling: Web only.
- composes with: 10 GB of arbitrary archive per work, with an explicit path above 10 GB, is the largest Japanese-language per-object figure found. Each work is a shard.
- reliability: Circle registration requires a payout bank account and, for paid sales, My Number (individual number) registration. So while the ID itself is email-based, monetisation is national-id gated. Review is write-gated (審査).
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: '作品本体 | 10GBまで。対応形式：zip・rar・7z ※4GB以上は、RARまたは7-zip形式で。'
  - [2] 2026-10-21: 'ファイル容量が10GBを超えてもお取り扱いは可能です。Webからのアップロードは10GBまで対応しており'
  - [3] 2026-10-21: 2026-02-19 raised trial-file upload cap to 10 GB
- sources:
  - [1] https://www.dlsite.com/circle/circle/webup
  - [2] https://cs-circle.dlsite.com/hc/ja/articles/1500003142381
  - [3] https://info.eisys.co.jp/dlsite/6a81fa92b485c613
