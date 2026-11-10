# Tembo

> tembo.io | Compute, Databases and KV; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/tembo/ | JSON https://fshy.ajam.dev/api/v1/entity/tembo.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Tembo (Nano: 2 vCPU / 2 GiB)

- `compute/tembo-computer` | paid-only | evidence documented | binding volume-quota | category full VM (dedicated Linux VM per session) | tier Nano: 2 vCPU / 2 GiB
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T01:42:18.426Z (live) | stale on 2026-12-04
- url https://docs.tembo.io/resources/pricing
- price parsed USD 77.82/mo
- free tier: Free trial: 'included usage allowance, up to 10 users, sandbox size up to xl, and priority support'. The size of the allowance and its duration are not stated on the pricing page. | unit: mixed | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: a dollar-denominated allowance, amount unpublished
- per-object cap: not applicable
- retention: unknown: 'Stopped, snapshotted, and otherwise non-running VMs do not accrue compute', and projects can cache reusable environments, but no page read states how long a stopped VM or its cached environment survives | source: [1]
- egress: Not published on the pricing page. Tembo Gateway model traffic and cloud VM compute 'draw from the same balance', but no traffic allowance or per-GB egress rate is stated. | metered: no | source: [1]
- identity: email | detail: Account signup for the free trial; Pro (USD 60) and Max (USD 200) are paid plans. Whether the trial requires a card, what card types are accepted, and whether any authorisation is held are not stated on the pricing page read.
- interface: rest, cli
- limits:
  - volume-quota (binding): Pro USD 60 a month includes a USD 90 usage allowance; Max USD 200 includes USD 400; compute draws at USD 0.0403/vCPU-hour + USD 0.0130/GiB-RAM-hour [1]
  - retention-clamped: the Pro plan caps sandbox size at 'medium' (4 vCPU / 8 GiB); only Max and the trial reach 'xl' (16 vCPU / 32 GiB) [1]
- limits note: 'Included monthly allowance expires at the end of each billing cycle and does not roll over. Prepaid balance does not expire.' Overage billing is optional and capped by a user-set maximum.
- binding note: The dollar allowance is what runs out first: the cheapest always-on shape spends USD 77.82 of it a month, inside a USD 90 Pro allowance, but a Medium VM at USD 0.2652 an hour uses up USD 90 in about 339 hours.
- interface detail: Agent sessions execute in dedicated ephemeral Linux VMs; the workspace is driven through Tembo's own gateway and model routing rather than a machine you connect to directly.
- tooling: Tembo's own workspace. It is a coding-agent product that happens to run a VM, not a VPS: no SSH contract is published on the pricing page.
- composes with: A full VM at USD 0.1066 an hour for the smallest shape is USD 77.82 a month, so it is not an answer to the cheap-machine questions. It matters here as the case where a full VM is priced by the running second and the binding cost is the USD 60 a month plan that must sit underneath it.
- reliability: no reliability event observed. Each session runs in a dedicated ephemeral VM, so state that is not in a cached project environment does not outlive the session.
- notes: Arithmetic: Nano at USD 0.1066 an hour × 730 = USD 77.818 a month, against a USD 90 Pro allowance, so the allowance covers 844 hours. At 10 h a day (300 h) it is USD 31.98. Verified against the component rates: 2 × 0.0403 + 2 × 0.0130 = USD 0.1066 an hour, which matches the size table exactly. Larger shapes: Micro (2/4) USD 0.1326/hr, Medium (4/8) USD 0.2652, Large (8/16) USD 0.5304, XL (16/32) USD 1.0608, XXL (16/64) USD 1.4768, Ultra (32/128) USD 2.9536. Region, egress and stopped-VM retention are unverified. sandboxprices.com could not price this row at all, so the site contributes discovery only.
- evidence note: Rates, the size table and the plan floors are quoted from the vendor's own pricing documentation read. The free-trial amount is explicitly unpublished, so no value is recorded for it. What would raise it: a trial run that reads the granted allowance, and the egress terms.
- extras:
  - shape.vcpu: 2
  - shape.ram_gib: 2
  - billing_model: hourly
  - term: monthly plan plus per-second metering
  - m10h_usd: 31.98
  - m24h_usd: 77.82
  - price_arithmetic: 0.1066/hr × 730 h = USD 77.818; × 300 h = USD 31.98. Component check: 2 vCPU × 0.0403 + 2 GiB × 0.0130 = 0.1066/hr.
  - free_tier_kind: trial
  - network_out.allow_outbound: yes
  - network_out.ports: not published
  - session_cap.restart_required: no
  - session_cap.note: no lifetime cap published; non-running VMs accrue no compute
  - aggregator_note: sandboxprices.com lists Tembo Computer as a Full VM row with no modelled total ('workload eligibility incomplete'); the vendor rate card prices it at USD 77.82 a month for the smallest shape.
- evidence:
  - [1] 2026-10-24: quoted: 'VM compute ... at $0.0403/vCPU-hour + $0.0130/GiB-RAM-hour' with 'Nano | 2 | 2 GiB | $0.1066' per hour
  - [1] 2026-10-24: metering: 'Tembo measures each running VM in seconds and bills its actual running time at the per-second equivalent of the hourly rate. Stopped, snapshotted, and otherwise non-running VMs do not accrue compute.'
  - [1] 2026-10-24: free trial: 'Free trial: included usage allowance, up to 10 users, sandbox size up to xl, and priority support' - no amount given
  - [1] 2026-11-03: the docs page lists Pro at USD 60 a month with a USD 90 monthly usage allowance | capture: sha256:d9142cae072dcf94e5a760bdca25365a22bc6d793d723888efd447990a3addc5 | quote: * Pro (\$60/month): \$90 monthly usage allowance, up to 5 users, sandbox size up to `medium`, with overage billing
  - [1] 2026-11-03: the docs page lists Max at USD 200 a month with a USD 400 monthly usage allowance | capture: sha256:d9142cae072dcf94e5a760bdca25365a22bc6d793d723888efd447990a3addc5 | quote: * Max (\$200/month): \$400 monthly usage allowance, up to 10 users, sandbox size up to `xl`, with overage billing
  - [1] 2026-11-03: the docs page gives the free trial an included usage allowance with no amount | capture: sha256:d9142cae072dcf94e5a760bdca25365a22bc6d793d723888efd447990a3addc5 | quote: * Free trial: included usage allowance, up to 10 users, sandbox size up to `xl`, and priority support
  - [1] 2026-11-03: the trial ends by time or by allowance; neither the amount nor the length is stated | capture: sha256:d9142cae072dcf94e5a760bdca25365a22bc6d793d723888efd447990a3addc5 | quote: Free trial: sessions stop when the trial ends or its allowance runs out.
  - [1] 2026-11-03: the Pro plan costs USD 60 a month and carries a USD 90 usage allowance, so the allowance in the arithmetic is USD 90 | capture: sha256:d9142cae072dcf94e5a760bdca25365a22bc6d793d723888efd447990a3addc5 | quote: * Pro (\$60/month): \$90 monthly usage allowance, up to 5 users, sandbox size up to `medium`, with overage billing
- sources:
  - [1] https://docs.tembo.io/resources/pricing

## Tembo (Databases and KV)

- `databases-kv/tembo` | dead | evidence documented | binding request-rate | category Postgres platform with an agent runtime
- needs card no, phone no, ID no, institution no | verified 2026-11-03T01:29:53.963Z (live) | stale on 2026-12-04
- url https://www.tembo.io/pricing/
- free tier: No stated free allowance at https://www.tembo.io/pricing/: a Free trial at $0 ("Get started with a free trial.") with no amount or length given, then Pro at $60/month or Max at $200/month. | unit: none | metered on: none | read on: 2026-10-30 | source: [1]
- per-object cap: no cap published; the allowance is denominated in dollars
- retention: the trial lasts until the allowance is spent; paid plans are Pro at USD 60 a month and Max at USD 200 | source: [1]
- egress: drawn from the same dollar allowance as compute and model usage | metered: yes | source: [1]
- identity: email | detail: email signup for the trial
- interface: rest, cli
- limits:
  - request-rate (binding): a free trial with no stated allowance; Pro at USD 60 a month includes USD 90 of usage a month and Max at USD 200 a month includes USD 400 [1]
- interface detail: the Postgres wire protocol for the database; an agent runtime over the same workspace
- tooling: psql, the Tembo CLI
- composes with: no path as a database; the product has moved to an agent workspace with cloud VMs
- reliability: the product was replaced by an agent workspace, so no reliability event at a Postgres host applies to it
- notes: The product is now an agent workspace rather than a Postgres host.
- evidence note: the pricing page was read and carries no perpetual free tier.
- extras:
  - death.on: 2026-10-30
  - death.cause: dead-service
- evidence:
  - [1] 2026-10-30: the pricing page lists a Free trial at $0 with no amount or length of allowance | capture: sha256:32854ab30df95eedecc4dcfc32be30c0da0b942c1c47f24eea81ef737dce31d6 | quote: Free trial Get started with a free trial. $0
  - [1] 2026-10-30: the pricing page states Pro includes $90 and Max $400 of usage a month, on plan prices of $60 and $200 | capture: sha256:32854ab30df95eedecc4dcfc32be30c0da0b942c1c47f24eea81ef737dce31d6 | quote: Pro includes $90 per month and Max includes $400 per month.
  - [1] 2026-10-30: the pricing FAQ names the trial without an allowance amount | capture: sha256:79fda55b61d449e4b93f2428126c7f44a37e3c9da40722683ba4940dc6128293 | quote: The free trial lets you try Tembo before choosing a paid plan.
  - [2] 2026-10-30: the docs give the trial an included allowance without an amount | capture: sha256:c1472552948ea4a848cfa15915d8666c71dbced5b75184c749ebeeaeab2f6ee6 | quote: Free trial: included usage allowance, up to 10 users, sandbox size up to `xl`, and priority support
  - [3] 2026-10-30: Tembo Cloud, the managed Postgres service, was sunset; the same page's timeline disabled instance creation on May 5, 2025 and set the paid instance migration deadline at June 27, 2025 | capture: sha256:04740fa1d6b0ce8ba8de02830aca55e07df7305ccdf8c37c65205213336b7595 | quote: We're now in the process of sunsetting Tembo Cloud, as we take a bold step toward the future.
  - [3] 2026-10-30: paid Tembo Cloud Postgres instances had to migrate off by June 27, 2025 | capture: sha256:04740fa1d6b0ce8ba8de02830aca55e07df7305ccdf8c37c65205213336b7595 | quote: | June 27, 2025 | Paid instance migration deadline |
  - [4] 2026-11-03: the pricing page FAQ states the same USD 90 and USD 400 monthly allowances as the docs page | capture: sha256:6698539f3a4d814ab1c9a31400f94dfe1f758a6bbe1c181f92abd844cf1bc4e1 | quote: Pro includes $90 per month and Max includes $400 per month.
  - [2] 2026-11-03: the docs page agrees: Pro at USD 60 a month includes a USD 90 allowance | capture: sha256:d9142cae072dcf94e5a760bdca25365a22bc6d793d723888efd447990a3addc5 | quote: * Pro (\$60/month): \$90 monthly usage allowance, up to 5 users, sandbox size up to `medium`, with overage billing
- sources:
  - [1] https://www.tembo.io/pricing/
  - [2] https://docs.tembo.io/resources/pricing
  - [3] https://tembo-io.notion.site/Tembo-Cloud-Migration-Guide-1de7c9367d6a80349570e7469ba7f17b
  - [4] https://www.tembo.io/pricing
