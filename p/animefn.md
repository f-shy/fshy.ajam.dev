# animefn servers

> animefn.com | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/animefn/ | JSON https://fshy.ajam.dev/api/v1/entity/animefn.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## animefn servers (سيد بوكس)

- `debrid/animefn-seedbox` | qualifies-with-caveat | evidence documented | binding per-ip-shaping | category shared seedbox (Arabic-language storefront; rTorrent/ruTorrent over FTP) | tier SB-500
- needs card no, phone no, ID no, institution no | verified 2026-10-23T03:17:21.000Z (live) | stale on 2026-11-23
- url https://servers.animefn.com/seedbox
- price EUR 7 per 500 GB-month at entry; traffic unmetered | parsed USD 15.67/TB-mo
- free tier: No free tier. The entry product is SB-500: 500 GB, 1 Gbps shared, unlimited traffic, EUR 7 per month. | unit: none | metered on: none | read on: 2026-10-23 | source: [1] | note: Tiers: SB-500 EUR 7, SB-1000 EUR 13, SB-1500 EUR 18 per month. A dedicated IP is EUR 2.5 per month extra.
- per-object cap: not applicable: a seedbox stores whatever fits in the plan's disk (500/1000/1500 GB). | source: [1]
- retention: Storage is the plan's disk and nothing on the page deletes on a timer; removal is manual. | source: [1]
- egress: Traffic is stated as unlimited on every shared and dedicated plan ('الترافيك: غير محدود'), and the connection is 1 Gbps shared. | metered: no | free allowance: unlimited | source: [1]
- identity: email | detail: An order account on the vendor's site; the checkout was not opened, so email as the minimum is inferred, not observed.
- interface: ftp, ssh
- limits:
  - per-ip-shaping (binding): 1 Gbps shared across the users of the box on every shared plan [1]
- limits note: Disk is the other ceiling: 500 GB on the entry plan against a user workload measured in terabytes, so the box is a staging area rather than storage.
- binding note: Traffic is not metered, so at 1 TiB/month nothing in the traffic terms fails; what fails is the disk (500 GB) and the shared gigabit, which is why the binding is throughput shaped by other tenants.
- interface detail: rTorrent with the ruTorrent web UI on every plan. Shared plans expose FTP; dedicated plans add SSH, HTTP and SSHFS ('FTP / SSH / HTTP / SSHFS').
- tooling: ruTorrent in a browser, FTP for transfer, SSH/SSHFS on dedicated plans. No rclone backend documented.
- composes with: A seedbox does not resolve file-host links, but it removes the local line from the swarm: the torrent is fetched at 1 Gbps and pulled down over FTP, so the home connection only carries the finished file once.
- reliability: Shared gigabit and shared disk mean a neighbour's swarm sets the observed speed; the page publishes no uptime figure and no refund condition.
- notes: The only Arabic-language seedbox storefront found among debrid providers that publishes prices. Its relevance to retrieval is indirect: it seeds and stages, it does not unlock file hosts, so it composes with a debrid service rather than replacing one.
- evidence note: The plan table, the unlimited-traffic row and the interface rows were read. The payment methods, the datacentre location and the delivery time were not on the page read.
- evidence:
  - [1] 2026-10-23: SB-500/1000/1500 at EUR 7/13/18 per month with 500/1000/1500 GB, 1 Gbps shared, unlimited traffic, rTorrent/ruTorrent and FTP; dedicated tiers from EUR 14 plus EUR 5 setup; dedicated IP EUR 2.5 per month
- sources:
  - [1] https://servers.animefn.com/seedbox
