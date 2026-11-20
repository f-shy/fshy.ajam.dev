# IIS.PUB FRP

> iis.pub | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/iis/ | JSON https://fshy.ajam.dev/api/v1/entity/iis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IIS.PUB FRP

- `egress/iis-pub-frp` | fails-quota | evidence reported | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-07
- url https://frp.iis.pub/
- price USD 0
- free tier: Personal edition CNY 0 per month: 2 usable tunnels, 10 GB monthly traffic, TCP/UDP/HTTP/HTTPS tunnels. [translated] | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 10 GB monthly traffic on the personal edition.; ingress: udp | metered: yes | free allowance: 10 GB monthly traffic on the personal edition. | source: [1]
- identity: email | detail: Panel registration; no real-name statement on the page read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 10 GB per month [1]
- interface detail: frpc with a panel-issued config.
- tooling: part of interface detail
- composes with: Same role as the other 10 GB tiers: a debugging tunnel.
- reliability: No reliability report found.
- notes: One of several small public-frps panels that publish a 10 GB free tier; the shape is identical across them.
- evidence note: The numbers came from the site's extracted pricing block rather than a direct read of the panel; a direct read would raise the rung.
- extras:
  - wg_path: inside-udp
  - wg_detail: UDP tunnels are advertised on the free tier; a WG datagram can be carried, with the caveats of any frp UDP proxy.
  - ingress: udp
  - volume_tib_month: 0.0091
  - volume_stated: 10 GB monthly traffic on the personal edition.
  - bytes_transit: yes
  - transit_note: IIS.PUB nodes relay the datagrams.
- evidence:
  - [1] 2026-10-23: personal edition is 2 tunnels and 10 GB per month with TCP/UDP support
- sources:
  - [1] https://frp.iis.pub/
