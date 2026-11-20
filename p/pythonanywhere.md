# PythonAnywhere

> pythonanywhere.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/pythonanywhere/ | JSON https://fshy.ajam.dev/api/v1/entity/pythonanywhere.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## PythonAnywhere

- `compute/pythonanywhere` | fails-quota | evidence documented | binding volume-quota | category shared shell | tier Beginner (free)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://www.pythonanywhere.com/pricing/
- free tier: USD 0 a month: one web app, up to 2 consoles, 100 CPU seconds a day, 512 MB of private file storage, outbound internet to a whitelist of sites only, no SSH | unit: seconds | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: the metered unit is CPU seconds, not wall clock; the table is headed 'CPU allowance'
- per-object cap: not applicable
- retention: not stated on the pricing page; the free plan includes 512 MB of private file storage with no expiry published there | source: [1] | note: the pricing page carries no deletion rule
- egress: the free plan reaches 'Specific sites via HTTP(S) only' through a whitelist; bandwidth is listed as 'Low' with no number | metered: yes | source: [1]
- identity: email | detail: an email address and a password. The pricing page offers the Beginner plan at USD 0 with no card, and no card or phone field appears in the plan description. No hold exists because no payment method is taken.
- interface: ssh
- limits:
  - volume-quota (binding): 100 CPU seconds a day [1]
  - volume-quota (binding): 512 MB of private file storage [1]
  - per-ip-shaping: outbound internet limited to a whitelist of sites [2]
- limits note: no SSH on the free plan; the console is in the browser
- binding note: 100 CPU seconds a day is the first wall; a single build or a pandas import can spend it.
- interface detail: a web app and a browser console; no SSH on the free plan
- tooling: WSGI and Flask or Django on a shared host; a scheduled task slot that is disabled on free
- composes with: 100 CPU-seconds a day and no always-on task, so nothing runs unattended
- reliability: no reliability event recorded
- notes: The free tier is real and permanent, and it is a web host. Without SSH and without general outbound access it cannot be a VPN node, a monitor that calls out, or a build machine. Unverified: a probe running a tight loop and reading the CPU counter.
- evidence note: every figure is from the vendor's own pricing table read, including the empty SSH cell and the whitelist link. That the signup form asks for nothing beyond email is an inference from the plan description, not a read form.
- extras:
  - shape.disk_gib: 0.5
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: consoles are capped at two concurrent, not by time
  - persistent_storage.included_gib: 0.5
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: private file storage
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while the account is active
  - network_out.allow_outbound: no
  - network_out.allow_inbound_listen: no
  - network_out.ports: one web app behind the vendor's front end
  - network_out.static_ip: no
  - free_tier_kind: always-free
  - ps.gib: 0.5
  - ps.price: 512 MB on free, 5 GB on Developer
  - ps.durability: private file storage
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: while the account exists
  - net.out: yes
  - net.in: yes
  - net.ports: HTTP through the web app
  - net.static_ip: no
  - net.allowance: bandwidth is 'Low' on free
  - shape_note: 512 MB of file storage; no RAM or vCPU published for the free plan
  - term: indefinite
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0 a month; the paid Developer plan is USD 10 a month
- evidence:
  - [1] 2026-10-06: free plan: 100 CPU-seconds a day, 512 MB of private file storage, 1 web app, max_always_on_tasks = 0
  - [1] 2026-10-22: the pricing table was read on 2026-10-22: 'CPU allowance: 100 seconds' on the Beginner ($0/month) column against 5,000 seconds on Developer, 'Private file storage: 512MB' on Beginner against 5GB, and 'Consoles: Up to 2'
  - [1] 2026-10-24: quoted table cells in the Beginner column: '100 seconds' under 'CPU allowance', '512MB' under 'Private file storage', 'Up to 2' under 'Consoles (Python, Bash, etc...)', and 'Specific sites via HTTP(S) only' under 'Access to external internet sites'
  - [1] 2026-10-24: quoted: 'SSH access to your account via `ssh.pythonanywhere.com`' appears with no mark in the Beginner column, while paid columns carry one
- sources:
  - [1] https://www.pythonanywhere.com/pricing/
  - [2] https://www.pythonanywhere.com/whitelist/
