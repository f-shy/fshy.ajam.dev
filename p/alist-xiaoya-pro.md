# alist.xiaoya.pro

> Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/alist-xiaoya-pro/ | JSON https://fshy.ajam.dev/api/v1/entity/alist-xiaoya-pro.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## alist.xiaoya.pro — 小雅 (xiaoya) public instance, the most famous chinese-pan

- `storage/alist-xiaoya-pro-public-instance-the-most-famous-chinese` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:46.271Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/alist-xiaoya-pro.md
- free tier: none reachable: DEAD. The canonical xiaoya host returns HTTP 302 from nginx and then a Cloudflare 504 on every path, including /api/public/settings. Xiaoya is the single largest AList deployment in China… | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the first-party host redirects to a consumer portal and states no per-object cap | note: not applicable
- retention: stated-absent: the first-party host redirects to a consumer portal and states no retention period
- egress: stated-absent: the first-party host redirects to a consumer portal and states no egress terms | metered: no
- identity: email
- interface: unknown
- interface detail: stated-absent: the first-party host redirects with HTTP 302 to a consumer portal and exposes no storage API interface
- tooling: not documented
- composes with: stated-absent: the first-party host redirects to a consumer portal and states no way to chain byte storage with other services
- reliability: Dead: the canonical AList host still redirects to an unrelated third-party site, so no public AList instance is served. A probe today followed the redirect off-host; the /api/public/settings path redirects the same way.
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: DEAD. The canonical xiaoya host returns HTTP 302 from nginx and then a Cloudflare 504 on every path, including /api/public/settings. Xiaoya is the single largest AList deployment in China…
  - dead_end.first_recorded: 2026-10-21
  - death.on: 2026-11-19
  - death.cause: dead-service
- evidence:
  - withheld 2026-10-21: DEAD. The canonical xiaoya host returns HTTP 302 from nginx and then a Cloudflare 504 on every path, including /api/public/settings. Xiaoya is the single largest AList deployment in China m
  - probe:https://alist.xiaoya.pro/ 2026-11-19: a probe of the canonical host still returns a page that redirects away from the AList instance | capture: sha256:5b7c03d3069790fa79b98ee57c800949570d61d51998c7564794954e22ca84c1 | quote: "status": 200
  - probe:https://alist.xiaoya.pro 2026-11-19: the host redirects to a consumer portal rather than serving a storage API, so no interface is exposed | capture: sha256:4a599e56cdc80cfa4e9fb3f54dad482b8cdb262316cbbfc3640a8f807a6e8704 | quote: "final_url": "https://bmh.163.com"
