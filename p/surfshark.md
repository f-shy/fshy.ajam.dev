# Surfshark

> surfshark.com | IP and proxies, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/surfshark/ | JSON https://fshy.ajam.dev/api/v1/entity/surfshark.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Surfshark (exit addresses)

- `ip-proxy/surfshark-exits` | paid-only | evidence measured | binding none | category vpn subscription (exit source) | tier exit addresses
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:30:00.000Z (live) | stale on 2026-12-05
- url https://surfshark.com/pricing
- free tier: No free plan read. The pricing page FAQ states monthly, 1-year and 2-year subscriptions; the amounts did not load in the captured text, so no price is recorded. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The price is the vendor's plan rate for the subscription whose exits are classified here; the exit-address measurement itself has no price.
- per-object cap: not applicable | source: [2] | note: The classified sample is 142 addresses over 18 ASNs; none of those numbers is an object size.
- retention: not applicable: an address, not an object | source: [2] | note: Nothing is stored, so no retention clock applies. How long one exit address is held before it is re-drawn was not observed.
- egress: unverified: no traffic allowance or per-GB price appears in the captured pages; metered is recorded false because no metered charge was read. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: unverified: the purchase flow was not read; an account is required to use the service.
- interface: unknown
- limits:
  - per-ip-shaping: unverified: no device or connection ceiling appears in the captured pages [1]
- binding note: No limit kind binds the record: it measures exit addresses and states no byte quota or request rate. What matters is list membership: 137 of 142 sampled exits are on a datacenter list.
- interface detail: The server list at https://api.surfshark.com/v4/server/clusters/generic is the source of the exit addresses classified here. The schema interface enum has no token for a VPN tunnel, so the tunnel protocols are not recorded as an interface.
- endpoint: part of interface detail
- tooling: The exit addresses are read from https://api.surfshark.com/v4/server/clusters/generic and classified with an IP-class detector; the service itself is reached with the vendor's own client or a WireGuard or OpenVPN configuration.
- composes with: A Worker or a free compute node dials the tunnel and the traffic leaves at one of these exit addresses, so the upstream sees an address in the ASNs listed here and not the caller's network.
- reliability: 137 of 142 sampled exit addresses are on a datacenter list and 113 of 142 on a VPN list, so a site that blocks those lists blocks most of this fleet; 0 of 142 are also on an abuse list.
- notes: List membership of 142 exit addresses (detector index version 20261103T163900Z-00d117b2, 2026-11-03): datacenter 137, VPN 113, abuse 0, none of the three 5. VPN list: 113 of 142, of which 108 are in the x4b VPN list. Definitions: datacenter is an address inside a range the x4b datacenter list publishes; VPN is inside the x4b VPN list or a per-provider server list; abuse is on at least one independent abuse family; none of the three states list membership, not physical siting.
- evidence note: The list membership, ASN spread and counts are measured: each address was answered by the detector at the stated index version. The plan price and the identity class are documented from the vendor's captured pages; where a page did not state them they are unverified. The sample is the addresses the vendor endpoint returned, not proof that every address a user is handed is in it.
- extras:
  - rung: 4
  - rung_note: Addresses came from the vendor's own server list and each was classified; no exit was connected to, so the address a user is handed at connect time was not observed.
  - list_membership.measured_on: 2026-11-03
  - list_membership.n: 142
  - list_membership.datacenter: 137
  - list_membership.vpn: 113
  - list_membership.vpn_in_x4b: 108
  - list_membership.abuse: 0
  - list_membership.none_of_the_three: 5
  - list_membership.detector_index_version: 20261103T163900Z-00d117b2
  - list_membership.probed_at: 2026-11-03T17:20:53Z
  - list_membership.endpoint: https://api.surfshark.com/v4/server/clusters/generic
  - asn_diversity.measured_on: 2026-11-03
  - asn_diversity.addresses: 142
  - asn_diversity.subnets_24: 142
  - asn_diversity.asns: 18
  - asn_diversity.largest_asn: AS209854 Cyberzonehub Cyberzone S.A.
  - asn_diversity.largest_asn_addresses: 65
  - asn_diversity.largest_asn_share: 46%
- evidence:
  - probe:https://api.surfshark.com/v4/server/clusters/generic 2026-11-03: The vendor endpoint https://api.surfshark.com/v4/server/clusters/generic gave 142 IPv4 exit addresses, each answered by the address-class detector at index version 20261103T163900Z-00d117b2 on 2026-11-03. Datacenter list: 137 of 142; VPN list: 113 of 142 (108 in the x4b VPN list); abuse list: 0 of 142; on none of the three: 5 of 142. 18 distinct ASNs and 142 distinct /24s; largest ASN AS209854 Cyberzonehub Cyberzone S.A. with 65 addresses. | capture: sha256:d359db0a5cace09ce84aa6278550ca6bb3c435918f4db8781353fac7c57b2e97 | quote: "n": 142,
  - probe:https://api.surfshark.com/v4/server/clusters/generic 2026-11-03: Detector index version 20261103T163900Z-00d117b2 was the one every one of the 142 answers carries. | capture: sha256:d359db0a5cace09ce84aa6278550ca6bb3c435918f4db8781353fac7c57b2e97 | quote: "index_version": "20261103T163900Z-00d117b2",
  - [1] 2026-11-04: the plans are monthly, 1-year and 2-year subscriptions | capture: sha256:122ce05cdc5bd135140b43734fb29fed1d9abc0c3d6b3f7f3e630cfc8bcf2e75 | quote: Surfshark offers monthly, 1-year, and 2-year subscriptions, and all of them are billed differently:
  - [1] 2026-11-04: one account has unlimited simultaneous device connections | capture: sha256:122ce05cdc5bd135140b43734fb29fed1d9abc0c3d6b3f7f3e630cfc8bcf2e75 | quote: Yes. Surfshark offers unlimited simultaneous device connections, which means you can protect your whole household for the cost of a single [VPN](https://surfshark.com/vpn) subscription.
- sources:
  - [1] https://surfshark.com/pricing
  - [2] https://api.surfshark.com/v4/server/clusters/generic

## Surfshark (paid)

- `egress/surfshark` | fails-egress | evidence documented | binding write-gated | category vpn port forward | tier paid
- identity a placeholder: card and phone unknown | verified 2026-11-04T10:29:23.993Z (live) | stale on 2026-12-05
- url https://surfshark.com/blog/vpn-port-forwarding
- price USD 2.49 per month on Surfshark Starter, USD 67.23 for the first 27 months (24 months plus 3 extra) | parsed USD 2.49/mo
- free tier: No free tier, and the vendor refuses the feature: Surfshark VPN does not support port forwarding because it creates a potential network entry point that exposes devices to unauthorized connections. Pricing page 2026-11-04: Surfshark Starter at $2.49/mo, $67.23 for the first 27 months (24 months plus 3 extra); a 1-year plan is mentioned but its price is unverified: the page shows no 1-year figure. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unverified: published terms state no explicit traffic allowance.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: unverified: the purchase flow was not read; an account is required to use the service. | country: None
- interface: cli
- limits:
  - write-gated (binding): the feature is not offered at any tier: Surfshark VPN does not support port forwarding [1]
- binding note: No inbound path exists, so no volume or identity constraint is reachable.
- interface detail: App and extension based. Protocols: WireGuard, IKEv2, OpenVPN (UDP or TCP) and Dausos (macOS app). Shadowsocks is not offered. No SOCKS5 proxy is offered (third-party report). Obfuscation: OpenVPN runs on obfuscated servers, and NoBorders covers restricted networks. P2P-optimized servers exist.
- tooling: Official apps; WireGuard supported for outbound.
- composes with: Client-side tunnel only.
- reliability: No inbound path exists at any tier.
- notes: A third-party guide from 2021 said the same thing, which makes the position at least five years old rather than a recent withdrawal. No conflict found. The dedicated IP product Surfshark sells is an address, not a forwarded port, and was not read.
- evidence note: The refusal is a direct vendor sentence on a vendor page read. Measured is impossible.
- extras:
  - wg_path: native-conf
  - wg_detail: WireGuard is a supported protocol under the vendor's own client; the config does not create an inbound path because none is sold.
  - ingress: none
  - volume_stated: unverified: no page read states a Surfshark traffic allowance.
  - bytes_transit: yes
  - transit_note: Outbound only from a user's point of view.
- evidence:
  - [1] 2026-10-23: Surfshark VPN does not support port forwarding, stated as the vendor's own answer, with security exposure given as the reason.
  - [2] 2026-11-04: the Starter plan sale price is $67.23 for the first 27 months | capture: sha256:f41e5c1e7f849798635d33274d50d905a31cf9e605a11a01e581ca2df87f9587 | quote: <s>$511.65</s> <span class="_7CafX">sale price</span> <strong>$67.23</strong> for the first 27 months
  - [3] 2026-11-04: Surfshark offers Dausos, WireGuard, OpenVPN and IKEv2 | capture: sha256:0f3b4644c91f9f8455efff56c3e58195e709eea7e28d990a40afc28100545024 | quote: Surfshark VPN protocols: Dausos, WireGuard, OpenVPN, IKEv2
  - [4] 2026-11-04: OpenVPN is selectable over UDP or TCP | capture: sha256:952d8cc29f5e893aa407f230dae78ad1af862f2f07566088f9d284404dbdb78e | quote: If you are using the Surfshark app, you will find two options for OpenVPN: UDP and TCP.
  - [4] 2026-11-04: OpenVPN on Surfshark uses obfuscated servers | capture: sha256:952d8cc29f5e893aa407f230dae78ad1af862f2f07566088f9d284404dbdb78e | quote: while using this protocol on Surfshark, you are using obfuscated servers
  - [5] 2026-11-04: NoBorders is the restricted-network mode | capture: sha256:763414df4290ef860302dccff5ddb90e0b9133e52a7799253c3418244308732c | quote: lets you use a VPN through network restrictions such as geoblocking or government censorship
  - [6] 2026-11-04:  | capture: sha256:1cae02594bffd9be2b9c9927f76705ed4eb40d96f6f7ac970330c48c31ed080c | quote: Surfshark will stop supporting Shadowsocks this week
  - [7] 2026-11-04: a third party reports no SOCKS5 proxy is offered | capture: sha256:7967e6acf4ffd84ae058772267b2c45dab987361a7f05ad73d7ec727582cd15b | quote: offer SOCKS5 proxy as a standalone service or an add-on to its VPN service
  - [8] 2026-11-04: the vendor blog lists P2P-optimized servers | capture: sha256:8c5f4897261c54d193e5d5df8b0ae99f738a4efcc6022274d1c2d994f28e716f | quote: Servers optimized for secure P2P (peer-to-peer) file exchange
  - [2] 2026-11-04: Surfshark Starter is 67.23 USD for the first 27 months | capture: sha256:8330d2f7ca4358bbb6aefe4c15665b127f082f4dca193cbe26079fb2228ac253 | quote: old price $511.65 sale price $67.23 for the first 27 months (VAT may apply).
- sources:
  - [1] https://surfshark.com/blog/vpn-port-forwarding
  - [2] https://surfshark.com/pricing
  - [3] https://surfshark.com/features/surfshark-vpn-protocols
  - [4] https://support.surfshark.com/hc/en-us/articles/360010324739-What-protocols-can-I-use-with-Surfshark
  - [5] https://support.surfshark.com/hc/en-us/articles/10448039999122-Surfshark-Features
  - [6] https://surfshark.com/blog/surfshark-will-stop-supporting-shadowsocks
  - [7] https://vpnalert.com/guides/surfshark-socks5/
  - [8] https://surfshark.com/blog/surfshark-vs-ipvanish
