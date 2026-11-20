# Deplexo

> deplexo.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deplexo/ | JSON https://fshy.ajam.dev/api/v1/entity/deplexo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Deplexo

- `compute/deplexo` | qualifies-with-caveat | evidence documented | binding per-object-cap | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://deplexo.com/plans
- free tier: Free plan, quoted: '1 app', 'CPU per app 0.25 CPU', 'RAM per app 128 MB RAM', 'Disk per app 250 MB disk', 'Network speed per app 10 Mbit/s', '100 GB/mo' transfer. Paid: 'Starter USD 5 / 30 days' for 3 apps at 0.5 CPU, 512 MB RAM, 2 GB disk, 500 GB transfer; 'Pro USD 10 / 30 days' for 6 apps at 1 CPU, 1 GB RAM, 10 GB disk, 1 TB. 'No credit card required to start'. Billing is '30 days, paid in advance ... We don't renew it automatically'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Aggregator claim checked: free-for.dev lists '1 app with 0.25 vCPU, 128 MB RAM, 250 MB disk, and 100 GB bandwidth'. | metered: no | source: [1]
- identity: email | detail: no card and no payment method: the homepage states 'Free tier - No credit card required', so no hold exists. The evidence does not say which identifier the account is created with, so whether an email alone suffices is not stated; debit and prepaid acceptance are not stated
- interface: rest
- limits:
  - per-object-cap (binding): 250 MB of disk and 128 MB of RAM per app is the wall: it fits a small API and not a build plus a runtime plus data. [1]
- limits note: 250 MB of disk and 128 MB of RAM per app is the wall: it fits a small API and not a build plus a runtime plus data.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a 128 MB container is enough for a scraper, a webhook receiver or a scheduling control plane, and because the paid step is a prepaid 30-day block rather than a subscription it can be switched on for one month of load and left off afterwards.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev lists '1 app with 0.25 vCPU, 128 MB RAM, 250 MB disk, and 100 GB bandwidth'. The vendor matches on every number, so the gap is zero here. What the aggregator omits: the read-only root filesystem with one writable volume at /data, no managed database, a single region, and that Starter and Pro are prepaid 30-day blocks renewed by hand through PayPal rather than subscriptions.
- extras:
  - facets.class: aggregator-confirmed
  - facets.free_tier_kind: free-forever
  - facets.shape.vcpu: 0.25
  - facets.shape.ram_gib: 0.125
- evidence:
  - [1] 2026-10-22: Free column: '1 app', '0.25 CPU', '128 MB RAM', '250 MB disk', '10 Mbit/s', '100 GB/mo'; Starter 'USD 5 / 30 days' with '3 apps', '0.5 CPU', '512 MB RAM', '2 GB disk'; Pro 'USD 10 / 30 days', quoted
  - [2] 2026-10-22: 'Free tier - No credit card required' and the stated stop points 'One instance per app', 'No managed databases', 'The container filesystem is read-only', 'Apps run in the EU (Germany)', quoted
- sources:
  - [1] https://deplexo.com/plans
  - [2] https://deplexo.com/
