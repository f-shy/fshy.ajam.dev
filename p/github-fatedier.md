# frp

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-fatedier/ | JSON https://fshy.ajam.dev/api/v1/entity/github-fatedier.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## frp

- `egress/frp` | self-hosted, last resort | verdict paid-only | evidence measured | binding volume-quota | category tunnel (self-hosted software)
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-12-22
- url https://github.com/fatedier/frp
- free tier: Apache-2.0 client and server; no hosted free tier found | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [1]
- egress: Self-hosted deployment: traffic is governed by host network terms. | metered: no | source: [1]
- identity: anonymous | detail: the software needs no account
- interface: cli
- binding note: the software imposes no limit, so what runs out first is the monthly egress allowance of the host it runs on, and that host is a separate provider with its own bill
- interface detail: frpc against your own frps
- tooling: frp
- composes with: composes only with a server that a user pays for, so it is self-hosted software, not a free service.
- reliability: no credible free public frps was found; every 'free frp server' lead was a VPS advertisement
- notes: Open-source reverse proxy software for publishing local services behind NAT or firewalls. Self-hosted tool requiring deployment on external server infrastructure.
- evidence note: frps and frpc 0.71.1 ran on this host: a 4,194,304-byte object read back through the TCP proxy byte-identically, sha256 46386cf4dbccceb80f80148d46d37f1a30d72912089cfbe4b3e51d9d55a79747, 42.91 MiB/s against a 38.73 MiB/s direct baseline. No hosted free tier exists, so this measures the software and not a service
- self hosted: yes
- extras:
  - stale_after_days: 180
  - bytes_transit: self-hosted
  - transit_note: no hosted free tier exists; the 4 MiB probe ran against a local frps and the bytes transited this host
  - hosting_requirement: a rented or free compute service with a public address; no local machine is assumed
- evidence:
  - [1] 2026-10-22: Apache-2.0 client and server
  - probe:frp-local://127.0.0.1:18080/blob4m.bin 2026-10-22: frps and frpc 0.71.1 on one host with a tcp proxy: GET /blob4m.bin returned 200 with 4,194,304 bytes, sha256 46386cf4dbccceb80f80148d46d37f1a30d72912089cfbe4b3e51d9d55a79747 matching the source, 0.093 s, 42.91 MiB/s against 38.73 MiB/s direct
- sources:
  - [1] https://github.com/fatedier/frp
