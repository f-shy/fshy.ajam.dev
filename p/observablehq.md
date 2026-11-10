# Observable

> observablehq.com | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/observablehq/ | JSON https://fshy.ajam.dev/api/v1/entity/observablehq.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Observable (Free)

- `compute/observable-free` | fails-quota | evidence documented | binding volume-quota | category notebook runtime | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://observablehq.com/pricing
- free tier: free notebooks with 'Few tokens / day' of agent and 1 GB a month of file attachments; the Compute row is blank on Free and 50 minutes a month on Pro at USD 22 a month | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: Compute is a paid-plan row. The Free cell is empty, so the free compute allowance is zero.
- per-object cap: not applicable: the unit is a session, not an object
- retention: not stated | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a free account; no card stated for Free
- interface: rest, graphql
- limits:
  - volume-quota (binding): 0 minutes of compute on Free; 50 minutes a month on Pro [1]
- binding note: the free allowance is zero minutes, so the first job fails immediately
- interface detail: JavaScript notebooks in the browser with database connectors
- tooling: the Observable notebook; no shell
- composes with: a JavaScript notebook and dashboard tool with no free compute
- reliability: no reliability event recorded
- notes: Observable offers a Free tier for notebooks without hosted compute allowances; compute is client-side or connected to external database services.
- evidence note: the blank Compute cell and the Pro figure are read from the plan table. A blank cell is an absence, so the zero is an inference from the row structure.
- extras:
  - billing_model: free
  - term: none
  - price_arithmetic: USD 0.00 on Free for zero compute; 50 minutes a month costs USD 22 a month on Pro
  - free_tier_kind: free-forever-with-feature-gate
  - unattended: no
  - unattended_mechanism: none: no compute allowance on Free
  - network_out.allow_outbound: no
  - network_out.allow_inbound_listen: no
  - network_out.ports: unstated
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: not published
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: quoted: '| Compute | | | 50 min. / mo. | | 50 min. / editor / mo. | Custom |' - the Free column is empty, Pro is 50 minutes
  - [1] 2026-10-24: quoted: '| File attachments | | 1 GB / mo. | 1 GB / mo. |' on the Free column
  - [1] 2026-10-24: quoted: 'Pro$22per monthor $25 billed monthly'
- sources:
  - [1] https://observablehq.com/pricing

## Observable (Storage)

- `storage/observable` | fails-quota | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://observablehq.com
- free tier: Free plan: 'File attachments 1 GB / mo.' | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not metered, but 1 GB/mo of attachments caps the whole play. | metered: yes | free allowance: 1 GB per month
- identity: email
- interface: rest
- limits note: 1 GB/mo attachments on Free and Pro alike; embed watermark on Free.
- interface detail: rest
- tooling: Observable notebooks/FileAttachment API; attachments are content-addressed and fetchable from notebook pages.
- composes with: 1 GB/mo per account, no rollover. Not viable.
- reliability: Attachments persist (unlike a notebook disk) but the monthly 1 GB ceiling makes this a rounding error.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Free plan: 'File attachments 1 GB / mo.'
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: comparison table: 'File attachments | 1 GB / mo.' on both Free and Pro (read via firecrawl after a 429 from the default provider)
- sources:
  - [1] https://observablehq.com/pricing
