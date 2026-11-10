# Private Internet Access

> privateinternetaccess.com | IP and proxies; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/privateinternetaccess/ | JSON https://fshy.ajam.dev/api/v1/entity/privateinternetaccess.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Private Internet Access

- `ip-proxy/private-internet-access-exits` | paid-only | evidence measured | binding none | category vpn subscription (exit source) | tier exit addresses
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:30:00.000Z (live) | stale on 2026-12-05
- url https://www.privateinternetaccess.com/buy-vpn-online
- free tier: No free tier. The buy page lists 1 Month at $11.95 per month, 1 Year at $3.99 per month billed $47.88, and a 3 Years plan at $2.03 per month autorenewing at $81.20 every 3 years. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The price is the vendor's plan rate for the subscription whose exits are classified here; the exit-address measurement itself has no price.
- per-object cap: not applicable | source: [2] | note: The classified sample is 120 addresses over 17 ASNs; none of those numbers is an object size.
- retention: not applicable: an address, not an object | source: [2] | note: Nothing is stored, so no retention clock applies. How long one exit address is held before it is re-drawn was not observed.
- egress: unverified: no traffic allowance or per-GB price appears in the captured pages; metered is recorded false because no metered charge was read. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: unverified: the buy page was read but the account and payment step behind Select Plan was not.
- interface: unknown
- limits:
  - per-ip-shaping: unverified: no device or connection ceiling appears in the captured pages [1]
- binding note: No limit kind binds the record: it measures exit addresses and states no byte quota or request rate. What matters is list membership: 114 of 120 sampled exits are on a datacenter list.
- interface detail: The server list at https://serverlist.piaservers.net/vpninfo/servers/v6 is the source of the exit addresses classified here. The schema interface enum has no token for a VPN tunnel, so the tunnel protocols are not recorded as an interface.
- endpoint: part of interface detail
- tooling: The exit addresses are read from https://serverlist.piaservers.net/vpninfo/servers/v6 and classified with an IP-class detector; the service itself is reached with the vendor's own client or a WireGuard or OpenVPN configuration.
- composes with: A Worker or a free compute node dials the tunnel and the traffic leaves at one of these exit addresses, so the upstream sees an address in the ASNs listed here and not the caller's network.
- reliability: 114 of 120 sampled exit addresses are on a datacenter list and 117 of 120 on a VPN list, so a site that blocks those lists blocks most of this fleet; 16 of 120 are also on an abuse list.
- notes: List membership of 120 exit addresses (detector index version 20261103T163900Z-00d117b2, 2026-11-03): datacenter 114, VPN 117, abuse 16, none of the three 0. VPN list: 117 of 120, of which 90 are in the x4b VPN list and the rest are in the vendor's own server list as ingested by the detector, so the VPN count includes the vendor feed. Definitions: datacenter is an address inside a range the x4b datacenter list publishes; VPN is inside the x4b VPN list or a per-provider server list; abuse is on at least one independent abuse family; none of the three states list membership, not physical siting.
- evidence note: The list membership, ASN spread and counts are measured: each address was answered by the detector at the stated index version. The plan price and the identity class are documented from the vendor's captured pages; where a page did not state them they are unverified. The sample is the addresses the vendor endpoint returned, not proof that every address a user is handed is in it.
- extras:
  - rung: 4
  - rung_note: Addresses came from the vendor's own server list and each was classified; no exit was connected to, so the address a user is handed at connect time was not observed.
  - list_membership.measured_on: 2026-11-03
  - list_membership.n: 120
  - list_membership.datacenter: 114
  - list_membership.vpn: 117
  - list_membership.vpn_in_x4b: 90
  - list_membership.abuse: 16
  - list_membership.none_of_the_three: 0
  - list_membership.detector_index_version: 20261103T163900Z-00d117b2
  - list_membership.probed_at: 2026-11-03T17:20:52Z
  - list_membership.endpoint: https://serverlist.piaservers.net/vpninfo/servers/v6
  - asn_diversity.measured_on: 2026-11-03
  - asn_diversity.addresses: 120
  - asn_diversity.subnets_24: 115
  - asn_diversity.asns: 17
  - asn_diversity.largest_asn: AS137409 GSLNETWORKS-AS-AP - GSL Networks Pty LTD
  - asn_diversity.largest_asn_addresses: 54
  - asn_diversity.largest_asn_share: 45%
- evidence:
  - probe:https://serverlist.piaservers.net/vpninfo/servers/v6 2026-11-03: The vendor endpoint https://serverlist.piaservers.net/vpninfo/servers/v6 gave 120 IPv4 exit addresses, each answered by the address-class detector at index version 20261103T163900Z-00d117b2 on 2026-11-03. Datacenter list: 114 of 120; VPN list: 117 of 120 (90 in the x4b VPN list); abuse list: 16 of 120; on none of the three: 0 of 120. 17 distinct ASNs and 115 distinct /24s; largest ASN AS137409 GSLNETWORKS-AS-AP - GSL Networks Pty LTD with 54 addresses. | capture: sha256:053490111d3c1f195eff597a14303552e2c67c03b671ff46e6c4c31ac76280a4 | quote: "n": 120,
  - probe:https://serverlist.piaservers.net/vpninfo/servers/v6 2026-11-03: Detector index version 20261103T163900Z-00d117b2 was the one every one of the 120 answers carries. | capture: sha256:053490111d3c1f195eff597a14303552e2c67c03b671ff46e6c4c31ac76280a4 | quote: "index_version": "20261103T163900Z-00d117b2",
  - [1] 2026-11-04: the 3-year plan autorenews at $81.20 every 3 years, shown as $2.03/mo | capture: sha256:08d0cfe4336400597c8147da26998530873da130415a14e4f0f2b9b677a7e439 | quote: Autorenews at $81.20 every 3 years
  - [1] 2026-11-04: the buy page offers plans with a Select Plan step; the identity requirement is behind it | capture: sha256:08d0cfe4336400597c8147da26998530873da130415a14e4f0f2b9b677a7e439 | quote: Cancel Anytime. No Hassle, No Risk.
- sources:
  - [1] https://www.privateinternetaccess.com/buy-vpn-online
  - [2] https://serverlist.piaservers.net/vpninfo/servers/v6
