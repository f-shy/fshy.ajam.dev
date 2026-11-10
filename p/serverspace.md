# Serverspace

> serverspace.by | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/serverspace/ | JSON https://fshy.ajam.dev/api/v1/entity/serverspace.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Serverspace

- `compute/serverspace` | trial-only | evidence documented | binding write-gated | category cloud VM
- needs card no, phone no, ID no, institution no | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://serverspace.by/support/help/kak-protestirovat-virtualnyj-server/
- free tier: A free trial of a virtual server of up to 8 CPU, 16 GB RAM and 200 GB of disk, lasting up to three days for an individual and up to five for a legal entity, with the exact period depending on the configuration. The trial is obtained in three steps: register and create the server within those ceilings, fill in the legal entity details if there is one, then open a support ticket stating the purpose of the test, with the final decision on the period or on refusal taken by support staff. The help page was updated on 22 October 2026. The paid catalogue starts at RUB 430 a month for one core at 3.1 GHz, 1 GB RAM and 25 GB SSD, with locations in Russia, Belarus, Kazakhstan, the Netherlands, Turkey, Canada, the United States, Brazil and Uzbekistan, payment by Mir card, SBP, bank transfer or bitcoin, and the Belarus page advertising unlimited free traffic and testing without card binding. | unit: minutes | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: approval-gated-trial
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: registration plus a support ticket stating the purpose of the test, and no card bound on the advertised route: the catalogue advertises 'testing without binding a card', so no hold exists there. The trial is granted by support staff, who may refuse it or shorten it. A third-party review reports that sole proprietors and companies registering with a corporate mailbox can receive a RUB 25,000 cloud grant, which would add an institution and corporate-email gate, reported and not read on the provider's own page
- interface: unknown
- limits:
  - write-gated (binding): The ceiling is a human decision, not a technical limit: the trial shape is the largest among documented hosts at 8 vCPU and 16 GiB for three days, but it is granted by support staff after a written purpose, so it can be refused and it cannot be renewed. [1]
- limits note: The ceiling is a human decision, not a technical limit: the trial shape is the largest among documented hosts at 8 vCPU and 16 GiB for three days, but it is granted by support staff after a written purpose, so it can be refused and it cannot be renewed.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: This is the only free machine in this category that reaches 16 GiB, so it is the only trial that can hold a working dataset in memory rather than stream it; three days at that shape is enough to run a real training or indexing job once, and the unlimited-traffic claim on the same catalogue removes the egress ceiling that binds every other trial here.
- reliability: no reliability event recorded
- notes: Three sources disagree on the length of the trial, from one day in a catalogue to five for a legal entity on the provider's own page, and the provider's page is preferred because it is dated today. The RUB 25,000 grant for sole proprietors and companies on a corporate mailbox is the largest Russian credit that is not tied to a grant programme, and it is recorded here as reported because the provider page for it was not read. Arithmetic: at the provider's own RUB 430 a month, RUB 25,000 is 58 months of the smallest machine. Not established: whether the ticket is granted in practice for an individual outside the region, and whether the 200 GB disk ceiling is included in the free trial or billed.
- extras:
  - facets.class: regional-approval-trial
  - facets.free_tier_kind: approval-gated-trial
  - facets.shape.vcpu: 8
  - facets.shape.ram_gib: 16
  - facets.shape.gpu_count: 0
  - facets.shape.disk_gib: 200
- evidence:
  - [1] 2026-10-22: trial up to 5 days for legal entities and up to 3 for individuals, a server within 8 CPU, 16 GB RAM and 200 GB of disk, obtained through a support ticket stating the purpose, with the final decision on the period or refusal made by support staff; page updated 22 October 2026, quoted and translated
  - [2] 2026-10-22: the catalogue advertises unlimited free traffic, billing every 10 minutes, and testing without binding a card, from 0.27 Belarusian roubles a day, quoted and translated
  - [3] 2026-10-22: a third-party review states there is no free test for everyone, that a welcome bonus is decided by an antifraud system, and that sole proprietors and companies registering with a corporate mailbox can receive a RUB 25,000 cloud grant extendable to three months
  - [4] 2026-10-22: a catalogue lists Serverspace with a one-day test at RUB 390 for 1 GB and 1 core, which is shorter and cheaper than the provider's own help page describes
- sources:
  - [1] https://serverspace.by/support/help/kak-protestirovat-virtualnyj-server/
  - [2] https://serverspace.by/services/vps-server/cheap/
  - [3] https://hostpulse.ru/obzory/serverspace/
  - [4] https://hostingrate.ru/
