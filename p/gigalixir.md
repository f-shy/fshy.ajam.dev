# Gigalixir

> gigalixir.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/gigalixir/ | JSON https://fshy.ajam.dev/api/v1/entity/gigalixir.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Gigalixir

- `compute/gigalixir` | qualifies-with-caveat | evidence documented | binding retention-clamped | category platform host
- needs card yes, phone no, ID no, institution no | verified 2026-11-04T02:24:32.964Z (live) | stale on 2026-12-05
- url https://gigalixir.com/pricing
- free tier: Free tier, quoted: '1 App Replica (0.5 GB memory)', 'Free Tier PostgreSQL Database', 'Custom Domains & SSL', 'Zero-downtime Deploys'. The free database is capped at '10k Rows' and '2 connections'. Paid Standard is 'USD 10/mo' for 0.2 GB, scaling to 'Up to 384 GB' of replica memory and '10+ (Horizontal)' replicas. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: a Free app 'Sleeps after 30 days' without a deploy, and the free database stops at 10,000 rows and 2 connections, which a real workload reaches first. | source: [1]
- egress: Standard production bandwidth is included with the provisioned resources, with no per-GB price and no numeric allowance published; a fair-use policy applies to extremely high-volume egress, and the page recommends Dedicated Ingress at USD 250/mo for massive data transfer. | metered: no | source: [1]
- identity: card | detail: a credit card required at signup on every plan, the free tier included: the pricing page states 'A credit card is required at signup for all plans. Free Tier usage is not charged.' The authorisation amount is not stated; whether debit or prepaid is accepted is not stated; no phone or ID step is stated
- interface: cli, ssh
- limits:
  - retention-clamped (binding): a Free app 'Sleeps after 30 days' without a deploy, and the free database stops at 10,000 rows and 2 connections, which a real workload reaches first. [1]
- limits note: a Free app 'Sleeps after 30 days' without a deploy, and the free database stops at 10,000 rows and 2 connections, which a real workload reaches first.
- binding note: the same as limits note
- interface detail: the gigalixir CLI (macOS, Linux, Windows); SSH and a remote console on every plan; no REST API page was found
- tooling: the gigalixir CLI installs with a one-line script; SSH and a remote console are available on every plan
- composes with: an Elixir or Phoenix app plus a 10,000-row Postgres on one free tier is a complete small backend with no charge; the free replica publishes no vCPU number, so sizing it needs a run rather than a table.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'one free instance that never sleeps and a free-tier PostgreSQL database limited to 2 connections, 10,000 rows'. The 'never sleeps' half is wrong: the vendor table says Free 'Sleeps after 30 days' of no deploy and only Standard never sleeps. The aggregator omits the card requirement at signup, which is the identity cost that decides whether this is reachable. vCPU is not published for the free replica and is null rather than guessed.
- extras:
  - facets.free_tier_kind: free-forever
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: Free Tier card: '1 App Replica (0.5 GB memory)', 'Free Tier PostgreSQL Database', 'Custom Domains & SSL', 'Zero-downtime Deploys', quoted
  - [1] 2026-10-22: comparison table: 'Inactivity Policy | Sleeps after 30 days | Never sleeps' and 'DB Size Limit | 10k Rows', quoted
  - [1] 2026-10-22: 'A credit card is required at signup for all plans. Free Tier usage is not charged.', quoted
  - [1] 2026-11-03: bandwidth is included with provisioned resources and no per-GB price is published | capture: sha256:0caede6d66b79d3112de089f4bce7e0276ceaa1dd7381d2b30701c83f1af88d1 | quote: Standard production bandwidth is included with your provisioned resources.
  - [1] 2026-11-03: a fair-use policy applies to extremely high-volume egress, with no stated volume | capture: sha256:0caede6d66b79d3112de089f4bce7e0276ceaa1dd7381d2b30701c83f1af88d1 | quote: However, to ensure platform stability for everyone, we maintain a fair-use policy for extremely high-volume egress.
  - [2] 2026-11-03: a CLI controls the platform | capture: sha256:196c2a2022cfb0033cd983f30bf070da680f2e606a56e5af5908ad90889b7b02 | quote: The Gigalixir Command-Line Interface or CLI is a tool you install on your local machine to control Gigalixir.
  - [1] 2026-11-03: SSH and a remote console are included on every plan, the Free plan included | capture: sha256:0caede6d66b79d3112de089f4bce7e0276ceaa1dd7381d2b30701c83f1af88d1 | quote: | SSH & Remote Console | ✓ Full Access | ✓ Full Access | ✓ Full Access |
- sources:
  - [1] https://gigalixir.com/pricing
  - [2] https://gigalixir.com/docs/cli
