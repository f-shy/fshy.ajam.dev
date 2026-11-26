# HoRain Cloud

> Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/horain-cloud/ | JSON https://fshy.ajam.dev/api/v1/entity/horain-cloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HoRain Cloud

- `compute/horain-cloud` | fails-identity | evidence reported | binding per-ip-shaping | category cloud VM
- needs card unknown, phone no, ID yes, institution no | verified 2026-10-22 (live) | stale on 2026-11-06
- url https://hostloc.com/thread-1422161-1-1.html
- free tier: The Bootes series is a dual Xeon E5-2689 at 16 cores / 32 threads with 64 GB RAM, a 512 GB NVMe disk and 20 Mbps of Telecom bandwidth at CNY 219 a month with the same price on renewal. The Kara series is 8 cores / 16 threads with 16 GB, a 240 GB SSD or 1 TB HDD and 100 Mbps dedicated at CNY 349. A Jiaxing machine with 2 x Xeon Gold 6138 at 40 cores / 80 threads, 384 GB RAM, 1.92 TB NVMe and 50 Mbps is CNY 699, and an 8 x RTX 4090 machine with 1 TB RAM and 8 TB NVMe is CNY 7500 a month. | unit: GiB | metered on: wall-clock | read on: 2025-07-14 | source: [1] | note: kind not stated
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: post dated 2025-07-14 reads 'Bootes series: dual E5-2689 (16 cores 32 threads) / 64G memory / 512G NVMe / 20M bandwidth, price 219 CNY per month (renewal same price)' and 'Kara series: 8 cores 16 threads / 16G / 240G SSD or 1TB HDD / 100M dedicated bandwidth, 349 CNY per month'; read on 2026-10-22 | metered: yes | source: [1]
- identity: national-id | detail: national-id: real-name verification 'is a basic requirement for using all of our services'; for an individual it requires a mainland Chinese resident aged 18 or over, holding a valid resident identity card, with true and valid details, verified in person through Alipay including a face check, reviewed instantly, with the first verification free and a repeat after a failure chargeable at a price the page does not give. The purchase flow puts this at step two, after email verification and a password, and no phone number appears in either step. A funded balance is a prerequisite for any service. Card, hold, debit and prepaid are not stated: unknown.
- interface: rest
- limits:
  - per-ip-shaping (binding): 20 Mbps of Telecom bandwidth is the whole point and the whole limit: it is about 6.5 TB a month at line rate, and it is a single-carrier port rather than a BGP blend. [1]
- limits note: 20 Mbps of Telecom bandwidth is the whole point and the whole limit: it is about 6.5 TB a month at line rate, and it is a single-carrier port rather than a BGP blend.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: At about sixty times the memory of a USD 6 VPS for about five times the price, this is the cheapest large-RAM machine in earlier readings, and it composes with nothing internationally because the port is a 20 Mbps single-carrier link.
- reliability: no reliability event recorded
- notes: The date is the part a reader must see first: the ladder is dated 2025-07-14 and a second post of 2025-07-07 carries the same figures word for word, so the price is fifteen months old at the time of reading and may have moved. A currency conversion is deliberately not given because the rate on the day is unquoted. The reseller table prices the same box at 299 CNY with 30M BGP against the vendor's 219 with 20M Telecom, which is the usual gap between a carrier port and a BGP blend and should not be read as a contradiction.
- extras:
  - facets.class: floor-price
  - facets.shape.cpu: 2x Intel Xeon E5-2689
  - facets.shape.vcpu: 16
  - facets.shape.threads: 32
  - facets.shape.ram_gib: 64
  - facets.shape.disk: 512 GB NVMe
  - facets.shape.bandwidth_mbit: 20
  - facets.shape.price_cny_month: 219
  - facets.shape.gpu_count: 0
- evidence:
  - [2] 2026-10-22: a reseller page lists the same Zhenjiang ladder in a table: 'E5-2689*2 | 32G DDR3 | 512G ordinary SSD | 30M BGP | 299' and the 100M BGP row at 599, with add-on pricing of 60 CNY per month per BGP IPv4 (read on 2026-10-22; the page carries no date of its own)
  - [3] 2026-10-22: independent listing 'HoRain: Jiangsu Zhenjiang BGP physical server, E5-2689*2/32G/20M bandwidth/512G SSD, from 299 CNY per month' (read on 2026-10-22)
  - [4] 2026-10-22: the vendor site returns no readable body, so the vendor's own price page could not be read and the numbers rest on reseller and forum listings
  - [5] 2026-10-22: vendor text, verbatim: ' ' (account real-name verification is an important measure for confirming a user's true identity, and is a basic requirement for using all of our services) -- the gate binds every service, not a paid tier alone
  - [5] 2026-10-22: individual conditions, quoted as four list items with markdown emphasis removed: ' 18 ' / ' ' / ' ' / ' ' (a mainland Chinese resident aged 18 or over / holding a valid resident identity card / with identity-card details that are true and valid / performing the verification in person)
  - [5] 2026-10-22: the check runs through Alipay and includes a face check: ' ' (the platform cooperates with Alipay, submits the material and the real-name request to Alipay, and Alipay processes the face-information verification; the platform only learns from Alipay whether it passed)
  - [5] 2026-10-22: review time and cost, quoted with the page's own emphasis markers: '** ** ' (individual verification: reviewed instantly) against '** ** 1-3 ' (enterprise verification: usually one to three working days); and on cost, ' ' together with ' ' (the first basic real-name verification is free; a repeat after a failure is chargeable, at a price the page does not give)
  - [5] 2026-10-22: 
  - [6] 2026-10-22: a funded balance is a precondition, so there is nothing free to reach before paying: ' HoRain Cloud ' (topping up is the prerequisite for using HoRain Cloud services; you need to keep enough balance in the account to buy and renew the various cloud services)
  - [7] 2026-10-22: the purchase flow puts the identity check at step two, after an email-only account step: ' ' lists ' ' (complete email verification) and ' ' (set an account password), then ' ' lists ' ' and ' ' (step two, real-name verification: identity card for an individual, business licence for an enterprise). No phone number appears in either step
  - [8] 2026-10-22: the shop is closed and everything moves to a human: page title ' ' (system under maintenance), body ' ' (for product activation, product renewal, back-end control, account top-up and service tickets, please contact a human customer-service agent)
  - [9] 2026-10-22: the promotional offer and its real-name condition, quoted from the search snippet because the page itself returned the forum's IPv6 wall: ' 2 2G 5M CN2 29/ ' (prize specification: 2 cores, 2 GB, 5 Mbps bandwidth on a CN2-optimised route, renewal price CNY 29 per month) and ' 30 ' (claim the prize within 30 days of the draw, after which it cannot be redeemed), with the forfeit clause ' NodeSeek ' (where the account on the corresponding platform has breached the service terms or has not completed real-name verification, and this is unresolved after contact, the win is treated as abandoned). The same snippet names three prizes and a draw at 2026/09/14 23:59:59, is posted by a thread starter named HoRain, and links purchase to the base.horain.net shop that now returns the maintenance notice; the snippet does not establish that the account is the company's own
  - [4] 2026-10-22: the vendor homepage answered 200 but the extraction returned 414 words of navigation only -- product lines, data-centre names, partner logos and the register / log in / console links -- with no price, no free-tier statement and no identity text, so no claim in this finding rests on the homepage
- sources:
  - [1] https://hostloc.com/thread-1422161-1-1.html
  - [2] https://woyard.com/33290.html
  - [3] https://www.yuntue.com/info/wulijigoumai
  - [4] https://www.horain.net/
  - [5] https://docs.horain.net/%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/%E8%B4%A6%E6%88%B7/%E8%B4%A6%E6%88%B7%E5%AE%9E%E5%90%8D.html
  - [6] https://docs.horain.net/%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/%E8%B4%A6%E6%88%B7/
  - [7] https://docs.horain.net/%E4%BA%A7%E5%93%81%E6%8C%87%E5%8D%97/GPU%E7%AE%97%E5%8A%9B%E7%A7%9F%E8%B5%81/%E8%B4%AD%E4%B9%B0%E6%8C%87%E5%8D%97.html
  - [8] https://base.horain.net/cart/goodsList.htm
  - [9] https://www.nodeseek.com/post-926650-1
