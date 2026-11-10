# NLnet

> nlnet.nl | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/nlnet/ | JSON https://fshy.ajam.dev/api/v1/entity/nlnet.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## NLnet / Restack fund (NGI Zero successor)

- `storage/nlnet-restack-fund` | qualifies-with-caveat | evidence reported | binding none | category academic
- identity a placeholder: card and phone unknown | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nlnet.nl/funding.html
- disagrees on identity_kind: `storage/nlnet-restack-fund` says institution, `storage/nlnet-restack-fund-the-grant-an-unaffiliated-individual` says email
- free tier: EUR 5,000-50,000 per first grant, 'with the possibility to scale them up if there is proven potential'. Storage is a claimable project cost, not a byte allocation. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A - cash grant. | metered: no
- identity: institution | detail: inferred from the category 'academic'; the source record states no identity cost, so this is a class assumption, not evidence
- interface: unknown
- limits note: Deadline 3rd of every odd month; next 3 Nov 2026 12:00 CET. EU-supported funds 'require a strong European dimension... applicants should (mostly) be from Horizon Europe-eligible countries' - a non-EU applicant should apply to the open call / non-EU-funded strand. AI projects out of scope. Must release everything under an open licence.
- interface detail: n/a
- tooling: the same as interface detail
- composes with: Explicitly open to individuals, so an unaffiliated individual can hold the grant directly - no fiscal sponsor needed. Restack's scope includes 'actual services and their client-side counterparts' and infrastructure layers, which covers a hosting/storage service.
- reliability: Small sums relative to 20 TB of storage; realistically funds the software, not the bytes. Disbursement requires a bank account and contracting entity.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'In principle anyone can apply: individuals, research organisations, non-profits, public institutions, companies'
  - [2] 2026-10-21: 'Between EUR 5 000 and EUR 50 000 for a first grant'; 'Next deadline November 3rd 2026'
  - [3] 2026-10-21: 'EUR 7 million euro in small to medium-size R&D grants'; scope includes infrastructure services
- sources:
  - [1] https://nlnet.nl/funding.html
  - [2] https://nlnet.nl/propose/
  - [3] https://nlnet.nl/restack/

## NLnet / Restack Fund - the grant an unaffiliated individual can actually hold

- `storage/nlnet-restack-fund-the-grant-an-unaffiliated-individual` | qualifies-with-caveat | evidence reported | binding none | category grant
- needs card no, phone no, ID no, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://nlnet.nl/propose/
- disagrees on identity_kind: `storage/nlnet-restack-fund` says institution, `storage/nlnet-restack-fund-the-grant-an-unaffiliated-individual` says email
- free tier: EUR 5,000-50,000 for a first grant, and storage is a claimable project expense rather than a byte allocation. Next deadline 3 November 2026 12:00 CET; deadlines fall on the 3rd of every odd month. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: n/a - cash. | metered: no
- identity: email | detail: email
- interface: unknown
- limits note: Must be technical development, released under an open licence, and no AI-generated proposals ('We are not interested in AI-generated projects or proposals'). EU-supported funds require a European dimension - a non-EU applicant must pick a fund whose eligibility section does not impose it. Money arrives against a contract, so a bank account and a legal entity are needed.
- interface detail: n/a
- tooling: the same as interface detail
- composes with: Explicitly individual-eligible: 'In principle anyone can apply: individuals, research organisations, non-profits, public institutions, companies of any size and type'. A second grant can follow a first. Funds open at proposal time: Restack, CodeSupply, Other/open call.
- reliability: Realistic size: a EUR 50k grant buys roughly 12-25 TB-months at Hetzner-class pricing, or funds an engineer - it does not buy 20 TB for five years. Treat grants as funding the software around the storage, not the storage.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'In principle anyone can apply: individuals, research organisations, non-profits, public institutions, companies of any size and type'
  - [2] 2026-10-21: 'Between EUR 5 000 and EUR 50 000 for a first grant'; 'Next deadline: November 3rd 2026 12:00 CET'; fund picker lists Restack Fund, CodeSupply Fund, Other/open call
- sources:
  - [1] https://nlnet.nl/funding.html
  - [2] https://nlnet.nl/propose/
