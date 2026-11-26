# 夸搜搜

> kuasoso.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kuasoso/ | JSON https://fshy.ajam.dev/api/v1/entity/kuasoso.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 夸搜搜 (kuasoso.com)

- `debrid/kuasoso` | qualifies | evidence documented | binding none | category pan link search engine (aggregator) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-25T09:46:56.526Z (live) | stale on 2026-12-26
- url https://www.kuasoso.com/
- price CNY 0
- free tier: 'kuasoso.com网盘资源无偿分享' - free, no account. The landing page lists the newest indexed shares per pan, tagged 夸克网盘 / 迅雷云盘 / 百度网盘. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Not applicable: links, not files. | source: [1]
- retention: Index lifetime not published; the '最新入库' list is the only freshness signal. | source: [1]
- egress: No traffic of its own; the pan behind each link holds the bytes and its terms apply. | metered: no | source: [1]
- identity: anonymous | detail: No login for reading the index.
- interface: rest
- limits:
  - request-rate: not published [1]
  - volume-quota: none: links only [1]
- binding note: No quota of its own.
- interface detail: HTTP GET on /doc/<id> per share and a search endpoint; HTML only.
- tooling: Browser.
- composes with: Same role as 盘行: a source of share links whose value depends entirely on whether the pan behind them can be opened.
- reliability: The 最新入库 list shows 夸克 and 迅雷 dominating and 百度 present, which is the current share-host mix in one picture.
- notes: Included because the index composition is itself a finding: 夸克 and 迅雷 shares outnumber 百度 in the newest rows, which matches 夸克 displacing 百度 as the default share host.
- evidence note: Landing page read. No search run.
- evidence:
  - [1] 2026-10-23: 'kuasoso.com网盘资源无偿分享，坚持做最好网盘搜索'; 最新入库 rows tagged [夸克网盘], [迅雷云盘], [百度网盘] with /doc/<id> links
  - [1] 2026-11-25: the index still describes itself as free share search with no account | capture: sha256:652338a4756f85bbd790677212a8eabc03b88f27b0c81eb1ceec905e49467bb1 | quote: kuasoso.com网盘资源无偿分享，坚持做最好网盘搜索
  - [1] 2026-11-25: the newest index rows are still tagged 夸克网盘 | capture: sha256:652338a4756f85bbd790677212a8eabc03b88f27b0c81eb1ceec905e49467bb1 | quote: - [[夸克网盘]《堕落春夜[gb]》作者：却蓝(1).txt](https://www.kuasoso.com/doc/cmwvowa8laqr5r18mue3jnn1u)
  - [2] 2026-11-25: a indexed share's detail page reports a validity check and a link to the pan | capture: sha256:5fc3e209ea91a2d99b5379d5a088570fcd3af6a42c166ec07fcfaf9206c43566 | quote: | 状态检测 | 有效 |
- sources:
  - [1] https://www.kuasoso.com/
  - [2] https://www.kuasoso.com/doc/cmwvowa8laqr5r18mue3jnn1u
