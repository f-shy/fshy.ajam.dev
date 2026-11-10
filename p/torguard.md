# TorGuard

> torguard.net | IP and proxies, Egress and tunnels; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/torguard/ | JSON https://fshy.ajam.dev/api/v1/entity/torguard.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## TorGuard (residential dedicated IP)

- `ip-proxy/torguard-residential` | qualifies-with-caveat | evidence unverified | binding none | category VPN with residential exit | tier residential dedicated IP
- needs card yes, phone no, ID no, institution no | verified 2026-11-03T08:33:43.034Z (live) | stale on 2026-11-18
- url https://torguard.net/
- price USD 19.99 per month per address; the product is priced per address, so no per-TB figure exists | parsed USD 19.99/mo
- free tier: No free tier. A residential dedicated IP is $19.99 per month, priced separately from the datacenter dedicated IP. | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: The unit of sale is the address, not a byte. The $19.99 buys one dedicated residential exit for a month, which is why no byte figure belongs in this field.
- per-object cap: not applicable | source: [1] | note: The product is one exit address. Nothing is stored, so the largest-single-object question has no subject here.
- retention: not applicable: an address, not stored bytes; how long one $19.99 payment holds the same address was not established | source: [1] | note: Address persistence policies across subscription renewal intervals are not stated in vendor documentation.
- egress: No traffic allowance or cap is published for the residential dedicated IP; the $19.99 per month is charged per address, so nothing read on 2026-10-24 prices traffic out per byte. | metered: no | free allowance: none published | source: [1]
- identity: card | detail: Card. There is no free tier, so the address is bought at $19.99 per month and a working card is what holds it. The facts name no second gate.
- interface: cli
- limits note: The one constraint found is the address count: $19.99 buys a single dedicated residential exit, so every request in the month presents from one IP and a second concurrent exit means a second subscription. No traffic allowance, request-rate figure or daily-volume limit was published in anything read on 2026-10-24, so no vocabulary kind carries a number here. Whether a fair-use ceiling exists is unstated, which is not the same as absent.
- binding note: Nothing in the vocabulary fails at 45 GB/month across about 599,000 requests, which averages roughly 14 requests a minute: no traffic allowance and no request-rate figure is published to hit. The ceiling that arrives first is structural and outside the vocabulary, because one address is the entire product, so a block on that IP stops every request at once and there is no second exit to fail over to without a second $19.99 subscription.
- interface detail: Reached as a tunnel exit: a user points its VPN client at the assigned address. The protocol list was not read, because every torguard.net path tried on 2026-10-24 returned HTTP 403 'Just a moment...'.
- tooling: A standard VPN client that consumes the config for the assigned address. Which protocols the residential product supports was not established, and no API for ordering or choosing the address was found. A missing wrapper is not a reason to reject an exit address; a tunnel client is all this shape needs.
- composes with: One residential exit in front of the Workers AI gateway: the gateway keeps its Cloudflare identity, and only the traffic that must not originate from a datacenter egresses through this address.
- reliability: One address carries the reputation of everything sent through it, so a block hits all ~599,000 monthly requests at once and there is no second exit to fail over to.
- notes: The residential arm of the TorGuard product, recorded separately from egress/torguard, which prices the standard plans and port forwarding. Two records for one vendor is correct here because the tiers differ and a reader acts on one. So the sentence is left unverified and named as the caveat rather than repeated as fact. That is the one claim this topic says never survives a registry check, so quoting it would have been the expensive error. What settles it: one purchase, then one RIPE query on the assigned address, answering three things at once, which ASN announces the address, whether that ASN is a consumer ISP or a hosting provider, and whether the address appears in that ISP's own whois. One sample is one sample: a single purchase establishes one address and not the class of the inventory, so the record should name the address that was tested. The price is one sample too. The probe row above records the wall, not a confirmation of the number. Whether that sentence covers this add-on was not established either, so it is not used in egress.terms here. binding is none because no constraint with a number was published. Rather than file an invented entry, limits is empty and limits_note carries the address-count prose, which is the shape egress/airvpn used for its structural ceilings. Until that enum is extended, records here will use cli and put the protocol in interface_detail, as this one does.
- evidence note: The price and the card gate are documented: both come from the vendor's own page, read 2026-10-24. The claim the caveat rests on, that the exit is residential and leased directly from major ISPs, could not be checked, because the server list and every other torguard.net path tried returned HTTP 403 'Just a moment...' and no inventory or ASN is published. That is the weakest rung among the fields the verdict depends on, so the record takes it. One purchase plus one RIPE query on the assigned address moves it to measured.
- extras:
  - rung: 5
  - rung_note: The product is judged on its registration class, whether the address is announced by a consumer ISP or by a hosting provider, which is rung 5 rather than an ASN or a subnet.
  - price_usd_month: 19.99
  - price_basis: per dedicated residential address, per month, priced separately from the datacenter dedicated IP
  - address_kind: residential dedicated IP
  - comparison: cheapest per-address residential product found in this topic's research
  - isp_origin_claim: leased directly from major ISPs
  - isp_claim_status: documented as a vendor statement, not checked against a registry: the vendor says the addresses are leased directly from major ISPs and terminate on servers it operates on bare metal in data centers, with the upstream ISP named for each US location (Spectrum, Sprint, AT&T, Windstream, Atlas); no per-address inventory or ASN is published, and the server list page returned no list.
  - isp_claim_settled_by: one purchase plus one RIPE query on the assigned address
- evidence:
  - [1] 2026-10-24: A residential dedicated IP is sold at $19.99 per month and is priced separately from the datacenter dedicated IP; it is the cheapest per-address residential product found in this topic's research.
  - probe:https://torguard.net/ 2026-10-24: Two fetch paths, curl with a browser user agent and the harness extractor, both returned HTTP 403 carrying the Cloudflare challenge text 'Just a moment...'. The server list and any ASN or ISP inventory were therefore unreadable, which is why the residential-origin claim stays unverified rather than quoted.
  - [2] 2026-11-03: the residential IP VPN is listed at 19.99 per month on the vendor's page | capture: sha256:0b1a4de8532928371f53c759809e3750fdf2fbade0615a2c804c264db80a4754 | quote: $$19.99//month
  - [2] 2026-11-03: the vendor's product page states that the residential addresses are leased directly from major ISPs | capture: sha256:0b1a4de8532928371f53c759809e3750fdf2fbade0615a2c804c264db80a4754 | quote: Our residential IPs are leased directly from major ISPs, making your connection indistinguishable from a regular home internet user.
  - [2] 2026-11-03: the vendor states the addresses are legacy residential addresses leased from major ISPs in the US and UK | capture: sha256:0b1a4de8532928371f53c759809e3750fdf2fbade0615a2c804c264db80a4754 | quote: Our Residential IP VPN service uses legacy residential IP addresses leased directly from major ISPs in the US and UK.
  - [3] 2026-11-03: the vendor states the exits are servers it controls, not residential proxies run through someone else's connection | capture: sha256:9188f29822d05f2f9d8de3e07339a4f242ee0391ba38b131f95d4793931b2a5b | quote: they are high-quality, fully controlled servers leased by TorGuard and used exclusively for our [Residential IP VPN](https://torguard.net/dedicated-ip-vpn/) service.
  - [3] 2026-11-03: the vendor names the upstream ISP for each residential location, for example Virginia is AT&T and Windstream | capture: sha256:9188f29822d05f2f9d8de3e07339a4f242ee0391ba38b131f95d4793931b2a5b | quote: VA (Virginia) – Powered by ATT and Windstream
  - [4] 2026-11-03: the vendor states the residential VPN servers run on its own bare metal servers in data centers | capture: sha256:30605a6689e4f7867203cac330fba2639d218e4c3b4f49901e08850bfa8c73c8 | quote: TorGuard’s residential VPN IP servers are controlled and operated by TorGuard on bare metal servers in trusted data center locations.
- sources:
  - [1] https://torguard.net/
  - [2] https://torguard.net/dedicated-ip-vpn/
  - [3] https://blog.torguard.net/torguard-launches-new-residential-ip-range-in-lax/
  - [4] https://blog.torguard.net/new-residential-ip-vpn-servers-online/

## TorGuard (standard)

- `egress/torguard` | paid-only | evidence documented | binding write-gated | category vpn port forward | tier standard
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:01:05.027Z (live) | stale on 2026-12-05
- url https://torguard.net/indexori.php?rp=/knowledgebase/276/Getting-Started-with-TorGuard-Port-Forwarding.html
- price USD 9.99 per month or USD 29.99 per year (standard); USD 12.99 or USD 59.50 (pro); USD 14.99 or USD 64.99 (premium) | parsed USD 9.99/mo
- free tier: No free tier. Plan block read 2026-10-23: Standard $9.99 per month or $29.99 per year, Pro $12.99 per month or $59.50 per year, Premium $14.99 per month or $64.99 per year, and Port Forwarding appears in the feature list of every plan. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: Unlimited Speeds and Unlimited Bandwidth appear in the feature list of every plan.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: An account in the client area is required to submit a Port Forward Request; payment can be made by card or crypto, and the site markets an anonymous purchase path. | country: None
- interface: cli
- limits:
  - write-gated (binding): a port is a reviewed request, not a self-service toggle: enter the public VPN IP, choose protocol and port, click Submit Request. Note that on occasion the request may need to be approved. [2]
  - per-ip-shaping: the forward is bound to one public VPN IP: enter the public VPN IP you had taken from the TorGuard software [2]
- binding note: Bandwidth is stated as unlimited, so volume does not bind. The gate is the request workflow plus its approval step, and the requirement to name the exact server IP, which means the port is only useful while the address stays on that server.
- interface detail: Client area under Services, Port Forward Request; no public API for port reservation in the pages read. Protocols: OpenVPN over UDP, TCP or Stealth on all servers, WireGuard, OpenConnect, Stunnel and IKEv2. Obfuscation: Stealth VPN wraps OpenVPN in SSL/TLS on an HTTPS port, and Shadowsocks is built in. A SOCKS5 proxy (with SSL and Shadowsocks) is sold as a separate Premium Proxy product, not in the VPN plan. All USA servers are P2P optimized with port forwarding.
- tooling: Client area request form; wg-quick or the TorGuard app for the tunnel.
- composes with: A static shared or dedicated IP plus a requested port gives a fixed endpoint a service on a free VM can publish behind.
- reliability: A port request can sit in approval; the forward is tied to one server IP, so moving servers loses ingress until a new request.
- notes: The first is supported by the per-tier device and IP lines; the second remains open. TorGuard root and product pages intermittently returned HTTP 530 while the knowledgebase path served normally, so the KB path was used.
- evidence note: Measured would need an account, an approved port and a byte count. The plan prices were extracted from the served HTML of the vendor page rather than from its rendered price widget, which is why they are listed as read rather than inferred.
- extras:
  - wg_path: native-conf
  - wg_detail: WireGuard is a listed transport and the port request names the tunnel type: select a protocol and then select the VPN port or Tunneltype, by choosing openconnect or wireguard you will use that tunneltype for your port forward.
  - ingress: tcp+udp
  - volume_stated: Unlimited Speeds and Unlimited Bandwidth appear in the feature list of every plan.
  - bytes_transit: yes
  - transit_note: Traffic crosses TorGuard servers at the named public VPN IP.
- evidence:
  - [2] 2026-10-23: Port forwarding is a client-area request against a named public VPN IP, TCP or UDP, all ports above 2048 allowed, and requests may need approval.
  - [1] 2026-10-23: Unlimited Speeds, Unlimited Bandwidth, Port Forwarding and SSL VPN via WireGuard appear in the feature list; the HTML carries Standard $9.99 or $29.99 per year, Pro $12.99 or $59.50, Premium $14.99 or $64.99.
  - [3] 2026-11-04: OpenVPN runs over UDP, TCP or Stealth on every server | capture: sha256:8cf9a33cbf4b970a646462b0d4f96e3b47efd3cce202746dce8cb896ace4b474 | quote: offers both UDP, TCP and Stealth connection options to all VPN servers
  - [1] 2026-11-04: OpenConnect is offered | capture: sha256:591c94efc2fe2167da1e05c62c12e41e845ae24241e761f38af44435293728ad | quote: SSL VPN via OpenConnect
  - [4] 2026-11-04: Stealth VPN is the obfuscation layer | capture: sha256:9db1c3f38401b7f30e797a1e7ff2b4ba64c733414669630a9be1a7c22967662e | quote: We wrap and obfuscate the header in SSL/TLS encryption and reroute traffic through a typical HTTPS port.
  - [5] 2026-11-04: SOCKS5 is a separate Premium Proxy product | capture: sha256:1d7765ac5bbc072c98200ca287421c7866f69b579369c9db9e76abeac92494ae | quote: featuring SSL, SOCKS5, and Shadowsocks
  - [6] 2026-11-04: USA servers are P2P optimized | capture: sha256:de1adf854b24cad549a119515adf0a78506fdb63e5d4505014619a5a76bdaf66 | quote: All USA servers are P2P optimized with port forwarding support
  - [1] 2026-11-04: the Standard plan is $29.99 for 12 months | capture: sha256:591c94efc2fe2167da1e05c62c12e41e845ae24241e761f38af44435293728ad | quote: Billed <s>$59.99.00</s> <b>$29.99</b> every 12 months.*
- sources:
  - [1] https://torguard.net/anonymoustorrentvpn.php/
  - [2] https://torguard.net/indexori.php?rp=/knowledgebase/276/Getting-Started-with-TorGuard-Port-Forwarding.html
  - [3] https://blog.torguard.net/openvpn-service-udp-vs-tcp-which-is-better/
  - [4] https://torguard.net/stealth-vpn/
  - [5] https://torguard.net/anonymous-proxy/
  - [6] https://torguard.net/united-states-vpn/
