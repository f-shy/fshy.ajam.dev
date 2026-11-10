# ix

> ix.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/ix/ | JSON https://fshy.ajam.dev/api/v1/entity/ix.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## ix

- `compute/ix` | paid-only | evidence documented | binding none | category container and VM sandbox
- identity a placeholder: card and phone unknown | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://ix.dev/pricing
- free tier: Three meters only: USD 0.0288 per vCPU-hour of CPU time used, USD 0.0108 per GiB-hour of memory in use, USD 0.101 per GiB-month of disk, and egress at USD 0 for measured outbound traffic. Memory the host caches is free and identical disk bytes are stored once across all machines. An idle machine costs about USD 0.14 a day, a stopped one pays only its disk, a removed one pays nothing. 'There is no free credit on signup.' | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: USD 0.0288 per vCPU-hour used, USD 0.0108 per GiB-hour in use, USD 0.101 per GiB-month of disk, outbound traffic USD 0 and measured, an idle machine about USD 0.14 a day, and 'There is no free credit on signup' | metered: no | source: [1]
- identity: card | detail: unverified: no page stating the signup requirement was read; the record's evidence covers the meters (USD 0.0288 per vCPU-hour used, USD 0.0108 per GiB-hour, USD 0.101 per GiB-month of disk, outbound traffic USD 0), 'There is no free credit on signup', prepaid bundles such as 'Dev USD 20 gives USD 40 of usage', and that running machines stop at once when funds run out. Whether a card is required, and whether debit or prepaid is accepted, is not stated.
- interface: unknown
- limits note: Nothing binds above the scale except the balance: running machines stop at once when funds run out with no grace period, and disks and snapshots are kept 24 hours before deletion.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: Billing on CPU time actually used rather than allocated is what makes a 24/7 agent VM affordable here: a machine that sits idle at 1 percent of a vCPU with 0.5 GiB resident costs USD 4.20 for 30 days, which is the cheapest always-up shape found among evaluated providers, and free egress means serving from it costs nothing extra.
- reliability: no reliability event recorded
- notes: Classified as paid-only because the vendor states plainly that there is no free credit on signup; that sentence is the finding, since three other providers among evaluated providers give USD 20 to USD 100 without a card. The notable terms are the free egress and the idle arithmetic: USD 4.20 for a month of an idle 0.5 GiB machine against USD 47.95 for BoxLite's Small box running 30 days and USD 20 flat for RemoteHost's Starter. Machines go up to 100 vCPUs. What kills a running job is the balance, with no grace period and a 24-hour window before the disk is deleted.
- extras:
  - facets.class: used-resource-vm
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 2
  - facets.shape.ram_gib: 8
  - facets.shape.disk_gib: 20
- evidence:
  - [1] 2026-10-22: USD 0.0288 per vCPU-hour used, USD 0.0108 per GiB-hour in use, USD 0.101 per GiB-month of disk, outbound traffic USD 0 and measured, an idle machine about USD 0.14 a day, and 'There is no free credit on signup'
  - [1] 2026-10-22: a busy 2 vCPU / 8 GiB / 20 GiB machine costs USD 105.70 per 30 days, a stopped one USD 2.03, and plans are prepaid bundles that never discount the meters: Dev USD 20 gives USD 40 of usage and 20 GiB of disk
  - [1] 2026-10-22: when funds run out running machines stop at once with no grace period, disks and snapshots are kept 24 hours, and after that window data is deleted
- sources:
  - [1] https://ix.dev/pricing
