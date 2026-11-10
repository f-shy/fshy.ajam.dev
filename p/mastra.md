# Mastra

> mastra.ai | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/mastra/ | JSON https://fshy.ajam.dev/api/v1/entity/mastra.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Mastra

- `compute/mastra` | qualifies-with-caveat | evidence documented | binding volume-quota | category platform host
- identity a placeholder: card and phone unknown | verified 2026-11-04T02:24:32.967Z (live) | stale on 2026-12-05
- url https://mastra.ai
- free tier: Mastra Platform Starter, $0 a month: 100K events and 24 CPU hours, then $10 per 100K events and $0.35 per CPU hour; the open-source framework is free to self-host | unit: mixed | metered on: wall-clock | read on: 2026-10-29 | source: [1] | note: read from the vendor pricing page; the plan is priced a month, and whether the allowance resets monthly is not stated
- per-object cap: not stated | source: [2]
- retention: not stated | source: [2]
- egress: Starter includes 10 GB of Server data egress, then USD 0.10 per GB; the Teams and Enterprise columns list 100 GB then USD 0.10 per GB | metered: yes | free allowance: 10 GB (Starter) | price per TB: USD 100 per TB | source: [2]
- identity: email
- interface: cli
- limits:
  - volume-quota (binding): the hosted Starter plan includes 100K events and 24 CPU hours; usage past them is billed at $10 per 100K events and $0.35 per CPU hour [1]
- limits note: Session cap, idle-reap and network policy are not documented. Exceeds capacity threshold.
- interface detail: the mastra CLI (mastra deploy) pushes a project to a platform environment; no hosted management REST API or SSH was found on the pages read
- tooling: the mastra CLI with mastra deploy to the hosted platform
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-29: the hosted Mastra Platform has a Starter plan at $0 a month with 100K events and 24 CPU hours, above Teams at $250 a month. The site read on 2026-10-22 described only the open-source framework
- self hosted: no
- extras:
  - keep_rate_basis: no field in the source
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the harness manages sessions inside a user's own deployment
  - persistent_storage.price: a user's own storage
  - persistent_storage.durability: thread storage in a user's database
  - persistent_storage.on_stop: yes
  - persistent_storage.on_destroy: no
  - persistent_storage.max_retention: as long as a user keeps it
  - free_tier_kind: none
- evidence:
  - [2] 2026-10-02: 
  - [2] 2026-10-22: the site was read on 2026-10-22 and describes an open-source TypeScript agent framework with workflows, memory and a harness; it publishes no plan, price or free tier
  - [1] 2026-10-29: the hosted Mastra Platform Starter plan is $0 a month with 100K events and 24 CPU hours, then $10 per 100K events and $0.35 per CPU hour | capture: sha256:936f71462973221783f3fe021a0488c107af750cc3e991c9a163971d3e209d13 | quote: 24 CPU hours+ $0.35/hr
  - [1] 2026-11-03: the Starter column of the Server data-egress row: 10 GB, then $0.10 per GB | capture: sha256:936f71462973221783f3fe021a0488c107af750cc3e991c9a163971d3e209d13 | quote: 10GBthen $0.10/GB
  - [3] 2026-11-03: the mastra CLI deploys to the hosted platform | capture: sha256:ed35f882359bbafecac74947b56b1cf0f171b0d728d6192abf362fb8808a8f66 | quote: Builds and deploys your project to the Mastra platform environment selected by `--env`.
- sources:
  - [1] https://mastra.ai/pricing
  - [2] https://mastra.ai
  - [3] https://mastra.ai/reference/cli/mastra
