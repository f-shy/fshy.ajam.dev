# Filen Pro

> filen.io | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/filen/ | JSON https://fshy.ajam.dev/api/v1/entity/filen.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Filen Pro X (10 TiB)

- `storage/filen-pro-x` | qualifies | evidence reported | binding none | category E2EE cloud drive, subscription
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filen.io/pricing
- price $4.49/TB at 10 TiB ($44.93); $4.49/TB at 20 TiB ($89.86) | parsed USD 4.49/TB-mo
- free tier: Pro I 200 GiB / Pro II 500 GiB / Pro III 2 TiB / Pro X 10 TiB. 'Plans stack on a single account. Combine two Pro X plans for 20 TiB on one Filen account, with no upper limit.' | unit: TiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Verbatim on every tier: 'Unlimited bandwidth' and 'Unlimited uploads' | metered: no
- identity: email | detail: email
- interface: rclone, cli
- limits note: none on transfer; quota is the cap
- interface detail: rclone `filen` backend, desktop client, CLI
- tooling: rclone native backend
- composes with: rclone -> anywhere; E2EE means server-side transcode/range-serve story is awkward
- reliability: Brief §1.5 warns Filen withholds quota behind VPN IPs. Client-driven E2EE means a lost password is unrecoverable. No mass data-loss event documented.
- notes: the same as the free tier
- extras:
  - price_verbatim: $4.49/TB at 10 TiB ($44.93); $4.49/TB at 20 TiB ($89.86)
- evidence:
  - [1] 2026-10-21: 'Pro X 10 TiB 39.99 EUR monthly ... Unlimited bandwidth ... Plans stack on a single account. Combine two Pro X plans for 20 TiB'
- sources:
  - [1] https://filen.io/pricing

## Filen

- `storage/filen` | fails-quota | evidence reported | binding none | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://filen.io
- free tier: 10 GiB free at signup; Pro I 200 GiB / €1.99 mo, Pro III 2 TiB / €8.99 mo | unit: GiB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'Unlimited bandwidth' on every paid plan; free tier is not bandwidth-metered but is 10 GiB, so egress is not the binding constraint | metered: yes
- identity: card
- interface: rest, rclone
- limits note: 10 GiB unless referred; 'Accounts that do not receive the free 10 GB will also not be eligible for any referral bonuses'; referrals add ~10 GB each up to 30 GB
- interface detail: rest
- tooling: rclone backend 'filen' (official); zero-knowledge client-side encryption
- composes with: The 10 GiB is per account. Separate accounts each held 10 GiB in the past, and Filen closed that: as of the Feb 2026 policy the free 10 GiB is only granted when signup looks like a consumer connection (one-time Ipregistry VPN/proxy classification)
- reliability: active, well-maintained service but the several-accounts route is now explicitly detected at signup; a VPN/proxy signup yields an account with zero free storage
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 10 GiB free at signup; Pro I 200 GiB / €1.99 mo, Pro III 2 TiB / €8.99 mo
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Get started with 10 GiB of free space', Pro tiers 200 GiB-10 TiB with 'Unlimited bandwidth'
  - [2] 2026-10-21: (published 2026-02-11) — free 10 GB granted only for non-anonymised signup IPs via Ipregistry; 'attempts to create large numbers of free accounts, often through VPNs or proxies, to collect huge amounts of free storage'
- sources:
  - [1] https://filen.io/pricing
  - [2] https://filen.io/hub/an-update-on-free-account-creation/
