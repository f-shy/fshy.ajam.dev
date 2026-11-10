# tilde.guru

> tilde.guru | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde-3/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde-3.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tilde.guru

- `compute/tilde-guru` | qualifies-with-caveat | evidence documented | binding write-gated | category shared shell
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://tilde.guru/
- free tier: a free FreeBSD pubnix account, about 214 users; no RAM, CPU or disk figure is published | unit: none | metered on: none | read on: 2026-10-06 | source: [1] | note: signup is curated: 'Talk to sarmonsiill about getting an account'
- per-object cap: not applicable
- retention: no idle policy documented
- egress: not published | metered: no | source: [1]
- identity: email | detail: a request to the operator; no card
- interface: rest, cli
- limits:
  - write-gated (binding): signup is curated by a person and was disabled at one point after excess use [1]
- limits note: the human gate is the constraint, not a quota
- binding note: signup is curated by a person and was disabled at one point, so the human gate binds before any quota
- interface detail: SSH on port 22
- tooling: SSH, cron, a FreeBSD userspace
- composes with: a FreeBSD shell behind a human gate
- reliability: no reliability event recorded
- notes: The port is open and the banner did not arrive, which is a slow or filtered greeting rather than a dead host. The gate is a person, and that is the fact that decides whether it is available.
- evidence note: reachability only: a probe proves the port answers, not the account gate, so the record is not `measured`
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: tilde.guru
  - port: 22
  - ms: 410
  - ok: yes
  - peer: 2a05:f480:1400:a93:5400:3ff:fe7b:d45d
- extras:
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: none documented
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://tilde.guru/
  - persistent_storage.price_gib_month: not offered
  - persistent_storage.durability: home directory
  - persistent_storage.survives_stop: yes
  - persistent_storage.survives_destroy: no
  - persistent_storage.max_retention: while active
  - network_out.allow_outbound: yes
  - network_out.static_ip: no
  - network_out.ipv6: yes
  - free_tier_kind: allowance
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - probe_result: port open, no banner within 12 s
- evidence:
  - probe:tilde.guru:22 2026-10-22: TCP connect succeeded in 0.41 s over IPv6 (2a05:f480:1400:a93:5400:3ff:fe7b:d45d) but the host sent no banner within 6 s
  - [1] 2026-10-22: 'tilde.guru is a FreeBSD pubnix server, part of the tildeverse. Free shell accounts for those who seek knowledge'; the page lists member home directories at 512 MB each
- sources:
  - [1] https://tilde.guru/
