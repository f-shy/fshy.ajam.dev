# Chan Zuckerberg

> chanzuckerberg.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/chanzuckerberg/ | JSON https://fshy.ajam.dev/api/v1/entity/chanzuckerberg.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Chan Zuckerberg Initiative - Essential Open Source Software for Science (EOSS)

- `storage/chan-zuckerberg-initiative-essential-open-source-softwar` | qualifies-with-caveat | evidence reported | binding write-gated | category academic
- needs card no, phone no, ID no, institution yes | verified 2026-11-19T21:12:58.758Z (live) | stale on 2026-12-04
- url https://chanzuckerberg.com/rfa/essential-open-source-software-for-science/
- free tier: No byte quota - $100,000-$400,000 total over two years, from which cloud/storage is a claimable line item. | unit: mixed | metered on: stored-bytes | read on: 2026-10-21 | source: [1]
- per-object cap: source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: N/A - grant money, you buy the egress. | metered: no
- identity: institution | detail: the award is made to an organisation and never to an individual: an eligible nonprofit or for-profit organisation, public or private institution, or a fiscal sponsor such as NumFOCUS for a project with no institution of its own. The application form asks for the applicant's institution or affiliation and, separately, the award organisation, and the full proposal needs institutional sign-off. No card and no phone number is asked for.
- interface: unknown
- limits:
  - write-gated (binding): invited full proposal) [1]
  - write-gated (binding): applications from any country' subject to US export-control screening [1]
- limits note: Two-year grants. Two-stage (LOI then invited full proposal). Requires an organisation or a fiscal sponsor secured by the full-proposal deadline. 'We welcome applications from any country' subject to US export-control screening; non-US institutions cannot subcontract to US institutions if CZI funds it.
- interface detail: n/a
- tooling: the same as interface detail
- composes with: The eligibility bridge matters more than the money: 'Grants are not permitted to individuals, only to organizations' but a fiscal sponsor is allowed (NumFOCUS, Code for Science & Society). An individual with an OSS project applies through the sponsor and can then budget multi-year object storage explicitly.
- reliability: Cycle-based, not rolling - the current cycle page shows Cycle 6 closed, so timing is the gate. Large award, slow cadence.
- notes: the same as the free tier
- evidence:
  - [1] 2026-10-21: 'Grants are not permitted to individuals, only to organizations'; 'it may designate a fiscal sponsor (e.g., NumFOCUS...)'
  - [1] 2026-10-21: '$50,000 USD and $200,000 USD total costs per year for two years'; 'All grants, regardless of funder, will be for two years'
  - [1] 2026-10-21: 'We welcome applications from any country, provided the proposed work is compliant with... OFAC'
  - [2] 2026-10-21: Cycle 6 $11.7M with Kavli and Wellcome
  - [1] 2026-11-01: a project with no eligible institution applies through a fiscal sponsor, which is the only non-institutional route | capture: sha256:5f1c38101cc909366cff3be29a01bb593c138dbf8f09134bca04be6dac18a032 | quote: it may designate a fiscal sponsor
  - [1] 2026-11-01: the request is $50,000 to $200,000 a year for two years, the $100,000 to $400,000 total over two years the record states | capture: sha256:5f1c38101cc909366cff3be29a01bb593c138dbf8f09134bca04be6dac18a032 | quote: Applications can request funding between $50,000 USD and $200,000 USD total costs per year for two years
  - [1] 2026-11-19: the RFA states the annual and two-year funding range | capture: sha256:64895e3f7ef1a6815ca425f568f2589fc0bb4ee9ecd03017a54f4739f17e03be | quote: Applications can request funding between $50,000 USD and $200,000 USD total costs per year for two years
  - [1] 2026-11-19: the RFA permits an independent project to use a fiscal sponsor | capture: sha256:64895e3f7ef1a6815ca425f568f2589fc0bb4ee9ecd03017a54f4739f17e03be | quote: it may designate a fiscal sponsor
  - [1] 2026-11-19: the RFA states the grant is made to organizations, not individuals | capture: sha256:64895e3f7ef1a6815ca425f568f2589fc0bb4ee9ecd03017a54f4739f17e03be | quote: Grants are not permitted to individuals, only to organizations.
  - [1] 2026-11-19: the RFA requires the sponsor to be secured by the full-proposal deadline | capture: sha256:64895e3f7ef1a6815ca425f568f2589fc0bb4ee9ecd03017a54f4739f17e03be | quote: If your application requires a fiscal sponsor, you must secure one by the full proposal application deadline.
- sources:
  - [1] https://chanzuckerberg.com/rfa/essential-open-source-software-for-science/
  - [2] https://chanzuckerberg.com/eoss/

## czi essential open source software for science (eoss) as an individual rout

- `storage/czi-essential-open-source-software-for-science-as-an-ind` | fails-quota | evidence reported | binding none | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-19T21:15:48.061Z (live) | stale on 2026-12-04
- page https://fshy.ajam.dev/p/chanzuckerberg.md
- free tier: none reachable: the first-party EOSS RFA states that grants are not permitted to individuals, only to organizations, and an unaffiliated applicant may designate a fiscal sponsor organization. | unit: none | metered on: none | read on: 2026-10-21
- per-object cap: stated-absent: the CZI EOSS program page states no per-object size cap | note: not applicable
- retention: stated-absent: the CZI EOSS RFA states no retention period for stored bytes
- egress: stated-absent: the CZI EOSS program page states no egress terms for stored bytes | metered: no
- identity: email
- interface: browser
- interface detail: stated-absent: the CZI EOSS program is a grant fund administered through an application portal and states no file or object storage interface
- tooling: not documented
- composes with: stated-absent: the CZI EOSS program is a grant fund and states no way to chain byte storage with other services
- reliability: Grants are awarded to institutions rather than individuals. Unaffiliated applicants must designate a formal fiscal sponsor.
- notes: the same as reliability
- evidence note: Rejection quoted from historical research records; unverified against live endpoints.
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: Grants go to organisations; an unaffiliated person must designate a fiscal sponsor, and every CZI RFA repeats 'All grants will be awarded to institutions, not individuals'. Also out…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - withheld 2026-10-21: Grants go to organisations; an unaffiliated person must designate a fiscal sponsor, and every CZI RFA repeats 'All grants will be awarded to institutions, not individuals'. Also out o
  - [1] 2026-11-19: the first-party RFA still states that grants go to organizations, not individuals | capture: sha256:64895e3f7ef1a6815ca425f568f2589fc0bb4ee9ecd03017a54f4739f17e03be | quote: Grants are not permitted to individuals, only to organizations. Open source software projects operating independently must be affiliated with an organization
  - [2] 2026-11-19: the CZI EOSS RFA is an application document processed through CZI's application portal, not a byte-storage service | capture: sha256:64895e3f7ef1a6815ca425f568f2589fc0bb4ee9ecd03017a54f4739f17e03be | quote: The Funders have partnered on this request for applications because of our shared commitment to supporting software critical to biomedical research.
  - [3] 2026-11-19: the program is a software-maintenance grant fund, not a byte store | capture: sha256:8042de09818de11bb876f7a2f6c5fc6dc63444cb48931cd96490f8cdb6093169 | quote: CZI’s Essential Open Source Software for Science program supports software maintenance, growth, development, and community engagement for critical open source tools.
  - [2] 2026-11-19: the RFA states a two-year grant duration, not a retention period for stored bytes | capture: sha256:64895e3f7ef1a6815ca425f568f2589fc0bb4ee9ecd03017a54f4739f17e03be | quote: All grants, regardless of funder, will be for two years
- sources:
  - [1] https://chanzuckerberg.com/rfa/essential-open-source-software-for-science
  - [2] https://chanzuckerberg.com/rfa/essential-open-source-software-for-science/
  - [3] https://chanzuckerberg.com/eoss
