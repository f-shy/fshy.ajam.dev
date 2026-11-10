# sososo

> sososo.io | IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sososo/ | JSON https://fshy.ajam.dev/api/v1/entity/sososo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## sososo (japan private room)

- `ip-proxy/sososo-japan-private-room` | paid-only | evidence documented | binding none | category ISP-registered VPS | tier Japan D zone private room (dedicated IPv4 and IPv6)
- needs card unknown, phone yes, ID no, institution no | verified 2026-11-03T07:35:32.672Z (live) | stale on 2026-12-04
- url https://sales.sososo.io/products/PrivateRoom/d
- free tier: No free tier. Japan D zone dedicated is $29.99 a month: 1 CPU, 2048 MB RAM, 30 GB NVMe, 100 Mbps peak, 10 TB a month in plus out (throttled above), one dedicated IPv6 with all ports and one dedicated IPv4 that is fixed and does not change. The product page showed 'sold out' on 2026-11-03. Other private-room zones are C at $99.99, E at $129.99 and H at $29.99 a month. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The listing page for private rooms shows the five zone prices; the D zone page states the specification and the sold-out state.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a rented machine and its address, not stored bytes | source: [1] | note: The page states the IPv4 and the IPv6 are fixed and do not change; an address-retention term at non-payment is not stated.
- egress: 10 TB a month counted as in plus out, with speed reduced above the allowance. The 100 Mbps figure is a peak: the page says the actual rate falls when the line is congested. Some high-risk IPv4 ports are blocked by the ISP, for example 25, 80 and 443. | metered: yes | free allowance: 10 TB per month (in plus out) on the D zone | source: [1]
- identity: email | detail: The registration form marks first name, last name, email, password and password confirmation as required (asterisks); phone, company, country, address and city are not marked required. Payment routes the notice lists are crypto through two processors, Alipay QR, Revolut and Wise (the last three confirmed by hand). Whether a card is accepted is unverified.
- interface: unknown
- limits:
  - volume-quota: 10 TB per month in plus out on the D zone, speed reduced above it [1]
  - per-ip-shaping: 100 Mbps peak on the D zone, lower when the line is congested [1]
- limits note: Stock decides this record: the D zone was sold out when read. The vendor's own pages do not use the word residential; they say the IPv4 ports are blocked by the ISP. A third-party test report of an earlier sososo plan titles it a BIGLOBE home-broadband VPS, which is reported, not verified for this plan.
- binding note: The 10 TB allowance is far above a low-volume exit. What decides the record is stock and the unverified registration class.
- interface detail: A virtual dedicated server (the page says all private-room products are VDS) with a fixed IPv4 and IPv6; the access method is not stated on the product page.
- tooling: An SSH or RDP client, whichever the image supports, plus a proxy or tunnel daemon the user installs on the machine. The vendor publishes no proxy endpoint on the pages read.
- composes with: A Worker opens an outbound connection to the server's fixed IPv4 and the server makes the upstream request, so the upstream sees an address on the ISP line the vendor sells. Some ports, for example 25, 80 and 443, are disabled by the ISP on the IPv4 per the page.
- reliability: The home page carries a notice dated 2026-10-18 that the site had been upgraded and should work normally again, so the storefront had an outage that month.
- notes: sososo sells Japanese lines on a Paymenter storefront in three groups: shared rooms (VPS), private rooms (VDS) and takeout services. This record covers the private-room D zone, the cheapest dedicated-IPv4 line; the Rakuten 5G mobile private room is its own record. Whether the D zone address is registered to a consumer ISP is unverified: the page publishes no test address.
- evidence note: Price, specification, stock and registration fields are documented from the vendor's shop pages. The residential label is third-party and the registration class is unverified because no test address is published.
- extras:
  - rung: 5
  - rung_note: The offer is a claim about the address class and no test address is published.
- evidence:
  - [1] 2026-11-03: the D zone is $29.99 a month with 1 CPU, 2048 MB RAM, 30 GB NVMe and a 100 Mbps peak | capture: sha256:c39adbc7ac46c44fdea437bf8c4ddfd812b48f47389674032efe19c285c4ac1c | quote: 29.99美元/月 CPU: 1 内存: 2048MB 硬盘: 30G (nvme) 网络: 100Mbps 峰值
  - [1] 2026-11-03: the allowance is 10 TB a month in plus out | capture: sha256:c39adbc7ac46c44fdea437bf8c4ddfd812b48f47389674032efe19c285c4ac1c | quote: 流量: 10TB/月 (in+out)(超出降速)
  - [1] 2026-11-03: the IPv4 is fixed | capture: sha256:c39adbc7ac46c44fdea437bf8c4ddfd812b48f47389674032efe19c285c4ac1c | quote: IPv4为固定ip，不会变化。
  - [1] 2026-11-03: ports 25, 80 and 443 are blocked by the ISP on the IPv4 | capture: sha256:c39adbc7ac46c44fdea437bf8c4ddfd812b48f47389674032efe19c285c4ac1c | quote: 独立IPv4(全端口，部分高风险端口isp商禁用，禁用端口例如25,80,443等)
  - [1] 2026-11-03: the D zone is sold out | capture: sha256:c39adbc7ac46c44fdea437bf8c4ddfd812b48f47389674032efe19c285c4ac1c | quote: 產品 日本D区独享 已售罄
  - [2] 2026-11-03: the registration form marks name, email and password fields required and leaves phone, company and address unmarked | capture: sha256:7e4564d38f66e6a77006c748ba424dae3c557a746003f17f028c6ea355aa1ea0 | quote: 名字 * 姓氏 * 電子郵件 * 密碼 * 確認密碼 * Phone Company Name Country
  - [3] 2026-11-03: crypto payment through a processor is enabled | capture: sha256:257acc543f2c5363149c0ba433d66161e84a5f43bf8d2d90bc5292a81a20c6b4 | quote: 加密货币支付系统nowpayments已经开通
  - [3] 2026-11-03: Alipay QR payment is enabled with manual confirmation | capture: sha256:257acc543f2c5363149c0ba433d66161e84a5f43bf8d2d90bc5292a81a20c6b4 | quote: 支付宝扫码支付已开通（人工确认）。
  - [4] 2026-11-03: a 2024 third-party test report titles an earlier sososo Japan plan a BIGLOBE home-broadband VPS | capture: sha256:e9d9b183d04ebd98524d9039c0aaf7a721c6fffdee4c09f60e9ce066dcae3e08 | quote: sososo 日本BIGLOBE 家宽VPS测试记录
- sources:
  - [1] https://sales.sososo.io/products/PrivateRoom/d
  - [2] https://sales.sososo.io/register
  - [3] https://sales.sososo.io/
  - [4] https://lowendaff.com/2024/06/15/%f0%9f%87%af%f0%9f%87%b5-sososo-%e6%97%a5%e6%9c%acbiglobe-%e5%ae%b6%e5%ae%bdvps%e6%b5%8b%e8%af%95%e8%ae%b0%e5%bd%95/

## sososo (Japan Rakuten 5G private room)

- `ip-proxy/sososo-rakuten-5g-private-room` | paid-only | evidence documented | binding none | category mobile proxy, 4G modem exit | tier Japan Rakuten 5G private room
- needs card unknown, phone yes, ID no, institution no | verified 2026-11-03T07:35:32.672Z (live) | stale on 2026-12-04
- url https://sales.sososo.io/products/PrivateRoom/rakuten5G
- free tier: No free tier. Japan Rakuten dedicated is $99.99 a month: 2 CPU, 4096 MB RAM, 30 GB NVMe, a Rakuten 5G mobile primary network at 300 Mbps peak, 20 TB a month one-way (throttled above), an IPv4-only dedicated address with no inbound ports, and a secondary IPv6 network. The IPv4 is dynamic and changes when the phone network restarts, with one change a month by ticket. The product page showed 'sold out' on 2026-11-03. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The page says the machine is switched on the same working day.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a rented machine and its address, not stored bytes | source: [1] | note: The page states the IPv4 is dynamic; no address-retention term at non-payment is stated.
- egress: 20 TB a month counted one-way, with speed reduced above the allowance. The 300 Mbps figure is a peak that falls when the line is congested. | metered: yes | free allowance: 20 TB per month (one-way) on the Rakuten 5G private room | source: [1]
- identity: email | detail: The registration form marks first name, last name, email, password and password confirmation as required (asterisks); phone, company, country, address and city are not marked required. Payment routes listed on the home page are crypto through two processors, Alipay QR, Revolut and Wise. Whether a card is accepted is unverified.
- interface: unknown
- limits:
  - volume-quota: 20 TB per month one-way on the Rakuten 5G private room, speed reduced above it [1]
  - per-ip-shaping: 300 Mbps peak on the Rakuten 5G network, lower when the line is congested [1]
- limits note: Stock decides this record: the product was sold out when read. The address is shared-carrier mobile, not a fixed consumer line: it is dynamic and one ticketed change is allowed each month.
- binding note: The 20 TB allowance is far above a low-volume exit. What decides the record is stock and the unverified registration class of the mobile carrier address.
- interface detail: A virtual dedicated server whose outbound IPv4 is a Rakuten 5G mobile line with no inbound ports; the access method is not stated on the product page.
- tooling: An SSH or RDP client, whichever the image supports, plus a proxy or tunnel daemon the user installs on the machine. Inbound connections to the mobile IPv4 are not available, so the machine reaches out. The vendor publishes no proxy endpoint on the pages read.
- composes with: A Worker reaches the server over its IPv6 secondary network and the server makes the upstream request over the Rakuten 5G primary line, so the upstream sees a Japanese mobile-carrier address instead of AS13335. The page says traffic comes in on the secondary network and goes out on the primary.
- reliability: The IPv4 changes when the phone network restarts, so a session can lose its address. The home page carries an upgrade notice dated 2026-10-18 after a storefront outage.
- notes: sososo's Rakuten private room is a Japanese mobile-carrier exit attached to a VDS, sold at $99.99 a month and sold out when read. It is a different product from the fixed-line D zone record of the same vendor.
- evidence note: Price, specification, stock and registration fields are documented from the vendor's shop pages. The registration class of the carrier address is unverified because no test address is published.
- extras:
  - rung: 5
  - rung_note: The offer is a claim about the address class (a mobile carrier address) and no test address is published.
- evidence:
  - [1] 2026-11-03: the Rakuten private room is $99.99 a month | capture: sha256:7ab870a3b201444ce0a9fbceacae8911490000692561c862b0e4b6ae7c1a55fd | quote: 99.99美元/月
  - [1] 2026-11-03: the primary network is Rakuten 5G mobile with an IPv4-only dedicated address and no inbound ports | capture: sha256:7ab870a3b201444ce0a9fbceacae8911490000692561c862b0e4b6ae7c1a55fd | quote: 主网络: 乐天5G移动网络,ipv4 only(无端口),独享ip
  - [1] 2026-11-03: the IPv4 is dynamic with one ticketed change a month | capture: sha256:7ab870a3b201444ce0a9fbceacae8911490000692561c862b0e4b6ae7c1a55fd | quote: IPv4为动态ip，重启手机网络，会变化。(每月可工单1次变更ip)
  - [1] 2026-11-03: the allowance is 20 TB a month one-way | capture: sha256:7ab870a3b201444ce0a9fbceacae8911490000692561c862b0e4b6ae7c1a55fd | quote: 流量: 20TB/月 (单边)(超出降速)
  - [1] 2026-11-03: the Rakuten room is sold out | capture: sha256:7ab870a3b201444ce0a9fbceacae8911490000692561c862b0e4b6ae7c1a55fd | quote: 產品 日本乐天独享-工作日当日开机 已售罄
  - [2] 2026-11-03: the registration form marks name, email and password fields required and leaves phone, company and address unmarked | capture: sha256:7e4564d38f66e6a77006c748ba424dae3c557a746003f17f028c6ea355aa1ea0 | quote: 名字 * 姓氏 * 電子郵件 * 密碼 * 確認密碼 * Phone Company Name Country
  - [3] 2026-11-03: crypto payment through a processor is enabled | capture: sha256:257acc543f2c5363149c0ba433d66161e84a5f43bf8d2d90bc5292a81a20c6b4 | quote: 加密货币支付系统nowpayments已经开通
- sources:
  - [1] https://sales.sososo.io/products/PrivateRoom/rakuten5G
  - [2] https://sales.sososo.io/register
  - [3] https://sales.sososo.io/
