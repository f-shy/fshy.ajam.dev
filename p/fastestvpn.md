# FastestVPN

> fastestvpn.com | IP and proxies, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fastestvpn/ | JSON https://fshy.ajam.dev/api/v1/entity/fastestvpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## FastestVPN (exit addresses)

- `ip-proxy/fastestvpn-exits` | paid-only | evidence measured | binding none | category vpn subscription (exit source) | tier exit addresses
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:30:00.000Z (live) | stale on 2026-12-05
- url https://fastestvpn.com/pricing
- free tier: No free tier. The pricing page lists a 1 Month Plan at $5 per month and a 1 Year + 1 Year Free plan at $0.83 per month billed $19.95 biennially. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The price is the vendor's plan rate for the subscription whose exits are classified here; the exit-address measurement itself has no price.
- per-object cap: not applicable | source: [2] | note: The classified sample is 15 addresses over 5 ASNs; none of those numbers is an object size.
- retention: not applicable: an address, not an object | source: [2] | note: Nothing is stored, so no retention clock applies. How long one exit address is held before it is re-drawn was not observed.
- egress: unverified: no traffic allowance or per-GB price appears in the captured pages; metered is recorded false because no metered charge was read. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: unverified: the purchase flow was not read; a subscription account is required to use the service.
- interface: unknown
- limits:
  - per-ip-shaping: unverified: no device or connection ceiling appears in the captured pages [1]
- binding note: No limit kind binds the record: it measures exit addresses and states no byte quota or request rate. What matters is list membership: 13 of 15 sampled exits are on a datacenter list.
- interface detail: The server list at https://support.fastestvpn.com/vpn-servers/ is the source of the exit addresses classified here. The schema interface enum has no token for a VPN tunnel, so the tunnel protocols are not recorded as an interface.
- endpoint: part of interface detail
- tooling: The exit addresses are read from https://support.fastestvpn.com/vpn-servers/ and classified with an IP-class detector; the service itself is reached with the vendor's own client or a WireGuard or OpenVPN configuration.
- composes with: A Worker or a free compute node dials the tunnel and the traffic leaves at one of these exit addresses, so the upstream sees an address in the ASNs listed here and not the caller's network.
- reliability: 13 of 15 sampled exit addresses are on a datacenter list and 10 of 15 on a VPN list, so a site that blocks those lists blocks most of this fleet; 8 of 15 are also on an abuse list.
- notes: List membership of 15 exit addresses (detector index version 20261103T163900Z-00d117b2, 2026-11-03): datacenter 13, VPN 10, abuse 8, none of the three 1. VPN list: 10 of 15, of which 10 are in the x4b VPN list. Definitions: datacenter is an address inside a range the x4b datacenter list publishes; VPN is inside the x4b VPN list or a per-provider server list; abuse is on at least one independent abuse family; none of the three states list membership, not physical siting.
- evidence note: The list membership, ASN spread and counts are measured: each address was answered by the detector at the stated index version. The plan price and the identity class are documented from the vendor's captured pages; where a page did not state them they are unverified. The sample is the addresses the vendor endpoint returned, not proof that every address a user is handed is in it.
- extras:
  - rung: 4
  - rung_note: Addresses came from the vendor's own server list and each was classified; no exit was connected to, so the address a user is handed at connect time was not observed.
  - list_membership.measured_on: 2026-11-03
  - list_membership.n: 15
  - list_membership.datacenter: 13
  - list_membership.vpn: 10
  - list_membership.vpn_in_x4b: 10
  - list_membership.abuse: 8
  - list_membership.none_of_the_three: 1
  - list_membership.detector_index_version: 20261103T163900Z-00d117b2
  - list_membership.probed_at: 2026-11-03T17:20:54Z
  - list_membership.endpoint: https://support.fastestvpn.com/vpn-servers/ (hostnames DNS-resolved)
  - asn_diversity.measured_on: 2026-11-03
  - asn_diversity.addresses: 15
  - asn_diversity.subnets_24: 14
  - asn_diversity.asns: 5
  - asn_diversity.largest_asn: AS9009 M247 M247 Europe SRL
  - asn_diversity.largest_asn_addresses: 10
  - asn_diversity.largest_asn_share: 67%
- evidence:
  - probe:https://support.fastestvpn.com/vpn-servers/ 2026-11-03: The vendor endpoint https://support.fastestvpn.com/vpn-servers/ gave 15 IPv4 exit addresses, each answered by the address-class detector at index version 20261103T163900Z-00d117b2 on 2026-11-03. Datacenter list: 13 of 15; VPN list: 10 of 15 (10 in the x4b VPN list); abuse list: 8 of 15; on none of the three: 1 of 15. 5 distinct ASNs and 14 distinct /24s; largest ASN AS9009 M247 M247 Europe SRL with 10 addresses. | capture: sha256:9e812589a5128ae420693686350a9edabb564dc0ba19b1bd833e4d01237b9384 | quote: "n": 15,
  - probe:https://support.fastestvpn.com/vpn-servers/ 2026-11-03: Detector index version 20261103T163900Z-00d117b2 was the one every one of the 15 answers carries. | capture: sha256:9e812589a5128ae420693686350a9edabb564dc0ba19b1bd833e4d01237b9384 | quote: "index_version": "20261103T163900Z-00d117b2",
  - [1] 2026-11-04: the cheapest plan is $0.83 per month billed $19.95 every two years | capture: sha256:6bcf9d509058850d787fb8e2330d11e17e995b9592790f28eaa42f13f8c3cc87 | quote: ##### Billed $19.95 Biennially
  - [1] 2026-11-04: a refund window applies to new purchases; the sign-up step was not read | capture: sha256:6bcf9d509058850d787fb8e2330d11e17e995b9592790f28eaa42f13f8c3cc87 | quote: With a 31-day money-back guarantee for new purchases
- sources:
  - [1] https://fastestvpn.com/pricing
  - [2] https://support.fastestvpn.com/vpn-servers/

## FastestVPN (paid)

- `egress/fastestvpn` | fails-egress | evidence documented | binding write-gated | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:29:23.991Z (live) | stale on 2026-12-05
- url https://fastestvpn.com/resources/how-to-port-forward-pldt-router/
- price USD 5 per month on the 1 Month plan; USD 0.83 per month on the 1 Year + 1 Year Free plan, billed USD 19.95 biennially; Lifetime Plus Plan USD 40 | parsed USD 0.83/mo
- free tier: No free tier, and the vendor states it does not offer forwarding: some VPNs allow port forwarding. However, FastestVPN doesn't, and we advise against PLDT port forwarding. Pricing page 2026-11-03: 1 Month $5 per month; the 1 Year + 1 Year Free plan is $0.83 per month, billed $19.95 biennially; Lifetime Plus Plan $40. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unverified: published terms state no explicit traffic allowance.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: A subscription account; the dedicated IP page says you must first create your account by buying a subscription, then either request or buy a dedicated IP. | country: None
- interface: cli
- limits:
  - write-gated (binding): no forwarding offered: FastestVPN doesn't offer router port forwarding features, and separately, some VPNs allow port forwarding. However, FastestVPN doesn't [1]
- binding note: There is no inbound path to meter, so volume never binds.
- interface detail: App-based; no port facility in the pages read.
- tooling: Official apps. Protocols: WireGuard, OpenVPN, IKEv2, IPSec, OpenConnect and L2TP. Servers optimized for P2P file sharing are offered. UDP, SOCKS5 endpoint and obfuscation: unverified: no page read states them.
- composes with: Client-side tunnel only.
- reliability: No inbound path is sold, so there is nothing to throttle.
- notes: Test applied: the vendor's dedicated IP page, which is where a paid ingress add-on would have to be sold, does not mention forwarding at all.
- evidence note: The negative is documented twice in the vendor's own words, dated 2025-05-21, and the features page read does not list port forwarding.
- extras:
  - wg_path: native-conf
  - wg_detail: WireGuard is one of the listed protocols: FastestVPN has multiple protocols, such as WireGuard, OpenVPN. A config alone gives no inbound path here.
  - ingress: none
  - volume_stated: unverified: no page read states a FastestVPN traffic allowance.
  - bytes_transit: yes
  - transit_note: Outbound only from a user's point of view.
- evidence:
  - [1] 2026-10-23: Published 2025-05-21: FastestVPN doesn't offer router port forwarding features, and some VPNs allow port forwarding, however FastestVPN doesn't.
  - [2] 2026-10-23: The dedicated IP page read lists no port forwarding among the benefits of a dedicated IP, and describes buying or requesting one.
  - [3] 2026-11-03: the 1 Year + 1 Year Free plan is billed 19.95 USD every two years | capture: sha256:6bcf9d509058850d787fb8e2330d11e17e995b9592790f28eaa42f13f8c3cc87 | quote: Billed $19.95 Biennially
  - [4] 2026-11-03: protocol list | capture: sha256:4f895610cb9ec34fb22d8c8cd5c493b93e7ffa7f4c9aa97c08280bab39e2295b | quote: FastestVPN has multiple protocols, such as WireGuard, OpenVPN, IKEv2, IPSec, OpenConnect, L2TP, and more.
  - [4] 2026-11-03: P2P servers exist | capture: sha256:4f895610cb9ec34fb22d8c8cd5c493b93e7ffa7f4c9aa97c08280bab39e2295b | quote: Choose any of our speedy servers that are optimized for P2P file sharing activities. Get fast speed while downloading files.
  - [3] 2026-11-04: the 1 Year + 1 Year Free plan is billed 19.95 USD every two years | capture: sha256:6bcf9d509058850d787fb8e2330d11e17e995b9592790f28eaa42f13f8c3cc87 | quote: Billed $19.95 Biennially
- sources:
  - [1] https://fastestvpn.com/resources/how-to-port-forward-pldt-router/
  - [2] https://fastestvpn.com/dedicated-ip-vpn
  - [3] https://fastestvpn.com/pricing
  - [4] https://fastestvpn.com/features
