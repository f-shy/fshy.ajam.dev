# Runsite

> runsite.app | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/runsite/ | JSON https://fshy.ajam.dev/api/v1/entity/runsite.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Runsite

- `compute/runsite` | paid-only | evidence documented | binding none | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://runsite.app/
- free tier: The free tier is static sites only: 'Static Sites | Free | CDN: Global, Bandwidth: 100 GB, Builds: ~20s, Sites: Unlimited | 0 EUR/mo', plus object storage '5 GB free'. Web services start at 'Nano | vCPU: 0.1, RAM: 256 MB, Disk: 1 GB, Bandwidth: 100 GB | 3 EUR/mo | 0.0041 EUR/hr' and 'Starter | vCPU: 0.5, RAM: 512 MB, Disk: 5 GB, Bandwidth: 1 TB | 5 EUR/mo | 0.0068 EUR/hr'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: none
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Static Sites | Free | CDN: Global, Bandwidth: 100 GB, Builds: ~20s, Sites: Unlimited | 0 EUR/mo | 0.0000 EUR/hr', quoted from the monthly and hourly table | metered: no | source: [1]
- identity: email
- interface: s3-compatible
- limits note: nothing binds above the scale at the paid floor; the free tier carries static hosting only, so the first wall is EUR 3 for a 0.1 vCPU web service.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: hourly billing at EUR 0.0041 for a 0.1 vCPU service means a six-hour job costs about EUR 0.03, so this is a cheap place to park a short-lived web endpoint beside the free static site.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: free-for.dev says 'European PaaS with automated deployments from GitHub for web services or static sites (1 web 0.1 vCPU/256 MB free), managed PostgreSQL and Valkey (30 days for free), Transactional Email (3,000 emails/month free), S3 compatible storage (5 GB/free)'. The free web service is wrong: the vendor table marks Static Sites as the 0 EUR row and prices the 0.1 vCPU web service at EUR 3 a month, so a reader would build against a free tier that does not exist. The 5 GB of object storage is real. The 30-day free database was not confirmed: the managed PostgreSQL rows on the same table start at EUR 3.
- extras:
  - facets.free_tier_kind: none
  - facets.shape.vcpu: 0.5
  - facets.shape.ram_gib: 0.5
- evidence:
  - [1] 2026-10-22: 'Static Sites | Free | CDN: Global, Bandwidth: 100 GB, Builds: ~20s, Sites: Unlimited | 0 EUR/mo | 0.0000 EUR/hr', quoted from the monthly and hourly table
  - [1] 2026-10-22: 'Web Services | Nano | vCPU: 0.1, RAM: 256 MB, Disk: 1 GB, Bandwidth: 100 GB | 3 EUR/mo | 0.0041 EUR/hr' and 'Starter | vCPU: 0.5, RAM: 512 MB, Disk: 5 GB, Bandwidth: 1 TB | 5 EUR/mo', quoted
  - [1] 2026-10-22: '5 GB free - EUR 0.025/GB' for S3-compatible object storage with 'Zero egress fees', quoted
- sources:
  - [1] https://runsite.app/
