# Silly Development

> sillydev.co.uk | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sillydev/ | JSON https://fshy.ajam.dev/api/v1/entity/sillydev.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Silly Development

- `compute/sillydev-free` | qualifies-with-caveat | evidence documented | binding volume-quota | category container-PaaS | tier Free server
- needs card no, phone no, ID no, institution no | verified 2026-10-24T04:12:03.000Z (live) | stale on 2026-11-24
- url https://sillydev.co.uk/
- free tier: '25% of a CPU core, 256 MB of memory, and 512 MB of disk', 'No card, no trial, no expiry', 'We do not sleep idle containers and we do not cap how many hours a month you run.' Plus '2 databases per account, 50 MB each' on MariaDB or PostgreSQL. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: '2 databases per account, 50 MB each'; the terms state 'each with a fixed disk quota shown in your panel' and 'A write that would go past it fails straight away'. The number of free servers per account is not published on the pages read.
- retention: 'No renewal button and no expiry timer. The only exception: a server never used at all in its first 7 days is removed, usually after an email warning.' Nothing else reaps it.
- egress: not published: no traffic allowance appears on the home page, the terms or the database page read. The terms state only that a web app is reachable at 'the address and port shown in your panel'. | metered: no | source: [2]
- identity: email | detail: no card: quoted 'No card, no trial, no expiry' and the register form asks username, email, password, confirm password, and optionally first and last name. No phone, no document, no card field. Payment by Stripe exists only for the optional paid plan.
- interface: ssh, rest
- limits:
  - volume-quota (binding): 256 MB RAM, 512 MB disk, 25 per cent of a core per server [2]
  - per-object-cap: 2 databases per account, 50 MB each, hard limit [3]
  - retention-clamped: a server never used in its first 7 days is removed [1]
- binding note: 256 MB of RAM with no swap and no sleep binds first: a scraper with a headless browser or a pandas frame will be killed by the OOM reaper long before any traffic allowance matters.
- interface detail: a panel with a live console that accepts input, a file manager, SFTP, automatic restarts, and scheduled tasks; Node.js, Python and Bun runtimes. No root shell: the terms call it 'not a general virtual server'.
- tooling: the vendor panel, or SFTP; no SSH client of your own choosing
- composes with: A process that must stay up and must not be visited to stay up: a scraper worker, a queue consumer, a Discord or Telegram bot, or a scheduled script with a stateful database beside it.
- reliability: Third-party reports of panel outages exist: one Trustpilot reviewer (read) writes that the panel 'stop working' and was down 'for 3 hours'; another says 'sometimes the server stops'. The vendor status host did not respond when checked, so uptime is not established.
- notes: This is the best answer in this category to the complaint documented records: a free tier that states in its own terms that it does not sleep, does not expire, and does not renew, with a 23 October 2026 date on the terms, and a register form with no card and no phone. The caveats are real. It is one UK sole trader, so it is identifiable but small, and the entity is a person rather than a company. No egress allowance is published at all. The absence of a root shell means it is a process host, not a machine: a WireGuard node is not possible here, but a cron and a listening port are. Third-party reviews report panel outages that the vendor's own status page could not be checked against, because that host did not answer.
- evidence note: Shape, the no-sleep statement, the no-expiry statement and the database quotas are quoted from the vendor's own pages read. Egress is not published anywhere read, so the row is documented about the allocation and unverified about bandwidth.
- extras:
  - shape.vcpu: 0.25
  - shape.ram_gib: 0.25
  - shape.disk_gib: 0.5
  - billing_model: free
  - term: no expiry; a server unused for its first 7 days is removed
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: GBP 0.00 for the free plan; the optional paid plan is '75p per month' and doubles the allocation to 50 per cent of a core, 512 MB and 1 GB, which is GBP 0.75 a month
  - free_tier_kind: always-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a port shown in the panel; no domain and no TLS certificate is provided
  - session_cap.restart_required: no
  - session_cap.note: quoted 'We do not sleep idle containers'; automatic restarts on an unhandled exception
  - payment_methods: none for the free plan; Stripe for the paid plan
- evidence:
  - [1] 2026-10-24: quoted: 'CPU 25%', 'RAM 256 MB', 'Disk 512 MB', 'Uptime 24/7', 'No card. No renewals. No sleeping.', 'We do not sleep idle containers and we do not cap how many hours a month you run.', 'a server never used at all in its first 7 days is removed'
  - [2] 2026-10-24: quoted: 'Silly Development is operated by an individual sole trader based in the United Kingdom'; 'Every free server receives a fixed allocation: 25% of a CPU core, 256 MB of memory, and 512 MB of disk'; 'The free service is not a trial and not a cut-down version of something better'; 'We are not a general virtual server and not a game server host'; terms page dated 'Last updated 23 October 2026'
  - [4] 2026-10-24: quoted form fields: 'Username', 'Email', 'Password', 'Confirm Password', 'First Name (optional)', 'Last Name (optional)'. No card and no phone field on the form
  - [3] 2026-10-24: quoted: 'Databases 2', 'Disk each 50 MB', 'A hard limit. A write that would go past it fails straight away'; '2 databases per account, 50 MB each'
  - [5] 2026-10-24: quoted: '201' reviews, '3.9' of 5, profile 'Claimed • Sep 2023'; reviewers describe the panel stopping and being down for 3 hours. Third-party and self-selected, so reported only
- sources:
  - [1] https://sillydev.co.uk/
  - [2] https://sillydev.co.uk/terms
  - [3] https://sillydev.co.uk/free-database-hosting
  - [4] https://sillydev.co.uk/panel/auth/register
  - [5] https://www.trustpilot.com/review/sillydev.co.uk
