# Replit

> replit.com | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/replit/ | JSON https://fshy.ajam.dev/api/v1/entity/replit.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Replit

- `compute/replit` | trial-only | evidence documented | binding volume-quota | category dev environment | tier Starter (free)
- needs card no, phone no, ID no, institution no | verified 2026-11-04T05:24:14.687Z (live) | stale on 2026-12-05
- url https://docs.replit.com/billing/plans
- free tier: Starter is free: daily Agent credits up to a monthly cap, monthly cloud-usage credits, one published app whose link goes down after 30 days, and Lite build only; no compute hours, RAM or session length are published | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: The free plan is denominated in credits and app count, never in machine time.
- per-object cap: not applicable: the unit is a session, not an object
- retention: the one free published app's link 'will automatically go down after 30 days' | days: 30 | source: [1]
- egress: Outbound data transfer from published deployments is priced at USD 0.05 per GiB from 2026-08-01 (USD 0.10 before); no free allowance is stated on the page | metered: yes | price per TB: USD 0.05 per GiB | source: [2]
- identity: email | detail: a Replit account; the Starter plan states no card
- interface: ssh
- limits:
  - volume-quota (binding): 1 published app, taken down after 30 days [1]
- limits note: compute is metered on paid tiers; the free tier is a preview
- binding note: there is no published compute allowance at all, so the free plan cannot be budgeted for a job
- interface detail: a browser IDE and a hosted app preview on the free Starter plan; SSH with an account-level public key, usable from a local editor, on Core, Pro and other paid plans only
- tooling: the Replit IDE, Nix-based environments, a shell in the browser
- composes with: 30 days of a preview URL, then nothing
- reliability: the free published link is taken down after 30 days, so anything served from it has a dated death
- notes: https://replit.com/pricing returned 403 with a 2026-10-21 snapshot and lists only Core, Pro and Enterprise, so no free price could be read there. The Starter limits come from the docs. GPU class, RAM and hours are unpublished.
- evidence note: The pricing page itself returned 403 with a cached snapshot, so no price was read from it.
- extras:
  - billing_model: free
  - session_cap.restart_required: no
  - session_cap.note: not published
  - network_out.allow_outbound: yes
  - network_out.allow_inbound_listen: yes
  - network_out.ports: a published app gets a public URL
  - network_out.static_ip: no
  - network_out.ipv6: no
  - free_tier_kind: free-forever-with-feature-gate
  - term: none
  - price_arithmetic: USD 0.00 on Starter; Core is USD 20 a month, USD 18 billed annually
  - unattended: no
  - unattended_mechanism: unverified: deployments exist but the free plan gets one app that is removed after 30 days
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-06: 'This published link will automatically go down after 30 days.'
  - [1] 2026-10-22: read live: the free published link expires after 30 days
  - [1] 2026-10-24: quoted: 'One free published app ... This published link will automatically go down after 30 days.'
  - [1] 2026-10-24: quoted: 'Starter plan builders can only use Lite build' and 'Removing the "Made with Replit" badge from your published apps requires Core'
  - [1] 2026-10-24: quoted: 'Get 1 free published app whether you're using Lite build or Design Canvas. This published link will automatically go down after 30 days.'
  - [1] 2026-10-24: quoted, with the link in the original: 'Starter plan builders can only use [Lite build](https://docs.replit.com/features/agent/agent-modes.md). Full build requires Core or Pro.'
  - [1] 2026-10-24: quoted: 'The Starter plan gives you everything you need to start building on Replit. Create apps and publish your first project — all at no cost.'
  - [2] 2026-11-03: Outbound data transfer on deployments is priced per GiB, USD 0.05 from 2026-08-01 | capture: sha256:4af163bf370cd1e8fe0526691a430b28b91e93f8e241724e35f2b57a5142df05 | quote: | Outbound data transfer | Per GiB | \$0.10 | \$0.05 |
  - [3] 2026-11-03: SSH access needs a paid plan; the free Starter plan has the browser IDE only | capture: sha256:235340e7722f55419cc57ef84871a7ec588283ca307a08f62c55e2acb3b7112b | quote: SSH functionality is available for Core, Pro, and all other paid plans.
- sources:
  - [1] https://docs.replit.com/billing/plans
  - [2] https://docs.replit.com/billing/aug-cloud-billing-updates
  - [3] https://docs.replit.com/replit-workspace/ssh

## Replit (App Storage)

- `storage/replit` | fails-egress | evidence reported | binding none | category paas
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://replit.com
- free tier: No free storage allowance. App Storage is metered: $0.015/GiB/mo storage, $0.05/GiB data transfer, $0.0004/1k basic ops. | unit: GiB | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: 'App Storage Data Transfer: $0.05 per GiB'. Plain metered egress, no free allowance. | metered: yes
- identity: card
- interface: s3, rest
- limits note: 7-day minimum billing period per object; Starter plan gets 1 published app whose link 'will automatically go down after 30 days'; per-account storage limits are 'determined by plan' and not published as a number.
- interface detail: rest
- tooling: S3-shaped API on top of GCS (buckets, access policies); usable with standard S3 tooling.
- composes with: None. Metered storage plus metered egress means multiplying accounts multiplies the bill, not the capacity.
- reliability: Backed by Google Cloud Storage with metered rates for storage and egress. No perpetual free storage tier is provided.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: egress
  - dead_end.why: No free storage allowance. App Storage is metered: $0.015/GiB/mo storage, $0.05/GiB data transfer, $0.0004/1k basic ops.
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: price table: '$0.015 per GiB per month', 'Data Transfer $0.05 per GiB'
  - [2] 2026-10-21: 'This published link will automatically go down after 30 days'
  - [3] 2026-10-21: 'Storage per account: determined by plan (hard)'
- sources:
  - [1] https://docs.replit.com/billing/object-storage-billing
  - [2] https://docs.replit.com/billing/plans/starter-plan
  - [3] https://docs.replit.com/legal-and-security-info/usage
