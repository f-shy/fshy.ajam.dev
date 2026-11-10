# SDF Public Access UNIX System

> sdf.org | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/sdf/ | JSON https://fshy.ajam.dev/api/v1/entity/sdf.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SDF Public Access UNIX System

- `compute/sdf-public-access-unix` | qualifies-with-caveat | evidence documented | binding volume-quota | category shared shell | tier USERS (free)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:56:00.000Z (live) | stale on 2026-11-24
- url https://sdf.org/?join
- free tier: The free USERS level: 20 MB disk quota for email, 20 MB for home, 20 MB for webspace and 20 MB for gopherspace; inbound ssh, ftp and sftp connections; no gcc, no python, no outbound ssh | unit: MB | metered on: stored-bytes | read on: 2026-10-24 | source: [1] | note: the same page lists a USD 36 one-time ARPA membership that adds compilers, outbound ssh and 150 MB quotas
- per-object cap: not applicable
- retention: Prevalidated accounts are automatically purged whether they are in use or not approximately 600 days of their creation. Validated accounts will expire if the user does not login at least once during a 2 year period. | days: 730 | source: [2] | note: the 730-day figure is the validated-account rule; an unvalidated account is purged at about 600 days regardless of use
- egress: not published as a volume; the free level is restricted by tool rather than by bytes (no outbound ssh, no wget, no compilers) | metered: no
- identity: email | detail: the account is created interactively over SSH at `ssh [address removed]`, then validated. No card and no phone appear on the join, signup or FAQ pages read. The exact fields of the new-user prompt were not read, so the email claim rests on the account-recovery pages rather than on the form itself.
- interface: rest, cli
- limits:
  - volume-quota (binding): 20 MB home, 20 MB webspace, 20 MB email, 20 MB gopherspace on the free level [1]
  - retention-clamped: unvalidated accounts purged at about 600 days; validated accounts expire after 2 years without a login [2]
- limits note: tens of thousands of users share one kernel; any admin can kill a process under load
- binding note: 20 MB of home is the smallest quota among documented hosts by an order of magnitude, and the free level withholds the compilers and the outbound ssh that a workload would need.
- interface detail: SSH on port 22, plus mail, gopher and web space
- tooling: SSH, screen or tmux, cron, a shared compiler toolchain
- composes with: a place to hold a shell and a cron job that survives reboots, not a place to run a server
- reliability: no reliability event recorded
- notes: A free shell that is real and permanent-ish, and far too small to be a machine. The 20 MB home would not hold a Python virtualenv. Unverified: one signup attempt reading the prompt, which this category did not do because it creates an account.
- evidence note: quotas, membership levels, the USD 36 ARPA tier and the purge rules are quoted from SDF's own join and FAQ pages read. The signup form's fields are not among them.
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: sdf.org
  - port: 22
  - ms: 557
  - ok: yes
  - banner: SSH-2.0-OpenSSH_10.4
  - peer: 205.166.94.16
- extras:
  - shape.disk_gib: 20
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: no session cap published; 600-day purge for unvalidated accounts
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing while idle
  - keep_rate.source: https://sdf.org/
  - persistent_storage.included_gib: 0
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: 2 years without a login
  - network_out.allow_outbound: no
  - network_out.allow_inbound_listen: no
  - network_out.ports: none published; the free level withholds outbound ssh and the compilers
  - free_tier_kind: always-free
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - shape_note: 20 MB is quoted in the vendor's own MB; no RAM or vCPU is published
  - term: indefinite with a login every 2 years once validated
  - price_arithmetic: no charge; the ARPA upgrade is USD 36 once, which is not required for the free level
- evidence:
  - probe:sdf.org:22 2026-10-22: TCP connect succeeded in 0.56 s to 205.166.94.16 and read banner SSH-2.0-OpenSSH_10.4, so the host is up and speaking SSH
  - [2] 2026-10-06: 20 MB disk quota per filesystem, 500-file cap, and a 2-year login expiry
  - [1] 2026-10-22: the FREE USER tier carries 20 MB of disk quota on each of four filesystems; the 150 MB and 5,000-file figures on the same page belong to the USD 36 ARPA membership
  - [2] 2026-10-22: a validated account expires if the user does not log in at least once during a 2-year period
  - [3] 2026-10-24: quoted: 'inbound ssh, ftp and sftp connections' listed under 'USERS (free)'; and under '$36 (one time initiation fee) LIFETIME ARPA Membership (arpa)': 'outbound telnet, ssh, sftp, ftp, ytalk, irc, snarf, wget' and 'gcc, elisp, perl, php, python, ruby'
  - [1] 2026-10-24: quoted: '20 MB disk quota for your email', '20 MB disk quota for your home directory', '20 MB disk quota for your webspace'
  - [2] 2026-10-24: quoted: 'Prevalidated accounts are automatically purged whether they are in use or not approximately 600 days of their creation. Validated accounts will expire if the user does not login at least once during a 2 year period.'
  - [4] 2026-10-24: quoted: 'Linux/UNIX users can type 'ssh [address removed]' at their shell prompts.'
- sources:
  - [1] https://sdf.org/?faq?MEMBERS?01
  - [2] https://sdf.org/?faq?MEMBERS?05
  - [3] https://sdf.org/?join
  - [4] https://sdf.org/?signup
