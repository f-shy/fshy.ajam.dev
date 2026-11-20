# tilde.town

> tilde.town | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde-7/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde-7.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tilde.town

- `compute/tilde-town` | qualifies-with-caveat | evidence documented | binding request-rate | category shared shell
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://tilde.town/wiki/faq.html
- free tier: a free shared shell account while active; no RAM, CPU or disk figure is published | unit: none | metered on: none | read on: 2026-10-06 | source: [1] | note: signup is by invitation or request
- per-object cap: not applicable
- retention: no expired-account policy is published; the 7-day auto-kick applies to the IRC channel and not the shell
- egress: ports are not opened for users | metered: no | source: [1]
- identity: email | detail: an account request; no card
- interface: rest, cli
- limits:
  - request-rate (binding): no user ports are opened; services are local-only [1]
  - write-gated: signup is by invitation or request [1]
- limits note: any admin may kill a process under load
- binding note: no user ports are opened at all: the network policy binds and no quota is published
- interface detail: SSH on port 22
- tooling: SSH, screen or tmux, crontab, a shared Debian userspace
- composes with: a shell to hold a cron job, reachable only outbound; a relay is required to serve anything
- reliability: no reliability event recorded
- notes: Reachable today and quiet. The network is the wall, not the machine: no inbound port exists, so anything served must be pulled out through a tunnel.
- evidence note: reachability only: a probe proves the port answers, not the quota, so the port policy carries the documented rung and the record is not `measured`
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: tilde.town
  - port: 22
  - ms: 560
  - ok: yes
  - banner: SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4
  - peer: 2602:f72c:0:400::be50:77ed
- extras:
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: none published
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://tilde.town/wiki/faq.html
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while active
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: none opened for users
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - free_tier_kind: allowance
  - m10h_usd: 0.0
  - m24h_usd: 0.0
- evidence:
  - probe:tilde.town:22 2026-10-22: TCP connect succeeded in 0.56 s over IPv6 and read banner SSH-2.0-OpenSSH_10.0p2 Debian-7+deb13u4; an earlier saved run on the same day recorded 7.49 s for the same host, so the connect time is a property of the path and not of the host
  - [1] 2026-10-22: 'we don't open any ports for users to use; however, you can run simple services or cron jobs for local-only access', quoted
- sources:
  - [1] https://tilde.town/wiki/faq.html
