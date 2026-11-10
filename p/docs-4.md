# srv.us

> docs.srv.us | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/docs-4/ | JSON https://fshy.ajam.dev/api/v1/entity/docs-4.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## srv.us

- `egress/srv-us` | fails-egress | evidence documented | binding none | category tunnel (SSH, HTTP/TLS only) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-12-06
- url https://docs.srv.us/
- price USD 0
- free tier: Free and fully open source. Stable URLs derived from your SSH key. No accounts. | unit: unlimited | metered on: none | read on: 2026-10-23 | source: [1]
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: no quota published; the offer is 'Free and fully open source' with no account and no stated cap; ingress: http-only | metered: no | free allowance: none published | source: [1]
- identity: anonymous | detail: an SSH key pair and nothing else: 'Stable URLs derived from your SSH key. No accounts.' | country: None
- interface: ssh
- limits:
  - per-ip-shaping: about 31-43 kB/s on the anonymous tier; a 4 MiB transfer does not complete in 60-80 s probe:https://h3pkbwcm6vf3gysn3lt26bpomq.srv.us/
- binding note: Nothing in the vocabulary binds because the transport cannot carry a UDP datagram at all; the limit is protocol, not quantity.
- interface detail: ssh srv.us -R 1:localhost:3000
- tooling: OpenSSH
- composes with: HTTP ingress only; composes with a web service and nothing that needs UDP
- reliability: one operator (xmit dev team); the tunnel lives only while the ssh session lives; a harness measured a 357 ms median latency and about 31-43 kB/s, so a 4 MiB transfer does not complete in 60-80 s.
- notes: Worth reading because it is the rare no-account service with a stable address, which is the property WireGuard needs. The protocol excludes it. A sandbox measured a 357 ms median latency and about 31-43 kB/s on 2026-11-05.
- evidence note: Raise by attempting a UDP forward with ssh -R and recording the server's refusal; not attempted because the service is documented as an HTTP terminator.
- extras:
  - wg_path: none
  - wg_detail: the service terminates TLS and speaks HTTP: 'expose any HTTP server to the Internet through a tunnel' and returns https URLs, so there is no UDP path
  - ingress: http-only
  - volume_stated: no quota published; the offer is 'Free and fully open source' with no account and no stated cap
  - bytes_transit: yes
  - transit_note: srv.us relays the HTTP traffic
- evidence:
  - [1] 2026-10-23: 'Yet another solution to expose any HTTP server to the Internet through a tunnel', 'Free & fully open source. Stable URLs derived from your SSH key. No accounts.'
  - probe:https://h3pkbwcm6vf3gysn3lt26bpomq.srv.us/ 2026-11-05: the anonymous tier transfers at about 31-43 kB/s | capture: sha256:37e445a31ee1c439875a6c6066b4342adc1b36f0c01c07cee9029600a10d4268 | quote: ~31-43 KB/s
- sources:
  - [1] https://docs.srv.us/
