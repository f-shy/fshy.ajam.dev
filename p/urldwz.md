# 轻麦云直链

> urldwz.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/urldwz/ | JSON https://fshy.ajam.dev/api/v1/entity/urldwz.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 轻麦云直链 (urldwz.com)

- `debrid/qingmai-cloud` | qualifies-with-caveat | evidence reported | binding volume-quota | category direct-link host with unlimited traffic | tier free
- needs card no, phone yes, ID no, institution no | verified 2026-11-25T09:46:37.626Z (live) | stale on 2026-12-10
- url http://www.urldwz.com/
- price CNY 0 for 10 GB; CNY 20 per 10 GB/month paid | parsed USD 299.84/TB-mo
- free tier: '注册即送10G永久空间，不限流量，更不限速' - 10 GB permanent, traffic and speed unlimited on the free tier. | unit: GB | metered on: stored-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: The free plan publishes a 500 MB maximum single-file upload. | bytes: 500 | source: [1]
- retention: Permanent for the free 10 GB ('永久空间'). | source: [1]
- egress: '不限流量' and '不限下载次数' on both free and paid, served from domestic nodes behind a CDN. The seller's claim is that neither tier is shaped. | metered: no | source: [1]
- identity: any-phone | detail: Registration is required for the free 10 GB; the form was not read. The vendor's contact channel is a Chinese 网络工作室, so a mainland phone is likely but unverified.
- interface: rest
- limits:
  - volume-quota (binding): free 10 GB storage; paid 20 元 per 10 GB per month, expansion 3 元/GB/month [1]
  - per-object-cap: 500 MB maximum single-file upload on Free [1]
- binding note: 10 GB is the whole free tier, so stored bytes bind long before traffic does. The paid expansion at 3 元/GB/month is the most expensive storage measured among debrid providers.
- interface detail: Files are served from a direct URL with no session, which is the product: a link that hot-links, embeds or feeds a player.
- tooling: Browser plus any HTTP client; the direct URL is the interface.
- composes with: A 10 GB unmetered direct-link shelf for the small files a client needs to hand to a player or a page, not a store for a library.
- reliability: A one-person studio, not a company: '青白江轻麦网络工作室'. Durability is the risk, not speed.
- notes: Included because published records has no record of a Chinese host that sells unmetered egress as the headline. At 3 元/GB/month for expansion it is 30x 115's 8-year price per TB.
- evidence note: The free allowance, the no-limit claims and the price ladder are quoted from the vendor page as returned by the reader. No upload or download was run.
- extras:
  - expansion_cny_gb_month: 3
- evidence:
  - [1] 2026-10-23: '现在注册即送10G永久空间，不限流量，更不限速'; '不管是免费用户还是付费用户，都不限速'; video host '20元/10G/月', 扩容 '3元/G/月'
  - [1] 2026-11-25: registration gives 10 GB permanent space with unmetered traffic and speed | capture: sha256:0a9b17639d25621b58309c37a7021ab12f92bbf9fdf3a0a08447b73d421f0995 | quote: 现在注册即送10G永久空间，不限流量，更不限速
  - [1] 2026-11-25: neither free nor paid users are speed-limited | capture: sha256:0a9b17639d25621b58309c37a7021ab12f92bbf9fdf3a0a08447b73d421f0995 | quote: 不管是免费用户还是付费用户，都不限速
  - [1] 2026-11-25: video hosting is 20 yuan per 10 GB per month, expansion 3 yuan per GB per month | capture: sha256:0a9b17639d25621b58309c37a7021ab12f92bbf9fdf3a0a08447b73d421f0995 | quote: 20元/10G/月，（扩容价格：3元/G/月）
  - [1] 2026-11-25: the free plan publishes a 500 MB maximum single-file upload | capture: sha256:0a9b17639d25621b58309c37a7021ab12f92bbf9fdf3a0a08447b73d421f0995 | quote: 单文件最大上传500M
- sources:
  - [1] http://www.urldwz.com/
