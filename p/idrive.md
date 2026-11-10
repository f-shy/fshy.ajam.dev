# IDrive e2

> idrive.com | Storage; 2 records: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/idrive/ | JSON https://fshy.ajam.dev/api/v1/entity/idrive.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## IDrive e2

- `storage/idrive-e2` | trial-only | evidence documented | binding volume-quota | category S3-compatible object storage | tier pay-as-you-go
- needs card no, phone no, ID no, institution no | verified 2026-11-01T23:50:14.298Z (live) | stale on 2026-12-02
- url https://www.idrive.com/s3-storage-e2/pricing
- price USD 6 per TB per month pay-as-you-go, 1 TB minimum; yearly 10 TB plan USD 595.00 a year (USD 4.96 per TB-month, derived: 595.00 / 10 / 12), half price in the first year | parsed USD 4.96/TB-mo
- free tier: Pay-as-you-go at USD 6 per month per TB 'Try with 10GB Free'; the sign-up page calls it a free trial ('Start your Free Trial with 10 GB') and the pages read do not state its length | unit: GB | metered on: stored-bytes | read on: 2026-10-30 | source: [1] | note: The create-account form asks for an email address and a password, with Google or Microsoft sign-in as the alternative, and shows no card field. The length of the trial is not stated on the pricing page or on the sign-up page.
- per-object cap: Maximum object size 50 TB; maximum object size per PUT operation 50 TB; parts of 5 MB to 5 GB, 10,000 parts per upload | source: [2] | note: the page does not say whether TB is decimal or binary, so bytes is left null; the minimum object size is 0 B.
- retention: No minimum storage duration: 'IDrive e2 does not impose a minimum storage duration on uploaded objects nor charge users for deleting the objects' | source: [1] | note: no expiry of stored objects is stated on a paid plan; on the free trial an empty region is removed after 30 days.
- egress: Free while monthly egress is at most 3x the active storage volume; beyond it USD 0.01/GB/month | metered: yes | free allowance: 3x the active storage volume per monthly billing cycle | price per TB: USD 0.01 per GB beyond the 3x allowance | source: [3]
- identity: email | detail: The create-account form asks for an email address and a password, with Google or Microsoft sign-in as the alternative, and carries no card field; a reCAPTCHA challenge guards submission. Card details are entered in the billing flow of a paid plan, which is paid by credit or debit card.
- interface: s3-compatible
- limits:
  - volume-quota (binding): egress free up to 3x the active storage volume per month; beyond it USD 0.01/GB [3]
  - volume-quota (binding): 10 GB of storage on the free trial [1]
  - per-object-cap: 50 TB per object, 50 TB per PUT operation [2]
- limits note: Pay-as-you-go bills a 1 TB minimum: storage under 1 TB is charged USD 6 for the month. No minimum object size (0 B) and no minimum storage duration; no charge for deletion or API calls. Storage above a yearly plan's quota is billed at USD 0.006/GB/month.
- binding note: the free path ends at the 10 GB trial; on a paid plan the 3x-of-stored egress allowance is the ceiling that meters
- interface detail: S3-compatible API; API calls carry no charge
- tooling: any S3 SDK or S3 client, rclone's s3 backend among them
- composes with: An S3 origin with no request fees and egress free up to 3x stored bytes; a CDN in front keeps reads inside that allowance.
- reliability: no throttle, suspension or data-loss event is stated on the pages read; a trial region left empty for 30 days is removed
- notes: S3-compatible object storage: confirmed. The only free path is the 10 GB trial; recurring use is paid. derived: USD 595.00 a year / 10 TB / 12 months = USD 4.96 per TB-month.
- evidence note: every value is quoted from a first-party IDrive page read on 2026-10-30; the trial length is behind a sign-up and the read path is unprobed.
- evidence:
  - [1] 2026-10-30: pay-as-you-go storage costs USD 6 per TB per month | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: $6 per month, per TB
  - [1] 2026-10-30: the pay-as-you-go plan offers 10 GB to try free | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: (Try with 10GB Free)
  - [1] 2026-10-30: storage under 1 TB is billed as a full 1 TB at USD 6 | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: IDrive® e2 charges a minimum storage fee of $6/TB. The minimum charge is per TB; even if your total storage is less than 1 TB, you will be charged for the entire 1 TB.
  - [1] 2026-10-30: the yearly plan for 10 TB is USD 595.00 a year | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: $595.00/year
  - [1] 2026-10-30: there is no minimum storage duration and no delete charge | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: No, unlike most competitors in the market, IDrive® e2 does not impose a minimum storage duration on uploaded objects nor charge users for deleting the objects.
  - [1] 2026-10-30: egress up to 3x the active storage volume is free | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: Free egress policy Download less than or equal to 3X your active storage volume for free!
  - [1] 2026-10-30: egress beyond the free allowance costs USD 0.01/GB | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: Free Egress Policy: Charges apply at $0.01/GB/month beyond free limits.
  - [1] 2026-10-30: API calls carry no charge | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: IDrive® e2 does not impose any additional charges for your API calls.
  - [1] 2026-10-30: IDrive e2 is S3-compatible storage | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: S3 Compatible Storage Integrations
  - [3] 2026-10-30: the free egress rule is 3x the storage volume per monthly billing cycle | capture: sha256:2c638643d0e72bdded9fa8f27cbfe4ef2e156a1762cf13ab419853b490b670c7 | quote: If you store 100 TB with IDrive® e2 and download 300 TB or less within a monthly billing cycle, then your storage use case is a good fit for our policy.
  - [3] 2026-10-30: there is no lock-in period and no minimum upload size | capture: sha256:2c638643d0e72bdded9fa8f27cbfe4ef2e156a1762cf13ab419853b490b670c7 | quote: IDrive® e2 does not implement any data lock-in period or limit the minimum file upload size.
  - [2] 2026-10-30: the maximum object size is 50 TB | capture: sha256:2d9054131ad0cf522b5430e5e8be6f594355f78a84e60cc3b1b6fc5213070252 | quote: | Maximum object size | 50 TB |
  - [2] 2026-10-30: the minimum object size is 0 B | capture: sha256:2d9054131ad0cf522b5430e5e8be6f594355f78a84e60cc3b1b6fc5213070252 | quote: | Minimum object size | 0 B |
  - [2] 2026-10-30: paid plans are paid by credit or debit card | capture: sha256:2d9054131ad0cf522b5430e5e8be6f594355f78a84e60cc3b1b6fc5213070252 | quote: IDrive® e2 allows you to process payments via credit and debit cards.
  - [2] 2026-10-30: a free-trial region with no data for more than 30 days is removed | capture: sha256:2d9054131ad0cf522b5430e5e8be6f594355f78a84e60cc3b1b6fc5213070252 | quote: Free trial users can enable as many regions as they want. However, if a region remains inactive and no data is stored in it for more than 30 days, the region will be removed from the account.
  - [4] 2026-10-30: the 10 GB is a free trial | capture: sha256:cfac31af9a192f671dec4a506eb01b541674a0c5ac9f5f902ae05ec1f63b177a | quote: Start your Free Trial with 10 GB
  - [4] 2026-10-30: the sign-up form asks for an email address and a password | capture: sha256:cfac31af9a192f671dec4a506eb01b541674a0c5ac9f5f902ae05ec1f63b177a | quote: Email address*
  - [4] 2026-11-01: the create-account form asks for an email address and a password and shows no card field | capture: sha256:5dd8781bbf8f135786c112318db8e2c826fa31a85923b0b0c4c90af6a0d5fd22 | quote: # Create account Email address* Password*
  - [4] 2026-11-01: registration asks for an email address and a password, with no card field on the form | capture: sha256:212d57867069fcaecc21106ab2aa7bfb69ebf8bce186b4b1c26d650d145c8536 | quote: # Create account Email address\* Password\*
  - [3] 2026-11-01: egress up to 3x the stored volume per monthly billing cycle is free | capture: sha256:2c638643d0e72bdded9fa8f27cbfe4ef2e156a1762cf13ab419853b490b670c7 | quote: If you store 100 TB with IDrive® e2 and download 300 TB or less within a monthly billing cycle, then your storage use case is a good fit for our policy.
  - [2] 2026-11-01: card details are entered when subscribing to a paid plan, not at account creation | capture: sha256:2d9054131ad0cf522b5430e5e8be6f594355f78a84e60cc3b1b6fc5213070252 | quote: 3. Enter your card details under Credit card information.
  - [4] 2026-11-01: Google or Microsoft sign-in is offered beside the email and password fields | capture: sha256:212d57867069fcaecc21106ab2aa7bfb69ebf8bce186b4b1c26d650d145c8536 | quote: Continue with Microsoft
  - [4] 2026-11-01: account creation passes a reCAPTCHA challenge | capture: sha256:212d57867069fcaecc21106ab2aa7bfb69ebf8bce186b4b1c26d650d145c8536 | quote: Recaptcha requires verification.
  - [2] 2026-11-01: an empty trial region is removed from the account after 30 days | capture: sha256:2d9054131ad0cf522b5430e5e8be6f594355f78a84e60cc3b1b6fc5213070252 | quote: if a region remains inactive and no data is stored in it for more than 30 days, the region will be removed from the account
  - [1] 2026-11-01: the pay-as-you-go plan still gives 10 GB to try free at USD 6 per TB | capture: sha256:50e1a3b694be3250ae301256e7d0bb2c5811e7d95d3622f2f6e712868d636b27 | quote: Pay-as-you-go $6 per month, per TB (Try with 10GB Free)
- sources:
  - [1] https://www.idrive.com/s3-storage-e2/pricing
  - [2] https://www.idrive.com/s3-storage-e2/faq-account-management
  - [3] https://www.idrive.com/s3-storage-e2/faq-pricing
  - [4] https://console.idrivee2.com/signup

## idrive personal 20 tb

- `storage/idrive-personal-20-tb` | paid-only | evidence documented | binding volume-quota | category rejected-provider
- identity a placeholder: card and phone unknown | verified 2026-11-03T15:04:31.558Z (live) | stale on 2026-12-04
- url https://www.idrive.com/pricing
- free tier: Paid plan: USD 29.99 per month for 20 TB on monthly billing, USD 1.50 per TB per month; no free allowance on this plan | unit: none | metered on: none | read on: 2026-10-21 | source: [1]
- per-object cap: not recorded | source: [1] | note: not applicable
- retention: not recorded | source: [1]
- egress: not recorded | metered: no
- identity: email
- interface: cli
- limits:
  - volume-quota (binding): 20 TB plan storage; overuse charge USD 0.25/GB/month beyond it [1]
- binding note: the price of the storage tier is the constraint: USD 29.99 per month for 20 TB, with an overuse charge beyond it
- interface detail: not documented
- tooling: vendor desktop application with a command line interface on Linux; a support reply reported on the rclone tracker says the Personal account does not support WebDAV
- composes with: not recorded
- reliability: Paid backup plan with an overuse charge of USD 0.25/GB/month beyond the plan storage
- notes: the same as reliability
- evidence note: the 2026-11-03 evidence rows read the vendor pages https://www.idrive.com/pricing (20 TB at $29.99 per month, overuse charge) and https://www.idrive.com/faq_linux (command line interface); the WebDAV statement rests on a support reply reported in an rclone tracker issue, and the sign-up fields were not read
- extras:
  - dead_end.failure_class: quota
  - dead_end.why: $29.99/mo for 20 TB = $1.50/TB/mo, the cheapest headline in several 2026 price roundups — but it is backup software, not a storage endpoint: no rclone backend ('I'm afraid we don't have a…
  - dead_end.first_recorded: 2026-10-21
- evidence:
  - [1] 2026-10-21: $29.99/mo for 20 TB = $1.50/TB/mo, the cheapest headline in several 2026 price roundups — but it is backup software, not a storage endpoint: no rclone backend 'I'm afraid we don't have a ba
  - [1] 2026-11-03: the 20 TB Personal plan costs USD 29.99 per month on monthly billing | capture: sha256:c308b8f6d8b861b0649c2f927fbac35dd6fc872044d17eb13052c9ca52ad62d9 | quote: 20 TB $29.99 / month
  - [1] 2026-11-03: overuse beyond the plan storage is charged at USD 0.25/GB/month on the Personal plan | capture: sha256:c308b8f6d8b861b0649c2f927fbac35dd6fc872044d17eb13052c9ca52ad62d9 | quote: If you exceed account storage limit, there may be an overuse charge of $0.25/GB/month for Personal plan and $0.50/GB/month for the Team and Business plans.
  - [2] 2026-11-03: a user reports IDrive support saying the Personal account does not support WebDAV | capture: sha256:881ce6a28423f5c522314d959018239beabc424c5221f17f98a5d0db3aa83129 | quote: I just cotnacted iDrive support. The Personal account does not support webDAV.
  - [3] 2026-11-03: the vendor application has a CLI | capture: sha256:0dc7d150df7a8b9a666d52d1e9eba869ec83b3fdb4719bb234dcac39e2a3c48a | quote: Yes, you can use the command line interface (CLI) with the desktop application.
  - [1] 2026-11-03: the 20 TB Personal plan is a paid plan at USD 29.99 per month | capture: sha256:c308b8f6d8b861b0649c2f927fbac35dd6fc872044d17eb13052c9ca52ad62d9 | quote: 20 TB $29.99 / month
  - [1] 2026-11-03: the plan is priced per storage tier | capture: sha256:c308b8f6d8b861b0649c2f927fbac35dd6fc872044d17eb13052c9ca52ad62d9 | quote: 20 TB $29.99 / month
- sources:
  - [1] https://www.idrive.com/pricing
  - [2] https://github.com/rclone/rclone/issues/5229
  - [3] https://www.idrive.com/faq_linux
