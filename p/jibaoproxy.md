# JibaoProxy

> jibaoproxy.com | IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/jibaoproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/jibaoproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## JibaoProxy

- `ip-proxy/jibaoproxy-residential` | dead | evidence measured | binding none | category per-GB dynamic residential and per-IP static proxy (Chinese market), site gone | tier Dynamic residential per GB, static residential per month (last seen 2026-01-08)
- identity a placeholder: card and phone unknown | verified 2026-11-03T07:35:32.366Z (live) | stale on 2026-12-04
- url https://www.jibaoproxy.com/
- duplicate of `ip-proxy/jibaoproxy`
- free tier: The site no longer serves: the home page answers HTTP 410. The copy archived on 2026-01-08 listed dynamic residential at $10 / GB, mobile at $15 / GB, dynamic datacenter at $1 / GB, static residential at $8 / 月 (per month, unlimited traffic), shared static datacenter at $0.1 / IP / 天 (per day) and dedicated static datacenter at $4 / IP / 月, with a top-up bonus of up to 80%. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The prices are the archived ones; they are not current.
- per-object cap: not applicable: an address or a traffic pack, not an object | source: [2]
- retention: not applicable: the service is gone. | source: [1]
- egress: Not applicable: the site answers HTTP 410. The archived page listed per-GB dynamic products and an unlimited-traffic static residential line at $8 per month. | metered: yes | free allowance: none | source: [1]
- identity: email | detail: unverified: the register page answers HTTP 410 too and the archived page showed no form; payment options on the archived page were WeChat, Alipay, Visa and Mastercard.
- interface: cli
- limits:
  - volume-quota: none to measure: the site answers HTTP 410; the archived page sold dynamic residential at $10 per GB [1]
- binding note: The service no longer answers, so no constraint is binding.
- interface detail: The archived page named HTTP(S)/SOCKS5-style proxy products; the service is gone.
- tooling: Not applicable: the site answers HTTP 410.
- composes with: Not applicable: the offer is gone.
- reliability: https://www.jibaoproxy.com/ answered HTTP 410 on 2026-11-03 from a direct probe and from the reader; the register path answered 410 as well. An archived copy from 2026-01-08 shows a live price list.
- notes: Named on the Chinese-language forum source in two promotion threads (one offering free dynamic traffic on registration). The vendor name in Chinese is 极豹代理. Cause: dead-service, observed 2026-11-03.
- evidence note: The probe of the home page answers HTTP 410; the archived copy proves what was sold on 2026-01-08. Whether the vendor moved to another domain is unverified.
- extras:
  - rung: 5
  - rung_note: No registration-class claim can be tested: the service is gone.
  - chinese_name: 极豹代理
  - last_archived_live: 2026-01-08
- evidence:
  - probe:www.jibaoproxy.com 2026-11-03: The home page answered HTTP 410 to a direct probe on 2026-11-03. | capture: sha256:c4d6c37cb7d3ea817e9b31cbe2bd2d8fe9b1e2996a0523a067cdc31c77de18d3 | quote: "status": 410
  - [1] 2026-11-03: The archived page of 2026-01-08 sold dynamic residential at $10 per GB. | capture: sha256:8d19dd37b6c9adbf420b06a7e188be2df632ae2af31f62c61f1aef5260a96239 | quote: $10 / GB
  - [1] 2026-11-03: The archived page of 2026-01-08 sold static residential at $8 per month with unlimited traffic. | capture: sha256:8d19dd37b6c9adbf420b06a7e188be2df632ae2af31f62c61f1aef5260a96239 | quote: $8 / 月
  - [2] 2026-11-03: The reader got an HTTP 410 page from the home page. | capture: sha256:3fdd6e31b026f4e31eec461104b998f5edadb5fe90b406344ac1710b359e47e2 | quote: 410 Gone
- sources:
  - [1] https://web.archive.org/web/20260108204925/http://www.jibaoproxy.com/
  - [2] https://www.jibaoproxy.com/

## JibaoProxy (极豹代理)

- `ip-proxy/jibaoproxy` | dead | evidence inferred | binding none | category rotating residential proxy (per GB) | tier Dynamic residential, pay as you go
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:30:28.054Z (live) | stale on 2026-12-05
- url https://www.jibaoproxy.com/
- free tier: 500 MB of dynamic residential traffic on registration, per a cached copy of the vendor's FAQ: 'All new users receive a 500MB free traffic upon registration to test Dynamic Residential Proxies at no cost.' Dynamic residential from $2/GB, dynamic datacenter $0.8/GB. Dynamic residential is priced differently at each read: $2/GB (cached FAQ, read 2026-11-03), $5 per GB (archive of 2026-06-16) and $10 / GB (archive of 2026-01-08); all three are dead-site prices. | unit: MB | metered on: downloaded-bytes | read on: 2026-11-03 | source: [1] | note: Read from a cached copy through one reader; the origin now answers HTTP 410 on every path.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [1]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [1]
- egress: Pay as you go per GB: 'you only pay for the bandwidth you actually use'; the minimum recharge is $20 and the maximum $5,000. | metered: yes | free allowance: 500 MB on registration | source: [1]
- identity: email | detail: The cached beginner's guide says to register at the vendor's site, with an optional invitation code, and that Mainland China IPs cannot reach the registration or usage pages; payment is Alipay or USDT (BEP20, ERC20, Polygon, TRC20). The registration fields are unverified: the site is unreachable.
- interface: unknown
- limits:
  - volume-quota: 500 MB free on registration; dynamic residential from $2/GB; minimum recharge $20 [1]
- limits note: The pool figure (90M+ residential IPs, 240+ countries) is a claim of the cached FAQ.
- binding note: The binding fact is availability: the origin answers HTTP 410, not a quota.
- interface detail: HTTP, HTTPS and SOCKS5 per the cached FAQ; credentials are generated in a dashboard.
- tooling: Any HTTP(S) or SOCKS5 proxy client with the generated credentials, while the service is reachable.
- composes with: A host-side hop would dial the generated proxy endpoint; the origin is currently unreachable, so no chain was possible.
- reliability: https://www.jibaoproxy.com/ answered HTTP 410 (a 136-byte nginx '410 Gone' page) to a direct probe and to a page reader on 2026-11-03, and so did the FAQ, documentation and product paths; an archived copy dated 2026-06-16 holds the FAQ and a documentation page was updated 2026-06-21. Whether the 410 is a permanent shutdown or a block of the probing networks is unverified.
- notes: Named on a Chinese-language proxy forum with '注册送500M动态住宅流量, 静态住宅2刀/月起'. The 410 on every path is recorded as the evidence of death, at an inferred rung.
- evidence note: The offer rests on a cached copy of a first-party page; the dead verdict rests on a 410 from two vantage points, and no third source confirms a shutdown.
- extras:
  - rung: 2
  - rung_note: A rotating residential pool is rung 2; the origin was unreachable, so nothing was checked.
- evidence:
  - probe:www.jibaoproxy.com 2026-11-03: A direct probe of the site root returned HTTP 410. | capture: sha256:9d5bd74fac339f9c94bdf4d08d0c743ef1bec4ed54b9eea2140a0dfcd5ae0290 | quote: "status": 410
  - probe:www.jibaoproxy.com 2026-11-03: The 136-byte body of the root is an nginx '410 Gone' page. | capture: sha256:9279fca4132ff075c7be32213a8ebe18e16cdf0fb61b7879d03c13b7f4838981 | quote: 410 Gone
  - [1] 2026-11-03: The cached FAQ prices dynamic residential traffic from $2 per GB. | capture: sha256:08cad12828adce74087a524c474fbfd18692b03cb7ba8d39cb4e46aa1640cbfa | quote: JIBAO's dynamic residential proxies start at $2/GB with pay-as-you-go billing — you only pay for the bandwidth you actually use.
  - [1] 2026-11-03: The cached FAQ promises 500 MB free on registration. | capture: sha256:08cad12828adce74087a524c474fbfd18692b03cb7ba8d39cb4e46aa1640cbfa | quote: All new users receive a 500MB free traffic upon registration to test Dynamic Residential Proxies at no cost.
  - [1] 2026-11-03: Payment is Alipay or USDT. | capture: sha256:08cad12828adce74087a524c474fbfd18692b03cb7ba8d39cb4e46aa1640cbfa | quote: JIBAO Proxy accepts Alipay and cryptocurrency (USDT on BEP20, ERC20, Polygon, and TRC20 networks).
  - [2] 2026-11-03: The service refuses Mainland China addresses at registration and use. | capture: sha256:c3bddba440b07a11f73ce997048408ec2faaf12f1550a959baf7c89e4c541d08 | quote: An overseas network environment(Mainland China IPs cannot access the registration or usage pages)
  - probe:https://jibaoproxy.com/ 2026-11-03: The vendor's domain answered HTTP 410 on 2026-11-03 after redirecting the apex to www. | capture: sha256:8f2e61cfca690a8d1dde39aaea7d159a44bfbad781d2494245d5ebd402334219 | quote: "status": 410
  - [2] 2026-11-03: A documentation path of the vendor's site also answers 410 Gone, with an origin web-server body. | capture: sha256:3fdd6e31b026f4e31eec461104b998f5edadb5fe90b406344ac1710b359e47e2 | quote: # 410 Gone
  - [3] 2026-11-03: The archived home page of 2026-06-16 claimed 90M+ residential IPs in 240+ countries and listed dynamic residential at 5 USD per GB, mobile at 9 USD per GB and static residential at 4 USD per month. | capture: sha256:f3d213395641eff62c46803f384207b469d4ce000a12b96c09cc84b780df55ad | quote: 90M+ residential IPs available in real time across 240+ countries.
  - [3] 2026-11-03: The archived static residential product was 4 USD per month with unlimited traffic. | capture: sha256:f3d213395641eff62c46803f384207b469d4ce000a12b96c09cc84b780df55ad | quote: $4 / Month
  - [4] 2026-11-03: The vendor's site root, its FAQ and its documentation path still answer HTTP 410 on re-read, so the dead verdict stands | capture: sha256:3fdd6e31b026f4e31eec461104b998f5edadb5fe90b406344ac1710b359e47e2 | quote: # 410 Gone
  - [5] 2026-11-04: The archive of 2026-01-08 priced dynamic residential at $10 per GB. | capture: sha256:8d19dd37b6c9adbf420b06a7e188be2df632ae2af31f62c61f1aef5260a96239 | quote: $10 / GB
  - [5] 2026-11-04: The archive of 2026-01-08 priced static residential at $8 per month with unlimited traffic. | capture: sha256:8d19dd37b6c9adbf420b06a7e188be2df632ae2af31f62c61f1aef5260a96239 | quote: $8 / 月
- sources:
  - [1] https://www.jibaoproxy.com/faq.html
  - [2] https://www.jibaoproxy.com/doc/docs/beginners-guide/
  - [3] https://web.archive.org/web/20260616155848/https://www.jibaoproxy.com/?provider=wayback
  - [4] https://www.jibaoproxy.com/
  - [5] https://web.archive.org/web/20260108204925/http://www.jibaoproxy.com/
