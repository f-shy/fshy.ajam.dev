# Binder

> mybinder.readthedocs.io | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mybinder-readthedocs-io/ | JSON https://fshy.ajam.dev/api/v1/entity/mybinder-readthedocs-io.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Binder (mybinder.org), public mybinder.org

- `compute/mybinder` | fails-quota | evidence documented | binding volume-quota | category notebook runtime | tier public mybinder.org
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html
- free tier: free and unauthenticated: at least 1 GB RAM with a 2 GB maximum, up to 6 hours of session time or 1 CPU-hour, whichever comes first; no persistent storage of any sort | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: The governing limit is one CPU-hour, so six hours of session is only available to an idle kernel.
- per-object cap: not applicable: the unit is a session, not an object
- retention: none: 'We do not offer persistent storage of any sort' | days: 0 | source: [1]
- egress: outgoing bandwidth limited to about 1 mbit per session | metered: yes | free allowance: about 1 mbit/s per session | source: [1]
- identity: anonymous | detail: no account and no card: a Binder link runs straight from a public repository. The service logs IP addresses for 30 days for abuse detection.
- interface: git, rest
- limits:
  - volume-quota (binding): 1 CPU-hour per session, or 6 hours of wall clock [1]
  - per-ip-shaping: about 1 mbit/s of outgoing bandwidth per session [1]
  - retention-clamped: 0 days: no persistent storage at all [1]
  - volume-quota (binding): 100 simultaneous user sessions per repository [1]
- binding note: one CPU-hour is reached in an hour of real work, and there is no disk to keep the result on
- interface detail: a Git repository is built into a Docker image and served as a JupyterHub session
- tooling: any repo with a requirements.txt or environment.yml; the launch URL is the interface
- composes with: a reproducible demo environment for a repo, not a place to compute: one CPU-hour and no disk
- reliability: the project states it has no dedicated funding and runs on donated cloud, and it caps launches from most cloud providers
- notes: The only anonymous provider in evaluated offerings, and the only one with a published CPU-hour cap that small. RAM is the project's own 'GB'; whether that is GB is not stated.
- evidence note: memory, session length, bandwidth and the absence of storage are all quoted from the project's user guidelines today.
- extras:
  - shape.ram_gib: 2
  - shape.disk_gib: 0
  - shape.note: 1 GB guaranteed, 2 GB maximum; CPU is bounded in cpu-hours rather than cores
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00: donated infrastructure, no paid tier
  - free_tier_kind: free-forever-with-quota
  - unattended: no
  - unattended_mechanism: none: the session is bound to the browser and to the one-cpu-hour budget
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: outbound only
  - network_out.static_ip: no
  - network_out.ipv6: no
  - network_out.per_session_bytes: about 1 mbit/s
  - session_cap.wall_clock_min: 360
  - session_cap.restart_required: yes
  - session_cap.note: 6 h or 1 CPU-hour, whichever comes first; no persistence
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: quoted, emphasis markers in the original: 'users are guaranteed at least 1GB of RAM, with a maximum of 2GB'
  - [1] 2026-10-24: quoted: 'Binder aims to provide up to six hours of session time per user session, or up to one cpu-hour for more computationally intensive sessions.'
  - [1] 2026-10-24: quoted: 'We do not offer persistent storage of any sort, to protect us from becoming a host for malware.'
  - [1] 2026-10-24: quoted, with the code span preserved: 'We limit outgoing bandwidth per-session ( `~1mbit`) to protect against being used as a DDoS vector.'
  - [1] 2026-10-24: quoted, bold markers in the original: 'The maximum number of simultaneous users for a given repo is 100.'
- sources:
  - [1] https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html

## binder (mybinder.org), binder

- `storage/binder` | dead | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html
- free tier: none reachable: Explicitly no persistence of any kind, and egress is throttled to ~1 mbit per session to stop it being used as a DDoS vector. Sessions die after 10 min idle / 6 h max, 1-2 GB RAM. A pure… | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
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
- extras:
  - dead_end.failure_class: dead-service
  - dead_end.why: Explicitly no persistence of any kind, and egress is throttled to ~1 mbit per session to stop it being used as a DDoS vector. Sessions die after 10 min idle / 6 h max, 1-2 GB RAM. A pure…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Explicitly no persistence of any kind, and egress is throttled to ~1 mbit per session to stop it being used as a DDoS vector. Sessions die after 10 min idle / 6 h max, 1-2 GB RAM. A pure…
- sources:
  - [1] https://mybinder.readthedocs.io/en/latest/about/user-guidelines.html
