# Deplexo

> deplexo.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/deplexo/ | JSON https://fshy.ajam.dev/api/v1/entity/deplexo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Deplexo

- `compute/deplexo` | qualifies-with-caveat | evidence documented | binding per-object-cap | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-25T11:17:24.267Z (live) | stale on 2026-12-26
- url https://deplexo.com/plans
- free tier: Free plan, quoted from the plans page: '1 app', 'CPU per app: 0.25 CPU', 'RAM per app: 128 MB RAM', table rows 'DiskPer app | 250 MB disk', 'Network speedPer app | 10 Mbit/s', and 'Monthly transferShared across your account | 100 GB/mo'. The page states '100 GB monthly transfer across your account.' Paid: 'Starter' '$5/ 30 days' for '3 apps' at '0.5 CPU', '512 MB RAM', '2 GB disk', '500 GB monthly transfer'; 'Pro' '$10/ 30 days' for '6 apps' at '1 CPU', '1 GB RAM', '10 GB disk', '1 TB monthly transfer'. Prices in USD. 'No. You can create an account and run one app on the Free plan without adding payment details.' Billing: '30 days, paid in advance: Pay through PayPal. Renewing the same active plan adds 30 days to its expiry date. We don’t renew it automatically.' | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: free-forever
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
  - [1] 2026-11-25: the capture states the Free, Starter and Pro per-app CPU, RAM, disk and network speed and the shared monthly transfer allowances | capture: sha256:30c982d68876f8d32946db5ce8b13e4839f20ee945458b151a888f8d648bf342 | quote: | CPU limitPer app · shared hardware | 0.25 CPU | 0.5 CPU | 1 CPU | ... | RAMPer app | 128 MB RAM | 512 MB RAM | 1 GB RAM | ... | DiskPer app | 250 MB disk | 2 GB disk | 10 GB disk | ... | Network speedPer app | 10 Mbit/s | 100 Mbit/s | 200 Mbit/s | ... | Monthly transferShared across your account | 100 GB/mo | 500 GB/mo | 1 TB/mo |
  - [1] 2026-11-25: the plans page still states the Free, Starter and Pro per-app limits and the shared monthly transfer allowances | capture: sha256:30c982d68876f8d32946db5ce8b13e4839f20ee945458b151a888f8d648bf342 | quote: | CPU limitPer app · shared hardware | 0.25 CPU | 0.5 CPU | 1 CPU | ... | RAMPer app | 128 MB RAM | 512 MB RAM | 1 GB RAM | ... | DiskPer app | 250 MB disk | 2 GB disk | 10 GB disk | ... | Network speedPer app | 10 Mbit/s | 100 Mbit/s | 200 Mbit/s | ... | Monthly transferShared across your account | 100 GB/mo | 500 GB/mo | 1 TB/mo |
- sources:
  - [1] https://deplexo.com/plans
  - [2] https://deplexo.com/
