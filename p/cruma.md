# Cruma

> cruma.io | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cruma/ | JSON https://fshy.ajam.dev/api/v1/entity/cruma.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Cruma

- `egress/cruma` | qualifies-with-caveat | evidence documented | binding volume-quota | category relay (hosted, HTTPS tunnel, anonymous tier) | tier anonymous
- needs card no, phone no, ID no, institution no | verified 2026-11-10T03:20:00.000Z (live) | stale on 2026-12-11
- url https://cruma.io/pricing
- free tier: Free with no account: a public HTTPS URL per tunnel, a 3-hour session window and 1 GiB of traffic per session on the anonymous tier. A free account removes the session window and allows 3 GiB per UTC day; paid plans have a full-speed allowance that refills continuously, and sustained use beyond it continues at a reduced rate. | unit: GiB | metered on: downloaded-bytes | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable: a tunnel, not an object | source: [1]
- retention: not applicable: a live tunnel; an anonymous session ends after 3 hours | source: [1]
- egress: 1 GiB per session on the anonymous tier and 3 GiB per UTC day on the free account; past the cap visitors get an HTTP 429 page. Paid plans have a continuously refilling full-speed allowance, 750 GB on Basic and 1.5 TB on Pro, and continue at a reduced rate beyond it.; ingress: http | metered: yes | free allowance: 1 GiB per session (anonymous); 3 GiB per UTC day (free account) | source: [1]
- identity: anonymous | detail: no account: the homepage says 'Free · no account needed'; a free account is optional and raises the daily cap to 3 GiB
- interface: cli
- limits:
  - volume-quota (binding): 1 GiB per session on the anonymous tier [1]
  - retention-clamped: a 3-hour session window on the anonymous tier [1]
  - request-rate: past the cap visitors get an HTTP 429 page [1]
- binding note: the session byte cap fails first: 1 GiB is one large file, and the 3-hour window ends the tunnel even when the bytes are unspent.
- interface detail: cruma proxy http <host:port> prints a public https://<id>.tun.cruma.io URL; the desktop app and the local reverse proxy use the same agent
- tooling: the cruma CLI from npm (@cruma-io/cli) or the desktop app; the agent is also a local web server and reverse proxy
- composes with: one anonymous tunnel publishes a webhook receiver or a small HTTP service; it carries TCP only, and the 1 GiB session cap makes it a test lane rather than a service lane
- reliability: an anonymous session ends after 3 hours and 1 GiB; a capability-free sandbox measured a 329 ms median latency and 117-126 kB/s on a 4 MiB transfer on 2026-11-05
- notes: The fastest hosted relay by its own harness's account in a 2026-11-05 benchmark of authless relays: 329 ms median latency (probe sha256:e3b9e671b9637952dcd876c4cad821a9d4e22a5d44064934190f68c60fd1a133). The anonymous tier is a development allowance of 3 hours and 1 GiB per session, not a service tier.
- evidence note: the anonymous tier's limits are read from the vendor pricing page; the latency and throughput are a sandbox measurement and are recorded as such
- evidence:
  - [1] 2026-11-10: the anonymous tier is a 3-hour session with 1 GiB of traffic | capture: sha256:f207d51497dd4b55fb5b9de57712199a8ba71891be8359619c0c696ca43aaf48 | quote: 3-hour session window
  - [1] 2026-11-10: past the cap visitors get an HTTP 429 page | capture: sha256:f207d51497dd4b55fb5b9de57712199a8ba71891be8359619c0c696ca43aaf48 | quote: past the cap, visitors get an HTTP 429 page
  - [1] 2026-11-10: the free account allows 3 GiB per UTC day | capture: sha256:f207d51497dd4b55fb5b9de57712199a8ba71891be8359619c0c696ca43aaf48 | quote: Free tunnels at 3 GiB per UTC day
  - [2] 2026-11-10: no account is needed for a free tunnel | capture: sha256:88542b15974b7a106bd63139e67f8aba6e38798746a31716d297e5477070dc22 | quote: Free · no account needed
  - probe:https://tun.cruma-cust1.com/ 2026-11-05: a 4 MiB transfer completed at 117-126 kB/s and /lat returned 200 | capture: sha256:e3b9e671b9637952dcd876c4cad821a9d4e22a5d44064934190f68c60fd1a133 | quote: 126 kB/s and 117 kB/s
- sources:
  - [1] https://cruma.io/pricing
  - [2] https://cruma.io/
