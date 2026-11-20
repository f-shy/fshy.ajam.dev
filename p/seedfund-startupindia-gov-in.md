# Startup India Seed

> seedfund.startupindia.gov.in | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/seedfund-startupindia-gov-in/ | JSON https://fshy.ajam.dev/api/v1/entity/seedfund-startupindia-gov-in.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## Startup India Seed

- `compute/startup-india-seed` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card no, phone no, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://seedfund.startupindia.gov.in/faq
- free tier: Up to INR 20 lakh as a milestone-based grant for proof of concept, prototype development or product trials, plus up to INR 50 lakh of investment through convertible debentures, debt or debt-linked instruments for market entry and commercialisation, disbursed through eligible incubators rather than directly by the government. | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: grant
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution
- interface: unknown
- limits:
  - write-gated (binding): The applicant must be 'A startup, recognized by DPIIT, incorporated not more than 2 years ago at the time of application', and DPIIT recognition requires an Indian incorporated entity, so a person with no Indian company fails before the incubator sees the application. [1]
- limits note: The applicant must be 'A startup, recognized by DPIIT, incorporated not more than 2 years ago at the time of application', and DPIIT recognition requires an Indian incorporated entity, so a person with no Indian company fails before the incubator sees the application.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The two halves do not stack into one cheque: the INR 20 lakh is a grant and the INR 50 lakh is a repayable instrument, so the free portion is the smaller number. Because disbursement runs through an incubator, the practical gate after DPIIT is an incubator selection, which is a second discretionary review.
- reliability: no reliability event recorded
- notes: The number worth remembering is 20 lakh, because the 50 lakh beside it is debt-like and a reader who takes the pair as a grant overstates the free capacity by a factor of 3.5. DPIIT recognition is not open to foreign founders: recognition requires an entity incorporated in India. Whether the scheme accepts a sole proprietorship is unresolved: the FAQ says 'incorporated', which in Indian usage usually means a company or LLP rather than a proprietorship. The 2-year incorporation clock cannot be paused: it is measured at the time of application.
- extras:
  - facets.class: government-grant
  - facets.free_tier_kind: grant
- evidence:
  - [1] 2026-10-22: 'Up to Rs. 20 Lakhs as grant for validation of Proof of Concept, or prototype development, or product trials'; 'Up to Rs. 50 Lakhs of investment for market entry, commercialization, or scaling up through convertible debentures or debt', quoted
  - [1] 2026-10-22: 'A startup, recognized by DPIIT, incorporated not more than 2 years ago at the time of application is invited to apply'
  - [2] 2026-10-22: the DPIIT playbook one-pager repeats 'DPIIT recognised startups' and 'Incorporated not more than 2 years ago at the time of application', quoted
  - [3] 2026-10-22: 
- sources:
  - [1] https://seedfund.startupindia.gov.in/faq
  - [2] https://www.startupindia.gov.in/content/dam/startupindia/homebanners/Startup-Schemes-Playbook-June-2026.pdf
  - [3] https://www.startupindia.gov.in/content/dam/invest-india/brics/gotomarket-guide-india.pdf
