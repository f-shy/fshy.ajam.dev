# stunl

> stunl.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/stunl/ | JSON https://fshy.ajam.dev/api/v1/entity/stunl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## stunl

- `egress/stunl` | fails-quota | evidence documented | binding volume-quota | category tunnel | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.stunl.com/
- price USD 0
- free tier: Free $0 /month - 2GB bandwidth/month - 1 tunnels - 1 hour sessions - HTTP/HTTPS, WebSocket tunneling - Multi-port tunnels - Custom tunnel IDs - 1 reserved subdomain - HTTP Inspector with webhook verification. | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 2GB bandwidth/month on Free; the docs add Anonymous Mode at 100 MB and 30 minutes.; ingress: http-only | metered: yes | free allowance: 2GB bandwidth/month on Free; the docs add Anonymous Mode at 100 MB and 30 minutes. | source: [1]
- identity: email | detail: An API key from portal.stunl.com. The docs say: Free tier with no credit card required. Anonymous mode needs no key at all. | country: None
- interface: cli, rest
- limits:
  - volume-quota (binding): 2 GB monthly bandwidth [1]
  - volume-quota (binding): 100 MB and 30 minutes in anonymous mode [2]
- binding note: 2 GB is 0.0018 TiB, so the monthly allowance is spent in about an hour of 1 TiB/month traffic; the 1-hour session cap binds even earlier on a long transfer.
- interface detail: stunl -port 3000 -id myapp; API key from portal.stunl.com.
- tooling: brew install stunl/tap/stunl or stunl.com/install.sh; stunl.yaml config file.
- composes with: Hosts an MCP or webhook endpoint on a free VM; for UDP it requires the $10 plan, which is cheaper than most VPS options but still a bill.
- reliability: Free tunnels expire after an hour; anonymous tunnels after 30 minutes and 100 MB.
- notes: The service markets itself at AI agents and MCP servers, which explains the HTTP-first free tier. UDP exists but is two tiers above free.
- evidence note: UDP on Pro is documented but not tested; a Pro trial run would confirm the UDP listener is a real raw port rather than a WebSocket frame.
- extras:
  - wg_path: inside-udp
  - wg_detail: UDP is a Pro feature. The CLI reference documents -protocol with the values http, tcp and udp, and the Pro tier lists HTTP, HTTPS, WebSocket, TCP, UDP tunneling, so a WireGuard datagram can only be carried on a paid plan.
  - ingress: http-only
  - volume_tib_month: 0.0018
  - volume_stated: 2GB bandwidth/month on Free; the docs add Anonymous Mode at 100 MB and 30 minutes.
  - bytes_transit: yes
  - transit_note: The stunl.io edge terminates TLS and relays to the local agent.
- evidence:
  - [1] 2026-10-23: Free tier 2 GB/month, 1 tunnel, HTTP/HTTPS and WebSocket only; Pro at $10/month adds TCP and UDP, 50 GB and no session limit.
  - [3] 2026-10-23: Free Tier: HTTP and WebSocket tunnels, 2GB monthly bandwidth, 60-minute sessions, no credit card.
  - [4] 2026-10-23: Protocol flag accepts http, tcp and udp; anonymous mode is limited to HTTP, 100MB and 30 minutes.
- sources:
  - [1] https://www.stunl.com/
  - [2] https://stunl.com/docs/anonymous
  - [3] https://stunl.com/docs/getting-started
  - [4] https://stunl.com/docs/cli-reference
