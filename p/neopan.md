# NeoPan

> neopan.cn | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neopan/ | JSON https://fshy.ajam.dev/api/v1/entity/neopan.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NeoPan (app.neopan.cn)

- `debrid/neopan` | self-hosted, last resort | verdict qualifies-with-caveat | evidence documented | binding write-gated | category batch transfer / share tool for Chinese pans | tier VIP1
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:56:12.309Z (live) | stale on 2026-11-23
- url https://app.neopan.cn/pricing
- price CNY 25/month; CNY 360 lifetime | parsed USD 3.75/mo
- free tier: No free tier of the batch features is priced on the page; the three paid tiers are ¥25/月, ¥30/月 and ¥360 永久. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: Not applicable: it drives the pan's own transfer, so the pan's cap applies. | source: [1]
- retention: Not applicable: nothing is stored by the tool. | source: [1]
- egress: No traffic of its own: transfers happen between the pan and the destination account, and downloads consume the pan's own quota. | metered: no | source: [1]
- identity: card | detail: Licence bought by 支付宝 QR; the account is local to the app. The gate is payment plus a pan account, which is the +86 wall.
- interface: cli
- limits:
  - write-gated (binding): batch 转存 needs the pan account's cookie, pasted into the app [1]
  - request-rate: not published; the pan's own rate limit applies [1]
- binding note: Nothing in this tool meters bytes; what gates it is the pan cookie it must hold, so the pan's identity wall is inherited and named here.
- interface detail: Windows and macOS desktop application. Credentials are stored encrypted locally; there is no server-side API.
- tooling: Desktop app for 夸克, 百度 and 迅雷: 批量转存, 批量重命名, 批量分享, 链接转换, 自动同步.
- composes with: The automation layer for 代下 at scale: when the route is 'save the share, then retrieve', this is the tool that turns a thousand share links into a thousand saved files.
- reliability: It stores pan cookies locally, so a pan that rotates its endpoints breaks the tool until it is updated - the same fragility as every cookie-driven client.
- notes: Priced per month for a batch tool, which only pays off when many shares are moved. For a single 1 TiB pull it is pure overhead.
- evidence note: All three prices and the feature matrix were read off the vendor page. No transfer was run.
- self hosted: yes
- extras:
  - pans: 夸克; 百度; 迅雷
- evidence:
  - [1] 2026-10-23: VIP1 ¥25/月, VIP2 ¥30/月, 专业版永久 ¥360; '夸克 / 百度 / 迅雷三大网盘'; 批量转存/重命名/分享/链接转换/自动同步; 支付宝付款
- sources:
  - [1] https://app.neopan.cn/pricing
