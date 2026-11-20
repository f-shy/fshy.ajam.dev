# 夸搜搜

> kuasoso.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kuasoso/ | JSON https://fshy.ajam.dev/api/v1/entity/kuasoso.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 夸搜搜 (kuasoso.com)

- `debrid/kuasoso` | qualifies | evidence documented | binding none | category pan link search engine (aggregator) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:57:23.974Z (live) | stale on 2026-11-23
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
- sources:
  - [1] https://www.kuasoso.com/
