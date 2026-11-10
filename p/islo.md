# Islo

> islo.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/islo/ | JSON https://fshy.ajam.dev/api/v1/entity/islo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Islo

- `compute/islo` | qualifies-with-caveat | evidence documented | binding request-rate | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T11:01:15.546Z (live) | stale on 2026-12-05
- url https://islo.dev/pricing
- free tier: starting credits at signup with no card; a running computer bills $0.07 a CPU-hour, $0.04 a GB-hour of memory and $0.0007 a GB-hour of disk, and a stopped computer bills nothing | unit: mixed | metered on: wall-clock | read on: 2026-10-22 | source: [1]
- per-object cap: not stated | source: [1]
- retention: not stated | source: [1]
- egress: No egress allowance or overage price is published on the pricing page; it prices CPU time, memory and storage only. | metered: no | source: [1]
- identity: email | detail: 'You get credits when you sign up. No credit card required.', quoted from islo.dev/pricing read 2026-10-22
- interface: cli
- limits:
  - request-rate (binding): $0.07 a CPU-hour, $0.04 a GB-hour of memory and $0.0007 a GB-hour of disk [1]
  - retention-clamped: stopping the computer stops the meter; there is no idle fee [1]
- interface detail: CLI, per the CLI reference: "The CLI follows the factory workflow."
- tooling: the islo command-line client, per the CLI reference: "Use `islo schema <command>` to see the installed command and manifest schema."
- composes with: not established
- reliability: no reliability event recorded
- evidence note: the pricing page was read on 2026-10-22 and states the three hourly meters and that stopping ends the meter. The credit's size is not published, so the record states a credit exists and does not put a number on it
- extras:
  - keep_rate: 0.0
  - keep_rate_basis: first-party: e alternatives More Community Agent infrastructure glossary Security Customers Pricing Sign in Start an agent
  - billing_model: unclassified
  - session_cap.restart_required: no
  - session_cap.note: the computer is stopped by the caller; the vendor states no reap, and cost limits per task are offered as a guardrail
  - free_tier_kind: one-time-credit
  - burst_x: 1.0
  - ps.price: $0.0007 a GB-hour
  - ps.durability: disk
  - ps.on_stop: yes
  - ps.on_destroy: no
  - ps.retention: until deleted
  - net.out: yes
  - net.in: yes
  - crosscheck.boat_compare_2026-09-26: USD 0.600/h at 4 vCPU / 8 GB
- evidence:
  - [1] 2026-10-02: 
  - [1] 2026-10-22: 'CPU, memory, and storage billed per hour. Stop the computer, stop the meter.' with '$0.07/CPU-hour', '$0.04/GB-hour', '$0.0007/GB-hour' of disk and 'You get credits when you sign up. No credit card required.' quoted
  - [2] 2026-10-22: a competitor's comparison table lists Islo at USD 0.600 per hour for a 4 vCPU / 8 GB / 50 GB machine, with list prices dated 2026-09-26; this is a reported rate about a third party and not a reading of the vendor's own page
  - [3] 2026-11-03: a CLI exists | capture: sha256:b387eb6388bddda88ab7f248c6a4192a54d468276fb5b38182afef4f85594252 | quote: The CLI follows the factory workflow.
  - [1] 2026-11-03: pricing lists CPU, memory and disk only; no egress line | capture: sha256:1410027da6890d65a038b8f251a1eaf51706f2bde3b961b66d532d05441bbf37 | quote: Pay only while the Machine runs: CPU + memory + disk.
  - [3] 2026-11-04: the page documents a CLI | capture: sha256:b387eb6388bddda88ab7f248c6a4192a54d468276fb5b38182afef4f85594252 | quote: The CLI follows the factory workflow.
  - [3] 2026-11-04: the page names the islo command | capture: sha256:b387eb6388bddda88ab7f248c6a4192a54d468276fb5b38182afef4f85594252 | quote: Use `islo schema <command>` to see the installed command and manifest schema.
- sources:
  - [1] https://islo.dev/pricing
  - [2] https://boat.dev/compare
  - [3] https://docs.islo.dev/cli/overview.md
