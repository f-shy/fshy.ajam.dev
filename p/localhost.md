# localhost.run

> localhost.run | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/localhost/ | JSON https://fshy.ajam.dev/api/v1/entity/localhost.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## localhost.run

- `egress/localhost-run` | fails-egress | evidence documented | binding per-ip-shaping | category tunnel (hosted, SSH)
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-12-06
- url https://localhost.run/docs/
- free tier: free random subdomain over SSH, no account | unit: unlimited | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable: a stream
- retention: the subdomain rotates per session | source: [1]
- egress: speed-limited with no published value; measured 11.4 kB/s (about 11.2 KiB/s), about 0.99 GB/day | metered: no | source: [1]
- identity: anonymous | detail: the nokey@ ssh target needs no account
- interface: ssh
- limits:
  - per-ip-shaping (binding): 4,128,768 of 104,857,600 bytes in 180 s on a 100 MiB object, and 1,027,916 of 1,048,576 in 90 s on a 1 MiB object probe
  - per-ip-shaping (binding): about 6-8 kB/s on the anonymous tier; a 4 MiB transfer does not complete probe:https://709bf77787aa29.lhr.life/
- binding note: two objects of different sizes hit the same ~23 KB/s aggregate ceiling, so it is shaping.
- interface detail: ssh -R 80:127.0.0.1:PORT nokey@localhost.run
- tooling: OpenSSH
- composes with: composes with nothing: at 11.4 kB/s a request/response API is usable and no bulk transfer is.
- reliability: the free hostname is a random <hex>.lhr.life subdomain that changes every session; the anonymous path is the nokey@ username, and a harness measured a hard throttle of about 6-8 kB/s, so a 4 MiB transfer does not complete.
- notes: SSH-based reverse tunneling service. Throughput on free connections measured at 11.4 kB/s (1,027,916 bytes in 90 s, about 11.2 KiB/s, approximately 0.99 GB/day). A sandbox measured about 6-8 kB/s on the anonymous tier on 2026-11-05.
- evidence note: the free tier works end to end but throttles to about 6-8 kB/s, so a 4 MiB transfer does not complete (measured 2026-11-05).
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: the tunnel carries the origin's bytes, at a measured 11.4 kB/s
  - wg_path: none
- evidence:
  - probe:https://2ea044f1475bd0.lhr.life/blob100m.bin 2026-10-22: 200 with 4,128,768 of 104,857,600 bytes in 180 s, then the client timeout
  - probe:https://2ea044f1475bd0.lhr.life/blob1m.bin 2026-10-22: 200 with 1,027,916 of 1,048,576 bytes in 90 s, then the client timeout
  - probe:https://2ea044f1475bd0.lhr.life/small.txt 2026-10-22: 200, 3 bytes in 1.75 s: the control path works
  - [1] 2026-10-23: 'Put a locally running HTTP, HTTPS or TLS app on the internet' and 'no account setup is needed for free domains'
  - probe:https://709bf77787aa29.lhr.life/ 2026-11-05: the anonymous tier throttles a transfer to about 6-8 kB/s | capture: sha256:1c52272c47512567e0682ca55a92e49de554676e0d01ae7004ab278defdb8c8e | quote: ~6-8 KB/s
- sources:
  - [1] https://localhost.run/docs/
