# RIPE Atlas

> ripe.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ripe/ | JSON https://fshy.ajam.dev/api/v1/entity/ripe.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## RIPE Atlas (host a probe or anchor)

- `storage/ripe-atlas` | self-hosted, last resort | verdict fails-quota | evidence reported | binding write-gated | category volunteer measurement network
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://atlas.ripe.net/get-involved/become-a-host/
- free tier: no storage; hosting earns credits spendable on custom measurements | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: you donate it | metered: no
- identity: email | detail: email
- interface: rest
- limits:
  - write-gated (binding): approval [1]
- limits note: Hosting a probe earns credits, and credits buy measurements - not bytes and not disk. A software probe can run on your own infrastructure, which makes it the most accessible thing in this whole slot (no shipping, no institution), but it is a measurement vantage point with trivial bandwidth and no storage. Anchors are bigger and require a datacentre-grade commitment plus approval.
- interface detail: probe hardware or software probe; REST API for measurements
- tooling: atlas.ripe.net API, software probe package
- composes with: none
- reliability: Hardware probes are frequently out of stock; software probes have negligible throughput by design.
- notes: the same as the free tier
- self hosted: yes
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: no storage; hosting earns credits spendable on custom measurements
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [2] 2026-10-21: 'You can either apply to host a hardware probe, which we will ship to you ... or a software probe, which you can install and run on your own infrastructure'; 'You'll earn credits you can use for your own customised measurements'
  - [1] 2026-10-21: 'They are not always in stock, you may have to apply and wait for one'; 'Apply for a software probe through your account'
  - [1] 2026-10-21: 'The vast majority of data that RIPE Atlas collects is freely available to anyone to browse, download or use'
- sources:
  - [1] https://www.ripe.net/analyse/internet-measurements/ripe-atlas/host-a-probe/
  - [2] https://atlas.ripe.net/get-involved/become-a-host/
