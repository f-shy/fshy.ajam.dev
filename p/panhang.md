# 盘行

> panhang.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/panhang/ | JSON https://fshy.ajam.dev/api/v1/entity/panhang.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 盘行 (panhang.com)

- `debrid/panhang` | qualifies | evidence documented | binding none | category pan link search engine (aggregator) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23T01:57:23.972Z (live) | stale on 2026-11-23
- url https://www.panhang.com/
- price CNY 0
- free tier: Free, no account: '收录超百万的网盘资源搜索引擎'. Search across 百度网盘, 阿里云盘, 夸克, 迅雷, UC, 蓝奏云 and 115. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Not applicable: it indexes share links, it does not host files. | source: [1]
- retention: Index lifetime is not published; dead share links are the normal state of such an index. | source: [1]
- egress: No traffic of its own: each result is a share link on the pan that holds the file, so the pan's egress terms apply once the link is opened. | metered: no | source: [1]
- identity: anonymous | detail: No account and no login for searching; the page renders results to an anonymous visitor.
- interface: rest
- limits:
  - request-rate: not published [1]
  - volume-quota: none: links only [1]
- binding note: No quota of its own; the pan behind each link is what comes next.
- interface detail: HTTP GET /search?q=... returns an HTML page of share links; no JSON endpoint was found.
- tooling: Browser. Results are pan share links with extraction codes, so a way to open them is still needed (a pan account or a 代下).
- composes with: The discovery half of retrieval: this is where a share link comes from, and every result it returns is subject to the identity wall of the pan behind it.
- reliability: An index of other people's shares, with the usual decay: a search result is not a live file, and the 115 API suspension plus 夸克's share purges shorten link life.
- notes: Free aggregation is the only retrieval layer with no identity cost at all, which is why it is the front door for the rest of this market.
- evidence note: The landing page and its topic links were read. A search was not run, so recall and dead-link rate are unmeasured.
- extras:
  - pans: 百度; 阿里云盘; 夸克; 迅雷; UC; 蓝奏云; 115
- evidence:
  - [1] 2026-10-23: '收录超百万的网盘资源搜索引擎'; description names 百度网盘、阿里云盘、夸克、迅雷、UC、蓝奏云、115; search links at /search?q=
- sources:
  - [1] https://www.panhang.com/
