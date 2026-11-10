# Hostim.dev

> hostim.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostim/ | JSON https://fshy.ajam.dev/api/v1/entity/hostim.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Hostim.dev

- `compute/hostim-dev` | trial-only | evidence documented | binding none | category platform host
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:20:49.286Z (live) | stale on 2026-12-05
- url https://hostim.dev/pricing/
- free tier: No perpetual free tier; a 5-day trial without a card, then a flat price per resource. Quoted: 'shared app plans are EUR 2.50 (1 vCPU / 1 GB), EUR 4.50 (2 / 2 GB), EUR 7.50 (3 / 4 GB) and EUR 13.50 (4 vCPU / 8 GB)', billed 'hourly with a 1-hour minimum', and 'every project includes a free Postgres (256 MB), MySQL (256 MB), Redis (128 MB) and a 1 GB volume'. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: No usage-based billing is claimed: 'no per-request, per-build-minute, or bandwidth-overage charges'. | metered: no | source: [1]
- identity: email | detail: no card for the trial: the pricing page states 'New accounts get a 5-day trial with no credit card required'. No hold exists on the trial because no payment method is taken. The signup form is not quoted, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated; a card enters only when a paid plan is bought.
- interface: cli
- limits note: nothing binds above the scale at EUR 2.50 a month for 1 vCPU and 1 GB; the wall is that the resource must be stopped by hand, because billing runs per hour with a one-hour minimum.
- binding note: the same as limits note
- interface detail: Web console and the hostim CLI (usable from CI), documented on the getting-started page; the CLI is a thin client over the public REST API at api.hostim.dev.
- tooling: hostim CLI (open source, installed with a shell script; `hostim agent` prints its manual); the REST API at api.hostim.dev directly.
- composes with: a flat EUR 2.50 for 1 vCPU and 1 GB, billed by the hour with a one-hour minimum, is the cheapest always-on western-European app host found among evaluated providers; a three-hour job costs about EUR 0.01, and the free 256 MB Postgres comes with the project.
- reliability: no reliability event recorded
- notes: Aggregator claim checked: dalisoft/awesome-hosting lists Hostim under lambda as 'sa-1-1 (EUR 2.5/m) - 5-Day trial - no free tier'. The vendor's own page agrees and adds the plan ladder, which the aggregator compresses to one entry. No usage-based billing is claimed: 'no per-request, per-build-minute, or bandwidth-overage charges'.
- extras:
  - facets.class: floor-price
  - facets.free_tier_kind: trial
  - facets.shape.vcpu: 1
  - facets.shape.ram_gib: 1
- evidence:
  - [1] 2026-10-22: 'shared app plans are EUR 2.50 (1 vCPU / 1 GB), EUR 4.50 (2 / 2 GB), EUR 7.50 (3 / 4 GB) and EUR 13.50 (4 vCPU / 8 GB)', quoted
  - [1] 2026-10-22: 'every project includes a free Postgres (256 MB), MySQL (256 MB), Redis (128 MB) and a 1 GB volume', quoted
  - [1] 2026-10-22: 'New accounts get a 5-day trial with no credit card required' and 'billed hourly with a 1-hour minimum, on EU servers in Germany', quoted
  - [2] 2026-11-04: the hostim CLI exists and covers the console steps | capture: sha256:8c39f2b9d444cea4d68f1d9fa8fc304d92b675eca800b830e7477ee916498690 | quote: The `hostim` CLI does everything this guide does, without a browser
  - [1] 2026-11-04: traffic is included in the app price, with no bandwidth overage charge | capture: sha256:018a9b1f09208e44ee1f6d3331bc361656dffdcda3bcb9870e93f68653c1e004 | quote: No. Traffic to your apps is included in the app price, and there are no build-minute, per-request, or per-function charges.
  - [2] 2026-11-04: the CLI is documented as a full alternative to the web console | capture: sha256:8c39f2b9d444cea4d68f1d9fa8fc304d92b675eca800b830e7477ee916498690 | quote: The `hostim` CLI does everything this guide does, without a browser, which is what you want in CI
  - [3] 2026-11-04: the hostim CLI is documented and wraps the REST API | capture: sha256:110c69279b8b4e107155b86bd53864db3830c4180926f46cbc233c3b47a6fe06 | quote: It is a thin client over the public REST API at `https://api.hostim.dev`
- sources:
  - [1] https://hostim.dev/pricing/
  - [2] https://hostim.dev/docs/
  - [3] https://hostim.dev/docs/cli/
