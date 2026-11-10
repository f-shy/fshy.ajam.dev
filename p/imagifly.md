# Dreamify AI

> imagifly.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/imagifly/ | JSON https://fshy.ajam.dev/api/v1/entity/imagifly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dreamify AI (Dreamifly, now Imagifly)

- `compute/dreamify-ai` | qualifies-with-caveat | evidence documented | binding volume-quota | category inference API for image and video generation; no rentable GPU time
- needs card no, phone no, ID no, institution no | verified 2026-11-06T16:58:46.847Z (live) | stale on 2026-12-07
- url https://imagifly.net/en/pricing
- free tier: 10 credits on each day the account visits, no card: 'Get 10 credits on each day you visit while signed in', and 'Try AI image and video generation with no credit card required.' The free plan runs the standard queue at 2 concurrent tasks and keeps images and videos for 2 days. The page prices 1,200 credits as 'Approx. 400 images with GPT-Image-2.6', which is 3 credits an image, so 10 credits is about three images of that model. | unit: credits | metered on: request-count | read on: 2026-11-06 | source: [1] | note: the daily grant is a check-in: the CLI's 'imagifly checkin' claims it and image or video generate does it first
- per-object cap: not applicable: the unit is a generation, not a stored object; the API accepts one image per request ('One image per request: imageCount is always 1') and returns a temporary delivery URL | source: [2] | note: no per-file size is published; the largest single output is one image or one short video
- retention: the free plan keeps images and videos for 2 days ('图片和视频保留 2 天'), against 5 days on Plus and Pro and 15 days on Max; the API docs say to treat the output URLs 'as temporary delivery links rather than permanent storage' | days: 2 | source: [3] | note: the clock is the plan's library retention, not a deletion on inactivity
- egress: not published: the output arrives as a URL on imagedelivery.net and no download quota, egress allowance or price per TB is stated on the pages read | metered: no | source: [2]
- identity: email | detail: the daily 10 credits are granted 'while signed in' and an API key is created in the console after signing in ('Open the API console, sign in, and click Create'); the pages state 'no credit card required'; no sign-up form is published and the sign-in dialog is rendered client-side, so an email address is the default assumption rather than a read value, and whether the generator accepts an anonymous request is not stated
- interface: rest, cli
- limits:
  - volume-quota (binding): 10 credits a day on the free plan, granted on each day the account visits ('10 credits on each day you visit'); the pricing page prices 1,200 credits as 'Approx. 400 images with GPT-Image-2.6', which is 3 credits an image, so the daily grant is about three images of that model [1]
  - retention-clamped: the free plan keeps images and videos for 2 days ('图片和视频保留 2 天'), against 5 days on Plus and Pro and 15 days on Max [3]
- limits note: the free plan's standard queue runs 2 concurrent tasks ('标准队列（2 个并行任务）') and a request above the plan's concurrency returns 429 CONCURRENCY_LIMIT; a request that the balance cannot cover is rejected with 402 before any work starts
- binding note: 10 credits a day is about three GPT-Image-2.6 images, so the allowance is spent before any concurrency or rate limit binds, and the 2-day retention then discards the output
- interface detail: a documented JSON API at https://imagifly.net/api/v1 authenticated with 'Authorization: Bearer imf_...' or 'x-api-key', an MCP server, and the npm CLI @imagifly/cli; the web app needs no client
- endpoint: part of interface detail
- tooling: a documented REST API, an MCP server and the npm CLI @imagifly/cli; the site itself is an open-source Next.js front end over ComfyUI API endpoints (LastLighter/Dreamifly) that a user could run on a rented or free machine, listed last because the hosted service above needs no machine
- composes with: composes as an image and video generator behind a polling loop: a submit returns 202 with a task id and there is 'no webhook, callback or push channel', so the caller polls every 2-5 seconds; the free 10 credits a day is about three GPT-Image-2.6 images, so it cannot carry a batch
- reliability: the Dreamifly-era page warned that generation may take a long time and that an occasional failed image is normal ('图片生成可能耗时较长，偶尔一张图片出错是正常情况'); the API returns the credits of a failed task automatically and does not refund a successful one
- notes: The compute is the vendor's, not the user's: the user buys generations and never gets a machine or a GPU-hour. The name Dreamify AI is the free-compute directory free.waxianzhi.com's label for the site at dreamify.slmnb.cn, which branded as Dreamifly and said its images ran on the idle RTX 4090 cards of 30 home computers, free and unlimited (archived 2025-11-01). On 2026-11-06 dreamify.slmnb.cn/zh answered HTTP 404 and dreamifly.com answered 301 to imagifly.net, whose project homepage is imagifly.net, and the Dreamifly project's own homepage field is imagifly.net, so the current site is the successor brand of the Dreamifly site; it grants 10 credits a day rather than an unlimited pool and no longer says which GPUs serve the models. Not established: whether an account can be created without an email address, whether an anonymous generation is accepted, and whether the 4090 pool still serves any model.
- evidence note: every field rests on a first-party page captured on 2026-11-06, with the 2025 distributed-4090 claim on an archived copy of the same site; the identity kind and the credit-to-image rate are the weakest, so one sign-up and one generation would move the record to measured
- extras:
  - lineage.name_in_directory: Dreamify AI 绘画公益站
  - lineage.directory_url: https://free.waxianzhi.com
  - lineage.directory_listing: https://web.archive.org/web/20251011073146/https://free.waxianzhi.com/tools.json
  - lineage.lead_url: https://dreamify.slmnb.cn/zh
  - lineage.lead_url_status: HTTP 404 on 2026-11-06
  - lineage.dreamifly_claim_2025_11_01: 由全国30台家用电脑的闲置4090显卡，免费无限制提供分布式算力支持。
  - lineage.current_paid_plans: Plus USD 9.90 for 1,200 credits, Pro USD 49.90 for 6,000, Max USD 150 for 19,500; credit packs 990 for USD 9.90 and 4,990 for USD 49.90
  - lineage.models_sold: Nano Banana 2, GPT-Image-2.6, Grok Image 2.0, Qwen Image Edit, Z-Image Turbo, Wai SDXL, Seedance 2.0/2.5, MiniMax H3, Wan 2.2 I2V Lightning
- evidence:
  - [1] 2026-11-06: the free plan's allowance is 10 credits granted on each day the account visits | capture: sha256:7844b3a7e5fb08a19a0d809d559953c95f667c81f1d81b5736cb07edc570dcec | quote: 10 credits on each day you visit
  - [1] 2026-11-06: 1,200 credits buys about 400 GPT-Image-2.6 images, which is 3 credits an image and about three images for the daily 10 | capture: sha256:7844b3a7e5fb08a19a0d809d559953c95f667c81f1d81b5736cb07edc570dcec | quote: Approx. 400 images with GPT-Image-2.6
  - [1] 2026-11-06: the Plus plan is 1,200 credits as a one-time payment, not a renewal | capture: sha256:7844b3a7e5fb08a19a0d809d559953c95f667c81f1d81b5736cb07edc570dcec | quote: 1,200Includes 200 bonus credits
  - [1] 2026-11-06: no card is required to start, so the identity gate is not a payment instrument | capture: sha256:7844b3a7e5fb08a19a0d809d559953c95f667c81f1d81b5736cb07edc570dcec | quote: Try AI image and video generation with no credit card required.
  - [3] 2026-11-06: the free plan's standard queue runs 2 concurrent tasks | capture: sha256:f192659b37f74ad11e882e37233acf099367c8b278dfeea69ab41bf900ff34f7 | quote: 标准队列（2 个并行任务）
  - [3] 2026-11-06: the free plan keeps images and videos for 2 days | capture: sha256:f192659b37f74ad11e882e37233acf099367c8b278dfeea69ab41bf900ff34f7 | quote: 图片和视频保留 2 天
  - [2] 2026-11-06: an API key is created only after signing in, so the API path costs an account | capture: sha256:23cb584ceed9e03b0c00714862599142654d190e041a94c392bda97a3c892f06 | quote: Open the API console, sign in, and click Create.
  - [2] 2026-11-06: generation is paid from a credit balance, and an empty balance stops the request before any work | capture: sha256:23cb584ceed9e03b0c00714862599142654d190e041a94c392bda97a3c892f06 | quote: A request that cannot be covered by the account balance is rejected with 402 before any work starts.
  - [2] 2026-11-06: a failed task is refunded and a successful one is not | capture: sha256:23cb584ceed9e03b0c00714862599142654d190e041a94c392bda97a3c892f06 | quote: the credits are returned automatically; successful tasks are not refunded
  - [2] 2026-11-06: a caller must poll the task id, which shapes how the service chains into a pipeline | capture: sha256:23cb584ceed9e03b0c00714862599142654d190e041a94c392bda97a3c892f06 | quote: There is no webhook, callback or push channel.
  - [2] 2026-11-06: one request yields one image, so there is no batch unit to amortise the credit cost | capture: sha256:23cb584ceed9e03b0c00714862599142654d190e041a94c392bda97a3c892f06 | quote: One image per request: `imageCount` is always `1`.
  - [4] 2026-11-06: the 2025-11-01 copy of the site said its compute was the idle RTX 4090 cards of 30 home computers, offered free and unlimited as distributed compute | capture: sha256:c19a220b5b468c0937ecfea48ec849dd54bd45f21d854db7da1be436e5227580 | quote: 由全国30台家用电脑的闲置4090显卡，...免费无限制...提供分布式算力支持
  - [4] 2026-11-06: the 2025-11-01 copy listed no login as a feature, against the current site's signed-in daily credits | capture: sha256:c19a220b5b468c0937ecfea48ec849dd54bd45f21d854db7da1be436e5227580 | quote: 无需登录
  - [4] 2026-11-06: the site warns that generation may be slow and that an occasional failed image is normal | capture: sha256:c19a220b5b468c0937ecfea48ec849dd54bd45f21d854db7da1be436e5227580 | quote: 图片生成可能耗时较长，偶尔一张图片出错是正常情况
  - probe:dreamify.slmnb.cn/zh 2026-11-06: the lead URL answers HTTP 404 on 2026-11-06, so the site the directory listed is gone at that address | capture: sha256:04fac09e59e2075569e7cd68824508c5b50049b7a2173bd07d6ea078c962d3fc | quote: "status": 404
  - [5] 2026-11-06: the Dreamifly project's own homepage field is imagifly.net, which ties the Dreamifly site to the current Imagifly site | capture: sha256:284e1c8da0fc5888e5d7d17243a124e64f4575bd5e658a208b64bed7d6ee5962 | quote: "homepage": "https://imagifly.net/"
  - [6] 2026-11-06: the name Dreamify AI is the free-compute directory's label for this site, at https://dreamify.slmnb.cn/zh | capture: sha256:3e1d58d10884cab6fc3fd0b54a82ad7a270d0ecb5e148774823d6a3b07cc84d1 | quote: Dreamify AI 绘画公益站
  - [6] 2026-11-06: the directory listed the offer as entirely free, which the current site's 10 credits a day no longer is | capture: sha256:3e1d58d10884cab6fc3fd0b54a82ad7a270d0ecb5e148774823d6a3b07cc84d1 | quote: 完全免费
- sources:
  - [1] https://imagifly.net/en/pricing
  - [2] https://imagifly.net/docs/api
  - [3] https://imagifly.net/zh/pricing
  - [4] https://web.archive.org/web/20251101135321/https://dreamifly.com/zh
  - [5] https://api.github.com/repos/LastLighter/Dreamifly
  - [6] https://web.archive.org/web/20251011073146/https://free.waxianzhi.com/tools.json?_t=1760167906363
