# playit.gg

> playit.gg | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/playit/ | JSON https://fshy.ajam.dev/api/v1/entity/playit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## playit.gg

- `egress/playit-gg` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category relay (hosted, game tunnel)
- needs card no, phone no, ID no, institution no | verified 2026-10-23 (live) | stale on 2026-11-23
- url https://playit.gg/
- free tier: free tunnels on global anycast with no published cap | unit: unlimited | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a tunnel
- retention: not applicable: a long-lived tunnel rather than stored bytes | source: [1]
- egress: no published quota; a staff post describes 1-2 TB/day on a free account as tolerated | metered: no | free allowance: none published | source: [2]
- identity: email | detail: a playit account for a persistent tunnel
- interface: cli
- limits:
  - per-ip-shaping (binding): no set limits; the operator said a free user was consuming about 1-2 TB per day and that this looked temporary, so he did not make contact; 100 GB+/day from Australia would probably draw contact [2]
  - write-gated: generic TCP and TCP+UDP are Premium; the free column carries the game presets and a generic UDP entry [3]
- binding note: An unpublished tolerance is weaker than a quota because no threshold can be designed against, but this one is measured per day and generous: 1 TiB/month is 33.3 GiB/day, against a stated tolerance of about 1-2 TB/day for a single free user. What fails first is the free tier's protocol gate, not volume: generic TCP tunnels need Premium, so only the game presets and the generic UDP entry are available at zero cost.
- interface detail: the playit agent opens a tunnel to a global anycast address
- tooling: playit-cli
- composes with: the only hosted relay found that a person at this volume could plausibly run free, and it composes with a home origin and nothing else. Its scarce link is one operator's tolerance.
- reliability: no published quota: the operator contacts a heavy user rather than throttling one, and the free network is one region with routing chosen by the visitor's ISP
- notes: The strongest free relay found and the least durable evidence: two sentences, one operator, one day (2026-05-28). Stays reported. The same thread says the tolerance moves with regional bandwidth cost, so the number is a cost observation rather than a policy. Free includes a generic UDP entry and the game presets; SSH, HTTPs, TCP and TCP+UDP are Premium. Adds the date the tolerance was stated and the current free/Premium split read from the pricing page. Re-read 2026-10-23: 'Minecraft Bedrock (NetherNet)' is now a premium-gated preset, so the free set is not every game preset. Custom UDP stays free.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the anycast relay carries the game traffic it forwards
  - wg_path: inside-udp
- evidence:
  - [2] 2026-10-22: operator, 2026-05-28: a free user at 1-2 TB/day was tolerated, and regional bandwidth cost decides whether contact happens
  - [1] 2026-10-22: a free tier exists, Premium is USD 3/month, and generic TCP is not a free port type
  - [4] 2026-10-23: the free tier's port types list UDP; TCP, TCP+UDP, SSH and HTTPS are under 'Requires Playit Premium'
  - [5] 2026-10-23: 'the number of ports you can allocate jumps from 4 to 16', and free tunnels are Global Anycast
  - [6] 2026-10-23: staff: the assigned random port 'Should be permanent'
  - [7] 2026-10-23: of a UDP-only game: 'This server uses UDP 7707 and UDP 7708, which means that all users can create this tunnel type'
  - [1] 2026-10-23: The Free column lists 'Minecraft Bedrock', 'MC: Simple Voice Chat' and 'UDP'; the Premium column lists 'Minecraft Bedrock (NetherNet)', 'TCP' and 'TCP+UDP'
- sources:
  - [1] https://playit.gg/
  - [2] https://discuss.playit.gg/t/traffic-limits/5574
  - [3] https://playit.gg/pricing/
  - [4] https://playit.gg/pricing
  - [5] https://playit.gg/support/playit-premium/
  - [6] https://discuss.playit.gg/t/question-about-custom-tcp/435
  - [7] https://playit.gg/support/killingfloor-server-windows/
