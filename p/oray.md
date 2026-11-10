# Oray Peanut Hull

> oray.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/oray/ | JSON https://fshy.ajam.dev/api/v1/entity/oray.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Oray Peanut Hull (Huashengke)

- `egress/oray-peanut-hull` | fails-identity | evidence documented | binding write-gated | category tcp+udp port forward | tier free
- needs card no, phone no, ID yes, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://hsk.oray.com/price/
- price USD 0
- free tier: The free edition provides 1 GB of traffic per month; when it runs out you wait for the next month's reset or expand it through official tasks, with no compulsory payment. [translated] | unit: GB | metered on: unstated | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [2]
- retention: not applicable | source: [2]
- egress: 1 GB per month on the free edition, resettable monthly or expandable through in-product tasks whose size is not stated.; ingress: udp | metered: yes | free allowance: 1 GB per month on the free edition, resettable monthly or expandable through in-product tasks whose size is not stated. | source: [2]
- identity: national-id | detail: Registration requires real-name verification before a mapping can be added: 'register a Peanut Hull account and complete real-name verification (the free edition needs the basic check)'. The checks offered are mainland identity checks. | country: None
- interface: cli
- limits:
  - volume-quota: 1 GB per month [1]
  - per-ip-shaping: 1 Mbps on the free edition, with a 18:00-08:00 speed boost [1]
  - write-gated (binding): real-name verification before the first mapping [3]
- binding note: Either of the other two would fail first in arithmetic (1 GB/month is 0.0009 TiB), but the counter is never reached: the real-name gate sits at registration.
- interface detail: Windows, Linux and NAS clients; a web console at console.hsk.oray.com manages mappings and domains.
- tooling: vendor client on Windows/Linux/NAS plus wg-quick on the local box
- composes with: 1 GB/month cannot carry a WG session for long; useful only as a reachability fallback for a control plane.
- reliability: Free-edition bandwidth is shaped to 1 Mbps outside an 18:00-08:00 window; the vendor rates free-edition stability at 99.5 percent.
- notes: The largest consumer tunnel brand in China and the one an English reader is most likely to have heard of. Two independent blocks: a 1 GB monthly counter and a mainland real-name check. The free external port can be randomised or set by the operator, and the vendor says free users can switch ports to pick a lower-latency node, so port stability is a choice rather than a guarantee.
- evidence note: Quota, bandwidth, mapping count and the real-name step are all on the vendor's own pages read. What would raise the rung is a probe of a UDP mapping, which needs a verified account.
- extras:
  - wg_path: inside-udp
  - wg_detail: The mapping form takes a protocol of 'TCP/UDP' or 'ALL', so a public UDP port can be mapped to a local UDP listener, which is all a WG endpoint needs. No WG config is issued.
  - ingress: udp
  - volume_tib_month: 0.00091
  - volume_stated: 1 GB per month on the free edition, resettable monthly or expandable through in-product tasks whose size is not stated.
  - bytes_transit: yes
  - transit_note: Oray cloud relays every byte; the vendor states the client opens an encrypted tunnel to the cloud and external requests are forwarded inward.
- evidence:
  - [1] 2026-10-23: free edition provides 1 GB per month and 1 Mbps, with a night-time speed boost
  - [3] 2026-10-23: free edition is 1 Mbps, 2 mapping routes, 10 concurrent connections, 1 free shell domain; protocol may be TCP/UDP or ALL; real-name verification required
  - [2] 2026-10-23: the paid ladder starts at CNY 1299/year, so the free edition is the only zero-cost rung
- sources:
  - [1] https://hsk.oray.com/news/47972.html
  - [2] https://hsk.oray.com/price/
  - [3] https://hsk.oray.com/news/49157.html
