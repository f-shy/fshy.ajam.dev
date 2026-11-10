# ctrl-c.club

> ctrl-c.club | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ctrl-c/ | JSON https://fshy.ajam.dev/api/v1/entity/ctrl-c.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ctrl-c.club

- `compute/ctrl-c-club` | qualifies-with-caveat | evidence documented | binding write-gated | category shared shell
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:30.358Z (live) | stale on 2026-12-05
- url https://ctrl-c.club/
- free tier: a free shared Linux account on DigitalOcean with a 1 GB soft storage limit | unit: GiB | metered on: stored-bytes | read on: 2026-10-06 | source: [1] | note: about 825 users; IRC on 6667 and Gemini
- per-object cap: not applicable
- retention: accounts with no login in 5 years are archived and can be restored on request | days: 1825
- egress: not published | metered: no | source: [1]
- identity: email | detail: a signup request; no card. Signups are CLOSED and waitlist only, quoted from signup.ctrl-c.club: 'Signups are closed for now! ... We're pausing signups to work on some scaling issues. You can still submit a signup to get on a waitlist.' A new person can join a waitlist; only an existing member can reach the host today
- interface: ssh
- limits:
  - per-object-cap: 1 GB soft limit per account [1]
  - retention-clamped: accounts idle for 5 years are archived [1]
  - write-gated (binding): signups are closed; a new account can only join a waitlist [2]
- limits note: the 5-year archive is the gentlest retention clock found in this class, and it is not the constraint that binds a new reader. The signup is closed and waitlist only, so the gate fails before the quota is reached
- binding note: the closed signup binds first: a new reader can only join a waitlist, so the 5-year archive clock never applies to them. The retention clock is the gentlest in the class and it is not reachable.
- interface detail: SSH on port 22; IRC and Gemini
- tooling: SSH, screen or tmux, cron
- composes with: a very long retention clock on a small account
- reliability: no reliability event recorded
- notes: The oldest OpenSSH in this set and the longest retention clock. 1 GB is not storage, but it is a stable shell with a cron. Two corrections historical research records made and this record had dropped: signups are closed and waitlist only, and the GB figure is a soft limit rather than a hard cap. The tier moved from T1 to T2 on review because T1 means no archival and this row archives at five years.
- evidence note: reachability and the 5-year archive policy were both confirmed on 2026-10-22. The record is not `measured` because a probe proves the port answers and the 1 GB quota is a page claim, so the weakest field decides
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: ctrl-c.club
  - port: 22
  - ms: 323
  - ok: yes
  - banner: SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.18
  - peer: 165.227.127.54
- extras:
  - shape.disk_gib: 1
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: none stated
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://ctrl-c.club/
  - persistent_storage.included_gib: 1
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: 5 years without a login
  - network_out.allow_outbound: yes
  - network_out.ports: IRC 6667 and Gemini outbound
  - network_out.static_ip: no
  - free_tier_kind: allowance
  - m10h_usd: 0.0
  - m24h_usd: 0.0
- evidence:
  - probe:ctrl-c.club:22 2026-10-22: TCP connect succeeded in 0.32 s to 165.227.127.54 and read banner SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.18
  - [1] 2026-10-22: 'we're archiving accounts that have not been logged into in 5 years or more', and an archived account can be restored on request
  - [2] 2026-10-06: not re-fetched
  - [2] 2026-10-06: 'One gigabyte storage limit (this is not a hard limit: brief, occasional overages are not a problem.)' which is the soft limit the record quotes
  - [1] 2026-11-03: access is by SSH; no REST API or CLI is stated | capture: sha256:23b7aace281d54c5e6b770aae920a14fa2bd0ff887edc62446a3feee4216c294 | quote: Ctrl-C.club is a Linux server offering free SSH and web accounts to users who want to build webpages, chat online, learn Linux, play text console games, or fiddle around writing software.
- sources:
  - [1] https://ctrl-c.club/
  - [2] https://signup.ctrl-c.club/
