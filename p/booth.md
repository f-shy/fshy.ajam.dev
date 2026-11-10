# BOOTH

> booth.pm | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/booth/ | JSON https://fshy.ajam.dev/api/v1/entity/booth.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## BOOTH (pixiv)

- `storage/booth` | fails-quota | evidence reported | binding per-object-cap | category Japanese doujin digital-goods marketplace
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://booth.pm
- free tier: 1.2 GB per file (raised from 1 GB on 2026-03-09), 10 GB total per shop; storage add-on ¥540/month per extra block. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: 1.2 GB per file | bytes: 1200000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Purchaser download; no public egress figure. | metered: no
- identity: email | detail: email
- interface: unknown
- limits:
  - per-object-cap (binding): 1.2 GB per file [1]
- limits note: per-object-cap 1.2 GB; per-account 10 GB free, expandable paid.
- interface detail: Web; pixiv account.
- tooling: Web only.
- composes with: 10 GB/shop with a paid storage-upgrade path is negligible at the scale, but the ¥540/mo add-on is a rare published per-block price in this niche.
- reliability: 10 GB total free makes it fails-quota against every other filter here; included for completeness and for the storage-upgrade pricing.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1.2 GB per file (raised from 1 GB on 2026-03-09), 10 GB total per shop; storage add-on ¥540/month per extra block.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'BOOTH — 1ファイル1GB以内、1ストア合計10GBまで'
  - [1] 2026-10-21: official title '1ファイルでアップロードできる容量が知りたい'; snippet '1ファイルのアップロードできるデータ容量は1.2GBまでです' (page itself 409'd; snippet route used)
  - [3] 2026-10-21: shop notice '1ファイルあたりの容量上限を1.2GBに引き上げました 2026-03-09'
  - [4] 2026-10-21: 2026-10-05 confirmation: 1.2 GB/file, 10 GB shop total
- sources:
  - [1] https://booth.pixiv.help/hc/ja/articles/230690327
  - [2] https://w.atwiki.jp/vbmaker/pages/24.html
  - [3] https://ciphlex.booth.pm/cart
  - [4] https://www.arukito.com/booth-digital-sales-guide/
