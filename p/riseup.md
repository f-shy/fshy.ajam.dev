# Riseup VPN

> riseup.net | Egress and tunnels, IP and proxies, Debrid; 4 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/riseup/ | JSON https://fshy.ajam.dev/api/v1/entity/riseup.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Riseup VPN, free (donations)

- `egress/riseup-vpn` | qualifies-with-caveat | evidence documented | binding none | category tunnel (hosted): free donation-funded VPN with no account, OpenVPN and obfs4 on 21 shared gateways | tier free (donations)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:11:45.490Z (live) | stale on 2026-12-05
- url https://riseup.net/en/vpn
- price USD 0; a suggested donation of USD 60 a year; not a per-TB price
- free tier: Free to use with no account: 'You just install it and run it—no configuration, no account registration.' The service is donation-funded: 'The cost for us to offer RiseupVPN is approximately $60 USD per person per year', and users are asked to donate at least that. The cheapest yearly price is therefore USD 0; the suggested donation is USD 60. | unit: unlimited | metered on: none | read on: 2026-11-04 | source: [1] | note: No byte or time quota is stated on the pages read, and the published service configuration marks each of its 21 gateways as 'limited': false; that flag's meaning is not documented on the pages read, so the unit unlimited is an absence of a stated quota, not a vendor promise.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a tunnel, not stored bytes | source: [1] | note: The vendor states it does not log the user's IP address; no stored-object retention applies.
- egress: No byte cap or rate is stated on the pages read. All 21 gateways in the published service configuration carry 'limited': false. The help page says RiseupVPN 'bypasses these restrictions and, because you get your own IP, makes p2p applications work much better'. | metered: no | free allowance: free to use; no quota stated | source: [1]
- identity: anonymous | detail: No account: 'no configuration, no account registration'. The vendor states it does not log the user's IP address. Donations are optional and go through Liberapay (card or Euro bank debit), PayPal or Bitcoin.
- interface: cli
- limits:
  - per-ip-shaping: 21 gateways, each a shared exit used by many users; the vendor asks for donations because capacity is funded by users ('approximately $60 USD per person per year') [1]
- limits note: The pages read state no byte quota, device count or rate. The service has no account, so no per-account limit can be enforced by a login.
- binding note: No quota or rate is published and no account exists to enforce one; the open question is capacity (a donation-funded service with 21 gateways), which the limit vocabulary does not name.
- interface detail: A tunnel with desktop and Android apps (RiseupVPN, built on the Bitmask code) and a published JSON service configuration. Protocols: OpenVPN (AES-256-GCM) on every gateway. UDP: yes, on ports 53, 80 and 1194 in both TCP and UDP. Port forwarding: unverified: no page read states it. SOCKS5: unverified: no page read states a SOCKS5 endpoint. Obfuscation: obfs4 over TCP port 443 on every gateway. BitTorrent: the legacy help page lists p2p as a use the VPN supports; no current page states a rule.
- tooling: The RiseupVPN app, or a plain OpenVPN client using the gateways, ports and cipher in the vendor's published service configuration (21 gateways, each with openvpn and obfs4 transports).
- composes with: A free tunnel exit: traffic leaves from the address of one of 21 gateways, so the upstream sees a shared hosting-network address.
- reliability: A donation-funded service run as 'an experiment to see if we can create a VPN service that is easy enough for everyone to use and that people will donate enough to sustain'; capacity and continuity depend on donations.
- notes: Cheapest yearly price: USD 0 (donation-funded). The published service configuration lists 21 gateways, each offering OpenVPN on ports 53, 80 and 1194 over TCP and UDP and obfs4 on TCP 443.
- evidence note: Documented for price, sign-up and the BitTorrent line; the protocol, UDP and obfuscation values are measured from the vendor's published service configuration (a probe of the JSON, status 200). The BitTorrent line comes from a legacy help page of unknown date, so it is the weakest value. Nothing was connected through the service.
- evidence:
  - [1] 2026-11-04: no account is needed to use RiseupVPN | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: no configuration, no account registration
  - [1] 2026-11-04: The service is donation-funded. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: The RiseupVPN service is entirely funded through donations from users.
  - [1] 2026-11-04: The vendor's stated cost per user per year is USD 60. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: The cost for us to offer RiseupVPN is approximately $60 USD per person per year.
  - [1] 2026-11-04: No IP logging is stated. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: Unlike most other VPN providers, Riseup does not log your IP address.
  - [2] 2026-11-04: The help page states p2p works with the VPN. | capture: sha256:eb9f8ee87c43f720ea02b6fb467f6c0f70149b00f9363baaa9aa1998ca69212f | quote: The RiseupVPN bypasses these restrictions and, because you get your own IP, makes p2p applications work much better.
  - probe:api.black.riseup.net/eip-service 2026-11-04: every gateway offers OpenVPN on ports 53, 80 and 1194 over TCP and UDP | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "ports": ["53", "80", "1194"], "protocols": ["tcp", "udp"], "type": "openvpn"
  - probe:api.black.riseup.net/eip-service 2026-11-04: every gateway offers obfs4 on TCP port 443 | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "ports": ["443"], "protocols": ["tcp"], "type": "obfs4"
  - probe:api.black.riseup.net/eip-service 2026-11-04: the gateways are not flagged limited | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "limited": false
  - probe:api.black.riseup.net/eip-service 2026-11-04: the OpenVPN cipher is AES-256-GCM | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "cipher": "AES-256-GCM"
- sources:
  - [1] https://riseup.net/en/vpn
  - [2] https://crabgrass.riseup.net/riseuphelp+en/riseup-vpn

## Riseup VPN (exit addresses)

- `ip-proxy/riseup-vpn-exits` | qualifies-with-caveat | evidence documented | binding none | category vpn service (exit source) | tier exit addresses
- needs card no, phone no, ID no, institution no | verified 2026-11-04T00:14:00.000Z (live) | stale on 2026-12-05
- url https://riseup.net/en/vpn
- price no price; donation funded
- free tier: Free to use: no configuration, no account registration; the service is funded through donations. | unit: unlimited | metered on: none | read on: 2026-11-03 | source: [1] | note: No traffic allowance or speed limit is stated on the page read.
- per-object cap: not applicable | source: [2]
- retention: not applicable: an address, not an object | source: [2]
- egress: unverified: this record covers the exit addresses of the fleet, not the plan; the plan-level traffic terms belong to the vendor's own egress record where one exists. | metered: no | free allowance: none published for the address list | source: [1]
- identity: anonymous | detail: No account registration is needed to install and run the app.
- interface: rest
- limits note: No limit with a number was read. Address concentration is the finding: 21 gateway addresses in 5 ASNs, 13 in AS12876 Scaleway, 18 of 21 on the datacenter list.
- binding note: No quota or ceiling is stated, so none binds on the sources read; the practical limit is the pool of 21 addresses in 5 ASNs.
- interface detail: The client configuration is a public JSON file, eip-service.json, listing every gateway with its address; it answers with no credential.
- endpoint: https://api.black.riseup.net:443/3/config/eip-service.json
- tooling: The vendor client RiseupVPN installs and runs with no account; the gateway list is a public JSON file, so addresses can be read with an HTTP client. No SOCKS5 or HTTP proxy endpoint was found.
- composes with: A free compute node runs the vendor client or an OpenVPN client from the gateway file and the traffic leaves at one of 21 gateway addresses; 13 of the 21 are in one ASN, so rotation reaches few distinct networks.
- reliability: No suspension, throttle or data loss was measured. 18 of 21 gateway addresses are datacenter-listed and 2 are on an abuse list, so expect datacenter-class blocks.
- notes: Exit-address record for the Riseup VPN fleet, classified with detector index 20261103T163900Z-00d117b2 on 2026-11-03: 21 addresses, 18 datacenter-listed, 0 VPN-listed, 0 Tor exits, 2 on an abuse list, 2 on none of the lists; 5 ASNs, largest AS12876 Scaleway with 13 addresses. The tier differs from any plan record.
- evidence note: Plan facts are documented from the vendor page and the list classification measured on 2026-11-03; weakest rung documented.
- extras:
  - exit_classification.detector_index_version: 20261103T163900Z-00d117b2
  - exit_classification.classified_on: 2026-11-03
  - exit_classification.n: 21
  - exit_classification.datacenter_listed: 18
  - exit_classification.vpn_listed: 0
  - exit_classification.tor_exit: 0
  - exit_classification.abuse_listed: 2
  - exit_classification.in_none_of_the_lists: 2
  - exit_classification.asns: 5
  - exit_classification.largest_asn: AS12876 Scaleway
  - exit_classification.largest_asn_addresses: 13
  - exit_classification.endpoint: https://api.black.riseup.net:443/3/config/eip-service.json
  - exit_classification.derived: counts taken over the 21 answers of the registered record; 13 / 21 = 61.9%
- evidence:
  - probe:https://api.black.riseup.net:443/3/config/eip-service.json 2026-11-03: The gateway file yielded 21 addresses, which were classified. | capture: sha256:7bc23924564cc3534952f2c6a3379c90afc106a067eddba81ebfefb3ce948539 | quote: "n": 21,
  - [1] 2026-11-03: No account is needed. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: You just install it and run it—no configuration, no account registration.
  - [1] 2026-11-03: The service has no price; it is funded by donations. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: The RiseupVPN service is entirely funded through donations from users.
- sources:
  - [1] https://riseup.net/en/vpn
  - [2] https://api.black.riseup.net:443/3/config/eip-service.json

## RiseupVPN

- `ip-proxy/riseup-vpn` | qualifies-with-caveat | evidence documented | binding none | category VPN service (donation-funded, free to use) | tier free (donations)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:58:00.000Z (live) | stale on 2026-12-05
- url https://riseup.net/en/vpn
- price USD 0; a suggested donation of USD 60 a year; not a per-TB price
- duplicate of `egress/riseup-vpn`
- free tier: Free to use with no account: 'You just install it and run it—no configuration, no account registration.' The service is donation-funded: 'The cost for us to offer RiseupVPN is approximately $60 USD per person per year', and users are asked to donate at least that. The cheapest yearly price is therefore USD 0; the suggested donation is USD 60. | unit: unlimited | metered on: none | read on: 2026-11-04 | source: [1] | note: No byte or time quota is stated on the pages read, and the published service configuration marks each of its 21 gateways as 'limited': false; that flag's meaning is not documented on the pages read, so the unit unlimited is an absence of a stated quota, not a vendor promise.
- per-object cap: not applicable | source: [1]
- retention: not applicable: a tunnel, not stored bytes | source: [1] | note: The vendor states it does not log the user's IP address; no stored-object retention applies.
- egress: No byte cap or rate is stated on the pages read. All 21 gateways in the published service configuration carry 'limited': false. The help page says RiseupVPN 'bypasses these restrictions and, because you get your own IP, makes p2p applications work much better'. | metered: no | free allowance: free to use; no quota stated | source: [1]
- identity: anonymous | detail: No account: 'no configuration, no account registration'. The vendor states it does not log the user's IP address. Donations are optional and go through Liberapay (card or Euro bank debit), PayPal or Bitcoin.
- interface: cli
- limits:
  - per-ip-shaping: 21 gateways, each a shared exit used by many users; the vendor asks for donations because capacity is funded by users ('approximately $60 USD per person per year') [1]
- limits note: The pages read state no byte quota, device count or rate. The service has no account, so no per-account limit can be enforced by a login.
- binding note: No quota or rate is published and no account exists to enforce one; the open question is capacity (a donation-funded service with 21 gateways), which the limit vocabulary does not name.
- interface detail: A tunnel with desktop and Android apps (RiseupVPN, built on the Bitmask code) and a published JSON service configuration. Protocols: OpenVPN (AES-256-GCM) on every gateway. UDP: yes, on ports 53, 80 and 1194 in both TCP and UDP. Port forwarding: unverified: no page read states it. SOCKS5: unverified: no page read states a SOCKS5 endpoint. Obfuscation: obfs4 over TCP port 443 on every gateway. BitTorrent: the legacy help page lists p2p as a use the VPN supports; no current page states a rule.
- tooling: The RiseupVPN app, or a plain OpenVPN client using the gateways, ports and cipher listed in the published configuration at api.black.riseup.net/3/config/eip-service.json (21 gateways, each with openvpn and obfs4 transports).
- composes with: A free tunnel exit: traffic leaves from the address of one of 21 gateways, so the upstream sees a shared hosting-network address.
- reliability: A donation-funded service run as 'an experiment to see if we can create a VPN service that is easy enough for everyone to use and that people will donate enough to sustain'; capacity and continuity depend on donations.
- notes: Duplicate of egress/riseup-vpn, which holds the offer: both records cite the same vendor page.
- evidence note: Documented for price, sign-up and the BitTorrent line; the protocol, UDP and obfuscation values are measured from the vendor's published service configuration (a probe of the JSON, status 200). The BitTorrent line comes from a legacy help page of unknown date, so it is the weakest value. Nothing was connected through the service.
- evidence:
  - [1] 2026-11-04: No account is needed. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: You just install it and run it—no configuration, no account registration.
  - [1] 2026-11-04: The service is donation-funded. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: The RiseupVPN service is entirely funded through donations from users.
  - [1] 2026-11-04: The vendor's stated cost per user per year is USD 60. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: The cost for us to offer RiseupVPN is approximately $60 USD per person per year.
  - [1] 2026-11-04: No IP logging is stated. | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: Unlike most other VPN providers, Riseup does not log your IP address.
  - [2] 2026-11-04: The help page states p2p works with the VPN. | capture: sha256:eb9f8ee87c43f720ea02b6fb467f6c0f70149b00f9363baaa9aa1998ca69212f | quote: The RiseupVPN bypasses these restrictions and, because you get your own IP, makes p2p applications work much better.
  - probe:api.black.riseup.net/eip-service 2026-11-04: The published service configuration answered. | capture: sha256:29d89876a30d3f90061ad6dd01b91cd3217217d9ed50e27cfba07ca44046d4ca | quote: "status": 200
  - [3] 2026-11-04: Each gateway offers OpenVPN on ports 53, 80 and 1194 over TCP and UDP. | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "ports": ["53", "80", "1194"], "protocols": ["tcp", "udp"], "type": "openvpn"
  - [3] 2026-11-04: Each gateway offers obfs4 on TCP 443. | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "ports": ["443"], "protocols": ["tcp"], "type": "obfs4"
  - [3] 2026-11-04: The OpenVPN data cipher is AES-256-GCM. | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "cipher": "AES-256-GCM"
  - [3] 2026-11-04: The gateways are not flagged as limited. | capture: sha256:363fa760a0cc49851de259be0422e5a4b077a3bd637fa53d574f58b254dbd618 | quote: "limited": false
  - [1] 2026-11-04: the vendor page that both records cite shows the same offer, which the egress record holds | capture: sha256:c1a049034a83cd97d62a5bd3847c63d1e30000061d8ad67b6afed65194e11144 | quote: no configuration, no account registration.
- sources:
  - [1] https://riseup.net/en/vpn
  - [2] https://crabgrass.riseup.net/riseuphelp+en/riseup-vpn
  - [3] https://api.black.riseup.net/3/config/eip-service.json

## Riseup Share

- `debrid/riseup-share` | fails-quota | evidence documented | binding retention-clamped | category temporary file host (client-side encrypted, 12 hours) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.656Z (live) | stale on 2026-12-04
- url https://share.riseup.net/
- free tier: Upload is currently limited to 50mb and files are stored no longer than 12 hours. | unit: none | metered on: none | read on: 2026-11-03 | source: [1]
- per-object cap: 50mb per file | source: [1]
- retention: stored no longer than 12 hours | source: [1]
- egress: No download volume or speed figure is published on the pages read. | metered: no | free allowance: not published | source: [1]
- identity: anonymous | detail: The page shows no login step.
- interface: cli, rest
- limits:
  - per-object-cap: upload limited to 50mb [1]
  - retention-clamped (binding): stored no longer than 12 hours [1]
- binding note: Twelve hours is the binding clock for any retrieval.
- interface detail: Up1 web upload with a Node.js command-line client linked from the page.
- tooling: Browser and the Up1 command-line client.
- composes with: A 50 MB cap and a 12-hour clock: a hand-off only.
- reliability: No status page was read.
- evidence note: Limits read on the operator page.
- evidence:
  - [1] 2026-11-03: cap 50 MB and a 12-hour storage limit | capture: sha256:46eaa9fff3c369604b697cc3ede6ad7ba3859f5f92b8a4ee027fedc47eac535c | quote: Upload is currently limited to 50mb and files are stored no longer than 12 hours!
- sources:
  - [1] https://share.riseup.net/
