# Syncthing community relay pool

> syncthing.net | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/syncthing/ | JSON https://fshy.ajam.dev/api/v1/entity/syncthing.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Syncthing community relay pool

- `storage/syncthing-community-relay-pool` | qualifies-with-caveat | evidence reported | binding per-ip-shaping | category P2P relay pool (operator-donated)
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://relays.syncthing.net/
- free tier: No quota at all. Relay operators cap themselves with -global-rate (commonly ~20 Mbps in and out). The pool is anonymous and unvetted. | unit: unlimited | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Free. Paid for by whoever runs each relay, not by a company with a budget. | metered: no
- identity: anonymous | detail: anonymous
- interface: unknown
- limits:
  - per-ip-shaping (binding): 20 Mbps [1]
- limits note: Per-relay bandwidth set by the operator; sessions per client and per relay are limited. Relays can vanish without notice.
- binding note: one stream is shaped, and aggregate throughput is the shaped rate times the number of streams
- interface detail: relay:// protocol on 22067; the pool is a JSON endpoint.
- tooling: strelaysrv; Syncthing's own relay selection.
- composes with: Relay is only used until a direct connection is established; Syncthing then switches to direct and the relay carries nothing.
- reliability: The pool endpoint returns dozens of `relay://IP:22067` entries with self-signed device IDs. No accounting means no sustainability, but also no gate.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: literal JSON list of relay:// URLs with IDs
  - [2] 2026-10-21: 'Anyone can run a relay server, and it will automatically join the relay pool'
  - [3] 2026-10-21: traffic is bounced via a relay only when a direct connection is impossible
  - [4] 2026-10-21: 'The relays listed on this page are not managed or vetted by the Syncthing project'
- sources:
  - [1] https://relays.syncthing.net/endpoint
  - [2] https://docs.syncthing.net/users/strelaysrv
  - [3] https://docs.syncthing.net/users/relaying.html
  - [4] https://relays.syncthing.net/
