# IndiaAI Compute Portal

> compute.indiaai.gov.in | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/compute-indiaai-gov-in/ | JSON https://fshy.ajam.dev/api/v1/entity/compute-indiaai-gov-in.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IndiaAI Compute Portal

- `compute/indiaai-compute-portal` | fails-identity | evidence documented | binding write-gated | category GPU cloud
- needs card unknown, phone yes, ID no, institution yes | verified 2026-11-03T10:24:21.780Z (live) | stale on 2026-12-04
- url https://compute.indiaai.gov.in/files/end-user-policy.pdf
- free tier: Empanelled AI cloud services at a subsidy of 'maximum up to 40%', borne by the IndiaAI mission, on a published average of 'approximately Rs 65 per GPU per hour' across 38,231 onboarded GPUs from 14 service providers. Requests of 5,000 GPU hours or fewer, with 50 GPUs or fewer, and with no subsidy sought, skip the PMEC committee and are approved by an institutional verifier or a MeitY Startup Hub CoE. | unit: hours | metered on: wall-clock | read on: 2026-10-22 | source: [1] | note: recurring-subsidy
- per-object cap: not applicable | source: [1]
- retention: not applicable | source: [1]
- egress: not stated | metered: no | source: [1]
- identity: institution | detail: institution: registration needs 'their name, institute / organization email address and mobile number', so a mobile number is collected alongside an institutional email. The student path adds 'Apaar ID' plus 'Endorsement by appointed academic faculty verifier and endorser or IndiaAI CEO'; the startup paths require 'Valid DPIIT startup recognition certificate along with DPIIT ID' and 'Certificate of Incorporation'. No card, hold, debit or prepaid statement appears in any evidence row: unknown.
- interface: unknown
- limits:
  - write-gated (binding): Registration requires a name, an 'institute / organization email address' and a mobile number, both verified with an OTP, and then an eligibility ID by category: a Google Scholar ID with h-index, ORCID ID or Scopus Author ID for researchers (h-index of 5 or more), an APAAR ID for UG/PG students, DPIIT recognition for startups, or an Udhyam ID for MSMEs; early-stage startups (3.6) need 4 years of founder experience and an endorsement by the CEO of IndiaAI or a JS rank officer and above. [1]
- limits note: Registration requires a name, an 'institute / organization email address' and a mobile number, both verified with an OTP, and then an eligibility ID by category: a Google Scholar ID with h-index, ORCID ID or Scopus Author ID for researchers (h-index of 5 or more), an APAAR ID for UG/PG students, DPIIT recognition for startups, or an Udhyam ID for MSMEs; early-stage startups (3.6) need 4 years of founder experience and an endorsement by the CEO of IndiaAI or a JS rank officer and above.
- binding note: the same as limits note
- interface detail: inferred from the tooling the provider documents; not probed
- tooling: not stated
- composes with: The 40% is a discount on an empanelled provider's list price, so it composes with the provider's own trial rather than replacing it: the same GPU appears at E2E Networks, NxtGen and Yotta, and the undiscounted lane can be priced directly with those vendors while the subsidy is unavailable.
- reliability: no reliability event recorded
- notes: Indian nationality is not required: the policy never states a nationality test. A company is not required on the 3.6 early-stage-startup path, which names only four years of founder experience and an endorsement, no incorporation document. An Indian institutional email is required, as stated at 4.1, and it is what actually stops a foreign individual, because APAAR IDs are issued by Indian institutions and the CoE endorsement chain runs through MeitY. Section 3.6 is therefore the only lane that a foreign individual might argue into, and it is decided by a discretionary endorsement rather than a document, so the verdict stays fails-identity and the open question is whether IndiaAI accepts a non-Indian organisation email at registration.
- extras:
  - facets.class: government-credit
  - facets.free_tier_kind: recurring-subsidy
  - facets.shape.gpu_class: A100 40GB, A100 80GB, H100 SXM, H100 NVL, H200 SXM, L40S, L4
  - facets.shape.gpu_count: 50
- evidence:
  - [1] 2026-10-22: 'A subsidy maximum up to 40% will be provided to the eligible end users which will be borne by IndiaAI mission', quoted from section 5.2
  - [1] 2026-10-22: 'To access the IndiaAI compute platform users would be required to register on the IndiaAI compute portal with their name, institute / organization email address and mobile number', quoted from 4.1
  - [1] 2026-10-22: 'This category applies to startups & MSMEs who are DPIIT registered and have either generated revenue or raised funds', requiring 'Valid DPIIT startup recognition certificate along with DPIIT ID' and 'Certificate of Incorporation', quoted from 3.4
  - [1] 2026-10-22: student path requires 'Apaar ID' plus 'Endorsement by appointed academic faculty verifier and endorser or IndiaAI CEO', quoted from 3.3
  - [1] 2026-10-22: 'This category applies to pre-revenue / funding startups' gated on 'Founder(s) / permanent staff with experience of 4 years' and 'Endorsement by CEO IndiaAI / JS rank officer and above', quoted from 3.6
  - [2] 2026-10-22: '38,231 GPUs have been onboarded from 14 empaneled service providers'; 'The average rate is approximately Rs 65 per GPU per hour, except for select high-end GPUs', quoted, Press Information Bureau
  - [3] 2026-10-22: published counter reads 'Total Subsidy Allocated: INR 11,89,44,82,338', read from the portal page
  - [4] 2026-10-22: allocation ledger row 13: Sarvam AI Axonwise Pvt Ltd, 4096 H100 SXM via Yotta, subsidy INR 98,68,62,256.12 on a bill of materials of INR 2,46,71,55,640.32, project 2025-06-01 to 2025-12-01, read from the table
  - [4] 2026-10-22: ledger rows show the subsidy equals 40.0% of the bill of materials: Keenheads 44,656 on 111,640; CloudMojo 352,848 on 882,120; Sarvam 98,68,62,256 on 2,46,71,55,640, derived by division from the published table
  - [5] 2026-11-03: the on-demand L1 bid for one H100 SXM is INR 170.00 per hour against a list price of INR 480.00; the annexure lists no RTX 4090 | capture: sha256:2666b9a8e109d94cec71c456728ddafe6ef7073d2c70c94d4dbcf3417868b044 | quote: 18 NVIDIA H100 SXM (1x) E2E Networks Ltd 170.00 480.00 64.58% 149.00 450.00 66.89%
  - [5] 2026-11-03: A100 80GB 1x on-demand L1 bid INR 151.00 per hour, list INR 226.00 | capture: sha256:2666b9a8e109d94cec71c456728ddafe6ef7073d2c70c94d4dbcf3417868b044 | quote: 13 NVIDIA A100 80GB (1x) E2E Networks Ltd 151.00 226.00 33.19% 99.00 137.00 27.74%
  - [5] 2026-11-03: A100 40GB 1x on-demand L1 bid INR 136.00 per hour, list INR 170.00 | capture: sha256:2666b9a8e109d94cec71c456728ddafe6ef7073d2c70c94d4dbcf3417868b044 | quote: 10 NVIDIA A100 40 GB (1x) E2E Networks Ltd 136.00 170.00 20.00% 89.00 103.00 13.59%
  - [5] 2026-11-03: H100 PCIe 1x on-demand L1 bid INR 252.00 per hour, list INR 378.00 | capture: sha256:2666b9a8e109d94cec71c456728ddafe6ef7073d2c70c94d4dbcf3417868b044 | quote: 16 NVIDIA H100 PCIe (1x) CtrlS Datacenters Ltd 252.00 378.00 33.33% 234.00 351.00 33.33%
  - [5] 2026-11-03: L4 1x on-demand L1 bid INR 50.00 per hour, list INR 221.08 | capture: sha256:2666b9a8e109d94cec71c456728ddafe6ef7073d2c70c94d4dbcf3417868b044 | quote: 24 NVIDIA L4 (1x) E2E Networks Ltd 50.00 221.08 77.38% 30.00 201.18 85.09%
  - [5] 2026-11-03: L40S 1x on-demand L1 bid INR 75.00 per hour, list INR 355.55 | capture: sha256:2666b9a8e109d94cec71c456728ddafe6ef7073d2c70c94d4dbcf3417868b044 | quote: 75.00 355.55 78.91% 55.00 323.55 83.00%
  - [1] 2026-11-03: registration needs a name, an institute or organization email address and a mobile number | capture: sha256:1b7dd1b6e4c430000ad324836a230041db2e7c339ae55e7863427e936ad5fd01 | quote: users would be required to register on the IndiaAI compute portal with their name, institute / organization email address and mobile number
  - [1] 2026-11-03: registration needs a name, an institute / organization email address and a mobile number | capture: sha256:1b7dd1b6e4c430000ad324836a230041db2e7c339ae55e7863427e936ad5fd01 | quote: To access the IndiaAI compute platform users would be required to register on the IndiaAI compute portal with their name, institute / organization email address and mobile number.
  - [1] 2026-11-03: researchers register with a Google Scholar, ORCID or Scopus Author ID, no APAAR ID or company | capture: sha256:1b7dd1b6e4c430000ad324836a230041db2e7c339ae55e7863427e936ad5fd01 | quote: d. Google Scholar ID with h-index / ORCID ID / Scopus Author ID for researchers
  - [1] 2026-11-03: startups use DPIIT recognition and MSMEs an Udhyam ID | capture: sha256:1b7dd1b6e4c430000ad324836a230041db2e7c339ae55e7863427e936ad5fd01 | quote: b. DPIIT recognition for startups c. Udhyam ID for MSMEs
  - [1] 2026-11-03: the researcher category in 3.1 is gated on an h-index of 5 or more | capture: sha256:1b7dd1b6e4c430000ad324836a230041db2e7c339ae55e7863427e936ad5fd01 | quote: The lead / sole researcher or faculty should have an h index greater than or equal to 5
  - [1] 2026-11-03: category 3.1 admits independent researchers as well as faculty | capture: sha256:1b7dd1b6e4c430000ad324836a230041db2e7c339ae55e7863427e936ad5fd01 | quote: This category applies to Independent AI researchers and AI researchers and faculty affiliated to academic institutions.
- sources:
  - [1] https://compute.indiaai.gov.in/files/end-user-policy.pdf
  - [2] https://www.pib.gov.in/PressReleasePage.aspx?PRID=2245063&lang=2&reg=48
  - [3] https://compute.indiaai.gov.in/endusers
  - [4] https://indiaai.gov.in/hub/indiaai-compute-capacity
  - [5] https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/jan/doc2025130492001.pdf
