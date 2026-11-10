# India DigiLocker

> digilocker.gov.in | Storage; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/digilocker-gov-in/ | JSON https://fshy.ajam.dev/api/v1/entity/digilocker-gov-in.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## India DigiLocker

- `storage/india-digilocker` | fails-quota | evidence reported | binding per-object-cap | category gov-citizen-wallet
- needs card no, phone no, ID yes, institution no | verified 2026-10-21 (inherited) | stale on 2026-11-05
- url https://www.digilocker.gov.in/
- free tier: 1 GB per account for citizen-uploaded documents (was 100 MB at launch). | unit: GB | metered on: unstated | read on: 2026-10-21 | source: [1]
- per-object cap: 10 MB/file | bytes: 10000000 | source: [1] | note: not stated
- retention: source: [1] | note: not stated
- egress: Not applicable. Documents are private to the account holder and to requesting agencies via consent; there is no public/anonymous retrieval URL. That alone disqualifies it as a serving or archive tier. | metered: no
- identity: national-id | detail: national-id
- interface: unknown
- limits:
  - per-object-cap (binding): 10 MB/file [1]
- limits note: per-object-cap 10 MB/file, per-account 1 GB. identity_cost is the hard stop: Aadhaar number + OTP to the Aadhaar-linked Indian mobile. A non-resident without an Aadhaar-linked +91 number cannot register at all.
- interface detail: No public upload API. Partner agencies integrate via DigiLocker APIs; individuals use the app/web UI only.
- tooling: none for bulk; UI-only for citizens.
- composes with: None. Private namespace, consent-gated sharing, no direct link model.
- reliability: ISO 27001 state service, very reliable, but 1 GB total and no public URLs mean it fails two of the four filters simultaneously.
- notes: the same as the free tier
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: 1 GB per account for citizen-uploaded documents (was 100 MB at launch).
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: 'It also provides 1 GB storage space to each account to upload scanned copies of legacy documents'; 'Users need to possess an Aadhaar number... identity is verified using a one-time password (OTP) sent to the linked mobile number'; 'Individual files are limited to 10 MB.'
  - [2] 2026-10-21: live, official NeGD/MeitY operator page (no consumer quota or API published there)
- sources:
  - [1] https://en.wikipedia.org/wiki/DigiLocker
  - [2] https://www.digilocker.gov.in/web/about
