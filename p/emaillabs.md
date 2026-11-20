# EmailLabs

> emaillabs.io | Email; 1 record: free tier, limits, identity cost and evidence.

HTML https://fshy.ajam.dev/p/emaillabs/ | JSON https://fshy.ajam.dev/api/v1/entity/emaillabs.json | how to read a record: https://fshy.ajam.dev/llms-full.txt

## EmailLabs

- `email/emaillabs` | qualifies-with-caveat | evidence documented | binding request-rate | category transactional sender and SMTP relay | tier Startup
- needs card no, phone yes, ID no, institution no | verified 2026-11-19T01:47:12.731Z (live) | stale on 2026-12-20
- url https://emaillabs.io/en/plan-comparison/
- free tier: Startup plan: up to 9 000 emails per month, 300 emails per day, 0 EUR per month, on a shared IP with 1 day of log retention | unit: requests | metered on: request-count | read on: 2026-11-19 | source: [1] | note: On the Startup plan the sender can only send the messages the plan offers, so sending stops at the plan volume instead of incurring an overage charge. Unused messages do not transfer to the next billing month. The Email RESTful API, SMTP relay, email templates and basic analytics are included. Mail goes out from a shared IP. The card requirement for the Startup plan is not stated on the public pricing pages.
- per-object cap: 15 MB maximum size of an email with an attachment; oversized mail is rejected | source: [2] | note: Oversized mail is rejected with SMTP error 552 or API error 413. The figure is a message weight in MB, so it is not a single binary object cap.
- retention: 1 day of log retention on the Startup plan | days: 1 | source: [1] | note: The plan comparison lists 1 day for Startup, 7 days for Essential and 15 days for Pro and Enterprise.
- egress: not applicable: an outbound sender | metered: no | source: [3]
- identity: any-phone | detail: Registration asks for an email address, a login and a password of at least 12 characters with an uppercase letter, a lowercase letter, a number and a special character, and acceptance of the terms. The address must be activated by a link in a message. Phone number verification by SMS code is a mandatory step and also activates two factor authentication. A three step survey then asks for company details including Tax ID and website address, the services of interest, and the size and source of the contact database. The account is then sent for verification by the EmailLabs team. Card requirement for the free Startup plan is unverified: not stated on the public pricing pages.
- interface: rest
- limits:
  - request-rate (binding): 300 emails per day and 9 000 emails per month on the Startup plan; mail beyond the plan volume is not delivered [1]
  - per-object-cap: 15 MB maximum email size with an attachment; oversized mail is rejected [2]
  - retention-clamped: 1 day of log retention on the Startup plan [1]
  - write-gated: the account is verified by the EmailLabs team at registration; a sandbox domain is assigned for testing, and production sending needs a plan and an authorized sending domain with SPF, DKIM and DMARC records [4]
- limits note: counts of messages and a message weight, not shaped rates; the daily and monthly ceilings are the volume counts that bind on the free plan.
- binding note: the 300 per day and 9 000 per month ceiling on Startup is the first hard ceiling at sustained sending scale, since mail beyond the plan volume is not delivered; a one time team verification and domain authorization gate production sending before that ceiling applies.
- interface detail: The Email RESTful API follows JSONAPI and is described by an OpenAPI 3.0.2 file. Cloud SMTP relay is at smtp-relay.emaillabs.net.pl on ports 587, 2525 and 25 with STARTTLS, or 465 with SSL. The interface vocabulary has no SMTP term.
- tooling: any SMTP client, or the REST API using the Application-Key and Authorization keys generated in the panel under Account, Settings, API
- composes with: a 300 per day relay with a 9 000 per month ceiling and a 15 MB message weight cap; the monthly volume does not carry over and the 1 day log retention needs prompt failure checking
- reliability: Startup mail stops at the plan volume rather than incurring an overage charge, unused messages do not carry to the next month, oversized mail is rejected, and 1 day of log retention leaves little time to inspect failures
- notes: Card requirement for the free Startup plan is not stated on the public pricing pages; No probe was run, so delivery is not verified. The price comparison page and the current pricing page carry the same Startup figures.
- evidence note: all values come from first party pricing, plan comparison, documentation and onboarding pages captured and quoted on 2026-11-19; no probe was run, so delivery and the account gate were not measured
- evidence:
  - [1] 2026-11-19: the Startup plan has a daily sending limit of 300, while paid plans have none | capture: sha256:ae028c3e97e0c75590de288dc607da1ce378cd39c8bf1befab1c2d2de14d26c1 | quote: | Daily sending limits | 300 | none | none | none |
  - [1] 2026-11-19: the Startup plan has a monthly sending limit of 9 000 emails | capture: sha256:ae028c3e97e0c75590de288dc607da1ce378cd39c8bf1befab1c2d2de14d26c1 | quote: | Monthly sending limit | 9 000 | 30 000/100 000 | none | none |
  - [1] 2026-11-19: the Startup plan monthly fee is 0 EUR | capture: sha256:ae028c3e97e0c75590de288dc607da1ce378cd39c8bf1befab1c2d2de14d26c1 | quote: | Monthly fee | ** 0 EUR** | ** 29-68 EUR** | ** 69-440 EUR** | ** Contact us** |
  - [1] 2026-11-19: the Startup plan keeps logs for 1 day, against 7 on Essential and 15 on Pro and Enterprise | capture: sha256:ae028c3e97e0c75590de288dc607da1ce378cd39c8bf1befab1c2d2de14d26c1 | quote: | Logs retention | 1 day | 7 days | 15 days | 15 days |
  - [5] 2026-11-19: sending on Startup stops at the plan volume instead of incurring an overage charge | capture: sha256:1960aafd896ba15aef686f0507649623993559f90b98e273321280585f730ab9 | quote: For the Startup, and Essential Plan, you can only send messages that they offer.
  - [5] 2026-11-19: unused messages do not carry over to the next month | capture: sha256:1960aafd896ba15aef686f0507649623993559f90b98e273321280585f730ab9 | quote: If you do not use all messages in your plan, they will not transfer to the next billing month.
  - [5] 2026-11-19: the separate sales approved trial needs no card | capture: sha256:1960aafd896ba15aef686f0507649623993559f90b98e273321280585f730ab9 | quote: You can enjoy a free trial period without the need to provide your credit card details
  - [5] 2026-11-19:  | capture: sha256:1960aafd896ba15aef686f0507649623993559f90b98e273321280585f730ab9 | quote: During the trial period, you should use test addresses to send emails, you cannot perform sends in a production environment.
  - [4] 2026-11-19: registration asks for email, login, a strong password and acceptance of the terms | capture: sha256:2f50d17723adae52b6c066155f243567e43c582677f20ee9fa988af1c794820e
  - [4] 2026-11-19: phone number verification by SMS code is mandatory at registration | capture: sha256:2f50d17723adae52b6c066155f243567e43c582677f20ee9fa988af1c794820e | quote: Phone number verification: A mandatory registration step. Enter the code from the SMS message.
  - [4] 2026-11-19: registration asks for company details including Tax ID and website address | capture: sha256:2f50d17723adae52b6c066155f243567e43c582677f20ee9fa988af1c794820e | quote: Survey (3 steps): Fill in your company details (including Tax ID and website address)
  - [4] 2026-11-19: the account is verified by the EmailLabs team before sending is unlocked | capture: sha256:2f50d17723adae52b6c066155f243567e43c582677f20ee9fa988af1c794820e | quote: Confirmation screen: The account is sent for verification by the EmailLabs team.
  - [4] 2026-11-19: production sending needs an authorized domain with SPF, DKIM and DMARC | capture: sha256:2f50d17723adae52b6c066155f243567e43c582677f20ee9fa988af1c794820e | quote: Authorize the sending domain: Add SPF, DKIM, and DMARC records to your DNS settings.
  - [4] 2026-11-19: a sandbox domain allows testing over API or SMTP before the sender has DNS records | capture: sha256:2f50d17723adae52b6c066155f243567e43c582677f20ee9fa988af1c794820e | quote: It allows for immediate testing of the integration via API or SMTP without the need to configure your own DNS records.
  - [6] 2026-11-19: the REST API uses two keys for authentication | capture: sha256:8dd407d5652183ed20a0a32dacfbac7536e407e55e67dac312880fc80d92bcc0 | quote: The EmailLabs API requires authentication using two keys:
  - [7] 2026-11-19: the SMTP relay host is smtp-relay.emaillabs.net.pl | capture: sha256:e3dfc431a054368abbc4068b3dbf34b9e80e1186c7719cffafa56e4e8ee278cd | quote: Server name: smtp-relay.emaillabs.net.pl
  - [7] 2026-11-19: the SMTP relay accepts STARTTLS on ports 587, 2525 and 25 | capture: sha256:e3dfc431a054368abbc4068b3dbf34b9e80e1186c7719cffafa56e4e8ee278cd | quote: option 1: TLS/STARTTLS; ports: 587, 2525, 25
  - [2] 2026-11-19: the platform caps an email with an attachment at 15 MB | capture: sha256:71ebb2a18af8acb2c5a9ccf221e1032d30973a1cbd714b6e7f2d61b050b25dd6 | quote: From May 1st this year, the maximum size of an email with an attachment on our platform will be limited to 15MB.
  - [2] 2026-11-19: mail beyond the size cap is rejected rather than queued | capture: sha256:71ebb2a18af8acb2c5a9ccf221e1032d30973a1cbd714b6e7f2d61b050b25dd6 | quote: Emails exceeding the 15MB limit will be rejected
- sources:
  - [1] https://emaillabs.io/en/plan-comparison/
  - [2] https://emaillabs.io/en/email-size-change-with-attachment-to-15mb/
  - [3] https://emaillabs.io/en/pricing-v2/
  - [4] https://docs.emaillabs.io/en/emaillabs-panel/first-steps.md
  - [5] https://emaillabs.io/en/pricing
  - [6] https://docs.emaillabs.io/en/integrations/api.md
  - [7] https://docs.emaillabs.io/en/integrations/smtp.md
