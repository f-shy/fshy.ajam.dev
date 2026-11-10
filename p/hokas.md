# HOKAS

> hokas.net | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hokas/ | JSON https://fshy.ajam.dev/api/v1/entity/hokas.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HOKAS

- `compute/hokas-free` | fails-quota | evidence documented | binding retention-clamped | category container-PaaS | tier Free plan
- needs card no, phone no, ID no, institution no | verified 2026-10-24T04:12:03.000Z (live) | stale on 2026-11-24
- url https://hokas.net/
- free tier: 'The free plan never expires', 'no credit card needed', 'Free subdomain for every server', 'Unmetered bandwidth on every plan'. The live panel mock on the home page shows 'CPU 0.3 vCPU', 'Memory 74 / 256 MB', 'Disk 120 / 512 MB'. | unit: none | metered on: none | read on: 2026-10-24 | source: [1]
- per-object cap: not published as a count: the free plan is described per server (0.3 vCPU, 256 MB RAM, 512 MB disk) and no page read states how many free servers an account may hold
- retention: The free plan is time-limited and renewed by hand. Quoted: 'The server runs for a limited time. Before it expires, complete a short advertising or link flow to extend its uptime. This funds the free plan.' The renewal options default to '12 or 24 hours', each usable 'once per renewal window', with a default window of 24 hours.
- egress: 'Unmetered bandwidth on every plan' | metered: no | free allowance: unmetered, per the signup page | source: [2]
- identity: email | detail: no card: quoted 'no credit card needed' on the signup page. The signup form itself was not rendered to fields on 2026-10-24; the page states only that an account is created. Paid plans require the user to be at least 18.
- interface: sftp, rest
- limits:
  - retention-clamped (binding): the free server expires unless an advertising or link flow is completed, with 12 or 24 hour renewal options [3]
  - volume-quota: 0.3 vCPU, 256 MB RAM, 512 MB disk per free server [1]
  - write-gated: a link or advertising flow must be completed to extend uptime [4]
- binding note: The machine does not survive unattended: its lifetime is measured in 12 or 24 hour blocks that a link or advertising flow has to renew, so a tab closed for a day ends the machine.
- interface detail: a dashboard with a live console that accepts input, a file manager, and a free subdomain per server; seven runtimes (Node.js, Python, PHP, Bun, Java, C#, Rust)
- tooling: the vendor dashboard; no SSH and no root
- composes with: A small long-running process with a public subdomain, kept alive by a browser flow every 12 to 24 hours. Useful only where a human or a browser can do that flow, which rules out a fully unattended node.
- reliability: The vendor status page at status.hokas.net reported 'All services are online' with 'Last updated on Oct 24, 2026 at 4:05am UTC', read. That is the vendor's own measurement.
- notes: Documented because it is the clearest example among evaluated providers of a free tier whose marketing says 'never expires' while its own documentation says the server 'runs for a limited time' and is renewed by completing an advertising or link flow in 12 or 24 hour blocks. The contradiction is the finding: the marketing sentence and the documentation sentence are both on the vendor's own site, read. That renewal loop is a human action, so the machine does not survive a tab closing, which is the bar evaluated providers set. Everything else about it is reasonable: a real dashboard, seven runtimes, a free subdomain, unmetered bandwidth, no card.
- evidence note: The renewal mechanics and the free plan's limits are quoted from the vendor's own documentation read. The exact free allocation is taken from the panel mock on the marketing page rather than from a plan table, which is weaker, and the signup form's fields were not read.
- extras:
  - shape.vcpu: 0.3
  - shape.ram_gib: 0.25
  - shape.disk_gib: 0.5
  - billing_model: free
  - term: 12 or 24 hour blocks, renewed by a link or advertising flow
  - m10h_usd: 0
  - m24h_usd: 0
  - price_arithmetic: USD 0 for the free plan
  - free_tier_kind: capped-free
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a free subdomain per server; port list not published
  - session_cap.wall_clock_min: 1440
  - session_cap.restart_required: no
  - session_cap.note: 12 or 24 hours per renewal, and each option is usable once per 24-hour window, so the practical maximum is 24 hours of uptime per renewal
- evidence:
  - [4] 2026-10-24: quoted: 'Free plan: There is no charge. The server runs for a limited time. Before it expires, complete a short advertising or link flow to extend its uptime. This funds the free plan.'
  - [3] 2026-10-24: quoted: 'If no custom duration is set, the options are 12 or 24 hours'; 'Complete the short link flow that opens. When you return, the duration is added to your server.'; 'You can use each duration option once per renewal window. The default window is 24 hours.'
  - [1] 2026-10-24: quoted: 'The free plan never expires', 'Paid plans are optional', 'CPU 0.3 vCPU', 'Memory 74 / 256 MB', 'Disk 120 / 512 MB'
  - [2] 2026-10-24: quoted: 'Free plan that never expires, no credit card needed'; 'Free subdomain for every server'; 'Unmetered bandwidth on every plan'
  - [5] 2026-10-24: quoted: 'All services are online', 'Last updated on Oct 24, 2026 at 4:05am UTC'
- sources:
  - [1] https://hokas.net/
  - [2] https://hokas.net/sign-up
  - [3] https://docs.hokas.net/how-do-i-renew-a-server.md
  - [4] https://docs.hokas.net/are-servers-free-or-paid.md
  - [5] https://status.hokas.net/
