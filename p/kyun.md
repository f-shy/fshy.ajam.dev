# Kyun.host Bricks

> kyun.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kyun/ | JSON https://fshy.ajam.dev/api/v1/entity/kyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kyun.host Bricks (HDD block)

- `storage/kyun-host-bricks` | qualifies-with-caveat | evidence reported | binding per-object-cap | category block-storage
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://blog.kyun.sh/p/bricks
- price $5.62/TB/mo flat (€5). At 5 TB: €25 = $28.09/mo. At 20 TB: €100 = $112.34/mo. No volume break. The caveats (20 TB total supply, price flagged to rise, provider's own no-SLA warning) make this a poor primary and a reasonable third replica. | parsed USD 5.62/TB-mo
- free tier: HDD block volumes attached to a Danbo VM, Romania only. Initial beta run ~20 TB capacity total across all customers. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 20 TB cap | bytes: 20000000000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not published as a per-plan number. The model is a VM plus attachable block, with the VM carrying the traffic allowance. Treat as unknown/unmetered-by-usage rather than free. This is a one-person operation and the beta explicitly has no published egress schedule. | metered: yes
- identity: email | detail: email
- interface: rest, sftp, ssh, rclone
- limits:
  - per-object-cap (binding): 20 TB cap [1]
- limits note: per-object-cap: none. Total supply is ~20 TB for the entire beta. Price explicitly flagged as likely to rise: 'This price will probably increase a bit for future restocks'.
- interface detail: block + sftp/ssh (Danbo), rest api
- tooling: rclone over SFTP, Kyun API v2 (api.kyun.sh/endpoints)
- composes with: Can be grown while attached, renamed in the UI, and switched between local SSD and Bricks 'with a single click'. Designed for media storage rather than hot reads.
- reliability: The most honest reliability disclosure and simultaneously the worst track record. The provider's own post-Mesa writeup describes a migration that 'took about 5 days' with intermittent unreachability, a multi-week server-delivery failure, and states plainly: 'do NOT use Kyun for anything that earns you money without a verified, up to date backup that you can roll over to at a moment's notice'. Also notes customers 'reported us to the cops'. No identity documents required — a rare property here.
- notes: the same as the free tier
- extras:
  - price_verbatim: $5.62/TB/mo flat (€5). At 5 TB: €25 = $28.09/mo. At 20 TB: €100 = $112.34/mo. No volume break. The caveats (20 TB total supply, price flagged to rise, provider's own no-SLA warning) make this a poor primary and a reasonable third replica.
- evidence:
  - [1] 2026-10-21: 'The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks'
  - [2] 2026-10-21: 'Bricks are now 5 EUR/TB/mo, down from 7 EUR'; the operational post-mortem quoted above
  - [3] 2026-10-21: 'it never asks for identity documents. An account is still required'; 'HDD block storage from €5/TB/month'
- sources:
  - [1] https://blog.kyun.sh/p/bricks
  - [2] https://blog.kyun.host/p/mesa
  - [3] https://cunicula.com/en/provider/kyun
