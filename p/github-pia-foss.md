# Private Internet Access

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-pia-foss/ | JSON https://fshy.ajam.dev/api/v1/entity/github-pia-foss.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Private Internet Access

- `egress/private-internet-access` | paid-only | evidence documented | binding retention-clamped | category vpn port forward | tier paid
- needs card no, phone no, ID no, institution no | verified 2026-11-04T10:29:23.996Z (live) | stale on 2026-12-05
- url https://github.com/pia-foss/manual-connections
- price USD 11.95 per month; USD 3.99 per month on 1 year (USD 47.88 first year, renewing at USD 47.88); USD 2.03 per month on 3 Years + 4 Months, autorenewing at USD 81.20 every 3 years | parsed USD 2.03/mo
- free tier: No free tier. Buy page 2026-11-04: 1 Month $11.95 per month; 1 Year $3.99 per month billed at $47.88 first year, then renews annually at $47.88; 3 Years + 4 Months $2.03 per month, autorenews at $81.20 every 3 years. | unit: none | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: unverified: the buy page states Unlimited Device Security without a published byte allowance.; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: An account with credentials used by the scripts as PIA_USER and PIA_PASS; payment by card or PayPal. | country: None
- interface: cli, rest
- limits:
  - retention-clamped (binding): a bound port is deleted if the bind is not renewed: Call /bindPort every 15 minutes, or the port will be deleted. The port signature is valid for two months: All ports currently expire after 2 months. [2]
  - write-gated: port forwarding is disabled server side in the United States: Port Forwarding is disabled on server-side in the United States. [2]
- binding note: No byte cap is stated, so the binding constraint is the 15-minute bind renewal: the port exists only while a loop keeps re-signing it. That is the same class of failure as Proton's lease but with a 900-second period instead of 60.
- interface detail: Token and port are HTTP calls to the connected gateway on port 19999 (/getSignature, /bindPort); the scripts wrap them.
- tooling: pia-foss manual-connections scripts with wg-quick and curl/jq, or the official app. Protocols: WireGuard and OpenVPN with UDP or TCP transport, or Automatic. A SOCKS5 proxy with separate credentials and a Shadowsocks proxy (obfuscation) are offered through the Multi-Hop setting. P2P traffic is supported on all server locations.
- composes with: A token endpoint plus a bind loop is a five-line cron job on a free VM; the VM then holds a stable public UDP endpoint for the life of the signature.
- reliability: Losing the 15-minute renewal loop silently drops the port mapping while the tunnel stays up. United States servers cannot forward at all.
- notes: VPN provider offering port forwarding on selected server regions. Port forwarding scripts and API integration are maintained in official GitHub repositories.
- evidence note: Measured would need a token, a bound port, a live UDP request through it and a byte count. The 15-minute and 2-month sentences are in the vendor's own repository README, read.
- extras:
  - wg_path: registration-api
  - wg_detail: Run with PIA_PF=true to bind the port on the same connection.
  - ingress: tcp+udp
  - volume_stated: unverified for a byte figure: the buy page states Unlimited Device Security but no page read states a traffic allowance. PIA is widely described as unmetered, which did not confirm from a vendor sentence.
  - bytes_transit: yes
  - transit_note: Traffic crosses the PIA server a user is bound to; the port is only valid on the gateway of that server.
- evidence:
  - [2] 2026-10-23: Native WireGuard plus port forwarding from vendor scripts; port signature valid 2 months; /bindPort must be called every 15 minutes or the port is deleted; port forwarding is off in the United States.
  - [1] 2026-10-23: Prices: $11.95 monthly, $3.99 per month on 1 year at $47.88, $2.03 per month on 3 years at $79.
  - [3] 2026-10-23: Indexed copy of the vendor article: a random port is automatically assigned, only specific locations support port forwarding, and a manual option exists for non-app clients. The live path returned 404 from the restructured helpdesk.
  - [4] 2026-11-04: the 1 Year plan is $47.88 for the first year and renews annually at $47.88 | capture: sha256:08d0cfe4336400597c8147da26998530873da130415a14e4f0f2b9b677a7e439 | quote: Billed at $47.88 first year and then autorenews annualy at $47.88
  - [4] 2026-11-04: the 3 Years + 4 Months plan renews at $81.20 every 3 years | capture: sha256:08d0cfe4336400597c8147da26998530873da130415a14e4f0f2b9b677a7e439 | quote: Autorenews at $81.20 every 3 years
  - [5] 2026-11-04: P2P and BitTorrent traffic is allowed on every PIA server location | capture: sha256:dcd32689864d28a4b6b0ad9bfd18ca2442bbe9ae912868571f8c9c1861975931 | quote: PIA supports P2P traffic on all server locations.
  - [6] 2026-11-04: the iOS app lists WireGuard and OpenVPN | capture: sha256:31b459618a7d744c311c20e109f5329f469cfbaa873d3af17ca1024ab5042522 | quote: The PIA app supports two: WireGuard and OpenVPN.
  - [6] 2026-11-04: the transport is selectable between UDP and TCP | capture: sha256:31b459618a7d744c311c20e109f5329f469cfbaa873d3af17ca1024ab5042522 | quote: Choose between UDP and TCP.
  - [7] 2026-11-04: Multi-Hop offers a Shadowsocks proxy and a SOCKS5 proxy | capture: sha256:62f6e92b793ee7e0465be763866067f27b9c28a8c07acc0c00d8afebe7bd5376 | quote: When you open the Multi-Hop tab, you see two options: Shadowsocks and SOCKS5 Proxy.
  - [7] 2026-11-04: Shadowsocks is the obfuscation option | capture: sha256:62f6e92b793ee7e0465be763866067f27b9c28a8c07acc0c00d8afebe7bd5376 | quote: Shadowsocks is an encrypted proxy designed to disguise VPN traffic as regular internet traffic.
  - [4] 2026-11-04: the 3 Years + 4 Months plan renews at 81.20 USD every 3 years | capture: sha256:08d0cfe4336400597c8147da26998530873da130415a14e4f0f2b9b677a7e439 | quote: Autorenews at $81.20 every 3 years
- sources:
  - [1] https://www.privateinternetaccess.com/buy-vpn-online
  - [2] https://github.com/pia-foss/manual-connections
  - [3] https://helpdesk.privateinternetaccess.com/kb/articles/pdf/how-do-i-enable-port-forwarding-on-my-vpn
  - [4] https://www.privateinternetaccess.com/pages/buy-vpn-online
  - [5] https://www.privateinternetaccess.com/vpn-server
  - [6] https://helpdesk.privateinternetaccess.com/hc/en-us/articles/46816425727259-Understanding-iOS-Settings-and-Protocols
  - [7] https://helpdesk.privateinternetaccess.com/hc/en-us/articles/46776477273627-Understanding-the-Multi-Hop-Feature
