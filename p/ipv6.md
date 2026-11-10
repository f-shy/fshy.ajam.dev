# IPv6rs

> ipv6.rs | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ipv6/ | JSON https://fshy.ajam.dev/api/v1/entity/ipv6.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IPv6rs

- `egress/ipv6rs` | paid-only | evidence documented | binding none | category IPv6 address provider (paid, unmetered) | tier monthly
- needs card yes, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.ipv6.rs/l/en-US/
- price USD 6.95/month | parsed USD 6.95/mo
- free tier: Monthly Plan: 5 Static Visible IPv6 Tunnels (VIPs), 1 Gbps Encrypted Tunnels, Free IPv4 Reverse Proxy, Port Forwarding, Tier-1 Bandwidth, Unmetered Traffic, $6.95/mo. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unmetered Traffic; ingress: tcp+udp | metered: no | free allowance: none published | source: [1]
- identity: card | detail: paid plan at $6.95/month; sign-in is by email address and the plan is bought, so a payment method is implied by the price and was not read as a form. | country: None
- interface: cli
- binding note: Unmetered traffic and 1 Gbps tunnels, so nothing in the vocabulary fails at 1 TiB/month. The gate is the subscription price, which is not a limit kind.
- interface detail: Cloud Seeder installers for Windows and macOS, or manual setup with their addresses
- tooling: Cloud Seeder (their client) or a manual WireGuard configuration
- composes with: a paid alternative to Route64 for the same job: a routed public prefix onto a machine that has no public address
- reliability: single small operator; the free IPv4 reverse proxy is listed as a feature of a paid plan, so a client without IPv6 cannot reach a service here without that proxy.
- notes: No free tier and no trial stated. The raw HTML is a Shells white-label shell titled 'KLB Vue Template' with a Realm name of shells.com, so nothing is readable without rendering; the numbers above come from the rendered markdown. Port forwarding on a public IPv6 is the ingress, so UDP is carried as routed IP rather than as a vendor feature.
- evidence note: the page is a client-rendered application; the price block was read from the rendered crawl, not the raw HTML, which returned a template shell.
- extras:
  - wg_path: extractable
  - wg_detail: No .conf is published without an account. Their client sets the tunnel up: 'Instantly launch and self host your favorite internet appliances with a click using Cloud Seeder ... or use our IPs to manually setup your own.' WireGuard is the sponsor logo and the transport in the how-it-works diagram.
  - ingress: tcp+udp
  - volume_stated: Unmetered Traffic
  - bytes_transit: yes
  - transit_note: IPv6rs carries the tunnel and its upstreams carry the routed prefix
- evidence:
  - [1] 2026-10-23: 'Unmetered Traffic', '5 Static Visible IPv6 Tunnels (VIPs)', 'Port Forwarding' and '$6.95/mo'
  - [2] 2026-10-23: a user that installs the tunnel, distributed as a signed installer
- sources:
  - [1] https://www.ipv6.rs/l/en-US/
  - [2] https://www.ipv6.rs/l/en-US/cloudseeder/
