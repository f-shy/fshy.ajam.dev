# OnesProxy

> onesproxy.com | IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/onesproxy/ | JSON https://fshy.ajam.dev/api/v1/entity/onesproxy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OnesProxy

- `ip-proxy/onesproxy-static-residential` | paid-only | evidence documented | binding per-ip-shaping | category per-address static residential proxy (dual-ISP native and broadcast) with dynamic residential and mobile GB products | tier Static residential proxy, per IP, from $4.8 each
- needs card yes, phone yes, ID no, institution no | verified 2026-11-04T00:30:28.990Z (live) | stale on 2026-12-05
- url https://www.onesproxy.com/
- price not applicable: an address, not a byte; from USD 4.8 per IP
- free tier: No standing free tier. New users can ask customer service, with the registered email, for a 1-day pack of a US static residential IP or datacentre IPs of all regions. Every standing product is paid, per IP or per GB. | unit: hours | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: The trial is issued by support on request, not self-service.
- per-object cap: not applicable: an address or a traffic pack, not an object | source: [1]
- retention: not applicable: an address, not stored bytes. The help centre has an article on whether an expired proxy can be recovered; its text was not read: unverified. | source: [2] | note: days is null because no bytes are stored.
- egress: Static residential: "无限流量与并发数" (unlimited traffic and concurrency); billed per IP. | metered: no | free allowance: a 1-day pack of static residential US IPs or datacentre IPs of all regions, on request; the count is not stated | source: [1]
- identity: email | detail: Sign-up and login support a Google account, a WeChat account, an email address or a phone number; the trial pack is requested from support with the registered email. Payment: Alipay, Visa or Mastercard credit card, or USDT. No ID document is named on the pages read.
- interface: cli, rest
- limits:
  - per-ip-shaping (binding): one address per unit with unlimited traffic and concurrency stated; the vendor states 99.99% availability [1]
  - volume-quota: none for the static product (unlimited traffic); dynamic products are metered per GB [1]
- binding note: Traffic is unlimited, so the single address and its registration class bind; the label offers a choice between native and broadcast IPs, which are not the same class.
- interface detail: HTTP and SOCKS5, stated in the vendor description; the page states API support ("支持API接口"). Configuration guides are published for fingerprint browsers and V2rayN, clash verge and V2rayNG.
- tooling: Any client that speaks SOCKS5 or an HTTP proxy, reached from a Worker through a relay that dials SOCKS5. The vendor publishes setup guides for fingerprint browsers; no SDK was seen. That is a note on tooling, not a reason to reject.
- composes with: The upstream sees the leased address. The vendor labels the static product 双ISP原生与广播IP (dual-ISP native and broadcast IP) and 双ISP住宅属性; no address was published, so the registration class is unverified.
- reliability: The vendor states 99.99% availability for its own backbone; no throughput, ban or replacement measurement was made.
- notes: Named on the Chinese-language forum source (a post titled with the vendor name and "NS 专属价", an NodeSeek-specific price); the forum is the lead and the evidence is the vendor page. The vendor name in Chinese is 壹创云.
- evidence note: Prices and product labels are read from the vendor home and register pages; trial, sign-up and payment terms from the help centre. The sign-up form and the delivered addresses were not seen.
- extras:
  - rung: 5
  - rung_note: The product is a registration-class claim (dual-ISP native and broadcast); nothing was delivered or looked up.
  - chinese_name: 壹创云
- evidence:
  - [1] 2026-11-03: The static residential product is labelled dual-ISP native and broadcast IP. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 纯净双ISP原生与广播IP
  - [1] 2026-11-03: The static residential price is $4.8 each. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: $4.8/个
  - [1] 2026-11-03: Static residential is billed by the number of IPs. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 按IP个数收费
  - [1] 2026-11-03: Static products state unlimited traffic and concurrency. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 无限流量与并发数
  - [1] 2026-11-03: Dynamic residential is $0.88 per GB. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: $0.88/GB
  - [1] 2026-11-03: A free trial is advertised. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 免费试用
  - [3] 2026-11-03: The register page lists dynamic mobile at $2.28 per GB. | capture: sha256:171048ea81a2294d4b1ad9fb17e4c27514e4f91ca3c1e5ee0877d1073294d095 | quote: 动态手机代理来自真实手机本地4G网络$2.28/GB
  - [2] 2026-11-03: The help centre has an article on a registration verification code that does not arrive. | capture: sha256:99c543ad2448e78bcba953956199c4645fd1754f843ad0a6639aaf9145aa19de | quote: 注册账号收不到验证码
  - [4] 2026-11-04: New users can get a 1-day pack of a US static residential IP or datacentre IPs by asking customer service with the registered email. | capture: sha256:263bacea6d27c1f38faccd5e67c7d368cd63ff3ad4927a4a79fbb9209d3bd4ed | quote: 对于新用户，目前OnesProxy提供静态住宅美国IP或者机房全量地区的1天使用礼包，若有需要请联系官网在线客服，提供注册邮箱获取。
  - [5] 2026-11-04: Accounts are opened with a Google account, WeChat, an email address or a phone number. | capture: sha256:86c245f0145735b5fb6a3ee26a8ecfe25dbf2d1c76e005e461f44d41539b275c | quote: 平台注册登录目前支持Google账号、微信账号、邮箱和手机号登录注册。
  - [6] 2026-11-04: Payment is by Alipay, Visa or Mastercard credit card, or USDT. | capture: sha256:6d080f6daeffbd3b5fbd02b18979d544238e43cf549aa4d78a5cbf0dd1da495a | quote: OnesProxy目前支持支付宝、信用卡（visa&万事达）、USDT等方式支付，具体可以在充值页面进行查看。
  - [6] 2026-11-04: Dynamic traffic carries a validity period and unconsumed traffic is billed as consumed. | capture: sha256:6d080f6daeffbd3b5fbd02b18979d544238e43cf549aa4d78a5cbf0dd1da495a | quote: 动态住宅代理：动态住宅代理会根据流量进行计费，且流量有时效限制，期限内未消耗完流量按全额消耗计费；
  - [1] 2026-11-04: The buyer chooses between native IPs and broadcast IPs for the static residential product. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 自由选择原生与广播IP
  - [1] 2026-11-04: The vendor claims cooperation with Cogent and Equinix and over 1000 self-built backbone servers. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 与Cogent、Equinix建立深度业务合作，自建超过1000台骨干网服务器。
  - [4] 2026-11-04: The 1-day trial pack is requested from customer service with the registered email. | capture: sha256:263bacea6d27c1f38faccd5e67c7d368cd63ff3ad4927a4a79fbb9209d3bd4ed | quote: 对于新用户，目前OnesProxy提供静态住宅美国IP或者机房全量地区的1天使用礼包，若有需要请联系官网在线客服，提供注册邮箱获取。
  - [4] 2026-11-04: New users get a 1-day pack of US static residential IPs or datacentre IPs of all regions on request; no count is named | capture: sha256:263bacea6d27c1f38faccd5e67c7d368cd63ff3ad4927a4a79fbb9209d3bd4ed | quote: 对于新用户，目前OnesProxy提供静态住宅美国IP或者机房全量地区的1天使用礼包，若有需要请联系官网在线客服，提供注册邮箱获取。
- sources:
  - [1] https://www.onesproxy.com/
  - [2] https://help.onesproxy.com/docs/c4b78TPI
  - [3] https://www.onesproxy.com/register
  - [4] https://help.onesproxy.com/docs/dai-li-IP-shi-fou-zhi-chi-shi-yong
  - [5] https://help.onesproxy.com/docs/zhu-ce-deng-lu
  - [6] https://help.onesproxy.com/docs/fu-kuan-fang-shi-yu-ji-fei-gui-ze

## OnesProxy (壹创云)

- `ip-proxy/onesproxy-residential` | paid-only | evidence documented | binding volume-quota | category rotating residential, static ISP and mobile proxy | tier Static ISP residential (per IP) and dynamic residential (per GB)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:35:31.081Z (live) | stale on 2026-12-04
- url https://www.onesproxy.com/
- duplicate of `ip-proxy/onesproxy-static-residential`
- free tier: No price-free tier stated; the page has a '免费试用' (free trial) button. Prices: 静态住宅代理 (static residential) $4.8 per IP, 静态数据中心代理 (static datacenter) $0.38 per IP, 动态住宅代理 (dynamic residential) $0.88/GB, 动态手机代理 (dynamic mobile) $2.38/GB. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The sign-up page of the same site lists the mobile product at $2.28/GB, against $2.38/GB on the home page. The size of the free trial is unverified: behind a sign-up.
- per-object cap: not applicable: an address or a traffic quota, not an object | source: [1]
- retention: not applicable: a proxy session or a rented address, not stored bytes | source: [1]
- egress: Static products: '按IP个数收费' (billed per IP), unlimited traffic and concurrency. Dynamic products: '按流量GB收费' (billed per GB), unlimited concurrency, sticky and rotating sessions. | metered: yes | free allowance: trial offered, size unverified | source: [1]
- identity: email | detail: The sign-up form was not rendered in the pages captured (the register page returned only navigation). unverified: behind a sign-up.
- interface: rest
- limits:
  - volume-quota (binding): dynamic residential $0.88/GB and mobile $2.38/GB metered per GB; static lines per IP with unlimited traffic [1]
- limits note: The vendor claims 10M+ own residential IPs, 190+ countries, Cogent and Equinix backbone partnerships with 1000+ own backbone servers, and ASN, ownership and geolocation customisation for enterprise orders. These are vendor claims, not measured.
- binding note: The dynamic lines are metered per GB; the static lines are bought per IP.
- interface detail: SOCKS5 and HTTP; the vendor sells native SOCKS5 residential proxies with API support, QR-code export of proxy details and integrations for fingerprint browsers; targeting down to city.
- tooling: Any client that speaks an HTTP(S) or SOCKS5 proxy with a username and password or an allowlisted source address: curl -x, python requests, rclone --socks5, or a host-side hop for a runtime that cannot dial a proxy itself. The vendor's help centre carries set-up guides for fingerprint browsers and phone apps.
- composes with: A host-side hop dials the vendor's HTTP(S) or SOCKS5 endpoint with credentials; the upstream sees an address from the vendor's pool in place of the caller's address.
- reliability: The operator named on the site is 浙江壹创云信息科技有限公司 with an ICP filing number in the footer. unverified: payment methods, the free-trial size, and the registration class of the static 'native' and 'broadcast' IPs (rung 5): no address was looked up.
- notes: Named on a Chinese-language proxy forum as '【OnesProxy】住宅代理: AI解锁/养号/多账号/VPS出口一条龙, NS专属价' with a pool of 70M+ residential IPs; a buyer thread on the same forum lists an OnesProxy address as a broadcast IP in one case.
- evidence note: Prices and product definitions are from the vendor's home page; identity and payment details are unread.
- extras:
  - rung: 5
  - rung_note: The static line sells 'native' and 'broadcast' IPs; the registration class was not checked.
- evidence:
  - [1] 2026-11-03: The static residential proxy is $4.8 per IP. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: $4.8/个
  - [1] 2026-11-03: The dynamic residential proxy is $0.88 per GB. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: $0.88/GB
  - [1] 2026-11-03: The dynamic mobile proxy is $2.38 per GB on this page. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: $2.38/GB
  - [1] 2026-11-03: Static products are billed per IP. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 按IP个数收费
  - [1] 2026-11-03: The vendor claims Cogent and Equinix partnerships and 1000+ own backbone servers. | capture: sha256:64982601067c4e97858dbdc42c2e60f76dfb0760d9063023baa55df4209ba5b5 | quote: 与Cogent、Equinix建立深度业务合作，自建超过1000台骨干网服务器。
  - [2] 2026-11-03: The sign-up page quotes the mobile product at $2.28 per GB. | capture: sha256:171048ea81a2294d4b1ad9fb17e4c27514e4f91ca3c1e5ee0877d1073294d095 | quote: $2.28/GB
- sources:
  - [1] https://www.onesproxy.com/
  - [2] https://www.onesproxy.com/register
