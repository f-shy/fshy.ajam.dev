# Suga

> suga.app | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/suga/ | JSON https://fshy.ajam.dev/api/v1/entity/suga.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Suga

- `compute/suga` | qualifies-with-caveat | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-04T02:23:58.526Z (live) | stale on 2026-12-05
- url https://suga.app/pricing
- free tier: Free plan at USD 0 with no credit card: 1 project, 1 environment, 0.1 vCPU, 256 MiB of RAM and 1 GB of storage, with zero-downtime deploys, HTTPS and a global CDN and 1 day of log retention. Hosting beyond the plan is metered per second. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: perpetual-allowance
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: Metered on every plan at USD 0.00012 per MB of egress; no free egress allowance is stated on the pricing page | metered: yes | price per TB: USD 120 per TB | source: [1]
- identity: email | detail: no card: the pricing page's Free plan at USD 0 lists 'no credit card required'. No hold exists because no payment method is taken on the free plan. The signup form is not quoted, so the email requirement is inferred rather than read, and debit and prepaid acceptance are not stated.
- interface: rest
- limits:
  - volume-quota (binding): 0.1 vCPU and 256 MiB is a single small service; there is no second project and no second environment on the free plan, so the limit is shape and count rather than a meter. [1]
- limits note: 0.1 vCPU and 256 MiB is a single small service; there is no second project and no second environment on the free plan, so the limit is shape and count rather than a meter.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: 0.1 vCPU and 256 MiB is smaller than a Streamlit app but it is a real always-on container with a CDN, so it fits an API or a webhook receiver that must answer when nothing else is awake; the 1 GB disk is the ceiling for anything stateful.
- reliability: no reliability event recorded
- notes: This is the record that stops the next reader chasing Nitric: nitric.io/pricing returns 404 and the company now sells Suga. Not established, the page gives one figure. The docs say Suga is under active development with frequent changes, so the shape may move.
- extras:
  - facets.class: perpetual-allowance
  - facets.free_tier_kind: perpetual-allowance
  - facets.shape.vcpu: 0.1
  - facets.shape.ram_gib: 0.25
- evidence:
  - [1] 2026-10-22: Free (USD 0): 1 project, 1 environment, 0.1 vCPU, 256 MiB RAM, 1 GB storage, zero-downtime deploys, HTTPS and global CDN, 1 day log retention, no credit card required, quoted
  - [2] 2026-10-22: Nitric Inc. now presents Suga as its hosting product for agents, apps and platforms, with signup at dashboard.suga.app and docs at docs.suga.app, quoted
  - [1] 2026-10-22: hosting is metered per second on top of the plan so an idle service costs close to nothing; Pro is USD 20/seat/month with USD 20 of hosting credits, quoted
  - [1] 2026-11-03: egress is metered at $0.00012 per MB | capture: sha256:2846069247fe59f8d1ad7b406e78a7b858cef088daddee6cbccac7173fad945c | quote: | Network | $0.00012 | per MB egress |
- sources:
  - [1] https://suga.app/pricing
  - [2] https://nitric.io/
