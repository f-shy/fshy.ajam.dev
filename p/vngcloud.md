# VNG Cloud

> vngcloud.vn | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/vngcloud/ | JSON https://fshy.ajam.dev/api/v1/entity/vngcloud.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## VNG Cloud

- `compute/vng-cloud` | fails-identity | evidence documented | binding write-gated | category cloud VM
- needs card no, phone yes, ID no, institution yes | verified 2026-10-22 (live) | stale on 2026-11-22
- url https://vngcloud.vn/promotions/chinh-sach-chuong-trinh-uu-dai-danh-cho-tat-ca-dich-vu-cua-vng-cloud
- free tier: 'B n d ng th mi n ph d nh cho kh ch h ng m i c a n n t ng VNG Cloud ch a s d ng d ch v tr c y. B n d ng th ch kh d ng cho c c d ch v vServer v vStorage, c gi tr t 3.500.000 n 20.000.000 VN ' (a free trial for new customers, only for vServer and vStorage, worth VND 3,500,000 to VND 20,000,000) for 30 days, and 'Ch p d ng cho kh ch h ng i n y chi ti t th ng tin Doanh nghi p v cung c p domain email Doanh nghi p' (only for customers who supply full business details and a corporate email domain). | unit: none | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: trial-credit
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: a registered business with its own email domain: the trial policy admits only "Doanh Nghi p" (businesses) that have never used the platform and requires the customer to supply full business details and a corporate email domain, and the live trial form requires "Full Name", "Your Company email", "Phone", "Company Name" and "Job Title". So a company, a company email domain and a phone number are all required; no card or hold is stated, and debit or prepaid do not arise because the trial credit is free. The policy text still says the programme ends 2023-12-31 while the form is live
- interface: unknown
- limits:
  - write-gated (binding): A registered business with its own email domain is the door: the trial form asks for 'Company email', 'Company Name' and 'Job Title', and the policy admits only 'Doanh Nghi p' (businesses) that have never used the platform, so no individual can claim the VND 20,000,000 ceiling at all. [1]
- limits note: A registered business with its own email domain is the door: the trial form asks for 'Company email', 'Company Name' and 'Job Title', and the policy admits only 'Doanh Nghi p' (businesses) that have never used the platform, so no individual can claim the VND 20,000,000 ceiling at all.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: None: the trial is a business instrument, and the free-tier experience the docs describe for a first vServer signup is not documented in enough detail to plan against.
- reliability: no reliability event recorded
- notes: VNG Cloud offers cloud infrastructure in Vietnam with promotional startup credits of up to USD 150 for 30 days, requiring corporate business registration and tax ID verification.
- extras:
  - facets.class: regional
  - facets.free_tier_kind: trial-credit
  - facets.shape.gpu_count: 0
- evidence:
  - [1] 2026-10-22: 'B n d ng th ch kh d ng cho c c d ch v vServer v vStorage, c gi tr t 3.500.000 n 20.000.000 VN ' and 'Ch p d ng cho kh ch h ng i n y chi ti t th ng tin Doanh nghi p v cung c p domain email Doanh nghi p', quoted; the same page also still carries 'Ch ng tr nh u i di n ra n h t ng y 31.12.2023' (the program runs to 31 December 2023)
  - [2] 2026-10-22: a live trial form headed 'Try VNG Cloud for free with US$150 credits in 30 days' with required fields 'Full Name', 'Your Company email', 'Phone', 'Company Name', 'Job Title', quoted
  - [3] 2026-10-22: 'When you first sign up for the vServer service, you can start with free usage', and after the free tier ends billing starts 'even if it is idle', quoted
- sources:
  - [1] https://vngcloud.vn/promotions/chinh-sach-chuong-trinh-uu-dai-danh-cho-tat-ca-dich-vu-cua-vng-cloud
  - [2] https://vngcloud.vn/form/VNGCloudTrialregistrationInterativetour/formperma/LOHqsCn6C-YKNFtnsJTN5IDmec_6GrCUrXnZ-n00bPw
  - [3] https://docsdev.vngcloud.vn/english/vserver/getting-started
