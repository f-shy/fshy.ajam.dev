# Waifly

> waifly.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/waifly/ | JSON https://fshy.ajam.dev/api/v1/entity/waifly.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Waifly

- `compute/waifly-free` | qualifies-with-caveat | evidence documented | binding volume-quota | category container-PaaS | tier FREE
- needs card no, phone no, ID no, institution no | verified 2026-10-24T04:12:03.000Z (live) | stale on 2026-11-24
- url https://docs.waifly.com/offres
- free tier: 'Waifly's free plan gives 300 MB of RAM, 1 GB of storage, one server and one MySQL database for €0 permanently, with CPU capped at 30% and no credit card required.' | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: '1 server, 1 MySQL database' on the free plan. An extra server slot costs EUR 1 a month, which is a paid add-on rather than a free cap.
- retention: 'A server's status is checked daily; it gets suspended after 3 days offline.' A suspended server created less than 7 days earlier 'is deleted after 3 days'; an older one is kept '15 days' and recoverable from backups.waifly.com. An automated inspection runs every 30 minutes. So the machine persists indefinitely while it keeps running, and dies 3 days after it stops.
- egress: not published: no traffic allowance appears on the pricing page, the rules page or the documentation index read | metered: no | source: [1]
- identity: email | detail: no card: quoted 'No payment method is requested for the free plan'. Signup is a username of at least 4 alphanumeric characters, an email, a password of at least 6 characters, a 'how did you find us' field and acceptance of the terms; Discord, Google or Apple login are alternatives. No phone and no document.
- interface: sftp, rest
- limits:
  - volume-quota (binding): 300 MB RAM, 1 GB storage, CPU capped at 30 per cent, 1 server [1]
  - retention-clamped: suspended after 3 days offline; deleted 3 days later if younger than 7 days, else 15 days [2]
  - write-gated: one account per person, with an automated inspection every 30 minutes [2]
- binding note: 300 MB of RAM with a 30 per cent CPU cap binds first: the anti-abuse rules also forbid tunnels and proxies on the free plan, so the machine cannot be repurposed as a relay when the application outgrows the memory.
- interface detail: a Pterodactyl panel with a live console, file manager, SFTP, databases, scheduled tasks and backups; the docs state 'there is no root access or SSH shell'
- tooling: the Pterodactyl panel or SFTP; no SSH
- composes with: A small always-on application process on a French host: a cron-driven fetch job, a bot, or a tiny API.
- reliability: The operator publishes 99.9 per cent measured uptime over 30 days on status.waifly.com; that is the vendor's own figure and unverified independently.
- notes: A French host with two named Paris nodes, a documented anti-abuse rule that is unusually explicit about its own suspension clock, and a free plan that needs no card. The founder is named in the documentation but no company registration number was found on any page read, so the entity is a named individual rather than a company. The one thing that would change the verdict is an egress number, which is not published.
- evidence note: Shape, price, the no-card statement and the suspension clock are quoted from the vendor's own documentation read. Egress is not published, so the row is documented about the allocation and unverified about bandwidth.
- extras:
  - shape.ram_gib: 0.29
  - shape.disk_gib: 1
  - billing_model: free
  - term: permanent while running; suspended 3 days after going offline
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: EUR 0.00 for the free plan; paid plans are EUR 4 (Nano), EUR 8 (Mega) and EUR 16 (Giga) a month, and an extra server slot is EUR 1 a month
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: not published for the free plan; paid plans list 2, 5 and 10 ports
  - session_cap.restart_required: no
  - session_cap.note: no idle sleep; a server offline for 3 days is suspended, which is a liveness check on the process rather than on traffic
  - payment_methods: none for the free plan; PayPal, Stripe, lava.top and crypto for paid plans
- evidence:
  - [1] 2026-10-24: quoted: '300 MB of RAM, 1 GB of storage, one server and one MySQL database for €0 permanently, with CPU capped at 30% and no credit card required'; 'Free plan (FREE) - €0, forever, no credit card or PayPal required'; '300 MB RAM', 'CPU capped at 30%', '1024 MB storage', '1 server, 1 MySQL database', 'Backups included, Pterodactyl panel'
  - [2] 2026-10-24: quoted: 'A server's status is checked daily; it gets suspended after 3 days offline'; 'Server created less than 7 days ago: deleted after 3 days of suspension'; 'Older server: 15-day retention after suspension'; 'One account per person'; 'VPNs / proxies / tunnels' are excluded from the free plan
  - [3] 2026-10-24: quoted: 'No payment method is requested for the free plan'; signup is 'a username of at least 4 alphanumeric characters and a password of at least 6', an email, and acceptance of the terms
  - [4] 2026-10-24: quoted: 'Servers are containers managed through a Pterodactyl panel, so there is no root access or SSH shell, but you get a live console, SFTP, databases, scheduled tasks and backups'; 'two Intel Xeon Gold 6138 nodes in Paris'; documentation 'Last updated 2026-08-12'
  - [1] 2026-10-24: quoted payment methods: 'PayPal, Stripe (debit/credit card), lava.top ... and cryptocurrencies'. This is what a paid plan accepts; the free plan asks for none
- sources:
  - [1] https://docs.waifly.com/offres
  - [2] https://docs.waifly.com/regles
  - [3] https://docs.waifly.com/compte
  - [4] https://docs.waifly.com/
