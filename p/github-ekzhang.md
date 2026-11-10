# bore

> github.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-ekzhang/ | JSON https://fshy.ajam.dev/api/v1/entity/github-ekzhang.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## bore

- `egress/bore` | qualifies-with-caveat | evidence documented | binding none | category tunnel software with a public relay
- needs card no, phone no, ID no, institution no | verified 2026-11-05 (live) | stale on 2026-12-06
- url https://github.com/ekzhang/bore
- free tier: MIT client and server; bore.pub is one shared public instance | unit: none | metered on: none | read on: 2026-10-22 | source: [1]
- per-object cap: not applicable
- retention: not applicable | source: [1]
- egress: self-host: the operator's NIC. bore.pub: shared, with no commitment | metered: no | source: [1]
- identity: anonymous | detail: the software needs no account
- interface: cli
- limits:
  - per-ip-shaping: no per-user byte cap: the whole public instance carried 1.5 TB in one month and 2.8 TB in a later month (figures from the instance's maintainer), with a standing request to 'be reasonable with how much data you transfer' and to use it for short-lived port exposure [2]
- limits note: no limit of any of the six kinds was published for bore.pub: it is one shared public instance with no commitment, and the software imposes none
- binding note: Nothing in the vocabulary binds: bore.pub publishes no quota and imposes no rate. The operator's numbers are the ceiling of the whole instance, 1.5 TB in one month (2023-01-02) and 2.8 TB in one month (2024-08-01), so a single client at 1 TiB/month would be 39 to 73 per cent of everything the public instance was observed to carry, and the operator's answer to that was a request to reduce.
- interface detail: bore local PORT --to bore.pub
- tooling: part of the free tier
- composes with: bore local PORT --to bore.pub reaches the public instance with no host; a bore server the user runs is the last resort.
- reliability: one shared instance on a single DigitalOcean host, funded by sponsorship, with a standing abuse problem: the author has publicly considered shutting it down and has had phishing reports on bore.pub. A harness measured a 406-410 ms median on bore.pub; its bulk-transfer figure came through that sandbox's WARP egress and is not a fact about bore.
- notes: Public demo instance at bore.pub provides ephemeral TCP tunnels without published throughput or bandwidth guarantees. Public infrastructure is shared and subject to rate limits and upstream abuse filtering. A sandbox measured a 406-410 ms median latency on bore.pub on 2026-11-05; its bulk-transfer figure there was an artifact of that sandbox egress path.
- evidence note: bore 0.6.0 server and client on one host carried a 4,194,304-byte object byte-identically (sha256 46386cf4dbccceb80f80148d46d37f1a30d72912089cfbe4b3e51d9d55a79747) at 1.88 MiB/s against a 53.47 MiB/s direct baseline, so the software is measured. The record is documented and not measured because bore.pub, the one public instance, publishes no capacity: a sandbox measured a 406-410 ms median latency on 2026-11-05, and its bulk-transfer figure there was an artifact of that sandbox egress path.
- self hosted: no
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: bore.pub relays the stream; the self-host probe proves the transport and not bore.pub capacity, which is unpublished
  - ingress: tcp
- evidence:
  - [1] 2026-10-22: MIT-licensed client and server
  - probe:bore-local://127.0.0.1:51768/blob4m.bin 2026-10-22: bore-cli 0.6.0 server and client on one host: GET /blob4m.bin returned 200 with 4,194,304 bytes, sha256 46386cf4dbccceb80f80148d46d37f1a30d72912089cfbe4b3e51d9d55a79747 matching the source, 2.123 s, 1.88 MiB/s, against 0.075 s and 53.47 MiB/s direct
  - probe:https://cloudflare-dns.com/dns-query?name=bore.pub&type=A 2026-10-22: bore.pub resolves to 159.223.110.159 and 2604:a880:400:d1:0:4:822c:e001 over DNS-over-HTTPS and TCP 7835 to that address accepts a connection
  - [3] 2026-10-23: 'A modern, simple TCP tunnel in Rust ... That's all it does' and 'forwarding TCP traffic'
  - [2] 2026-11-03: the public-instance operator states a request to be reasonable with transferred volume and sets no per-user byte cap; the same page gives 1.5 TB and 2.8 TB per month for the whole instance | capture: sha256:4cc9926c0cf89a6b0323cfd9a8360e4ec69f4490b131f605b9359ac8038a93c6 | quote: Please respect other users and be reasonable with how much data you transfer.
  - [1] 2026-11-03: bore.pub is the one public instance of the server | capture: sha256:f0000d4963e55d52d576cef6947643ca67f1317eb04e368e48a6da7b7b4f1682 | quote: As mentioned in the startup instructions, there is a public instance of the `bore` server running at `bore.pub`.
  - probe:bore.pub:2898 2026-11-05: bore.pub answered with a 406-410 ms median latency | capture: sha256:c2b7d914b3c3f54f523c99110ca0e6ecc6d3688effa6272495a7eb3dd562aafa | quote: med 406-410 / p95 422-462 ms
- sources:
  - [1] https://github.com/ekzhang/bore
  - [2] https://github.com/ekzhang/bore/issues/68
  - [3] https://raw.githubusercontent.com/ekzhang/bore/main/README.md
