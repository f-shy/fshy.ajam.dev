# IPFLY

> ipfly.net | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipfly/ | JSON https://fshy.ajam.dev/api/v1/entity/ipfly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPFLY (Chengdu Smart Mapping Technology)

- `ip-proxy/ipfly` | paid-only | evidence documented | binding volume-quota | category rotating residential proxy | tier Rotating Residential (per GB) and ISP Proxies (per IP)
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:35:31.960Z (live) | stale on 2026-12-04
- url https://www.ipfly.net/en/
- price not a per-TB-month product: rotating residential from 1 USD per GB; ISP from 2.5 USD per IP; datacenter from 4.5 USD per IP.
- free tier: No standing free tier with a stated size. The home page carries 'Free Trial for New Users' beside 'Buy Now'; the trial's size and duration are not stated on the pages read. | unit: none | metered on: none | read on: 2026-11-03 | source: [1] | note: The sign-up and console pages did not return readable content.
- per-object cap: not applicable: a traffic plan or an address, not an object | source: [1]
- retention: Rotating residential traffic: 'Traffic Never Expires'. ISP proxies: 'Exclusive IP' for the validity period with 'Unlimited Bandwidth'. | source: [2]
- egress: Residential is 'Pay-As-You-Go' per GB; ISP proxies and datacenter proxies are priced per IP, the ISP page stating 'Unlimited Bandwidth'. | metered: yes | free allowance: a trial of unstated size for new users | source: [2]
- identity: email | detail: The terms state 'You may use the email address you provided or confirmed, or other methods permitted by IPFLY, to log in to the website.' No ID document or card is requested before checkout on the pages read; the payment-method icons on the page footer are PayPal, Visa, USDT and Alipay. The registration form itself was not readable.
- interface: unknown
- limits:
  - volume-quota (binding): rotating residential from 1 USD per GB, traffic never expires; ISP proxies from 2.5 USD per IP; datacenter proxies from 4.5 USD per IP [1]
- limits note: The vendor also publishes time-limited sale pages with lower promotional prices; they are not used as the price. Pool claims: more than 90 million residential IPs in 190+ regions, 'Unlimited concurrent requests', 0.6 s average response.
- binding note: The purchased GB is the quantity that runs out; the ISP product is per IP and has no byte limit.
- interface detail: Forward proxy ('Full protocol support'), API integration and a proxy manager are advertised. The protocols were not enumerated on the pricing pages read.
- tooling: Any client that speaks an HTTP or SOCKS5 proxy with credentials, or the vendor's API.
- composes with: The vendor's gateway is an HTTP or SOCKS5 forward proxy, so it is dialled from a host that can open outbound proxy connections (a rented or free virtual machine); the upstream then sees an address from the vendor's pool instead of the host's own.
- reliability: The refund agreement says 'refunds are not supported in principle' once delivery is complete, with a 24-hour exception for a total technical failure. The vendor publishes 99.9% availability; unverified here.
- notes: Three product lines: rotating residential, ISP and datacenter. The operator is named in the footer as Chengdu Smart Mapping Technology Co., Ltd.
- evidence note: Prices and terms are quoted from the vendor's own pages read on 2026-11-03. The registration form, the trial size, the protocol list and the registration class of the ISP addresses were not read, and no address was sampled, so rung 5 is unverified.
- extras:
  - rung: 2
  - rung_note: A rotating residential pool presents a different single address per session (rung 2); the ISP product would reach rung 5 only if its addresses are registered to an access network, which no page read shows and no address was sampled.
  - pool_claim: more than 90 million residential IPs, 190+ regions (vendor claim)
- evidence:
  - [2] 2026-11-03: Rotating residential starts at 1 USD per GB, pay as you go, with traffic that never expires. | capture: sha256:edb1ebbe3440ce74b7186adc91e793994b09460eeb0dee7317dcd4c6d4a7f01f | quote: ## Rotating Residential Proxy PricingFrom $1/GB, Pay-As-You-Go, Traffic Never Expires
  - [3] 2026-11-03: ISP proxies start at 2.5 USD per IP with unlimited bandwidth. | capture: sha256:51246ae52873b50c24d403f0037f2eecea2be486b264416ffad31252309d5fe2 | quote: ## Static Residential Proxy (ISP Proxy) PricingDedicated IPs from $2.5/IP, Unlimited Bandwidth
  - [1] 2026-11-03: The pool claim is more than 90 million residential IPs in more than 190 regions; the page also lists datacenter proxies from 4.5 USD per IP. | capture: sha256:7f36157e18249172afd0f793dbf183ffc9a0fd71d52aeb07ced223e2b385e687 | quote: The world's leading proxy network with more than 90 million real residential IP addresses from more than 190 regions
  - [1] 2026-11-03: A free trial for new users is offered beside the purchase button; its size is not stated. | capture: sha256:7f36157e18249172afd0f793dbf183ffc9a0fd71d52aeb07ced223e2b385e687 | quote: Buy NowFree Trial for New Users
  - [4] 2026-11-03: Accounts are keyed to an email address. | capture: sha256:11347275de791999a812b514563fe4a5b4babf96e253e3899397bcf649f2dd45 | quote: You may use the email address you provided or confirmed, or other methods permitted by IPFLY, to log in to the website.
  - [5] 2026-11-03: Once delivery is complete, refunds are not supported in principle, with a 24-hour exception for a total technical failure. | capture: sha256:328785c05003e53f6f26ecfab627144271ab8126034342dc1dbcbed6638f2efc | quote: refunds are not supported in principle
  - [6] 2026-11-03: The footer lists PayPal, Visa, USDT and Alipay payment icons. | capture: sha256:fe7e486a32fb01a761b49cddf45df977b230dc224b7c1224ffe91728898ec1fb | quote: paypal payment iconvisa payment iconusdt payment iconalipay payment icon
- sources:
  - [1] https://www.ipfly.net/en/
  - [2] https://www.ipfly.net/resident-price/
  - [3] https://www.ipfly.net/isp-price/
  - [4] https://www.ipfly.net/agreement/
  - [5] https://www.ipfly.net/en/refund-agreement/
  - [6] https://www.ipfly.net/en/faq/
