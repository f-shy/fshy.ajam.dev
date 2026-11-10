# SnapDeploy

> snapdeploy.dev | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/snapdeploy/ | JSON https://fshy.ajam.dev/api/v1/entity/snapdeploy.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SnapDeploy

- `compute/snapdeploy` | qualifies-with-caveat | evidence documented | binding retention-clamped | category container and VM sandbox
- needs card no, phone no, ID no, institution no | verified 2026-11-04T06:29:28.859Z (live) | stale on 2026-12-05
- url https://snapdeploy.dev/pricing
- free tier: One Small container per app, up to 4 apps, no credit card: 512 MB RAM, 0.25 vCPU, 10 deploys a day (at most 5 in any 12 hours), 100 running hours a month across the account, sleeps after 15 minutes without visitors. Quoted from the pricing page. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-free
- per-object cap: not applicable | source: [1]
- retention: 100 running hours a month across the whole account, not per container, so four containers average about 25 hours each and the box sleeps after 15 idle minutes and takes about a minute to wake, which breaks any request that must answer cold. | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: no card and no payment method: the pricing page lists the free tier with 'no credit card', so no hold exists. The evidence does not say which identifier the account is created with, so whether an email alone suffices is not stated; debit and prepaid acceptance are not stated
- interface: unknown
- limits:
  - retention-clamped (binding): 100 running hours a month across the whole account, not per container, so four containers average about 25 hours each and the box sleeps after 15 idle minutes and takes about a minute to wake, which breaks any request that must answer cold. [1]
- limits note: 100 running hours a month across the whole account, not per container, so four containers average about 25 hours each and the box sleeps after 15 idle minutes and takes about a minute to wake, which breaks any request that must answer cold.
- binding note: the same as limits note
- interface detail: web dashboard, GitHub push-to-deploy, an MCP connector (npx @snapdeploy/mcp), and an HTTP API reference at https://snapdeploy.dev/api for the /api/mobile/** endpoints, authenticated with a scoped personal access token or a legacy API key sent as X-API-Key; the docs/api path answers HTTP 404
- tooling: not stated
- composes with: 100 hours is enough for a daily batch job that runs a few minutes, and the 2 GB Docker image limit lets a real scientific Python image ship; it does not compose into anything always-on.
- reliability: no reliability event recorded
- notes: Found via awesome-hosting Containers section, which lists the free tier as 100 h/month and the paid floor as USD 12 a month. The docs/free-tier page was not read separately; the pricing page already states the cap.
- extras:
  - facets.class: perpetual-free-allowance
  - facets.free_tier_kind: perpetual-free
  - facets.shape.vcpu: 0.25
  - facets.shape.ram_gib: 0.5
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: free tier: one Small container per app, up to 4 apps, 512 MB RAM and 0.25 vCPU, 10 deploys a day, 100 running hours a month across the account, sleeps after 15 minutes, no credit card, quoted
  - [1] 2026-10-22: reference to the free-tier page at https://snapdeploy.dev/docs/free-tier as the authority for free-tier rules
  - [2] 2026-11-03: an MCP connector exists for deploying and managing containers | capture: sha256:406e85dbe948851eb8e0e090732b66b5592fa080cae094c258f0ac6f8b3bada2 | quote: SnapDeploy's official MCP connector lets any Model-Context-Protocol client
  - [3] 2026-11-03: a web dashboard exists | capture: sha256:23e218ee8e127c172a54c241df90e51bfa58cb50a027981b173ba1b6096c38fb | quote: Custom domain, monitoring, logs, and scaling — all from one dashboard.
  - [4] 2026-11-04: an API reference page exists for the /api/mobile/** endpoints, authenticated by a scoped token or legacy API key | capture: sha256:4f9a94b2f8573c505309709535d0bc6387fe6a184ec2cc24f79aff4082816bab | quote: A scoped personal access token (`sd_pat_…`, created on the API Keys page with a scope and an expiry) or a legacy API key (`sk_…`, unscoped) authenticates the `/api/mobile/**` endpoints documented on this page.
- sources:
  - [1] https://snapdeploy.dev/pricing
  - [2] https://snapdeploy.dev/docs/mcp
  - [3] https://snapdeploy.dev
  - [4] https://snapdeploy.dev/api
