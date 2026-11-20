# DataCamp DataLab

> datacamp.com | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/datacamp/ | JSON https://fshy.ajam.dev/api/v1/entity/datacamp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## DataCamp DataLab

- `compute/datacamp-datalab-free` | fails-quota | evidence documented | binding volume-quota | category notebook runtime | tier Free DataLab
- needs card no, phone no, ID no, institution no | verified 2026-10-24T01:52:00.000Z (live) | stale on 2026-11-24
- url https://www.datacamp.com/workspace
- free tier: a free DataLab tier with any DataCamp account: up to three workbooks and 15 uses of the AI Assistant; no compute allowance, RAM or session length is published | unit: none | metered on: none | read on: 2026-10-24 | source: [1] | note: The free tier is counted in workbooks, not hours. That is the only number the page gives.
- per-object cap: not applicable: the unit is a session, not an object
- retention: not stated | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: email | detail: a DataCamp account, which can be created for free; no card stated
- interface: rest
- limits:
  - volume-quota (binding): 3 workbooks and 15 AI Assistant uses on the free tier [1]
- binding note: three workbooks is the whole free allowance; there is no published hour budget to plan against
- interface detail: a browser workbook with Python and SQL cells
- tooling: the web workbook; DataCamp API is not documented for the workbook runtime
- composes with: a teaching workbench with three notebooks; nothing here to run a job
- reliability: no reliability event recorded
- notes: No hardware specifications are published in available documentation.
- evidence note: the workbook cap is quoted. RAM, session length and idle timeout are absent from both pages read, so this record cannot answer evaluated offerings's questions.
- extras:
  - shape.note: 'powerful hardware' is a Premium feature, unnamed
  - billing_model: free
  - term: none
  - price_arithmetic: USD 0.00 for the free tier; Premium is USD 7 a month billed annually
  - free_tier_kind: free-forever
  - unattended: no
  - unattended_mechanism: unverified: none described
  - network_out.allow_outbound: no
  - network_out.allow_inbound_listen: no
  - network_out.ports: unstated
  - network_out.static_ip: no
  - network_out.ipv6: no
  - session_cap.restart_required: no
  - session_cap.note: not published
  - units: RAM and disk are quoted in the vendor's own decimal GB, not GiB. The ram_gib and disk_gib keys carry the vendor's number unconverted, so where a vendor writes 30 GB the key holds 30 and the true value is about 27.9 GiB. No conversion was performed.
- evidence:
  - [1] 2026-10-24: quoted: 'There is a free tier of DataLab; all you need is a DataCamp account. Free DataLab users can create up to three workbooks (data projects in DataLab), and make use of the AI Assistant 15 times.'
  - [1] 2026-10-24: quoted: 'To create unlimited workbooks, use the AI assistant without limitations, access powerful hardware, prolonged version history and more, you need to upgrade to DataLab Premium.'
  - [2] 2026-10-24: the pricing page covers courses only; it publishes no DataLab compute allowance
- sources:
  - [1] https://www.datacamp.com/workspace
  - [2] https://www.datacamp.com/pricing
