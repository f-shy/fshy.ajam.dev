# NetAssist IPv6

> netassist.ua | Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/netassist/ | JSON https://fshy.ajam.dev/api/v1/entity/netassist.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NetAssist IPv6 tunnel broker

- `egress/netassist-tb` | qualifies-with-caveat | evidence unverified | binding none | category IPv6 tunnel broker (Ukraine, protocol unnamed) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:52:57.443Z (live) | stale on 2026-11-19
- url https://tb.netassist.ua/reg.php
- price USD 0
- free tier: 'Please, fill in this form to get your FREE IPv6 tunnel.' The form asks for an email and 'IPv4 address of your side of the tunnel'. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1] | note: Each user of the tunnel broker is provided with an own IPv6 network of size /48.
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'We provide our service free of charge.' No traffic allowance, rate or fair-use clause is published.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: 'E-mail (will be your login)'. No card, phone or national identity is asked for. The vendor warns against hotmail and live.com addresses because mail to them is blocked. | country: None
- interface: cli
- limits note: A public IPv4 address is required at the user's end of the tunnel.
- binding note: No quota, rate or object cap is published, so nothing in the vocabulary fails at 1 TiB/month. What is unproven is whether the tunnel can carry the traffic at all, which is a protocol question rather than a limit.
- interface detail: a web form for registration and an HTTP auto-update URL for a dynamic endpoint address
- tooling: unknown until the protocol is known; iproute2 for a 6in4 tunnel, wg-quick if WireGuard exists
- composes with: would compose with a free VM the same way Route64 does, if the protocol turns out to be routable
- reliability: mail to hotmail and live.com addresses is blocked by the mail provider, so a password may never arrive; support is one address and a phone number in Kyiv.
- notes: The site is a 2011-era broker with an email login, an IPv4 endpoint field and a dynamic-IP updater, which is the classic protocol-41 shape described in the Wikipedia tunnel broker article; that is inference, not evidence.
- evidence note: The free tunnel and the IPv4 endpoint shape are documented. The protocol, the prefix size and whether WireGuard is offered at all were not established: reading the FAQ and help paths returned 404, and the account pages need a login. One vendor sentence naming the tunnel type and prefix would raise this to documented.
- extras:
  - wg_path: unknown
  - wg_detail: No page read names the tunnel protocol. WireGuard is not mentioned on the front page, the registration page, or either FAQ path tried (both returned 404). The endpoint field is an IPv4 address, which is the 6in4 or GRE shape.
  - ingress: udp
  - volume_stated: 'We provide our service free of charge.' No traffic allowance, rate or fair-use clause is published.
  - bytes_transit: yes
  - transit_note: NetAssist carries the tunnel from its Ukrainian network
- evidence:
  - [2] 2026-10-23: free registration, the auto-update endpoint for a dynamic IPv4, and 'We provide our service free of charge.'
  - [1] 2026-10-23: 'Please, fill in this form to get your FREE IPv6 tunnel.' and the two fields a new account supplies
  - [3] 2026-11-03: the vendor's company page states that each tunnel broker user gets an own IPv6 network of size /48, and that the service is free | capture: sha256:84964a32db6f4e7eb62fc200efec95eee3f7d4233885e43a971c5e6219007a87 | quote: each user of the tunnel broker is provided with his own IPv6 network of size / 48.
  - [3] 2026-11-03: the tunnel needs a public IPv4 address at the user's end | capture: sha256:84964a32db6f4e7eb62fc200efec95eee3f7d4233885e43a971c5e6219007a87 | quote: To work the tunnel, you need to have a public ("honest") IPv4 address.
  - [2] 2026-11-03: the front page states the service is free of charge; it publishes no traffic allowance, rate or fair-use clause | capture: sha256:5871043008e3832455df3816735ebf90ff3b9431ebf1c83286232a0e3d5c8df7 | quote: We provide our service free of charge.
  - [1] 2026-11-03: the registration form asks for an e-mail address that becomes the login, and for the IPv4 address of the user's side of the tunnel | capture: sha256:518d4a1dc8cd8782767dc8382acf441c710b0c5a0ef4f5a0eb61e68c644a8a04 | quote: <tr><td>E-mail (will be your login):</td><td><input type="text" name="email" value=""></td></tr>
  - [1] 2026-11-04: the tunnel is free and the registration form takes an e-mail address | capture: sha256:9e536dd503603b88fde361cf39621be5dc61be452238bafde84a12984c4c0294 | quote: Please, fill in this form to get your FREE IPv6 tunnel. Your password will be sent to your e-mail.
  - [2] 2026-11-04: the service is free of charge, no allowance published | capture: sha256:5871043008e3832455df3816735ebf90ff3b9431ebf1c83286232a0e3d5c8df7 | quote: We provide our service free of charge.
- sources:
  - [1] https://tb.netassist.ua/reg.php
  - [2] https://tb.netassist.ua/
  - [3] https://netassist.ua/en/service/ipv6

## NetAssist tunnel broker

- `egress/netassist-tunnelbroker` | qualifies-with-caveat | evidence reported | binding none | category ipv6 tunnel broker | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:53:00.067Z (live) | stale on 2026-11-19
- url https://netassist.ua/en/service/ipv6
- price USD 0
- free tier: We provide this service for free! Also, each user of the tunnel broker is provided with his own IPv6 network of size / 48. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No traffic allowance is published in available documentation; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: email | detail: https://tb.netassist.ua/ offers 'register a new user (it's FREE!)'; the login page warns 'Please, do NOT use hotmail and live.com mail accounts! They've baned us for some unknown reasons'. | country: None
- interface: cli
- binding note: Nothing in the vocabulary is stated: the /48 is free, no byte meter is published and no rate is published. The gate is a capability rather than a quota: 'To work the tunnel, you need to have a public ("honest") IPv4 address', so a client behind CGNAT cannot use it at all. Reachability is IPv6-only.
- interface detail: 'The broker's website contains a large number of different configurations for various operating systems and equipment.'
- tooling: iproute2 or any 6in4-capable router; the site publishes per-OS configurations
- composes with: pairs with any free VM that has a public IPv4, since 6in4 needs one; it is the cheapest way to give such a VM a routed /48.
- reliability: single country, single PoP; the operator states that hotmail and live.com mail domains are blocked on its side.
- notes: One PoP (Kiev), operating since 2011, page footer says 2011-2026. A BGP-enabled tunnel is available by email for clients with their own AS and address space. The company sells /48 PI space plus an ASN for EUR 300/year, which is a separate product from the free broker. The site is a 2011-era broker with an email login, an IPv4 endpoint field and a dynamic-IP updater, which is the classic protocol-41 shape described in the Wikipedia tunnel broker article; that is inference, not evidence.
- evidence note: the /48, the price and the public-IPv4 requirement are documented from the vendor page; the transport protocol is only named by the handwiki broker list, not by NetAssist, and that third-party statement is what holds the record at reported. A vendor page naming 6in4 or GRE, or a provisioned tunnel, would raise it.
- extras:
  - wg_path: none
  - wg_detail: no WireGuard option appears on any NetAssist page read.
  - ingress: tcp+udp
  - volume_stated: no traffic allowance is published anywhere or company pages read
  - bytes_transit: yes
  - transit_note: NetAssist carries the traffic on AS29632 from Kiev.
- evidence:
  - [1] 2026-10-23: 'We provide this service for free! Also, each user of the tunnel broker is provided with his own IPv6 network of size / 48.'
  - [1] 2026-10-23: 'To work the tunnel, you need to have a public ("honest") IPv4 address.'
  - [2] 2026-10-23: registration is a free web account; the site warns that hotmail and live.com addresses are blocked
  - [2] 2026-10-23: dynamic IPv4 endpoints are handled by an autochangeip URL with a sub-60-second update time
  - [3] 2026-10-23: NetAssist listed with a /48 subnet and 6in4 as the transport
  - [4] 2026-10-23: 'Please, fill in this form to get your FREE IPv6 tunnel.' and the two fields a new account supplies
  - [1] 2026-11-04:  | capture: sha256:84964a32db6f4e7eb62fc200efec95eee3f7d4233885e43a971c5e6219007a87 | quote: We provide this service for free!
- sources:
  - [1] https://netassist.ua/en/service/ipv6
  - [2] https://tb.netassist.ua/
  - [3] https://handwiki.org/wiki/List_of_IPv6_tunnel_brokers
  - [4] https://tb.netassist.ua/reg.php
