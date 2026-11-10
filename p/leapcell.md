# Leapcell

> leapcell.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/leapcell/ | JSON https://fshy.ajam.dev/api/v1/entity/leapcell.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Leapcell

- `compute/leapcell` | qualifies-with-caveat | evidence documented | binding retention-clamped | category serverless runtime | tier Hobby
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:55:00.000Z (live) | stale on 2026-11-24
- url https://leapcell.io/pricing
- free tier: Hobby at USD 0 per seat a month: 20 projects, up to 3 vCPUs and 4 GB RAM per project, 1 free PostgreSQL database, custom domains with SSL, a global CDN; 'Persistent Servers' appear only on the paid Plus plan, so the free tier is serverless. | unit: none | metered on: unstated | read on: 2026-10-24 | source: [1]
- per-object cap: up to 3 vCPUs and 4 GB RAM per project on Hobby
- retention: not stated on the pricing page; the free tier has no persistent server
- egress: not stated on the pricing page; traffic is served through the vendor's CDN | metered: no | free allowance: unstated | source: [1]
- identity: email | detail: an account; the pricing page states no card for the Hobby plan
- interface: rest
- limits:
  - per-object-cap: 3 vCPU and 4 GB RAM per project, 20 projects [1]
  - retention-clamped (binding): no persistent servers on the free tier: the Hobby plan is serverless and scales to zero [1]
- limits note: 3 GB-hours of compute a month at 3 vCPU per project is roughly one hour of the full-size worker per month, so a model-inference endpoint on the advertised shape exhausts the allowance almost immediately; requests past the limit return 429 and nothing is charged.
- binding note: 'Persistent Servers' is a paid-tier line item, so the free tier cannot hold a process between requests.
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: a 3 vCPU / 4 GB serverless project with a free Postgres is a complete model-serving stack with no card, and it composes with a Kaggle or Colab notebook that trains the weights; what breaks is the 3 GB-hour monthly compute pool, which is about one full-size inference hour.
- reliability: no reliability event recorded
- notes: The pricing page read still does not print those numbers, so the quota remains unverified; what is new is the tier comparison, which places persistent servers on Plus and therefore shows the free tier scales to zero.
- evidence note: the plan contents and the absence of persistent servers on Hobby were read on the pricing page; the invocation and GB-hour quota is still not printed there
- extras:
  - facets.class: perpetual-free-allowance
  - facets.free_tier_kind: perpetual-free
  - facets.shape.vcpu: 3
  - facets.shape.ram_gib: 4
  - facets.shape.gpu_count: 0
  - shape.vcpu: 3
  - shape.ram_gib: 4
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0 for the Hobby plan; metered usage beyond it is not published
  - free_tier_kind: free-plan
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: serverless HTTP through the CDN
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: scales to zero; the idle interval is not published
- evidence:
  - [1] 2026-10-22: Hobby: 20 projects, up to 3 vCPUs per project (3 vCPUs, 4 GB RAM), 1 free PostgreSQL database, custom domains and SSL, quoted
  - [2] 2026-10-21: free tier: 100,000 invocations a month, 3 GB-hours serverless compute, 2 GB networking, 60 build minutes, 10-minute deployment cap, 7-day log retention; a fair-use policy against multiple accounts; last checked 2026-10-21
  - [3] 2026-10-22: Hobby requests past a limit get a 429 error and nothing is charged; 3 vCPU / 4 GB per project
  - [1] 2026-10-24: quoted: 'Hobby ... 20 Projects (Services) ... Up to 3 vCPUs per project (3 vCPUs, 4GB RAM) ... 1 Free PostgreSQL database'
  - [1] 2026-10-24: quoted: 'All the benefits of Hobby, plus: Persistent Servers' on the Plus plan, which places persistent servers outside the free tier
- sources:
  - [1] https://leapcell.io/pricing
  - [2] https://freetier.wiki/services/leapcell/
  - [3] https://whichdevtool.com/tools/leapcell/
