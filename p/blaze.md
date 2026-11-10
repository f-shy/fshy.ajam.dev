# Blaze

> blaze.cx | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/blaze/ | JSON https://fshy.ajam.dev/api/v1/entity/blaze.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Blaze (BLAZE Quantum)

- `storage/blaze` | fails-quota | evidence reported | binding per-object-cap | category cloud-drive
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://blaze.cx
- free tier: Free Forever: 2 GB transfer with 7-day retention, plus 2 GB of BLAZE Drive storage, 2 workspaces, 2 upload portals. Starter €6/user/mo: 100 GB transfer / 30-day retention / 100 GB Drive. | unit: GB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: per-object-cap: 2 GB | bytes: 2000000000 | source: [1] | note: not stated
- retention: Free Forever: 2 GB transfer with 7-day retention, plus 2 GB of BLAZE Drive storage, 2 workspaces, 2 upload portals | days: 7 | source: [1] | note: not stated
- egress: not separately metered. | metered: yes
- identity: card
- interface: cli
- limits:
  - per-object-cap (binding): per-object-cap: 2 GB [1]
- limits note: per-object-cap: 2 GB transfer, 7-day retention on free. The 2 GB Drive is permanent but tiny. Workspace count (2) is the multiplication lever and it is too small to matter.
- interface detail: none
- tooling: No public API or CLI found. Account-gated workspace product (quantum-safe E2EE suite: Transfer + Drive + Notes + Messaging).
- composes with: 2 free workspaces x 2 GB. Trivial volume, and the transfer allowance and Drive storage are separate small pools. Nothing here multiplies.
- reliability: Its marketing page claims 'No size limits' for Transfer while its own pricing page says 2 GB. A direct contradiction within the same site. Trust the pricing page.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: retention
  - dead_end.why: Free Forever: 2 GB transfer with 7-day retention, plus 2 GB of BLAZE Drive storage, 2 workspaces, 2 upload portals. Starter €6/user/mo: 100 GB transfer / 30-day retention / 100 GB Drive.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'Free Forever ... 2GB transfer / 7-day retention, 2GB BLAZE Drive storage, 2 free workspaces'
  - [2] 2026-10-21: 'Transfer ... No size limits. No account required for recipients' (contradicts pricing)
- sources:
  - [1] https://blaze.cx/pricing/
  - [2] https://blaze.cx/
