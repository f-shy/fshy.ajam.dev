# AzireVPN

> azirevpn.com | Egress and tunnels, IP and proxies; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/azirevpn/ | JSON https://fshy.ajam.dev/api/v1/entity/azirevpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## AzireVPN (paid)

- `egress/azirevpn` | paid-only | evidence documented | binding retention-clamped | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:39:32.203Z (live) | stale on 2026-12-05
- url https://blog.azirevpn.com/port-forwarding/
- price EUR 5.00 per month; EUR 4.00 per month on 3 months; EUR 3.75 per month on 12 months (45.00) | parsed USD 4.2/mo
- free tier: No free tier. Pricing page 2026-10-23: 1 Month 5.00 EUR per month; 3 Months 4.00 EUR per month (12.00 EUR); 12 Months 3.75 EUR per month (45.00 EUR), with a 7-day money-back guarantee. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: unverified: published terms state no explicit byte allowance. Marketing describes 10G servers and unlimited browsing.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: Registration at manager.azirevpn.com with an account; card and PayPal are listed, and crypto is advertised on the pricing page description. | country: None
- interface: cli, rest
- limits:
  - retention-clamped (binding): a granted port carries an expiry and can be extended: Done, you will see the port you have been granted and when the port will expire. The API takes expires_in, and PUT updates the port. [2]
  - per-ip-shaping: the port is bound to the internal IPv4 of a connected device, so it is only valid while that device holds the address on that server [2]
- binding note: No byte quota is stated, so the expiry is what fails first: the port is leased with an explicit expires_in and must be renewed by API call. Renewal is scriptable, which makes this the most controllable lease of the paid set, but it is still a lease.
- interface detail: Documented REST endpoints under api.azirevpn.com/v2/portforward for get, request, update, delete and check.
- tooling: API with a bearer token; wg-quick from the manager-generated config. Protocols: WireGuard. Peer-to-peer traffic and the BitTorrent protocol are allowed on all servers. UDP, SOCKS5 endpoint and obfuscation: unverified: no page read states them.
- composes with: The cleanest scripted path in the paid set: a cron job renews the lease and writes the current port into the service config.
- reliability: A server outage invalidates the port and forces a new random one; the mapping is tied to the device's internal IPv4.
- notes: The blog also warns that a server outage costs the port: If the server goes down, your port becomes unretrievable and you will have to generate a new random port. That is the weakest link in an otherwise scriptable design: the lease is renewable but the number is not guaranteed across a server failure. AzireVPN is now part of Malwarebytes per its own homepage, which matters only as a continuity risk.
- evidence note: Measured would need a token, a generated port and a byte count. The API shape is quoted from the vendor blog, and an unauthenticated check endpoint exists at api.azirevpn.com/v2/portforward/check which would let a measured claim be made later.
- extras:
  - wg_path: registration-api
  - wg_detail: The port is obtained by HTTP against the vendor API with a bearer token: POST https://api.azirevpn.com/v2/portforward with internal_ipv4, expires_in and hidden, and PUT to update the same port. The configuration file is tied to the device on the WireGuard manager page: Press Port forwarding on the configuration file tied to the device that you are connected on.
  - ingress: tcp+udp
  - volume_stated: unverified: no page read states an AzireVPN traffic allowance. The site describes 10G servers and unlimited browsing, not bytes.
  - bytes_transit: yes
  - transit_note: Traffic crosses AzireVPN's own servers; the vendor states it owns 100 percent of its infrastructure.
- evidence:
  - [2] 2026-10-23: Port forwarding launches against the WireGuard configuration of a connected device; the port has an expiry; the API offers POST with expires_in, PUT to update and DELETE; a check endpoint returns port status.
  - [1] 2026-10-23: Plans at 5.00, 4.00 and 3.75 EUR per month with a 7-day money-back guarantee; no free plan listed.
  - [3] 2026-10-23: Port forwarding is a listed feature, WireGuard is a listed protocol, and P2P traffic is allowed on all servers.
  - [3] 2026-11-03: BitTorrent allowed on all servers | capture: sha256:c7ce9cd4cee75599a22009840a669be4e90521820a51d482a9eedd813bb8b52a | quote: We strongly believe in internet neutrality, so peer-to-peer traffic and the BitTorrent protocol are allowed on all of our servers
  - [1] 2026-11-03: WireGuard is offered | capture: sha256:aee760f4acf7a56af8379b1a4d5fd359fd1d5fbad5b865e92679a9c1ced3ae21 | quote: AzireVPN was the first to implement WireGuard in 2017 and has made a donation to support its development.
  - [1] 2026-11-03: the 12-month plan is 3.75 EUR per month | capture: sha256:aee760f4acf7a56af8379b1a4d5fd359fd1d5fbad5b865e92679a9c1ced3ae21 | quote: Prices like it's 2017! We’re rolling it back — AzireVPN now starts at just 3,75 €/month with the 12-month plan.
- sources:
  - [1] https://www.azirevpn.com/pricing
  - [2] https://blog.azirevpn.com/port-forwarding/
  - [3] https://www.azirevpn.com/

## AzireVPN (exit addresses)

- `ip-proxy/azirevpn-exits` | paid-only | evidence measured | binding none | category vpn subscription (exit source) | tier exit addresses
- identity a placeholder: card and phone unknown | verified 2026-11-04T00:30:00.000Z (live) | stale on 2026-12-05
- url https://www.azirevpn.com/pricing
- free tier: No free tier. The pricing page lists 1 Month at 5.00 EUR, 3 Months at 4.00 EUR per month (12.00 EUR) and 12 Months at 3.75 EUR per month (45.00 EUR), with a 7-day money-back guarantee. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The price is the vendor's plan rate for the subscription whose exits are classified here; the exit-address measurement itself has no price.
- per-object cap: not applicable | source: [2] | note: The classified sample is 32 addresses over 15 ASNs; none of those numbers is an object size.
- retention: not applicable: an address, not an object | source: [2] | note: Nothing is stored, so no retention clock applies. How long one exit address is held before it is re-drawn was not observed.
- egress: unverified: no traffic allowance or per-GB price appears in the captured pages; metered is recorded false because no metered charge was read. | metered: no | free allowance: none published | source: [1]
- identity: email | detail: unverified: the captured register page lists only password rules; the payment methods listed are visa, mastercard, paypal, apple-pay and american-express.
- interface: unknown
- limits:
  - per-ip-shaping: unverified: no device or connection ceiling appears in the captured pages [1]
- binding note: No limit kind binds the record: it measures exit addresses and states no byte quota or request rate. What matters is list membership: 20 of 32 sampled exits are on a datacenter list.
- interface detail: The server list at https://api.azirevpn.com/v3/locations is the source of the exit addresses classified here. The schema interface enum has no token for a VPN tunnel, so the tunnel protocols are not recorded as an interface.
- endpoint: part of interface detail
- tooling: The exit addresses are read from https://api.azirevpn.com/v3/locations and classified with an IP-class detector; the service itself is reached with the vendor's own client or a WireGuard or OpenVPN configuration.
- composes with: A Worker or a free compute node dials the tunnel and the traffic leaves at one of these exit addresses, so the upstream sees an address in the ASNs listed here and not the caller's network.
- reliability: 20 of 32 sampled exit addresses are on a datacenter list and 1 of 32 on a VPN list, so a site that blocks those lists blocks most of this fleet; 24 of 32 are also on an abuse list.
- notes: List membership of 32 exit addresses (detector index version 20261103T163900Z-00d117b2, 2026-11-03): datacenter 20, VPN 1, abuse 24, none of the three 2. VPN list: 1 of 32, of which 0 are in the x4b VPN list. Definitions: datacenter is an address inside a range the x4b datacenter list publishes; VPN is inside the x4b VPN list or a per-provider server list; abuse is on at least one independent abuse family; none of the three states list membership, not physical siting.
- evidence note: The list membership, ASN spread and counts are measured: each address was answered by the detector at the stated index version. The plan price and the identity class are documented from the vendor's captured pages; where a page did not state them they are unverified. The sample is the addresses the vendor endpoint returned, not proof that every address a user is handed is in it.
- extras:
  - rung: 4
  - rung_note: Addresses came from the vendor's own server list and each was classified; no exit was connected to, so the address a user is handed at connect time was not observed.
  - list_membership.measured_on: 2026-11-03
  - list_membership.n: 32
  - list_membership.datacenter: 20
  - list_membership.vpn: 1
  - list_membership.vpn_in_x4b: 0
  - list_membership.abuse: 24
  - list_membership.none_of_the_three: 2
  - list_membership.detector_index_version: 20261103T163900Z-00d117b2
  - list_membership.probed_at: 2026-11-03T17:20:54Z
  - list_membership.endpoint: https://api.azirevpn.com/v3/locations (pool hostnames DNS-resolved)
  - asn_diversity.measured_on: 2026-11-03
  - asn_diversity.addresses: 32
  - asn_diversity.subnets_24: 32
  - asn_diversity.asns: 15
  - asn_diversity.largest_asn: AS60068 CDN77 Datacamp Limited
  - asn_diversity.largest_asn_addresses: 9
  - asn_diversity.largest_asn_share: 28%
- evidence:
  - probe:https://api.azirevpn.com/v3/locations 2026-11-03: The vendor endpoint https://api.azirevpn.com/v3/locations gave 32 IPv4 exit addresses, each answered by the address-class detector at index version 20261103T163900Z-00d117b2 on 2026-11-03. Datacenter list: 20 of 32; VPN list: 1 of 32 (0 in the x4b VPN list); abuse list: 24 of 32; on none of the three: 2 of 32. 15 distinct ASNs and 32 distinct /24s; largest ASN AS60068 CDN77 Datacamp Limited with 9 addresses. | capture: sha256:233d6cd3b6c111e7cd30d924cf8495d8046c8659e771807f52a1252a8974344c | quote: "n": 32,
  - probe:https://api.azirevpn.com/v3/locations 2026-11-03: Detector index version 20261103T163900Z-00d117b2 was the one every one of the 32 answers carries. | capture: sha256:233d6cd3b6c111e7cd30d924cf8495d8046c8659e771807f52a1252a8974344c | quote: "index_version": "20261103T163900Z-00d117b2",
  - [1] 2026-11-04: the cheapest plan is 3.75 EUR per month on the 12-month term | capture: sha256:aee760f4acf7a56af8379b1a4d5fd359fd1d5fbad5b865e92679a9c1ced3ae21 | quote: Prices like it's 2017! We’re rolling it back — AzireVPN now starts at just 3,75 €/month with the 12-month plan.
  - [1] 2026-11-04: the pricing page lists card and PayPal payment methods | capture: sha256:aee760f4acf7a56af8379b1a4d5fd359fd1d5fbad5b865e92679a9c1ced3ae21 | quote: visa mastercard paypal apple-pay american-express
- sources:
  - [1] https://www.azirevpn.com/pricing
  - [2] https://api.azirevpn.com/v3/locations
