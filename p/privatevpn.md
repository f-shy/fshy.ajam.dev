# PrivateVPN

> privatevpn.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/privatevpn/ | JSON https://fshy.ajam.dev/api/v1/entity/privatevpn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PrivateVPN

- `egress/privatevpn` | paid-only | evidence documented | binding per-ip-shaping | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://privatevpn.com/features/vpn-port-forwarding/
- price USD 9.90 per month; USD 6.00 per month on 3 months; USD 2.00 per month on 36 months (72.00) | parsed USD 2/mo
- free tier: No free tier. Prices read 2026-10-23: 1 Month 9.90 USD per month; 3 Months 6.00 USD per month (17.99 USD); 12 Months plus 36 Months 2.00 USD per month (72.00 USD billed every 36 months). | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: All plans include all PrivateVPN apps, 24/7 customer support, and high-speed unlimited bandwidth.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: Checkout takes an email and password plus a tax residence: Create Secure Account with Email, Password, Password repetition. | country: None
- interface: cli
- limits:
  - per-ip-shaping (binding): only selected servers forward: PrivateVPN supports port forwarding on selected servers. Availability may vary by location. [2]
- binding note: Bandwidth is stated as unlimited, so volume does not bind; the port is assigned by the server, which makes server choice the constraint that fails first when a location without forwarding is picked.
- interface detail: App-based activation per the feature page.
- tooling: Official app; protocol support was not read.
- composes with: Would serve as an endpoint for a service on a free VM if the assigned port holds.
- reliability: unverified: no page read states port lifetime or reconnect behaviour.
- notes: The page is written for a reader who wants P2P connectivity, not ingress, and it never states whether the assigned port survives a reconnect. That single missing sentence is the difference between usable and not, and it was not answered by the pages read, so it stays open rather than guessed.
- evidence note: Measured would need an account, a port and a byte count. The WireGuard config path is the weakest field and is left unknown rather than assumed.
- extras:
  - wg_path: unknown
  - wg_detail: unverified: the port-forwarding page describes the assignment but not the config format. PrivateVPN assigns you a specific port on the VPN server, and external traffic reaches that open port on the VPN server. Whether a WireGuard .conf can be downloaded was not established in the pages read.
  - ingress: tcp+udp
  - volume_stated: All plans include all PrivateVPN apps, 24/7 customer support, and high-speed unlimited bandwidth.
  - bytes_transit: yes
  - transit_note: Traffic crosses PrivateVPN servers on the selected location.
- evidence:
  - [2] 2026-10-23: Port forwarding exists on selected servers; the flow is connect, get an assigned port, receive inbound traffic on it; no port count or range stated.
  - [1] 2026-10-23: Plan prices and the sentence All plans include all PrivateVPN apps, 24/7 customer support, and high-speed unlimited bandwidth.
- sources:
  - [1] https://privatevpn.com/prices/
  - [2] https://privatevpn.com/features/vpn-port-forwarding/
