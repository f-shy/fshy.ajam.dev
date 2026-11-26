# Fnat

> fnat.cc | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fnat/ | JSON https://fshy.ajam.dev/api/v1/entity/fnat.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fnat

- `egress/fnat` | fails-quota | evidence documented | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://www.fnat.cc/shop
- price USD 0
- free tier: Free plan: CNY 0 per month, permanently free, 3 to 5 tunnels, bandwidth 5 to 20 Mbps, 20 to 50 G of traffic. [translated] | unit: GB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: The shop page states 20 to 50 G of traffic for the free plan while the same page and the home page advertise 'unlimited traffic, no speed limit'. The two statements are on the same vendor.; ingress: udp | metered: yes | free allowance: The shop page states 20 to 50 G of traffic for the free plan while the same page and the home page advertise 'unlimited traffic, no speed limit'. The two statements are on the same vendor. | source: [1]
- identity: email | detail: Registration on the console; the site says nothing about real-name on the pages read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 20 to 50 GB per month [1]
  - per-ip-shaping: 5 to 20 Mbps [1]
- binding note: Even the top of the range, 50 GB, is about 0.045 TiB, so the byte quota fails first and by a wide margin.
- interface detail: frpc with a console-generated config.
- tooling: frpc plus a console
- composes with: Unusable for 1 TiB; at 50 GB it is a debugging tunnel.
- reliability: No reliability report found; the site claims 8 BGP nodes and 99.9 percent availability without evidence.
- notes: This is the cleanest example in the sweep of an unlimited-traffic headline that its own pricing table contradicts. Treat the 20 to 50 GB as the number; the headline is marketing copy on the same page.
- evidence note: Pricing, mapped port allocations and protocol specifications are documented on vendor storefront pages.
- extras:
  - wg_path: inside-udp
  - wg_detail: The site advertises UDP protocol penetration and an FRP UDP option for game servers; a WG datagram fits inside, but no node list with a UDP flag was found.
  - ingress: udp
  - volume_tib_month: 0.018
  - volume_stated: The shop page states 20 to 50 G of traffic for the free plan while the same page and the home page advertise 'unlimited traffic, no speed limit'. The two statements are on the same vendor.
  - bytes_transit: yes
  - transit_note: Fnat BGP nodes relay the datagrams.
- evidence:
  - [1] 2026-10-23: free plan lists 20 to 50 G of traffic next to an 'unlimited traffic' headline
  - [2] 2026-10-23: home page repeats 'unlimited traffic, no speed limit'
- sources:
  - [1] https://www.fnat.cc/shop
  - [2] https://www.fnat.cc/
