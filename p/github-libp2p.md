# libp2p circuit-relay

> github.com | Egress and tunnels, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-libp2p/ | JSON https://fshy.ajam.dev/api/v1/entity/github-libp2p.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## libp2p circuit-relay v2

- `egress/libp2p-circuit-relay-v2` | fails-quota | evidence documented | binding per-object-cap | category relay (protocol)
- needs card no, phone no, ID no, institution no | verified 2026-10-22T03:20:00.000Z (live) | stale on 2026-11-22
- url https://github.com/libp2p/specs/blob/master/relay/circuit-v2.md
- free tier: whatever the relay operator allows; the reference implementations cap a circuit by default | unit: none | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 128 KiB per direction per relayed connection by default | bytes: 131072 | source: [1]
- retention: 2 minutes per relayed connection by default | source: [1]
- egress: not applicable: the protocol's own default ends a circuit at 128 KiB per direction | metered: no | source: [1]
- identity: anonymous | detail: peers are identified by a generated keypair
- interface: unknown
- limits:
  - per-object-cap (binding): 128 KiB per direction per relayed connection by default [2]
  - retention-clamped: 2 minutes per relayed connection by default [1]
- limits note: the 128 KiB value is defined in both reference implementations and their wording differs. go-libp2p's Data field comment reads 'The limit of data relayed (on each direction) before resetting the connection', which is where the per-direction qualifier comes from; js-libp2p defines DEFAULT_DATA_LIMIT = 1 << 17 with '128k is the default data limit' and no per-direction language
- interface detail: /libp2p/circuit/relay/0.2.0/hop and /stop
- tooling: js-libp2p, go-libp2p
- composes with: composes with nothing at this volume: 128 KiB per circuit means a 1 GiB object needs 8,192 relayed connections, so it is a NAT-traversal primitive and not a transport.
- reliability: the limits are defaults an operator can raise; the reference implementations ship them at these values
- notes: Architecturally excluded from bulk, not merely slow: 128 KiB is 2^17 bytes, so 1 TiB needs 8.4 million relayed connections. The free tier is genuine and the capacity is zero.
- extras:
  - stale_after_days: 180
  - bytes_transit: yes
  - transit_note: a relayed circuit carries bytes in both directions, capped at 128 KiB per direction by default
- evidence:
  - [1] 2026-10-22: DEFAULT_DATA_LIMIT = BigInt(1 << 17) and DEFAULT_DURATION_LIMIT = 2 * minute, with the comment '128k is the default data limit'
  - [2] 2026-10-22: quoted from the Data field comment: 'Data is the limit of data relayed (on each direction) before resetting the connection', 'Defaults to 128KB', with Data: 1 << 17 in the default Resources literal
- sources:
  - [1] https://github.com/libp2p/js-libp2p/blob/master/packages/transport-circuit-relay-v2/src/constants.ts
  - [2] https://github.com/libp2p/go-libp2p/blob/master/p2p/protocol/circuitv2/relay/resources.go

## libp2p circuit-v2 public relays

- `storage/libp2p-circuit-v2-public-relays` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://github.com/libp2p/js-libp2p/blob/master/packages/transport-circuit-relay-v2/src/constants.ts
- free tier: none reachable: Default relay limits are signalling-grade, not transport-grade: 128 KiB of data and 2 minutes per relayed connection. Fine for hole-punching, useless for bytes. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Default relay limits are signalling-grade, not transport-grade: 128 KiB of data and 2 minutes per relayed connection. Fine for hole-punching, useless for bytes.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Default relay limits are signalling-grade, not transport-grade: 128 KiB of data and 2 minutes per relayed connection. Fine for hole-punching, useless for bytes.
  - [2] 2026-10-21: cited as the basis of the rejection: Default relay limits are signalling-grade, not transport-grade: 128 KiB of data and 2 minutes per relayed connection. Fine for hole-punching, useless for bytes.
- sources:
  - [1] https://github.com/libp2p/js-libp2p/blob/master/packages/transport-circuit-relay-v2/src/constants.ts
  - [2] https://github.com/libp2p/specs/blob/master/relay/circuit-v2.md
