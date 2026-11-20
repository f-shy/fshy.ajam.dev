# DLsite

> dlsite.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dlsite/ | JSON https://fshy.ajam.dev/api/v1/entity/dlsite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DLsite (circle / web upload)

- `storage/dlsite` | qualifies-with-caveat | evidence documented | binding per-object-cap | category Japanese doujin marketplace — GB-scale arbitrary archives
- needs card no, phone no, ID no, institution no | verified 2026-11-10T00:50:14.094Z (live) | stale on 2026-12-11
- url https://www.dlsite.com/circle/circle/webup
- free tier: （1） 作品本体 | 10GBまで。対応形式：zip・rar・7z ※4GB以上は、RARまたは7-zip形式で。 | unit: GB | metered on: unstated | read on: 2026-11-09 | source: [1] | note: ファイル容量が10GBを超えてもお取り扱いは可能です。
- per-object cap: 10GBまで | bytes: 10000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Purchaser-authenticated download; no public egress figure. No CDN hot-link. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - write-gated: Review is write-gated (審査) [1]
  - per-object-cap (binding): 10GBまで [1]
- limits note: per-object-cap 10 GB web / larger on request; formats zip/rar/7z; >4 GB must be RAR or 7z.
- interface detail: Web circle upload; no public write API. viviON ID login.
- tooling: Web only.
- composes with: 10 GB of arbitrary archive per work, with an explicit path above 10 GB, is the largest Japanese-language per-object figure found. Each work is a shard.
- reliability: Circle registration requires a payout bank account and, for paid sales, My Number (individual number) registration. So while the ID itself is email-based, monetisation is national-id gated. Review is write-gated (審査).
- notes: ファイル容量が10GBを超えてもお取り扱いは可能です。
- evidence note: the webup page states the 10 GB per-work cap and the accepted formats
- evidence:
  - [1] 2026-10-21: '作品本体 | 10GBまで。対応形式：zip・rar・7z ※4GB以上は、RARまたは7-zip形式で。'
  - [2] 2026-10-21: 'ファイル容量が10GBを超えてもお取り扱いは可能です。Webからのアップロードは10GBまで対応しており'
  - [3] 2026-10-21: 2026-02-19 raised trial-file upload cap to 10 GB
  - [1] 2026-11-09: the webup page caps a work at 10 GB and lists zip, rar and 7z, with rar or 7z required above 4 GB | capture: sha256:f7b12af2dd4e1a3973d9cbb7490608e9ee4c8b1d1e9f5ded1eba89a97858ddb5 | quote: （1） 作品本体 | 10GBまで。対応形式：zip・rar・7z ※4GB以上は、RARまたは7-zip形式で。
  - [2] 2026-11-09: the help page states works over 10 GB can be handled | capture: sha256:b4a831582db7cf47997e94f5e18f461415e73e445ed6ae5d9a7daa919a882f03 | quote: ファイル容量が10GBを超えてもお取り扱いは可能です。
- sources:
  - [1] https://www.dlsite.com/circle/circle/webup
  - [2] https://cs-circle.dlsite.com/hc/ja/articles/1500003142381
  - [3] https://info.eisys.co.jp/dlsite/6a81fa92b485c613
