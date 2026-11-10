# AdGuard VPN

> adguard-vpn.com | Egress and tunnels, IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/adguard-vpn/ | JSON https://fshy.ajam.dev/api/v1/entity/adguard-vpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AdGuard VPN (Egress and tunnels)

- `egress/adguard-vpn` | qualifies-with-caveat | evidence documented | binding volume-quota | category vpn tunnel (hosted subscription) | tier 1 year plan, $3.99 per month billed annually ($47.88 per year); free version 3 GB per month
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:11:45.779Z (live) | stale on 2026-12-05
- url https://adguard-vpn.com/en/license.html
- price USD 3.99 per month billed annually (USD 47.88 per year) on the 1 year plan; a subscription price, not a per-TB price | parsed USD 3.99/mo
- free tier: Free version: 'Unlimited VPN traffic, compared to 3 GB per month in the free version', up to 2 devices ('compared to only 2 in the free version') and fewer server locations. Paid: all locations, unlimited speed and traffic, up to 10 devices. | unit: GB | metered on: unstated | read on: 2026-11-04 | source: [1] | note: The free version needs an AdGuard account login (email, or Google, Apple or Facebook sign-in). The paid price cards: 1 month $11.99 per month, 1 year $3.99 per month billed annually, 2 years $2.99 per month billed every two years.
- per-object cap: not applicable: an exit address, not an object | source: [1] | note: No object is stored; the constraints are the free 3 GB per month and the device counts in limits.
- retention: not applicable: a live tunnel and a rented exit address, not stored bytes | source: [2] | note: The vendor's privacy page says it does not collect logs on VPN servers; no byte retention applies.
- egress: Paid plans list 'Unlimited traffic' and 'Unlimited speed'; the free version is '3 GB per month'. No overage price exists because the paid plan is unmetered; no byte was counted through a tunnel. | metered: yes | free allowance: 3 GB per month on the free version | source: [1]
- identity: email | detail: An AdGuard account is needed even for the free version: 'first you need to log into your AdGuard account', by email or via Google, Apple ID or Facebook; 'We need your email address to register an AdGuard account and log you in.' A paid purchase takes an email address plus 'bank cards, PayPal, and cryptocurrency'. No phone number or identity document is asked on the pages read.
- interface: cli
- limits:
  - volume-quota (binding): Free version: '3 GB per month'; paid plans: 'Unlimited traffic' [1]
  - request-rate: 10 simultaneous devices on paid plans, 2 on the free version [1]
- limits note: Port forwarding and the BitTorrent rule are stated on no AdGuard VPN page read: unverified. Server locations on the paid plan are '75+' per the vendor home page.
- binding note: On the free version the 3 GB monthly traffic cap fails first; on the paid plan no byte quota is stated and the 10-device cap is the first stated limit. No rate was measured.
- interface detail: AdGuard VPN CLI (adguardvpn-cli) on Linux with a TUN mode and a SOCKS5 mode; apps for Windows, macOS, Android and iOS and browser extensions. The SOCKS5 mode is a local proxy on 127.0.0.1:1080 by default; the vendor documents no remote SOCKS5 endpoint with credentials.
- tooling: The vendor's CLI on a Linux machine gives a local SOCKS5 proxy (TCP and UDP) that any client on that machine can use; the apps and extensions cover the other platforms. The CLI's protocol option is HTTP2, QUIC or automatic.
- composes with: A compute node runs the CLI in SOCKS5 mode and sends requests to 127.0.0.1:1080, so they leave at the chosen location's address; a Worker cannot reach that loopback proxy, so it needs a node in front of it.
- reliability: The 1 year card shows a struck-through $11.99 per month and a '-67%' badge, so the $3.99 may be a promotional rate that the page can change. unverified: no exit-IP registry class was measured.
- notes: Derived: $3.99 per month x 12 months = $47.88 per year. The 1 year card shows a struck-through $11.99 per month and a '-67%' badge. The protocol is the vendor's own, TrustTunnel, over HTTP/2 or HTTP/3; there is no WireGuard or OpenVPN option named on the pages read. Port forwarding: unverified: no AdGuard VPN page read states port forwarding. BitTorrent rule: unverified: no AdGuard VPN page read states a BitTorrent or P2P rule.
- evidence note: Documented from the vendor's licence page, home page and knowledge base as served. Measured would need an account, a tunnel brought up in each mode and a byte count against the 3 GB free cap.
- evidence:
  - [3] 2026-11-04: The 1 year plan is $3.99 per month (struck-through $11.99 per month); the 2 years plan is $2.99 per month; the 1 month plan is $11.99 per month. | capture: sha256:eb7ae61ef280e375a781814005acabfef9060d0aab9a908e85fc243236354aba | quote: $3.99/month
  - [3] 2026-11-04: The 1 year price is billed annually, i.e. $3.99 x 12 = $47.88 per year; the vendor's own blog states the same yearly total of $47.88. | capture: sha256:70c2adbd9116f39cfff92547a70c331348de609d3743289c3dbf0b2ae27b1ff2 | quote: billed annually
  - [3] 2026-11-04: The paid plans include all locations, unlimited speed and unlimited traffic. | capture: sha256:465fbe060a3952e32c009958943430484ef6ad03972191956328a8a10cb59750 | quote: Unlimited traffic
  - [1] 2026-11-04: The free version is limited to 3 GB of VPN traffic per month; the paid version is unlimited. | capture: sha256:27b0d921ee445f3b317e0600f8ebafe8a1d84511e23120d51a908dc10a6bbde5 | quote: Unlimited VPN traffic, compared to 3 GB per month in the free version
  - [1] 2026-11-04: Paid allows 10 simultaneous devices; the free version 2. | capture: sha256:27b0d921ee445f3b317e0600f8ebafe8a1d84511e23120d51a908dc10a6bbde5 | quote: AdGuard VPN can be used on up to 10 devices simultaneously, compared to only 2 in the free version
  - [3] 2026-11-04: Payment methods: bank cards, PayPal and cryptocurrency. | capture: sha256:465fbe060a3952e32c009958943430484ef6ad03972191956328a8a10cb59750 | quote: We accept bank cards, PayPal, and cryptocurrency for payments.
  - [3] 2026-11-04: 30-day money-back guarantee on 1-year and 2-year plans; monthly plans are non-refundable. | capture: sha256:465fbe060a3952e32c009958943430484ef6ad03972191956328a8a10cb59750 | quote: For 1-year and 2-year subscriptions, we offer a 30-day money-back guarantee.
  - [4] 2026-11-04: The apps need a login to an AdGuard account (or Google, Apple or Facebook sign-in). | capture: sha256:2bd9e9f05cd4b3fd1495d19c805c3d2ce62ee69c39bd41beb384f77b37e00c01 | quote: To use AdGuard VPN for iOS, first you need to log into your [AdGuard account](https://adguardaccount.com/).
  - [5] 2026-11-04: Buying on the website needs an email address that is associated with the subscription. | capture: sha256:1708e875af35d8f63e33c8a621544fbbad4953387ea7aec5ff360a608ce39ae3 | quote: enter the email address that will be associated with your subscription
  - [6] 2026-11-04: The email address is what registers the AdGuard account. | capture: sha256:a524bfec2505beaf79891fa2d5ecdaf99f6cd4ab1fbdb7ff4f1e56a3e1929371 | quote: We need your email address to register an AdGuard account and log you in.
  - [7] 2026-11-04: The protocol is TrustTunnel, an open-source VPN protocol that 'disguises itself as normal traffic' (obfuscation). | capture: sha256:fd9505371c4c4769ed8d05ad96ceeac5393e46b7ecae2f38ae7c0e46b69eee47 | quote: we use [TrustTunnel](https://trusttunnel.org/) â€” a modern, stealthy, and fast open-source VPN protocol developed by us. It disguises itself as normal traffic, so it is much more difficult to track and block it.
  - [8] 2026-11-04: The protocol can be set to HTTP2, QUIC or automatic: the tunnel rides HTTP/2 over TLS or HTTP/3 over QUIC, and QUIC is UDP-based. | capture: sha256:5be55b10ba782ae18773975e1c77e57fd37311b54900cb265a0aabe3e840690a | quote: To set the protocol used by AdGuard VPN (HTTP2, QUIC, or automatic choice between them), type one of the commands, depending on your choice:
  - [8] 2026-11-04: The only SOCKS5 documented is a local proxy on the user's machine (127.0.0.1:1080) in the CLI's SOCKS5 mode, not a remote endpoint with credentials. | capture: sha256:5be55b10ba782ae18773975e1c77e57fd37311b54900cb265a0aabe3e840690a | quote: Starts a local SOCKS5 proxy that by default listens on 127.0.0.1:1080 (configurable via the `set-socks-host` and `set-socks-port` commands).
  - [8] 2026-11-04: In the CLI's SOCKS5 mode both TCP and UDP proxying are provided. | capture: sha256:5be55b10ba782ae18773975e1c77e57fd37311b54900cb265a0aabe3e840690a | quote: AdGuard VPN CLI provides both TCP and UDP proxying in SOCKS5 mode.
- sources:
  - [1] https://adguard-vpn.com/
  - [2] https://adguard-vpn.com/en/privacy.html
  - [3] https://adguard-vpn.com/en/license.html
  - [4] https://adguard-vpn.com/kb/adguard-vpn-for-ios/overview/
  - [5] https://adguard-vpn.com/kb/general/subscription/
  - [6] https://adguard-vpn.com/en/privacy/windows.html
  - [7] https://adguard-vpn.com/kb/
  - [8] https://adguard-vpn.com/kb/adguard-vpn-for-linux/settings/

## AdGuard VPN (IP and proxies)

- `ip-proxy/adguard-vpn` | qualifies-with-caveat | evidence documented | binding volume-quota | category VPN subscription (exit source) | tier 1 year plan, $3.99 per month billed annually ($47.88 per year); free version 3 GB per month
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:00:31.322Z (live) | stale on 2026-12-05
- url https://adguard-vpn.com/en/license.html
- price USD 3.99 per month billed annually (USD 47.88 per year) on the 1 year plan; a subscription price, not a per-TB price | parsed USD 3.99/mo
- duplicate of `egress/adguard-vpn`
- free tier: Free version: 'Unlimited VPN traffic, compared to 3 GB per month in the free version', up to 2 devices ('compared to only 2 in the free version') and fewer server locations. Paid: all locations, unlimited speed and traffic, up to 10 devices. | unit: GB | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The free version needs an AdGuard account login (email, or Google, Apple or Facebook sign-in). The paid price cards: 1 month $11.99 per month, 1 year $3.99 per month billed annually, 2 years $2.99 per month billed every two years.
- per-object cap: not applicable: an exit address, not an object | source: [1] | note: No object is stored; the constraints are the free 3 GB per month and the device counts in limits.
- retention: not applicable: a live tunnel and a rented exit address, not stored bytes | source: [2] | note: The vendor's privacy page says it does not collect logs on VPN servers; no byte retention applies.
- egress: Paid plans list 'Unlimited traffic' and 'Unlimited speed'; the free version is '3 GB per month'. No overage price exists because the paid plan is unmetered; no byte was counted through a tunnel. | metered: yes | free allowance: 3 GB per month on the free version | source: [1]
- identity: email | detail: An AdGuard account is needed even for the free version: 'first you need to log into your AdGuard account', by email or via Google, Apple ID or Facebook; 'We need your email address to register an AdGuard account and log you in.' A paid purchase takes an email address plus 'bank cards, PayPal, and cryptocurrency'. No phone number or identity document is asked on the pages read.
- interface: cli
- limits:
  - volume-quota (binding): Free version: '3 GB per month'; paid plans: 'Unlimited traffic' [1]
  - request-rate: 10 simultaneous devices on paid plans, 2 on the free version [1]
- limits note: Server locations on the paid plan are '75+' per the vendor home page.
- binding note: On the free version the 3 GB monthly traffic cap fails first; on the paid plan no byte quota is stated and the 10-device cap is the first stated limit. No rate was measured.
- interface detail: AdGuard VPN CLI (adguardvpn-cli) on Linux with a TUN mode and a SOCKS5 mode; apps for Windows, macOS, Android and iOS and browser extensions. The SOCKS5 mode is a local proxy on 127.0.0.1:1080 by default; the vendor documents no remote SOCKS5 endpoint with credentials.
- tooling: The vendor's CLI on a Linux machine gives a local SOCKS5 proxy (TCP and UDP) that any client on that machine can use; the apps and extensions cover the other platforms. The CLI's protocol option is HTTP2, QUIC or automatic.
- composes with: A compute node runs the CLI in SOCKS5 mode and sends requests to 127.0.0.1:1080, so they leave at the chosen location's address; a Worker cannot reach that loopback proxy, so it needs a node in front of it.
- reliability: The default page extraction of the licence page returned no price cards (they load by script); the prices above come from a second reader of the same page, and the vendor blog gives the same $47.88 yearly total. A third reader returned the same page in Korean won, so the displayed currency follows the reader's location. unverified: no exit-IP registry class was measured.
- notes: Duplicate of egress/adguard-vpn, which holds the offer.
- evidence note: Documented from the vendor's licence page, home page and knowledge base as served. Measured would need an account, a tunnel brought up in each mode and a byte count against the 3 GB free cap.
- evidence:
  - [3] 2026-11-03: The 1 year plan is $3.99 per month (struck-through $11.99 per month); the 2 years plan is $2.99 per month; the 1 month plan is $11.99 per month. | capture: sha256:eb7ae61ef280e375a781814005acabfef9060d0aab9a908e85fc243236354aba | quote: $3.99/month
  - [3] 2026-11-03: The 1 year price is billed annually, i.e. $3.99 x 12 = $47.88 per year; the vendor's own blog states the same yearly total of $47.88. | capture: sha256:eb7ae61ef280e375a781814005acabfef9060d0aab9a908e85fc243236354aba | quote: billed annually
  - [3] 2026-11-03: The paid plans include all locations, unlimited speed and unlimited traffic. | capture: sha256:eb7ae61ef280e375a781814005acabfef9060d0aab9a908e85fc243236354aba | quote: Unlimited traffic
  - [1] 2026-11-03: The free version is limited to 3 GB of VPN traffic per month; the paid version is unlimited. | capture: sha256:27b0d921ee445f3b317e0600f8ebafe8a1d84511e23120d51a908dc10a6bbde5 | quote: Unlimited VPN traffic, compared to 3 GB per month in the free version
  - [1] 2026-11-03: Paid allows 10 simultaneous devices; the free version 2. | capture: sha256:27b0d921ee445f3b317e0600f8ebafe8a1d84511e23120d51a908dc10a6bbde5 | quote: AdGuard VPN can be used on up to 10 devices simultaneously, compared to only 2 in the free version
  - [3] 2026-11-03: Payment methods: bank cards, PayPal and cryptocurrency. | capture: sha256:eb7ae61ef280e375a781814005acabfef9060d0aab9a908e85fc243236354aba | quote: We accept bank cards, PayPal, and cryptocurrency for payments.
  - [3] 2026-11-03: 30-day money-back guarantee on 1-year and 2-year plans; monthly plans are non-refundable. | capture: sha256:eb7ae61ef280e375a781814005acabfef9060d0aab9a908e85fc243236354aba | quote: For 1-year and 2-year subscriptions, we offer a 30-day money-back guarantee.
  - [4] 2026-11-03: The apps need a login to an AdGuard account (or Google, Apple or Facebook sign-in). | capture: sha256:2bd9e9f05cd4b3fd1495d19c805c3d2ce62ee69c39bd41beb384f77b37e00c01 | quote: To use AdGuard VPN for iOS, first you need to log into your [AdGuard account](https://adguardaccount.com/).
  - [5] 2026-11-03: Buying on the website needs an email address that is associated with the subscription. | capture: sha256:1708e875af35d8f63e33c8a621544fbbad4953387ea7aec5ff360a608ce39ae3 | quote: enter the email address that will be associated with your subscription
  - [6] 2026-11-03: The email address is what registers the AdGuard account. | capture: sha256:a524bfec2505beaf79891fa2d5ecdaf99f6cd4ab1fbdb7ff4f1e56a3e1929371 | quote: We need your email address to register an AdGuard account and log you in.
  - [7] 2026-11-03: The protocol is TrustTunnel, an open-source VPN protocol that 'disguises itself as normal traffic' (obfuscation). | capture: sha256:fd9505371c4c4769ed8d05ad96ceeac5393e46b7ecae2f38ae7c0e46b69eee47 | quote: we use [TrustTunnel](https://trusttunnel.org/) — a modern, stealthy, and fast open-source VPN protocol developed by us. It disguises itself as normal traffic, so it is much more difficult to track and block it.
  - [8] 2026-11-03: The protocol can be set to HTTP2, QUIC or automatic: the tunnel rides HTTP/2 over TLS or HTTP/3 over QUIC, and QUIC is UDP-based. | capture: sha256:5be55b10ba782ae18773975e1c77e57fd37311b54900cb265a0aabe3e840690a | quote: To set the protocol used by AdGuard VPN (HTTP2, QUIC, or automatic choice between them), type one of the commands, depending on your choice:
  - [8] 2026-11-03: The only SOCKS5 documented is a local proxy on the user's machine (127.0.0.1:1080) in the CLI's SOCKS5 mode, not a remote endpoint with credentials. | capture: sha256:5be55b10ba782ae18773975e1c77e57fd37311b54900cb265a0aabe3e840690a | quote: Starts a local SOCKS5 proxy that by default listens on 127.0.0.1:1080 (configurable via the `set-socks-host` and `set-socks-port` commands).
  - [8] 2026-11-03: In the CLI's SOCKS5 mode both TCP and UDP proxying are provided. | capture: sha256:5be55b10ba782ae18773975e1c77e57fd37311b54900cb265a0aabe3e840690a | quote: AdGuard VPN CLI provides both TCP and UDP proxying in SOCKS5 mode.
  - [3] 2026-11-04: The vendor license page lists the VPN plan that both records cite. | capture: sha256:d2a3f9f083f644e6fd4cdf7a2939772257516afb8ac99a44dcb43a496c09fc8a | quote: unlimited speed and traffic, the ability to connect up to 10 devices
- sources:
  - [1] https://adguard-vpn.com/
  - [2] https://adguard-vpn.com/en/privacy.html
  - [3] https://adguard-vpn.com/en/license.html
  - [4] https://adguard-vpn.com/kb/adguard-vpn-for-ios/overview/
  - [5] https://adguard-vpn.com/kb/general/subscription/
  - [6] https://adguard-vpn.com/en/privacy/windows.html
  - [7] https://adguard-vpn.com/kb/
  - [8] https://adguard-vpn.com/kb/adguard-vpn-for-linux/settings/
