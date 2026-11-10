# ZoogVPN

> zoogvpn.com | Egress and tunnels, IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/zoogvpn/ | JSON https://fshy.ajam.dev/api/v1/entity/zoogvpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ZoogVPN (Egress and tunnels)

- `egress/zoogvpn` | fails-quota | evidence documented | binding volume-quota | category vpn tunnel (hosted subscription) | tier Premium, 1 year
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:11:45.779Z (live) | stale on 2026-12-05
- url https://zoogvpn.com/pricing
- price USD 39.99 billed for 12 months; a subscription price, not a per-TB price
- free tier: A Free plan exists: '10 GB of monthly traffic', 1 device, 5 locations, 128-bit encryption and no dedicated IP. Premium 1 year is listed at 'USD 3.39 /mo' and 'Billed $39.99 for 12 months' (against USD 9.99 a month); 1 month is $9.99 and 2 years is $59.99 for 27 months. | unit: GB | metered on: unstated | read on: 2026-11-04 | source: [1] | note: The free plan's traffic direction is not stated ('10 GB of monthly traffic'). The record is priced at the cheapest yearly Premium plan.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a tunnel, not stored bytes | source: [1]
- egress: Premium: 'Unlimited traffic (bandwidth)'. Free: '10 GB of monthly traffic' with limited speed and possible congestion. | metered: yes | free allowance: free plan: 10 GB a month; Premium: unlimited | source: [1]
- identity: email | detail: An email address and a password: 'you will need to provide your email address and password only for account management purposes'; the privacy notice says 'We only collect your email address (which can be a disposable one)'. The free plan needs a sign-up; no card is stated for it on the pages read.
- interface: unknown
- limits:
  - volume-quota (binding): free plan: 10 GB of monthly traffic; Premium: unlimited traffic [1]
  - request-rate: 1 device on the free plan; up to 10 devices on Premium [1]
- limits note: The device counts are filed under request-rate because the vocabulary has no concurrent-connection kind. P2P is limited to the servers marked P2P.
- binding note: On the free plan the 10 GB monthly traffic quota is what fails first for any bulk workload; Premium states unlimited traffic, so the quota does not bind on the paid tier this record is priced at.
- interface detail: A tunnel and a proxy through apps (Windows, macOS, iOS, Android, FireTV, Linux and routers). Protocols in the vendor's table: WireGuard, IKEv2/IPSec, OpenVPN (UDP), OpenVPN (TCP), Shadow and ZoogTLS; the pricing page also names PPTP and L2TP/IPSec. UDP: yes, OpenVPN (UDP). Port forwarding: unverified: no page read states it. SOCKS5: yes, 'Several ZoogVPN servers allow you to connect using the SOCKS5 proxy technology.' Obfuscation: the Shadow protocol disguises VPN traffic as HTTPS. BitTorrent: allowed on servers marked 'P2P'; the terms say P2P is only permitted on those servers.
- tooling: The vendor's apps, or OpenVPN, IKEv2 or WireGuard clients; SOCKS5 on selected servers.
- composes with: A tunnel or SOCKS5 exit with a free 10 GB tier and an unlimited paid tier; the upstream sees a shared VPN address.
- reliability: The free plan is described by the vendor as one that 'may be interrupted or blocked', with limited speed and possible congestion.
- notes: Cheapest yearly price: 'Billed $39.99 for 12 months' on the pricing page. The 2-year plan is $59.99 for 27 months. A free plan with 10 GB a month is also offered.
- evidence note: Documented: price, free quota, protocols, UDP, SOCKS5, obfuscation, sign-up and BitTorrent lines are quoted from the vendor's own pages. Nothing was connected through the service. Port forwarding is unverified because no page read states it.
- evidence:
  - [1] 2026-11-04: The 1-year Premium plan is USD 39.99. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Billed $39.99 for 12 months
  - [1] 2026-11-04: The free plan is capped at 10 GB a month. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: 10 GB of monthly traffic
  - [1] 2026-11-04: Premium has unlimited traffic. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Unlimited traffic (bandwidth)
  - [1] 2026-11-04: Premium allows 10 devices. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Up to 10 devices
  - [1] 2026-11-04: Premium lists P2P and torrenting. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Full P2P & torrenting
  - [2] 2026-11-04: WireGuard is offered in-app. | capture: sha256:56fc1f8b2de5991bfe5da8d820eda917e07a0c9d12ea45d4b72fefc6b74d17c5 | quote: | WireGuard | Very fast | Very strong | Good | Good | Good | Good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [2] 2026-11-04: OpenVPN over UDP is offered. | capture: sha256:56fc1f8b2de5991bfe5da8d820eda917e07a0c9d12ea45d4b72fefc6b74d17c5 | quote: | OpenVPN (UDP) | Fast | Very strong | Good | Good | Good | Good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [2] 2026-11-04: OpenVPN over TCP is offered. | capture: sha256:56fc1f8b2de5991bfe5da8d820eda917e07a0c9d12ea45d4b72fefc6b74d17c5 | quote: | OpenVPN (TCP) | Moderate | Very strong | Very stable | Good | Good | Good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [2] 2026-11-04: The Shadow protocol is offered in-app. | capture: sha256:56fc1f8b2de5991bfe5da8d820eda917e07a0c9d12ea45d4b72fefc6b74d17c5 | quote: | Shadow | Moderate | Strong | Very stable | Very good | Very good | Very good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [3] 2026-11-04: Obfuscation: Shadow disguises VPN traffic as HTTPS. | capture: sha256:b74eba79b52c171c1f9b341fd1b57f3fc0e7aaa6519bc4bdfcd603e7cc8fdcc5 | quote: Its performance lies in disguising VPN traffic, which is undetectable from regular HTTPS traffic.
  - [4] 2026-11-04: SOCKS5 is offered on several servers. | capture: sha256:e1351f3ded45e8c104d705a0a3c744d7bde60ef1499f9514832f630b8b7b18e9 | quote: Several ZoogVPN servers allow you to connect using the SOCKS5 proxy technology.
  - [4] 2026-11-04: Torrenting runs on servers marked P2P. | capture: sha256:e1351f3ded45e8c104d705a0a3c744d7bde60ef1499f9514832f630b8b7b18e9 | quote: Download torrents with peace of mind and confidence on dozens of torrent friendly, fast and unlimited VPN servers marked as â€˜P2Pâ€™.
  - [5] 2026-11-04: P2P is limited to listed servers. | capture: sha256:7cdfe98d3e08c4d47d01e7e2305d240e851022f4c3ebbfcc54092e607d070968 | quote: this activity is only permitted on certain VPN servers which are listed on [VPN network](https://zoogvpn.com/network/) page
  - [5] 2026-11-04: Registration needs an email and a password. | capture: sha256:7cdfe98d3e08c4d47d01e7e2305d240e851022f4c3ebbfcc54092e607d070968 | quote: you will need to provide your email address and password only for account management purposes
  - [6] 2026-11-04: Only an email address is collected. | capture: sha256:821f3b8487955b0371fa2c2a01b0988a3ea326c6892c03667b0c20f6a53ff789 | quote: We only collect your email address (which can be a disposable one) because of the nature of our service.
- sources:
  - [1] https://zoogvpn.com/pricing
  - [2] https://zoogvpn.com/faq/
  - [3] https://zoogvpn.com/features/zoog-shadowing/
  - [4] https://zoogvpn.com/features/
  - [5] https://zoogvpn.com/terms/
  - [6] https://zoogvpn.com/privacy/

## ZoogVPN (IP and proxies)

- `ip-proxy/zoogvpn` | fails-quota | evidence documented | binding volume-quota | category VPN subscription (exit source) | tier Premium, 1 year
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:58:00.000Z (live) | stale on 2026-12-05
- url https://zoogvpn.com/pricing
- price USD 39.99 billed for 12 months; a subscription price, not a per-TB price
- duplicate of `egress/zoogvpn`
- free tier: A Free plan exists: '10 GB of monthly traffic', 1 device, 5 locations, 128-bit encryption and no dedicated IP. Premium 1 year is listed at 'USD 3.39 /mo' and 'Billed $39.99 for 12 months' (against USD 9.99 a month); 1 month is $9.99 and 2 years is $59.99 for 27 months. | unit: GB | metered on: unstated | read on: 2026-11-04 | source: [1] | note: The free plan's traffic direction is not stated ('10 GB of monthly traffic'). The record is priced at the cheapest yearly Premium plan.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a tunnel, not stored bytes | source: [1]
- egress: Premium: 'Unlimited traffic (bandwidth)'. Free: '10 GB of monthly traffic' with limited speed and possible congestion. | metered: yes | free allowance: free plan: 10 GB a month; Premium: unlimited | source: [1]
- identity: email | detail: An email address and a password: 'you will need to provide your email address and password only for account management purposes'; the privacy notice says 'We only collect your email address (which can be a disposable one)'. The free plan needs a sign-up; no card is stated for it on the pages read.
- interface: unknown
- limits:
  - volume-quota (binding): free plan: 10 GB of monthly traffic; Premium: unlimited traffic [1]
  - request-rate: 1 device on the free plan; up to 10 devices on Premium [1]
- limits note: The device counts are filed under request-rate because the vocabulary has no concurrent-connection kind. P2P is limited to the servers marked P2P.
- binding note: On the free plan the 10 GB monthly traffic quota is what fails first for any bulk workload; Premium states unlimited traffic, so the quota does not bind on the paid tier this record is priced at.
- interface detail: A tunnel and a proxy through apps (Windows, macOS, iOS, Android, FireTV, Linux and routers). Protocols in the vendor's table: WireGuard, IKEv2/IPSec, OpenVPN (UDP), OpenVPN (TCP), Shadow and ZoogTLS; the pricing page also names PPTP and L2TP/IPSec. UDP: yes, OpenVPN (UDP). Port forwarding: unverified: no page read states it. SOCKS5: yes, 'Several ZoogVPN servers allow you to connect using the SOCKS5 proxy technology.' Obfuscation: the Shadow protocol disguises VPN traffic as HTTPS. BitTorrent: allowed on servers marked 'P2P'; the terms say P2P is only permitted on those servers.
- tooling: The vendor's apps, or OpenVPN, IKEv2 or WireGuard clients; SOCKS5 on selected servers.
- composes with: A tunnel or SOCKS5 exit with a free 10 GB tier and an unlimited paid tier; the upstream sees a shared VPN address.
- reliability: The free plan is described by the vendor as one that 'may be interrupted or blocked', with limited speed and possible congestion.
- notes: Duplicate of egress/zoogvpn, which holds the offer; both records cite the same vendor page.
- evidence note: Documented: price, free quota, protocols, UDP, SOCKS5, obfuscation, sign-up and BitTorrent lines are quoted from the vendor's own pages. Nothing was connected through the service. Port forwarding is unverified because no page read states it.
- evidence:
  - [1] 2026-11-04: The 1-year Premium plan is USD 39.99. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Billed $39.99 for 12 months
  - [1] 2026-11-04: The free plan is capped at 10 GB a month. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: 10 GB of monthly traffic
  - [1] 2026-11-04: Premium has unlimited traffic. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Unlimited traffic (bandwidth)
  - [1] 2026-11-04: Premium allows 10 devices. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Up to 10 devices
  - [1] 2026-11-04: Premium lists P2P and torrenting. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Full P2P & torrenting
  - [2] 2026-11-04: WireGuard is offered in-app. | capture: sha256:ced9870ac97818fd92dc9a04e6b62ded38b9800e36399f9059cc5c4475ede964 | quote: | WireGuard | Very fast | Very strong | Good | Good | Good | Good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [2] 2026-11-04: OpenVPN over UDP is offered. | capture: sha256:ced9870ac97818fd92dc9a04e6b62ded38b9800e36399f9059cc5c4475ede964 | quote: | OpenVPN (UDP) | Fast | Very strong | Good | Good | Good | Good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [2] 2026-11-04: OpenVPN over TCP is offered. | capture: sha256:ced9870ac97818fd92dc9a04e6b62ded38b9800e36399f9059cc5c4475ede964 | quote: | OpenVPN (TCP) | Moderate | Very strong | Very stable | Good | Good | Good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [2] 2026-11-04: The Shadow protocol is offered in-app. | capture: sha256:ced9870ac97818fd92dc9a04e6b62ded38b9800e36399f9059cc5c4475ede964 | quote: | Shadow | Moderate | Strong | Very stable | Very good | Very good | Very good | Yes | Windows, macOS, iOS, Android, Linux, Routers |
  - [3] 2026-11-04: Obfuscation: Shadow disguises VPN traffic as HTTPS. | capture: sha256:b74eba79b52c171c1f9b341fd1b57f3fc0e7aaa6519bc4bdfcd603e7cc8fdcc5 | quote: Its performance lies in disguising VPN traffic, which is undetectable from regular HTTPS traffic.
  - [4] 2026-11-04: SOCKS5 is offered on several servers. | capture: sha256:e1351f3ded45e8c104d705a0a3c744d7bde60ef1499f9514832f630b8b7b18e9 | quote: Several ZoogVPN servers allow you to connect using the SOCKS5 proxy technology.
  - [4] 2026-11-04: Torrenting runs on servers marked P2P. | capture: sha256:e1351f3ded45e8c104d705a0a3c744d7bde60ef1499f9514832f630b8b7b18e9 | quote: Download torrents with peace of mind and confidence on dozens of torrent friendly, fast and unlimited VPN servers marked as ‘P2P’.
  - [5] 2026-11-04: P2P is limited to listed servers. | capture: sha256:e112b5ef74b14277008bebb05189ec6b9eab11320aae855407604dc39318dd5f | quote: this activity is only permitted on certain VPN servers which are listed on [VPN network](https://zoogvpn.com/network/) page
  - [5] 2026-11-04: Registration needs an email and a password. | capture: sha256:e112b5ef74b14277008bebb05189ec6b9eab11320aae855407604dc39318dd5f | quote: you will need to provide your email address and password only for account management purposes
  - [6] 2026-11-04: Only an email address is collected. | capture: sha256:821f3b8487955b0371fa2c2a01b0988a3ea326c6892c03667b0c20f6a53ff789 | quote: We only collect your email address (which can be a disposable one) because of the nature of our service.
  - [1] 2026-11-04: A standing Free plan exists and is capped at 10 GB of monthly traffic, so the offer is not paid-only. | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: 10 GB of monthly traffic
  - [1] 2026-11-04: the ZoogVPN pricing page lists the plan both records describe | capture: sha256:773547a7dc33508c7bf5b8abc7ee32d8179886ccf4464e6ead465e30d4265eae | quote: Billed $39.99 for 12 months
- sources:
  - [1] https://zoogvpn.com/pricing
  - [2] https://zoogvpn.com/faq/
  - [3] https://zoogvpn.com/features/zoog-shadowing/
  - [4] https://zoogvpn.com/features/
  - [5] https://zoogvpn.com/terms/
  - [6] https://zoogvpn.com/privacy/
