# serveo

> serveo.net | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serveo/ | JSON https://fshy.ajam.dev/api/v1/entity/serveo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## serveo

- `egress/serveo` | fails-egress | evidence reported | binding per-ip-shaping | category tunnel (hosted, SSH)
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-11-20
- url https://serveo.net/
- free tier: 3 active tunnels and custom subdomains, no account | unit: requests | metered on: request-count | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: the assigned hostname is unusable, so nothing is served for any period | source: [1]
- egress: not published; the assigned hostname resolves to 0.0.0.0 and ::, so no byte is reachable | metered: no | source: [1]
- identity: anonymous | detail: the ssh target needs no account; a key is optional for reserved names
- interface: ssh
- limits:
  - per-ip-shaping (binding): the tunnel hostname has no usable A or AAAA record, so the data path does not exist probe
  - per-ip-shaping (binding): anonymous raw TCP: one random port for 10 minutes, two connections, 256 KiB/s cap; with a key: 30 minutes, five connections, 1 MiB/s [2]
  - per-ip-shaping (binding): public TCP and UDP forwarding are paid-only [3]
  - per-object-cap: a large transfer is cut at about 2.4-2.5 MiB after about 10 s on the anonymous tier probe:https://cc2e2fd2b49711e2-104-28-207-178.serveousercontent.com/
- binding note: with no resolvable address there is no meter and no capacity; the control plane is the whole product that works.
- interface detail: ssh -R 80:localhost:3000 serveo.net
- tooling: OpenSSH
- composes with: composes with nothing: the SSH leg succeeds and the HTTP leg has no DNS record.
- reliability: the SSH banner printed a tunnel URL that has no usable DNS record, on two separate sessions; a harness measured a 710 ms median latency and a 4 MiB transfer cut at about 2.4-2.5 MiB after about 10 s, while the tunnel itself stayed up.
- notes: Serveo provides SSH and WireGuard port forwarding. Free tiers receive an HTTP hostname; raw public TCP and UDP forwarding require a paid Pro subscription at $60 annually. A sandbox measured a 710 ms median latency and a transfer cut at about 2.4-2.5 MiB after about 10 s on 2026-11-05, while the tunnel stayed up.
- evidence note: the anonymous tier carries about 230 kB/s and cuts a transfer at about 2.4-2.5 MiB after about 10 s, while the tunnel stays up (measured 2026-11-05).
- extras:
  - stale_after_days: 180
  - bytes_transit: no
  - transit_note: the control plane answers and the data path does not exist: the assigned hostname resolves to 0.0.0.0 and ::
- evidence:
  - [1] 2026-10-22: 3 active tunnels and custom subdomains on the free plan
  - probe:https://8c67940209469eab-103-129-134-194.serveousercontent.com/ 2026-10-22: the hostname from the SSH banner resolves to 0.0.0.0 and :: from 8.8.8.8; two sessions, two dead names, curl exits 6
  - [3] 2026-10-23: 'wg.serveo.net:51820 is the public UDP endpoint used to connect to Serveo.' and 'Paid accounts can forward a raw TCP or UDP port through a WireGuard peer.'
  - [2] 2026-10-23: 'Public UDP forwarding remains a paid WireGuard feature.' and the anonymous raw TCP cap
  - [1] 2026-10-23: 'Get 3 active tunnels and custom subdomains for $0/month' and Pro at $60/yr
  - probe:https://cc2e2fd2b49711e2-104-28-207-178.serveousercontent.com/ 2026-11-05: a 4 MiB transfer is cut at about 2.4-2.5 MiB after about 10 s while the tunnel stays up | capture: sha256:463ee9a99b08d1fdbe7df302753f6e4ab1f14ac4754c77bce1f1b2eca0a65023 | quote: connection died at 10.5s, 2,400,032
- sources:
  - [1] https://serveo.net/
  - [2] https://serveo.net/docs
  - [3] https://serveo.net/docs/wireguard
