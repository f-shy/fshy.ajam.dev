# 0DayDown

> 0daydown.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/0daydown/ | JSON https://fshy.ajam.dev/api/v1/entity/0daydown.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## 0DayDown

- `debrid/0daydown` | paid-only | evidence documented | binding write-gated | category DDL index, Chinese-language (software, tutorials, ebooks; Baidu Pan links) | tier free
- needs card yes, phone no, ID no, institution no | verified 2026-10-23T01:52:28.000Z (live) | stale on 2026-11-23
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
- reliability: Baidu Pan links die with the uploader's account and are shaped by region; posts share a fixed archive password ('0daydown') which must be applied before the file opens.
- notes: Included because an English-language pass would not surface it: the feed is reachable, the catalogue is software and courses rather than video, and the download path is Baidu Pan, which no English DDL index uses.
- evidence note: Home page, feed headers and one post were read on 2026-10-23. Purchasing a VIP account confirms the payment rail and the real per-link quota.
- extras:
  - language: zh
  - feed_protocol: rss2
  - storage_target: baidu-pan
  - vip_gate: yes
- evidence:
  - [2] 2026-10-23: live Chinese-language DDL index with categories such as tutorials and software, newest post timestamped 11 seconds before the read
  - [1] 2026-10-23: content-type application/rss+xml, so the index has a machine-readable feed
  - [3] 2026-10-23: VIP-only download notice in place of the link, and 'Password/解压密码 0daydown' in the post body
- sources:
  - [1] https://www.0daydown.com/feed/
  - [2] https://www.0daydown.com/
  - [3] https://www.0daydown.com/10/3668985.html
