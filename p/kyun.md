# Kyun.host Bricks

> kyun.sh | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/kyun/ | JSON https://fshy.ajam.dev/api/v1/entity/kyun.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Kyun.host Bricks (HDD block)

- `storage/kyun-host-bricks` | qualifies-with-caveat | evidence reported | binding per-object-cap | category block-storage
- needs card no, phone no, ID no, institution no | verified 2026-11-25T13:25:55.252Z (live) | stale on 2026-12-10
- url https://blog.kyun.sh/p/bricks
- price $5.62/TB/mo flat (€5). At 5 TB: €25 = $28.09/mo. At 20 TB: €100 = $112.34/mo. No volume break. The caveats (20 TB total supply, price flagged to rise, provider's own no-SLA warning) make this a poor primary and a reasonable third replica. | parsed USD 5.62/TB-mo
- free tier: HDD block volumes attached to a Danbo VM, Romania only. Initial beta run ~20 TB capacity total across all customers. | unit: TB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: unverified: the ~20TB figure is total initial beta supply, not a per-object cap | source: [1] | note: not stated
- retention: unverified: no retention clause stated on the Bricks post | source: [1] | note: unverified: no retention clause stated on the Bricks post
- egress: unverified: no egress price or quota stated on the Bricks post | metered: yes
- identity: email | detail: email
- interface: unknown
- limits:
  - per-object-cap (binding): unverified: no per-object cap stated; ~20TB is total initial beta supply [1]
- limits note: Total supply is ~20TB for the entire beta; the price is flagged to rise. No per-object cap stated.
- interface detail: Inside the VM the disks show up as regular raw disks (/dev/sdx); no upload interface stated on the Bricks post
- tooling: Format the raw disk with any filesystem; no upload interface stated on the Bricks post
- composes with: Bricks can be attached and detached to and from any Danbo in the same datacenter.
- reliability: The most honest reliability disclosure and simultaneously the worst track record. The provider's own post-Mesa writeup describes a migration that 'took about 5 days' with intermittent unreachability, a multi-week server-delivery failure, and states plainly: 'do NOT use Kyun for anything that earns you money without a verified, up to date backup that you can roll over to at a moment's notice'. Also notes customers 'reported us to the cops'. No identity documents required — a rare property here.
- notes: the same as the free tier
- extras:
  - price_verbatim: $5.62/TB/mo flat (€5). At 5 TB: €25 = $28.09/mo. At 20 TB: €100 = $112.34/mo. No volume break. The caveats (20 TB total supply, price flagged to rise, provider's own no-SLA warning) make this a poor primary and a reasonable third replica.
- evidence:
  - [1] 2026-10-21: 'The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks'
  - [2] 2026-10-21: 'Bricks are now 5 EUR/TB/mo, down from 7 EUR'; the operational post-mortem quoted above
  - [3] 2026-10-21: 'it never asks for identity documents. An account is still required'; 'HDD block storage from €5/TB/month'
  - [4] 2026-11-19: the archived first-party page confirms the ~20 TB initial beta run and its price | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks
  - [4] 2026-11-19: the archived first-party page confirms the Romania-only availability | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: For now, Bricks are only available in Romania.
  - [4] 2026-11-25: Bricks appear inside the VM as raw disks | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: Inside the VM, they show up as regular raw disks (/dev/sdx), and you can format them with any filesystem you like.
  - [4] 2026-11-25: the raw disk can be formatted with any filesystem | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: Inside the VM, they show up as regular raw disks (/dev/sdx), and you can format them with any filesystem you like.
  - [4] 2026-11-25: ~20TB is the size of the initial beta run, not a per-object limit | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks, so get 'em while they're hot.
  - [4] 2026-11-25: the beta run is ~20TB and the price is flagged to rise | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks, so get 'em while they're hot.
  - [4] 2026-11-25: the Bricks post states attachment and detachment within a datacenter | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: Bricks are virtual disks that can be attached and detached to and from any Danbo in the same datacenter as the Brick.
  - [4] 2026-11-25: the Bricks post states a storage price and beta capacity, with no traffic price or quota | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks, so get 'em while they're hot.
  - [4] 2026-11-25: the Bricks post states price and capacity, with no retention clause | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks, so get 'em while they're hot.
  - [4] 2026-11-25: the Bricks post states price and beta capacity only | capture: sha256:e21ad43b58d05dea5c358dea1ddba424b82c2fa1c61255251c84adbac6618b5b | quote: The current price for the initial ~20TB beta run is 5 EUR/TB/month. This price will probably increase a bit for future restocks, so get 'em while they're hot.
- sources:
  - [1] https://blog.kyun.sh/p/bricks
  - [2] https://blog.kyun.host/p/mesa
  - [3] https://cunicula.com/en/provider/kyun
  - [4] https://web.archive.org/web/20260516014833/https://blog.kyun.sh/p/bricks?provider=wayback
