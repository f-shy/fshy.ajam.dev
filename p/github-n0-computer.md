# iroh Mainline-DHT

> github.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-n0-computer/ | JSON https://fshy.ajam.dev/api/v1/entity/github-n0-computer.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## iroh Mainline-DHT content discovery (iroh-content-discovery)

- `storage/iroh-mainline-dht-content-discovery` | self-hosted, last resort | verdict qualifies | evidence reported | binding none | category discovery layer over the public Mainline DHT, published from an iroh node the user runs
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/n0-computer/iroh-content-discovery
- free tier: No quota, no storage. Pure discovery: publishes BLAKE3->provider mappings onto the public BitTorrent Mainline DHT. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: UDP DHT traffic only, kilobytes. Mainline lookups measured at 37 ms in n0's own example. | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits note: Mainline traffic is unencrypted and 'easily blocked by middleboxes'; no privacy ('anybody can look up your ip address'); the address-index service is last-writer-wins, in-memory, and records expire. Publishers must re-announce on a schedule.
- interface detail: `n0-mainline` crate; `iroh-mainline-address-lookup` (pkarr/BEP 44 records); `iroh_mainline_content_discovery` (`query_dht`, `query_iroh`).
- tooling: Publishes a signed endpoint record (endpoint id + UDP socket + timestamp) to a tiny UDP address-index service, then `announce_peer` for SHA-1(BLAKE3 hash). Discovery returns candidate EndpointIds which are then dialled with normal iroh hole punching.
- composes with: Removes the last central dependency: no DNS, no pkarr relay, no account. Requires at least one reachable address-index service, found by rendezvous hash or a curated BEP 44 record.
- reliability: Experimental repo (12 stars, last push 2026-10-16). SHA-1 is used only as a keyspace key, so a malicious DHT answer can waste time but cannot corrupt data. Verification is against the BLAKE3 root.
- notes: the same as the free tier
- self hosted: yes
- evidence:
  - [1] 2026-10-21: announce/discovery workflow, udp-addr-index rationale, 37 ms lookup, 'mainline does not provide any privacy'
  - [2] 2026-10-16: repo alive, pushed 2026-10-16
  - [3] 2026-10-21: DHT publishes the same signed records as DNS, different storage
  - [4] 2026-10-21: iroh-flavoured fork of a Mainline DHT implementation
- sources:
  - [1] https://www.iroh.computer/blog/iroh-global-content-discovery
  - [2] https://github.com/n0-computer/iroh-content-discovery
  - [3] https://docs.iroh.computer/connecting/dht-address-lookup
  - [4] https://github.com/n0-computer/n0-mainline

## dumbpipe / pigeons / iroh-ssh (as storage)

- `storage/dumbpipe-pigeons-iroh-ssh` | self-hosted, last resort | verdict fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/n0-computer/pigeons
- free tier: None reachable: Tunnel products, not stores. dumbpipe's own tagline is 'Unix pipes between devices'; pigeons is SSH-over-iroh; iroh-ssh is 'SSH to any machine without ip'. They pass bytes and keep none. Us. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Tunnel products, not stores. dumbpipe's own tagline is 'Unix pipes between devices'; pigeons is SSH-over-iroh; iroh-ssh is 'SSH to any machine without ip'. They pass bytes and keep none…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Tunnel products, not stores. dumbpipe's own tagline is 'Unix pipes between devices'; pigeons is SSH-over-iroh; iroh-ssh is 'SSH to any machine without ip'. They pass bytes and keep none…
  - [2] 2026-10-21: cited as the basis of the rejection: Tunnel products, not stores. dumbpipe's own tagline is 'Unix pipes between devices'; pigeons is SSH-over-iroh; iroh-ssh is 'SSH to any machine without ip'. They pass bytes and keep none — us
- sources:
  - [1] https://github.com/n0-computer/pigeons
  - [2] https://github.com/n0-computer/dumbpipe
