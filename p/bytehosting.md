# ByteHosting

> bytehosting.cloud | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/bytehosting/ | JSON https://fshy.ajam.dev/api/v1/entity/bytehosting.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ByteHosting

- `egress/bytehosting-xeon-6gb` | paid-only | evidence documented | binding volume-quota | category cheap-egress VPS (KVM, Frankfurt, dedicated IPv4) | tier Xeon 6GB
- identity a placeholder: card and phone unknown | verified 2026-11-04T05:55:17.777Z (live) | stale on 2026-12-05
- url https://bytehosting.cloud/all-products
- free tier: No free tier. Xeon 6GB is EUR 3.49 a month, prepaid, with a 5 TB bandwidth line and 1 IPv4 address. | unit: none | metered on: none | read on: 2026-11-04 | source: [1] | note: The aggregator lists it at EUR 3.49 a month with a 1Gbps port and 1x IPv6; the vendor page read lists no port speed and no IPv6 line.
- per-object cap: not applicable: a VPS, not an object store | source: [1]
- retention: not applicable | source: [1]
- egress: 5 TB bandwidth, period not stated on the plan page. | metered: yes | free allowance: 5 TB, period not stated | source: [1]
- identity: email | detail: unverified: behind a sign-up. The vendor states that all payments are prepaid; no sign-up form was read.
- interface: ssh
- limits:
  - volume-quota (binding): 5 TB bandwidth, period and overage behaviour not published on the pages read [1]
- limits note: The terms page names no fair-use figure and no shaping rule.
- binding note: The only published cap is the 5 TB bandwidth line; the period is not stated.
- interface detail: KVM VPS in Frankfurt am Main with one IPv4 address.
- tooling: Any SSH client; a panel at panel.bytehosting.cloud handles orders.
- composes with: One dedicated IPv4 address, so inbound TCP and UDP can be bound on the VPS itself; no port filter or protocol list is published on the pages read.
- reliability: The terms list Tor exit nodes, DDoS relay, unauthorised port scans, torrenting and cryptocurrency mining as grounds for immediate suspension with no refund.
- notes: Billing and location per the vendor home page: KVM VPS deployed in Frankfurt am Main.
- evidence note: Plan table and terms read on 2026-11-04; the port speed and the overage rule are unverified.
- extras:
  - nat_ports: not applicable: one dedicated IPv4
  - ipv6: unverified: the aggregator lists 1x IPv6, the vendor page lists none
  - udp_forwarding: unverified: not stated
  - routed_ipv6_prefix: unverified
  - inbound_ipv4_ports: unverified: no port filter published
  - term: monthly, prepaid
  - virtualization: KVM
- evidence:
  - [1] 2026-11-04: the Xeon 6GB block lists 5 TB Bandwidth | capture: sha256:a00eca6a974d44e2809126c1801f4debf8b1e626e8013966da885807ae450e74 | quote: 5 TB Bandwidth
  - [1] 2026-11-04: the Xeon 6GB block is priced at EUR 3.49 a month | capture: sha256:a00eca6a974d44e2809126c1801f4debf8b1e626e8013966da885807ae450e74 | quote: € 3.49 / month
  - [1] 2026-11-04: the plan carries one IPv4 address | capture: sha256:a00eca6a974d44e2809126c1801f4debf8b1e626e8013966da885807ae450e74 | quote: 1 IPv4 Address
  - [2] 2026-11-04: all payments are prepaid | capture: sha256:ac4c2120974d9492cb9c9f98f313d12f830d78ad0a700c6aa54f9ba98e4848e2 | quote: All payments with ByteHosting are prepaid
  - [3] 2026-11-04:  | capture: sha256:be8b111603e2cd590fa440fea477a8e94f800a4e9da82c9250b547899d0f22b7 | quote: Operating TOR exit nodes.
  - [4] 2026-11-04: serverdeals lists ByteHosting Xeon 6GB at EUR 3.49 a month with 5 TB and a 1Gbps port | quote: #### EUR 3.49 / month
- sources:
  - [1] https://bytehosting.cloud/all-products
  - [2] https://bytehosting.cloud/
  - [3] https://bytehosting.cloud/terms-of-service
  - [4] https://serverdeals.cc/
