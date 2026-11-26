# Shenzhuo Hulian

> shenzhuohl.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/shenzhuohl/ | JSON https://fshy.ajam.dev/api/v1/entity/shenzhuohl.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Shenzhuo Hulian

- `egress/shenzhuo-hulian` | trial-only | evidence documented | binding none | category tcp+udp port forward | tier free
- needs card no, phone no, ID yes, institution no | verified 2026-11-19T21:10:55.764Z (live) | stale on 2026-12-20
- url https://www.shenzhuohl.com/price/first.html
- price USD 0
- free tier: Notice: from 22 May 2020 the free edition no longer limits traffic and becomes a free three-day trial. [translated] | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Unlimited traffic, but only for three days: the free edition became a three-day trial in May 2020 and the paid ladder starts at CNY 528 with 2 Mbps.; ingress: udp | metered: no | free allowance: none published | source: [1]
- identity: national-id | detail: Not established: the page offers free registration and an enterprise quote line, but the registration fields were not read. The vendor is a mainland company selling to enterprises on a 400 number. | country: None
- interface: cli
- limits:
  - volume-quota: unlimited monthly traffic on every tier listed on the current price page [1]
  - per-ip-shaping: line bandwidth 2 Mbps (upgradeable) on the CNY 528 standard tier; 4 Mbps on CNY 858 and 6 Mbps on CNY 1583 tiers [1]
- binding note: The first-party price page lists unlimited monthly traffic on every tier, so no byte quota binds this offer; the only numeric egress rate on the page is paid-tier line bandwidth, and the free window ends by wall clock, which the constraint vocabulary does not name.
- interface detail: A client for local servers and NAS, a web console for mappings and mesh groups, and an optional hardware box.
- tooling: vendor client on a local server or NAS, or the vendor's hardware box; wg-quick on the local box
- composes with: A three-day window is enough to test a WG-over-UDP path end to end before deciding whether the paid tier is worth CNY 528.
- reliability: Reconnect times are published per tier, from 30 seconds on the cheapest to 5 seconds on the flagship, which is a statement about how often the link drops.
- notes: Chinese tunneling provider offering port forwarding with unmetered byte volume subject to bandwidth speed caps. Free tier operates as a temporary 3-day trial.
- evidence note: The trial notice and the paid ladder are in the page HTML read. Whether the trial is still granted in 2026 needs a registration to confirm; the notice is dated 2020 and nothing on the page supersedes it.
- extras:
  - wg_path: inside-udp
  - wg_detail: The vendor states compatibility with every application above TCP/UDP, so a WG datagram can ride a UDP mapping. No WG config is issued.
  - ingress: udp
  - volume_stated: Unlimited traffic, but only for three days: the free edition became a three-day trial in May 2020 and the paid ladder starts at CNY 528 with 2 Mbps.
  - bytes_transit: yes
  - transit_note: Vendor clusters of 30 to 180 servers on 3 to 7 lines carry the tunnel.
- evidence:
  - [1] 2026-10-23: free edition became a 3-day trial with no traffic limit on 2020-05-22; paid tiers CNY 528 to CNY 1583, all unlimited traffic, 2 to 6 Mbps
  - [2] 2026-10-23: claims compatibility with everything above TCP/UDP and offers a dedicated public IP product
  - [1] 2026-11-19: the current first-party price page lists unlimited monthly traffic on every tier | capture: sha256:9c29893282d7e020d58daaad67c2eec0ee8a84f6169a364e21faca414f50af18 | quote: 每月流量 | 不限
  - [1] 2026-11-19: the first-party price page states a 2 Mbps line-bandwidth cap on the cheapest paid tier | capture: sha256:9c29893282d7e020d58daaad67c2eec0ee8a84f6169a364e21faca414f50af18 | quote: 线路带宽 | 2Mbps(可升级)
  - [1] 2026-11-19: unlimited monthly traffic on every listed tier means no byte quota binds | capture: sha256:9c29893282d7e020d58daaad67c2eec0ee8a84f6169a364e21faca414f50af18 | quote: 每月流量 | 不限
  - [1] 2026-11-19: the binding is none because the current price page lists unlimited monthly traffic and no byte quota | capture: sha256:9c29893282d7e020d58daaad67c2eec0ee8a84f6169a364e21faca414f50af18 | quote: 每月流量 | 不限
  - [1] 2026-11-19: the paid tiers carry a 2 Mbps line-bandwidth cap with a number and unit | capture: sha256:9c29893282d7e020d58daaad67c2eec0ee8a84f6169a364e21faca414f50af18 | quote: 线路带宽 | 2Mbps(可升级)
- sources:
  - [1] https://www.shenzhuohl.com/price/first.html
  - [2] https://www.shenzhuohl.com/index.html
