# HostSlate

> hostslate.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostslate/ | JSON https://fshy.ajam.dev/api/v1/entity/hostslate.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostSlate

- `compute/hostslate` | qualifies-with-caveat | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:45.576Z (live) | stale on 2026-12-05
- url https://www.hostslate.com/
- free tier: A newly launched Chinese-language merchant that issues free NAT VPS instances to new registrants, one in Japan and one in the United States, with renewal driven by coupons announced in its Telegram group rather than by a published free plan. A community user reports the pair as 有一台日本一台美国的，后续应该是免费续费的, quoted. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-renewable
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: The registration page asks for a username, an email address and a password, and offers GitHub sign-in as an alternative, quoted from the form headings , , and the button GitHub. Real-name KYC is not required of every user but may be demanded on a risk trigger, naming and a selfie among the documents it can ask for.
- interface: ssh
- limits:
  - write-gated (binding): The free term is only as long as the next coupon, and the coupons are distributed in a Telegram group, so the machine survives by following an announcement channel. The terms add that no data is guaranteed after expiry and that no refund is given for any reason, so an unrenewed box loses its data silently. [1]
- limits note: The free term is only as long as the next coupon, and the coupons are distributed in a Telegram group, so the machine survives by following an announcement channel. The terms add that no data is guaranteed after expiry and that no refund is given for any reason, so an unrenewed box loses its data silently.
- binding note: the same as limits note
- interface detail: web console with an in-browser SSH terminal; the home page names no CLI, SDK or API
- tooling: the web console's in-browser SSH terminal; the home page read names no CLI, SDK or API library
- composes with: A free NAT instance in Tokyo plus a free DNS-fronted tunnel is a complete always-on origin for a scraper at zero cost; the NAT port mapping is what limits inbound services.
- reliability: no reliability event recorded
- notes: HostSlate provides VPS hosting services.
- extras:
  - facets.class: perpetual-vps
  - facets.free_tier_kind: perpetual-renewable
- evidence:
  - [2] 2026-10-22: the signup form asks for 用户名, 邮箱, 密码 and offers GitHub sign-in, quoted from the crawled page
  - [3] 2026-10-22: terms state HostSlate 为在英国注册并运营的服务器及云基础设施服务品牌 (a brand registered and operated in the United Kingdom), quoted
  - [3] 2026-10-22: terms state 原则上不提供退款 (no refund in principle) and 服务到期后，HostSlate 不保证服务器数据仍然保留 (no guarantee that data survives expiry), quoted
  - [4] 2026-10-22: a user states 注册完官方push给你 有一台日本一台美国的，后续应该是免费续费的, quoted from the snippet
  - [5] 2026-10-22: the merchant posts a coupon code for free NAT machines and points to its Telegram group for stock announcements
  - [6] 2026-10-22: three machines in sg, jp and us were given away as free instances, and the giver states renewal coupons are handed out in the group
  - [1] 2026-11-03: the management console offers an in-browser SSH terminal (browser console; no REST API or CLI is described on the page) | capture: sha256:804bed8c4be37eb3aeed9e0afc908f4e0ad9f49b115e96cbf53ca0ffb8c175fe | quote: 浏览器内 SSH 终端，无需额外工具
  - [7] 2026-11-04: the console offers an in-browser SSH terminal | capture: sha256:5640d8a5075ffcc8d3014d7c468d455c95ecc460eea44f4690736f56f21c4406 | quote: 浏览器内 SSH 终端，无需额外工具
  - [7] 2026-11-04: the documented client is the browser terminal, no installed client named | capture: sha256:5640d8a5075ffcc8d3014d7c468d455c95ecc460eea44f4690736f56f21c4406 | quote: 浏览器内 SSH 终端，无需额外工具
- sources:
  - [1] https://www.hostslate.com/
  - [2] https://hostslate.com/register
  - [3] https://hostslate.com/legal/tos
  - [4] https://www.nodeseek.com/post-971532-1
  - [5] https://www.nodeseek.com/post-943001-1
  - [6] https://www.nodeseek.com/post-972539-1
  - [7] https://hostslate.com/
