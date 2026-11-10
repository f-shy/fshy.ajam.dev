# NeoNeko Git

> neoneko.org | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/neoneko/ | JSON https://fshy.ajam.dev/api/v1/entity/neoneko.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NeoNeko Git (Forgejo, open registration)

- `storage/neoneko-git` | qualifies-with-caveat | evidence reported | binding per-object-cap | category registry
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://git.neoneko.org
- free tier: No published storage quota. Site advertises 'no seat limits, no repository caps'; Forgejo ships quota disabled by default (quota.ENABLED=false, quota.default.TOTAL=-1 = unlimited), and this instance exposes no quota documentation. | unit: unlimited | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: No per-file cap documented | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: No metered download policy published; Cloudflare-fronted. Not contradicted anywhere on the instance. | metered: yes
- identity: institution
- interface: rest, oci
- limits:
  - per-object-cap (binding): No per-file cap documented [1]
- limits note: Unstated. No per-file cap documented. Small instance (29 public repos observed via API search), self-hosted runner, Patreon-funded. Accounts left unactivated are auto-removed.
- interface detail: rest
- tooling: Full Forgejo API v1 with Swagger at /api/swagger; OCI registry at /v2/; generic package registry; LFS; Actions on an owner-run runner.
- composes with: Unknown per-account cap x unlimited free accounts. If the default holds (TOTAL=-1), each account is effectively unbounded. This is the 'unlimited free identity x no quota' case, strictly better than CodeFloe but with zero published guarantee.
- reliability: Hobby instance run by one admin; tiny disk budget implied by the funding model. Unpublished quota means an admin can introduce one at any moment with no notice. Data-loss risk is materially higher than a commercial forge.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Public and private repositories, no seat limits, no repository caps'; 'Full API access ... documented with Swagger'
  - [2] 2026-10-21: probe: GET -> {"version":"16.0.5+gitea-1.22.0"} (live Forgejo 16.0.5)
  - [3] 2026-10-21: probe: GET -> 401 with Bearer realm https://git.neoneko.org/v2/token (registry enabled, not a stub)
  - withheld 2026-10-21: probe: anonymous /v2/token -> 200 (anonymous pull path exists)
  - [4] 2026-10-21: probe: GET -> 29 repos (small instance, quota never exercised at scale)
  - [5] 2026-10-21: quota.ENABLED defaults false, quota.default.TOTAL defaults -1
- sources:
  - [1] https://git.neoneko.org/
  - [2] https://git.neoneko.org/api/v1/version
  - [3] https://git.neoneko.org/v2/
  - [4] https://git.neoneko.org/api/v1/repos/search?limit=50
  - [5] https://forgejo.org/docs/latest/admin/config-cheat-sheet/
