# DLsite

> dlsite.com | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dlsite/ | JSON https://fshy.ajam.dev/api/v1/entity/dlsite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DLsite (circle / web upload)

- `storage/dlsite` | qualifies-with-caveat | evidence documented | binding per-object-cap | category Japanese doujin marketplace — GB-scale arbitrary archives
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:54:53.002Z (live) | stale on 2026-12-26
- url https://www.dlsite.com/circle/circle/webup
- free tier: （1） 作品本体 | 10GBまで。対応形式：zip・rar・7z ※4GB以上は、RARまたは7-zip形式で。 | unit: GB | metered on: unstated | read on: 2026-11-09 | source: [1] | note: ファイル容量が10GBを超えてもお取り扱いは可能です。
- per-object cap: 10GBまで | bytes: 10000000000 | source: [1] | note: Web upload is capped at 10 GB per work; works above 10 GB can be handled and files of 40 GB or more are split for sale.
- retention: source: [1] | note: No fixed retention period is stated; purchased works can be downloaded repeatedly.
- egress: Purchaser-authenticated downloads from the product page, purchase history, DLsite Play and DLsiteNEST; no egress figure is published. | metered: no
- identity: email | detail: email
- interface: browser
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
  - [1] 2026-11-25: the circle upload page documents uploading the work file through the website | capture: sha256:f7b12af2dd4e1a3973d9cbb7490608e9ee4c8b1d1e9f5ded1eba89a97858ddb5 | quote: 作品本体・（体験版）・各種画像をアップロード
  - [2] 2026-11-25: the circle help article states a 10 GB web-upload limit, handling above 10 GB and splitting at 40 GB | capture: sha256:b4a831582db7cf47997e94f5e18f461415e73e445ed6ae5d9a7daa919a882f03 | quote: Webからのアップロードは10GBまで対応しております。 ... ファイル容量が10GBを超えてもお取り扱いは可能です。 ... ただし、40GB以上のファイルは販売時のファイルを分割ファイルとさせていただきます。
  - [4] 2026-11-25: the download help page states purchased products can be downloaded repeatedly and gives no retention period | capture: sha256:683d3bdb07816b554392b71b052f2c3dee8f2c004d562ad5e0b28b35a2c337c3 | quote: DLsite allows you to download your purchased products as many times as you like.
  - [4] 2026-11-25: the download help page states four purchaser download routes, a login gate and no egress figure | capture: sha256:683d3bdb07816b554392b71b052f2c3dee8f2c004d562ad5e0b28b35a2c337c3 | quote: You can download purchased titles not only from the product page, but also from your purchase history, DLsite Play (browser streaming), and DLsiteNEST (DLsite's dedicated application). ... ※If you do not see "Account", you are not logged in.
  - [5] 2026-11-25: a notice states that works whose sale ended can still be downloaded without a fixed expiry, with exceptions | capture: sha256:1622308d2f32d6b16d723fb22017416b3af48d02cac8a1acb7d9858707cc235a | quote: 販売終了した作品も、無期限でダウンロード！
  - [1] 2026-11-25: the circle upload page caps a work at 10 GB and lists zip, rar and 7z with rar or 7z above 4 GB | capture: sha256:f7b12af2dd4e1a3973d9cbb7490608e9ee4c8b1d1e9f5ded1eba89a97858ddb5 | quote: （1） 作品本体 | 10GBまで。対応形式：zip・rar・7z ※4GB以上は、RARまたは7-zip形式で。
- sources:
  - [1] https://www.dlsite.com/circle/circle/webup
  - [2] https://cs-circle.dlsite.com/hc/ja/articles/1500003142381
  - [3] https://info.eisys.co.jp/dlsite/6a81fa92b485c613
  - [4] https://cs.dlsite.com/hc/en-us/articles/10077048450713-Downloading-and-Extracting
  - [5] https://info.eisys.co.jp/dlsite/91939aacb2194f18?locale=default
