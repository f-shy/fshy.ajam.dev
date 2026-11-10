# CoCalc

> cocalc.ai | Compute, Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/cocalc/ | JSON https://fshy.ajam.dev/api/v1/entity/cocalc.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## CoCalc, Free (trial project)

- `compute/cocalc-free` | fails-quota | evidence documented | binding write-gated | category notebook runtime | tier Free (trial project)
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://cocalc.ai/pricing
- free tier: a free trial project with no expiry, described only as 'just enough resources to explore the platform and do basic work', with no internet access and a small idle timeout | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: No RAM, CPU or hour number is published anywhere reachable today. The zero is the network, not the clock.
- per-object cap: not applicable: the unit is a session, not an object
- retention: trial projects do not expire at the moment; a free project can be stopped at any time | source: [1]
- egress: no outbound internet at all from a free project | metered: yes | free allowance: 0 bytes | source: [2]
- identity: email | detail: an account; the free trial project needs no card
- interface: rest, ssh, cli
- limits:
  - write-gated (binding): no internet access from a free project; a licence is required [2]
  - volume-quota: unpublished and small: 'Your hardware resources are quite limited' [1]
- binding note: no outbound network means no pip, no git clone and no API call, which ends most work before any quota is reached
- interface detail: a browser IDE with a Linux terminal, Jupyter, RStudio and LaTeX
- tooling: the web IDE and its terminal; pip and git clone both fail without network
- composes with: a free LaTeX and R workbench with no internet, which rules out installing anything or fetching data
- reliability: a free project can be stopped at any time and the docs say it happens at least daily, so long computations need checkpointing
- notes: CoCalc moved its pricing to cocalc.ai; cocalc.com/pricing now 404s through automated retrieval. The free tier publishes no number at all, which is why this record has dashes where a shape should be.
- evidence note: the no-internet rule and the idle/session language are quoted from the manual today. RAM and CPU are unverified because neither the pricing page nor the manual publishes a number for the free tier.
- extras:
  - shape.note: unpublished; the manual only says 'quite limited'
  - billing_model: free
  - term: none
  - m10h_usd: 0.0
  - m24h_usd: 0.0
  - price_arithmetic: USD 0.00; the first paid tier is USD 6 a month billed annually
  - free_tier_kind: free-forever-with-feature-gate
  - unattended: no
  - unattended_mechanism: none: no network and a project that can be stopped at least daily
  - network_out.allow_outbound: no
  - network_out.allow_inbound_listen: no
  - network_out.ports: none
  - network_out.static_ip: no
  - network_out.ipv6: no
  - network_out.per_session_bytes: 0
  - session_cap.restart_required: yes
  - session_cap.note: 'Idle timeout is small and overall session duration is limited' - no number given
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [2] 2026-10-24: quoted: 'Processes running inside a free project are not allowed to directly access the internet.'
  - [1] 2026-10-24: quoted, with a link and code spans in the original: 'You do not have direct Internet access. You can upload files to CoCalc from your computer, but not from other sites. You cannot `git clone` repositories from GitHub and you cannot [install packages](https://doc.cocalc.com/howto/install-python-lib.html) even as a regular user via `pip`.'
  - [1] 2026-10-24: quoted: 'Idle timeout is small and overall session duration is limited.'
  - [1] 2026-10-24: quoted: 'Yes, you can - trial projects do not expire at the moment.'
  - [3] 2026-10-24: quoted: 'Start using CoCalc with just enough resources to explore the platform and do basic work.' - the Free tier carries no number
  - [3] 2026-10-24: quoted: 'Network access' appears as a benefit of the Basic and Standard tiers, not of Free
- sources:
  - [1] https://doc.cocalc.com/trial.html
  - [2] https://doc.cocalc.com/upgrades.html
  - [3] https://cocalc.ai/pricing

## cocalc (Storage)

- `storage/cocalc` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://cocalc.ai/pricing
- free tier: None reachable: Pricing page has been reduced to a membership/licensing blurb with no comparable tier table and no published storage figure. The numbers that used to make CoCalc interesting (free hosted pr. | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: unknown
- interface detail: not documented
- tooling: the same as interface detail
- composes with: not recorded
- reliability: part of the free tier
- notes: part of the free tier
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Pricing page has been reduced to a membership/licensing blurb with no comparable tier table and no published storage figure — the numbers that used to make CoCalc interesting (free hosted…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: Pricing page has been reduced to a membership/licensing blurb with no comparable tier table and no published storage figure — the numbers that used to make CoCalc interesting free hosted pr
- sources:
  - [1] https://cocalc.ai/pricing
