# Fiscal Data

> fiscaldata.treasury.gov | Data APIs; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/fiscaldata-treasury-gov/ | JSON https://fshy.ajam.dev/api/v1/entity/fiscaldata-treasury-gov.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Fiscal Data (U.S. Treasury)

- `data-apis/fiscal-data-treasury` | qualifies | evidence documented | binding none | category government finance data API (debt, revenue, spending, interest rates, exchange rates) | tier Free
- needs card no, phone no, ID no, institution no | verified 2026-11-03T00:30:00.000Z (live) | stale on 2026-12-04
- url https://fiscaldata.treasury.gov/api-documentation/
- free tier: Open API with no account and no token; no request rate or quota is stated; data free without restriction, in JSON, CSV or XML | unit: unlimited | metered on: none | read on: 2026-11-02 | source: [1] | note: Base https://api.fiscaldata.treasury.gov/services/api/fiscal_service; fields, filter, sort, format and page[number] and page[size] parameters apply. A keyless debt-to-the-penny call answered HTTP 200.
- per-object cap: not stated on the documentation page | source: [1] | note: Paging uses page[number] and page[size].
- retention: not applicable
- egress: not metered; no quota is stated | metered: no | source: [1]
- identity: anonymous | detail: The API is open and needs no user account or registration for a token; a keyless call answered HTTP 200.
- interface: rest
- limits:
  - request-rate: no request rate stated [1]
- limits note: Bulk path: every dataset is available as a machine-readable file download on the website.
- binding note: No request count or rate is published.
- interface detail: GET https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny with fields, filter, sort, format and paging parameters, no key
- endpoint: part of interface detail
- tooling: curl or any HTTP client; every dataset also downloads as a file from the website
- composes with: Keyless US federal debt, rates and exchange-rate tables; they pair with FRED series and the BLS data.
- reliability: No limit is published; a shared government service can throttle heavy callers.
- notes: Keyless with no stated rate. Bulk path: file downloads per dataset.
- evidence note: Access terms are read from the vendor pages and a keyless call answered 200; no rate was measured.
- extras:
  - bulk_path: file downloads of every dataset on the website
- evidence:
  - [1] 2026-11-02: the API needs no account or token registration | capture: sha256:8660e02c942d9f97f204db1979e09e897b2168fb1875f6011d5a5754fb64f48b | quote: Our API is open, meaning that it does not require a user account or registration for a token.
  - [1] 2026-11-02: the data is free without restriction | capture: sha256:8660e02c942d9f97f204db1979e09e897b2168fb1875f6011d5a5754fb64f48b | quote: The data is offered free, without restriction, and available to copy, adapt, redistribute
  - [1] 2026-11-02: paging parameters | capture: sha256:8660e02c942d9f97f204db1979e09e897b2168fb1875f6011d5a5754fb64f48b | quote: The `page[number]=` and `page[size]=` parameters both accept integers.
  - [2] 2026-11-02: every dataset downloads in machine-readable formats | capture: sha256:25f5a54176b06cb91117cf46d0b01397b85a5e328d9e91b54ac59cdec02ed2b7 | quote: All of our datasets are available for download in multiple machine-readable formats
  - probe:https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?page%5Bsize%5D=1 2026-11-03: a keyless call answered HTTP 200 | capture: sha256:59917c780b0b9420fd630657721aca5d49b3cf1bc680a4fb62cf5986a79fd1f4 | quote: "status": 200
- sources:
  - [1] https://fiscaldata.treasury.gov/api-documentation/
  - [2] https://fiscaldata.treasury.gov/about-us/
