# StarryFrp

> starryfrp.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/starryfrp/ | JSON https://fshy.ajam.dev/api/v1/entity/starryfrp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## StarryFrp

- `egress/starryfrp` | fails-quota | evidence documented | binding volume-quota | category udp port forward | tier free
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://frp.starryfrp.com/
- price USD 0
- free tier: Basic features are free forever: daily check-in grants 1 to 10 GiB of traffic; upgrade when you need more bandwidth or more tunnels. [translated] | unit: GiB | metered on: downloaded-bytes | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Daily check-in grants 1 to 10 GiB, so the monthly ceiling from check-in alone is about 30 to 300 GiB.; ingress: udp | metered: yes | free allowance: Daily check-in grants 1 to 10 GiB, so the monthly ceiling from check-in alone is about 30 to 300 GiB. | source: [1]
- identity: email | detail: Registration then a console; no real-name requirement is stated on the page read. | country: None
- interface: cli
- limits:
  - volume-quota (binding): 1 to 10 GiB per day via check-in [1]
- binding note: Even a perfect 10 GiB every day for 30 days is 300 GiB, about 0.29 TiB, so the daily grant fails 1 TiB/month.
- interface detail: frpc client, console-generated config.
- tooling: frpc with a TOML config
- composes with: A debugging tunnel, not a 1 TiB path.
- reliability: No reliability report found.
- notes: The page is a marketing site with no published per-tunnel quota table; the check-in sentence is the only number on it.
- evidence note: The check-in figure came from the page's extracted text today; the read that followed returned only the feature copy, so the figure rests on that one extraction.
- extras:
  - wg_path: inside-udp
  - wg_detail: The page lists UDP alongside TCP, HTTP and HTTPS and names UDP ports 19132 and 27015 as examples; a WG datagram can be carried on such a tunnel.
  - ingress: udp
  - volume_tib_month: 0.029
  - volume_stated: Daily check-in grants 1 to 10 GiB, so the monthly ceiling from check-in alone is about 30 to 300 GiB.
  - bytes_transit: yes
  - transit_note: StarryFrp nodes relay the datagrams.
- evidence:
  - [1] 2026-10-23: UDP is a supported tunnel type, with check-in traffic of 1 to 10 GiB per day
- sources:
  - [1] https://frp.starryfrp.com/
