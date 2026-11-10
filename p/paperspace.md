# Paperspace Gradient

> paperspace.com | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/paperspace/ | JSON https://fshy.ajam.dev/api/v1/entity/paperspace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Paperspace Gradient

- `compute/paperspace-gradient` | qualifies-with-caveat | evidence documented | binding volume-quota | category GPU cloud | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://www.paperspace.com/pricing
- free tier: USD 0 with 'FREE GPU', a 12-hour auto-shutdown limit and 5 GB of storage; the free machine list names 'Free GPU (M4000)' and 'Free CPU (C4)' as available on the Free plan | unit: hours | metered on: wall-clock | read on: 2026-10-24 | source: [1] | note: No weekly or monthly GPU-hour cap is published on either page. The 12-hour auto-shutdown is the only time number.
- per-object cap: not applicable: the unit is a session, not an object
- retention: 5 GB of storage on the Free plan; storage overage is billed at USD 0.29/GB | source: [2]
- egress: 'We do not charge for ingress or egress bandwidth for Paperspace Machines.' | metered: no | free allowance: unmetered | source: [1]
- identity: email | detail: a Paperspace account; the pricing page states no card for the Free plan, and the free-tier note says paid instances are billed per hour so a card is needed only for those
- interface: rest
- limits:
  - volume-quota (binding): 12-hour auto-shutdown per session; no published hourly or weekly GPU cap [2]
  - per-object-cap: 5 GB of storage on the Free plan [2]
- limits note: the 12-hour auto-shutdown binds first, and behind it a shared capacity pool: a free notebook can sit pending while paid instances start immediately
- binding note: the 12-hour auto-shutdown is the only enforced clock published; the absence of an hour cap is a gap in the documentation, not a promise
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: A single M4000 with 5 GB of storage is a scratch lane, not a training lane; it composes with Kaggle by giving an always-on notebook that does not consume Kaggle's weekly quota.
- reliability: a powered-off machine still bills its storage and public IP until it is destroyed
- notes: Two first-party pages conflict: the Paperspace plans page gives the Free plan 'Public projects' only, while DigitalOcean's pricing page says free machines 'can only be used for Notebooks in private workspaces'. Both were read. Which is enforced is unknown, and it decides whether free GPU work is visible to everyone.
- evidence note: the plan lines and the free-machine table are quoted from the vendor and DigitalOcean pages today. The GPU class comes from DigitalOcean's table, not Paperspace's, and the two pages disagree about whether Free projects can be private.
- extras:
  - facets.class: perpetual-free-instance
  - facets.free_tier_kind: allowance
  - facets.shape.gpu_class: M4000
  - facets.shape.gpu_count: 1
  - shape.disk_gib: 5
  - shape.gpu_class: M4000
  - shape.gpu_count: 1
  - shape.note: the GPU class is named; vCPU and RAM for the free M4000 notebook are not published
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00 on the Free plan; the same M4000 card is USD 0.45/hr on a paid instance
  - free_tier_kind: free-forever-with-quota
  - unattended: no
  - unattended_mechanism: unverified: the 12-hour auto-shutdown implies a running notebook, and no scheduler is described
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: no
  - network_out.ports: unstated
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.wall_clock_min: 720
  - session_cap.restart_required: yes
  - session_cap.note: 12-hour auto-shutdown on the Free plan
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [2] 2026-10-22: quoted: Free plan USD 0 with 'FREE GPU', 'Auto-shutdown (12 hour limit)', '5GB storage', 'Basic instances', 'Public projects'
  - [1] 2026-10-22: quoted free machine table: 'Free GPU (M4000)' available on the Free, Pro and Growth plans; free machines provide limited CPU and GPU resources for development and testing
  - [2] 2026-10-22: probe 200, 127225 bytes, sha256 f55fdd9f941c, 2026-10-22T14:24:06Z, no false-200 signature
  - [3] 2026-10-22: the legacy Gradient instance-type page returned no instance text; the retired-generation docs describe a 'limited pool of free instances' where a notebook may be Pending while it waits for a machine
  - [2] 2026-10-24: the Free plan column is a bullet list reading 'FREE GPU', '$0', 'Public projects', 'Auto-shutdown (12 hour limit)', '5GB storage', 'Basic instances'
  - [1] 2026-10-24: quoted: '| Free GPU (M4000) | Free, Pro, Growth |'
  - [1] 2026-10-24: quoted: 'Free machines provide limited CPU and GPU resources for development and testing and can only be used for Notebooks in private workspaces.'
  - [1] 2026-10-24: quoted: 'We do not charge for ingress or egress bandwidth for Paperspace Machines.'
  - [1] 2026-10-24: quoted: '| GPU+ (M4000) | $0.45/hr | Free, Pro, Growth |' — the paid rate for the same card
- sources:
  - [1] https://docs.digitalocean.com/products/paperspace/pricing/
  - [2] https://www.paperspace.com/pricing
  - [3] https://docs.paperspace.com/gradient/instances/instance-types

## Paperspace Gradient (DigitalOcean)

- `storage/paperspace-gradient` | fails-quota | evidence reported | binding none | category iaas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.paperspace.com/gradient
- free tier: Free tier: '5GB storage', basic instances, free GPU, public projects. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered separately on the free tier. | metered: yes
- identity: card | detail: inferred from the category 'iaas'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: rest, cli
- limits note: 'Auto-shutdown (12 hour limit)'; free machines are C1-class; notebooks must be public on the free tier; 1 running notebook.
- interface detail: rest
- tooling: Gradient notebooks/CLI; persistent storage is a mounted `/storage` volume shared across notebooks on the account.
- composes with: 5 GB x N accounts. Too small to matter; the next tiers (15 GB, 50 GB) are paid or trial.
- reliability: Stable and long-running, but 5 GB is 1% of the 500 GB minimum and there is no free path upward.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free tier: '5GB storage', basic instances, free GPU, public projects.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Free tier: 'Auto-shutdown (12 hour limit)', '5GB storage', 'Basic instances'
  - [1] 2026-10-21: paid tiers list '15GB storage' and '50GB storage'
- sources:
  - [1] https://www.paperspace.com/pricing
