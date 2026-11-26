# harvis.dev

> harvis.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/harvis/ | JSON https://fshy.ajam.dev/api/v1/entity/harvis.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## harvis.dev

- `compute/harvis-dev` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://harvis.dev/about
- free tier: The vendor's about page carries a reduction with a date, quoted: 'Each site can be up to 50 MB in total (until 2027 Jan 1st, after that the limit will be reduced), spread across up to 500 files.' The pricing page also states that crossing any one of four ceilings moves the whole account to the next paid step, quoted: 'Your account lands on the cheapest step that covers every one of them: cross a single ceiling and it moves up.' | unit: requests | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-monthly
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'cross a single ceiling and it moves up ... a quiet month drops you back down on its own'; free step is 1 GB storage, 100k requests a month, 50 deploys, 0 custom domains; bandwidth, SSL, CPU time and seats are explicitly not billed | metered: no | source: [2]
- identity: anonymous
- interface: rest
- limits:
  - volume-quota (binding): A single month above 100,000 requests or 1 GB-month moves the account to the USD 5 step automatically, so the failure is a bill that arrives without a purchase decision, and the per-site 50 MB cap is scheduled to shrink on 2027-01-01. [1]
- limits note: A single month above 100,000 requests or 1 GB-month moves the account to the USD 5 step automatically, so the failure is a bill that arrives without a purchase decision, and the per-site 50 MB cap is scheduled to shrink on 2027-01-01.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A free static host with unlimited bandwidth and no card composes with a free CI runner for the build, which is the shape of a site that costs nothing to serve and nothing to rebuild.
- reliability: no reliability event recorded
- notes: The free step exists and is metered on stored bytes. Two further facts: the step is applied automatically in both directions, so a traffic spike is a bill and not a suspension, and the per-site size limit has a printed end date of 2027-01-01. The limits can change at any time, and the vendor says so in the plainest language found. Custom domains are not on the free step, which is the one component of a serving chain that still has to be bought.
- extras:
  - facets.class: enforcement
  - facets.free_tier_kind: perpetual-monthly
- evidence:
  - [1] 2026-10-22: quoted: 'Each site can be up to 50 MB in total (until 2027 Jan 1st, after that the limit will be reduced), spread across up to 500 files'
  - [2] 2026-10-22: quoted: 'cross a single ceiling and it moves up ... a quiet month drops you back down on its own'; free step is 1 GB storage, 100k requests a month, 50 deploys, 0 custom domains; bandwidth, SSL, CPU time and seats are explicitly not billed
  - [3] 2026-10-22: 
  - [4] 2026-10-22: the vendor's machine-readable terms: up to 50 MB and 500 files per site, static files only, server-side code is not executed
  - [5] 2026-10-22: 'No account, no config, no build step', a remote MCP server at https://harvis.dev/api/mcp exposing a deploy_site tool that needs 'no account and no API key', quoted
  - [2] 2026-10-22: 'Publishing is free, and when a month outgrows the free limits your account moves onto the nearest paid step - then back down again when the traffic dies off', with meters for stored GB, hits and custom domains, quoted
- sources:
  - [1] https://harvis.dev/about
  - [2] https://harvis.dev/pricing
  - [3] https://harvis.dev/legal/terms-of-service
  - [4] https://harvis.dev/llms.txt
  - [5] https://harvis.dev/
