# OVPN

> ovpn.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ovpn/ | JSON https://fshy.ajam.dev/api/v1/entity/ovpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## OVPN

- `egress/ovpn` | paid-only | evidence documented | binding none | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:29:23.994Z (live) | stale on 2026-12-05
- url https://support.ovpn.com/hc/en-us/articles/18731795296788-Opening-Ports
- price EUR 12 per month; EUR 4.99 per month on 12 months; EUR 4.22 per month on 36 months | parsed USD 4.75/mo
- free tier: No free tier. Pricing page 2026-11-03 (EUR): 1 month 12 EUR per month, 12 months 4.99 EUR per month, 36 months 4.22 EUR per month, each row carrying Port forwarding and a 10-day money-back guarantee. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Our subscriptions contain unlimited bandwidth and traffic which means you can stream as much as you want.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: Checkout collects an email: We value your privacy, the email is required for payment and shared only with the provider for tax purposes. | country: None
- interface: cli
- limits:
  - volume-quota: none stated; subscriptions contain unlimited bandwidth and traffic [3]
  - write-gated: 7 ports per account, each between 49152 and 65535, and the connection must be re-established after a port is opened [2]
- binding note: No byte quota exists to hit at 1 TiB/month. What arrives first is the port range: 49152-65535 only, 7 ports, and a reconnect after each change. A service that must listen below 49152 needs the Public IPv4 add-on.
- interface detail: Account web UI for port forwarding and config download; no public API for port reservation found in the read pages.
- tooling: wg-quick from downloaded configs; ports set in the web profile and each can be TCP, UDP, or TCP and UDP. Protocols: OpenVPN over UDP or TCP (UDP recommended) and WireGuard. SOCKS5 endpoint, obfuscation and the BitTorrent rule: unverified: no page read states them.
- composes with: Supplies a routable port for a service on a free VM or a home box; the account's own compute does the serving.
- notes: The port range is the sharp edge. RFC6335 dynamic range means a service that insists on 80 or 443 cannot be published without buying Public IPv4, which is an add-on rather than part of the subscription. Nothing in the read pages states that the port survives a server change, so a pinned server is implied rather than promised.
- evidence note: Measured would need an account, a bound port and a byte count. The unlimited-traffic sentence sits on a marketing page while the terms carry a non-commercial capacity clause, which is why this is documented and not inferred from speed.
- extras:
  - wg_path: native-conf
  - wg_detail: WireGuard configs are downloaded per device from the account: You need to be logged in to download the configuration files. Ports are opened per protocol, Profile then Port Forwarding for OpenVPN or WireGuard.
  - ingress: tcp+udp
  - volume_stated: Our subscriptions contain unlimited bandwidth and traffic which means you can stream as much as you want.
  - bytes_transit: yes
  - transit_note: Traffic crosses OVPN servers, which the vendor describes as diskless.
- evidence:
  - [2] 2026-10-23: 7 ports per account, range 49152-65535 per RFC6335, TCP, UDP or both, and the requirement to reconnect before the port opens.
  - [1] 2026-10-23: Plan prices and the fact that Port forwarding appears on every plan row; no free plan is offered.
  - [3] 2026-10-23: Our subscriptions contain unlimited bandwidth and traffic.
  - [4] 2026-10-23: WireGuard configuration files are generated and downloaded from the logged-in account, one per device.
  - [1] 2026-11-03: 12-month plan per month | capture: sha256:864ee134196f51f96fff45a1ef7cb5d04e4d72c95733170055d4fa225655bf8c | quote: €4.99 −71%
  - [5] 2026-11-03: protocols | capture: sha256:11bd268f2ee4237d3ec255204e38ac414283bfae99518e0fa6acc6afb2f440e5 | quote: OVPN supports both OpenVPN and Wireguard protocols, which provide high levels of security.
  - [6] 2026-11-03: UDP and TCP | capture: sha256:6d52933ef1684904770003b848f7c3d6478f0944ab835d3c452c26f65d494f9e | quote: OpenVPN works both over UDP and TCP, while we mainly recommend using UDP.
  - [5] 2026-11-03: forwarded ports can be UDP | capture: sha256:11bd268f2ee4237d3ec255204e38ac414283bfae99518e0fa6acc6afb2f440e5 | quote: When you open a port, you can choose if it should be a TCP, UDP, or TCP and UDP ports.
  - [1] 2026-11-04: the 36-month plan is 4.22 EUR per month | capture: sha256:864ee134196f51f96fff45a1ef7cb5d04e4d72c95733170055d4fa225655bf8c | quote: €4.22 −75%
- sources:
  - [1] https://www.ovpn.com/en/pricing
  - [2] https://support.ovpn.com/hc/en-us/articles/18731795296788-Opening-Ports
  - [3] https://www.ovpn.com/en/streaming
  - [4] https://www.ovpn.com/en/guides/wireguard/mac-wg
  - [5] https://www.ovpn.com/en/
  - [6] https://www.ovpn.com/en/openvpn
