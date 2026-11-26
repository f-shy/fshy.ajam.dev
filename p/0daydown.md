# 0DayDown

> 0daydown.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/0daydown/ | JSON https://fshy.ajam.dev/api/v1/entity/0daydown.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 0DayDown

- `debrid/0daydown` | dead | evidence documented | binding write-gated | category DDL index, Chinese-language (software, tutorials, ebooks; Baidu Pan links) | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-11-25T19:21:26.872Z (live) | stale on 2026-12-26
- url https://www.0daydown.com/
- price USD 0
- free tier: The index is free to read and its RSS feed answers with application/rss+xml. The download is not free: a post prints a notice that the resource is VIP-only and asks the reader to log in first. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: The Chinese notice in the post read is 抱歉，此资源仅限VIP下载，请先登录.
- per-object cap: not applicable: an index | source: [2]
- retention: Posts persist and the feed carries the latest items; the Pan link behind a post dies with the uploader's quota. | source: [2]
- egress: No byte allowance from the index; downloads are served by Baidu Pan (pan.baidu.com) behind the post's VIP link. | metered: no | free allowance: none | source: [3]
- identity: card | detail: An account plus a VIP purchase stands between a caller and the link. The registration form was not opened, so the payment rail is unverified. | country: CN
- interface: rest
- limits:
  - write-gated (binding): every download link in the post read was replaced by the VIP notice, and the archive password is the fixed string '0daydown' [3]
- limits note: The index itself answered without an account; only the link is gated. The 794-word home page and the feed are fully readable.
- binding note: Nothing is metered in bytes on the index; the first thing that stops a caller is the paid VIP gate on the link itself.
- interface detail: WordPress RSS at /feed/ (application/rss+xml) plus an HTML category tree; wp-login.php is the door the VIP notice points at. No JSON API found.
- endpoint: https://www.0daydown.com/feed/
- tooling: An RSS reader reads the index. The links are Baidu Pan URLs, which need a Pan account and a client that speaks Baidu's protocol; a plain HTTP GET does not.
- composes with: Feed to post to VIP link to Baidu Pan. Complements the English DDL feeds because the software catalogue and the Chinese-language tutorials do not overlap with them.
- reliability: unverified: the site's pages no longer answer: https://www.0daydown.com/ and https://www.0daydown.com/feed/ each returned HTTP 200 with a 114-byte HTML body that only redirects to /lander on 2026-11-25. Routes tried: reader, two provider pins, fetch, archive, three HTTP probes and a TCP connect probe.
- notes: Included because an English-language pass would not surface it: the feed is reachable, the catalogue is software and courses rather than video, and the download path is Baidu Pan, which no English DDL index uses.
- evidence note: Home page, feed headers and one post were read on 2026-10-23. Purchasing a VIP account confirms the payment rail and the real per-link quota.
- extras:
  - language: zh
  - feed_protocol: rss2
  - storage_target: baidu-pan
  - vip_gate: yes
  - death.on: 2026-11-25
  - death.cause: dead-service
- evidence:
  - [2] 2026-10-23: live Chinese-language DDL index with categories such as tutorials and software, newest post timestamped 11 seconds before the read
  - [1] 2026-10-23: content-type application/rss+xml, so the index has a machine-readable feed
  - [3] 2026-10-23: VIP-only download notice in place of the link, and 'Password/解压密码 0daydown' in the post body
  - probe:https://www.0daydown.com/ 2026-11-25: the probe recorded the status of the response from the site's home page | capture: sha256:e6af07d617eac52e3a4ca971957675a0a40aabc60d8314f512629cf3e8975985 | quote: "status": 200,
  - probe:https://www.0daydown.com/ 2026-11-25: the body of the 200 response is only a redirect to a lander, not the index | capture: sha256:6dc9c7fc93bb488bb0520a6c780a8d3c0fb5486a4711aca49b4c53fac7393023 | quote: window.location.href="/lander"
  - probe:https://www.0daydown.com/feed/ 2026-11-25: the feed probe also recorded a 200 with a 114-byte redirect-only body | capture: sha256:0255a45ed12b6fc11310407f7aa4605f3f91c3d005c8f8ebb2ab6317c45c6153 | quote: "status": 200,
  - [2] 2026-11-25: a provider read of the domain shows a GoDaddy parked-domain page, so the index is gone | capture: sha256:c3600a3ac3289ae5a61c0246c2b4019ed6b41c47ec28b7c89678ed6f46c58303 | quote: is parked free, courtesy of GoDaddy.com.
  - [4] 2026-11-25: a third-party user report says the site is down | capture: sha256:793fa7692559103d1d42f18dad7078fe37cee13c7479376a55d7a279565926cc | quote: 已经挂了
  - [2] 2026-11-25: the domain is parked, so the index no longer exists | capture: sha256:c3600a3ac3289ae5a61c0246c2b4019ed6b41c47ec28b7c89678ed6f46c58303 | quote: is parked free, courtesy of GoDaddy.com.
  - probe:https://www.0daydown.com/ 2026-11-25: the probe record targets the home page named by the record | capture: sha256:e6af07d617eac52e3a4ca971957675a0a40aabc60d8314f512629cf3e8975985 | quote: "url": "https://www.0daydown.com/",
- sources:
  - [1] https://www.0daydown.com/feed/
  - [2] https://www.0daydown.com/
  - [3] https://www.0daydown.com/10/3668985.html
  - [4] https://www.v2ex.com/t/1254635
