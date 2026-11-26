# Dothome

> dothome.co.kr | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/dothome/ | JSON https://fshy.ajam.dev/api/v1/entity/dothome.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Dothome

- `compute/dothome` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:43:13.247Z (live) | stale on 2026-12-05
- url https://www.dothome.co.kr/web/free/index.php
- free tier: '무료호스팅 기본사양 무료' (free hosting, base spec, free) with '디스크 500M' (500 MB disk), '트래픽(월) 15G' (15 GB traffic a month), '기본 도메인 제공' (a base domain supplied) and 'DB 무제한' (unlimited databases). PHP 7.4, 8.0, 8.2 or 8.4 with MySQL 8.x. The page description reads '지금 신청하면 평생 무료호스팅을 이용할 수 있습니다' (apply now for lifetime free hosting), and the manual says '무료호스팅은 6개월 단위로 연장하면 계속해서 무료로 사용하실 수 있습니다' (renew every six months and it stays free). | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-renewable
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Traffic is metered at 15 GB a month on the free hosting; extra traffic is sold as 50 GB for KRW 3,000 a month or a 100 GB top-up for KRW 10,000. | metered: yes | free allowance: 15 GB per month | source: [1]
- identity: email | detail: email verification plus a Google reCAPTCHA, with no phone step in the documented flow: the manual describes the application as email verification then reCAPTCHA then apply, and records that no phone step appears in that flow. Whether a Korean mobile number is demanded at member level is not established, because the signup form itself was not opened. No card is stated for the free plan
- interface: ssh
- limits:
  - volume-quota (binding): 500 MiB of disk and 15 GiB of traffic a month, on a shared host with no SSH, so the first wall is the byte counter and the second is the absence of a shell: this is a place to serve a small PHP app from, not a machine to compute on. [1]
- limits note: 500 MiB of disk and 15 GiB of traffic a month, on a shared host with no SSH, so the first wall is the byte counter and the second is the absence of a shell: this is a place to serve a small PHP app from, not a machine to compute on.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A Korean-region PHP and MySQL host with no card is a durable place to keep a small service and its database, and it chains with any free compute that can call an HTTP endpoint: the compute does the work, Dothome keeps the state and the domain, and neither needs a card.
- reliability: no reliability event recorded
- notes: Korea's most durable free allowance, running since the company's founding and still advertised as lifetime. The one thing not established is whether member signup demands a Korean mobile number: the free-hosting manual documents only email verification and a reCAPTCHA, and no identity step appears in that flow, but Korean sites often add a real-name step at member level and on 2026-11-04 did not open the signup form. Settling it needs a signup attempt. The paid sibling, at KRW 500 a month, is the cheapest route found among evaluated providers to attach an owned domain to a free host.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: perpetual-renewable
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: ' 500M', ' ( ) 15G', ' ', 'DB ', ' PHP 7.4, 8.0, 8.2, 8.4 ', quoted; the meta description reads ' '
  - [2] 2026-10-22: ' PHP 7.4 , 8.0 , 8.2, 8.4 / MySQL 8.x ' and, for applications after 2025-07-17, SSL on the base domain 'https:// .dothome.co.kr', quoted
  - [3] 2026-10-22: the application flow is email verification then a Google reCAPTCHA then apply: ' ... [ ]', then ' ', quoted; no phone step appears in the documented flow
  - [4] 2026-10-22: the free plan excludes domain connection, SSL on your own domain and 'SSH ' (SSH access) unless the paid option is added at KRW 500 a month, quoted
  - [1] 2026-11-03: the free hosting base spec lists 15 GB of traffic a month | capture: sha256:4f273992231860d1371e91c34ba0296d7eeeacd2413e277e2b7a932a6dcf6369 | quote: 트래픽(월) 15G
- sources:
  - [1] https://www.dothome.co.kr/web/free/index.php
  - [2] https://docs.dothome.co.kr/books/9bf31/page/41f1f
  - [3] https://docs.dothome.co.kr/books/9bf31/page/084b6
  - [4] https://docs.dothome.co.kr/books/faq-GiU
