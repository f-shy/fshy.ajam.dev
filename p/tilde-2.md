# tilde.green

> tilde.green | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tilde-2/ | JSON https://fshy.ajam.dev/api/v1/entity/tilde-2.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## tilde.green

- `compute/tilde-green` | qualifies-with-caveat | evidence documented | binding per-object-cap | category shared shell
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:31.813Z (live) | stale on 2026-12-05
- url https://tilde.green/
- free tier: a free shared Ubuntu 24.04 account; the provider publishes 50 processes, nice 10, a 40-login limit and 1 GB soft and 1.5 GB hard storage | unit: GiB | metered on: stored-bytes | read on: 2026-10-06 | source: [1] | note: the operator states 'we don't mind if you register and stay idle'
- per-object cap: not applicable
- retention: no idle policy; the operator states a positive promise that idle accounts are welcome
- egress: not published | metered: no | source: [1]
- identity: email | detail: an account request; no card
- interface: ssh
- limits:
  - per-object-cap (binding): 1 GB soft and 1.5 GB hard per account [1]
  - request-rate: 50 processes, nice 10, 40 concurrent logins [1]
- binding note: 1.5 GB hard storage is the published ceiling and the operator states idle accounts are welcome, so the quota is what binds
- interface detail: SSH on port 22
- tooling: SSH, screen or tmux, cron, an Ubuntu userspace
- composes with: the only pubnix here with an explicit no-idle-kill promise from the operator
- reliability: no reliability event recorded
- notes: Tilde.green provides shared Unix shell accounts on OpenBSD systems with basic file hosting, IRC, and email services.
- evidence note: Service reachability was confirmed on 2026-10-22; quota figures reflect terms read on 2026-10-06, as tilde.green/tos returned HTTP 404 upon re-request.
- probe:
  - probed_at: 2026-10-22T03:55:15.270Z
  - host: tilde.green
  - port: 22
  - ms: 300
  - ok: yes
  - banner: SSH-2.0-OpenSSH_10.6p1 Debian-1
  - peer: 2001:41d0:303:5ddb::
- extras:
  - shape.disk_gib: 1.5
  - billing_model: flat-pool
  - session_cap.restart_required: no
  - session_cap.note: none documented
  - keep_rate.value: 0.0
  - keep_rate.basis: a free account costs nothing
  - keep_rate.source: https://tilde.green/
  - persistent_storage.included_gib: 1.5
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
- evidence:
  - probe:tilde.green:22 2026-10-22: TCP connect succeeded in 0.30 s and read banner SSH-2.0-OpenSSH_10.6p1 Debian-1
  - [1] 2026-10-22: 'we don't mind if you register and stay idle', and the host states Ubuntu 24.04.1 LTS
  - [1] 2026-11-03: the host publishes SSH host keys, so SSH is the access interface | capture: sha256:cd2807228b519c250a39c06dece34ea717f48cc6eb7f96d5e484f0da4ad9a9bf | quote: tilde.green ssh-ed25519
  - [1] 2026-11-03: idle accounts are welcome | capture: sha256:cd2807228b519c250a39c06dece34ea717f48cc6eb7f96d5e484f0da4ad9a9bf | quote: we don't mind if you register and stay idle
- sources:
  - [1] https://tilde.green/
