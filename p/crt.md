# crt.sh certificate transparency search

> crt.sh | Netdisk and pan; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/crt/ | JSON https://fshy.ajam.dev/api/v1/entity/crt.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## crt.sh certificate transparency search (AList and OpenList hostnames)

- `netdisk-pan/crt-sh-alist-openlist-ct-channel` | qualifies-with-caveat | evidence measured | binding request-rate | category index-list
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:15:21.167Z (live) | stale on 2026-11-26
- url https://crt.sh/
- free tier: not stated: crt.sh is a public certificate transparency search with a JSON output and prints no allowance, quota or price | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: not applicable; it is a search over issued certificates | source: [1]
- retention: a certificate stays listed after it expires; exclude=expired limits a query to certificates that are still valid | source: [1]
- egress: no egress; it is a search answer, and one prefix query returned a JSON body of several hundred KB | metered: no | source: [1]
- identity: anonymous | detail: an open search page and JSON endpoint, read with no account
- interface: rest
- limits:
  - request-rate (binding): a single wildcard query alist.%25 returned a truncated result set (the four known hosts alist.qsesvick.top, alist.tianmoy.cn, alist.shenzjd.com and alist.jiejingfan.vip were all missing from it) and crt.sh answered 502, 404 or no reply on many attempts; one query per next character, retried, was needed [2]
- binding note: crt.sh throttles and truncates wide wildcard queries, so a prefix partition is required and the result is a lower bound.
- tooling: GET https://crt.sh/?q=alist.PREFIX%25&output=json&exclude=expired, one query per next character; a read client needs no login. The hostnames then go through GET /api/public/settings and GET /api/me on each host; the listing step is a POST that a GET-only probe cannot make
- composes with: a hostname list for the capability probe in the public-instances protocol, to be run after the hosted index lists (bangumi.tv, kuhehe.github.io) and in addition to them
- reliability: crt.sh answered HTTP 502, 404 or no reply on a share of its requests and needed repeated tries; a hostname in CT is a certificate, not a live instance.
- notes: Certificate transparency lists hosts whose name starts with alist or openlist, including hosts that no forum or GitHub index names. It holds 7447 distinct hostnames with such a label (wildcard form included), 4 with an existing record. Of these, 2356 return the AList or OpenList envelope on GET /api/public/settings and 588 an enabled guest session on GET /api/me, so 586 new hostnames pass steps 0 and 1. The listing step (POST /api/fs/list) is not done, so none counts as a readable instance. Hosts named pan, cloud or share are not reachable by this channel.
- extras:
  - access_mode: index
  - ct_hostnames: 7447
  - with_existing_record: 4
  - answered_settings: 2356
  - guest_enabled: 588
  - new_guest_enabled: 586
  - listing_step_run: no
- evidence:
  - probe:crt.sh-alist-a-body 2026-11-03: the prefix query alist.a%25 with exclude=expired returns certificates whose names carry an alist label, such as the wildcard *.alist.anhdv.workers.dev | capture: sha256:ccf4e04be45ae1d71dd6409c1c1dae07782e1d21c52453e1bc0d8bf52bf554e2 | quote: "common_name":"anhdv.workers.dev","name_value":"*.alist.anhdv.workers.dev"
  - probe:crt.sh-openlist-a-body 2026-11-03: the prefix query openlist.a%25 with exclude=expired returns certificates whose names carry an openlist label, such as openlist.akz.cc.cd | capture: sha256:752bbd2cb48601a932cbf5e6364d7249e60dd68b568e50944396bab6f2a7199a | quote: "common_name":"openlist.akz.cc.cd","name_value":"openlist.akz.cc.cd"
  - probe:crt.sh-alist-tianmoy-body 2026-11-03: a direct query for a known instance finds its certificate, so the instance is in CT even where the broad alist.%25 query did not return it | capture: sha256:2e03b5526ebfd78ebbf14debaf25d33da19ed561acd18337fa84cc49fc9280f2 | quote: "common_name":"alist.tianmoy.cn","name_value":"alist.tianmoy.cn"
  - probe:openlist.011206.xyz-me 2026-11-03: a hostname found only through CT, openlist.011206.xyz, answers GET /api/me with an enabled guest session, which is step 1 of the instance protocol | capture: sha256:92b5f17df4530587fe3412ec271b5970bf2cf3764f1adab0b418c9d9a10368fe | quote: "username":"guest","password":"","base_path":"/","role":1,"disabled":false
  - probe:crt-sh-alist-openlist-ct-hostnames 2026-11-04: the stored CT hostname list holds 7447 lines, one distinct hostname with an alist or openlist label each | capture: sha256:e47630d7f625ce61eb6469313ffb18decb8d26e8435460ede8ba07b91bf79b51 | quote: alist-barbers.com
  - probe:crt-sh-alist-openlist-settings-hosts 2026-11-04: the stored list of hosts that answered GET /api/public/settings holds 2356 lines | capture: sha256:422e5df1133eb71181bbf74f14e1623e10713162ca5771bdc418a2f504e12ecb | quote: alist.002199.xyz
  - probe:crt-sh-alist-openlist-guest-hosts 2026-11-04: the stored list of guest-enabled hosts holds 588 lines | capture: sha256:28cb921d51cc591ca2e910a7877f05ab5f38ab6676354929ef9d3a907432c458 | quote: alist.0101111.xyz
  - probe:crt-sh-alist-openlist-guest-hosts 2026-11-04: the stored guest-enabled host list holds 588 lines | capture: sha256:28cb921d51cc591ca2e910a7877f05ab5f38ab6676354929ef9d3a907432c458 | quote: alist.0101111.xyz
- sources:
  - [1] https://crt.sh/?q=alist.a%25&output=json&exclude=expired
  - [2] https://crt.sh/?q=alist.%25&output=json
