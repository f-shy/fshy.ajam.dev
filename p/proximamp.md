# ProximaTunnel

> proximamp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/proximamp/ | JSON https://fshy.ajam.dev/api/v1/entity/proximamp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ProximaTunnel

- `egress/proximatunnel` | fails-quota | evidence unverified | binding volume-quota | category udp port forward | tier free
- needs card unknown, phone unknown, ID no, institution no | verified 2026-11-04T06:52:59.171Z (live) | stale on 2026-11-19
- url https://proximamp.com/en/tunnel
- price USD 0
- free tier: Free: 2 TCP, UDP or HTTPS tunnels, 30 GB a month. Cheapest paid plan: Pro, 250 ₽ for 30 days. | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Free plan: 30 GB a month of traffic and 2 TCP, UDP or HTTPS tunnels; which direction is metered is not stated.; ingress: tcp+udp | metered: no | free allowance: 30 GB a month | source: [1]
- identity: email | detail: A Windows client download and an account are implied but not shown; no card, phone or identity document is mentioned on the tunnel page, and the signup flow was not read. | country: None
- interface: unknown
- limits:
  - volume-quota (binding): free plan: 30 GB a month and 2 tunnels [1]
- binding note: The free plan's 30 GB a month of traffic is the first failure; it is far below a 1 TiB/month need. TCP and UDP are both on the free plan, so the protocol is not the wall. The number is the vendor's own claim in its comparison table.
- interface detail: Graphical client with a single tunnel checkbox; no CLI or API is named.
- tooling: ProximaClient for Windows.
- composes with: A Windows client is a poor fit for a headless free VM; it would expose a service from a desktop, not from a Linux box.
- reliability: Windows client only on the page read; no published limits, so throttling terms are unknown.
- notes: The vendor's own comparison table puts it beside tuna.am, fxTunnel, ngrok and Cloudflare Tunnel, and claims UDP and TCP on every plan, an HTTPS link with no interstitial page, and a request inspector. The download is a Windows client. Free: 30 GB a month.
- evidence note: The free allowance is read from the vendor's comparison table on the tunnel page (checked October 25, 2026, per the page); no in-client plan screen was read.
- extras:
  - wg_path: inside-udp
  - wg_detail: The page says: One checkbox raises a TCP and UDP tunnel from your PC to the outside. A WireGuard handshake is an opaque UDP datagram and would pass through that path.
  - ingress: tcp+udp
  - volume_stated: Free plan: 30 GB a month and 2 TCP, UDP or HTTPS tunnels (vendor comparison table checked on October 25, 2026).
  - bytes_transit: yes
  - transit_note: ProximaMP relays between the PC and the public address.
- evidence:
  - [1] 2026-10-23: Both protocols: web and game connections, voice chats; one checkbox raises a TCP and UDP tunnel; plans promise more tunnels, traffic and speed without numbers.
  - [2] 2026-10-23: 404: the URL does not exist.
  - [1] 2026-11-03: the vendor's comparison table states the free plan: 2 TCP, UDP or HTTPS tunnels and 30 GB a month | capture: sha256:0aacf407366b29dba58aade74101a6e06625a7a0d1f48373d4e811abfc67c33f | quote: | Free | 2 TCP, UDP or HTTPS tunnels, 30 GB a month |
  - [1] 2026-11-03: the cheapest paid plan is Pro at 250 rubles for 30 days | capture: sha256:0aacf407366b29dba58aade74101a6e06625a7a0d1f48373d4e811abfc67c33f | quote: Pro: 250 ₽ for 30 days
  - [1] 2026-11-03: the vendor dates its comparison table to October 25, 2026 | capture: sha256:0aacf407366b29dba58aade74101a6e06625a7a0d1f48373d4e811abfc67c33f | quote: Checked on October 25, 2026 against the services’ pricing and documentation pages.
  - [1] 2026-11-04: the vendor's page states the free plan: 2 TCP, UDP or HTTPS tunnels and 30 GB a month | capture: sha256:0aacf407366b29dba58aade74101a6e06625a7a0d1f48373d4e811abfc67c33f | quote: | Free | 2 TCP, UDP or HTTPS tunnels, 30 GB a month |
- sources:
  - [1] https://proximamp.com/en/tunnel
  - [2] https://proximamp.com/en/pricing
