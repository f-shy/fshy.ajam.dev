# EasyFileUpload

> easyfileupload.io | Debrid; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/easyfileupload/ | JSON https://fshy.ajam.dev/api/v1/entity/easyfileupload.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EasyFileUpload

- `debrid/easyfileupload` | qualifies-with-caveat | evidence documented | binding retention-clamped | category file transfer service (free, premium, assured plan) | tier assured
- needs card no, phone no, ID no, institution no | verified 2026-11-03T07:37:12.225Z (live) | stale on 2026-12-04
- url https://easyfileupload.io/en/pricing
- price USD 7 per month for 500 GB of live files (Assured) | parsed USD 14/TB-mo
- free tier: unverified: the free per-file size is not printed; links last from 1 hour up to 7 days on the free plan; no signup. | unit: none | metered on: unstated | read on: 2026-11-03 | source: [1] | note: The homepage says 'Upload any file or folders - no size limit'.
- per-object cap: Keep files live up to 30 days instead of 7, with no per-file size limit. | source: [1] | note: Premium has no per-file size limit; the free plan's cap is not printed.
- retention: Links expire from 1 hour up to 7 days on the free plan, or 30 days on Premium. | days: 7 | source: [2]
- egress: Assured: 500 GB of live files and 30-day links with no per-transfer cap. | metered: no | free allowance: unstated | source: [1]
- identity: anonymous | detail: The homepage says 'Start without signing up' and 'No account, no email to verify.'; payment details for Premium were not read.
- interface: rest, cli
- limits:
  - retention-clamped (binding): 7 days free, 30 days Premium and Assured [1]
  - volume-quota: 500 GB of live files on Assured [1]
- binding note: Free links last at most 7 days.
- interface detail: Premium adds API access for scripted and CLI uploads.
- tooling: API and CLI uploads on Premium; browser on the free plan.
- composes with: The Assured plan at $7 holds 500 GB of live files for 30 days, the cheapest paid tier of this slice with a stated size.
- reliability: The homepage's lede line 'no size limit' is not repeated with a number on the pricing page.
- evidence note: Pricing page and homepage read on 2026-11-03; the free per-file cap is unverified.
- extras:
  - plans: Free; Assured $7; Premium $29/month
- evidence:
  - [1] 2026-11-03: Assured costs $7 for 500 GB of live files | capture: sha256:ad46ec3ca989447f813b245c7ccaa562d1bd80dc0386bdc3375b1ed47cc77a08 | quote: Hitting WeTransfer's monthly limit? Assured is $7 for 500 GB of live files and 30-day links, with no per-transfer cap, no ads, and no AI training on your files.
  - [1] 2026-11-03: Premium costs $29 a month | capture: sha256:ad46ec3ca989447f813b245c7ccaa562d1bd80dc0386bdc3375b1ed47cc77a08 | quote: Premium is $29/month.
  - [1] 2026-11-03: free links last 7 days; Premium has no per-file limit | capture: sha256:ad46ec3ca989447f813b245c7ccaa562d1bd80dc0386bdc3375b1ed47cc77a08 | quote: Keep files live up to 30 days instead of 7, with no per-file size limit.
- sources:
  - [1] https://easyfileupload.io/en/pricing
  - [2] https://easyfileupload.io/
