# SMTP.com

> smtp.com | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/smtp/ | JSON https://fshy.ajam.dev/api/v1/entity/smtp.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## SMTP.com

- `email/smtp-com` | paid-only | evidence documented | binding write-gated | category transactional sender and SMTP relay with managed deliverability
- needs card yes, phone no, ID no, institution no | verified 2026-11-19T00:19:24.889Z (live) | stale on 2026-12-20
- url https://www.smtp.com/pricing/
- free tier: no free plan and no free trial; plans start at USD 25/month for 50,000 emails/month on a shared IP (Essential), overages billed per email | unit: none | metered on: none | read on: 2026-11-19 | source: [1] | note: The signup page offers only paid plans; there is no self-serve sandbox. Third-party reviewers report a 30-day, 50,000-email trial arranged through a reseller, but the first-party blog states there is no free trial.
- per-object cap: not applicable: an outbound sender | source: [2]
- retention: up to 90 days of sending data retention on every plan; detailed reporting statistics are only available for the most recent 31 days while the dashboard shows high-level volumes for up to 1 year | source: [3] | note: The 90-day figure is the marketing claim on the email API page; the knowledge-base reporting article gives the 31-day window for detailed statistics and 1 year only for high-level dashboard numbers.
- egress: not applicable: an outbound sender | metered: no | source: [4]
- identity: card | detail: The registration form at registration.smtp.com asks for First Name, Last Name, Email, Confirm Email, Website, Company Name and Phone, then states: "On the next page, you will confirm your plan and enter your payment information." A paid plan must be bought to send, so a payment method is required.
- interface: rest
- limits:
  - write-gated (binding): no free trial: a paid plan must be purchased before the account can send [5]
  - volume-quota: 50,000 emails/month on the Essential plan at USD 25/month, with usage fees charged per email above the allowance [1]
  - retention-clamped: detailed statistics only for the most recent 31 days; up to 90 days of sending data retention stated [3]
- binding note: no message can be sent before a plan is bought, so the write gate binds before the 50,000/month volume cap or the 31-day reporting window; there is no free or trial sending path at all.
- interface detail: the SMTP.com API v4 is a REST, JSON-formatted API at api.smtp.com/v4; the relay is also reachable over SMTP with any SMTP client, which has no token in the interface vocabulary
- tooling: any SMTP client against the relay; the SMTP.com v4 REST API authenticated with an API key
- composes with: a paid relay with a 50,000-email entry allowance and expert-managed onboarding, so it composes with an application that buys a plan before it sends; the monthly volume cap and the 31-day reporting window bind inside that paid lane.
- reliability: detailed reporting statistics cover only the most recent 31 days even though a 1-year high-level dashboard is shown; there is no self-serve sandbox, and guided onboarding with a deliverability specialist replaces free testing.
- notes: A managed-deliverability sender with no free or trial lane: the first-party blog says the absence of a free trial is deliberate. Some resellers advertise a 30-day 50,000-email trial that is not offered on the first-party pricing or signup pages. The SMTP relay has no token in the interface vocabulary, so only REST is recorded and the relay is named in interface_detail (open_question filed).
- evidence note: every value comes from first-party SMTP.com pages captured and quoted on 2026-11-19; the send path was not probed, so the rung stays documented rather than measured.
- evidence:
  - [1] 2026-11-19: the API v4 is a REST, JSON-formatted programmable interface | capture: sha256:e1d7c0724f63348602e37e7f627ad492d6c489e8030fb558fd705ca96f1c6311 | quote: The SMTP.com API v4 is a RESTful (but not HATEOAS) JSON formatted API.
  - [1] 2026-11-19: the entry plan is USD 25 per month for 50,000 emails per month | capture: sha256:e1d7c0724f63348602e37e7f627ad492d6c489e8030fb558fd705ca96f1c6311 | quote: Get started with 50,000 emails for $25/ mo.
  - [5] 2026-11-19: there is no free trial; guided onboarding and a specialist replace self-serve testing | capture: sha256:d26390dad7579f226fdd704114b81d7c8f1c8eeaa26fce810624692605a482bd | quote: There is no free trial, and that is deliberate. Guided onboarding replaces it, matching new customers with a specialist who helps migrate lists and configure authentication before launch.
  - [2] 2026-11-19: sending data is retained for up to 90 days, as a vendor claim | capture: sha256:c6f384532c4549a0a872d0e198e946df2cedbc4d53759c1bd337acbe2c354752 | quote: Up to 90 days data retention.
  - [3] 2026-11-19: detailed reporting statistics are limited to 31 days; high-level dashboard volumes reach 1 year | capture: sha256:8f7cef5b7818c62ea98bb4ce9328b0c1c688fa480f3af27a529ae3cfdae92ce1 | quote: Note: While the dashboard displays high-level numbers and volumes for up to 1 year, detailed statistics are only available for the most recent 31 days.
  - [6] 2026-11-19: the registration form asks for personal and company identity fields including First Name | capture: sha256:935f6a00a178599580aa2831c8ad3332583b3433e4dadcfe379a9a18fbe62a5d | quote: First Name
  - [6] 2026-11-19: signup requires entering payment information for a paid plan | capture: sha256:935f6a00a178599580aa2831c8ad3332583b3433e4dadcfe379a9a18fbe62a5d | quote: On the next page, you will confirm your plan and enter your payment information.
  - [7] 2026-11-19: the monthly allowance is a paid-plan volume cap with per-email overage charges and no rollover | capture: sha256:6c2a847800130b41382e97528e25800c2e60394d3ea4df2bd8d29de7900bc6ac | quote: Your payment plan may include a monthly allowance of free emails, or contacts. In the event that you have exceeded your rate plan’s allotted allowance you will be automatically charged usage fees for each email or contact in excess of your monthly allowance. Unused allowances are not transferable from month to month.
- sources:
  - [1] https://www.smtp.com/resources/api-documentation
  - [2] https://www.smtp.com/email-api
  - [3] https://knowledge.smtp.com/s/article/Reporting-and-Statistics
  - [4] https://www.smtp.com/pricing/
  - [5] https://www.smtp.com/blog/transactional-email/the-10-best-transactional-email-services
  - [6] https://registration.smtp.com/?plan=50000
  - [7] https://www.smtp.com/policies/terms-and-conditions
