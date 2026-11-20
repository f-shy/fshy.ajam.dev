# centron

> centron.de | Compute; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/centron/ | JSON https://fshy.ajam.dev/api/v1/entity/centron.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## centron

- `compute/centron` | trial-only | evidence documented | binding volume-quota | category GPU cloud
- needs card unknown, phone no, ID no, institution no | verified 2026-11-03T07:36:21.177Z (live) | stale on 2026-12-04
- url https://www.centron.de/en/pricing/gpu
- free tier: a starting credit of EUR 200 for new accounts within the first 60 days, a promotional offer for new accounts available exclusively to businesses; after it, dedicated GPU instances are billed by the hour, the A100 (80 GB) at EUR 1.7917 an hour | unit: credits | metered on: wall-clock | read on: 2026-11-03 | source: [1] | note: trial
- per-object cap: not applicable | source: [1] | note: the ceiling that matters is the GPU class: 16, 24, 40, 48 or 80 GB of VRAM per instance
- retention: not stated on the pages read | source: [1] | note: a machine record: instances are billed from creation until deleted
- egress: not stated on the pages read: no egress term was found, so nothing is asserted | metered: no | source: [1]
- identity: email | detail: The registration form asks for an email address and a password, or Sign up with Google or GitHub, behind a Friendly Captcha widget. The credit is stated as available exclusively to businesses. Whether a business check or a payment method is asked after sign-up is unverified: behind a sign-up.
- interface: unknown
- limits:
  - volume-quota (binding): EUR 200 of starting credit within the first 60 days of a new account, available exclusively to businesses; billing then runs by the hour [1]
- limits note: the binding count is the EUR 200 credit and its 60-day window; the same page limits the offer to businesses
- binding note: the binding count is the EUR 200 starting credit inside 60 days; the offer is stated as available exclusively to businesses
- interface detail: a web console at cloud.centron.de; no API or CLI was read, so the interface is not established
- tooling: a web console for creating GPU instances, with Linux or Windows Server images; no client tooling was read
- composes with: none established: the credit is EUR 200 for 60 days and limited to businesses, so it does not chain into a longer free lane.
- reliability: no reliability event was observed on the pages read and no status page was read
- notes: The vendor GPU price table read on 2026-11-03 lists five cards: RTX A4000 16 GB at EUR 0.2069, Quadro RTX 6000 24 GB at EUR 0.2764, A100 40 GB at EUR 0.9583, A100 80 GB at EUR 1.7917 and RTX 6000 Ada 48 GB at EUR 1.1919, each an hourly rate before the vCPU, RAM and SSD of the instance, which are billed separately. The prices are in EUR; no conversion to USD is made here.
- evidence:
  - [1] 2026-11-03: the A100 80 GB is EUR 1.7917 an hour or EUR 1,290.00 a month on the vendor page read on 2026-11-03 | capture: sha256:dd6fb2ea130dc506c11fd1a9a7ab02a1cb247b828a7e5212daae559bbd84e8af | quote: | NVIDIA A100 (80 GB) | 80 GB | €1.7917 | €1,290.00 |
  - [1] 2026-11-03: the RTX A4000 16 GB is EUR 0.2069 an hour | capture: sha256:dd6fb2ea130dc506c11fd1a9a7ab02a1cb247b828a7e5212daae559bbd84e8af | quote: | NVIDIA RTX A4000 | 16 GB | €0.2069 | €149.00 |
  - [1] 2026-11-03: the A100 40 GB is EUR 0.9583 an hour; the table lists five cards and no H100, L40S, RTX 4090 or L4 | capture: sha256:dd6fb2ea130dc506c11fd1a9a7ab02a1cb247b828a7e5212daae559bbd84e8af | quote: | NVIDIA A100 (40 GB) | 40 GB | €0.9583 | €690.00 |
  - [1] 2026-11-03: the RTX 6000 Ada 48 GB is EUR 1.1919 an hour | capture: sha256:dd6fb2ea130dc506c11fd1a9a7ab02a1cb247b828a7e5212daae559bbd84e8af | quote: | NVIDIA RTX 6000 Ada | 48 GB | €1.1919 | €858.19 |
  - [1] 2026-11-03: new accounts get a EUR 200 credit within 60 days | capture: sha256:dd6fb2ea130dc506c11fd1a9a7ab02a1cb247b828a7e5212daae559bbd84e8af | quote: New accounts receive a €200 starting credit within the first 60 days
  - [1] 2026-11-03: the credit is for new accounts and exclusively for businesses | capture: sha256:dd6fb2ea130dc506c11fd1a9a7ab02a1cb247b828a7e5212daae559bbd84e8af | quote: This promotional offer applies to new accounts only. Available exclusively to businesses.
  - [1] 2026-11-03: hourly billing with no minimum term and no set-up fee | capture: sha256:dd6fb2ea130dc506c11fd1a9a7ab02a1cb247b828a7e5212daae559bbd84e8af | quote: There is no minimum contract term and no set-up fee.
  - [2] 2026-11-03: the registration form's first field is an email address, followed by a password with complexity rules | capture: sha256:091638c1558d92728b7a8faa713067d42da88d7f8ca9c9b960eb7cb354c17139 | quote: Email address
  - [2] 2026-11-03: the registration form offers Sign up with Google, and with GitHub | capture: sha256:091638c1558d92728b7a8faa713067d42da88d7f8ca9c9b960eb7cb354c17139 | quote: Sign up with Google
  - [2] 2026-11-03: the registration form carries a Friendly Captcha anti-spam widget | capture: sha256:091638c1558d92728b7a8faa713067d42da88d7f8ca9c9b960eb7cb354c17139 | quote: Friendly Captcha
  - [3] 2026-11-03: the aggregator lists a business-customers-only limitation for this host | capture: sha256:5b39de661df7ec844c86dc609e2c611ee82146cf9525ae35ce914550d0c8113d | quote: Limited to business customers only
- sources:
  - [1] https://www.centron.de/en/pricing/gpu
  - [2] https://cloud.centron.de/register/
  - [3] https://computeprices.com/providers/centron
