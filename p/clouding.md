# Clouding.io

> clouding.io | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/clouding/ | JSON https://fshy.ajam.dev/api/v1/entity/clouding.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Clouding.io

- `compute/clouding-io` | trial-only | evidence documented | binding volume-quota | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-11-07T11:15:30.076Z (live) | stale on 2026-12-08
- url https://clouding.io/
- free tier: A 1 GB cloud server at EUR 0.004/hour capped at EUR 3/month: half a vCore, 1 GB RAM, 5 GB NVMe on triple-replicated storage, 4 TB of transfer a month included, hosted in Barcelona. The page also advertises '5 EUR de saldo GRATIS al registrarte', which is EUR 5 of free credit on signup. | unit: GiB | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: 4 TB per month included; beyond that EUR 0.004 per GB or EUR 4 per TB, quoted on the page | metered: yes | free allowance: 4 TB/month | source: [1]
- identity: email | detail: Email and password only. The registration form renders two fields, 'Email' and 'Password', beneath the heading 'Give us a try for free, no strings attached.', then two consent ticks, and its button reads 'Create a free account'. The form carries no phone, card, country or identity-document field, and a balance gift is added at signup: 'Start with a 5€ gift to your balance upon signup.'
- interface: rest
- limits:
  - volume-quota (binding): 4 TB of monthly transfer is included and the page prices the rest at EUR 0.004/GB or EUR 4/TB; the harder ceiling at this shape is the 5 GB of NVMe and half a core, not the transfer [1]
- limits note: 4 TB of monthly transfer is included and the page prices the rest at EUR 0.004/GB or EUR 4/TB; the harder ceiling at this shape is the 5 GB of NVMe and half a core, not the transfer
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated on the page read: hourly billing with a web configurator and no documented API on the homepage; the tracker records IPv4 only and no IPv6 for this plan
- composes with: a EUR 3 monthly cap with 4 TB of included transfer in Barcelona makes this a cheap EU egress point or a scheduler, and the EUR 5 signup credit covers a full month at the cap; 5 GB of disk and half a core exclude it from any storage or inference role
- reliability: no reliability event recorded
- notes: The vendor page states 4 TB of monthly transfer where the tracker states 2,560 GB, so the vendor figure is recorded and the tracked figure stays in evidence. The EUR 5 signup credit is a one-off balance, not a recurring free tier, which is why the verdict is trial-only rather than paid-only. Company details on the page: Cloudi NextGen S.L., Barcelona.
- extras:
  - facets.free_tier_kind: credit
  - facets.shape.vcpu: 0.5
  - facets.shape.ram_gib: 1
  - facets.shape.disk_gib: 5
  - monthly_eur: 3.0
  - billing_term: hourly, capped at EUR 3 per month
  - in_stock: unverified: behind a sign-up; the configurator that prices the plan lives at portal.clouding.io and needs an account
  - cart_note: unverified: behind a sign-up; the hourly configurator at portal.clouding.io prices the plan only for a signed-in account
  - renewal_eur: not published: no page read prints a renewal or month-13 sentence
  - annual_eur: not published: billing is hourly with a monthly cap and no page read prints an annual term or figure
- evidence:
  - [1] 2026-10-22: plan quoted: '0.004 EUR /hora (max. 3 EUR /mes)', '1 GB RAM', '1/2 vCore', '5 GB SSD NVMe'; next tiers '0.011 EUR /hora (max. 8 EUR /mes)' with '2 GB RAM', '1 vCore', '30 GB SSD NVMe' and '0.022 EUR /hora (max. 16 EUR /mes)' with '4 GB RAM', '2 vCore', '60 GB SSD NVMe'
  - [1] 2026-10-22: transfer and credit quoted: '4 TB mensuales de transferencia incluidos. Despues, 0,004 EUR/GB o 4 EUR/TB.' and '5 EUR de saldo GRATIS al registrarte!'
  - [2] 2026-10-22: tracker row quoted: 'Clouding.io - EUR3.00 / month', '1 Intel Cores (shared)', '1,024 MB RAM', '5 GB NVMe', '2,560 GB/month bandwidth', '0.49 Gbps port speed', 'IPv4', 'Barcelona Spain'; info page marks it 'In stock now' and lists IPv6 as absent
  - [3] 2026-11-02: the registration form asks for an email address and a password and no other identity field | capture: sha256:360503e39f2d1ba7b04e1305198aac244bce6028fb86b869474fe2891286def0 | quote: Email Please fill this input Password Please fill this input
  - [3] 2026-11-02: a EUR 5 balance gift is added at signup on the same form | capture: sha256:360503e39f2d1ba7b04e1305198aac244bce6028fb86b869474fe2891286def0 | quote: Start with a 5€ gift to your balance upon signup.
  - [1] 2026-11-07: the vendor's homepage prices the smallest cloud server at EUR 0.004 an hour capped at EUR 3 a month | capture: sha256:a8d868afa5d74abca09b781bc05c1b6d85043f8a0c17e8a30c5b7e1b3ba0d9a5 | quote: 0.004
  - [1] 2026-11-07: the homepage still prices the smallest cloud server at EUR 0.004 an hour capped at EUR 3 a month | capture: sha256:a8d868afa5d74abca09b781bc05c1b6d85043f8a0c17e8a30c5b7e1b3ba0d9a5 | quote: 0.004
  - [3] 2026-11-02: the portal's registration form asks for an email and a password before any configurator is reachable | capture: sha256:360503e39f2d1ba7b04e1305198aac244bce6028fb86b869474fe2891286def0 | quote: Email Please fill this input Password Please fill this input
  - [1] 2026-11-07: the page prints the list price and no renewal sentence | capture: sha256:a8d868afa5d74abca09b781bc05c1b6d85043f8a0c17e8a30c5b7e1b3ba0d9a5 | quote: 0.004
  - [1] 2026-11-07: the page prices the smallest server hourly with a monthly cap and prints no annual term | capture: sha256:6838359f9a05ad8c77cdec463988c9f1583ff72d08db4dae86122b9e2ef4c1c2 | quote: 0.004€ /hora (máx. 3€ /mes)
  - [1] 2026-11-07: the page still prices the smallest server at EUR 0.004 an hour capped at EUR 3 a month | capture: sha256:6838359f9a05ad8c77cdec463988c9f1583ff72d08db4dae86122b9e2ef4c1c2 | quote: 0.004€ /hora (máx. 3€ /mes)
  - [1] 2026-11-07: the public configurator renders the entry shape's total as 3.00 EUR a month from RAM 1.25 plus Procesador 1.25 plus SSD NVMe 0.50 | capture: sha256:6838359f9a05ad8c77cdec463988c9f1583ff72d08db4dae86122b9e2ef4c1c2 | quote: | 3.00€<br> /mes<br> <br> /hora |
  - [1] 2026-11-07: the configurator states 4 TB of monthly transfer included | capture: sha256:6838359f9a05ad8c77cdec463988c9f1583ff72d08db4dae86122b9e2ef4c1c2 | quote: 4 TB mensuales de transferencia incluidos.
  - [1] 2026-11-07: the page still advertises EUR 5 of free balance at signup | capture: sha256:2bed048e8df298c468252cb2d11cac1cda21636a957c0d44427ec705761cb495 | quote: ¡5€ de saldo GRATIS al registrarte!
- sources:
  - [1] https://clouding.io/
  - [2] https://vpspricetracker.com/provider/Clouding_io/vps
  - [3] https://portal.clouding.io/register?lang=en
