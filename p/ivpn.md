# IVPN

> ivpn.net | IP and proxies, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ivpn/ | JSON https://fshy.ajam.dev/api/v1/entity/ivpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IVPN (exit addresses)

- `ip-proxy/ivpn-exits` | paid-only | evidence measured | binding none | category vpn subscription (exit source) | tier exit addresses
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:30:00.000Z (live) | stale on 2026-12-05
- url https://www.ivpn.net/pricing/
- free tier: No free tier. The pricing page lists three plans, Standard, Plus and Pro, and a 1 Week term at $2; no monthly or yearly rate was read from the captured text. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The price is the vendor's plan rate for the subscription whose exits are classified here; the exit-address measurement itself has no price.
- per-object cap: not applicable | source: [2] | note: The classified sample is 89 addresses over 22 ASNs; none of those numbers is an object size.
- retention: not applicable: an address, not an object | source: [2] | note: Nothing is stored, so no retention clock applies. How long one exit address is held before it is re-drawn was not observed.
- egress: unverified: no traffic allowance or per-GB price appears in the captured pages; metered is recorded false because no metered charge was read. | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: The pricing page states no email is required for signup, with cash, Monero and Bitcoin accepted.
- interface: unknown
- limits:
  - per-ip-shaping: 5 devices on the Standard plan [1]
- binding note: No limit kind binds the record: it measures exit addresses and states no byte quota or request rate. What matters is list membership: 81 of 89 sampled exits are on a datacenter list.
- interface detail: The server list at https://api.ivpn.net/v5/servers.json is the source of the exit addresses classified here. The schema interface enum has no token for a VPN tunnel, so the tunnel protocols are not recorded as an interface.
- endpoint: part of interface detail
- tooling: The exit addresses are read from https://api.ivpn.net/v5/servers.json and classified with an IP-class detector; the service itself is reached with the vendor's own client or a WireGuard or OpenVPN configuration.
- composes with: A Worker or a free compute node dials the tunnel and the traffic leaves at one of these exit addresses, so the upstream sees an address in the ASNs listed here and not the caller's network.
- reliability: 81 of 89 sampled exit addresses are on a datacenter list and 89 of 89 on a VPN list, so a site that blocks those lists blocks most of this fleet; 1 of 89 are also on an abuse list.
- notes: List membership of 89 exit addresses (detector index version 20261103T163900Z-00d117b2, 2026-11-03): datacenter 81, VPN 89, abuse 1, none of the three 0. VPN list: 89 of 89, of which 23 are in the x4b VPN list and the rest are in the vendor's own server list as ingested by the detector, so the VPN count includes the vendor feed. Definitions: datacenter is an address inside a range the x4b datacenter list publishes; VPN is inside the x4b VPN list or a per-provider server list; abuse is on at least one independent abuse family; none of the three states list membership, not physical siting.
- evidence note: The list membership, ASN spread and counts are measured: each address was answered by the detector at the stated index version. The plan price and the identity class are documented from the vendor's captured pages; where a page did not state them they are unverified. The sample is the addresses the vendor endpoint returned, not proof that every address a user is handed is in it.
- extras:
  - rung: 4
  - rung_note: Addresses came from the vendor's own server list and each was classified; no exit was connected to, so the address a user is handed at connect time was not observed.
  - list_membership.measured_on: 2026-11-03
  - list_membership.n: 89
  - list_membership.datacenter: 81
  - list_membership.vpn: 89
  - list_membership.vpn_in_x4b: 23
  - list_membership.abuse: 1
  - list_membership.none_of_the_three: 0
  - list_membership.detector_index_version: 20261103T163900Z-00d117b2
  - list_membership.probed_at: 2026-11-03T17:20:51Z
  - list_membership.endpoint: https://api.ivpn.net/v5/servers.json
  - asn_diversity.measured_on: 2026-11-03
  - asn_diversity.addresses: 89
  - asn_diversity.subnets_24: 85
  - asn_diversity.asns: 22
  - asn_diversity.largest_asn: AS60068 CDN77 Datacamp Limited
  - asn_diversity.largest_asn_addresses: 28
  - asn_diversity.largest_asn_share: 31%
- evidence:
  - probe:https://api.ivpn.net/v5/servers.json 2026-11-03: The vendor endpoint https://api.ivpn.net/v5/servers.json gave 89 IPv4 exit addresses, each answered by the address-class detector at index version 20261103T163900Z-00d117b2 on 2026-11-03. Datacenter list: 81 of 89; VPN list: 89 of 89 (23 in the x4b VPN list); abuse list: 1 of 89; on none of the three: 0 of 89. 22 distinct ASNs and 85 distinct /24s; largest ASN AS60068 CDN77 Datacamp Limited with 28 addresses. | capture: sha256:8a9f7c199f64b8b176f644eaf717638912b22377f36153b71a7d0db8f0cc6da9 | quote: "n": 89,
  - probe:https://api.ivpn.net/v5/servers.json 2026-11-03: Detector index version 20261103T163900Z-00d117b2 was the one every one of the 89 answers carries. | capture: sha256:8a9f7c199f64b8b176f644eaf717638912b22377f36153b71a7d0db8f0cc6da9 | quote: "index_version": "20261103T163900Z-00d117b2",
  - [1] 2026-11-04: the pricing page lists a 1 Week term at $2 in USD | capture: sha256:6c579f599d280e72ca1a91d49de547ce6cecd84507e44b4e1787ea07f2417b1d | quote: 1 Week $2
  - [1] 2026-11-04: signup needs no email; payment by cash, Monero or Bitcoin is accepted | capture: sha256:6c579f599d280e72ca1a91d49de547ce6cecd84507e44b4e1787ea07f2417b1d | quote: No email required for signup 30-day refund window Cash, Monero, Bitcoin accepted
  - [1] 2026-11-04: the Standard plan row lists 5 devices | capture: sha256:6c579f599d280e72ca1a91d49de547ce6cecd84507e44b4e1787ea07f2417b1d | quote: IVPN / 5 Devices [i] AntiTracker [i]
- sources:
  - [1] https://www.ivpn.net/pricing/
  - [2] https://api.ivpn.net/v5/servers.json

## IVPN (pro)

- `egress/ivpn` | fails-egress | evidence documented | binding write-gated | category vpn port forward | tier pro
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:39:32.219Z (live) | stale on 2026-12-05
- url https://www.ivpn.net/blog/gradual-removal-of-port-forwarding/
- price unverified; pricing page shows a 1 Week plan at USD 2 and three tiers without byte or price detail in the extracted text
- free tier: No free tier, and no port forwarding since 2023: we have made the decision to gradually phase out the port forwarding feature from the IVPN Pro plan. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: unverified: the pricing page read lists tiers, device counts and a 1 Week plan at $2, but no byte allowance.; ingress: none | metered: no | free allowance: none published | source: [1]
- identity: email | detail: The pricing page states No email required for signup, with cash, Monero and Bitcoin accepted and a 30-day refund window. | country: None
- interface: cli
- limits:
  - write-gated (binding): port forwarding removed from the Pro plan from 2023-06-29 onward [1]
- binding note: The feature does not exist, so nothing about volume is reachable: the constraint that fails first is that there is no inbound path at all.
- interface detail: Account area for configs; no port API.
- tooling: wg-quick with account-generated configs; no port facility. Protocols: WireGuard, OpenVPN and IPSec. Obfuscation: V2Ray (VMess over QUIC or TCP) on every platform, and obfs4 for OpenVPN on desktop. A SOCKS5 proxy service is listed among the features. BitTorrent rule and UDP: unverified: no page read states them.
- composes with: Useful only as a client-side tunnel; it cannot publish a service.
- reliability: No inbound path exists, so there is no throttle or drop to record.
- notes: The 2023 announcement says gradually, so the open question was whether any tier retained it; the 2026 pricing page lists no port forwarding on any tier, which closes that question for the product as sold. IVPN remains a credible WireGuard provider with anonymous signup, which is why the record names what it lost rather than dismissing it.
- evidence note: The removal is documented from the vendor blog, read, and dated 2023-06-29. Measured is impossible because there is no feature to measure; a 2026 support-page read confirming the removal still stands would be the next check.
- extras:
  - wg_path: native-conf
  - wg_detail: WireGuard is a supported protocol and configs are generated in the account area; this does not help, because there is no port to forward.
  - ingress: none
  - volume_stated: unverified: the pricing page read lists tiers, device counts and a 1 Week plan at $2, but no byte allowance.
  - bytes_transit: yes
  - transit_note: Traffic crosses IVPN servers outbound only, from a user's point of view.
- evidence:
  - [1] 2026-10-23: Port forwarding was phased out of IVPN Pro, posted 2023-06-29, with the reason given as abuse, law enforcement inquiries and data centre relationships.
  - [2] 2026-10-23: Three tiers, Standard, Plus and Pro, with no port forwarding listed anywhere in the plan text, and no email required for signup.
  - [3] 2026-11-03: protocols | capture: sha256:fd44b8711570741680669550559ac52a1686ee15a8d10b502d0af82f361364df | quote: Choice of WireGuard, OpenVPN or IPSec protocols using either the IVPN apps or any other compatible VPN client.
  - [3] 2026-11-03: obfuscation | capture: sha256:fd44b8711570741680669550559ac52a1686ee15a8d10b502d0af82f361364df | quote: V2Ray obfuscation (VMess over QUIC or TCP) on every platform, plus obfs4 for OpenVPN on desktop, to connect from networks that block VPNs.
  - [2] 2026-11-03: SOCKS5 proxy service is a listed feature | capture: sha256:0a7e67727e16d6b2f6ab9df918dc6ab47c10af9ff1874d273215479bd1ddfbfe | quote: SOCKS5 proxy service
  - [2] 2026-11-03: no port forwarding | capture: sha256:0a7e67727e16d6b2f6ab9df918dc6ab47c10af9ff1874d273215479bd1ddfbfe | quote: We don't offer port forwarding.
- sources:
  - [1] https://www.ivpn.net/blog/gradual-removal-of-port-forwarding/
  - [2] https://www.ivpn.net/pricing/
  - [3] https://www.ivpn.net/en/
