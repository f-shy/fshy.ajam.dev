# 镜芯 API

> wer.plus | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/wer/ | JSON https://fshy.ajam.dev/api/v1/entity/wer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 镜芯 API (api2.wer.plus)

- `debrid/jingxin-api` | qualifies-with-caveat | evidence documented | binding request-rate | category paid direct-link resolver API | tier pay-per-call
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:56:12.306Z (live) | stale on 2026-11-23
- url https://api2.wer.plus/doc/53
- price CNY 880 per 1,000,000 resolutions; CNY 0.00088 per call
- free tier: 500 calls in total, of which 1000/month and 100/day are sub-allowances: '总免费额度 500 次, 每月免费额度 1000 次 包含在总免费额度, 每日免费额度 100 次'. Free users are throttled to 3 seconds per request. | unit: requests | metered on: request-count | read on: 2026-10-23 | source: [1]
- per-object cap: Not applicable: the resolver returns a URL, it does not store the object. The 123云盘 endpoint notes that large files need the sharing account to hold VIP. | source: [1]
- retention: Not applicable: no bytes are stored by the resolver. | source: [1]
- egress: The API returns a resolved URL; the bytes come from the pan's own CDN. Charges are per call, not per byte: 0.0010 元/次 on balance, 0.00088 元/次 in the largest pack. | metered: no | source: [1]
- identity: email | detail: A console account issues the key. The signup form was not read, so the exact field set is unconfirmed; no phone gate is visible in the docs.
- interface: rest
- limits:
  - request-rate (binding): free 3s/request; paid 10 QPS; 10,000 requests/day per user [1]
  - volume-quota: free allowance 500 calls total [1]
- binding note: Calls, not bytes, bind: 1 TiB of monthly transfer is one call per file, so a large library is cheap and a large single file is free. The free tier's 3s/request is the only wall.
- interface detail: HTTP GET, JSON response, key in the query string: https://api2.wer.plus/api/123pan?key=...&url=...
- endpoint: part of interface detail
- tooling: Any HTTP client. Priced per call, so the cost is knowable before a run; QPS 10 for paying users.
- composes with: The metered alternative to a self-run resolver: 1,000,000 resolutions for ¥880 is a fixed cost that does not depend on how much is downloaded.
- reliability: Coverage is narrow: 123云盘, 蓝奏云, 蓝奏云优享版 and OneDrive are documented. Baidu, Quark, UC, 115 and 迅雷 are absent from the catalogue, which is the mirror image of netdisk-fast-download's paid tier.
- notes: Its catalogue is the map of which Chinese pans still allow a third-party resolver to mint a direct link: 123 and 蓝奏 yes, Baidu/Quark/UC/115 no.
- evidence note: The price table, the free allowance, the rate limits and the endpoint were read off the vendor's own doc page. No key was issued and no call was made.
- extras:
  - packs.100: 0.1
  - packs.1000: 0.98
  - packs.10000: 9.2
  - packs.100000: 90
  - packs.1000000: 880
- evidence:
  - [1] 2026-10-23: '参考价格 0.001元/次'; packs 100次¥0.1 to 1000000次¥880; '免费额度 500'; '每日限制 10000次'; '请求频率限制 1秒10次'; endpoint https://api2.wer.plus/api/123pan
  - [2] 2026-10-23: 蓝奏云直链解析 on the same platform, 免费额度 1000, '直链有效期较短，记得及时使用'
- sources:
  - [1] https://api2.wer.plus/doc/53
  - [2] https://api2.wer.plus/doc/19
