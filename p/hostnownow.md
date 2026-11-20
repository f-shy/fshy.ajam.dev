# HostNowNow Flux

> hostnownow.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/hostnownow/ | JSON https://fshy.ajam.dev/api/v1/entity/hostnownow.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## HostNowNow Flux

- `compute/hostnownow-flux` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone unknown, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://hostnownow.com/products/flux
- free tier: 'Yes. Flux Free is free forever with hard caps and never bills overage, so you can build and learn without a card', with '10 projects and 100 GB bandwidth' on the free tier, 'Automatic TLS, DDoS protection, and a managed WAF on every project', and an OpenAI-compatible inference endpoint per project billed in naira from Flux credits. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-free-tier
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 'Free tier with 10 projects and 100 GB bandwidth', 'Flux Free is free forever with hard caps and never bills overage, so you can build and learn without a card', 'Every project gets an OpenAI-compatible endpoint at ai.hnnflux.app', quoted | metered: no | source: [1]
- identity: email | detail: no card: 'Flux Free is free forever with hard caps and never bills overage, so you can build and learn without a card', so no payment method is taken and no hold exists. The signup form's own fields are not described in any evidence row, so whether an email, phone number or ID document is required is unknown; kind kept as email without an evidence row stating it.
- interface: rest
- limits:
  - volume-quota (binding): 100 GB of bandwidth a month across 10 projects is the whole allowance and the platform does not bill overage, so the service stops rather than charging, which makes an unexpected traffic spike a hard stop instead of an invoice. [1]
- limits note: 100 GB of bandwidth a month across 10 projects is the whole allowance and the platform does not bill overage, so the service stops rather than charging, which makes an unexpected traffic spike a hard stop instead of an invoice.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A no-card platform in Lagos with 10 projects and 100 GB is a place to land an API service whose users are in West Africa, which is the one thing a European or American free tier cannot give: a short path to the audience, with the inference endpoint on the same host removing a second vendor from the chain.
- reliability: no reliability event recorded
- notes: Africa's answer to the free-PaaS tier, and the first one on 2026-10-22 that is free rather than a trial: a07-regional already records GoCloud (USD 300 credits, Lagos) and Savannaa (750 hours of t2.micro for 12 months) as trials, and this is the perpetual complement to both. Three more Nigerian and South African candidates were read and are thinner: Zanode (Cape Town) offers a card-free trial with 3 projects, one managed PostgreSQL and 10 GB of bandwidth, HostNowNow's sibling products bundle a free tier with the paid ones, and Ping Africa bills in KES from 500 a month with no free lane. Not established: the per-project memory and CPU cap on Flux Free, which the product page does not state.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: perpetual-free-tier
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'Free tier with 10 projects and 100 GB bandwidth', 'Flux Free is free forever with hard caps and never bills overage, so you can build and learn without a card', 'Every project gets an OpenAI-compatible endpoint at ai.hnnflux.app', quoted
  - [2] 2026-10-22: a second Nigerian platform with the same shape: 'OneBit Deploy has a 0/month free tier. No credit card. No FX.', Node.js and static sites, 'Free apps sleep after 15 minutes without traffic', reported
- sources:
  - [1] https://hostnownow.com/products/flux
  - [2] https://docs.onebit.ng/blog/free-hosting-nigerian-students
