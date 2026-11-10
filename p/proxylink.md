# ProxyLink

> proxylink.dev | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proxylink/ | JSON https://fshy.ajam.dev/api/v1/entity/proxylink.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ProxyLink

- `egress/proxylink-dev` | trial-only | evidence documented | binding none | category WireGuard overlay with public TCP and UDP port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://proxylink.dev/docs/proxy-links/tcp-udp
- price USD 0 during early access
- free tier: ProxyLink is currently free during early access, with no usage limits except a 200 MB recording cap; the published plan grid gives Free "3 proxy links (HTTP/HTTPS only)" and "No tunnels", and puts TCP and UDP behind the Developer plan at EUR 17/month | unit: users | metered on: identity-count | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: no usage limits except those noted below; the only noted limit is 'Recording storage is limited to 200 MB per account'; ingress: tcp+udp | metered: no | free allowance: none published | source: [2]
- identity: email | detail: 'Early Access - everything free, no credit card.' and 'No card. No trial countdown.' The registration form at app.proxylink.dev/register was not read. | country: None
- interface: cli
- limits note: The same vendor publishes a paid grid that gives Free zero tunnels: Free is "3 proxy links (HTTP/HTTPS only)", "No tunnels"; Developer is EUR 17/month and carries "5 tunnels"; MSP is EUR 69/month and carries 300. The TCP/UDP doc says "TCP links require an active tunnel (VPN)", and the pricing FAQ says "TCP links, browser SSH/RDP/VNC, and LAN access all require a tunnel (Developer plan or above)". So the free tier has no published TCP or UDP path once early access ends.
- binding note: No byte quota, no rate and no published consumption meter exist, so nothing in the vocabulary fails in bytes; what ends the arrangement is the end of early access, and the exit price is already published at EUR 17/month
- interface detail: 'import the .conf file in under 2 minutes'; the dashboard assigns the public port
- tooling: any WireGuard client; browser dashboard; MikroTik one-click autoconfig
- composes with: The only managed service found that issues a WG peer and forwards arbitrary TCP and UDP, and the free version of that path is time-limited: today everything is free, after early access the free plan is HTTP proxy links only
- reliability: The free arrangement is bounded by the early-access period rather than by a quota; the vendor states the post-launch position in its own plan grid
- notes: An adversarial re-read on 2026-10-23 opened proxylink.dev/pricing, which this record had never read. It publishes a free plan with no tunnels at all, and the TCP and UDP docs say a TCP link requires an active tunnel. The early-access sentence is still true today and it is the whole of the free path. Verdict moved from qualifies-with-caveat to trial-only because the free arrangement has a published end and a published price.
- evidence note: A live UDP packet to tcp.proxylink.dev:PORT and back from a peer would raise this to measured.
- extras:
  - wg_path: native-conf
  - wg_detail: 'OpenWRT, pfSense, OPNsense, TP-Link - import the .conf file in under 2 minutes.' One peer covers the account: 'issue them one WireGuard peer for your whole account, not one per client site'.
  - ingress: tcp+udp
  - volume_stated: no usage limits except those noted below; the only noted limit is 'Recording storage is limited to 200 MB per account'
  - bytes_transit: yes
  - transit_note: ProxyLink's proxy cluster in Hetzner Germany terminates the public side and relays over WireGuard to the peer
- evidence:
  - [2] 2026-10-23: UDP and TCP tunnel links, the tcp.proxylink.dev host with a per-link port, and the UDP transparency sentence
  - [1] 2026-10-23: 'currently free during early access ... there are no usage limits except those noted below' and the 200 MB recording cap
  - [3] 2026-10-23: .conf import, one WireGuard peer per account, and EU-only proxying on Hetzner Germany
  - [4] 2026-10-23: Free plan: '3 proxy links (HTTP/HTTPS only)', 'No tunnels', 'No browser terminals', 'No custom domains'; Developer 'EUR 17 / month' with '5 tunnels'; FAQ: 'TCP links, browser SSH/RDP/VNC, and LAN access all require a tunnel (Developer plan or above)'
- sources:
  - [1] https://proxylink.dev/terms
  - [2] https://proxylink.dev/docs/proxy-links/tcp-udp
  - [3] https://proxylink.dev/
  - [4] https://proxylink.dev/pricing
