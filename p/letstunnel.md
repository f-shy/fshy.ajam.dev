# LetsTunnel

> letstunnel.com | Egress and tunnels; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/letstunnel/ | JSON https://fshy.ajam.dev/api/v1/entity/letstunnel.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## LetsTunnel

- `egress/letstunnel` | fails-egress | evidence reported | binding none | category relay (hosted, HTTPS tunnel, QUIC) | tier free
- needs card no, phone no, ID no, institution no | verified 2026-11-10T03:20:00.000Z (live) | stale on 2026-11-25
- url https://letstunnel.com/
- free tier: Free for developers with no account, with public HTTPS URLs, QUIC on UDP 8443 and a desktop app. On 2026-11-05 the relay presented a self-signed certificate and no tunnel could be established. | unit: none | metered on: none | read on: 2026-11-10 | source: [1]
- per-object cap: not applicable: a tunnel, not an object | source: [1]
- retention: not applicable: a live tunnel | source: [1]
- egress: no byte quota is published; the relay was unreachable with a valid certificate on 2026-11-05 | metered: no | source: [1]
- identity: anonymous | detail: no account is claimed: the page says 'Free for developers', and no signup was attempted
- interface: cli
- binding note: nothing is reachable to bind on: the relay presented a self-signed certificate on 2026-11-05, so a client that verifies TLS cannot connect.
- interface detail: the letstunnel CLI starts a tunnel and prints a public https://<name>.letstunnel.com URL; the documented relay port is UDP 8443 over QUIC
- tooling: the letstunnel npm CLI, a node wrapper around a Rust client
- composes with: nothing chains until the relay certificate is fixed; the authless claim looks genuine and the CLI loads
- reliability: the relay presented a self-signed certificate on 2026-11-05, so a client that verifies TLS cannot connect; the documented relay port 8443 was unreachable
- notes: The authless claim looks genuine and the CLI loads, but the relay presented a self-signed certificate on 2026-11-05, so no tunnel could be established. Retest when the certificate is fixed.
- evidence note: the free and no-account claims are read from the vendor page; the certificate failure is a sandbox observation, so the record is reported
- evidence:
  - [1] 2026-11-10: a user is free for developers | capture: sha256:d81003b301c95239418c5f7f55a1d858639d0cde75ef8409b2f162278c425ae8 | quote: Free for developers.
  - probe:https://relay.letstunnel.com:443 2026-11-05: the relay presented a self-signed certificate | capture: sha256:827d21fcb63a90b50a38a346bcd6b225a023bc86743668470d7e5282abaf6983 | quote: self-signed certificate
- sources:
  - [1] https://letstunnel.com/
