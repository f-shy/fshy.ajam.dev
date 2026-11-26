# libp2p circuit-relay

> github.com | Egress and tunnels, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/github-libp2p/ | JSON https://fshy.ajam.dev/api/v1/entity/github-libp2p.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## libp2p circuit-relay v2

- `egress/libp2p-circuit-relay-v2` | fails-quota | evidence documented | binding per-object-cap | category relay (protocol)
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:04:40.150Z (live) | stale on 2026-12-26
- url https://github.com/libp2p/specs/blob/master/relay/circuit-v2.md
- free tier: whatever the relay operator allows; the reference implementations cap a circuit by default | unit: none | metered on: downloaded-bytes | read on: 2026-10-22 | source: [1]
- per-object cap: 128 KiB per direction per relayed connection by default | bytes: 131072 | source: [1]
- retention: 2 minutes per relayed connection by default | source: [1]
- egress: not applicable: the protocol's own default ends a circuit at 128 KiB per direction | metered: no | source: [1]
- identity: anonymous | detail: peers are identified by a generated keypair
- interface: unknown
- limits:
  - per-object-cap (binding): 128 KiB per direction per relayed connection by default [1]
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
  - [1] 2026-11-25: the js-libp2p source states the default data limit is 128 KiB | capture: sha256:6cd6c3388867a4945ce3fa478fc0ad1ee47cbea88f99e6347a79454431f7387d | quote: // 128k is the default data limit
  - [1] 2026-11-25: the reference implementation still defaults to 128 KiB and a 2-minute circuit duration | capture: sha256:6cd6c3388867a4945ce3fa478fc0ad1ee47cbea88f99e6347a79454431f7387d | quote: export const DEFAULT_DURATION_LIMIT = 2 * minute // 128k is the default data limit export const DEFAULT_DATA_LIMIT = BigInt(1 << 17)
  - [2] 2026-11-25: the go-libp2p reference implementation states the same 128 KB default per direction | capture: sha256:911144c74d289910035c2d4010d6a8e78d11d068808f451831823f40c71e5937 | quote: // Defaults to 128KB
- sources:
  - [1] https://github.com/libp2p/js-libp2p/blob/master/packages/transport-circuit-relay-v2/src/constants.ts
  - [2] https://github.com/libp2p/go-libp2p/blob/master/p2p/protocol/circuitv2/relay/resources.go

## libp2p circuit-v2 public relays

- `storage/libp2p-circuit-v2-public-relays` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:14:07.998Z (live) | stale on 2026-12-04
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
  - [1] 2026-11-19: first-party constants.ts still sets the default relay data limit to 128 KiB and duration to 2 minutes | capture: sha256:6cd6c3388867a4945ce3fa478fc0ad1ee47cbea88f99e6347a79454431f7387d | quote: // 2 min is the default connection duration export const DEFAULT_DURATION_LIMIT = 2 * minute // 128k is the default data limit export const DEFAULT_DATA_LIMIT = BigInt(1 << 17)
- sources:
  - [1] https://github.com/libp2p/js-libp2p/blob/master/packages/transport-circuit-relay-v2/src/constants.ts
  - [2] https://github.com/libp2p/specs/blob/master/relay/circuit-v2.md
